# Анализ кода модуля `factory.py`

**Качество кода**
9
-   Плюсы
    -   Код хорошо структурирован и разбит на классы и методы, что облегчает его понимание и поддержку.
    -   Используется `logger` для логирования, что помогает отслеживать работу программы и диагностировать ошибки.
    -   Применяются декораторы `@transactional` для кэширования, что повышает производительность.
    -   Код использует шаблоны `chevron` для генерации текстовых запросов, что делает код более гибким.
    -   Документация присутствует, но требует доработки.
-   Минусы
    -   Используется `json.dumps`, нужно использовать `j_dumps` из `src.utils.jjson`.
    -   Не все функции и методы имеют подробные docstring, что затрудняет понимание их назначения.
    -   В некоторых местах используются общие `try-except`, которые можно заменить на более конкретную обработку ошибок с помощью `logger.error`.
    -   Импорты не приведены в соответствие с другими модулями.

**Рекомендации по улучшению**

1.  **Импорты**:
    -   Добавить импорт `from src.utils.jjson import j_dumps`
    -   Импортировать `logger` из `src.logger.logger`.
2.  **Документация**:
    -   Добавить подробные docstring в стиле RST ко всем классам, методам и функциям.
    -   Уточнить назначение всех переменных.
    -   Привести примеры использования.
3.  **Обработка ошибок**:
    -   Использовать `logger.error` вместо общих `try-except` блоков.
    -   Уточнить сообщения об ошибках, добавив контекст.
4.  **Код**:
    -   Заменить `json.dumps` на `j_dumps` из `src.utils.jjson`
    -   Убрать лишнее дублирование кода, где это возможно.
5.  **Комментарии**:
    -   Добавить комментарии `#` к строкам, объясняющие логику кода.
    -   Избегать комментариев, описывающих общие действия, вроде "получаем" или "делаем", заменив их на более конкретные формулировки, такие как "проверка", "отправка" или "код исполняет ...".
6.  **Форматирование**:
    -   Использовать одинарные кавычки для строк в коде Python, двойные - только в операциях вывода.

**Оптимизированный код**

