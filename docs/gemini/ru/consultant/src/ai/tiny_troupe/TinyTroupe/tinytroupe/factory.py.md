# Анализ кода модуля `factory.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и разделен на классы `TinyFactory` и `TinyPersonFactory`, что соответствует принципам объектно-ориентированного программирования.
    - Используются статические методы для создания и управления фабриками.
    - Применяется декоратор `@transactional` для кэширования вызовов модели.
    - Есть логирование для отслеживания ошибок и процесса генерации.
    - Применяется шаблон проектирования "Фабрика" для создания объектов `TinyPerson`.
    - Использование `chevron` для шаблонизации запросов к модели.
- Минусы
    -  Недостаточно документации в формате RST.
    -  Используется стандартный `json.dumps` вместо `j_dumps` из `src.utils.jjson` (хотя в требованиях не было указано обратного).
    -  Не везде используется логирование ошибок.
    - В `aux_generate` не указано что за ошибка может возникнуть при вызове `utils.extract_json` (стоит добавить `except Exception as e`)

**Рекомендации по улучшению**

1.  Добавить RST-документацию для всех классов, методов и функций.
2.  Заменить `json.dumps` на `j_dumps` из `src.utils.jjson`.
3.  Добавить обработку ошибок в `aux_generate` при вызове `utils.extract_json`.
4.  Улучшить логирование, добавив больше деталей об ошибках.
5.  Избегать `try-except` там, где достаточно проверки и логирования ошибки.
6.  Уточнить комментарии, сделать их более конкретными и содержательными.
7.  Добавить проверки на наличие необходимых ключей в словаре `result` перед их использованием.

**Оптимизированный код**

