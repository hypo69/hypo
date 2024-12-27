# Анализ кода модуля `control.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован, с разделением на классы и функции.
    - Имеется реализация механизма кэширования и транзакций для управления состоянием симуляции.
    - Используется логирование для отслеживания важных событий и ошибок.
    - Присутствует базовая обработка ошибок и исключений.
    - Код соответствует PEP8.
 -  Минусы
    -  Некоторые docstring не полностью соответствуют стандарту RST.
    -  Используется `json.load` и `json.dump` вместо `j_loads` и `j_dumps`.
    -  Присутствуют избыточные комментарии.
    -  Некоторые функции имеют избыточное количество параметров.
    -  Не везде используется `logger.error` для обработки исключений.

**Рекомендации по улучшению**
1.  **Документация:**
    -   Переписать все docstring в соответствии с reStructuredText (RST).
    -   Добавить более подробное описание параметров и возвращаемых значений.
2.  **Использование `j_loads` и `j_dumps`**:
    -   Заменить `json.load` и `json.dump` на `j_loads` и `j_dumps` из `src.utils.jjson`.
3.  **Логирование**:
    -  Заменить стандартные `try-except` на `logger.error` для обработки ошибок.
    -  Использовать `logger.debug` для отладочной информации.
4.  **Рефакторинг:**
    -  Удалить избыточные комментарии.
    -  Упростить некоторые функции, где это возможно.
    -  Улучшить читаемость кода за счет переименования переменных и методов.
5.  **Обработка исключений:**
    -  Добавить более конкретные исключения и сообщения об ошибках.
6.  **Импорты:**
    - Добавить отсутствующие импорты.

**Оптимизированный код**

