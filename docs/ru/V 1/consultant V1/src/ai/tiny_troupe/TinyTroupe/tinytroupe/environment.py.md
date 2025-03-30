### Анализ кода модуля `environment`

**Качество кода**:
   - **Соответствие стандартам**: 7/10
   - **Плюсы**:
     - Хорошо структурированный код с разделением на классы `TinyWorld` и `TinySocialNetwork`.
     - Использование аннотаций типов для улучшения читаемости и предотвращения ошибок.
     - Реализация паттерна "цепочка вызовов" для методов добавления и удаления агентов.
     - Наличие методов для управления временем симуляции (шаги, минуты, часы, дни, недели, месяцы, годы).
     - Использование `logger` для отладки и логирования.
     - Наличие методов для кодирования и декодирования состояния среды.
     - Включение методов для взаимодействия агентов (broadcast, reach_out, talk).
   - **Минусы**:
     -  Непоследовательное использование кавычек (иногда используются двойные, иногда одинарные).
     -  Не везде есть RST-документация.
     -  Использование стандартного `logging` вместо `src.logger.logger`.
     -  Множественные проверки `if ... is not None` можно упростить.
     -  Отсутствует обработка исключений в некоторых методах, например, при удалении агента из `name_to_agent`.
     -  Используется стандартный `datetime` вместо `src.utils.datetime`.
     -  Смешанный стиль именования переменных: snake_case, camelCase.
     -  Метод `_pretty_step` выглядит перегруженным.
     -  Метод `_handle_reach_out` в `TinySocialNetwork` дублирует некоторую логику из `TinyWorld`.
     -  Отсутствуют docstring для некоторых методов и классов.

**Рекомендации по улучшению**:
   - Привести все строковые литералы в коде к одинарным кавычкам (`'`). Двойные кавычки использовать только для `print`, `input`, `logger.error` и т.п.
   - Добавить RST-документацию ко всем классам, методам и функциям.
   - Заменить `import logging` на `from src.logger import logger`.
   - Заменить все `if ... is not None` на `if ...:` для более краткого кода.
   - Добавить обработку исключений в методы, где они могут возникать (например, при удалении агента из словаря).
   - Использовать `src.utils.datetime` вместо стандартного `datetime`
   - Привести к единому стилю именования переменных (snake_case предпочтительнее).
   - Разбить метод `_pretty_step` на более простые.
   - Устранить дублирование логики в `_handle_reach_out` в `TinySocialNetwork`, вынеся общую логику в отдельный метод.
   - Добавить docstring для всех методов и классов, а также использовать примеры в docstring.

