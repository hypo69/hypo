# Анализ кода модуля `environment.py`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован, с четким разделением на классы `TinyWorld` и `TinySocialNetwork`, что способствует модульности и повторному использованию.
    - Используются логирование для отслеживания действий и ошибок, что упрощает отладку и мониторинг.
    - Присутствуют docstring для классов, методов и функций.
    - Реализовано управление временем в виде шагов, минут, часов, дней, недель, месяцев и лет, что делает симуляции гибкими.
    - Код поддерживает сохранение и восстановление состояния среды.
    - Есть удобные методы для добавления, удаления и получения агентов.
-  Минусы
    -  Отсутствуют некоторые импорты, например,  `from src.logger.logger import logger`.
    -  В docstring местами отсутствует использование reStructuredText.
    -  Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -  Используется `try-except` с `...` вместо `logger.error`.
    -  Не все комментарии в коде переписаны в формате reStructuredText.

**Рекомендации по улучшению**
1. **Импорты**: Добавить отсутствующие импорты, такие как `from src.logger.logger import logger`, `from src.utils.jjson import j_loads`.
2. **Формат документации**: Привести все docstring к формату reStructuredText (RST), включая описания параметров и возвращаемых значений.
3. **Обработка данных**: Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.load` (если это требуется, так как в коде нет `json.load`).
4. **Логирование ошибок**: Заменить блоки `try-except` с `...` на использование `logger.error` для обработки ошибок.
5. **Комментарии**: Переписать все комментарии к функциям, методам и переменным в формате reStructuredText (RST), соблюдая стандарты оформления docstring в Python.

**Оптимизированный код**
```python
"""
Модуль предоставляет классы для создания и управления виртуальными средами.
=========================================================================================

Этот модуль содержит классы :class:`TinyWorld` и :class:`TinySocialNetwork`, которые используются для
создания симуляционных сред, в которых агенты могут взаимодействовать друг с другом и с внешними сущностями.

Пример использования
--------------------

Пример создания и запуска виртуального мира:

.. code-block:: python

    from datetime import timedelta

    world = TinyWorld(name="MyWorld")
    world.run(steps=10, timedelta_per_step=timedelta(minutes=5))
"""

import copy
from datetime import datetime, timedelta
from typing import Any, TypeVar, Union

from rich.console import Console

# Добавлен импорт logger из src.logger.logger
from src.logger.logger import logger
from tinytroupe.agent import TinyPerson
from tinytroupe.utils import name_or_empty, pretty_datetime
import tinytroupe.control as control
from tinytroupe.control import transactional

AgentOrWorld = Union["TinyPerson", "TinyWorld"]