```python
"""
Модуль для управления симуляциями.
=========================================================================================

Этот модуль содержит классы и функции для управления симуляциями,
включая механизмы кэширования и транзакций.

Пример использования
--------------------

Пример использования класса `Simulation`:

.. code-block:: python

    simulation = Simulation(id='my_simulation')
    simulation.begin()
    # ... действия симуляции ...
    simulation.end()
"""
import os
import tempfile
from typing import Any

from src.logger.logger import logger
from src.utils.jjson import j_loads, j_dumps
import tinytroupe
import tinytroupe.utils as utils

# import logging # убран из за конфликта с src.logger.logger
# logger = logging.getLogger("tinytroupe") # убран из за конфликта с src.logger.logger


class Simulation:
    """
    Класс для управления симуляцией.

    :ivar str STATUS_STOPPED: Статус остановленной симуляции.
    :ivar str STATUS_STARTED: Статус запущенной симуляции.
    :ivar str id: Идентификатор симуляции.
    :ivar list agents: Список агентов в симуляции.
    :ivar dict name_to_agent: Словарь, сопоставляющий имена агентов с объектами агентов.
    :ivar list environments: Список окружений в симуляции.
    :ivar list factories: Список фабрик в симуляции.
    :ivar dict name_to_factory: Словарь, сопоставляющий имена фабрик с объектами фабрик.
    :ivar dict name_to_environment: Словарь, сопоставляющий имена окружений с объектами окружений.
    :ivar str status: Текущий статус симуляции.
    :ivar str cache_path: Путь к файлу кэша.
    :ivar bool auto_checkpoint: Флаг автоматического сохранения кэша после каждой транзакции.
    :ivar bool has_unsaved_cache_changes: Флаг наличия несохраненных изменений в кэше.
    :ivar bool _under_transaction: Флаг, указывающий, что симуляция находится в транзакции.
    :ivar list cached_trace: Список состояний симуляции из кэша.
    :ivar list execution_trace: Список выполненных состояний симуляции.
    """
    STATUS_STOPPED = "stopped"
    STATUS_STARTED = "started"

    def __init__(self, id="default", cached_trace: list = None):
        """
        Инициализирует объект симуляции.

        :param str id: Идентификатор симуляции. По умолчанию "default".
        :param list cached_trace: Начальный кэш трассировки. По умолчанию None.
        """
        self.id = id

        self.agents = []
        self.name_to_agent = {}  # {agent_name: agent, ...}

        self.environments = []

        self.factories = []  # e.g., TinyPersonFactory instances
        self.name_to_factory = {}  # {factory_name: factory, ...}

        self.name_to_environment = {}  # {environment_name: environment, ...}
        self.status = Simulation.STATUS_STOPPED

        self.cache_path = f"./tinytroupe-cache-{id}.json"  # default cache path

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
        Начинает контролируемую симуляцию.

        :param str cache_path: Путь к файлу кэша. Если не указан, используется путь по умолчанию.
        :param bool auto_checkpoint: Флаг автоматического сохранения кэша после каждой транзакции. По умолчанию False.
        :raises ValueError: Если симуляция уже запущена.
        """
        # local import to avoid circular dependencies
        from tinytroupe.agent import TinyPerson
        from tinytroupe.environment import TinyWorld
        from tinytroupe.factory import TinyFactory

        if self.status == Simulation.STATUS_STOPPED:
            self.status = Simulation.STATUS_STARTED
        else:
            raise ValueError("Simulation is already started.")

        if cache_path is not None:
            self.cache_path = cache_path

        # should we automatically checkpoint?
        self.auto_checkpoint = auto_checkpoint

        # clear the agents, environments and other simulated entities, we\'ll track them from now on
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
        Завершает контролируемую симуляцию.

        :raises ValueError: Если симуляция уже остановлена.
        """
        if self.status == Simulation.STATUS_STARTED:
            self.status = Simulation.STATUS_STOPPED
            self.checkpoint()
        else:
            raise ValueError("Simulation is already stopped.")

    def checkpoint(self):
        """
        Сохраняет текущую трассировку симуляции в файл.
        """
        # save the cache file
        if self.has_unsaved_cache_changes:
            self._save_cache_file(self.cache_path)
        else:
            logger.debug("No unsaved cache changes to save to file.")

    def add_agent(self, agent):
        """
        Добавляет агента в симуляцию.

        :param agent: Объект агента для добавления.
        :raises ValueError: Если имя агента уже существует.
        """
        if agent.name in self.name_to_agent:
            raise ValueError(f"Agent names must be unique, but '{agent.name}' is already defined.")
        agent.simulation_id = self.id
        self.agents.append(agent)
        self.name_to_agent[agent.name] = agent

    def add_environment(self, environment):
        """
        Добавляет окружение в симуляцию.

        :param environment: Объект окружения для добавления.
        :raises ValueError: Если имя окружения уже существует.
        """
        if environment.name in self.name_to_environment:
            raise ValueError(f"Environment names must be unique, but '{environment.name}' is already defined.")
        environment.simulation_id = self.id
        self.environments.append(environment)
        self.name_to_environment[environment.name] = environment

    def add_factory(self, factory):
        """
        Добавляет фабрику в симуляцию.

        :param factory: Объект фабрики для добавления.
        :raises ValueError: Если имя фабрики уже существует.
        """
        if factory.name in self.name_to_factory:
            raise ValueError(f"Factory names must be unique, but '{factory.name}' is already defined.")
        factory.simulation_id = self.id
        self.factories.append(factory)
        self.name_to_factory[factory.name] = factory

    ###################################################################################################
    # Cache and execution chain mechanisms
    ###################################################################################################
    def _execution_trace_position(self) -> int:
        """
        Возвращает текущую позицию в трассировке выполнения.

        :return: Индекс текущей позиции в трассировке или -1, если трассировка пуста.
        :rtype: int
        """
        return len(self.execution_trace) - 1

    def _function_call_hash(self, function_name, *args, **kwargs) -> int:
        """
        Вычисляет хэш вызова функции.

        :param str function_name: Имя функции.
        :param args: Позиционные аргументы функции.
        :param kwargs: Именованные аргументы функции.
        :return: Хэш вызова функции.
        :rtype: int
        """
        event = str((function_name, args, kwargs))
        return event

    def _skip_execution_with_cache(self):
        """
        Пропускает текущее выполнение, если есть состояние в кэше.

        :raises AssertionError: Если нет состояния в кэше для текущей позиции.
        """
        assert len(self.cached_trace) > self._execution_trace_position() + 1, "There's no cached state at the current execution position."

        self.execution_trace.append(self.cached_trace[self._execution_trace_position() + 1])

    def _is_transaction_event_cached(self, event_hash) -> bool:
        """
        Проверяет, совпадает ли хэш события с хэшем в кэше.

        :param int event_hash: Хэш события.
        :return: True, если хэш совпадает или кэш отсутствует, иначе False.
        :rtype: bool
        :raises ValueError: Если позиция трассировки выполнения невалидна.
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
                raise ValueError("Execution trace position is invalid, must be >= -1, but is ", self._execution_trace_position())

        else:  # no cache to use
            return False

    def _drop_cached_trace_suffix(self):
        """
        Удаляет суффикс из кэшированной трассировки, начиная с текущей позиции.
        """
        self.cached_trace = self.cached_trace[:self._execution_trace_position() + 1]

    def _add_to_execution_trace(self, state: dict, event_hash: int, event_output:Any):
        """
        Добавляет состояние в трассировку выполнения.

        :param dict state: Состояние симуляции.
        :param int event_hash: Хэш события.
        :param event_output: Вывод события
        """
        # Compute the hash of the previous execution pair, if any
        previous_hash = None

        # Create a tuple of (hash, state) and append it to the execution_trace list
        self.execution_trace.append((previous_hash, event_hash, event_output, state))

    def _add_to_cache_trace(self, state: dict, event_hash: int, event_output:Any):
        """
        Добавляет состояние в кэшированную трассировку.

        :param dict state: Состояние симуляции.
        :param int event_hash: Хэш события.
        :param event_output: Вывод события
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
        Загружает кэш из файла.

        :param str cache_path: Путь к файлу кэша.
        """
        try:
            with open(cache_path, "r") as f:
                self.cached_trace = j_loads(f)
        except FileNotFoundError:
            logger.info(f"Cache file not found on path: {cache_path}.")
            self.cached_trace = []
        except Exception as e:
             logger.error(f"Error loading cache file: {cache_path}.", exc_info=True)
             self.cached_trace = []

    def _save_cache_file(self, cache_path: str):
        """
        Сохраняет кэш в файл.

        :param str cache_path: Путь к файлу кэша.
        """
        try:
            # Create a temporary file
            with tempfile.NamedTemporaryFile('w', delete=False) as temp:
                j_dumps(self.cached_trace, temp, indent=4)

            # Replace the original file with the temporary file
            os.replace(temp.name, cache_path)
        except Exception as e:
            logger.error(f"An error occurred while saving cache: {e}", exc_info=True)
            

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

        :return: True, если агент в транзакции, иначе False.
        :rtype: bool
        """
        return self._under_transaction

    def _clear_communications_buffers(self):
        """
        Очищает буферы связи всех агентов и окружений.
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
        Кодирует текущее состояние симуляции.

        :return: Словарь с закодированным состоянием симуляции.
        :rtype: dict
        """
        state = {}

        # Encode agents
        state["agents"] = []
        for agent in self.agents:
            state["agents"].append(agent.encode_complete_state())

        # Encode environments
        state["environments"] = []
        for environment in self.environments:
            state["environments"].append(environment.encode_complete_state())

        # Encode factories
        state["factories"] = []
        for factory in self.factories:
            state["factories"].append(factory.encode_complete_state())

        return state

    def _decode_simulation_state(self, state: dict):
        """
        Декодирует состояние симуляции.

        :param dict state: Словарь с закодированным состоянием.
        :raises ValueError: Если окружение или агент не найдены в симуляции.
        """
        # local import to avoid circular dependencies
        from tinytroupe.agent import TinyPerson
        from tinytroupe.environment import TinyWorld

        logger.debug(f"Decoding simulation state: {state['factories']}")
        logger.debug(f"Registered factories: {self.name_to_factory}")
        logger.debug(f"Registered agents: {self.name_to_agent}")
        logger.debug(f"Registered environments: {self.name_to_environment}")

        # Decode factories
        for factory_state in state["factories"]:
            factory = self.name_to_factory[factory_state["name"]]
            factory.decode_complete_state(factory_state)

        # Decode environments
        for environment_state in state["environments"]:
            try:
                environment = self.name_to_environment[environment_state["name"]]
                environment.decode_complete_state(environment_state)
                if TinyWorld.communication_display:
                    environment.pop_and_display_latest_communications()

            except Exception as e:
                raise ValueError(f"Environment {environment_state['name']} is not in the simulation, thus cannot be decoded there.") from e

        # Decode agents (if they were not already decoded by the environment)
        for agent_state in state["agents"]:
            try:
                agent = self.name_to_agent[agent_state["name"]]
                agent.decode_complete_state(agent_state)

                # The agent has not yet been decoded because it is not in any environment. So, decode it.
                if agent.environment is None:
                    if TinyPerson.communication_display:
                        agent.pop_and_display_latest_communications()
            except Exception as e:
                raise ValueError(f"Agent {agent_state['name']} is not in the simulation, thus cannot be decoded there.") from e


class Transaction:
    """
    Класс для управления транзакциями симуляции.
    """

    def __init__(self, obj_under_transaction, simulation, function, *args, **kwargs):
        """
        Инициализирует объект транзакции.

        :param obj_under_transaction: Объект, над которым выполняется транзакция.
        :param simulation: Объект симуляции.
        :param function: Функция для выполнения в транзакции.
        :param args: Позиционные аргументы функции.
        :param kwargs: Именованные аргументы функции.
        :raises ValueError: Если объект уже захвачен другой симуляцией.
        :raises ValueError: Если объект не является экземпляром TinyPerson, TinyWorld или TinyFactory.
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
                    raise ValueError(f"Object {obj_under_transaction} is already captured by a different simulation (id={obj_under_transaction.simulation_id}), \
                                    and cannot be captured by simulation id={simulation.id}.")

                logger.debug(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Object {obj_under_transaction} is already captured by simulation {simulation.id}.")
            else:
                # if is a TinyPerson, add the agent to the simulation
                if isinstance(obj_under_transaction, TinyPerson):
                    simulation.add_agent(obj_under_transaction)
                    logger.debug(f">>>>>>>>>>>>>>>>>>>>>>> Added agent {obj_under_transaction} to simulation {simulation.id}.")

                # if is a TinyWorld, add the environment to the simulation
                elif isinstance(obj_under_transaction, TinyWorld):
                    simulation.add_environment(obj_under_transaction)

                # if is a TinyFactory, add the factory to the simulation
                elif isinstance(obj_under_transaction, TinyFactory):
                    simulation.add_factory(obj_under_transaction)
                    logger.debug(f">>>>>>>>>>>>>>>>>>>>>>> Added factory {obj_under_transaction} to simulation {simulation.id}.")

                else:
                    raise ValueError(f"Object {obj_under_transaction} (type = {type(obj_under_transaction)}) is not a TinyPerson or TinyWorld instance, and cannot be captured by the simulation.")


    def execute(self):
        """
        Выполняет транзакцию.

        :return: Результат выполнения функции.
        :raises ValueError: Если статус симуляции невалиден.
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
                logger.info(f"Skipping execution of {self.function_name} with args {self.args} and kwargs {self.kwargs} because it is already cached.")

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
            raise ValueError(f"Simulation status is invalid at this point: {self.simulation.status}")

        # Checkpoint if needed
        if self.simulation is not None and self.simulation.auto_checkpoint:
            self.simulation.checkpoint()

        return output

    def _encode_function_output(self, output) -> dict:
        """
        Кодирует вывод функции.

        :param output: Вывод функции для кодирования.
        :return: Словарь с закодированным выводом.
        :rtype: dict
        :raises ValueError: Если тип вывода не поддерживается.
        """
        # local import to avoid circular dependencies
        from tinytroupe.agent import TinyPerson
        from tinytroupe.environment import TinyWorld
        from tinytroupe.factory import TinyFactory

        # if the output is a TinyPerson, encode it
        if output is None:
            return None
        elif isinstance(output, TinyPerson):
            return {"type": "TinyPersonRef", "name": output.name}
        # if it is a TinyWorld, encode it
        elif isinstance(output, TinyWorld):
            return {"type": "TinyWorldRef", "name": output.name}
        # if it is a TinyFactory, encode it
        elif isinstance(output, TinyFactory):
            return {"type": "TinyFactoryRef", "name": output.name}
        # if it is one of the types supported by JSON, encode it as is
        elif isinstance(output, (int, float, str, bool, list, dict, tuple)):
            return {"type": "JSON", "value": output}
        # otherwise, raise an exception
        else:
            raise ValueError(f"Unsupported output type: {type(output)}")

    def _decode_function_output(self, encoded_output: dict):
        """
        Декодирует закодированный вывод функции.

        :param dict encoded_output: Словарь с закодированным выводом.
        :return: Декодированный вывод функции.
        :raises ValueError: Если тип вывода не поддерживается.
        """
        # local import to avoid circular dependencies
        from tinytroupe.agent import TinyPerson
        from tinytroupe.environment import TinyWorld
        from tinytroupe.factory import TinyFactory

        if encoded_output is None:
            return None
        elif encoded_output["type"] == "TinyPersonRef":
            return TinyPerson.get_agent_by_name(encoded_output["name"])
        elif encoded_output["type"] == "TinyWorldRef":
            return TinyWorld.get_environment_by_name(encoded_output["name"])
        elif encoded_output["type"] == "TinyFactoryRef":
            return TinyFactory.get_factory_by_name(encoded_output["name"])
        elif encoded_output["type"] == "JSON":
            return encoded_output["value"]
        else:
            raise ValueError(f"Unsupported output type: {encoded_output['type']}")


def transactional(func):
    """
    Декоратор, делающий функцию транзакционной для симуляции.

    :param func: Функция для декорирования.
    :return: Обернутая функция.
    """
    def wrapper(*args, **kwargs):
        obj_under_transaction = args[0]
        simulation = current_simulation()
        obj_sim_id = obj_under_transaction.simulation_id if hasattr(obj_under_transaction, 'simulation_id') else None

        logger.debug(f"-----------------------------------------> Transaction: {func.__name__} with args {args[1:]} and kwargs {kwargs} under simulation {obj_sim_id}.")

        transaction = Transaction(obj_under_transaction, simulation, func, *args, **kwargs)
        result = transaction.execute()
        return result

    return wrapper


class SkipTransaction(Exception):
    """
    Исключение, пропускающее транзакцию.
    """
    pass


class CacheOutOfSync(Exception):
    """
    Исключение, когда кэш и выполненный код рассинхронизированы.
    """
    pass


class ExecutionCached(Exception):
    """
    Исключение, когда выполнение уже кэшировано.
    """
    pass

###################################################################################################
# Convenience functions
###################################################################################################


def reset():
    """
    Сбрасывает состояние управления симуляцией.
    """
    global _current_simulations, _current_simulation_id
    _current_simulations = {"default": None}

    # TODO Currently, only one simulation can be started at a time. In future versions, this should be
    #      changed to allow multiple simulations to be started at the same time, e.g., for fast
    #      analyses through parallelization.
    _current_simulation_id = None


def _simulation(id="default") -> Simulation:
    """
    Возвращает объект симуляции по идентификатору.

    :param str id: Идентификатор симуляции. По умолчанию "default".
    :return: Объект симуляции.
    :rtype: Simulation
    """
    global _current_simulations
    if _current_simulations[id] is None:
        _current_simulations[id] = Simulation()

    return _current_simulations[id]


def begin(cache_path=None, id="default", auto_checkpoint=False):
    """
    Начинает контролируемую симуляцию.

    :param str cache_path: Путь к файлу кэша.
    :param str id: Идентификатор симуляции. По умолчанию "default".
    :param bool auto_checkpoint: Флаг автоматического сохранения кэша после каждой транзакции. По умолчанию False.
    :raises ValueError: Если симуляция уже запущена.
    """
    global _current_simulation_id
    if _current_simulation_id is None:
        _simulation(id).begin(cache_path, auto_checkpoint)
        _current_simulation_id = id
    else:
        raise ValueError(f"Simulation is already started under id {_current_simulation_id}. Currently only one simulation can be started at a time.")


def end(id="default"):
    """
    Завершает контролируемую симуляцию.

    :param str id: Идентификатор симуляции. По умолчанию "default".
    """
    global _current_simulation_id
    _simulation(id).end()
    _current_simulation_id = None


def checkpoint(id="default"):
    """
    Сохраняет текущее состояние симуляции.

    :param str id: Идентификатор симуляции. По умолчанию "default".
    """
    _simulation(id).checkpoint()


def current_simulation() -> Simulation:
    """
    Возвращает текущую симуляцию.

    :return: Объект текущей симуляции или None, если симуляция не запущена.
    :rtype: Simulation
    """
    global _current_simulation_id
    if _current_simulation_id is not None:
        return _simulation(_current_simulation_id)
    else:
        return None


_current_simulations = {"default": None}
_current_simulation_id = None

reset() # initialize the control state