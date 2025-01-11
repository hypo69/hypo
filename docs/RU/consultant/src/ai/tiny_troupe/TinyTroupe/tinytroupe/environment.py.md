# Анализ кода модуля `environment.py`

**Качество кода: 7/10**

-  **Плюсы**
    - Код хорошо структурирован с использованием классов `TinyWorld` и `TinySocialNetwork`, что обеспечивает гибкость и расширяемость.
    - Присутствует подробное документирование методов и классов.
    - Используются логирование для отслеживания действий агентов и обработки ошибок.
    - Реализованы методы для управления временем и шагами симуляции.
    - Присутствуют методы для добавления, удаления и управления агентами.
    - Код поддерживает сохранения и восстановление состояния среды.
-  **Минусы**
    -   Не все методы имеют docstring в формате RST.
    -   Используется `logging`, а не `src.logger.logger`.
    -   Много повторяющегося кода для `run_...` и `skip_...` методов, который можно вынести в одну функцию.
    -  Импорт `datetime` выполняется как `import datetime`, в то время как нужно `from datetime import datetime, timedelta`.
    -  Отсутствует проверка на типы для передаваемых аргументов в некоторых функциях.

**Рекомендации по улучшению**

1.  **Импорты:**
    -   Использовать `from src.logger.logger import logger` вместо `import logging` для логирования.
    -   Использовать `from datetime import datetime, timedelta` вместо `import datetime`.

2.  **Документация:**
    -   Добавить docstring в формате RST для всех функций, методов и классов.
    -   Улучшить описания методов, сделав их более информативными и подробными.

3.  **Рефакторинг:**
    -   Вынести общую логику для методов `run_...` и `skip_...` в отдельные методы.
    -   Улучшить обработку ошибок, используя `logger.error` вместо общих `try-except` блоков.
    -   Добавить проверку типов для аргументов в функциях.

4. **Улучшения:**
    - Добавить возможность кастомизировать вывод сообщений в консоль.
    - Использовать более конкретные исключения.
    - Использовать `f-strings` для форматирования строк.

**Оптимизированный код**

