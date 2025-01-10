## Анализ кода модуля `factory.py`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разбит на классы, что способствует его организации и повторному использованию.
    - Использование `chevron` для шаблонизации промптов.
    - Применение `transactional` декоратора для кэширования вызовов.
    - Наличие логирования с использованием `logger`.
    - Использование `utils.fresh_id()` для генерации уникальных идентификаторов.
    - Обработка ошибок с помощью `try-except` и логированием.
    - Применение статических методов для управления фабриками.
    - Наличие методов для кодирования и декодирования состояния фабрик.
- Минусы
    -  Не везде используется `j_loads` для загрузки json.
    -  Не везде присутствуют docstrings, что затрудняет понимание кода.
    -  Импорт `logging` вместо `from src.logger import logger`
    -  Некоторые комментарии не соответствуют стандарту RST.

**Рекомендации по улучшению**

1.  **Импорты:**
    - Заменить `import logging` на `from src.logger.logger import logger`.
    - Добавить импорт `from src.utils.jjson import j_loads`.
2.  **Документация:**
    - Добавить docstrings в формате RST для всех классов, методов и функций.
    - Улучшить комментарии, сделав их более информативными и соответствующими стандарту RST.
3.  **Логирование:**
    - Использовать `logger.error` для обработки ошибок вместо `print`.
4.  **JSON:**
    - Использовать `j_loads` из `src.utils.jjson` вместо стандартного `json.loads` для чтения файлов.
5.  **Улучшения:**
    - Добавить проверку на наличие ключей в словаре `result` перед их использованием, например, при обращении к `result["name"]`.
    -  Использовать `os.path.join` для корректного формирования путей.
6.  **Стиль кода:**
    - Использовать одинарные кавычки для строк в коде, как указано в требованиях.

**Оптимизированный код**