class TinyWorld:
    """
    Базовый класс для создания виртуальных сред.

    :ivar all_environments: Словарь, содержащий все созданные среды, где ключ - это имя среды, а значение - объект среды.
    :vartype all_environments: dict
    :ivar communication_display: Флаг, определяющий, нужно ли отображать коммуникации в консоли для всех сред.
    :vartype communication_display: bool
    """
    # A dict of all environments created so far.
    all_environments = {}  # name -> environment

    # Whether to display environments communications or not, for all environments.
    communication_display = True

    def __init__(self, name: str = "A TinyWorld", agents: list = [],
                 initial_datetime: datetime = datetime.now(),
                 broadcast_if_no_target: bool = True):
        """
        Инициализирует объект среды.

        :param name: Имя среды.
        :type name: str
        :param agents: Список агентов для добавления в среду.
        :type agents: list
        :param initial_datetime: Начальное время среды. По умолчанию - текущее время.
        :type initial_datetime: datetime
        :param broadcast_if_no_target: Если `True`, то действия рассылаются всем, если цель действия не найдена.
        :type broadcast_if_no_target: bool
        """
        self.name = name
        self.current_datetime = initial_datetime
        self.broadcast_if_no_target = broadcast_if_no_target
        self.simulation_id = None  # будет сброшен позже, если агент используется в рамках определенной симуляции

        self.agents = []
        self.name_to_agent = {}  # {agent_name: agent, agent_name_2: agent_2, ...}

        # буфер коммуникаций, которые были отображены, используется для
        # сохранения этих коммуникаций в другом формате позже (например, кэширование)
        self._displayed_communications_buffer = []

        self.console = Console()

        # добавить среду в список всех сред
        TinyWorld.add_environment(self)

        self.add_agents(agents)

    #######################################################################
    # Simulation control methods
    #######################################################################
    @transactional
    def _step(self, timedelta_per_step=None):
        """
        Выполняет один шаг в среде. Эта реализация по умолчанию просто заставляет
        всех агентов в среде действовать и обрабатывает результирующие действия.
        Подклассы могут переопределить этот метод для реализации других политик.

        :param timedelta_per_step: Временной интервал для продвижения времени на каждом шаге.
        :type timedelta_per_step: timedelta, optional
        :return: Действия агентов на этом шаге.
        :rtype: dict
        """
        # увеличиваем текущее время, если указан timedelta. Это должно произойти перед
        # любыми другими обновлениями симуляции, чтобы убедиться, что агенты действуют
        # в правильное время, особенно если выполняется только один шаг.
        self._advance_datetime(timedelta_per_step)

        # агенты могут действовать
        agents_actions = {}
        for agent in self.agents:
            logger.debug(f"[{self.name}] Agent {name_or_empty(agent)} is acting.")
            actions = agent.act(return_actions=True)
            agents_actions[agent.name] = actions

            self._handle_actions(agent, agent.pop_latest_actions())

        return agents_actions

    def _advance_datetime(self, timedelta):
        """
        Продвигает текущее время среды на указанный интервал времени.

        :param timedelta: Временной интервал, на который нужно продвинуть время.
        :type timedelta: timedelta
        """
        if timedelta is not None:
            self.current_datetime += timedelta
        else:
            logger.info(f"[{self.name}] No timedelta provided, so the datetime was not advanced.")

    @transactional
    def run(self, steps: int, timedelta_per_step=None, return_actions=False):
        """
        Запускает симуляцию среды на заданное количество шагов.

        :param steps: Количество шагов для запуска среды.
        :type steps: int
        :param timedelta_per_step: Временной интервал между шагами. По умолчанию `None`.
        :type timedelta_per_step: timedelta, optional
        :param return_actions: Если `True`, то возвращает действия агентов. По умолчанию `False`.
        :type return_actions: bool, optional
        :return: Список действий агентов за время симуляции, если `return_actions` `True`.
        :rtype: list, optional
        """
        agents_actions_over_time = []
        for i in range(steps):
            logger.info(f"[{self.name}] Running world simulation step {i + 1} of {steps}.")

            if TinyWorld.communication_display:
                self._display_communication(cur_step=i + 1, total_steps=steps, kind='step',
                                            timedelta_per_step=timedelta_per_step)

            agents_actions = self._step(timedelta_per_step=timedelta_per_step)
            agents_actions_over_time.append(agents_actions)

        if return_actions:
            return agents_actions_over_time

    @transactional
    def skip(self, steps: int, timedelta_per_step=None):
        """
        Пропускает заданное количество шагов в среде. То есть время проходит, но никакие
        действия не выполняются агентами или другими сущностями в среде.

        :param steps: Количество шагов для пропуска.
        :type steps: int
        :param timedelta_per_step: Временной интервал между шагами. По умолчанию `None`.
        :type timedelta_per_step: timedelta, optional
        """
        self._advance_datetime(steps * timedelta_per_step)

    def run_minutes(self, minutes: int):
        """
        Запускает среду на заданное количество минут.

        :param minutes: Количество минут для запуска.
        :type minutes: int
        """
        self.run(steps=minutes, timedelta_per_step=timedelta(minutes=1))

    def skip_minutes(self, minutes: int):
        """
        Пропускает заданное количество минут в среде.

        :param minutes: Количество минут для пропуска.
        :type minutes: int
        """
        self.skip(steps=minutes, timedelta_per_step=timedelta(minutes=1))

    def run_hours(self, hours: int):
        """
        Запускает среду на заданное количество часов.

        :param hours: Количество часов для запуска.
        :type hours: int
        """
        self.run(steps=hours, timedelta_per_step=timedelta(hours=1))

    def skip_hours(self, hours: int):
        """
        Пропускает заданное количество часов в среде.

        :param hours: Количество часов для пропуска.
        :type hours: int
        """
        self.skip(steps=hours, timedelta_per_step=timedelta(hours=1))

    def run_days(self, days: int):
        """
        Запускает среду на заданное количество дней.

        :param days: Количество дней для запуска.
        :type days: int
        """
        self.run(steps=days, timedelta_per_step=timedelta(days=1))

    def skip_days(self, days: int):
        """
        Пропускает заданное количество дней в среде.

        :param days: Количество дней для пропуска.
        :type days: int
        """
        self.skip(steps=days, timedelta_per_step=timedelta(days=1))

    def run_weeks(self, weeks: int):
        """
        Запускает среду на заданное количество недель.

        :param weeks: Количество недель для запуска.
        :type weeks: int
        """
        self.run(steps=weeks, timedelta_per_step=timedelta(weeks=1))

    def skip_weeks(self, weeks: int):
        """
        Пропускает заданное количество недель в среде.

        :param weeks: Количество недель для пропуска.
        :type weeks: int
        """
        self.skip(steps=weeks, timedelta_per_step=timedelta(weeks=1))

    def run_months(self, months: int):
        """
        Запускает среду на заданное количество месяцев.

        :param months: Количество месяцев для запуска.
        :type months: int
        """
        self.run(steps=months, timedelta_per_step=timedelta(weeks=4))

    def skip_months(self, months: int):
        """
        Пропускает заданное количество месяцев в среде.

        :param months: Количество месяцев для пропуска.
        :type months: int
        """
        self.skip(steps=months, timedelta_per_step=timedelta(weeks=4))

    def run_years(self, years: int):
        """
        Запускает среду на заданное количество лет.

        :param years: Количество лет для запуска.
        :type years: int
        """
        self.run(steps=years, timedelta_per_step=timedelta(days=365))

    def skip_years(self, years: int):
        """
        Пропускает заданное количество лет в среде.

        :param years: Количество лет для пропуска.
        :type years: int
        """
        self.skip(steps=years, timedelta_per_step=timedelta(days=365))

    #######################################################################
    # Agent management methods
    #######################################################################
    def add_agents(self, agents: list):
        """
        Добавляет список агентов в среду.

        :param agents: Список агентов для добавления.
        :type agents: list
        :return: Ссылка на текущий объект для цепочки вызовов.
        :rtype: TinyWorld
        """
        for agent in agents:
            self.add_agent(agent)

        return self  # for chaining

    def add_agent(self, agent: TinyPerson):
        """
        Добавляет агента в среду. Имя агента должно быть уникальным в пределах среды.

        :param agent: Агент для добавления.
        :type agent: TinyPerson
        :raises ValueError: Если имя агента не уникально в пределах среды.
        :return: Ссылка на текущий объект для цепочки вызовов.
        :rtype: TinyWorld
        """
        # проверяем, что агента еще нет в среде
        if agent not in self.agents:
            logger.debug(f"Adding agent {agent.name} to the environment.")

            # Имена агентов должны быть уникальными в среде.
            # Проверяем, что имени агента еще нет в словаре.
            if agent.name not in self.name_to_agent:
                agent.environment = self
                self.agents.append(agent)
                self.name_to_agent[agent.name] = agent
            else:
                raise ValueError(f"Agent names must be unique, but '{agent.name}' is already in the environment.")
        else:
            logger.warn(f"Agent {agent.name} is already in the environment.")

        return self  # for chaining

    def remove_agent(self, agent: TinyPerson):
        """
        Удаляет агента из среды.

        :param agent: Агент для удаления.
        :type agent: TinyPerson
        :return: Ссылка на текущий объект для цепочки вызовов.
        :rtype: TinyWorld
        """
        logger.debug(f"Removing agent {agent.name} from the environment.")
        self.agents.remove(agent)
        del self.name_to_agent[agent.name]

        return self  # for chaining

    def remove_all_agents(self):
        """
        Удаляет всех агентов из среды.
        :return: Ссылка на текущий объект для цепочки вызовов.
        :rtype: TinyWorld
        """
        logger.debug(f"Removing all agents from the environment.")
        self.agents = []
        self.name_to_agent = {}

        return self  # for chaining

    def get_agent_by_name(self, name: str) -> TinyPerson:
        """
        Возвращает агента с указанным именем. Если агента с таким именем нет в среде,
        возвращает `None`.

        :param name: Имя агента, которого нужно вернуть.
        :type name: str
        :return: Агент с указанным именем или `None`, если такого агента нет.
        :rtype: TinyPerson, optional
        """
        if name in self.name_to_agent:
            return self.name_to_agent[name]
        else:
            return None

    #######################################################################
    # Action handlers
    #
    # Specific actions issued by agents are handled by the environment,
    # because they have effects beyond the agent itself.
    #######################################################################
    @transactional
    def _handle_actions(self, source: TinyPerson, actions: list):
        """
        Обрабатывает действия, выданные агентами.

        :param source: Агент, выдавший действия.
        :type source: TinyPerson
        :param actions: Список действий, выданных агентами. Каждое действие является JSON-спецификацией.
        :type actions: list
        """
        for action in actions:
            action_type = action["type"]  # это единственное обязательное поле
            content = action["content"] if "content" in action else None
            target = action["target"] if "target" in action else None

            logger.debug(
                f"[{self.name}] Handling action {action_type} from agent {name_or_empty(source)}. Content: {content}, target: {target}.")

            # только некоторые действия требуют вмешательства среды
            if action_type == "REACH_OUT":
                self._handle_reach_out(source, content, target)
            elif action_type == "TALK":
                self._handle_talk(source, content, target)

    @transactional
    def _handle_reach_out(self, source_agent: TinyPerson, content: str, target: str):
        """
        Обрабатывает действие `REACH_OUT`. Эта реализация по умолчанию всегда позволяет
        `REACH_OUT` выполняться успешно. Подклассы могут переопределить этот метод для реализации
        других политик.

        :param source_agent: Агент, выдавший действие `REACH_OUT`.
        :type source_agent: TinyPerson
        :param content: Содержание сообщения.
        :type content: str
        :param target: Цель сообщения.
        :type target: str
        """

        # Эта реализация по умолчанию всегда позволяет REACH_OUT выполняться успешно.
        target_agent = self.get_agent_by_name(target)

        source_agent.make_agent_accessible(target_agent)
        target_agent.make_agent_accessible(source_agent)

        source_agent.socialize(f"{name_or_empty(target_agent)} was successfully reached out, and is now available for interaction.", source=self)
        target_agent.socialize(f"{name_or_empty(source_agent)} reached out to you, and is now available for interaction.", source=self)

    @transactional
    def _handle_talk(self, source_agent: TinyPerson, content: str, target: str):
        """
        Обрабатывает действие `TALK`, доставляя указанное сообщение указанной цели.

        :param source_agent: Агент, выдавший действие `TALK`.
        :type source_agent: TinyPerson
        :param content: Содержание сообщения.
        :type content: str
        :param target: Цель сообщения.
        :type target: str, optional
        """
        target_agent = self.get_agent_by_name(target)

        logger.debug(f"[{self.name}] Delivering message from {name_or_empty(source_agent)} to {name_or_empty(target_agent)}.")

        if target_agent is not None:
            target_agent.listen(content, source=source_agent)
        elif self.broadcast_if_no_target:
            self.broadcast(content, source=source_agent)

    #######################################################################
    # Interaction methods
    #######################################################################
    @transactional
    def broadcast(self, speech: str, source: AgentOrWorld=None):
        """
        Доставляет сообщение всем агентам в среде.

        :param speech: Содержание сообщения.
        :type speech: str
        :param source: Агент или среда, выдавшие сообщение. По умолчанию `None`.
        :type source: AgentOrWorld, optional
        """
        logger.debug(f"[{self.name}] Broadcasting message: '{speech}'.")

        for agent in self.agents:
            # не доставляем сообщение источнику
            if agent != source:
                agent.listen(speech, source=source)

    @transactional
    def broadcast_thought(self, thought: str, source: AgentOrWorld=None):
        """
        Рассылает мысль всем агентам в среде.

        :param thought: Содержание мысли.
        :type thought: str
        """
        logger.debug(f"[{self.name}] Broadcasting thought: '{thought}'.")

        for agent in self.agents:
            agent.think(thought)

    @transactional
    def broadcast_internal_goal(self, internal_goal: str):
        """
        Рассылает внутреннюю цель всем агентам в среде.

        :param internal_goal: Содержание внутренней цели.
        :type internal_goal: str
        """
        logger.debug(f"[{self.name}] Broadcasting internal goal: '{internal_goal}'.")

        for agent in self.agents:
            agent.internalize_goal(internal_goal)

    @transactional
    def broadcast_context_change(self, context: list):
        """
        Рассылает изменение контекста всем агентам в среде.

        :param context: Содержание изменения контекста.
        :type context: list
        """
        logger.debug(f"[{self.name}] Broadcasting context change: '{context}'.")

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
    # Formatting conveniences
    ###########################################################

    # TODO better names for these "display" methods
    def _display_communication(self, cur_step, total_steps, kind, timedelta_per_step=None):
        """
        Отображает текущее сообщение и сохраняет его в буфере для дальнейшего использования.
        
        :param cur_step: Текущий шаг симуляции.
        :type cur_step: int
        :param total_steps: Общее количество шагов в симуляции.
        :type total_steps: int
        :param kind: Тип сообщения (например, 'step').
        :type kind: str
        :param timedelta_per_step: Временной интервал между шагами.
        :type timedelta_per_step: timedelta, optional
        """
        if kind == 'step':
            rendering = self._pretty_step(cur_step=cur_step, total_steps=total_steps,
                                         timedelta_per_step=timedelta_per_step)
        else:
            raise ValueError(f"Unknown communication kind: {kind}")

        self._push_and_display_latest_communication({"content": rendering, "kind": kind})

    def _push_and_display_latest_communication(self, rendering):
        """
        Помещает последние сообщения в буфер агента.
        
        :param rendering: Сообщение для добавления в буфер.
        :type rendering: dict
        """
        self._displayed_communications_buffer.append(rendering)
        self._display(rendering)

    def pop_and_display_latest_communications(self):
        """
        Извлекает последние сообщения и отображает их.
        
        :return: Список извлеченных сообщений.
        :rtype: list
        """
        communications = self._displayed_communications_buffer
        self._displayed_communications_buffer = []

        for communication in communications:
            self._display(communication)

        return communications

    def _display(self, communication):
        """
        Отображает сообщения в консоли.
        
        :param communication: Сообщение для отображения.
        :type communication: dict or str
        """
        # распаковываем сообщение для получения дополнительной информации
        if isinstance(communication, dict):
            content = communication["content"]
            kind = communication["kind"]
        else:
            content = communication
            kind = None

        # отображаем в соответствии с типом сообщения
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
        """
        Возвращает строковое представление объекта.

        :return: Строковое представление объекта.
        :rtype: str
        """
        return f"TinyWorld(name='{self.name}')"

    def _pretty_step(self, cur_step, total_steps, timedelta_per_step=None):
        """
        Форматирует вывод текущего шага.
        
        :param cur_step: Текущий шаг симуляции.
        :type cur_step: int
        :param total_steps: Общее количество шагов в симуляции.
        :type total_steps: int
        :param timedelta_per_step: Временной интервал между шагами.
        :type timedelta_per_step: timedelta, optional
        :return: Отформатированная строка с информацией о текущем шаге.
        :rtype: str
        """
        rendering = f"{self.name} step {cur_step} of {total_steps}"
        if timedelta_per_step is not None:
            rendering += f" ({pretty_datetime(self.current_datetime)})"

        return rendering

    def pp_current_interactions(self, simplified=True, skip_system=True):
        """
        Выводит в консоль текущие сообщения от агентов в этой среде.
        
        :param simplified: Упрощенный вывод.
        :type simplified: bool, optional
        :param skip_system: Пропуск системных сообщений.
        :type skip_system: bool, optional
        """
        print(self.pretty_current_interactions(simplified=simplified, skip_system=skip_system))

    def pretty_current_interactions(self, simplified=True, skip_system=True, max_content_length=default["max_content_display_length"], first_n=None, last_n=None, include_omission_info:bool=True):
        """
        Возвращает отформатированную строку с текущими сообщениями агентов в этой среде.
        
        :param simplified: Упрощенный вывод.
        :type simplified: bool, optional
        :param skip_system: Пропуск системных сообщений.
        :type skip_system: bool, optional
        :param max_content_length: Максимальная длина содержимого сообщения.
        :type max_content_length: int, optional
        :param first_n: Первые N сообщений.
        :type first_n: int, optional
        :param last_n: Последние N сообщений.
        :type last_n: int, optional
        :param include_omission_info: Включать информацию о пропущенных сообщениях.
        :type include_omission_info: bool, optional
        :return: Строка с отформатированными сообщениями агентов.
        :rtype: str
        """
        agent_contents = []

        for agent in self.agents:
            agent_content = f"#### Interactions from the point of view of {agent.name} agent:\\n"
            agent_content += f"**BEGIN AGENT {agent.name} HISTORY.**\\n "
            agent_content += agent.pretty_current_interactions(simplified=simplified, skip_system=skip_system, max_content_length=max_content_length, first_n=first_n, last_n=last_n, include_omission_info=include_omission_info) + "\\n"
            agent_content += f"**FINISHED AGENT {agent.name} HISTORY.**\\n\\n"
            agent_contents.append(agent_content)

        return "\\n".join(agent_contents)

    #######################################################################
    # IO
    #######################################################################

    def encode_complete_state(self) -> dict:
        """
        Кодирует полное состояние среды в словарь.

        :return: Словарь, кодирующий полное состояние среды.
        :rtype: dict
        """
        to_copy = copy.copy(self.__dict__)

        # remove the logger and other fields
        del to_copy['console']
        del to_copy['agents']
        del to_copy['name_to_agent']
        del to_copy['current_datetime']

        state = copy.deepcopy(to_copy)

        # агенты кодируются отдельно
        state["agents"] = [agent.encode_complete_state() for agent in self.agents]

        # datetime также должен быть закодирован отдельно
        state["current_datetime"] = self.current_datetime.isoformat()

        return state

    def decode_complete_state(self, state: dict):
        """
        Декодирует полное состояние среды из словаря.

        :param state: Словарь, кодирующий полное состояние среды.
        :type state: dict
        :return: Объект среды, декодированный из словаря.
        :rtype: Self
        """
        state = copy.deepcopy(state)

        #################################
        # восстанавливаем агентов на месте
        #################################
        self.remove_all_agents()
        for agent_state in state["agents"]:
            try:
                try:
                    agent = TinyPerson.get_agent_by_name(agent_state["name"])
                except Exception as e:
                   logger.error(f"Could not find agent {agent_state['name']} for environment {self.name}.", exc_info=True)
                   raise ValueError(f"Could not find agent {agent_state['name']} for environment {self.name}.") from e
                    
                agent.decode_complete_state(agent_state)
                self.add_agent(agent)

            except Exception as e:
                logger.error(f"Could not decode agent {agent_state['name']} for environment {self.name}.", exc_info=True)
                raise ValueError(f"Could not decode agent {agent_state['name']} for environment {self.name}.") from e

        # удаляем состояния агентов, чтобы обновить остальную часть среды
        del state["agents"]

        # восстанавливаем datetime
        state["current_datetime"] = datetime.fromisoformat(state["current_datetime"])

        # восстанавливаем другие поля
        self.__dict__.update(state)

        return self

    @staticmethod
    def add_environment(environment):
        """
        Добавляет среду в список всех сред. Имена сред должны быть уникальными,
        поэтому, если среда с таким же именем уже существует, вызывается ошибка.

        :param environment: Среда для добавления.
        :type environment: TinyWorld
        :raises ValueError: Если имя среды не уникально.
        """
        if environment.name in TinyWorld.all_environments:
            raise ValueError(f"Environment names must be unique, but '{environment.name}' is already defined.")
        else:
            TinyWorld.all_environments[environment.name] = environment

    @staticmethod
    def set_simulation_for_free_environments(simulation):
        """
        Устанавливает симуляцию, если она `None`. Это позволяет свободным средам быть захваченными
        конкретными областями симуляции, если это необходимо.

        :param simulation: Симуляция для установки.
        :type simulation: Simulation
        """
        for environment in TinyWorld.all_environments.values():
            if environment.simulation_id is None:
                simulation.add_environment(environment)

    @staticmethod
    def get_environment_by_name(name: str):
        """
        Возвращает среду с указанным именем. Если среды с таким именем нет,
        возвращает `None`.

        :param name: Имя среды, которую нужно вернуть.
        :type name: str
        :return: Среда с указанным именем или `None`, если такой среды нет.
        :rtype: TinyWorld, optional
        """
        if name in TinyWorld.all_environments:
            return TinyWorld.all_environments[name]
        else:
            return None

    @staticmethod
    def clear_environments():
        """
        Очищает список всех сред.
        """
        TinyWorld.all_environments = {}


