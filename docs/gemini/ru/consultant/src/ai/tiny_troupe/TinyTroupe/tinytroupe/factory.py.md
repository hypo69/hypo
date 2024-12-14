# Анализ кода модуля `factory.py`

**Качество кода**
   - Соответствие требованиям по оформлению кода: 6/10
   -  Плюсы:
        - Использование `chevron` для шаблонизации.
        -  Разделение ответственности между классами `TinyFactory` и `TinyPersonFactory`.
        -  Использование логгера `logger` для отладки.
        - Применение декоратора `@transactional` для кэширования.
   -  Минусы:
        - Не везде используется reStructuredText для комментариев.
        - Отсутствие обработки ошибок при чтении файлов.
        - Использование `json.dumps` вместо `j_dumps`.
        -  Не полное соответствие PEP8 (например, длинные строки).
        -  Не используется `j_loads_ns` для загрузки JSON.
        -  Избыточное использование `try-except`.

**Рекомендации по улучшению**

1. **Форматирование документации:**
   - Заменить все комментарии на reStructuredText (RST) docstrings.
   - Добавить подробное описание для каждого класса, метода и функции.
   - Описать параметры и возвращаемые значения в docstrings.
2.  **Использование `j_loads`:**
    -   Заменить стандартное `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
3.  **Улучшение обработки ошибок:**
    -   Убрать избыточные `try-except` блоки, использовать `logger.error` для логирования ошибок.
4.  **Улучшение именования:**
    -   Именовать переменные и методы согласно PEP8.
5.  **Улучшение логирования:**
    -   Добавить более детальное логирование.
6.  **Упрощение кода**:
    -   Удалить лишние строки кода и упростить логику.
7.  **Улучшение производительности:**
    -   Избегать ненужных копирований объектов.

**Оптимизированный код**

```python
"""
Модуль для создания фабрик TinyPerson.
=========================================================================================

Этот модуль содержит классы :class:`TinyFactory` и :class:`TinyPersonFactory`,
которые используются для создания и управления экземплярами агентов TinyPerson.
Модуль обеспечивает механизмы кэширования и транзакций для эффективного управления
созданием агентов.

Пример использования
--------------------

Пример создания и использования TinyPersonFactory:

.. code-block:: python

    from tinytroupe.factory import TinyPersonFactory

    factory = TinyPersonFactory(context_text="some context")
    person = factory.generate_person()
"""
import os
import logging
import copy

from src.utils.jjson import j_loads_ns # импортируем j_loads_ns
import chevron

from tinytroupe import openai_utils
from tinytroupe.agent import TinyPerson
import tinytroupe.utils as utils
from tinytroupe.control import transactional
from src.logger.logger import logger # импортируем logger

class TinyFactory:
    """
    Базовый класс для различных типов фабрик.
    
    Этот класс обеспечивает основу для расширения системы, особенно в отношении
    кэширования транзакций.
    """
    all_factories = {}  #: dict: Словарь всех созданных фабрик.
    
    def __init__(self, simulation_id: str = None) -> None:
        """
        Инициализирует экземпляр TinyFactory.

        :param simulation_id: Идентификатор симуляции.
        :type simulation_id: str, optional
        """
        self.name = f"Factory {utils.fresh_id()}"
        self.simulation_id = simulation_id
        TinyFactory.add_factory(self)

    def __repr__(self):
        """
        Возвращает строковое представление объекта TinyFactory.
        """
        return f"TinyFactory(name='{self.name}')"

    @staticmethod
    def set_simulation_for_free_factories(simulation):
        """
        Устанавливает симуляцию для свободных фабрик.

        Это позволяет свободным окружениям быть захваченными конкретными
        областями симуляции, если это необходимо.

        :param simulation: Объект симуляции.
        """
        for factory in TinyFactory.all_factories.values():
            if factory.simulation_id is None:
                simulation.add_factory(factory)

    @staticmethod
    def add_factory(factory):
        """
        Добавляет фабрику в список всех фабрик.

        Имена фабрик должны быть уникальными. Если фабрика с таким именем уже существует,
        выбрасывается исключение ValueError.

        :param factory: Фабрика для добавления.
        :raises ValueError: Если имя фабрики уже существует.
        """
        if factory.name in TinyFactory.all_factories:
            logger.error(f"Factory names must be unique, but '{factory.name}' is already defined.")
            raise ValueError(f"Factory names must be unique, but '{factory.name}' is already defined.")
        else:
            TinyFactory.all_factories[factory.name] = factory

    @staticmethod
    def clear_factories():
        """
        Очищает глобальный список всех фабрик.
        """
        TinyFactory.all_factories = {}

    def encode_complete_state(self) -> dict:
        """
        Кодирует полное состояние фабрики.

        Если подклассы имеют несериализуемые элементы, они должны переопределить этот метод.

        :return: Словарь, представляющий состояние фабрики.
        """
        state = copy.deepcopy(self.__dict__)
        return state

    def decode_complete_state(self, state: dict):
        """
        Декодирует полное состояние фабрики.

        Если подклассы имеют несериализуемые элементы, они должны переопределить этот метод.

        :param state: Словарь, представляющий состояние фабрики.
        :return: Объект фабрики с восстановленным состоянием.
        """
        state = copy.deepcopy(state)
        self.__dict__.update(state)
        return self

