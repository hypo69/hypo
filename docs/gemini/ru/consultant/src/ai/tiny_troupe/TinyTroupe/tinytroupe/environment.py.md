# Анализ кода модуля `environment.py`

**Качество кода: 7/10**

-   **Плюсы**
    -   Код хорошо структурирован, с разделением на классы `TinyWorld` и `TinySocialNetwork`.
    -   Используется логирование для отслеживания действий.
    -   Реализованы методы для управления агентами и временем в симуляции.
    -   Присутствует базовая обработка ошибок.
    -   Используется `transactional` декоратор для обеспечения атомарности операций.
    -   Добавлены методы для сохранения и восстановления состояния окружения.
-   **Минусы**
    -   Отсутствует документация в формате reStructuredText (RST) для всех классов, методов и переменных.
    -   Не используется `j_loads` или `j_loads_ns` для чтения файлов.
    -   Используются стандартные блоки `try-except` без `logger.error`.
    -   В комментариях есть фразы, которые можно переформулировать для большей конкретики.
    -   Некоторые методы с `display` требуют более точного именования.
    -   Отсутствуют импорты для `Self`.
    -   Используется `datetime.datetime.now()` напрямую.

**Рекомендации по улучшению**

1.  **Документация:**
    -   Добавить docstring в формате RST для всех классов, методов и переменных.
    -   Описать назначение каждого модуля, класса, метода и переменной.
2.  **Импорты:**
    -   Добавить импорт `from typing import Self` для аннотации типа `Self`.
3.  **Обработка ошибок:**
    -   Заменить `try-except` блоки на использование `logger.error` для более эффективного логирования ошибок.
4.  **Использование `j_loads`:**
    -   В данном коде не производится чтение файлов, поэтому замена не требуется.
5.  **Рефакторинг:**
    -   Переименовать методы `_display_communication`, `_push_and_display_latest_communication`, `pop_and_display_latest_communications`, `_display` для большей ясности, например, `_render_step_info`, `_add_to_buffer_and_render`, `render_and_clear_buffer`, `_render_output`.
    -   Уточнить комментарии, избегая общих фраз, и использовать более конкретные формулировки.
    -   Избегать вызова `datetime.datetime.now()` напрямую. Создать поле в классе для начального времени, чтобы при тестах можно было его задавать.
6.  **Улучшения:**
    -   Упростить метод `_pretty_step`.
    -   Добавить проверку на существование агента в методе `is_in_relation_with`, прежде чем к нему обращаться.
    -   В классе `TinySocialNetwork` при добавлении связи между агентами использовать `self.add_agent()` вместо прямого добавления в список `self.agents`.

**Оптимизированный код**

