# Анализ кода модуля `factory.py`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован с использованием классов и методов для организации функциональности.
    - Присутствует базовая документация в виде docstring для классов и методов.
    - Используется логгирование для отслеживания выполнения кода и ошибок.
    - Применяется шаблон проектирования "Фабрика" для создания экземпляров классов `TinyPerson`.
    - Используется библиотека `chevron` для шаблонизации, что способствует читаемости кода.
    - Применяется декоратор `@transactional` для кэширования результатов вызова методов модели.
- Минусы
    - Отсутствует полная документация в формате reStructuredText (RST).
    - Используется `json.dumps` вместо `j_dumps` или `j_dumps_ns` из `src.utils.jjson`.
    - Некоторые комментарии после `#` не соответствуют стандарту RST.
    - Использование `try-except` в цикле `while` может быть пересмотрено в пользу более конкретной обработки ошибок.
    -  `aux_generate`  не соответствует PEP 8 по именованию
    - Имя параметра `attepmpts` в методе `generate_person` написано с опечаткой, должно быть `attempts`

**Рекомендации по улучшению**
1.  **Документация**: Полностью переписать все docstring и комментарии в формате RST, включая описание модулей, классов, методов и параметров.
2.  **Использование `j_dumps`**: Заменить использование `json.dumps` на `j_dumps` или `j_dumps_ns` из `src.utils.jjson`.
3.  **Обработка ошибок**: Пересмотреть использование `try-except` в цикле `while` в методе `generate_person` и использовать `logger.error` для регистрации ошибок с более подробными сообщениями.
4.  **Имена переменных**: Исправить опечатку в имени переменной `attepmpts` на `attempts`.
5.  **Имена переменных**: Переименовать `aux_generate` в `_aux_generate` в соответствии с PEP 8
6.  **Импорты**: Добавить отсутствующие импорты `from src.utils.jjson import j_loads, j_dumps` и `from src.logger.logger import logger`.

