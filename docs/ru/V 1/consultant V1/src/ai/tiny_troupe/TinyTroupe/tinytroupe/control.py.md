### Анализ кода модуля `control`

**Качество кода**:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код хорошо структурирован, разделен на классы и функции, что облегчает понимание и поддержку.
    - Присутствует базовая обработка ошибок через исключения.
    - Реализована логика для кэширования и транзакций.
- **Минусы**:
    - Используется `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Логгер импортируется из `logging`, а не из `src.logger.logger`.
    - Некоторые комментарии не соответствуют стандарту RST.
    - Присутствуют неясные комментарии, такие как "получаем", "делаем".
    - Избыточное использование блоков try-except, лучше использовать logger.error для обработки ошибок.
    - Не везде используется f-строки, где это возможно.
    - Используются двойные кавычки в коде, где должны быть одинарные.
    - Не хватает RST-документации для функций и классов.

**Рекомендации по улучшению**:
- Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
- Импортировать `logger` из `src.logger.logger`.
- Добавить RST-документацию для всех функций и классов, включая описание параметров, возвращаемых значений и исключений.
- Пересмотреть комментарии, сделав их более точными и информативными.
- Уменьшить использование блоков `try-except` и использовать `logger.error` для обработки ошибок.
- Использовать f-строки для форматирования строк, где это уместно.
- Использовать одинарные кавычки в коде, где это необходимо.
- Привести код в соответствие со стандартами PEP8 для улучшения читаемости.

**Оптимизированный код**:
```python
"""
Модуль для управления симуляциями.
====================================

Модуль содержит классы и функции для управления симуляциями,
включая управление агентами, средами, фабриками, а также механизмами
кэширования и транзакций.

Пример использования
----------------------
.. code-block:: python

    simulation = Simulation(id='my_simulation')
    simulation.begin()
    # ... действия в симуляции ...
    simulation.end()
"""
import os
import tempfile
from pathlib import Path

from src.logger.logger import logger  # Импорт logger из src.logger.logger
import tinytroupe
import tinytroupe.utils as utils
from src.utils.jjson import j_loads  # Используем j_loads из src.utils.jjson