```python
"""
Модуль предоставляет классы для создания и управления виртуальными средами,
в которых агенты могут взаимодействовать друг с другом и с окружением.
=========================================================================================

Этот модуль содержит классы :class:`TinyWorld` и :class:`TinySocialNetwork`,
которые используются для создания различных типов сред для моделирования
поведения агентов.

Пример использования
--------------------

Пример использования класса `TinyWorld`:

.. code-block:: python

    from datetime import datetime, timedelta
    from tinytroupe.environment import TinyWorld
    from tinytroupe.agent import TinyPerson
    
    world = TinyWorld(name='TestWorld', initial_datetime=datetime(2024, 1, 1, 10, 0, 0))
    agent1 = TinyPerson(name='Agent1')
    agent2 = TinyPerson(name='Agent2')
    world.add_agents([agent1, agent2])
    world.run(steps=5, timedelta_per_step=timedelta(minutes=15))
    
Пример использования класса `TinySocialNetwork`:

.. code-block:: python
    
    from datetime import datetime, timedelta
    from tinytroupe.environment import TinySocialNetwork
    from tinytroupe.agent import TinyPerson

    network = TinySocialNetwork(name='TestNetwork', initial_datetime=datetime(2024, 1, 1, 10, 0, 0))
    agent1 = TinyPerson(name='Agent1')
    agent2 = TinyPerson(name='Agent2')
    network.add_agents([agent1, agent2])
    network.add_relation(agent1, agent2, name='friends')
    network.run(steps=5, timedelta_per_step=timedelta(minutes=15))
"""
import logging
#  Инициализация логгера для модуля tinytroupe
logger = logging.getLogger('tinytroupe')
import copy
from datetime import datetime, timedelta

from tinytroupe.agent import *
#  Импорт вспомогательных функций
from tinytroupe.utils import name_or_empty, pretty_datetime
import tinytroupe.control as control
from tinytroupe.control import transactional

from rich.console import Console

from typing import Any, TypeVar, Union, Self
#  Определение типа для агентов или окружения
AgentOrWorld = Union['TinyPerson', 'TinyWorld']

class TinyWorld:
    """
    Базовый класс для создания виртуальных сред.
    
    :ivar all_environments: Словарь всех созданных сред, где ключ - имя среды, значение - объект среды.
    :vartype all_environments: dict
    :ivar communication_display: Флаг, определяющий, отображать ли сообщения в среде.
    :vartype communication_display: bool
    """

    # Словарь всех созданных сред
    all_environments = {} # name -> environment

    # Флаг, определяющий, отображать ли сообщения в среде.
    communication_display = True

    def __init__(self, name: str='A TinyWorld', agents: list =[],
                 initial_datetime: datetime =datetime.now(),
                 broadcast_if_no_target: bool =True):
        """
        Инициализирует окружение.

        :param name: Имя среды.
        :type name: str
        :param agents: Список агентов для добавления в среду.
        :type agents: list
        :param initial_datetime: Начальное время среды.
        :type initial_datetime: datetime
        :param broadcast_if_no_target: Флаг, определяющий, транслировать ли действия, если цель не найдена.
        :type broadcast_if_no_target: bool
        """

        self.name = name
        #  Устанавливает текущее время среды
        self.current_datetime = initial_datetime
        #  Флаг для трансляции действий
        self.broadcast_if_no_target = broadcast_if_no_target
        #  Идентификатор симуляции
        self.simulation_id = None # будет сброшен, если агент используется в симуляции
        
        # Список агентов в среде
        self.agents = []
        #  Словарь для быстрого доступа к агентам по имени
        self.name_to_agent = {} # {agent_name: agent, agent_name_2: agent_2, ...}

        # Буфер для сохранения отображенных сообщений
        self._displayed_communications_buffer = []

        self.console = Console()

        # Добавляет среду в список всех сред
        TinyWorld.add_environment(self)
        
        # Добавляет агентов в среду
        self.add_agents(agents)
        
    #######################################################################
    # Методы управления симуляцией
    #######################################################################
    @transactional
    def _step(self, timedelta_per_step=None):
        """
        Выполняет один шаг симуляции. По умолчанию, заставляет всех агентов
        в среде действовать и обрабатывает полученные действия.

        :param timedelta_per_step: Временной интервал для одного шага симуляции.
        :type timedelta_per_step: timedelta
        :return: Словарь действий агентов.
        :rtype: dict
        """
        #  Увеличивает текущее время перед обновлением симуляции
        self._advance_datetime(timedelta_per_step)

        #  Агенты действуют
        agents_actions = {}
        for agent in self.agents:
            logger.debug(f'[{self.name}] Agent {name_or_empty(agent)} is acting.')
            actions = agent.act(return_actions=True)
            agents_actions[agent.name] = actions

            #  Обрабатывает действия агента
            self._handle_actions(agent, agent.pop_latest_actions())
        
        return agents_actions

    def _advance_datetime(self, timedelta):
        """
        Увеличивает текущее время среды на заданный интервал.

        :param timedelta: Временной интервал для увеличения.
        :type timedelta: timedelta
        """
        if timedelta is not None:
            #  Увеличивает текущее время на заданный интервал
            self.current_datetime += timedelta
        else:
            logger.info(f'[{self.name}] No timedelta provided, so the datetime was not advanced.')

    @transactional
    def run(self, steps: int, timedelta_per_step=None, return_actions=False):
        """
        Запускает симуляцию на заданное количество шагов.

        :param steps: Количество шагов для выполнения симуляции.
        :type steps: int
        :param timedelta_per_step: Временной интервал между шагами.
        :type timedelta_per_step: timedelta, optional
        :param return_actions: Флаг, определяющий, возвращать ли действия агентов.
        :type return_actions: bool, optional
        :return: Список действий агентов за все шаги, если return_actions=True.
        :rtype: list, optional
        """
        agents_actions_over_time = []
        for i in range(steps):
            logger.info(f'[{self.name}] Running world simulation step {i+1} of {steps}.')

            if TinyWorld.communication_display:
                self._render_step_info(cur_step=i+1, total_steps=steps, kind='step', timedelta_per_step=timedelta_per_step)

            agents_actions = self._step(timedelta_per_step=timedelta_per_step)
            agents_actions_over_time.append(agents_actions)
        
        if return_actions:
            return agents_actions_over_time
    
    @transactional
    def skip(self, steps: int, timedelta_per_step=None):
        """
        Пропускает заданное количество шагов в среде, не вызывая действий агентов.

        :param steps: Количество шагов для пропуска.
        :type steps: int
        :param timedelta_per_step: Временной интервал между шагами.
        :type timedelta_per_step: timedelta, optional
        """
        #  Увеличивает текущее время на заданный интервал, пропуская шаги
        self._advance_datetime(steps * timedelta_per_step)

    def run_minutes(self, minutes: int):
        """
        Запускает симуляцию на заданное количество минут.

        :param minutes: Количество минут для запуска симуляции.
        :type minutes: int
        """
        #  Запускает симуляцию на заданное количество минут
        self.run(steps=minutes, timedelta_per_step=timedelta(minutes=1))
    
    def skip_minutes(self, minutes: int):
        """
        Пропускает заданное количество минут в симуляции.

        :param minutes: Количество минут для пропуска.
        :type minutes: int
        """
        #  Пропускает заданное количество минут
        self.skip(steps=minutes, timedelta_per_step=timedelta(minutes=1))
    
    def run_hours(self, hours: int):
        """
        Запускает симуляцию на заданное количество часов.

        :param hours: Количество часов для запуска симуляции.
        :type hours: int
        """
        #  Запускает симуляцию на заданное количество часов
        self.run(steps=hours, timedelta_per_step=timedelta(hours=1))
    
    def skip_hours(self, hours: int):
        """
        Пропускает заданное количество часов в симуляции.

        :param hours: Количество часов для пропуска.
        :type hours: int
        """
        #  Пропускает заданное количество часов
        self.skip(steps=hours, timedelta_per_step=timedelta(hours=1))
    
    def run_days(self, days: int):
        """
        Запускает симуляцию на заданное количество дней.

        :param days: Количество дней для запуска симуляции.
        :type days: int
        """
        #  Запускает симуляцию на заданное количество дней
        self.run(steps=days, timedelta_per_step=timedelta(days=1))
    
    def skip_days(self, days: int):
        """
        Пропускает заданное количество дней в симуляции.

        :param days: Количество дней для пропуска.
        :type days: int
        """
        #  Пропускает заданное количество дней
        self.skip(steps=days, timedelta_per_step=timedelta(days=1))
    
    def run_weeks(self, weeks: int):
        """
        Запускает симуляцию на заданное количество недель.

        :param weeks: Количество недель для запуска симуляции.
        :type weeks: int
        """
        #  Запускает симуляцию на заданное количество недель
        self.run(steps=weeks, timedelta_per_step=timedelta(weeks=1))
    
    def skip_weeks(self, weeks: int):
        """
        Пропускает заданное количество недель в симуляции.

        :param weeks: Количество недель для пропуска.
        :type weeks: int
        """
        #  Пропускает заданное количество недель
        self.skip(steps=weeks, timedelta_per_step=timedelta(weeks=1))
    
    def run_months(self, months: int):
        """
        Запускает симуляцию на заданное количество месяцев.

        :param months: Количество месяцев для запуска симуляции.
        :type months: int
        """
        #  Запускает симуляцию на заданное количество месяцев
        self.run(steps=months, timedelta_per_step=timedelta(weeks=4))
    
    def skip_months(self, months: int):
        """
        Пропускает заданное количество месяцев в симуляции.

        :param months: Количество месяцев для пропуска.
        :type months: int
        """
        #  Пропускает заданное количество месяцев
        self.skip(steps=months, timedelta_per_step=timedelta(weeks=4))
    
    def run_years(self, years: int):
        """
        Запускает симуляцию на заданное количество лет.

        :param years: Количество лет для запуска симуляции.
        :type years: int
        """
        #  Запускает симуляцию на заданное количество лет
        self.run(steps=years, timedelta_per_step=timedelta(days=365))
    
    def skip_years(self, years: int):
        """
        Пропускает заданное количество лет в симуляции.

        :param years: Количество лет для пропуска.
        :type years: int
        """
        #  Пропускает заданное количество лет
        self.skip(steps=years, timedelta_per_step=timedelta(days=365))

    #######################################################################
    # Методы управления агентами
    #######################################################################
    def add_agents(self, agents: list):
        """
        Добавляет список агентов в среду.

        :param agents: Список агентов для добавления.
        :type agents: list
        :return: Среда после добавления агентов.
        :rtype: TinyWorld
        """
        for agent in agents:
            self.add_agent(agent)
        
        return self # для цепочки вызовов

    def add_agent(self, agent: TinyPerson):
        """
        Добавляет агента в среду. Имя агента должно быть уникальным в пределах среды.

        :param agent: Агент для добавления.
        :type agent: TinyPerson
        :raises ValueError: Если имя агента не уникально в пределах среды.
        :return: Среда после добавления агента.
        :rtype: TinyWorld
        """

        #  Проверяет, что агента нет в среде
        if agent not in self.agents:
            logger.debug(f'Adding agent {agent.name} to the environment.')
            
            #  Проверяет, что имя агента уникально
            if agent.name not in self.name_to_agent:
                agent.environment = self
                self.agents.append(agent)
                self.name_to_agent[agent.name] = agent
            else:
                raise ValueError(f'Agent names must be unique, but \'{agent.name}\' is already in the environment.')
        else:
            logger.warn(f'Agent {agent.name} is already in the environment.')
        
        return self # для цепочки вызовов

    def remove_agent(self, agent: TinyPerson):
        """
        Удаляет агента из среды.

        :param agent: Агент для удаления.
        :type agent: TinyPerson
        :return: Среда после удаления агента.
        :rtype: TinyWorld
        """
        logger.debug(f'Removing agent {agent.name} from the environment.')
        #  Удаляет агента из списка и словаря
        self.agents.remove(agent)
        del self.name_to_agent[agent.name]

        return self # для цепочки вызовов
    
    def remove_all_agents(self):
        """
        Удаляет всех агентов из среды.

        :return: Среда после удаления всех агентов.
        :rtype: TinyWorld
        """
        logger.debug(f'Removing all agents from the environment.')
        #  Очищает список и словарь агентов
        self.agents = []
        self.name_to_agent = {}

        return self # для цепочки вызовов

    def get_agent_by_name(self, name: str) -> TinyPerson:
        """
        Возвращает агента с указанным именем. Возвращает None, если агента нет в среде.

        :param name: Имя агента для поиска.
        :type name: str
        :return: Агент с указанным именем или None.
        :rtype: TinyPerson
        """
        if name in self.name_to_agent:
            #  Возвращает агента по имени
            return self.name_to_agent[name]
        else:
            return None
        

    #######################################################################
    # Обработчики действий
    #
    # Действия, инициированные агентами, обрабатываются средой,
    # так как они имеют эффекты за пределами самого агента.
    #######################################################################
    @transactional
    def _handle_actions(self, source: TinyPerson, actions: list):
        """
        Обрабатывает действия, инициированные агентами.

        :param source: Агент, инициировавший действия.
        :type source: TinyPerson
        :param actions: Список действий, каждое из которых является JSON.
        :type actions: list
        """
        for action in actions:
            action_type = action['type'] # это обязательное поле
            content = action['content'] if 'content' in action else None
            target = action['target'] if 'target' in action else None

            logger.debug(f'[{self.name}] Handling action {action_type} from agent {name_or_empty(source)}. Content: {content}, target: {target}.')

            #  Некоторые действия требуют вмешательства среды
            if action_type == 'REACH_OUT':
                self._handle_reach_out(source, content, target)
            elif action_type == 'TALK':
                self._handle_talk(source, content, target)

    @transactional
    def _handle_reach_out(self, source_agent: TinyPerson, content: str, target: str):
        """
        Обрабатывает действие REACH_OUT. Разрешает действие по умолчанию.
        Подклассы могут переопределить этот метод.

        :param source_agent: Агент, инициировавший действие REACH_OUT.
        :type source_agent: TinyPerson
        :param content: Содержание сообщения.
        :type content: str
        :param target: Цель сообщения.
        :type target: str
        """

        #  По умолчанию REACH_OUT всегда успешен.
        target_agent = self.get_agent_by_name(target)
        
        source_agent.make_agent_accessible(target_agent)
        target_agent.make_agent_accessible(source_agent)

        source_agent.socialize(f'{name_or_empty(target_agent)} was successfully reached out, and is now available for interaction.', source=self)
        target_agent.socialize(f'{name_or_empty(source_agent)} reached out to you, and is now available for interaction.', source=self)

    @transactional
    def _handle_talk(self, source_agent: TinyPerson, content: str, target: str):
        """
        Обрабатывает действие TALK, доставляя сообщение указанной цели.

        :param source_agent: Агент, инициировавший действие TALK.
        :type source_agent: TinyPerson
        :param content: Содержание сообщения.
        :type content: str
        :param target: Цель сообщения.
        :type target: str, optional
        """
        target_agent = self.get_agent_by_name(target)

        logger.debug(f'[{self.name}] Delivering message from {name_or_empty(source_agent)} to {name_or_empty(target_agent)}.')

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
        Доставляет сообщение всем агентам в среде.

        :param speech: Содержание сообщения.
        :type speech: str
        :param source: Агент или среда, инициировавшая сообщение.
        :type source: AgentOrWorld, optional
        """
        logger.debug(f'[{self.name}] Broadcasting message: \'{speech}\'.')

        for agent in self.agents:
            #  Не отправляет сообщение источнику
            if agent != source:
                agent.listen(speech, source=source)
    
    @transactional
    def broadcast_thought(self, thought: str, source: AgentOrWorld=None):
        """
        Транслирует мысль всем агентам в среде.

        :param thought: Содержание мысли.
        :type thought: str
        """
        logger.debug(f'[{self.name}] Broadcasting thought: \'{thought}\'.')

        for agent in self.agents:
            agent.think(thought)
    
    @transactional
    def broadcast_internal_goal(self, internal_goal: str):
        """
        Транслирует внутреннюю цель всем агентам в среде.

        :param internal_goal: Содержание внутренней цели.
        :type internal_goal: str
        """
        logger.debug(f'[{self.name}] Broadcasting internal goal: \'{internal_goal}\'.')

        for agent in self.agents:
            agent.internalize_goal(internal_goal)
    
    @transactional
    def broadcast_context_change(self, context:list):
        """
        Транслирует изменение контекста всем агентам в среде.

        :param context: Содержание изменения контекста.
        :type context: list
        """
        logger.debug(f'[{self.name}] Broadcasting context change: \'{context}\'.')

        for agent in self.agents:
            agent.change_context(context)

    def make_everyone_accessible(self):
        """
        Делает всех агентов в среде доступными друг для друга.
        """
        for agent_1 in self.agents:
            for agent_2 in self.agents:
                if agent_1 != agent_2:
                    agent_1.make_agent_accessible(agent_2)
            

    ###########################################################
    # Методы форматирования
    ###########################################################

    def _render_step_info(self, cur_step, total_steps, kind, timedelta_per_step=None):
        """
        Отображает информацию о текущем шаге симуляции и сохраняет ее в буфер.

        :param cur_step: Текущий шаг.
        :type cur_step: int
        :param total_steps: Общее количество шагов.
        :type total_steps: int
        :param kind: Тип сообщения.
        :type kind: str
        :param timedelta_per_step: Временной интервал для одного шага симуляции.
        :type timedelta_per_step: timedelta, optional
        :raises ValueError: Если передан неизвестный тип сообщения.
        """
        if kind == 'step':
            rendering = self._pretty_step(cur_step=cur_step, total_steps=total_steps, timedelta_per_step=timedelta_per_step)
        else:
            raise ValueError(f'Unknown communication kind: {kind}')

        #  Добавляет сообщение в буфер и отображает
        self._add_to_buffer_and_render({'content': rendering, 'kind': kind})
    
    def _add_to_buffer_and_render(self, rendering):
        """
        Добавляет сообщение в буфер и отображает его.

        :param rendering: Сообщение для добавления в буфер и отображения.
        :type rendering: dict
        """
        #  Добавляет сообщение в буфер
        self._displayed_communications_buffer.append(rendering)
        #  Отображает сообщение
        self._render_output(rendering)

    def render_and_clear_buffer(self):
        """
        Отображает все накопленные сообщения и очищает буфер.

        :return: Список отображенных сообщений.
        :rtype: list
        """
        communications = self._displayed_communications_buffer
        self._displayed_communications_buffer = []

        for communication in communications:
            self._render_output(communication)

        return communications
    
    def _render_output(self, communication):
        """
        Отображает сообщение.

        :param communication: Сообщение для отображения.
        :type communication: dict or str
        """
        #  Распаковывает сообщение для получения информации
        if isinstance(communication, dict):
            content = communication['content']
            kind = communication['kind']
        else:
            content = communication
            kind = None
            
        #  Отображает сообщение в зависимости от типа
        if kind == 'step':
            self.console.rule(content)
        else:
            self.console.print(content)
    
    def clear_communications_buffer(self):
        """
        Очищает буфер сообщений.
        """
        self._displayed_communications_buffer = []

    def __repr__(self):
        return f'TinyWorld(name=\'{self.name}\')'

    def _pretty_step(self, cur_step, total_steps, timedelta_per_step=None):
        """
        Форматирует строку для отображения информации о шаге.

        :param cur_step: Текущий шаг.
        :type cur_step: int
        :param total_steps: Общее количество шагов.
        :type total_steps: int
        :param timedelta_per_step: Временной интервал для одного шага симуляции.
        :type timedelta_per_step: timedelta, optional
        :return: Отформатированная строка информации о шаге.
        :rtype: str
        """
        rendering = f'{self.name} step {cur_step} of {total_steps}'
        if timedelta_per_step is not None:
            rendering += f' ({pretty_datetime(self.current_datetime)})'

        return rendering

    def pp_current_interactions(self, simplified=True, skip_system=True):
        """
        Выводит в консоль отформатированные текущие сообщения от агентов.

        :param simplified: Флаг упрощенного вывода.
        :type simplified: bool
        :param skip_system: Флаг пропуска системных сообщений.
        :type skip_system: bool
        """
        print(self.pretty_current_interactions(simplified=simplified, skip_system=skip_system))

    def pretty_current_interactions(self, simplified=True, skip_system=True, max_content_length=default['max_content_display_length'], first_n=None, last_n=None, include_omission_info:bool=True):
      """
      Возвращает строку с форматированными текущими сообщениями от агентов.

      :param simplified: Флаг упрощенного вывода.
      :type simplified: bool
      :param skip_system: Флаг пропуска системных сообщений.
      :type skip_system: bool
      :param max_content_length: Максимальная длина отображаемого контента.
      :type max_content_length: int
      :param first_n: Количество первых сообщений для отображения.
      :type first_n: int, optional
      :param last_n: Количество последних сообщений для отображения.
      :type last_n: int, optional
      :param include_omission_info: Флаг включения информации о пропущенных сообщениях.
      :type include_omission_info: bool, optional
      :return: Отформатированная строка сообщений агентов.
      :rtype: str
      """
      agent_contents = []

      for agent in self.agents:
          agent_content = f'#### Interactions from the point of view of {agent.name} agent:\\n'
          agent_content += f'**BEGIN AGENT {agent.name} HISTORY.**\\n '
          agent_content += agent.pretty_current_interactions(simplified=simplified, skip_system=skip_system, max_content_length=max_content_length, first_n=first_n, last_n=last_n, include_omission_info=include_omission_info) + '\\n'
          agent_content += f'**FINISHED AGENT {agent.name} HISTORY.**\\n\\n'
          agent_contents.append(agent_content)
          
      return '\\n'.join(agent_contents)
    
    #######################################################################
    # Методы ввода/вывода
    #######################################################################

    def encode_complete_state(self) -> dict:
        """
        Кодирует полное состояние среды в словарь.

        :return: Словарь, содержащий состояние среды.
        :rtype: dict
        """
        to_copy = copy.copy(self.__dict__)

        #  Удаляет логгер и другие поля
        del to_copy['console']
        del to_copy['agents']
        del to_copy['name_to_agent']
        del to_copy['current_datetime']

        state = copy.deepcopy(to_copy)

        #  Агенты кодируются отдельно
        state['agents'] = [agent.encode_complete_state() for agent in self.agents]

        #  Время также кодируется отдельно
        state['current_datetime'] = self.current_datetime.isoformat()

        return state
    
    def decode_complete_state(self, state:dict) -> Self:
        """
        Декодирует полное состояние среды из словаря.

        :param state: Словарь, содержащий состояние среды.
        :type state: dict
        :return: Среда, восстановленная из словаря.
        :rtype: Self
        """
        state = copy.deepcopy(state)

        #################################
        #  Восстанавливает агентов на месте
        #################################
        self.remove_all_agents()
        for agent_state in state['agents']:
            try:
                try:
                    agent = TinyPerson.get_agent_by_name(agent_state['name'])
                except Exception as e:
                    raise ValueError(f'Could not find agent {agent_state[\'name\']} for environment {self.name}.') from e
                
                agent.decode_complete_state(agent_state)
                self.add_agent(agent)
                
            except Exception as e:
                raise ValueError(f'Could not decode agent {agent_state[\'name\']} for environment {self.name}.') from e
        
        #  Удаляет состояния агентов для обновления остальной части среды
        del state['agents']

        #  Восстанавливает время
        state['current_datetime'] = datetime.fromisoformat(state['current_datetime'])

        #  Восстанавливает остальные поля
        self.__dict__.update(state)

        return self

    @staticmethod
    def add_environment(environment):
        """
        Добавляет среду в список всех сред. Имена сред должны быть уникальными.

        :param environment: Среда для добавления.
        :type environment: TinyWorld
        :raises ValueError: Если среда с таким именем уже существует.
        """
        if environment.name in TinyWorld.all_environments:
            raise ValueError(f'Environment names must be unique, but \'{environment.name}\' is already defined.')
        else:
            TinyWorld.all_environments[environment.name] = environment
        

    @staticmethod
    def set_simulation_for_free_environments(simulation):
        """
        Устанавливает симуляцию, если она None. Позволяет свободным средам
        захватываться конкретными областями симуляции.

        :param simulation: Симуляция для установки.
        :type simulation: Simulation
        """
        for environment in TinyWorld