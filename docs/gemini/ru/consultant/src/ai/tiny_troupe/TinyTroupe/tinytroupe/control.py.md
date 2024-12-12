# Анализ кода модуля tinytroupe.control

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разделен на логические блоки.
    - Используется кэширование для оптимизации повторных выполнений.
    - Реализована поддержка транзакций.
    - Добавлены механизмы для отслеживания выполнения и состояния симуляции.
    - Присутствует подробное логирование.
- Минусы
    -  Используется `json.load` вместо `j_loads` или `j_loads_ns`.
    -  В некоторых местах `try-except` используются избыточно.
    -  Не все функции и методы имеют docstring в формате RST.
    -  Некоторые переменные и функции не соответствуют стандартам именования.

**Рекомендации по улучшению**

1.  **Использование `j_loads`**: Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов.
2.  **Обработка ошибок**: Использовать `logger.error` для обработки ошибок вместо общих `try-except` блоков.
3.  **Документация**: Добавить docstring в формате RST для всех функций, методов и классов.
4.  **Импорты**: Добавить недостающие импорты.
5.  **Форматирование**: Привести код в соответствие со стандартом PEP8, включая пробелы и отступы.
6.  **Улучшение логирования**: Добавить более информативные сообщения в логи.
7.  **Избегать избыточных комментариев**: Убрать комментарии которые не несут смысловой нагрузки.
8.  **Транзакции**:  Использовать явные проверки для статуса транзакции и вызывать исключение в случае несоответствия.
9.  **Именование**: Привести имена переменных и функций к общему стилю.
10. **Избегать ненужных комментариев**: Убрать комментарии, которые не несут смысловой нагрузки и не поясняют код.