class TinyPersonFactory(TinyFactory):
    """
    Фабрика для создания агентов TinyPerson.

    Этот класс отвечает за генерацию экземпляров TinyPerson на основе заданного контекста.
    """
    def __init__(self, context_text, simulation_id: str = None):
        """
        Инициализирует экземпляр TinyPersonFactory.

        :param context_text: Контекст, используемый для генерации экземпляров TinyPerson.
        :type context_text: str
        :param simulation_id: Идентификатор симуляции.
        :type simulation_id: str, optional
        """
        super().__init__(simulation_id)
        self.person_prompt_template_path = os.path.join(os.path.dirname(__file__), 'prompts/generate_person.mustache')
        self.context_text = context_text
        self.generated_minibios = []  #: list: Список сгенерированных мини-биографий.
        self.generated_names = []  #: list: Список сгенерированных имен.
    
    @staticmethod
    def generate_person_factories(number_of_factories, generic_context_text):
        """
        Генерирует список экземпляров TinyPersonFactory с использованием LLM OpenAI.

        :param number_of_factories: Количество экземпляров TinyPersonFactory для генерации.
        :type number_of_factories: int
        :param generic_context_text: Общий контекст для генерации TinyPersonFactory.
        :type generic_context_text: str
        :return: Список экземпляров TinyPersonFactory или None в случае ошибки.
        :rtype: list or None
        """
        logger.info(f"Starting the generation of the {number_of_factories} person factories based on that context: {generic_context_text}")
        
        try:
            with open(os.path.join(os.path.dirname(__file__), 'prompts/generate_person_factory.md'), 'r') as f:
                system_prompt = f.read()
        except Exception as e:
             logger.error(f"Error reading the prompt file: {e}")
             return None

        messages = [{"role": "system", "content": system_prompt}]

        user_prompt = chevron.render("Please, create {{number_of_factories}} person descriptions based on the following broad context: {{context}}", {
            "number_of_factories": number_of_factories,
            "context": generic_context_text
        })

        messages.append({"role": "user", "content": user_prompt})

        response = openai_utils.client().send_message(messages)

        if response is not None:
            try:
               result = utils.extract_json(response["content"])
            except Exception as e:
                logger.error(f"Error extracting JSON: {e}")
                return None

            factories = []
            for i in range(number_of_factories):
                logger.debug(f"Generating person factory with description: {result[i]}")
                factories.append(TinyPersonFactory(result[i]))

            return factories

        return None

    def generate_person(self, agent_particularities: str = None, temperature: float = 1.5, attepmpts: int = 5):
        """
        Генерирует экземпляр TinyPerson с использованием LLM OpenAI.

        :param agent_particularities: Особенности агента.
        :type agent_particularities: str, optional
        :param temperature: Температура для выборки из LLM.
        :type temperature: float, optional
        :param attepmpts: Количество попыток генерации.
        :type attepmpts: int, optional
        :return: Экземпляр TinyPerson или None в случае ошибки.
        :rtype: TinyPerson or None
        """
        logger.info(f"Starting the person generation based on that context: {self.context_text}")
        try:
            with open(self.person_prompt_template_path, 'r') as f:
                prompt = chevron.render(f.read(), {
                "context": self.context_text,
                "agent_particularities": agent_particularities,
                "already_generated": [minibio for minibio in self.generated_minibios]
            })
        except Exception as e:
             logger.error(f"Error reading the prompt template file: {e}")
             return None

        def aux_generate():
            messages = []
            messages += [{"role": "system", "content": "You are a system that generates specifications of artificial entities."},
                         {"role": "user", "content": prompt}]
            
            message = self._aux_model_call(messages=messages, temperature=temperature)
            
            if message is not None:
                try:
                    result = utils.extract_json(message["content"])
                except Exception as e:
                    logger.error(f"Error extracting JSON: {e}")
                    return None

                logger.debug(f"Generated person parameters:\\n{result}")

                if result["name"].lower() not in self.generated_names:
                    return result
            return None
        
        agent_spec = None
        attempt = 0
        while agent_spec is None and attempt < attepmpts:
            try:
                attempt += 1
                agent_spec = aux_generate()
            except Exception as e:
                 logger.error(f"Error while generating agent specification: {e}")

        if agent_spec is not None:
            person = TinyPerson(agent_spec["name"])
            self._setup_agent(person, agent_spec["_configuration"])
            self.generated_minibios.append(person.minibio())
            self.generated_names.append(person.get("name").lower())
            return person
        else:
            logger.error(f"Could not generate an agent after {attepmpts} attempts.")
            return None
    
    @transactional
    def _aux_model_call(self, messages, temperature):
        """
        Вспомогательный метод для вызова модели.
        
        Это необходимо для использования декоратора @transactional, иначе
        создание агента будет пропущено при повторном использовании кэша.
        
        :param messages: Сообщения для отправки модели.
        :type messages: list
        :param temperature: Температура для выборки из LLM.
        :type temperature: float
        :return: Ответ модели.
        """
        return openai_utils.client().send_message(messages, temperature=temperature)
    
    @transactional
    def _setup_agent(self, agent, configuration):
        """
        Настраивает агента с необходимыми элементами.
        
        :param agent: Экземпляр TinyPerson для настройки.
        :type agent: TinyPerson
        :param configuration: Конфигурация для настройки агента.
        :type configuration: dict
        """
        for key, value in configuration.items():
            if isinstance(value, list):
                agent.define_several(key, value)
            else:
                agent.define(key, value)
```