class TinySocialNetwork(TinyWorld):
    """
    Класс для создания социальной сети как типа виртуальной среды.
    """
    def __init__(self, name, broadcast_if_no_target=True):
        """
        Создает новую среду `TinySocialNetwork`.

        :param name: Имя среды.
        :type name: str
        :param broadcast_if_no_target: Если `True`, то действия рассылаются через доступные связи агента, если цель не найдена.
        :type broadcast_if_no_target: bool, optional
        """

        super().__init__(name, broadcast_if_no_target=broadcast_if_no_target)

        self.relations = {}

    @transactional
    def add_relation(self, agent_1, agent_2, name="default"):
        """
        Добавляет связь между двумя агентами.
        
        :param agent_1: Первый агент.
        :type agent_1: TinyPerson
        :param agent_2: Второй агент.
        :type agent_2: TinyPerson
        :param name: Имя связи.
        :type name: str, optional
        :return: Ссылка на текущий объект для цепочки вызовов.
        :rtype: TinySocialNetwork
        """

        logger.debug(f"Adding relation {name} between {agent_1.name} and {agent_2.name}.")

        # агенты должны быть уже в среде, если нет, то сначала добавляем их
        if agent_1 not in self.agents:
            self.agents.append(agent_1)
        if agent_2 not in self.agents:
            self.agents.append(agent_2)

        if name in self.relations:
            self.relations[name].append((agent_1, agent_2))
        else:
            self.relations[name] = [(agent_1, agent_2)]

        return self  # for chaining

    @transactional
    def _update