```python
"""
Модуль для управления фабриками агентов TinyTroupe.
====================================================

Этот модуль предоставляет классы для создания и управления фабриками, которые генерируют агентов `TinyPerson`.
Он включает в себя базовый класс `TinyFactory` и класс `TinyPersonFactory` для генерации персон с использованием LLM.

Пример использования
--------------------

Пример создания и использования фабрики персон:

.. code-block:: python

    from tinytroupe.factory import TinyPersonFactory
    
    factory = TinyPersonFactory(context_text="Some context")
    person = factory.generate_person()
    
"""
import os
# import json # Стандартный json не используется, нужно использовать j_loads
import logging
import copy
from typing import List, Dict, Any

from src.utils.jjson import j_dumps # Используем j_dumps
from tinytroupe import openai_utils
from tinytroupe.agent import TinyPerson
import tinytroupe.utils as utils
from tinytroupe.control import transactional
from src.logger.logger import logger

import chevron # type: ignore


class TinyFactory:
    """
    Базовый класс для различных типов фабрик.
    
    Этот класс важен для расширения системы, особенно в части транзакционного кэширования.
    
    :ivar all_factories: Словарь всех созданных фабрик.
    :vartype all_factories: Dict[str, TinyFactory]
    """

    all_factories = {}  # type: Dict[str, TinyFactory] # name -> factories

    def __init__(self, simulation_id: str = None) -> None:
        """
        Инициализирует экземпляр TinyFactory.

        :param simulation_id: Идентификатор симуляции.
        :type simulation_id: str, optional
        """
        self.name = f"Factory {utils.fresh_id()}"  # Имя фабрики, не настраивается
        self.simulation_id = simulation_id

        TinyFactory.add_factory(self)

    def __repr__(self):
        """
        Возвращает строковое представление объекта TinyFactory.

        :return: Строковое представление фабрики.
        :rtype: str
        """
        return f"TinyFactory(name='{self.name}')"

    @staticmethod
    def set_simulation_for_free_factories(simulation):
        """
        Устанавливает симуляцию для свободных фабрик.
        
        Позволяет захватывать свободные окружения определенными областями симуляции.

        :param simulation: Объект симуляции.
        :type simulation: Any
        """
        for factory in TinyFactory.all_factories.values():
            if factory.simulation_id is None:
                simulation.add_factory(factory)

    @staticmethod
    def add_factory(factory):
        """
        Добавляет фабрику в список всех фабрик.

        Имена фабрик должны быть уникальными. Если фабрика с таким именем уже существует, возникает ошибка.

        :param factory: Объект фабрики для добавления.
        :type factory: TinyFactory
        :raises ValueError: Если фабрика с таким именем уже существует.
        """
        if factory.name in TinyFactory.all_factories:
            logger.error(f"Фабрика с именем '{factory.name}' уже существует.") # Логирование ошибки
            raise ValueError(f"Factory names must be unique, but '{factory.name}' is already defined.")
        else:
            TinyFactory.all_factories[factory.name] = factory

    @staticmethod
    def clear_factories():
        """
        Очищает глобальный список всех фабрик.
        """
        TinyFactory.all_factories = {}

    ################################################################################################
    # Caching mechanisms
    #
    # Factories can also be cached in a transactional way. This is necessary because the agents they
    # generate can be cached, and we need to ensure that the factory itself is also cached in a
    # consistent way.
    ################################################################################################

    def encode_complete_state(self) -> dict:
        """
        Кодирует полное состояние фабрики.

        Если подклассы имеют несериализуемые элементы, они должны переопределить этот метод.

        :return: Словарь с состоянием фабрики.
        :rtype: dict
        """
        state = copy.deepcopy(self.__dict__)
        return state

    def decode_complete_state(self, state: dict):
        """
        Декодирует полное состояние фабрики.

        Если подклассы имеют несериализуемые элементы, они должны переопределить этот метод.

        :param state: Словарь с состоянием для декодирования.
        :type state: dict
        :return: Экземпляр фабрики с декодированным состоянием.
        :rtype: TinyFactory
        """
        state = copy.deepcopy(state)

        self.__dict__.update(state)
        return self


class TinyPersonFactory(TinyFactory):
    """
    Фабрика для создания агентов TinyPerson.
    
    Этот класс использует LLM для генерации персон на основе заданного контекста.

    :ivar person_prompt_template_path: Путь к шаблону промпта для генерации персон.
    :vartype person_prompt_template_path: str
    :ivar context_text: Контекст для генерации персон.
    :vartype context_text: str
    :ivar generated_minibios: Список сгенерированных мини-биографий.
    :vartype generated_minibios: List[str]
    :ivar generated_names: Список сгенерированных имен.
    :vartype generated_names: List[str]
    """

    def __init__(self, context_text, simulation_id: str = None):
        """
        Инициализирует экземпляр TinyPersonFactory.

        :param context_text: Текст контекста для генерации экземпляров TinyPerson.
        :type context_text: str
        :param simulation_id: Идентификатор симуляции.
        :type simulation_id: str, optional
        """
        super().__init__(simulation_id)
        self.person_prompt_template_path = os.path.join(os.path.dirname(__file__), 'prompts/generate_person.mustache')
        self.context_text = context_text
        self.generated_minibios = []  # тип: List[str] # keep track of the generated persons. We keep the minibio to avoid generating the same person twice.
        self.generated_names = [] # type: List[str]

    @staticmethod
    def generate_person_factories(number_of_factories: int, generic_context_text: str) -> List['TinyPersonFactory'] | None:
        """
        Генерирует список экземпляров TinyPersonFactory, используя LLM OpenAI.

        :param number_of_factories: Количество экземпляров TinyPersonFactory для генерации.
        :type number_of_factories: int
        :param generic_context_text: Общий текст контекста для генерации экземпляров TinyPersonFactory.
        :type generic_context_text: str
        :return: Список экземпляров TinyPersonFactory или None в случае ошибки.
        :rtype: List[TinyPersonFactory] | None
        """
        logger.info(f"Начинается генерация {number_of_factories} фабрик персон на основе контекста: {generic_context_text}") # Логирование начала процесса

        system_prompt = open(os.path.join(os.path.dirname(__file__), 'prompts/generate_person_factory.md')).read()

        messages = []
        messages.append({"role": "system", "content": system_prompt})

        user_prompt = chevron.render("Please, create {{number_of_factories}} person descriptions based on the following broad context: {{context}}", {
            "number_of_factories": number_of_factories,
            "context": generic_context_text
        })

        messages.append({"role": "user", "content": user_prompt})

        response = openai_utils.client().send_message(messages)

        if response is not None:
            result = utils.extract_json(response["content"])
            
            if not isinstance(result, list):
                 logger.error(f'Ожидался список, но получен результат типа: {type(result)}. Контент ответа: {response["content"]}')
                 return None
            
            if len(result) != number_of_factories:
                  logger.error(f'Ожидалось {number_of_factories} фабрик, но получено {len(result)}. Контент ответа: {response["content"]}')
                  return None

            factories = []
            for i in range(number_of_factories):
                logger.debug(f"Генерируется фабрика персон с описанием: {result[i]}") # Логирование генерации фабрики
                factories.append(TinyPersonFactory(result[i]))

            return factories
        else:
            logger.error('Не удалось получить ответ от модели') # Логирование ошибки
            return None

    def generate_person(self, agent_particularities: str = None, temperature: float = 1.5, attepmpts: int = 5) -> 'TinyPerson' | None:
        """
        Генерирует экземпляр TinyPerson, используя LLM OpenAI.

        :param agent_particularities: Особенности агента.
        :type agent_particularities: str, optional
        :param temperature: Температура для сэмплирования из LLM.
        :type temperature: float, optional
        :param attepmpts: Количество попыток генерации.
        :type attepmpts: int, optional
        :return: Экземпляр TinyPerson или None в случае ошибки.
        :rtype: TinyPerson | None
        """
        logger.info(f"Начинается генерация персоны на основе контекста: {self.context_text}") # Логирование начала процесса

        prompt = chevron.render(open(self.person_prompt_template_path).read(), {
            "context": self.context_text,
            "agent_particularities": agent_particularities,
            "already_generated": [minibio for minibio in self.generated_minibios]
        })

        def aux_generate() -> Dict[str, Any] | None:
            """
            Вспомогательный метод для вызова модели.

            :return: Словарь с параметрами агента или None в случае ошибки.
            :rtype: dict | None
            """
            messages = []
            messages += [{"role": "system", "content": "You are a system that generates specifications of artificial entities."},
                         {"role": "user", "content": prompt}]

            # из-за технической особенности, необходимо использовать вспомогательный метод, чтобы можно было использовать декоратор transactional.
            message = self._aux_model_call(messages=messages, temperature=temperature)

            if message is not None:
                try:
                    result = utils.extract_json(message["content"])
                except Exception as e:
                    logger.error(f"Ошибка при извлечении JSON: {e}, контент ответа: {message['content']}")
                    return None # Обработка ошибки при извлечении json
                
                logger.debug(f"Сгенерированные параметры персоны:\\n{j_dumps(result, indent=4, sort_keys=True)}") # Логирование сгенерированных параметров

                # принимается только сгенерированная спецификация, если имени нет в списке сгенерированных имен, так как они должны быть уникальными.
                if "name" in result and result["name"].lower() not in self.generated_names:
                    return result
            else:
                  logger.error('Не получен ответ от модели')

            return None # Не удалось сгенерировать подходящего агента

        agent_spec = None
        attempt = 0
        while agent_spec is None and attempt < attepmpts:
            try:
                attempt += 1
                agent_spec = aux_generate()
            except Exception as e:
                logger.error(f"Ошибка при генерации спецификации агента: {e}")
        
        # код создает нового агента
        if agent_spec is not None:
            # Агент создается здесь. Именно поэтому данный метод не может быть закеширован. Вместо этого используется вспомогательный метод
            # для фактического вызова модели, чтобы он был правильно закеширован без пропуска создания агента.
            if "name" not in agent_spec or "_configuration" not in agent_spec:
                logger.error(f"Недопустимый формат спецификации агента: {agent_spec}")
                return None
            person = TinyPerson(agent_spec["name"])
            self._setup_agent(person, agent_spec["_configuration"])
            self.generated_minibios.append(person.minibio())
            self.generated_names.append(person.get("name").lower())
            return person
        else:
            logger.error(f"Не удалось сгенерировать агента после {attepmpts} попыток.") # Логирование ошибки
            return None

    @transactional
    def _aux_model_call(self, messages: List[Dict[str, str]], temperature: float) -> Dict[str, Any] | None:
        """
        Вспомогательный метод для вызова модели.
        
        Необходим для использования декоратора transactional, иначе создание агента будет пропущено во время повторного использования кэша.

        :param messages: Список сообщений для отправки в модель.
        :type messages: List[Dict[str, str]]
        :param temperature: Температура для сэмплирования из LLM.
        :type temperature: float
        :return: Ответ от модели или None в случае ошибки.
        :rtype: Dict[str, Any] | None
        """
        return openai_utils.client().send_message(messages, temperature=temperature)

    @transactional
    def _setup_agent(self, agent: TinyPerson, configuration: Dict[str, Any]) -> None:
        """
        Настраивает агента необходимыми элементами.

        :param agent: Объект агента для настройки.
        :type agent: TinyPerson
        :param configuration: Словарь с конфигурацией агента.
        :type configuration: Dict[str, Any]
        """
        for key, value in configuration.items():
            if isinstance(value, list):
                agent.define_several(key, value)
            else:
                agent.define(key, value)
        
        # не возвращает ничего, так как мы не хотим кэшировать сам объект агента.
```