```python
"""
Модуль для создания фабрик персонажей.
=========================================================================================

Этот модуль содержит классы :class:`TinyFactory` и :class:`TinyPersonFactory`,
которые используются для создания и управления фабриками персонажей,
а также для генерации экземпляров :class:`TinyPerson`.

Пример использования
--------------------

Пример создания и использования фабрики персонажей:

.. code-block:: python

    from tinytroupe.factory import TinyPersonFactory
    
    # Создание фабрики
    factory = TinyPersonFactory(context_text='Общий контекст')

    # Генерация персонажа
    person = factory.generate_person()

    if person:
        print(f"Сгенерирован персонаж: {person.get('name')}")
"""
import os
# import json # импорт удален, т.к. используется j_loads
import copy
# import logging # импорт заменен на from src.logger.logger import logger
import chevron

from src.logger.logger import logger # импорт логгера
from src.utils.jjson import j_loads # импорт j_loads
from tinytroupe import openai_utils
from tinytroupe.agent import TinyPerson
import tinytroupe.utils as utils
from tinytroupe.control import transactional


class TinyFactory:
    """
    Базовый класс для различных типов фабрик.
    
    Этот класс обеспечивает основу для создания и управления фабриками,
    а также поддерживает транзакционное кэширование.
    """

    # Словарь всех созданных на данный момент фабрик.
    all_factories = {}  # name -> factories

    def __init__(self, simulation_id: str = None) -> None:
        """
        Инициализирует экземпляр TinyFactory.

        Args:
            simulation_id (str, optional): Идентификатор симуляции. Defaults to None.
        """
        self.name = f'Factory {utils.fresh_id()}'  # требуется имя, но нет смысла делать его настраиваемым
        self.simulation_id = simulation_id

        TinyFactory.add_factory(self)

    def __repr__(self):
        """
        Возвращает строковое представление объекта TinyFactory.

        Returns:
             str: Строковое представление объекта.
        """
        return f'TinyFactory(name=\'{self.name}\')'

    @staticmethod
    def set_simulation_for_free_factories(simulation):
        """
        Устанавливает симуляцию, если она None.
        
        Позволяет свободным окружениям быть захваченными конкретными областями симуляции,
        если это необходимо.
        """
        for factory in TinyFactory.all_factories.values():
            if factory.simulation_id is None:
                simulation.add_factory(factory)

    @staticmethod
    def add_factory(factory):
        """
        Добавляет фабрику в список всех фабрик.

        Имена фабрик должны быть уникальными. Если фабрика с таким именем уже существует,
        возникает ошибка.

        Args:
            factory (TinyFactory): Фабрика для добавления.
        Raises:
            ValueError: Если фабрика с таким именем уже существует.
        """
        if factory.name in TinyFactory.all_factories:
            raise ValueError(f'Factory names must be unique, but \'{factory.name}\' is already defined.')
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

        Если подклассы имеют элементы, которые не являются сериализуемыми,
        они должны переопределить этот метод.
        
        Returns:
             dict: Словарь, представляющий состояние объекта.
        """
        state = copy.deepcopy(self.__dict__)
        return state

    def decode_complete_state(self, state: dict):
        """
        Декодирует полное состояние фабрики.

        Если подклассы имеют элементы, которые не являются сериализуемыми,
        они должны переопределить этот метод.
        
         Args:
             state (dict): Словарь, представляющий состояние объекта.
        Returns:
             TinyFactory: Объект фабрики с декодированным состоянием.
        """
        state = copy.deepcopy(state)

        self.__dict__.update(state)
        return self


class TinyPersonFactory(TinyFactory):
    """
    Фабрика для создания объектов :class:`TinyPerson`.

    Этот класс наследуется от :class:`TinyFactory` и предоставляет функциональность
    для генерации персонажей на основе контекста.
    """

    def __init__(self, context_text, simulation_id: str = None):
        """
        Инициализирует экземпляр TinyPersonFactory.

        Args:
            context_text (str): Контекстный текст, используемый для генерации экземпляров TinyPerson.
            simulation_id (str, optional): Идентификатор симуляции. Defaults to None.
        """
        super().__init__(simulation_id)
        self.person_prompt_template_path = os.path.join(os.path.dirname(__file__), 'prompts/generate_person.mustache')
        self.context_text = context_text
        self.generated_minibios = []  # отслеживание сгенерированных персон. Храним мини-биографию, чтобы не генерировать одного и того же человека дважды.
        self.generated_names = []

    @staticmethod
    def generate_person_factories(number_of_factories, generic_context_text):
        """
        Генерирует список экземпляров TinyPersonFactory с использованием LLM OpenAI.

        Args:
            number_of_factories (int): Количество экземпляров TinyPersonFactory для генерации.
            generic_context_text (str): Общий контекстный текст, используемый для генерации экземпляров TinyPersonFactory.

        Returns:
             list: Список экземпляров TinyPersonFactory.
        """
        logger.info(f'Starting the generation of the {number_of_factories} person factories based on that context: {generic_context_text}')

        system_prompt = open(os.path.join(os.path.dirname(__file__), 'prompts/generate_person_factory.md')).read()

        messages = []
        messages.append({'role': 'system', 'content': system_prompt})

        user_prompt = chevron.render('Please, create {{number_of_factories}} person descriptions based on the following broad context: {{context}}', {
            'number_of_factories': number_of_factories,
            'context': generic_context_text
        })

        messages.append({'role': 'user', 'content': user_prompt})

        response = openai_utils.client().send_message(messages)

        if response is not None:
            result = utils.extract_json(response['content'])

            factories = []
            for i in range(number_of_factories):
                logger.debug(f'Generating person factory with description: {result[i]}')
                factories.append(TinyPersonFactory(result[i]))

            return factories

        return None

    def generate_person(self, agent_particularities: str = None, temperature: float = 1.5, attepmpts: int = 5):
        """
        Генерирует экземпляр TinyPerson с использованием LLM OpenAI.

        Args:
            agent_particularities (str, optional): Особенности агента.
            temperature (float, optional): Температура для использования при выборке из LLM. Defaults to 1.5.
            attepmpts (int, optional): Количество попыток генерации. Defaults to 5.

        Returns:
            TinyPerson: Экземпляр TinyPerson, сгенерированный с использованием LLM.
        """
        logger.info(f'Starting the person generation based on that context: {self.context_text}')

        prompt = chevron.render(open(self.person_prompt_template_path).read(), {
            'context': self.context_text,
            'agent_particularities': agent_particularities,
            'already_generated': [minibio for minibio in self.generated_minibios]
        })

        def aux_generate():
            """
            Вспомогательная функция для генерации спецификации агента.
            """
            messages = []
            messages += [{'role': 'system', 'content': 'You are a system that generates specifications of artificial entities.'},
                         {'role': 'user', 'content': prompt}]

            # из-за технической особенности, требуется вызвать вспомогательный метод, чтобы использовать декоратор transactional
            message = self._aux_model_call(messages=messages, temperature=temperature)

            if message is not None:
                result = utils.extract_json(message['content'])

                logger.debug(f'Generated person parameters:\\n{j_loads(str(result), indent=4, sort_keys=True)}')

                # принимать сгенерированную спецификацию только если имя еще не в сгенерированных именах, т.к. они должны быть уникальными
                if result.get("name", "").lower() not in self.generated_names:
                     return result

            return None  # подходящий агент не был сгенерирован

        agent_spec = None
        attempt = 0
        while agent_spec is None and attempt < attepmpts:
            try:
                attempt += 1
                agent_spec = aux_generate()
            except Exception as e:
                logger.error(f'Error while generating agent specification: {e}')

        # создание нового агента
        if agent_spec is not None:
            # агент создается здесь. Поэтому данный метод не может быть кэширован.
            # Вместо этого используется вспомогательный метод
            # для фактического вызова модели, чтобы он правильно кэшировался, не пропуская создание агента.
            person = TinyPerson(agent_spec['name'])
            self._setup_agent(person, agent_spec['_configuration'])
            self.generated_minibios.append(person.minibio())
            self.generated_names.append(person.get('name').lower())
            return person
        else:
            logger.error(f'Could not generate an agent after {attepmpts} attempts.')
            return None

    @transactional
    def _aux_model_call(self, messages, temperature):
        """
        Вспомогательный метод для вызова модели.
        
        Это необходимо для того, чтобы использовать декоратор transactional,
        из-за технической особенности - иначе создание агента будет пропущено
        во время повторного использования кэша, и мы этого не хотим.
        """
        return openai_utils.client().send_message(messages, temperature=temperature)

    @transactional
    def _setup_agent(self, agent, configuration):
        """
        Настраивает агента с необходимыми элементами.
        
         Args:
             agent (TinyPerson): Объект агента.
             configuration (dict): Словарь с настройками.
        """
        for key, value in configuration.items():
            if isinstance(value, list):
                agent.define_several(key, value)
            else:
                agent.define(key, value)

        # ничего не возвращает, так как мы не хотим кэшировать сам объект агента.