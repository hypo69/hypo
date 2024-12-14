## Анализ кода модуля `control.py`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован с использованием классов `Simulation` и `Transaction`, что способствует модульности.
    -  Присутствует подробная логика управления состоянием симуляции, включая кэширование и транзакции.
    - Используется логгер для отслеживания ошибок и отладки.
    -  Реализована система кэширования состояний и механизма выполнения транзакций.
    - Код содержит docstring, описывающие основную функциональность классов и методов.
-  Минусы
    -  Не все docstring соответствуют стандарту reStructuredText (RST).
    -  Не везде используются `j_loads` или `j_loads_ns` для чтения JSON файлов.
    -  Использование `print` для ошибок.
    -  Некоторые комментарии `#` не объясняют последующий код в деталях.
    -  Отсутствуют проверки типов для параметров в некоторых функциях.
    -  Присутствуют некоторые избыточные комментарии в коде.
    -  Отсутсвует консистентность в использовании кавычек (где-то одинарные, где-то двойные).

**Рекомендации по улучшению**

1.  **Документация**:
    -   Переписать все docstring в формате RST, включая параметры и возвращаемые значения.
    -   Добавить более подробные описания классов и методов.
2.  **Импорты**:
    -   Добавить `from src.utils.jjson import j_loads` и `from src.logger.logger import logger`.
3.  **Обработка файлов**:
    -   Использовать `j_loads` для загрузки данных из JSON файлов.
4.  **Логирование**:
    -   Заменить `print` на `logger.error` для логирования ошибок.
    -   Обеспечить консистентное использование логгера для всех важных событий.
5.  **Транзакции**:
    -   Рассмотреть возможность добавления более гибкого механизма для работы с транзакциями.
6.  **Кэширование**:
    -   Оптимизировать логику кэширования для повышения производительности.
7.  **Улучшение комментариев**:
    -  Уточнить комментарии после `#`, чтобы они более точно описывали действие следующего кода.
8.  **Консистентность кавычек**:
    - Привести к единообразному виду использование кавычек `''`.
9.  **Удалить избыточные комментарии**:
    - Убрать не нужные коментарии, которые не несут смысловой нагрузки

**Оптимизированный код**