```python
"""
Модуль для создания и управления фабриками агентов.
=========================================================================================

Этот модуль содержит классы :class:`TinyFactory` и :class:`TinyPersonFactory`,
которые используются для создания различных типов фабрик агентов.
Фабрики управляют созданием агентов :class:`TinyPerson` и их кэшированием.

Пример использования
--------------------

Пример создания фабрики `TinyPersonFactory` и генерации агента:

.. code-block:: python

    factory = TinyPersonFactory(context_text='Example context')
    agent = factory.generate_person()

"""
import os
import chevron
import copy
from src.logger.logger import logger # Импорт logger из sr.logger
from src.utils.jjson import j_dumps # Импортируем j_dumps
from tinytroupe import openai_utils
from tinytroupe.agent import TinyPerson
import tinytroupe.utils as utils
from tinytroupe.control import transactional

class TinyFactory:
    """
    Базовый класс для различных типов фабрик.
    Этот класс облегчает расширение системы, особенно в отношении транзакционного кэширования.

    :ivar all_factories: Словарь всех созданных на данный момент фабрик.
    :vartype all_factories: dict
    """

    # Словарь всех созданных на данный момент фабрик.
    all_factories = {} # name -> factories
    
    def __init__(self, simulation_id:str=None) -> None:
        """
        Инициализирует экземпляр :class:`TinyFactory`.

        :param simulation_id: ID симуляции.
        :type simulation_id: str, optional
        """
        # Присваивает имя фабрике и устанавливает simulation_id
        self.name = f'Factory {utils.fresh_id()}' # имя фабрики
        self.simulation_id = simulation_id

        # Добавляет фабрику в общий список фабрик
        TinyFactory.add_factory(self)
    
    def __repr__(self):
        """
        Возвращает строковое представление экземпляра :class:`TinyFactory`.

        :return: Строковое представление фабрики.
        :rtype: str
        """
        return f'TinyFactory(name=\'{self.name}\')'
    
    @staticmethod
    def set_simulation_for_free_factories(simulation):
        """
        Устанавливает симуляцию для фабрик, у которых simulation_id равен None.
        
        :param simulation: Объект симуляции.
        :type simulation: Simulation
        """
        # Проходит по всем фабрикам
        for factory in TinyFactory.all_factories.values():
            # Если у фабрики нет simulation_id, добавляет ее в симуляцию
            if factory.simulation_id is None:
                simulation.add_factory(factory)

    @staticmethod
    def add_factory(factory):
        """
        Добавляет фабрику в список всех фабрик.
        
        :param factory: Экземпляр фабрики.
        :type factory: TinyFactory
        :raises ValueError: Если фабрика с таким именем уже существует.
        """
        # Проверка уникальности имени фабрики
        if factory.name in TinyFactory.all_factories:
            # Если фабрика с таким именем уже существует, выбрасывает исключение
            raise ValueError(f'Factory names must be unique, but \'{factory.name}\' is already defined.')
        else:
            # Иначе, добавляет фабрику в список
            TinyFactory.all_factories[factory.name] = factory
    
    @staticmethod
    def clear_factories():
        """
        Очищает глобальный список всех фабрик.
        """
        # Очищает список всех фабрик
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
        
        :return: Словарь, представляющий состояние фабрики.
        :rtype: dict
        """
        # Копирует состояние фабрики
        state = copy.deepcopy(self.__dict__)
        return state

    def decode_complete_state(self, state:dict):
        """
        Декодирует полное состояние фабрики.
        
        :param state: Словарь с состоянием фабрики.
        :type state: dict
        :return: Экземпляр фабрики с восстановленным состоянием.
        :rtype: TinyFactory
        """
        # Копирует состояние и обновляет атрибуты фабрики
        state = copy.deepcopy(state)
        self.__dict__.update(state)
        return self
 

class TinyPersonFactory(TinyFactory):
    """
    Фабрика для создания экземпляров :class:`TinyPerson`.

    :ivar person_prompt_template_path: Путь к шаблону промпта для генерации персоны.
    :vartype person_prompt_template_path: str
    :ivar context_text: Контекстный текст, используемый для генерации экземпляров :class:`TinyPerson`.
    :vartype context_text: str
    :ivar generated_minibios: Список сгенерированных минибиографий.
    :vartype generated_minibios: list
    :ivar generated_names: Список сгенерированных имен.
    :vartype generated_names: list
    """

    def __init__(self, context_text, simulation_id:str=None):
        """
        Инициализирует экземпляр :class:`TinyPersonFactory`.

        :param context_text: Контекстный текст для генерации экземпляров :class:`TinyPerson`.
        :type context_text: str
        :param simulation_id: ID симуляции.
        :type simulation_id: str, optional
        """
        # Вызывает конструктор родительского класса
        super().__init__(simulation_id)
        # Устанавливает путь к шаблону промпта и контекстный текст
        self.person_prompt_template_path = os.path.join(os.path.dirname(__file__), 'prompts/generate_person.mustache')
        self.context_text = context_text
        # Инициализирует списки для отслеживания сгенерированных персонажей
        self.generated_minibios = [] # keep track of the generated persons. We keep the minibio to avoid generating the same person twice.
        self.generated_names = []

    @staticmethod
    def generate_person_factories(number_of_factories, generic_context_text):
        """
        Генерирует список экземпляров :class:`TinyPersonFactory` с использованием LLM.
        
        :param number_of_factories: Количество экземпляров :class:`TinyPersonFactory` для генерации.
        :type number_of_factories: int
        :param generic_context_text: Общий контекстный текст.
        :type generic_context_text: str
        :return: Список экземпляров :class:`TinyPersonFactory`.
        :rtype: list
        """
        
        # Логируем начало генерации
        logger.info(f'Starting the generation of the {number_of_factories} person factories based on that context: {generic_context_text}')
        
        # Читает системный промпт
        system_prompt = open(os.path.join(os.path.dirname(__file__), 'prompts/generate_person_factory.md')).read()

        messages = []
        # Добавляет системный промпт в список сообщений
        messages.append({'role': 'system', 'content': system_prompt})

        # Формирует пользовательский промпт
        user_prompt = chevron.render('Please, create {{number_of_factories}} person descriptions based on the following broad context: {{context}}', {
            'number_of_factories': number_of_factories,
            'context': generic_context_text
        })

        # Добавляет пользовательский промпт в список сообщений
        messages.append({'role': 'user', 'content': user_prompt})

        # Отправляет сообщение в LLM
        response = openai_utils.client().send_message(messages)

        # Обрабатывает ответ
        if response is not None:
            # Извлекает JSON из ответа
            result = utils.extract_json(response['content'])

            factories = []
            # Создает экземпляры TinyPersonFactory
            for i in range(number_of_factories):
                logger.debug(f'Generating person factory with description: {result[i]}')
                factories.append(TinyPersonFactory(result[i]))

            return factories

        return None

    def generate_person(self, agent_particularities:str=None, temperature:float=1.5, attepmpts:int=5):
        """
        Генерирует экземпляр :class:`TinyPerson` с использованием LLM.
        
        :param agent_particularities: Особенности агента.
        :type agent_particularities: str, optional
        :param temperature: Температура для сэмплирования из LLM.
        :type temperature: float, optional
        :param attepmpts: Количество попыток генерации.
        :type attepmpts: int, optional
        :return: Экземпляр :class:`TinyPerson`.
        :rtype: TinyPerson
        """

        # Логируем начало генерации персоны
        logger.info(f'Starting the person generation based on that context: {self.context_text}')

        # Формирует промпт для генерации персоны
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
            # Формирует сообщения для LLM
            messages += [{'role': 'system', 'content': 'You are a system that generates specifications of artificial entities.'},
                        {'role': 'user', 'content': prompt}]

            # Вызывает вспомогательный метод для отправки запроса в модель
            message = self._aux_model_call(messages=messages, temperature=temperature)

            # Обрабатывает ответ
            if message is not None:
                # Извлекает JSON из ответа
                result = utils.extract_json(message['content'])
                # Логируем параметры сгенерированной персоны
                logger.debug(f'Generated person parameters:\\n{j_dumps(result, indent=4, sort_keys=True)}') # Используем j_dumps

                # Проверяет уникальность имени
                if result['name'].lower() not in self.generated_names:
                    return result

            return None # Если агент не был сгенерирован

        agent_spec = None
        attempt = 0
        # Выполняет попытки генерации агента
        while agent_spec is None and attempt < attepmpts:
            try:
                attempt += 1
                agent_spec = aux_generate()
            except Exception as e:
                # Логируем ошибку
                logger.error(f'Error while generating agent specification: {e}')
        
        # Создаем агента, если спецификация была получена
        if agent_spec is not None:
            # Создание агента
            person = TinyPerson(agent_spec['name'])
            # Настраиваем агента
            self._setup_agent(person, agent_spec['_configuration'])
            # Добавляем минибиографию и имя в списки
            self.generated_minibios.append(person.minibio())
            self.generated_names.append(person.get('name').lower())
            return person
        else:
            # Логируем ошибку, если агент не был сгенерирован
            logger.error(f'Could not generate an agent after {attepmpts} attempts.')
            return None
        
    
    @transactional
    def _aux_model_call(self, messages, temperature):
        """
        Вспомогательный метод для вызова модели.
        Этот метод необходим для использования декоратора @transactional.
        
        :param messages: Список сообщений для LLM.
        :type messages: list
        :param temperature: Температура для сэмплирования из LLM.
        :type temperature: float
        :return: Ответ от LLM.
        :rtype: dict
        """
        # Отправляет сообщение в LLM
        return openai_utils.client().send_message(messages, temperature=temperature)
    
    @transactional
    def _setup_agent(self, agent, configuration):
        """
        Настраивает агента с необходимыми элементами.
        
        :param agent: Экземпляр агента.
        :type agent: TinyPerson
        :param configuration: Конфигурация агента.
        :type configuration: dict
        """
        # Проходит по всем элементам конфигурации
        for key, value in configuration.items():
            # Если значение является списком, настраивает несколько значений
            if isinstance(value, list):
                agent.define_several(key, value)
            else:
                # Иначе, настраивает одно значение
                agent.define(key, value)
        
        # Не возвращает ничего, так как мы не хотим кэшировать объект агента