**Оптимизированный код**
```python
"""
Модуль для управления симуляциями.
=========================================================================================

Этот модуль предоставляет механизмы для управления симуляциями, включая
запуск, остановку, кэширование и отслеживание транзакций.
Он также содержит классы для представления симуляций и транзакций.

Пример использования
--------------------

Пример использования класса `Simulation`:

.. code-block:: python

    simulation = Simulation(id='test_sim')
    simulation.begin()
    # ... действия симуляции ...
    simulation.end()
"""
import os
import tempfile
from typing import Any, Dict, List, Optional, Tuple

from src.logger.logger import logger
import tinytroupe
import tinytroupe.utils as utils
from src.utils.jjson import j_loads

class Simulation:
    """
    Класс, представляющий симуляцию.

    Атрибуты:
        STATUS_STOPPED (str): Статус остановленной симуляции.
        STATUS_STARTED (str): Статус запущенной симуляции.
        id (str): Идентификатор симуляции.
        agents (list): Список агентов в симуляции.
        name_to_agent (dict): Словарь для поиска агентов по имени.
        environments (list): Список окружений в симуляции.
        factories (list): Список фабрик в симуляции.
        name_to_factory (dict): Словарь для поиска фабрик по имени.
        name_to_environment (dict): Словарь для поиска окружений по имени.
        status (str): Текущий статус симуляции.
        cache_path (str): Путь к файлу кэша.
        auto_checkpoint (bool): Флаг автоматического сохранения.
        has_unsaved_cache_changes (bool): Флаг наличия несохраненных изменений кэша.
        _under_transaction (bool): Флаг нахождения в транзакции.
        cached_trace (list): Список состояний симуляции из кэша.
        execution_trace (list): Список текущих состояний выполнения симуляции.
    """

    STATUS_STOPPED = 'stopped'
    STATUS_STARTED = 'started'

    def __init__(self, id: str = 'default', cached_trace: Optional[List[Tuple]] = None):
        """
        Инициализирует объект симуляции.

        :param id: Идентификатор симуляции, по умолчанию 'default'.
        :param cached_trace: Список кэшированных состояний, если есть.
        """
        self.id = id

        self.agents: List[Any] = []
        self.name_to_agent: Dict[str, Any] = {}  # {agent_name: agent, ...}

        self.environments: List[Any] = []

        self.factories: List[Any] = []  # e.g., TinyPersonFactory instances
        self.name_to_factory: Dict[str, Any] = {}  # {factory_name: factory, ...}

        self.name_to_environment: Dict[str, Any] = {}  # {environment_name: environment, ...}
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
            self.cached_trace: List[Tuple] = []
        else:
            self.cached_trace = cached_trace

        # Execution chain mechanism.
        #
        # The actual, current, execution trace. Each state is a tuple (prev_node_hash, event_hash, state), where prev_node_hash is a hash
        # of the previous node in this chain, if any, event_hash is a hash of the event that triggered the transition to this state, if any,
        # event_output is the output of the event, if any, and state is the actual complete state that resulted.
        self.execution_trace: List[Tuple] = []

    def begin(self, cache_path: Optional[str] = None, auto_checkpoint: bool = False):
        """
        Начинает управляемую симуляцию.

        :param cache_path: Путь к файлу кэша, если нужно использовать нестандартный путь.
        :param auto_checkpoint: Флаг автоматического сохранения состояния.
        """
        # local import to avoid circular dependencies
        from tinytroupe.agent import TinyPerson
        from tinytroupe.environment import TinyWorld
        from tinytroupe.factory import TinyFactory

        if self.status == Simulation.STATUS_STOPPED:
            self.status = Simulation.STATUS_STARTED
        else:
            raise ValueError('Симуляция уже запущена.')

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
        Завершает управляемую симуляцию.
        """
        if self.status == Simulation.STATUS_STARTED:
            self.status = Simulation.STATUS_STOPPED
            self.checkpoint()
        else:
            raise ValueError('Симуляция уже остановлена.')

    def checkpoint(self):
        """
        Сохраняет текущее состояние симуляции в файл.
        """
        # save the cache file
        if self.has_unsaved_cache_changes:
            self._save_cache_file(self.cache_path)
        else:
            logger.debug('Нет несохраненных изменений кэша для сохранения в файл.')

    def add_agent(self, agent: Any):
        """
        Добавляет агента в симуляцию.

        :param agent: Агент для добавления.
        """
        if agent.name in self.name_to_agent:
            raise ValueError(f'Имена агентов должны быть уникальными, но \'{agent.name}\' уже определено.')
        agent.simulation_id = self.id
        self.agents.append(agent)
        self.name_to_agent[agent.name] = agent

    def add_environment(self, environment: Any):
        """
        Добавляет окружение в симуляцию.

        :param environment: Окружение для добавления.
        """
        if environment.name in self.name_to_environment:
            raise ValueError(
                f'Имена окружений должны быть уникальными, но \'{environment.name}\' уже определено.')
        environment.simulation_id = self.id
        self.environments.append(environment)
        self.name_to_environment[environment.name] = environment

    def add_factory(self, factory: Any):
        """
        Добавляет фабрику в симуляцию.

        :param factory: Фабрика для добавления.
        """
        if factory.name in self.name_to_factory:
            raise ValueError(f'Имена фабрик должны быть уникальными, но \'{factory.name}\' уже определено.')
        factory.simulation_id = self.id
        self.factories.append(factory)
        self.name_to_factory[factory.name] = factory

    ###################################################################################################
    # Cache and execution chain mechanisms
    ###################################################################################################
    def _execution_trace_position(self) -> int:
        """
        Возвращает текущую позицию в трассе выполнения, или -1, если трасса выполнения пуста.

        :return: Текущая позиция в трассе выполнения.
        """
        return len(self.execution_trace) - 1

    def _function_call_hash(self, function_name: str, *args: Any, **kwargs: Any) -> str:
        """
        Вычисляет хэш вызова функции.

        :param function_name: Имя функции.
        :param args: Позиционные аргументы.
        :param kwargs: Именованные аргументы.
        :return: Хэш вызова функции.
        """
        event = str((function_name, args, kwargs))
        return event

    def _skip_execution_with_cache(self):
        """
        Пропускает текущее выполнение, предполагая, что есть кэшированное состояние на той же позиции.
        """
        assert len(self.cached_trace) > self._execution_trace_position() + 1, \
            'Нет кэшированного состояния на текущей позиции выполнения.'

        self.execution_trace.append(self.cached_trace[self._execution_trace_position() + 1])

    def _is_transaction_event_cached(self, event_hash: str) -> bool:
        """
        Проверяет, соответствует ли хэш события кэшированному, если таковой имеется.
        Если соответствующего кэшированного состояния нет, возвращает True.

        :param event_hash: Хэш события.
        :return: True, если хэш соответствует кэшированному или кэша нет, иначе False.
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
                raise ValueError('Позиция трассы выполнения недопустима, должна быть >= -1, но равна ',
                                 self._execution_trace_position())

        else:  # no cache to use
            return False

    def _drop_cached_trace_suffix(self):
        """
        Удаляет суффикс кэшированной трассы, начиная с текущей позиции трассы выполнения. Это эффективно
        обновляет кэш до текущего состояния выполнения и начинает построение нового кэша оттуда.
        """
        self.cached_trace = self.cached_trace[:self._execution_trace_position() + 1]

    def _add_to_execution_trace(self, state: dict, event_hash: str, event_output: Any):
        """
        Добавляет состояние в список execution_trace и вычисляет соответствующий хэш.
        Вычисленный хэш сравнивается с хэшем кэшированной трассы на той же позиции,
        и если они не совпадают, выполнение прерывается. Аналогично, event_hash сравнивается
        с хэшем события в кэшированной трассе на той же позиции, и если они не совпадают, выполнение
        прерывается.

        :param state: Состояние для добавления.
        :param event_hash: Хэш события.
        :param event_output: Выход события.
        """
        # Compute the hash of the previous execution pair, if any
        previous_hash = None

        # Create a tuple of (hash, state) and append it to the execution_trace list
        self.execution_trace.append((previous_hash, event_hash, event_output, state))

    def _add_to_cache_trace(self, state: dict, event_hash: str, event_output: Any):
        """
        Добавляет состояние в список cached_trace и вычисляет соответствующий хэш.

        :param state: Состояние для добавления.
        :param event_hash: Хэш события.
        :param event_output: Выход события.
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
        Загружает кэш из файла по указанному пути.

        :param cache_path: Путь к файлу кэша.
        """
        try:
            with open(cache_path, 'r') as f:
                self.cached_trace = j_loads(f)
        except FileNotFoundError:
            logger.info(f'Файл кэша не найден по пути: {cache_path}.')
            self.cached_trace = []

    def _save_cache_file(self, cache_path: str):
        """
        Сохраняет кэш в файл по указанному пути. Всегда перезаписывает.

        :param cache_path: Путь к файлу для сохранения кэша.
        """
        try:
            # Create a temporary file
            with tempfile.NamedTemporaryFile('w', delete=False) as temp:
                import json
                json.dump(self.cached_trace, temp, indent=4)

            # Replace the original file with the temporary file
            os.replace(temp.name, cache_path)
        except Exception as e:
            logger.error(f'Произошла ошибка при сохранении файла кэша: {e}')
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

    def is_under_transaction(self) -> bool:
        """
        Проверяет, находится ли агент в транзакции.

        :return: True, если агент находится в транзакции, иначе False.
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
    # Simulation state handling
    ###################################################################################################

    def _encode_simulation_state(self) -> Dict:
        """
        Кодирует текущее состояние симуляции, включая агентов, окружения и другую
        соответствующую информацию.

        :return: Словарь, представляющий состояние симуляции.
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

    def _decode_simulation_state(self, state: Dict):
        """
        Декодирует заданное состояние симуляции, включая агентов, окружения и другую
        соответствующую информацию.

        :param state: Состояние для декодирования.
        """
        # local import to avoid circular dependencies
        from tinytroupe.agent import TinyPerson
        from tinytroupe.environment import TinyWorld

        logger.debug(f'Декодирование состояния симуляции: {state["factories"]}')
        logger.debug(f'Зарегистрированные фабрики: {self.name_to_factory}')
        logger.debug(f'Зарегистрированные агенты: {self.name_to_agent}')
        logger.debug(f'Зарегистрированные окружения: {self.name_to_environment}')

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
                raise ValueError(
                    f'Окружение {environment_state["name"]} отсутствует в симуляции, поэтому не может быть декодировано.') from e

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
                raise ValueError(
                    f'Агент {agent_state["name"]} отсутствует в симуляции, поэтому не может быть декодирован.') from e


class Transaction:
    """
    Класс, представляющий транзакцию.

    Атрибуты:
        obj_under_transaction (Any): Объект, над которым выполняется транзакция.
        simulation (Simulation): Объект симуляции.
        function_name (str): Имя функции, выполняемой в транзакции.
        function (callable): Функция, выполняемая в транзакции.
        args (tuple): Позиционные аргументы функции.
        kwargs (dict): Именованные аргументы функции.
    """

    def __init__(self, obj_under_transaction: Any, simulation: Optional[Simulation], function: callable, *args: Any,
                 **kwargs: Any):
        """
        Инициализирует объект транзакции.

        :param obj_under_transaction: Объект, над которым выполняется транзакция.
        :param simulation: Объект симуляции.
        :param function: Функция, выполняемая в транзакции.
        :param args: Позиционные аргументы функции.
        :param kwargs: Именованные аргументы функции.
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
                    raise ValueError(
                        f'Объект {obj_under_transaction} уже захвачен другой симуляцией (id={obj_under_transaction.simulation_id}), \\\
                                    и не может быть захвачен симуляцией id={simulation.id}.')

                logger.debug(
                    f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Object {obj_under_transaction} is already captured by simulation {simulation.id}.')
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
                    raise ValueError(
                        f'Объект {obj_under_transaction} (type = {type(obj_under_transaction)}) не является экземпляром TinyPerson или TinyWorld, и не может быть захвачен симуляцией.')

    def execute(self) -> Any:
        """
        Выполняет транзакцию.

        :return: Результат выполнения функции.
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
                logger.info(
                    f'Пропуск выполнения {self.function_name} с аргументами {self.args} и kwargs {self.kwargs}, так как оно уже кэшировано.')

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
            raise ValueError(f'Недопустимый статус симуляции на данный момент: {self.simulation.status}')

        # Checkpoint if needed
        if self.simulation is not None and self.simulation.auto_checkpoint:
            self.simulation.checkpoint()

        return output

    def _encode_function_output(self, output: Any) -> Optional[Dict]:
        """
        Кодирует выходные данные функции.

        :param output: Выходные данные функции.
        :return: Словарь с закодированными данными.
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
            raise ValueError(f'Неподдерживаемый тип выходных данных: {type(output)}')

    def _decode_function_output(self, encoded_output: Optional[Dict]) -> Any:
        """
        Декодирует закодированные выходные данные функции.

        :param encoded_output: Словарь с закодированными данными.
        :return: Декодированные выходные данные функции.
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
            raise ValueError(f'Неподдерживаемый тип выходных данных: {encoded_output["type"]}')


def transactional(func: callable) -> callable:
    """
    Декоратор, делающий функцию транзакционной для симуляции.

    :param func: Функция для декорирования.
    :return: Декорированная функция.
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        obj_under_transaction = args[0]
        simulation = current_simulation()
        obj_sim_id = obj_under_transaction.simulation_id if hasattr(obj_under_transaction, 'simulation_id') else None

        logger.debug(
            f'-----------------------------------------> Transaction: {func.__name__} с аргументами {args[1:]} и kwargs {kwargs} под симуляцией {obj_sim_id}.')

        transaction = Transaction(obj_under_transaction, simulation, func, *args, **kwargs)
        result = transaction.execute()
        return result

    return wrapper


class SkipTransaction(Exception):
    """
    Исключение, сигнализирующее о пропуске транзакции.
    """
    pass


class CacheOutOfSync(Exception):
    """
    Исключение, возникающее, когда кэшированные и свежевыполненные элементы не синхронизированы.
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

_current_simulations: Dict[str, Optional[Simulation]] = {}
_current_simulation_id: Optional[str] = None


def reset():
    """
    Сбрасывает все состояние управления симуляцией.
    """
    global _current_simulations, _current_simulation_id
    _current_simulations = {'default': None}

    # TODO Currently, only one simulation can be started at a time. In future versions, this should be
    #      changed to allow multiple simulations to be started at the same time, e.g., for fast
    #      analyses through parallelization.
    _current_simulation_id = None


def _simulation(id: str = 'default') -> Simulation:
    """
    Возвращает объект симуляции по её id.

    :param id: Идентификатор симуляции.
    :return: Объект симуляции.
    """
    global _current_simulations
    if _current_simulations[id] is None:
        _current_simulations[id] = Simulation()

    return _current_simulations[id]


def begin(cache_path: Optional[str] = None, id: str = 'default', auto_checkpoint: bool = False):
    """
    Начинает управляемую симуляцию.

    :param cache_path: Путь к файлу кэша, если нужно использовать нестандартный путь.
    :param id: Идентификатор симуляции, по умолчанию 'default'.
    :param auto_checkpoint: Флаг автоматического сохранения состояния.
    """
    global _current_simulation_id
    if _current_simulation_id is None:
        _simulation(id).begin(cache_path, auto_checkpoint)
        _current_simulation_id = id
    else:
        raise ValueError(
            f'Симуляция уже запущена под id {_current_simulation_id}. В настоящее время одновременно может быть запущена только одна симуляция.')


def end(id: str = 'default'):
    """
    Завершает управляемую симуляцию.

    :param id: Идентификатор симуляции.
    """
    global _current_simulation_id
    _simulation(id).end()
    _current_simulation_id = None


def checkpoint(id: str = 'default'):
    """
    Сохраняет текущее состояние симуляции.

    :param id: Идентификатор симуляции.
    """
    _simulation(id).checkpoint()


def current_simulation() -> Optional[Simulation]:
    """
    Возвращает текущую симуляцию.

    :return: Текущая симуляция или None, если симуляция не