class Simulation:
    """
    Класс для управления симуляциями.

    :ivar STATUS_STOPPED: Статус остановленной симуляции.
    :vartype STATUS_STOPPED: str
    :ivar STATUS_STARTED: Статус запущенной симуляции.
    :vartype STATUS_STARTED: str
    :ivar id: Идентификатор симуляции.
    :vartype id: str
    :ivar agents: Список агентов в симуляции.
    :vartype agents: list
    :ivar name_to_agent: Словарь для быстрого доступа к агентам по имени.
    :vartype name_to_agent: dict
    :ivar environments: Список сред в симуляции.
    :vartype environments: list
    :ivar factories: Список фабрик в симуляции.
    :vartype factories: list
    :ivar name_to_factory: Словарь для быстрого доступа к фабрикам по имени.
    :vartype name_to_factory: dict
    :ivar name_to_environment: Словарь для быстрого доступа к средам по имени.
    :vartype name_to_environment: dict
    :ivar status: Текущий статус симуляции.
    :vartype status: str
    :ivar cache_path: Путь к файлу кэша.
    :vartype cache_path: str
    :ivar auto_checkpoint: Флаг автоматического сохранения после каждой транзакции.
    :vartype auto_checkpoint: bool
    :ivar has_unsaved_cache_changes: Флаг наличия несохраненных изменений в кэше.
    :vartype has_unsaved_cache_changes: bool
    :ivar _under_transaction: Флаг нахождения в транзакции.
    :vartype _under_transaction: bool
    :ivar cached_trace: Список состояний симуляции из кэша.
    :vartype cached_trace: list
    :ivar execution_trace: Список состояний симуляции во время выполнения.
    :vartype execution_trace: list
    """

    STATUS_STOPPED = 'stopped'
    STATUS_STARTED = 'started'

    def __init__(self, id='default', cached_trace: list = None):
        """
        Инициализирует объект симуляции.

        :param id: Идентификатор симуляции.
        :type id: str, optional
        :param cached_trace: Кэшированный след симуляции.
        :type cached_trace: list, optional
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

        # should we always automatically checkpoint at the every transaction?
        self.auto_checkpoint = False

        # whether there are changes not yet saved to the cache file
        self.has_unsaved_cache_changes = False

        # whether the agent is under a transaction or not, used for managing
        # simulation caching later
        self._under_transaction = False

        # Cache chain mechanism.
        #
        # stores a list of simulation states.
        # Each state is a tuple (prev_node_hash, event_hash, event_output, state), where prev_node_hash is a hash of the previous node in this chain,
        # if any, event_hash is a hash of the event that triggered the transition to this state, if any, event_output is the output of the event,
        # if any, and state is the actual complete state that resulted.
        if cached_trace is None:
            self.cached_trace = []
        else:
            self.cached_trace = cached_trace

        # Execution chain mechanism.
        #
        # The actual, current, execution trace. Each state is a tuple (prev_node_hash, event_hash, state), where prev_node_hash is a hash
        # of the previous node in this chain, if any, event_hash is a hash of the event that triggered the transition to this state, if any,
        # event_output is the output of the event, if any, and state is the actual complete state that resulted.
        self.execution_trace = []

    def begin(self, cache_path: str = None, auto_checkpoint: bool = False):
        """
        Отмечает начало управляемой симуляции.

        :param cache_path: Путь к файлу кэша. Если не указан, используется путь по умолчанию, определенный в классе.
        :type cache_path: str, optional
        :param auto_checkpoint: Флаг автоматического создания чекпоинта в конце каждой транзакции. Значение по умолчанию - False.
        :type auto_checkpoint: bool, optional
        :raises ValueError: Если симуляция уже запущена.
        """
        # local import to avoid circular dependencies
        from tinytroupe.agent import TinyPerson
        from tinytroupe.environment import TinyWorld
        from tinytroupe.factory import TinyFactory

        if self.status == Simulation.STATUS_STOPPED:
            self.status = Simulation.STATUS_STARTED
        else:
            raise ValueError('Simulation is already started.')

        if cache_path is not None:
            self.cache_path = cache_path

        # should we automatically checkpoint?
        self.auto_checkpoint = auto_checkpoint

        # clear the agents, environments and other simulated entities, we'll track them from now on
        TinyPerson.clear_agents()
        TinyWorld.clear_environments()
        TinyFactory.clear_factories()

        # All automated fresh ids will start from 0 again for this simulation
        utils._fresh_id_counter = 0

        # load the cache file, if any
        if self.cache_path is not None:
            self._load_cache_file(self.cache_path)

    def end(self):
        """
        Отмечает конец управляемой симуляции.

        :raises ValueError: Если симуляция уже остановлена.
        """
        if self.status == Simulation.STATUS_STARTED:
            self.status = Simulation.STATUS_STOPPED
            self.checkpoint()
        else:
            raise ValueError('Simulation is already stopped.')

    def checkpoint(self):
        """
        Сохраняет текущий след симуляции в файл.
        """
        # save the cache file
        if self.has_unsaved_cache_changes:
            self._save_cache_file(self.cache_path)
        else:
            logger.debug('No unsaved cache changes to save to file.')

    def add_agent(self, agent):
        """
        Добавляет агента в симуляцию.

        :param agent: Объект агента для добавления.
        :type agent: TinyPerson
        :raises ValueError: Если имя агента не уникально.
        """
        if agent.name in self.name_to_agent:
            raise ValueError(f'Agent names must be unique, but \'{agent.name}\' is already defined.')
        agent.simulation_id = self.id
        self.agents.append(agent)
        self.name_to_agent[agent.name] = agent

    def add_environment(self, environment):
        """
        Добавляет среду в симуляцию.

        :param environment: Объект среды для добавления.
        :type environment: TinyWorld
        :raises ValueError: Если имя среды не уникально.
        """
        if environment.name in self.name_to_environment:
            raise ValueError(f'Environment names must be unique, but \'{environment.name}\' is already defined.')
        environment.simulation_id = self.id
        self.environments.append(environment)
        self.name_to_environment[environment.name] = environment

    def add_factory(self, factory):
        """
        Добавляет фабрику в симуляцию.

        :param factory: Объект фабрики для добавления.
        :type factory: TinyFactory
        :raises ValueError: Если имя фабрики не уникально.
        """
        if factory.name in self.name_to_factory:
            raise ValueError(f'Factory names must be unique, but \'{factory.name}\' is already defined.')
        factory.simulation_id = self.id
        self.factories.append(factory)
        self.name_to_factory[factory.name] = factory

    ###################################################################################################
    # Cache and execution chain mechanisms
    ###################################################################################################
    def _execution_trace_position(self) -> int:
        """
        Возвращает текущую позицию в следе выполнения или -1, если след выполнения пуст.

        :return: Текущая позиция в следе выполнения.
        :rtype: int
        """
        return len(self.execution_trace) - 1

    def _function_call_hash(self, function_name, *args, **kwargs) -> int:
        """
        Вычисляет хэш вызова заданной функции.

        :param function_name: Имя функции.
        :type function_name: str
        :param args: Позиционные аргументы функции.
        :type args: tuple
        :param kwargs: Именованные аргументы функции.
        :type kwargs: dict
        :return: Хэш вызова функции.
        :rtype: int
        """
        event = str((function_name, args, kwargs))
        return event

    def _skip_execution_with_cache(self):
        """
        Пропускает текущее выполнение, предполагая наличие кэшированного состояния в той же позиции.
        
        :raises AssertionError: Если кэшированное состояние отсутствует в текущей позиции выполнения.
        """
        assert len(self.cached_trace) > self._execution_trace_position() + 1, 'There\'s no cached state at the current execution position.'

        self.execution_trace.append(self.cached_trace[self._execution_trace_position() + 1])

    def _is_transaction_event_cached(self, event_hash) -> bool:
        """
        Проверяет, соответствует ли заданный хэш события соответствующему кэшированному, если таковой имеется.
        Если соответствующего кэшированного состояния нет, возвращает True.

        :param event_hash: Хэш события для проверки.
        :type event_hash: int
        :return: True, если хэш события соответствует кэшированному, иначе False.
        :rtype: bool
        :raises ValueError: Если позиция выполнения является недопустимой.
        """
        # there's cache that could be used
        if len(self.cached_trace) > self._execution_trace_position() + 1:
            if self._execution_trace_position() >= -1:
                # here's a graphical depiction of the logic:
                #
                # Cache:         c0:(c_prev_node_hash_0, c_event_hash_0, _,  c_state_0) ------------------> c1:(c_prev_node_hash_1, c_event_hash_1,  _,  c_state_1) -> ...
                # Execution:     e0:(e_prev_node_hash_0, e_event_hash_0, _,  e_state_0) -<being computed>-> e1:(e_prev_node_hash_1, <being computed>, <being computed>, <being computed>)
                #   position = 0 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                #
                #   Must satisfy:
                #     - event_hash == c_event_hash_1
                #     - hash(e0) == c_prev_node_hash_1
                event_hash_match = event_hash == self.cached_trace[self._execution_trace_position() + 1][1]
                prev_node_match = True

                return event_hash_match and prev_node_match

            else:
                raise ValueError('Execution trace position is invalid, must be >= -1, but is ', self._execution_trace_position())

        else:  # no cache to use
            return False

    def _drop_cached_trace_suffix(self):
        """
        Удаляет суффикс кэшированного следа, начиная с текущей позиции следа выполнения.
        Это эффективно обновляет кэш до текущего состояния выполнения и начинает строить новый кэш с этого момента.
        """
        self.cached_trace = self.cached_trace[:self._execution_trace_position() + 1]

    def _add_to_execution_trace(self, state: dict, event_hash: int, event_output):
        """
        Добавляет состояние в список execution_trace и вычисляет соответствующий хэш.
        Вычисленный хэш сравнивается с хэшем кэшированного следа в той же позиции,
        и если они не совпадают, выполнение прерывается. Аналогично, event_hash сравнивается
        с хэшем события в кэшированном следе в той же позиции, и если они не совпадают, выполнение
        прерывается.

        :param state: Текущее состояние симуляции.
        :type state: dict
        :param event_hash: Хэш события, вызвавшего переход в это состояние.
        :type event_hash: int
        :param event_output: Выходные данные события.
        :type event_output: any
        """

        # Compute the hash of the previous execution pair, if any
        previous_hash = None

        # Create a tuple of (hash, state) and append it to the execution_trace list
        self.execution_trace.append((previous_hash, event_hash, event_output, state))

    def _add_to_cache_trace(self, state: dict, event_hash: int, event_output):
        """
        Добавляет состояние в список cached_trace и вычисляет соответствующий хэш.

        :param state: Текущее состояние симуляции.
        :type state: dict
        :param event_hash: Хэш события, вызвавшего переход в это состояние.
        :type event_hash: int
        :param event_output: Выходные данные события.
        :type event_output: any
        """
        # Compute the hash of the previous cached pair, if any
        previous_hash = None
        if self.cached_trace:
            previous_hash = utils.custom_hash(self.cached_trace[-1])

        # Create a tuple of (hash, state) and append it to the cached_trace list
        self.cached_trace.append((previous_hash, event_hash, event_output, state))

        self.has_unsaved_cache_changes = True

    def _load_cache_file(self, cache_path: str):
        """
        Загружает файл кэша по заданному пути.

        :param cache_path: Путь к файлу кэша.
        :type cache_path: str
        """
        try:
            with open(cache_path, 'r') as f:
                self.cached_trace = j_loads(f)  # Используем j_loads
        except FileNotFoundError:
            logger.info(f'Cache file not found on path: {cache_path}.')
            self.cached_trace = []
        except Exception as e:  # Добавлена общая обработка исключений для j_loads
            logger.error(f"Error loading cache file from {cache_path}: {e}")
            self.cached_trace = []

    def _save_cache_file(self, cache_path: str):
        """
        Сохраняет файл кэша по заданному пути. Всегда перезаписывает.

        :param cache_path: Путь к файлу кэша.
        :type cache_path: str
        """
        try:
            # Create a temporary file
            with tempfile.NamedTemporaryFile('w', delete=False) as temp:
                # TODO: replace with j_dumps
                import json
                json.dump(self.cached_trace, temp, indent=4)

            # Replace the original file with the temporary file
            os.replace(temp.name, cache_path)
        except Exception as e:
            logger.error(f"An error occurred while saving cache file: {e}")  # Используем logger.error

        self.has_unsaved_cache_changes = False

    ###################################################################################################
    # Transactional control
    ###################################################################################################

    def begin_transaction(self):
        """
        Начинает транзакцию.
        """
        self._under_transaction = True
        self._clear_communications_buffers()  # TODO <----------------------------------------------------------------

    def end_transaction(self):
        """
        Завершает транзакцию.
        """
        self._under_transaction = False

    def is_under_transaction(self):
        """
        Проверяет, находится ли агент в транзакции.

        :return: True, если агент в транзакции, иначе False.
        :rtype: bool
        """
        return self._under_transaction

    def _clear_communications_buffers(self):
        """
        Очищает буферы связи всех агентов и сред.
        """
        for agent in self.agents:
            agent.clear_communications_buffer()

        for environment in self.environments:
            environment.clear_communications_buffer()
    ###################################################################################################
    # Simulation state handling
    ###################################################################################################

    def _encode_simulation_state(self) -> dict:
        """
        Кодирует текущее состояние симуляции, включая агентов, среды и другую
        соответствующую информацию.

        :return: Словарь с закодированным состоянием симуляции.
        :rtype: dict
        """
        state = {}

        # Encode agents
        state['agents'] = []
        for agent in self.agents:
            state['agents'].append(agent.encode_complete_state())

        # Encode environments
        state['environments'] = []
        for environment in self.environments:
            state['environments'].append(environment.encode_complete_state())

        # Encode factories
        state['factories'] = []
        for factory in self.factories:
            state['factories'].append(factory.encode_complete_state())

        return state

    def _decode_simulation_state(self, state: dict):
        """
        Декодирует заданное состояние симуляции, включая агентов, среды и другую
        соответствующую информацию.

        :param state: Состояние для декодирования.
        :type state: dict
        :raises ValueError: Если среда или агент не найдены в симуляции.
        """
        # local import to avoid circular dependencies
        from tinytroupe.agent import TinyPerson
        from tinytroupe.environment import TinyWorld

        logger.debug(f'Decoding simulation state: {state["factories"]}')
        logger.debug(f'Registered factories: {self.name_to_factory}')
        logger.debug(f'Registered agents: {self.name_to_agent}')
        logger.debug(f'Registered environments: {self.name_to_environment}')

        # Decode factories
        for factory_state in state['factories']:
            factory = self.name_to_factory[factory_state['name']]
            factory.decode_complete_state(factory_state)

        # Decode environments
        for environment_state in state['environments']:
            try:
                environment = self.name_to_environment[environment_state['name']]
                environment.decode_complete_state(environment_state)
                if TinyWorld.communication_display:
                    environment.pop_and_display_latest_communications()

            except Exception as e:
                raise ValueError(f'Environment {environment_state["name"]} is not in the simulation, thus cannot be decoded there.') from e

        # Decode agents (if they were not already decoded by the environment)
        for agent_state in state['agents']:
            try:
                agent = self.name_to_agent[agent_state['name']]
                agent.decode_complete_state(agent_state)

                # The agent has not yet been decoded because it is not in any environment. So, decode it.
                if agent.environment is None:
                    if TinyPerson.communication_display:
                        agent.pop_and_display_latest_communications()
            except Exception as e:
                raise ValueError(f'Agent {agent_state["name"]} is not in the simulation, thus cannot be decoded there.') from e

class Transaction:
    """
    Класс для управления транзакциями в симуляции.

    :ivar obj_under_transaction: Объект, над которым выполняется транзакция.
    :vartype obj_under_transaction: object
    :ivar simulation: Объект симуляции, в которой выполняется транзакция.
    :vartype simulation: Simulation
    :ivar function_name: Имя функции, выполняемой в транзакции.
    :vartype function_name: str
    :ivar function: Функция, выполняемая в транзакции.
    :vartype function: callable
    :ivar args: Позиционные аргументы функции.
    :vartype args: tuple
    :ivar kwargs: Именованные аргументы функции.
    :vartype kwargs: dict
    """
    def __init__(self, obj_under_transaction, simulation, function, *args, **kwargs):
        """
        Инициализирует объект транзакции.

        :param obj_under_transaction: Объект, над которым выполняется транзакция.
        :type obj_under_transaction: object
        :param simulation: Объект симуляции, в которой выполняется транзакция.
        :type simulation: Simulation
        :param function: Функция, выполняемая в транзакции.
        :type function: callable
        :param args: Позиционные аргументы функции.
        :type args: tuple
        :param kwargs: Именованные аргументы функции.
        :type kwargs: dict
        :raises ValueError: Если объект уже захвачен другой симуляцией или не является TinyPerson, TinyWorld, TinyFactory
        """
        # local import to avoid circular dependencies
        from tinytroupe.agent import TinyPerson
        from tinytroupe.environment import TinyWorld
        from tinytroupe.factory import TinyFactory

        self.obj_under_transaction = obj_under_transaction
        self.simulation = simulation
        self.function_name = function.__name__
        self.function = function
        self.args = args
        self.kwargs = kwargs

        #
        # If we have an ongoing simulation, set the simulation id of the object under transaction if it is not already set.
        #
        if simulation is not None:
            if hasattr(obj_under_transaction, 'simulation_id') and obj_under_transaction.simulation_id is not None:
                if obj_under_transaction.simulation_id != simulation.id:
                    raise ValueError(f'Object {obj_under_transaction} is already captured by a different simulation (id={obj_under_transaction.simulation_id}), \
                                    and cannot be captured by simulation id={simulation.id}.')
                
                logger.debug(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Object {obj_under_transaction} is already captured by simulation {simulation.id}.')
            else:
                # if is a TinyPerson, add the agent to the simulation
                if isinstance(obj_under_transaction, TinyPerson):
                    simulation.add_agent(obj_under_transaction)
                    logger.debug(f'>>>>>>>>>>>>>>>>>>>>>> Added agent {obj_under_transaction} to simulation {simulation.id}.')

                # if is a TinyWorld, add the environment to the simulation
                elif isinstance(obj_under_transaction, TinyWorld):
                    simulation.add_environment(obj_under_transaction)
                
                # if is a TinyFactory, add the factory to the simulation
                elif isinstance(obj_under_transaction, TinyFactory):
                    simulation.add_factory(obj_under_transaction)
                    logger.debug(f'>>>>>>>>>>>>>>>>>>>>>> Added factory {obj_under_transaction} to simulation {simulation.id}.')

                else:
                    raise ValueError(f'Object {obj_under_transaction} (type = {type(obj_under_transaction)}) is not a TinyPerson or TinyWorld instance, and cannot be captured by the simulation.')

    def execute(self):
        """
        Выполняет транзакцию.

        :return: Результат выполнения функции транзакции.
        :rtype: any
        :raises ValueError: Если статус симуляции недопустим.
        """
        output = None

        # Transaction caching will only operate if there is a simulation and it is started
        if self.simulation is None or self.simulation.status == Simulation.STATUS_STOPPED:
            # Compute the function and return it, no caching, since the simulation is not started
            output = self.function(*self.args, **self.kwargs)

        elif self.simulation.status == Simulation.STATUS_STARTED:
            # Compute the event hash
            event_hash = self.simulation._function_call_hash(self.function_name, *self.args, **self.kwargs)

            # Check if the event hash is in the cache
            if self.simulation._is_transaction_event_cached(event_hash):
                # Restore the full state and return the cached output
                logger.info(f'Skipping execution of {self.function_name} with args {self.args} and kwargs {self.kwargs} because it is already cached.')

                self.simulation._skip_execution_with_cache()
                state = self.simulation.cached_trace[self.simulation._execution_trace_position()][3]  # state
                self.simulation._decode_simulation_state(state)

                # Output encoding/decoding is used to preserve references to TinyPerson and TinyWorld instances
                # mainly. Scalar values (int, float, str, bool) and composite values (list, dict) are
                # encoded/decoded as is.
                encoded_output = self.simulation.cached_trace[self.simulation._execution_trace_position()][2]  # output
                output = self._decode_function_output(encoded_output)

            else:  # not cached

                # reentrant transactions are not cached, since what matters is the final result of
                # the top-level transaction
                if not self.simulation.is_under_transaction():
                    self.simulation.begin_transaction()

                    # immediately drop the cached trace suffix, since we are starting a new execution from this point on
                    self.simulation._drop_cached_trace_suffix()

                    # Compute the function, cache the result and return it
                    output = self.function(*self.args, **self.kwargs)

                    encoded_output = self._encode_function_output(output)
                    state = self.simulation._encode_simulation_state()

                    self.simulation._add_to_cache_trace(state, event_hash, encoded_output)
                    self.simulation._add_to_execution_trace(state, event_hash, encoded_output)

                    self.simulation.end_transaction()

                else:  # reentrant transactions are just run, but not cached
                    output = self.function(*self.args, **self.kwargs)
        else:
            raise ValueError(f'Simulation status is invalid at this point: {self.simulation.status}')

        # Checkpoint if needed
        if self.simulation is not None and self.simulation.auto_checkpoint:
            self.simulation.checkpoint()

        return output

    def _encode_function_output(self, output) -> dict:
        """
        Кодирует заданный результат функции.

        :param output: Результат функции для кодирования.
        :type output: any
        :return: Словарь с закодированным результатом.
        :rtype: dict
        :raises ValueError: Если тип выходных данных не поддерживается.
        """
        # local import to avoid circular dependencies
        from tinytroupe.agent import TinyPerson
        from tinytroupe.environment import TinyWorld
        from tinytroupe.factory import TinyFactory

        # if the output is a TinyPerson, encode it
        if output is None:
            return None
        elif isinstance(output, TinyPerson):
            return {'type': 'TinyPersonRef', 'name': output.name}
        # if it is a TinyWorld, encode it
        elif isinstance(output, TinyWorld):
            return {'type': 'TinyWorldRef', 'name': output.name}
        # if it is a TinyFactory, encode it
        elif isinstance(output, TinyFactory):
            return {'type': 'TinyFactoryRef', 'name': output.name}
        # if it is one of the types supported by JSON, encode it as is
        elif isinstance(output, (int, float, str, bool, list, dict, tuple)):
            return {'type': 'JSON', 'value': output}
        # otherwise, raise an exception
        else:
            raise ValueError(f'Unsupported output type: {type(output)}')

    def _decode_function_output(self, encoded_output: dict):
        """
        Декодирует заданный закодированный результат функции.

        :param encoded_output: Словарь с закодированным результатом.
        :type encoded_output: dict
        :return: Декодированный результат.
        :rtype: any
        :raises ValueError: Если тип выходных данных не поддерживается.
        """
        # local import to avoid circular dependencies
        from tinytroupe.agent import TinyPerson
        from tinytroupe.environment import TinyWorld
        from tinytroupe.factory import TinyFactory

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
    Декоратор, делающий функцию транзакционной для симуляции.

    :param func: Функция, которую нужно сделать транзакционной.
    :type func: callable
    :return: Обернутая функция.
    :rtype: callable
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
    Исключение, которое можно использовать для пропуска транзакции.
    """
    pass

class CacheOutOfSync(Exception):
    """
    Исключение, возникающее, когда кэшированные и вновь выполненные элементы не синхронизированы.
    """
    pass

class ExecutionCached(Exception):
    """
    Исключение, возникающее, когда предложенное выполнение уже кэшировано.
    """
    pass

###################################################################################################
# Convenience functions
###################################################################################################

def reset():
    """
    Сбрасывает все состояние управления симуляцией.
    """
    global _current