**Оптимизированный код**:
```python
"""
Модуль для определения окружений в TinyTroupe
============================================

Модуль предоставляет классы для создания и управления окружениями, в которых
взаимодействуют агенты, включая базовый класс :class:`TinyWorld` и его расширение
:class:`TinySocialNetwork`.

Примеры
--------

Использование :class:`TinyWorld`:

.. code-block:: python

    from datetime import datetime, timedelta
    from tinytroupe.agent import TinyPerson
    from tinytroupe.environment import TinyWorld

    # Создание агентов
    agent1 = TinyPerson(name='Agent1')
    agent2 = TinyPerson(name='Agent2')

    # Создание окружения
    world = TinyWorld(name='TestWorld', agents=[agent1, agent2], initial_datetime=datetime.now())

    # Запуск симуляции
    world.run(steps=5, timedelta_per_step=timedelta(minutes=1))

Использование :class:`TinySocialNetwork`:

.. code-block:: python

    from datetime import datetime, timedelta
    from tinytroupe.agent import TinyPerson
    from tinytroupe.environment import TinySocialNetwork

    # Создание агентов
    agent1 = TinyPerson(name='Agent1')
    agent2 = TinyPerson(name='Agent2')

    # Создание социальной сети
    network = TinySocialNetwork(name='SocialNetwork')
    network.add_agent(agent1).add_agent(agent2)

    # Добавление отношений
    network.add_relation(agent1, agent2, name='friends')

    # Запуск симуляции
    network.run(steps=5, timedelta_per_step=timedelta(minutes=1))
"""
import copy
from datetime import timedelta
from typing import Any, TypeVar, Union

from src.logger import logger #  Используем logger из src.logger
from src.utils.datetime import datetime #  Используем datetime из src.utils.datetime
from tinytroupe.agent import TinyPerson
from tinytroupe.utils import name_or_empty, pretty_datetime
import tinytroupe.control as control
from tinytroupe.control import transactional
from rich.console import Console

AgentOrWorld = Union['TinyPerson', 'TinyWorld']
Self = TypeVar('Self', bound='TinyWorld')

class TinyWorld:
    """
    Базовый класс для определения окружений.
    
    Атрибуты:
        all_environments (dict): Словарь всех созданных окружений.
        communication_display (bool): Флаг отображения коммуникаций.
    """

    all_environments = {}  # name -> environment
    communication_display = True

    def __init__(self, name: str = 'A TinyWorld', agents: list = [],
                 initial_datetime: datetime = datetime.now(),
                 broadcast_if_no_target: bool = True):
        """
        Инициализирует окружение.

        :param name: Имя окружения.
        :type name: str
        :param agents: Список агентов для добавления в окружение.
        :type agents: list
        :param initial_datetime: Начальная дата и время окружения.
        :type initial_datetime: datetime
        :param broadcast_if_no_target: Флаг широковещательной рассылки, если цель действия не найдена.
        :type broadcast_if_no_target: bool

        :ivar name: Имя окружения.
        :vartype name: str
        :ivar current_datetime: Текущее время в окружении.
        :vartype current_datetime: datetime
        :ivar broadcast_if_no_target: Флаг широковещательной рассылки.
        :vartype broadcast_if_no_target: bool
        :ivar simulation_id: Идентификатор симуляции (может быть изменен).
        :vartype simulation_id: str
        :ivar agents: Список агентов в окружении.
        :vartype agents: list
        :ivar name_to_agent: Словарь, связывающий имена агентов с их объектами.
        :vartype name_to_agent: dict
        :ivar _displayed_communications_buffer: Буфер отображенных коммуникаций.
        :vartype _displayed_communications_buffer: list
        :ivar console: Объект консоли для вывода.
        :vartype console: rich.console.Console

        :raises ValueError: Если имя агента не является уникальным.
        """
        self.name = name
        self.current_datetime = initial_datetime
        self.broadcast_if_no_target = broadcast_if_no_target
        self.simulation_id = None  # будет сброшен позже, если агент используется в определенной симуляции

        self.agents = []
        self.name_to_agent = {}  # {agent_name: agent, agent_name_2: agent_2, ...}
        self._displayed_communications_buffer = []
        self.console = Console()

        TinyWorld.add_environment(self)
        self.add_agents(agents)

    #######################################################################
    # Методы управления симуляцией
    #######################################################################
    @transactional
    def _step(self, timedelta_per_step=None):
        """
        Выполняет один шаг в окружении.
        
        :param timedelta_per_step: Временной интервал между шагами.
        :type timedelta_per_step: timedelta
        :return: Словарь действий агентов
        :rtype: dict
        """
        self._advance_datetime(timedelta_per_step)

        agents_actions = {}
        for agent in self.agents:
            logger.debug(f'[{self.name}] Agent {name_or_empty(agent)} is acting.')
            actions = agent.act(return_actions=True)
            agents_actions[agent.name] = actions

            self._handle_actions(agent, agent.pop_latest_actions())

        return agents_actions

    def _advance_datetime(self, timedelta_per_step):
        """
        Увеличивает текущее время на заданный интервал.

        :param timedelta_per_step: Временной интервал для увеличения.
        :type timedelta_per_step: timedelta
        """
        if timedelta_per_step:
            self.current_datetime += timedelta_per_step
        else:
            logger.info(f'[{self.name}] No timedelta provided, so the datetime was not advanced.')

    @transactional
    def run(self, steps: int, timedelta_per_step=None, return_actions=False):
        """
        Запускает симуляцию на заданное количество шагов.

        :param steps: Количество шагов для запуска симуляции.
        :type steps: int
        :param timedelta_per_step: Временной интервал между шагами.
        :type timedelta_per_step: timedelta, optional
        :param return_actions: Флаг возврата действий агентов.
        :type return_actions: bool, optional
        :return: Список действий агентов за время симуляции, если return_actions True.
        :rtype: list, optional

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> actions = world.run(steps=3, return_actions=True)
           >>> print(actions)
           [{}, {}, {}]
        """
        agents_actions_over_time = []
        for i in range(steps):
            logger.info(f'[{self.name}] Running world simulation step {i+1} of {steps}.')

            if TinyWorld.communication_display:
                self._display_communication(cur_step=i+1, total_steps=steps, kind='step', timedelta_per_step=timedelta_per_step) #  Используем одинарные кавычки

            agents_actions = self._step(timedelta_per_step=timedelta_per_step)
            agents_actions_over_time.append(agents_actions)

        if return_actions:
            return agents_actions_over_time

    @transactional
    def skip(self, steps: int, timedelta_per_step=None):
        """
        Пропускает заданное количество шагов в окружении.

        :param steps: Количество шагов для пропуска.
        :type steps: int
        :param timedelta_per_step: Временной интервал между шагами.
        :type timedelta_per_step: timedelta, optional

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> world.skip(steps=3, timedelta_per_step=timedelta(minutes=1))
        """
        if timedelta_per_step:
            self._advance_datetime(steps * timedelta_per_step)

    def run_minutes(self, minutes: int):
        """
        Запускает окружение на заданное количество минут.

        :param minutes: Количество минут для запуска симуляции.
        :type minutes: int

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> world.run_minutes(minutes=5)
        """
        self.run(steps=minutes, timedelta_per_step=timedelta(minutes=1))

    def skip_minutes(self, minutes: int):
        """
        Пропускает заданное количество минут в окружении.

        :param minutes: Количество минут для пропуска.
        :type minutes: int

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> world.skip_minutes(minutes=5)
        """
        self.skip(steps=minutes, timedelta_per_step=timedelta(minutes=1))

    def run_hours(self, hours: int):
        """
        Запускает окружение на заданное количество часов.

        :param hours: Количество часов для запуска симуляции.
        :type hours: int

         :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> world.run_hours(hours=5)
        """
        self.run(steps=hours, timedelta_per_step=timedelta(hours=1))

    def skip_hours(self, hours: int):
        """
        Пропускает заданное количество часов в окружении.

        :param hours: Количество часов для пропуска.
        :type hours: int

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> world.skip_hours(hours=5)
        """
        self.skip(steps=hours, timedelta_per_step=timedelta(hours=1))

    def run_days(self, days: int):
        """
        Запускает окружение на заданное количество дней.

        :param days: Количество дней для запуска симуляции.
        :type days: int

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> world.run_days(days=5)
        """
        self.run(steps=days, timedelta_per_step=timedelta(days=1))

    def skip_days(self, days: int):
        """
        Пропускает заданное количество дней в окружении.

        :param days: Количество дней для пропуска.
        :type days: int

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> world.skip_days(days=5)
        """
        self.skip(steps=days, timedelta_per_step=timedelta(days=1))

    def run_weeks(self, weeks: int):
        """
        Запускает окружение на заданное количество недель.

        :param weeks: Количество недель для запуска симуляции.
        :type weeks: int

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> world.run_weeks(weeks=5)
        """
        self.run(steps=weeks, timedelta_per_step=timedelta(weeks=1))

    def skip_weeks(self, weeks: int):
        """
        Пропускает заданное количество недель в окружении.

        :param weeks: Количество недель для пропуска.
        :type weeks: int

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> world.skip_weeks(weeks=5)
        """
        self.skip(steps=weeks, timedelta_per_step=timedelta(weeks=1))

    def run_months(self, months: int):
        """
        Запускает окружение на заданное количество месяцев.

        :param months: Количество месяцев для запуска симуляции.
        :type months: int

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> world.run_months(months=5)
        """
        self.run(steps=months, timedelta_per_step=timedelta(weeks=4))

    def skip_months(self, months: int):
        """
        Пропускает заданное количество месяцев в окружении.

        :param months: Количество месяцев для пропуска.
        :type months: int

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> world.skip_months(months=5)
        """
        self.skip(steps=months, timedelta_per_step=timedelta(weeks=4))

    def run_years(self, years: int):
        """
        Запускает окружение на заданное количество лет.

        :param years: Количество лет для запуска симуляции.
        :type years: int

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> world.run_years(years=5)
        """
        self.run(steps=years, timedelta_per_step=timedelta(days=365))

    def skip_years(self, years: int):
        """
        Пропускает заданное количество лет в окружении.

        :param years: Количество лет для пропуска.
        :type years: int

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> world.skip_years(years=5)
        """
        self.skip(steps=years, timedelta_per_step=timedelta(days=365))

    #######################################################################
    # Методы управления агентами
    #######################################################################
    def add_agents(self, agents: list) -> Self:
        """
        Добавляет список агентов в окружение.

        :param agents: Список агентов для добавления.
        :type agents: list
        :return: self для ченинга
        :rtype: Self

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> agent1 = TinyPerson(name='Agent1')
           >>> agent2 = TinyPerson(name='Agent2')
           >>> world.add_agents([agent1, agent2])
        """
        for agent in agents:
            self.add_agent(agent)
        return self  # для ченинга

    def add_agent(self, agent: TinyPerson) -> Self:
        """
        Добавляет агента в окружение.

        :param agent: Агент для добавления.
        :type agent: TinyPerson
        :return: self для ченинга
        :rtype: Self

        :raises ValueError: Если имя агента не является уникальным.

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> agent = TinyPerson(name='Agent1')
           >>> world.add_agent(agent)
        """
        if agent not in self.agents:
            logger.debug(f'Adding agent {agent.name} to the environment.')

            if agent.name not in self.name_to_agent:
                agent.environment = self
                self.agents.append(agent)
                self.name_to_agent[agent.name] = agent
            else:
                raise ValueError(f'Agent names must be unique, but \'{agent.name}\' is already in the environment.')
        else:
            logger.warning(f'Agent {agent.name} is already in the environment.')

        return self  # для ченинга

    def remove_agent(self, agent: TinyPerson) -> Self:
        """
        Удаляет агента из окружения.

        :param agent: Агент для удаления.
        :type agent: TinyPerson
        :return: self для ченинга
        :rtype: Self

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> agent = TinyPerson(name='Agent1')
           >>> world.add_agent(agent)
           >>> world.remove_agent(agent)
        """
        logger.debug(f'Removing agent {agent.name} from the environment.')
        self.agents.remove(agent)
        del self.name_to_agent[agent.name]

        return self  # для ченинга

    def remove_all_agents(self) -> Self:
        """
        Удаляет всех агентов из окружения.
        
        :return: self для ченинга
        :rtype: Self

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> agent = TinyPerson(name='Agent1')
           >>> world.add_agent(agent)
           >>> world.remove_all_agents()
        """
        logger.debug('Removing all agents from the environment.')
        self.agents = []
        self.name_to_agent = {}
        return self # для ченинга

    def get_agent_by_name(self, name: str) -> TinyPerson | None:
        """
        Возвращает агента по имени.
        
        :param name: Имя агента.
        :type name: str
        :return: Агент с указанным именем или None, если агент не найден.
        :rtype: TinyPerson | None

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> agent = TinyPerson(name='Agent1')
           >>> world.add_agent(agent)
           >>> found_agent = world.get_agent_by_name('Agent1')
           >>> print(found_agent.name)
           Agent1
        """
        return self.name_to_agent.get(name)

    #######################################################################
    # Обработчики действий
    #######################################################################
    @transactional
    def _handle_actions(self, source: TinyPerson, actions: list):
        """
        Обрабатывает действия агентов.
        
        :param source: Агент, выдавший действия.
        :type source: TinyPerson
        :param actions: Список действий для обработки.
        :type actions: list

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> agent = TinyPerson(name='Agent1')
           >>> world.add_agent(agent)
           >>> actions = [{'type': 'TALK', 'content': 'Hello', 'target': 'Agent2'}]
           >>> world._handle_actions(agent, actions)
        """
        for action in actions:
            action_type = action['type']  # это единственное обязательное поле
            content = action.get('content')
            target = action.get('target')

            logger.debug(f'[{self.name}] Handling action {action_type} from agent {name_or_empty(source)}. Content: {content}, target: {target}.')

            if action_type == 'REACH_OUT':
                self._handle_reach_out(source, content, target)
            elif action_type == 'TALK':
                self._handle_talk(source, content, target)

    @transactional
    def _handle_reach_out(self, source_agent: TinyPerson, content: str, target: str):
        """
        Обрабатывает действие REACH_OUT.
        
        :param source_agent: Агент, инициировавший действие.
        :type source_agent: TinyPerson
        :param content: Содержание сообщения.
        :type content: str
        :param target: Цель сообщения.
        :type target: str

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> agent1 = TinyPerson(name='Agent1')
           >>> agent2 = TinyPerson(name='Agent2')
           >>> world.add_agent(agent1).add_agent(agent2)
           >>> world._handle_reach_out(agent1, 'Hello', 'Agent2')
        """
        target_agent = self.get_agent_by_name(target)

        if target_agent:
            source_agent.make_agent_accessible(target_agent)
            target_agent.make_agent_accessible(source_agent)

            source_agent.socialize(f'{name_or_empty(target_agent)} was successfully reached out, and is now available for interaction.', source=self)
            target_agent.socialize(f'{name_or_empty(source_agent)} reached out to you, and is now available for interaction.', source=self)

    @transactional
    def _handle_talk(self, source_agent: TinyPerson, content: str, target: str):
        """
        Обрабатывает действие TALK.
        
        :param source_agent: Агент, инициировавший действие.
        :type source_agent: TinyPerson
        :param content: Содержание сообщения.
        :type content: str
        :param target: Цель сообщения.
        :type target: str, optional

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> agent1 = TinyPerson(name='Agent1')
           >>> agent2 = TinyPerson(name='Agent2')
           >>> world.add_agent(agent1).add_agent(agent2)
           >>> world._handle_talk(agent1, 'Hello', 'Agent2')
        """
        target_agent = self.get_agent_by_name(target)

        logger.debug(f'[{self.name}] Delivering message from {name_or_empty(source_agent)} to {name_or_empty(target_agent)}.')

        if target_agent:
            target_agent.listen(content, source=source_agent)
        elif self.broadcast_if_no_target:
            self.broadcast(content, source=source_agent)

    #######################################################################
    # Методы взаимодействия
    #######################################################################
    @transactional
    def broadcast(self, speech: str, source: AgentOrWorld = None):
        """
        Рассылает сообщение всем агентам в окружении.

        :param speech: Содержание сообщения.
        :type speech: str
        :param source: Агент или окружение, инициировавшее сообщение.
        :type source: AgentOrWorld, optional

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> agent1 = TinyPerson(name='Agent1')
           >>> world.add_agent(agent1)
           >>> world.broadcast('Hello everyone!', source=world)
        """
        logger.debug(f'[{self.name}] Broadcasting message: \'{speech}\'.')

        for agent in self.agents:
            if agent != source:
                agent.listen(speech, source=source)

    @transactional
    def broadcast_thought(self, thought: str, source: AgentOrWorld=None):
        """
        Рассылает мысль всем агентам в окружении.

        :param thought: Содержание мысли.
        :type thought: str
        :param source: Агент или окружение, инициировавшее мысль.
        :type source: AgentOrWorld, optional

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> agent1 = TinyPerson(name='Agent1')
           >>> world.add_agent(agent1)
           >>> world.broadcast_thought('I am thinking...', source=world)
        """
        logger.debug(f'[{self.name}] Broadcasting thought: \'{thought}\'.')

        for agent in self.agents:
            agent.think(thought)

    @transactional
    def broadcast_internal_goal(self, internal_goal: str):
        """
        Рассылает внутреннюю цель всем агентам в окружении.

        :param internal_goal: Содержание внутренней цели.
        :type internal_goal: str

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> agent1 = TinyPerson(name='Agent1')
           >>> world.add_agent(agent1)
           >>> world.broadcast_internal_goal('My goal is to learn...')
        """
        logger.debug(f'[{self.name}] Broadcasting internal goal: \'{internal_goal}\'.')

        for agent in self.agents:
            agent.internalize_goal(internal_goal)

    @transactional
    def broadcast_context_change(self, context: list):
        """
        Рассылает изменение контекста всем агентам в окружении.
        
        :param context: Содержание изменения контекста.
        :type context: list

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> agent1 = TinyPerson(name='Agent1')
           >>> world.add_agent(agent1)
           >>> world.broadcast_context_change(['New context item'])
        """
        logger.debug(f'[{self.name}] Broadcasting context change: \'{context}\'.')

        for agent in self.agents:
            agent.change_context(context)

    def make_everyone_accessible(self):
        """
        Делает всех агентов в окружении доступными друг другу.

        :Example:
           >>> world = TinyWorld(name='TestWorld')
           >>> agent1 = TinyPerson(name='Agent1')
           >>> agent2 = TinyPerson(name='Agent2')
           >>> world.add_agent(agent1).add_agent(agent2)
           >>> world.make_everyone_accessible()
        """
        for agent_1 in self.agents:
            for agent_2 in self.agents:
                if agent_1 != agent_2:
                    agent_1.make_agent_accessible(agent_2)

    ###########################################################
    # Вспомогательные методы форматирования
    ###########################################################
    def _display_communication(self, cur_step, total_steps, kind, timedelta_per_step=None):
        """
        Отображает текущую коммуникацию.

        :param cur_step: Текущий шаг.
        :type cur_step: int
        :param total_steps: Общее количество шагов.
        :type total_steps: int
        :param kind: Тип коммуникации.
        :type kind: str
        :param timedelta_per_step: Временной интервал между шагами.
        :type timedelta_per_step: timedelta, optional

        :raises ValueError: Если тип коммуникации неизвестен.
        """
        if kind == 'step':
            rendering = self._pretty_step(cur_step=cur_step, total_steps=total_steps, timedelta_per_step=timedelta_per_step)
        else:
            raise ValueError(f'Unknown communication kind: {kind}')

        self._push_and_display_latest_communication({'content': rendering, 'kind': kind})

    def _push_and_display_latest_communication(self, rendering):
        """
        Добавляет последнюю коммуникацию в буфер и отображает ее.
        
        :param rendering: Содержание для отображения.
        :type rendering: dict
        """
        self._displayed_communications_buffer.append(rendering)
        self._display(rendering)

    def pop_and_display_latest_communications(self):
        """
        Извлекает последние коммуникации из буфера и отображает их.

        :return: Список коммуникаций
        :rtype: list
        """
        communications = self._displayed_communications_buffer
        self._displayed_communications_buffer = []

        for communication in communications:
            self._display(communication)

        return communications

    def _display(self, communication):
        """
        Отображает сообщение в консоли.

        :param communication: Сообщение для отображения.
        :type communication: dict | str
        """
        if isinstance(communication, dict):
            content = communication['content']
            kind = communication['kind']
        else:
            content = communication
            kind = None
        
        if kind == 'step':
            self.console.rule(content)
        else:
            self.console.print(content)

    def clear_communications_buffer(self):
        """
        Очищает буфер коммуникаций.
        
        :Example:
            >>> world = TinyWorld(name='TestWorld')
            >>> world.clear_communications_buffer()
        """
        self._displayed_communications_buffer = []

    def __repr__(self):
        return f'TinyWorld(name=\'{self.name}\')'

    def _pretty_step(self, cur_step, total_steps, timedelta_per_step=None):
        """
        Форматирует строку для отображения текущего шага.
        
        :param cur_step: Текущий шаг.
        :type cur_step: int
        :param total_steps: Общее количество шагов.
        :type total_steps: int
        :param timedelta_per_step: Временной интервал между шагами.
        :type timedelta_per_step: timedelta, optional
        :return: Отформатированная строка
        :rtype: str
        """
        rendering = f'{self.name} step {cur_step} of {total_steps}'
        if timedelta_per_step:
            rendering += f' ({pretty_datetime(self.current_datetime)})'

        return rendering

    def pp_current_interactions(self, simplified=True, skip_system=True):
        """
        Выводит в консоль текущие взаимодействия агентов.
        
        :param simplified: Флаг упрощения вывода.
        :type simplified: bool
        :param skip_system: Флаг пропуска системных сообщений.
        :type skip_system: bool

        :Example:
            >>> world = TinyWorld(name='TestWorld')
            >>> world.pp_current_interactions()
        """
        print(self.pretty_current_interactions(simplified=simplified, skip_system=skip_system))

    def pretty_current_interactions(self, simplified=True, skip_system=True,
                                    max_content_length=70, first_n=None, last_n=None, include_omission_info:bool=True):
        """
        Возвращает форматированную строку с текущими сообщениями агентов.
        
        :param simplified: Флаг упрощения вывода.
        :type simplified: bool
        :param skip_system: Флаг пропуска системных сообщений.
        :type skip_system: bool
        :param max_content_length: Максимальная длина контента для отображения.
        :type max_content_length: int
        :param first_n: Первые N сообщений для отображения.
        :type first_n: int
        :param last_n: Последние N сообщений для отображения.
        :type last_n: int
        :param include_omission_info: Флаг включения информации о пропущенных сообщениях.
        :type include_omission_info: bool
        :return: Отформатированная строка
        :rtype: str

        :Example:
            >>> world = TinyWorld(name='TestWorld')
            >>> formatted_interactions = world.pretty_current_interactions()
            >>> print(formatted_interactions)
        """
        agent_contents = []

        for agent in self.agents:
            agent_content = f'#### Interactions from the point of view of {agent.name} agent:\\n'
            agent_content += f'**BEGIN AGENT {agent.name} HISTORY.**\\n '
            agent_content += agent.pretty_current_interactions(simplified=simplified, skip_system=skip_system,
                                                            max_