```python
"""
Модуль для управления симуляцией.
=========================================================================================

Этот модуль содержит класс :class:`Simulation` для управления состоянием симуляции,
а также класс :class:`Transaction` для управления транзакциями в симуляции.

Пример использования
--------------------

Пример использования класса `Simulation`:

.. code-block:: python

    simulation = Simulation(id='my_simulation')
    simulation.begin()
    # ... actions ...
    simulation.end()

Пример использования декоратора `@transactional`:

.. code-block:: python

    @transactional
    def some_action(self, param1, param2):
        # ... действия в рамках транзакции ...
        pass
"""
import os
import tempfile
from typing import Any

# from tinytroupe.utils import j_loads, j_dumps # TODO удалить, если не нужно
from src.utils.jjson import j_loads  # Используем j_loads для загрузки JSON
from src.logger.logger import logger
import tinytroupe.utils as utils
from tinytroupe.agent import TinyPerson # TODO перенести импорт внутрь методов, где он используется
from tinytroupe.environment import TinyWorld # TODO перенести импорт внутрь методов, где он используется
from tinytroupe.factory import TinyFactory # TODO перенести импорт внутрь методов, где он используется

class Simulation:
    """
    Управляет состоянием симуляции, включая агентов, окружения и кэширование.
    """

    STATUS_STOPPED = 'stopped'
    STATUS_STARTED = 'started'

    def __init__(self, id='default', cached_trace: list = None):
        """
        Инициализирует объект симуляции.

        :param id: Идентификатор симуляции.
        :param cached_trace: Список для хранения кэшированной трассировки.
        """
        self.id = id

        self.agents = []
        self.name_to_agent = {}  # {agent_name: agent, ...}

        self.environments = []

        self.factories = []  # e.g., TinyPersonFactory instances
        self.name_to_factory = {}  # {factory_name: factory, ...}

        self.name_to_environment = {}  # {environment_name: environment, ...}
        self.status = Simulation.STATUS_STOPPED

        self.cache_path = f'./tinytroupe-cache-{id}.json'  # default cache path

        #  Определяет, нужно ли автоматически сохранять состояние после каждой транзакции
        self.auto_checkpoint = False

        # Определяет, есть ли несохраненные изменения в кэше
        self.has_unsaved_cache_changes = False

        #  Определяет, выполняется ли транзакция, для управления кэшированием
        self._under_transaction = False

        # Механизм кэширования. Хранит список состояний симуляции.
        # Каждое состояние — это кортеж (prev_node_hash, event_hash, event_output, state),
        # где prev_node_hash — хеш предыдущего узла, event_hash — хеш события, event_output - вывод события,
        # state — фактическое состояние.
        if cached_trace is None:
            self.cached_trace = []
        else:
            self.cached_trace = cached_trace

        # Механизм трассировки выполнения.
        # Фактическая текущая трассировка выполнения.
        # Каждое состояние — это кортеж (prev_node_hash, event_hash, state),
        # где prev_node_hash — хеш предыдущего узла, event_hash — хеш события, state — состояние.
        self.execution_trace = []

    def begin(self, cache_path: str = None, auto_checkpoint: bool = False):
        """
        Отмечает начало управляемой симуляции.

        :param cache_path: Путь к файлу кэша.
        :param auto_checkpoint: Флаг автоматического сохранения после каждой транзакции.
        """
        if self.status == Simulation.STATUS_STOPPED:
            self.status = Simulation.STATUS_STARTED
        else:
            raise ValueError('Simulation is already started.')

        if cache_path is not None:
            self.cache_path = cache_path

        # Установка флага автосохранения
        self.auto_checkpoint = auto_checkpoint

        # Очистка агентов, окружений и других сущностей
        TinyPerson.clear_agents()
        TinyWorld.clear_environments()
        TinyFactory.clear_factories()

        # Сброс счетчика id для новой симуляции
        utils._fresh_id_counter = 0

        # Загрузка кэша, если есть
        if self.cache_path is not None:
            self._load_cache_file(self.cache_path)

    def end(self):
        """
        Отмечает конец управляемой симуляции.
        """
        if self.status == Simulation.STATUS_STARTED:
            self.status = Simulation.STATUS_STOPPED
            self.checkpoint()
        else:
            raise ValueError('Simulation is already stopped.')

    def checkpoint(self):
        """
        Сохраняет текущую трассировку симуляции в файл.
        """
        if self.has_unsaved_cache_changes:
            self._save_cache_file(self.cache_path)
        else:
            logger.debug('No unsaved cache changes to save to file.')

    def add_agent(self, agent):
        """
        Добавляет агента в симуляцию.

        :param agent: Объект агента.
        """
        if agent.name in self.name_to_agent:
            raise ValueError(f'Agent names must be unique, but \'{agent.name}\' is already defined.')
        agent.simulation_id = self.id
        self.agents.append(agent)
        self.name_to_agent[agent.name] = agent

    def add_environment(self, environment):
        """
        Добавляет окружение в симуляцию.

        :param environment: Объект окружения.
        """
        if environment.name in self.name_to_environment:
            raise ValueError(f'Environment names must be unique, but \'{environment.name}\' is already defined.')
        environment.simulation_id = self.id
        self.environments.append(environment)
        self.name_to_environment[environment.name] = environment

    def add_factory(self, factory):
        """
        Добавляет фабрику в симуляцию.

        :param factory: Объект фабрики.
        """
        if factory.name in self.name_to_factory:
            raise ValueError(f'Factory names must be unique, but \'{factory.name}\' is already defined.')
        factory.simulation_id = self.id
        self.factories.append(factory)
        self.name_to_factory[factory.name] = factory

    ###################################################################################################
    # Механизмы кэширования и цепочки выполнения
    ###################################################################################################
    def _execution_trace_position(self) -> int:
        """
        Возвращает текущую позицию в трассировке выполнения, или -1, если трассировка пуста.
        """
        return len(self.execution_trace) - 1

    def _function_call_hash(self, function_name, *args, **kwargs) -> int:
        """
        Вычисляет хеш вызова функции.

        :param function_name: Имя функции.
        :param args: Аргументы функции.
        :param kwargs: Ключевые аргументы функции.
        :return: Хеш вызова функции.
        """
        event = str((function_name, args, kwargs))
        return utils.custom_hash(event) # TODO проверить, почему тут не используется хеш

    def _skip_execution_with_cache(self):
        """
        Пропускает текущее выполнение, если в кэше есть состояние в текущей позиции.
        """
        assert len(self.cached_trace) > self._execution_trace_position() + 1, 'There\'s no cached state at the current execution position.'

        self.execution_trace.append(self.cached_trace[self._execution_trace_position() + 1])

    def _is_transaction_event_cached(self, event_hash) -> bool:
        """
        Проверяет, совпадает ли хеш события с кэшированным, если он есть.

        :param event_hash: Хеш события.
        :return: True, если событие кэшировано или нет кэша, иначе False.
        """
        #  есть кэш, который можно использовать
        if len(self.cached_trace) > self._execution_trace_position() + 1:
            if self._execution_trace_position() >= -1:
                # тут логика:
                #
                # Cache:         c0:(c_prev_node_hash_0, c_event_hash_0, _,  c_state_0) ------------------> c1:(c_prev_node_hash_1, c_event_hash_1,  _,  c_state_1) -> ...
                # Execution:     e0:(e_prev_node_hash_0, e_event_hash_0, _,  e_state_0) -<вычисляется>-> e1:(e_prev_node_hash_1, <вычисляется>, <вычисляется>, <вычисляется>)
                #   position = 0 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                #
                #   Должно выполняться:
                #     - event_hash == c_event_hash_1
                #     - hash(e0) == c_prev_node_hash_1
                event_hash_match = event_hash == self.cached_trace[self._execution_trace_position() + 1][1]
                prev_node_match = True

                return event_hash_match and prev_node_match

            else:
                raise ValueError('Execution trace position is invalid, must be >= -1, but is ', self._execution_trace_position())

        else:  # нет кэша для использования
            return False

    def _drop_cached_trace_suffix(self):
        """
        Удаляет суффикс кэшированной трассировки, начиная с текущей позиции.
        Обновляет кэш до текущего состояния выполнения и начинает строить новый кэш.
        """
        self.cached_trace = self.cached_trace[:self._execution_trace_position() + 1]

    def _add_to_execution_trace(self, state: dict, event_hash: int, event_output):
        """
        Добавляет состояние в трассировку выполнения.

        :param state: Состояние симуляции.
        :param event_hash: Хеш события.
        :param event_output: Вывод события.
        """

        # Вычисляем хеш предыдущей пары выполнения, если есть
        previous_hash = None

        # Создаем кортеж (hash, state) и добавляем его в список execution_trace
        self.execution_trace.append((previous_hash, event_hash, event_output, state))

    def _add_to_cache_trace(self, state: dict, event_hash: int, event_output):
        """
        Добавляет состояние в кэшированную трассировку.

        :param state: Состояние симуляции.
        :param event_hash: Хеш события.
         :param event_output: Вывод события.
        """
        # Вычисляем хеш предыдущей кэшированной пары, если есть
        previous_hash = None
        if self.cached_trace:
            previous_hash = utils.custom_hash(self.cached_trace[-1])

        # Создаем кортеж (hash, state) и добавляем его в список cached_trace
        self.cached_trace.append((previous_hash, event_hash, event_output, state))

        self.has_unsaved_cache_changes = True

    def _load_cache_file(self, cache_path: str):
        """
        Загружает кэш из файла.

        :param cache_path: Путь к файлу кэша.
        """
        try:
            # self.cached_trace = json.load(open(cache_path, 'r')) # TODO использовать j_loads
            with open(cache_path, 'r') as f:
                self.cached_trace = j_loads(f)
        except FileNotFoundError:
            logger.info(f'Cache file not found on path: {cache_path}.')
            self.cached_trace = []

    def _save_cache_file(self, cache_path: str):
        """
        Сохраняет кэш в файл.

        :param cache_path: Путь к файлу кэша.
        """
        try:
            # Создаем временный файл
            with tempfile.NamedTemporaryFile('w', delete=False) as temp:
                # json.dump(self.cached_trace, temp, indent=4) # TODO использовать j_dumps
                import json
                json.dump(self.cached_trace, temp, indent=4)

            # Заменяем исходный файл временным файлом
            os.replace(temp.name, cache_path)
        except Exception as e:
            logger.error(f'An error occurred: {e}', exc_info=True) # TODO тут не используется логгер

        self.has_unsaved_cache_changes = False

    ###################################################################################################
    # Управление транзакциями
    ###################################################################################################

    def begin_transaction(self):
        """
        Начинает транзакцию.
        """
        self._under_transaction = True
        self._clear_communications_buffers()

    def end_transaction(self):
        """
        Завершает транзакцию.
        """
        self._under_transaction = False

    def is_under_transaction(self) -> bool:
        """
        Проверяет, выполняется ли транзакция.
        """
        return self._under_transaction

    def _clear_communications_buffers(self):
        """
        Очищает буферы сообщений всех агентов и окружений.
        """
        for agent in self.agents:
            agent.clear_communications_buffer()

        for environment in self.environments:
            environment.clear_communications_buffer()
    ###################################################################################################
    # Обработка состояния симуляции
    ###################################################################################################

    def _encode_simulation_state(self) -> dict:
        """
        Кодирует текущее состояние симуляции, включая агентов, окружения и т.д.

        :return: Словарь, представляющий состояние симуляции.
        """
        state = {}

        # Кодируем агентов
        state['agents'] = []
        for agent in self.agents:
            state['agents'].append(agent.encode_complete_state())

        # Кодируем окружения
        state['environments'] = []
        for environment in self.environments:
            state['environments'].append(environment.encode_complete_state())

        # Кодируем фабрики
        state['factories'] = []
        for factory in self.factories:
            state['factories'].append(factory.encode_complete_state())

        return state

    def _decode_simulation_state(self, state: dict):
        """
        Декодирует состояние симуляции, включая агентов, окружения и т.д.

        :param state: Словарь, представляющий состояние симуляции.
        """

        logger.debug(f'Decoding simulation state: {state["factories"]}')
        logger.debug(f'Registered factories: {self.name_to_factory}')
        logger.debug(f'Registered agents: {self.name_to_agent}')
        logger.debug(f'Registered environments: {self.name_to_environment}')

        # Декодируем фабрики
        for factory_state in state['factories']:
            factory = self.name_to_factory[factory_state['name']]
            factory.decode_complete_state(factory_state)

        # Декодируем окружения
        # self.environments = [] # TODO удалить, т.к. не используется
        for environment_state in state['environments']:
            try:
                environment = self.name_to_environment[environment_state['name']]
                environment.decode_complete_state(environment_state)
                if TinyWorld.communication_display:
                    environment.pop_and_display_latest_communications()

            except Exception as e:
                raise ValueError(f'Environment {environment_state["name"]} is not in the simulation, thus cannot be decoded there.') from e

        # Декодируем агентов (если они не были декодированы окружением)
        # self.agents = [] # TODO удалить, т.к. не используется
        for agent_state in state['agents']:
            try:
                agent = self.name_to_agent[agent_state['name']]
                agent.decode_complete_state(agent_state)

                # Агент еще не декодирован, поскольку не находится ни в каком окружении. Декодируем его.
                if agent.environment is None:
                    if TinyPerson.communication_display:
                        agent.pop_and_display_latest_communications()
            except Exception as e:
                raise ValueError(f'Agent {agent_state["name"]} is not in the simulation, thus cannot be decoded there.') from e


class Transaction:
    """
    Управляет выполнением транзакций в симуляции.
    """
    def __init__(self, obj_under_transaction, simulation, function, *args, **kwargs):
        """
        Инициализирует объект транзакции.

        :param obj_under_transaction: Объект, участвующий в транзакции.
        :param simulation: Объект симуляции.
        :param function: Функция для выполнения.
        :param args: Позиционные аргументы функции.
        :param kwargs: Именованные аргументы функции.
        """
        self.obj_under_transaction = obj_under_transaction
        self.simulation = simulation
        self.function_name = function.__name__
        self.function = function
        self.args = args
        self.kwargs = kwargs

        # Если симуляция запущена, устанавливаем id симуляции объекта
        if simulation is not None:
            if hasattr(obj_under_transaction, 'simulation_id') and obj_under_transaction.simulation_id is not None:
                if obj_under_transaction.simulation_id != simulation.id:
                    raise ValueError(f'Object {obj_under_transaction} is already captured by a different simulation (id={obj_under_transaction.simulation_id}), \
                                    and cannot be captured by simulation id={simulation.id}.')

                logger.debug(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Object {obj_under_transaction} is already captured by simulation {simulation.id}.')
            else:
                # Если это TinyPerson, добавляем агента в симуляцию
                if isinstance(obj_under_transaction, TinyPerson):
                    simulation.add_agent(obj_under_transaction)
                    logger.debug(f'>>>>>>>>>>>>>>>>>>>>>>>>> Added agent {obj_under_transaction} to simulation {simulation.id}.')

                # Если это TinyWorld, добавляем окружение в симуляцию
                elif isinstance(obj_under_transaction, TinyWorld):
                    simulation.add_environment(obj_under_transaction)

                # Если это TinyFactory, добавляем фабрику в симуляцию
                elif isinstance(obj_under_transaction, TinyFactory):
                    simulation.add_factory(obj_under_transaction)
                    logger.debug(f'>>>>>>>>>>>>>>>>>>>>>>>>> Added factory {obj_under_transaction} to simulation {simulation.id}.')

                else:
                    raise ValueError(f'Object {obj_under_transaction} (type = {type(obj_under_transaction)}) is not a TinyPerson or TinyWorld instance, and cannot be captured by the simulation.')

    def execute(self):
        """
        Выполняет транзакцию.

        :return: Результат выполнения функции.
        """
        output = None

        # Кэширование транзакций работает только если есть симуляция и она запущена
        if self.simulation is None or self.simulation.status == Simulation.STATUS_STOPPED:
            # Вычисляем функцию и возвращаем результат, кэширование не производится, т.к. симуляция не запущена
            output = self.function(*self.args, **self.kwargs)

        elif self.simulation.status == Simulation.STATUS_STARTED:
            # Вычисляем хеш события
            event_hash = self.simulation._function_call_hash(self.function_name, *self.args, **self.kwargs)

            # Проверяем, есть ли хеш события в кэше
            if self.simulation._is_transaction_event_cached(event_hash):
                # Восстанавливаем полное состояние и возвращаем кэшированный вывод
                logger.info(f'Skipping execution of {self.function_name} with args {self.args} and kwargs {self.kwargs} because it is already cached.')

                self.simulation._skip_execution_with_cache()
                state = self.simulation.cached_trace[self.simulation._execution_trace_position()][3]  # state
                self.simulation._decode_simulation_state(state)

                # Кодирование/декодирование вывода используется для сохранения ссылок на TinyPerson и TinyWorld,
                # в основном. Скалярные значения и составные значения кодируются/декодируются как есть.
                encoded_output = self.simulation.cached_trace[self.simulation._execution_trace_position()][2]  # output
                output = self._decode_function_output(encoded_output)

            else:  # не кэшировано

                # повторные транзакции не кэшируются, т.к. важен конечный результат
                if not self.simulation.is_under_transaction():
                    self.simulation.begin_transaction()

                    # немедленно удаляем суффикс кэшированной трассировки
                    self.simulation._drop_cached_trace_suffix()

                    # Вычисляем функцию, кэшируем результат и возвращаем его
                    output = self.function(*self.args, **self.kwargs)

                    encoded_output = self._encode_function_output(output)
                    state = self.simulation._encode_simulation_state()

                    self.simulation._add_to_cache_trace(state, event_hash, encoded_output)
                    self.simulation._add_to_execution_trace(state, event_hash, encoded_output)

                    self.simulation.end_transaction()

                else:  # повторные транзакции просто выполняются, но не кэшируются
                    output = self.function(*self.args, **self.kwargs)
        else:
            raise ValueError(f'Simulation status is invalid at this point: {self.simulation.status}')

        # Сохраняем состояние, если нужно
        if self.simulation is not None and self.simulation.auto_checkpoint:
            self.simulation.checkpoint()

        return output

    def _encode_function_output(self, output) -> dict:
        """
        Кодирует вывод функции.

        :param output: Вывод функции.
        :return: Словарь, представляющий закодированный вывод.
        """
        # Если вывод - TinyPerson, кодируем его
        if output is None:
            return None
        elif isinstance(output, TinyPerson):
            return {'type': 'TinyPersonRef', 'name': output.name}
        # Если вывод - TinyWorld, кодируем его
        elif isinstance(output, TinyWorld):
            return {'type': 'TinyWorldRef', 'name': output.name}
        # Если вывод - TinyFactory, кодируем его
        elif isinstance(output, TinyFactory):
            return {'type': 'TinyFactoryRef', 'name': output.name}
        # Если это один из типов, поддерживаемых JSON, кодируем как есть
        elif isinstance(output, (int, float, str, bool, list, dict, tuple)):
            return {'type': 'JSON', 'value': output}
        # Иначе, выбрасываем исключение
        else:
            raise ValueError(f'Unsupported output type: {type(output)}')

    def _decode_function_output(self, encoded_output: dict):
        """
        Декодирует закодированный вывод функции.

        :param encoded_output: Словарь, представляющий закодированный вывод.
        :return: Декодированный вывод функции.
        """
        if encoded_output is None:
            return None
        elif encoded_output['type'] == 'TinyPersonRef':
            return TinyPerson.get_agent_by_name(encoded_output['name'])
        elif encoded_output['type'] == 'TinyWorldRef':
            return TinyWorld.get_environment_by_name(encoded_output['name'])
        elif encoded_output['type'] == 'TinyFactoryRef':
            return TinyFactory.get_factory_by_name(encoded_output['name'])
        elif encoded_output['type'] == 'JSON':
            return encoded_output['value']
        else:
            raise ValueError(f'Unsupported output type: {encoded_output["type"]}')

def transactional(func):
    """
    Декоратор, делающий функцию транзакционной в рамках симуляции.

    :param func: Функция, которую нужно сделать транзакционной.
    :return: Обернутая функция.
    """
    def wrapper(*args, **kwargs):
        obj_under_transaction = args[0]
        simulation = current_simulation()
        obj_sim_id = obj_under_transaction.simulation_id if hasattr(obj_under_transaction, 'simulation_id') else None

        logger.debug(f'-----------------------------------------> Transaction: {func.__name__} with args {args[1:]} and kwargs {kwargs} under simulation {obj_sim_id}.')

        transaction = Transaction(obj_under_transaction, simulation, func, *args, **kwargs)
        result = transaction.execute()
        return result

    return wrapper

class SkipTransaction(Exception):
    """
    Исключение для пропуска транзакции.
    """
    pass

class CacheOutOfSync(Exception):
    """
    Исключение, если кэш и выполненные элементы рассинхронизированы.
    """
    pass

class ExecutionCached(Exception):
    """
    Исключение, если предложенное выполнение уже кэшировано.
    """
    pass

###################################################################################################
# Вспомогательные функции
###################################################################################################

_current_simulations = {'default': None}
_current_simulation_id = None

def reset():
    """
    Сбрасывает состояние управления симуляцией.
    """
    global _current_simulations, _current_simulation_id
    _current_simulations = {'default': None}

    # TODO В настоящее время одновременно можно запустить только одну симуляцию.
    #      В будущих версиях это должно быть изменено, чтобы можно было запускать несколько симуляций
    #      одновременно, например, для быстрого анализа посредством параллелизации.
    _current_simulation_id = None

def _simulation(id='default'):
    """
    Возвращает симуляцию по id.
    """
    global _current_simulations
    if _current_simulations[id] is None:
        _current_simulations[id] = Simulation(id=id)

    return _current_simulations[id]

def begin(cache_path=None, id='default', auto_checkpoint=False):
    """
    Начинает управляемую симуляцию.
    """
    global _current_simulation_id
    if _current_simulation_id is None:
        _simulation(id).begin(cache_path, auto_checkpoint)
        _current_simulation_id = id
    else:
        raise ValueError(f'Simulation is already started under id {_current_simulation_id}. Currently only one simulation can be started at a time.')

def end(id='default'):
    """
    Завершает управляемую симуляцию.
    """
    global _current_simulation_id
    _simulation(id).end()
    _current_simulation_id = None

def checkpoint(id='default'):
    """
    Сохраняет текущее состояние симуляции.
    """
    _simulation(id).checkpoint()

def current_simulation():
    """
    Возвращает текущую симуляцию.
    """
    global _current_simulation_id
    if _current_simulation_id is not None:
        return _simulation(_current_simulation_id)
    else:
        return None

reset()  # инициализация состояния управления