```python
"""
Модуль для определения среды, в которой взаимодействуют агенты.
=========================================================================================

Этот модуль содержит классы :class:`TinyWorld` и :class:`TinySocialNetwork`,
которые обеспечивают основу для создания и управления виртуальными средами,
в которых действуют агенты.

Класс `TinyWorld` является базовым классом для всех сред, предоставляя
основные функции, такие как управление временем, агентами и их взаимодействиями.

Класс `TinySocialNetwork` расширяет `TinyWorld`, добавляя поддержку социальных
отношений между агентами.

Примеры использования
--------------------

Пример создания и запуска симуляции:

.. code-block:: python

    from datetime import datetime, timedelta
    from tinytroupe.agent import TinyPerson
    from tinytroupe.environment import TinyWorld

    # Создание агентов
    agent1 = TinyPerson(name='Alice')
    agent2 = TinyPerson(name='Bob')

    # Создание среды
    world = TinyWorld(name='MyWorld', agents=[agent1, agent2], initial_datetime=datetime.now())

    # Запуск симуляции на 10 шагов
    world.run(steps=10, timedelta_per_step=timedelta(minutes=1))

Пример создания и использования социальной сети:

.. code-block:: python

    from datetime import datetime, timedelta
    from tinytroupe.agent import TinyPerson
    from tinytroupe.environment import TinySocialNetwork

    # Создание агентов
    agent1 = TinyPerson(name='Alice')
    agent2 = TinyPerson(name='Bob')
    agent3 = TinyPerson(name='Charlie')

    # Создание социальной сети
    social_network = TinySocialNetwork(name='MyNetwork', broadcast_if_no_target=True)

    # Добавление агентов в сеть
    social_network.add_agent(agent1).add_agent(agent2).add_agent(agent3)

    # Установка отношений между агентами
    social_network.add_relation(agent1, agent2, name='friends')

    # Запуск симуляции на 5 шагов
    social_network.run(steps=5, timedelta_per_step=timedelta(minutes=1))
"""
from src.logger.logger import logger # Используем src.logger.logger для логирования
import copy
from datetime import datetime, timedelta
from typing import Any, TypeVar, Union, List
from pathlib import Path
from tinytroupe.agent import TinyPerson
from tinytroupe.utils import name_or_empty, pretty_datetime
import tinytroupe.control as control
from tinytroupe.control import transactional
from rich.console import Console
from tinytroupe.config import default

AgentOrWorld = Union["TinyPerson", "TinyWorld"]
Self = TypeVar("Self", bound="TinyWorld")

class TinyWorld:
    """
    Базовый класс для окружений.

    Атрибуты:
        all_environments (dict): Словарь всех созданных окружений.
            Ключ - имя окружения, значение - объект окружения.
        communication_display (bool): Флаг для отображения коммуникаций окружений.
        name (str): Имя окружения.
        current_datetime (datetime): Текущее время окружения.
        broadcast_if_no_target (bool): Если True, то действия транслируются, если цель не найдена.
        simulation_id (Any): ID симуляции, в которой используется окружение.
        agents (list): Список агентов в окружении.
        name_to_agent (dict): Словарь, связывающий имена агентов с их объектами.
        _displayed_communications_buffer (list): Буфер для отображаемых сообщений.
        console (Console): Объект для вывода в консоль.
    """
    all_environments = {} # name -> environment
    communication_display = True

    def __init__(self, name: str='A TinyWorld', agents: List[TinyPerson] = [],
                 initial_datetime: datetime = datetime.now(),
                 broadcast_if_no_target: bool = True):
        """
        Инициализирует окружение.

        Args:
            name (str): Имя окружения.
            agents (list): Список агентов для добавления в окружение.
            initial_datetime (datetime): Начальное время окружения.
            broadcast_if_no_target (bool): Если True, транслирует действия, если цель не найдена.
        """
        self.name = name
        self.current_datetime = initial_datetime
        self.broadcast_if_no_target = broadcast_if_no_target
        self.simulation_id = None # будет переопределено позже, если агент используется в рамках конкретной симуляции
        
        self.agents = []
        self.name_to_agent = {} # {agent_name: agent, agent_name_2: agent_2, ...}
        self._displayed_communications_buffer = []
        self.console = Console()

        TinyWorld.add_environment(self)
        self.add_agents(agents)
    
    #######################################################################
    # Методы управления симуляцией
    #######################################################################
    @transactional
    def _step(self, timedelta_per_step: timedelta = None):
        """
        Выполняет один шаг симуляции. По умолчанию, вызывает действия всех агентов.

        Args:
            timedelta_per_step (timedelta): Временной интервал для шага.

        Returns:
            dict: Словарь действий агентов.
        """
        # Увеличивает текущее время, если задано.
        self._advance_datetime(timedelta_per_step)

        # Агенты выполняют действия.
        agents_actions = {}
        for agent in self.agents:
            logger.debug(f"[{self.name}] Agent {name_or_empty(agent)} действует.")
            actions = agent.act(return_actions=True)
            agents_actions[agent.name] = actions

            self._handle_actions(agent, agent.pop_latest_actions())
        
        return agents_actions

    def _advance_datetime(self, timedelta_per_step: timedelta):
        """
        Увеличивает текущее время окружения на заданный интервал.

        Args:
            timedelta_per_step (timedelta): Временной интервал для увеличения времени.
        """
        if timedelta_per_step is not None:
            self.current_datetime += timedelta_per_step
        else:
            logger.info(f"[{self.name}] Не задан интервал времени, время не было увеличено.")

    @transactional
    def run(self, steps: int, timedelta_per_step: timedelta = None, return_actions: bool = False):
        """
        Запускает симуляцию на заданное количество шагов.

        Args:
            steps (int): Количество шагов для запуска симуляции.
            timedelta_per_step (timedelta): Временной интервал между шагами.
            return_actions (bool): Если True, возвращает действия агентов.

        Returns:
            list: Список действий агентов за все шаги, если return_actions True.
        """
        agents_actions_over_time = []
        for i in range(steps):
            logger.info(f"[{self.name}] Запуск шага {i+1} из {steps}.")

            if TinyWorld.communication_display:
                self._display_communication(cur_step=i+1, total_steps=steps, kind='step', timedelta_per_step=timedelta_per_step)

            agents_actions = self._step(timedelta_per_step=timedelta_per_step)
            agents_actions_over_time.append(agents_actions)
        
        if return_actions:
            return agents_actions_over_time
    
    @transactional
    def skip(self, steps: int, timedelta_per_step: timedelta = None):
        """
        Пропускает заданное количество шагов в окружении.

        Args:
            steps (int): Количество шагов для пропуска.
            timedelta_per_step (timedelta): Временной интервал между шагами.
        """
        self._advance_datetime(steps * timedelta_per_step)
    
    def _run_time(self, steps: int, time_unit: str):
        """
        Выполняет симуляцию на заданное количество временных единиц.

        Args:
            steps (int): Количество временных единиц.
            time_unit (str): Единица времени ('minutes', 'hours', 'days', 'weeks', 'months', 'years').
        """
        if time_unit == 'minutes':
            self.run(steps=steps, timedelta_per_step=timedelta(minutes=1))
        elif time_unit == 'hours':
            self.run(steps=steps, timedelta_per_step=timedelta(hours=1))
        elif time_unit == 'days':
            self.run(steps=steps, timedelta_per_step=timedelta(days=1))
        elif time_unit == 'weeks':
            self.run(steps=steps, timedelta_per_step=timedelta(weeks=1))
        elif time_unit == 'months':
            self.run(steps=steps, timedelta_per_step=timedelta(weeks=4))
        elif time_unit == 'years':
            self.run(steps=steps, timedelta_per_step=timedelta(days=365))
    
    def _skip_time(self, steps: int, time_unit: str):
        """
        Пропускает заданное количество временных единиц в окружении.

        Args:
            steps (int): Количество временных единиц для пропуска.
            time_unit (str): Единица времени ('minutes', 'hours', 'days', 'weeks', 'months', 'years').
        """
        if time_unit == 'minutes':
            self.skip(steps=steps, timedelta_per_step=timedelta(minutes=1))
        elif time_unit == 'hours':
            self.skip(steps=steps, timedelta_per_step=timedelta(hours=1))
        elif time_unit == 'days':
            self.skip(steps=steps, timedelta_per_step=timedelta(days=1))
        elif time_unit == 'weeks':
            self.skip(steps=steps, timedelta_per_step=timedelta(weeks=1))
        elif time_unit == 'months':
            self.skip(steps=steps, timedelta_per_step=timedelta(weeks=4))
        elif time_unit == 'years':
            self.skip(steps=steps, timedelta_per_step=timedelta(days=365))

    def run_minutes(self, minutes: int):
        """Запускает окружение на заданное количество минут."""
        self._run_time(minutes, 'minutes')
    
    def skip_minutes(self, minutes: int):
        """Пропускает заданное количество минут в окружении."""
        self._skip_time(minutes, 'minutes')
    
    def run_hours(self, hours: int):
        """Запускает окружение на заданное количество часов."""
        self._run_time(hours, 'hours')
    
    def skip_hours(self, hours: int):
       """Пропускает заданное количество часов в окружении."""
       self._skip_time(hours, 'hours')
    
    def run_days(self, days: int):
       """Запускает окружение на заданное количество дней."""
       self._run_time(days, 'days')
    
    def skip_days(self, days: int):
        """Пропускает заданное количество дней в окружении."""
        self._skip_time(days, 'days')
    
    def run_weeks(self, weeks: int):
        """Запускает окружение на заданное количество недель."""
        self._run_time(weeks, 'weeks')
    
    def skip_weeks(self, weeks: int):
        """Пропускает заданное количество недель в окружении."""
        self._skip_time(weeks, 'weeks')
    
    def run_months(self, months: int):
        """Запускает окружение на заданное количество месяцев."""
        self._run_time(months, 'months')
    
    def skip_months(self, months: int):
        """Пропускает заданное количество месяцев в окружении."""
        self._skip_time(months, 'months')
    
    def run_years(self, years: int):
        """Запускает окружение на заданное количество лет."""
        self._run_time(years, 'years')
    
    def skip_years(self, years: int):
        """Пропускает заданное количество лет в окружении."""
        self._skip_time(years, 'years')

    #######################################################################
    # Методы управления агентами
    #######################################################################
    def add_agents(self, agents: List[TinyPerson]) -> Self:
        """
        Добавляет список агентов в окружение.

        Args:
            agents (list): Список агентов для добавления.

        Returns:
            Self: Возвращает self для цепочного вызова.
        """
        for agent in agents:
            self.add_agent(agent)
        
        return self # for chaining

    def add_agent(self, agent: TinyPerson) -> Self:
        """
        Добавляет агента в окружение. Имя агента должно быть уникальным.

        Args:
            agent (TinyPerson): Агент для добавления.

        Raises:
            ValueError: Если имя агента не уникально.

        Returns:
            Self: Возвращает self для цепочного вызова.
        """
        if agent not in self.agents:
            logger.debug(f"Добавление агента {agent.name} в окружение.")
            
            if agent.name not in self.name_to_agent:
                agent.environment = self
                self.agents.append(agent)
                self.name_to_agent[agent.name] = agent
            else:
                raise ValueError(f"Имена агентов должны быть уникальными, но \'{agent.name}\' уже есть в окружении.")
        else:
            logger.warn(f"Агент {agent.name} уже в окружении.")
        
        return self # for chaining

    def remove_agent(self, agent: TinyPerson) -> Self:
        """
        Удаляет агента из окружения.

        Args:
            agent (TinyPerson): Агент для удаления.

        Returns:
            Self: Возвращает self для цепочного вызова.
        """
        logger.debug(f"Удаление агента {agent.name} из окружения.")
        self.agents.remove(agent)
        del self.name_to_agent[agent.name]

        return self # for chaining
    
    def remove_all_agents(self) -> Self:
        """
        Удаляет всех агентов из окружения.

        Returns:
            Self: Возвращает self для цепочного вызова.
        """
        logger.debug(f"Удаление всех агентов из окружения.")
        self.agents = []
        self.name_to_agent = {}

        return self # for chaining

    def get_agent_by_name(self, name: str) -> TinyPerson | None:
        """
        Возвращает агента по имени. Если агента нет, возвращает None.

        Args:
            name (str): Имя агента для поиска.

        Returns:
            TinyPerson: Агент с указанным именем, или None.
        """
        if name in self.name_to_agent:
            return self.name_to_agent[name]
        else:
            return None
    
    #######################################################################
    # Обработчики действий
    #######################################################################
    @transactional
    def _handle_actions(self, source: TinyPerson, actions: List[dict]):
        """
        Обрабатывает действия, выполненные агентами.

        Args:
            source (TinyPerson): Агент, выполнивший действия.
            actions (list): Список действий агента.
        """
        for action in actions:
            action_type = action['type']
            content = action.get('content')
            target = action.get('target')

            logger.debug(f"[{self.name}] Обработка действия {action_type} от агента {name_or_empty(source)}. Содержание: {content}, цель: {target}.")

            if action_type == 'REACH_OUT':
                self._handle_reach_out(source, content, target)
            elif action_type == 'TALK':
                self._handle_talk(source, content, target)

    @transactional
    def _handle_reach_out(self, source_agent: TinyPerson, content: str, target: str):
        """
        Обрабатывает действие REACH_OUT.

        Args:
            source_agent (TinyPerson): Агент, инициирующий действие.
            content (str): Содержание сообщения.
            target (str): Цель сообщения.
        """
        target_agent = self.get_agent_by_name(target)
        
        source_agent.make_agent_accessible(target_agent)
        target_agent.make_agent_accessible(source_agent)

        source_agent.socialize(f"{name_or_empty(target_agent)} был успешно достигнут, и теперь доступен для взаимодействия.", source=self)
        target_agent.socialize(f"{name_or_empty(source_agent)} обратился к вам, и теперь доступен для взаимодействия.", source=self)

    @transactional
    def _handle_talk(self, source_agent: TinyPerson, content: str, target: str):
        """
        Обрабатывает действие TALK, доставляя сообщение цели.

        Args:
            source_agent (TinyPerson): Агент, инициирующий действие.
            content (str): Содержание сообщения.
            target (str): Цель сообщения.
        """
        target_agent = self.get_agent_by_name(target)

        logger.debug(f"[{self.name}] Доставка сообщения от {name_or_empty(source_agent)} к {name_or_empty(target_agent)}.")

        if target_agent is not None:
            target_agent.listen(content, source=source_agent)
        elif self.broadcast_if_no_target:
            self.broadcast(content, source=source_agent)

    #######################################################################
    # Методы взаимодействия
    #######################################################################
    @transactional
    def broadcast(self, speech: str, source: AgentOrWorld=None):
        """
        Рассылает сообщение всем агентам в окружении.

        Args:
            speech (str): Содержание сообщения.
            source (AgentOrWorld): Агент или окружение, отправившее сообщение.
        """
        logger.debug(f"[{self.name}] Рассылка сообщения: \'{speech}\'.")

        for agent in self.agents:
            if agent != source:
                agent.listen(speech, source=source)
    
    @transactional
    def broadcast_thought(self, thought: str, source: AgentOrWorld=None):
        """
        Рассылает мысль всем агентам в окружении.

        Args:
            thought (str): Содержание мысли.
        """
        logger.debug(f"[{self.name}] Рассылка мысли: \'{thought}\'.")

        for agent in self.agents:
            agent.think(thought)
    
    @transactional
    def broadcast_internal_goal(self, internal_goal: str):
        """
        Рассылает внутреннюю цель всем агентам в окружении.

        Args:
            internal_goal (str): Содержание внутренней цели.
        """
        logger.debug(f"[{self.name}] Рассылка внутренней цели: \'{internal_goal}\'.")

        for agent in self.agents:
            agent.internalize_goal(internal_goal)
    
    @transactional
    def broadcast_context_change(self, context: list):
        """
        Рассылает изменение контекста всем агентам в окружении.

        Args:
            context (list): Изменение контекста.
        """
        logger.debug(f"[{self.name}] Рассылка изменения контекста: \'{context}\'.")

        for agent in self.agents:
            agent.change_context(context)

    def make_everyone_accessible(self):
        """
        Делает всех агентов доступными друг для друга.
        """
        for agent_1 in self.agents:
            for agent_2 in self.agents:
                if agent_1 != agent_2:
                    agent_1.make_agent_accessible(agent_2)
            

    ###########################################################
    # Удобства форматирования
    ###########################################################

    def _display_communication(self, cur_step: int, total_steps: int, kind: str, timedelta_per_step: timedelta = None):
        """
        Отображает текущее сообщение и сохраняет его в буфере.

        Args:
            cur_step (int): Текущий шаг симуляции.
            total_steps (int): Общее количество шагов симуляции.
            kind (str): Тип сообщения.
            timedelta_per_step (timedelta, optional): Временной интервал между шагами.
        """
        if kind == 'step':
            rendering = self._pretty_step(cur_step=cur_step, total_steps=total_steps, timedelta_per_step=timedelta_per_step)
        else:
            raise ValueError(f"Неизвестный тип сообщения: {kind}")

        self._push_and_display_latest_communication({"content": rendering, "kind": kind})
    
    def _push_and_display_latest_communication(self, rendering: dict):
        """
        Сохраняет последнее сообщение в буфер и отображает его.

        Args:
            rendering (dict): Сообщение для отображения.
        """
        self._displayed_communications_buffer.append(rendering)
        self._display(rendering)

    def pop_and_display_latest_communications(self) -> list:
        """
        Извлекает и отображает все последние сообщения.

        Returns:
            list: Список сообщений.
        """
        communications = self._displayed_communications_buffer
        self._displayed_communications_buffer = []

        for communication in communications:
            self._display(communication)

        return communications    

    def _display(self, communication: dict | str):
        """
        Отображает сообщение.

        Args:
            communication (dict|str): Сообщение для отображения.
        """
        if isinstance(communication, dict):
            content = communication["content"]
            kind = communication["kind"]
        else:
            content = communication
            kind = None
        
        if kind == 'step':
            self.console.rule(content)
        else:
            self.console.print(content)
    
    def clear_communications_buffer(self):
        """
        Очищает буфер сообщений.
        """
        self._displayed_communications_buffer = []

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Строковое представление объекта.
        """
        return f"TinyWorld(name='{self.name}')"

    def _pretty_step(self, cur_step: int, total_steps: int, timedelta_per_step: timedelta = None) -> str:
        """
        Форматирует сообщение о шаге.

        Args:
            cur_step (int): Текущий шаг.
            total_steps (int): Общее количество шагов.
            timedelta_per_step (timedelta, optional): Временной интервал между шагами.

        Returns:
            str: Отформатированное сообщение о шаге.
        """
        rendering = f"{self.name} шаг {cur_step} из {total_steps}"
        if timedelta_per_step is not None:
            rendering += f" ({pretty_datetime(self.current_datetime)})"

        return rendering

    def pp_current_interactions(self, simplified: bool = True, skip_system: bool = True):
        """
        Выводит в консоль текущие сообщения агентов.

        Args:
            simplified (bool, optional): Если True, вывод упрощен. Defaults to True.
            skip_system (bool, optional): Если True, системные сообщения пропускаются. Defaults to True.
        """
        print(self.pretty_current_interactions(simplified=simplified, skip_system=skip_system))

    def pretty_current_interactions(self, simplified: bool = True, skip_system: bool = True, max_content_length: int = default["max_content_display_length"], first_n:int = None, last_n:int = None, include_omission_info:bool = True) -> str:
        """
        Возвращает отформатированную строку с сообщениями агентов.

        Args:
            simplified (bool, optional): Если True, вывод упрощен. Defaults to True.
            skip_system (bool, optional): Если True, системные сообщения пропускаются. Defaults to True.
            max_content_length (int, optional): Максимальная длина сообщения. Defaults to default["max_content_display_length"].
            first_n (int, optional): Количество первых сообщений для отображения. Defaults to None.
            last_n (int, optional): Количество последних сообщений для отображения. Defaults to None.
            include_omission_info (bool, optional): Если True, то выводится информация о пропущенных сообщениях. Defaults to True.

        Returns:
             str: Отформатированная строка с сообщениями агентов.
        """
        agent_contents = []

        for agent in self.agents:
            agent_content = f"#### Взаимодействия от лица агента {agent.name}:\\n"
            agent_content += f"**НАЧАЛО ИСТОРИИ АГЕНТА {agent.name}.**\\n "
            agent_content += agent.pretty_current_interactions(simplified=simplified, skip_system=skip_system, max_content_length=max_content_length, first_n=first_n, last_n=last_n, include_omission_info=include_omission_info) + "\\n"
            agent_content += f"**КОНЕЦ ИСТОРИИ АГЕНТА {agent.name}.**\\n\\n"
            agent_contents.append(agent_content)
            
        return "\\n".join(agent_contents)
    
    #######################################################################
    # IO
    #######################################################################

    def encode_complete_state(self) -> dict:
        """
        Кодирует полное состояние окружения в словарь.

        Returns:
            dict: Словарь, содержащий полное состояние окружения.
        """
        to_copy = copy.copy(self.__dict__)

        del to_copy['console']
        del to_copy['agents']
        del to_copy['name_to_agent']
        del to_copy['current_datetime']

        state = copy.deepcopy(to_copy)

        state["agents"] = [agent.encode_complete_state() for agent in self.agents]
        state["current_datetime"] = self.current_datetime.isoformat()

        return state
    
    def decode_complete_state(self, state: dict) -> Self:
        """
        Декодирует полное состояние окружения из словаря.

        Args:
            state (dict): Словарь с состоянием окружения.

        Returns:
            Self: Восстановленное окружение.
        """
        state = copy.deepcopy(state)

        self.remove_all_agents()
        for agent_state in state["agents"]:
            try:
                try:
                    agent = TinyPerson.get_agent_by_name(agent_state["name"])
                except Exception as e:
                    raise ValueError(f"Не удалось найти агента {agent_state['name']} для окружения {self.name}.") from e
                
                agent.decode_complete_state(agent_state)
                self.add_agent(agent)
                
            except Exception as e:
                raise ValueError(f"Не удалось декодировать агента {agent_state['name']} для окружения {self.name}.") from e
        
        del state["agents"]
        state["current_datetime"] = datetime.fromisoformat(state["current_datetime"])

        self.__dict__.update(state)

        return self

    @staticmethod
    def add_environment(environment: Self):
        """
        Добавляет окружение в список всех окружений. Имена должны быть уникальными.

        Args:
            environment (TinyWorld): Окружение для добавления.

        Raises:
            ValueError: Если имя окружения не уникально.
        """
        if environment.name in TinyWorld.all_environments:
            raise ValueError(f"Имена окружений должны быть уникальными, но \'{environment.name}\' уже определено.")
        else:
            TinyWorld.all_environments[environment.name] = environment
        

    @staticmethod
    def set_simulation_for_free_environments(simulation: Any):
        """
        Устанавливает симуляцию для свободных окружений.

        Args:
            simulation (Any): Симуляция для установки.
        """
        for environment in TinyWorld.all_environments.values():
            if environment.simulation_id is None:
                simulation.add_environment(environment)
    
    @staticmethod
    def get_environment_by_name(name: str) -> Self | None:
        """
        Возвращает окружение по имени.

        Args:
            name (str): Имя окружения для поиска.

        Returns:
            TinyWorld: Окружение с указанным именем.
        """
        if name in TinyWorld.all_environments:
            return TinyWorld.all_environments[name]
        else:
            return None
    
    @staticmethod
    def clear_environments():
        """
        Очищает список всех окружений.
        """
        TinyWorld.all_environments = {}

class TinySocialNetwork(TinyWorld):
    """
    Класс для социальных сетей, расширяет TinyWorld.

    Атрибуты:
        relations (dict): Словарь отношений между агентами.
    """
    def __init__(self, name: str, broadcast_if_no_target: bool = True):
        """
        Создает новую социальную сеть.

        Args:
            name (str): Имя социальной сети.
            broadcast_if_no_target (bool): Если True, транслирует действия через отношения.
        """
        super().__init__(name, broadcast_if_no_target=broadcast_if_no_target)
        self.relations = {}
    
    @transactional
    def add_relation(self, agent_1: TinyPerson, agent_2: TinyPerson, name: str = "default") -> Self:
        """
        Добавляет отношение между двумя агентами.

        Args:
            agent_1 (TinyPerson): Первый агент.
            agent_2 (TinyPerson): Второй агент.
            name (str): Имя отношения.

        Returns:
            Self: Возвращает self для цепочного вызова.
        """
        logger.debug(f"Добавление отношения {name} между {agent_1.name} и {agent_2.name}.")

        if agent_1 not in self.agents:
            self.agents.append(agent_1)
        if agent_2 not in self.agents:
            self.agents.append(agent_2)

        if name in self.relations:
            self.relations[name].append((agent_1, agent_2))
        else:
            self.relations[name] = [(agent_1, agent_2)]

        return self # for chaining
    
    @transactional
    def _update_agents_contexts(self):
        """
        Обновляет контекст агентов на основе текущего состояния мира.
        """
        for agent in self.agents:
            agent.make_all_agents_inaccessible()

        for relation_name, relation in self.relations.items():
            logger.debug(f"Обновление контекста агентов для отношения {relation_name}.")
            for agent_1, agent_2 in relation:
                agent_1.make_agent_accessible(agent_2)
                agent_2.make_