**Оптимизированный код**
```python
"""
Модуль для создания агентов TinyPerson с использованием фабрик.
==================================================================

Этот модуль содержит классы :class:`TinyFactory` и :class:`TinyPersonFactory`,
которые используются для создания и управления агентами TinyPerson.
Фабрики обеспечивают гибкость и возможность кэширования в транзакционном режиме.

Пример использования
--------------------

Пример создания и использования фабрики TinyPersonFactory:

.. code-block:: python

    factory = TinyPersonFactory(context_text="Some context")
    person = factory.generate_person(agent_particularities="Some particularities")
"""
import os
# import json #  заменен на j_dumps, j_loads
import chevron
import logging
import copy
from typing import Any, Dict, List

from src.utils.jjson import j_loads, j_dumps # импортируем j_loads, j_dumps
from src.logger.logger import logger # импортируем logger
from tinytroupe import openai_utils
from tinytroupe.agent import TinyPerson
import tinytroupe.utils as utils
from tinytroupe.control import transactional

# logger = logging.getLogger("tinytroupe") #  перенесён в  src.logger.logger


class TinyFactory:
    """
    Базовый класс для различных типов фабрик.
    
    Этот класс облегчает расширение системы, особенно в отношении кэширования транзакций.
    """

    # Словарь всех созданных фабрик.
    all_factories: Dict[str, 'TinyFactory'] = {} # name -> factories
    
    def __init__(self, simulation_id: str = None) -> None:
        """
        Инициализирует экземпляр TinyFactory.

        :param simulation_id: Идентификатор симуляции.
        :type simulation_id: str, optional
        """
        self.name: str = f"Factory {utils.fresh_id()}" # имя фабрики, но нет смысла делать его настраиваемым
        self.simulation_id: str = simulation_id

        TinyFactory.add_factory(self)
    
    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта TinyFactory.

        :return: Строковое представление.
        :rtype: str
        """
        return f"TinyFactory(name=\'{self.name}\')"
    
    @staticmethod
    def set_simulation_for_free_factories(simulation: 'Simulation') -> None:
        """
        Устанавливает симуляцию для свободных фабрик.

        Позволяет свободным окружениям быть захваченными конкретными областями симуляции, если это необходимо.
        :param simulation: Экземпляр симуляции.
        :type simulation: Simulation
        """
        for factory in TinyFactory.all_factories.values():
            if factory.simulation_id is None:
                simulation.add_factory(factory)

    @staticmethod
    def add_factory(factory: 'TinyFactory') -> None:
        """
        Добавляет фабрику в список всех фабрик.

        Имена фабрик должны быть уникальными. Если фабрика с таким же именем уже существует,
        вызывается исключение ValueError.
        :param factory: Экземпляр фабрики.
        :type factory: TinyFactory
        :raises ValueError: Если фабрика с таким именем уже существует.
        """
        if factory.name in TinyFactory.all_factories:
            raise ValueError(f"Factory names must be unique, but \'{factory.name}\' is already defined.")
        else:
            TinyFactory.all_factories[factory.name] = factory
    
    @staticmethod
    def clear_factories() -> None:
        """
        Очищает глобальный список всех фабрик.
        """
        TinyFactory.all_factories = {}

    ################################################################################################
    # Механизмы кэширования
    #
    # Фабрики также могут быть кэшированы в транзакционном режиме. Это необходимо, потому что
    # агенты, которых они генерируют, могут быть кэшированы, и нужно убедиться, что сама
    # фабрика также кэшируется последовательным образом.
    ################################################################################################

    def encode_complete_state(self) -> dict:
        """
        Кодирует полное состояние фабрики.

        Если подклассы имеют элементы, которые не подлежат сериализации, они должны
        переопределить этот метод.

        :return: Словарь, представляющий состояние фабрики.
        :rtype: dict
        """

        state = copy.deepcopy(self.__dict__)
        return state

    def decode_complete_state(self, state: dict) -> 'TinyFactory':
        """
        Декодирует полное состояние фабрики.

        Если подклассы имеют элементы, которые не подлежат сериализации, они должны
        переопределить этот метод.

        :param state: Словарь, представляющий состояние фабрики.
        :type state: dict
        :return: Экземпляр фабрики.
        :rtype: TinyFactory
        """
        state = copy.deepcopy(state)

        self.__dict__.update(state)
        return self
 

class TinyPersonFactory(TinyFactory):
    """
    Фабрика для создания агентов TinyPerson.
    
    Использует текстовый контекст для генерации агентов.
    """
    def __init__(self, context_text: str, simulation_id: str = None) -> None:
        """
        Инициализирует экземпляр TinyPersonFactory.

        :param context_text: Текст контекста, используемый для генерации экземпляров TinyPerson.
        :type context_text: str
        :param simulation_id: Идентификатор симуляции.
        :type simulation_id: str, optional
        """
        super().__init__(simulation_id)
        self.person_prompt_template_path: str = os.path.join(os.path.dirname(__file__), 'prompts/generate_person.mustache')
        self.context_text: str = context_text
        self.generated_minibios: List[str] = [] # отслеживаем сгенерированных персон. Сохраняем мини-биографии, чтобы избежать повторной генерации одного и того же человека.
        self.generated_names: List[str] = []

    @staticmethod
    def generate_person_factories(number_of_factories: int, generic_context_text: str) -> List['TinyPersonFactory']:
        """
        Генерирует список экземпляров TinyPersonFactory с использованием LLM OpenAI.

        :param number_of_factories: Количество экземпляров TinyPersonFactory для генерации.
        :type number_of_factories: int
        :param generic_context_text: Общий текст контекста, используемый для генерации экземпляров TinyPersonFactory.
        :type generic_context_text: str
        :return: Список экземпляров TinyPersonFactory.
        :rtype: List[TinyPersonFactory]
        """
        
        logger.info(f"Starting the generation of the {number_of_factories} person factories based on that context: {generic_context_text}")
        
        system_prompt: str = open(os.path.join(os.path.dirname(__file__), 'prompts/generate_person_factory.md')).read()

        messages: List[Dict[str, str]] = []
        messages.append({"role": "system", "content": system_prompt})

        user_prompt: str = chevron.render("Please, create {{number_of_factories}} person descriptions based on the following broad context: {{context}}", {
            "number_of_factories": number_of_factories,
            "context": generic_context_text
        })

        messages.append({"role": "user", "content": user_prompt})

        response:  Dict[str, Any] = openai_utils.client().send_message(messages)
        
        if response is not None:
            result:  List[str] = utils.extract_json(response["content"])

            factories: List['TinyPersonFactory'] = []
            for i in range(number_of_factories):
                logger.debug(f"Generating person factory with description: {result[i]}")
                factories.append(TinyPersonFactory(result[i]))

            return factories

        return None

    def generate_person(self, agent_particularities: str = None, temperature: float = 1.5, attempts: int = 5) -> 'TinyPerson':
        """
        Генерирует экземпляр TinyPerson с использованием LLM OpenAI.

        :param agent_particularities: Особенности агента.
        :type agent_particularities: str, optional
        :param temperature: Температура для сэмплирования из LLM.
        :type temperature: float, optional
        :param attempts: Количество попыток для генерации агента.
        :type attempts: int, optional
        :return: Экземпляр TinyPerson, сгенерированный с использованием LLM.
        :rtype: TinyPerson
        """

        logger.info(f"Starting the person generation based on that context: {self.context_text}")

        prompt: str = chevron.render(open(self.person_prompt_template_path).read(), {
            "context": self.context_text,
            "agent_particularities": agent_particularities,
            "already_generated": [minibio for minibio in self.generated_minibios]
        })

        def _aux_generate() -> Dict:
            """
            Вспомогательный метод для генерации параметров агента.
            
            Этот метод используется для обхода проблем с кэшированием при использовании декоратора `@transactional`.
             
            :return: Словарь с параметрами агента.
            :rtype: Dict
            """

            messages: List[Dict[str, str]] = []
            messages += [{"role": "system", "content": "You are a system that generates specifications of artificial entities."},
                        {"role": "user", "content": prompt}]
            # из-за технических особенностей необходимо вызвать вспомогательный метод, чтобы иметь возможность использовать декоратор transactional.
            message: Dict[str, Any] = self._aux_model_call(messages=messages, temperature=temperature)

            if message is not None:
                result: Dict = utils.extract_json(message["content"])
                
                logger.debug(f"Generated person parameters:\\n{j_dumps(result, indent=4, sort_keys=True)}") # используем j_dumps

                # Принимаем сгенерированную спецификацию только в том случае, если имя еще не входит в список сгенерированных имен, поскольку они должны быть уникальными.
                if result["name"].lower() not in self.generated_names:
                    return result

            return None # подходящий агент не был сгенерирован
        
        agent_spec:  Dict = None
        attempt: int = 0
        while agent_spec is None and attempt < attempts:
            try:
                attempt += 1
                agent_spec = _aux_generate()
            except Exception as e:
                logger.error(f"Error while generating agent specification: {e}", exc_info=True) # добавил exc_info=True

        # создание нового агента
        if agent_spec is not None:
            # агент создается здесь. Именно поэтому данный метод не может быть кэширован. Вместо этого используется вспомогательный метод
            # для фактического вызова модели, чтобы он кэшировался правильно, не пропуская создание агента.
            person: TinyPerson = TinyPerson(agent_spec["name"])
            self._setup_agent(person, agent_spec["_configuration"])
            self.generated_minibios.append(person.minibio())
            self.generated_names.append(person.get("name").lower())
            return person
        else:
            logger.error(f"Could not generate an agent after {attempts} attempts.")
            return None
        
    
    @transactional
    def _aux_model_call(self, messages: List[Dict[str, str]], temperature: float) -> Dict[str, Any]:
        """
        Вспомогательный метод для вызова модели.

        Это необходимо для того, чтобы иметь возможность использовать декоратор transactional,
        из-за технических особенностей - в противном случае создание агента будет пропущено при повторном использовании кэша,
        и нам этого не хочется.

        :param messages: Список сообщений для отправки в модель.
        :type messages: List[Dict[str, str]]
        :param temperature: Температура для сэмплирования из LLM.
        :type temperature: float
        :return: Ответ от модели.
        :rtype: Dict[str, Any]
        """
        return openai_utils.client().send_message(messages, temperature=temperature)
    
    @transactional
    def _setup_agent(self, agent: 'TinyPerson', configuration: Dict) -> None:
        """
        Настраивает агента необходимыми элементами.

        :param agent: Экземпляр агента.
        :type agent: TinyPerson
        :param configuration: Словарь с конфигурацией агента.
        :type configuration: Dict
        """
        for key, value in configuration.items():
            if isinstance(value, list):
                agent.define_several(key, value)
            else:
                agent.define(key, value)
        
        # ничего не возвращает, так как мы не хотим кэшировать сам объект агента.
```