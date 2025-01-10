## Анализ кода модуля `environment.py`

**Качество кода: 8/10**

-   **Плюсы:**
    *   Хорошая структура классов и методов, код разбит на логические блоки.
    *   Использование `logger` для отладки и логирования.
    *   Наличие базового класса `TinyWorld` и его расширения `TinySocialNetwork` демонстрирует принципы ООП.
    *   Присутствует документация в формате docstring для большинства методов.
    *   Реализованы основные методы для управления агентами и симуляцией.
    *   Имеется возможность сохранения и восстановления состояния среды.
    *   Использование `transactional` декоратора для обеспечения консистентности данных.

-   **Минусы:**
    *   Некоторые docstring не соответствуют стандартам (отсутствуют Args, Returns, Example).
    *   Использование `datetime.datetime.now()` без указания `tzinfo` может привести к проблемам при работе с разными часовыми поясами.
    *   Не все методы имеют полные docstring.
    *   В некоторых местах используется `logger.info`, хотя по смыслу лучше подходит `logger.debug`.
    *   Следует проверить именование переменных и методов на консистентность, в том числе сокращения `pp`.
    *   Не хватает примеров использования для некоторых методов.

**Рекомендации по улучшению:**

1.  **Документация:**
    *   Дополнить docstring для всех методов и классов, включая описание аргументов, возвращаемых значений и примеров использования.
    *   Привести docstring к единому стандарту RST.
    *   Добавить описание модуля в начале файла.
2.  **Обработка времени:**
    *   В `__init__` вместо `datetime.datetime.now()` использовать `datetime.datetime.now(datetime.timezone.utc)` для корректной работы с часовыми поясами.
3.  **Логирование:**
    *   Использовать `logger.debug` вместо `logger.info` для информационных сообщений о ходе выполнения, `logger.info` оставить для сообщений о важных событиях.
4.  **Именование:**
    *   Привести в соответствие имена переменных и методов с ранее обработанными файлами.
5.  **Улучшения кода:**
    *   Избегать избыточного использования `try-except`, использовать `logger.error` для обработки ошибок.
    *   Добавить проверки на корректность типов входных данных.
    *   Уточнить комментарии, где это необходимо.

**Оптимизированный код**

```python
"""
Модуль для определения окружения, в котором взаимодействуют агенты.
=========================================================================================

Этот модуль содержит классы:

*   :class:`TinyWorld` - базовый класс для окружений.
*   :class:`TinySocialNetwork` - класс для моделирования социальной сети.

Оба класса предоставляют методы для управления агентами, моделирования времени и
взаимодействия между агентами.

Пример использования
--------------------

Пример создания и запуска симуляции:

.. code-block:: python

    from datetime import timedelta
    from tinytroupe.environment import TinyWorld, TinyPerson

    world = TinyWorld(name='MyWorld')
    agent1 = TinyPerson(name='Alice')
    agent2 = TinyPerson(name='Bob')
    world.add_agents([agent1, agent2])
    world.run(steps=10, timedelta_per_step=timedelta(minutes=1))

"""
import copy
from datetime import datetime, timedelta
from typing import Any, TypeVar, Union

from rich.console import Console

from src.logger.logger import logger
from tinytroupe.agent import TinyPerson
from tinytroupe.utils import name_or_empty, pretty_datetime
import tinytroupe.control as control
from tinytroupe.control import transactional


AgentOrWorld = Union["TinyPerson", "TinyWorld"]


class TinyWorld:
    """
    Базовый класс для окружений.

    :ivar all_environments: Словарь всех созданных окружений.
    :vartype all_environments: dict
    :ivar communication_display: Флаг отображения коммуникаций.
    :vartype communication_display: bool
    """

    # Словарь всех созданных окружений.
    all_environments = {}  # name -> environment

    # Флаг для отображения коммуникаций в консоли.
    communication_display = True

    def __init__(self, name: str = 'A TinyWorld', agents: list = [],
                 initial_datetime: datetime = datetime.now(datetime.timezone.utc),
                 broadcast_if_no_target: bool = True):
        """
        Инициализирует окружение.

        :param name: Имя окружения.
        :type name: str
        :param agents: Список агентов для добавления в окружение.
        :type agents: list
        :param initial_datetime: Начальное время окружения.
        :type initial_datetime: datetime
        :param broadcast_if_no_target: Флаг широковещания действий, если цель не найдена.
        :type broadcast_if_no_target: bool
        """
        self.name = name
        self.current_datetime = initial_datetime
        self.broadcast_if_no_target = broadcast_if_no_target
        self.simulation_id = None  # будет сброшен позже, если агент используется в рамках определенной симуляции

        self.agents = []
        self.name_to_agent = {}  # {agent_name: agent, agent_name_2: agent_2, ...}

        # буфер коммуникаций, который был отображен, используется для сохранения в другом формате
        self._displayed_communications_buffer = []

        self.console = Console()

        # добавление окружения в список всех окружений
        TinyWorld.add_environment(self)

        self.add_agents(agents)

    #######################################################################
    # Методы управления симуляцией
    #######################################################################
    @transactional
    def _step(self, timedelta_per_step: timedelta = None) -> dict:
        """
        Выполняет один шаг в окружении.

        Этот метод вызывает метод act() у каждого агента в окружении
        и обрабатывает полученные действия.

        :param timedelta_per_step: Временной интервал для шага.
        :type timedelta_per_step: timedelta, optional
        :return: Словарь действий агентов.
        :rtype: dict
        """
        # увеличение текущей даты, если задано timedelta.
        self._advance_datetime(timedelta_per_step)

        # агенты выполняют действия
        agents_actions = {}
        for agent in self.agents:
            logger.debug(f'[{self.name}] Агент {name_or_empty(agent)} выполняет действие.')
            actions = agent.act(return_actions=True)
            agents_actions[agent.name] = actions

            self._handle_actions(agent, agent.pop_latest_actions())

        return agents_actions

    def _advance_datetime(self, timedelta: timedelta) -> None:
        """
        Увеличивает текущую дату на указанный интервал.

        :param timedelta: Временной интервал для увеличения.
        :type timedelta: timedelta
        """
        if timedelta is not None:
            self.current_datetime += timedelta
        else:
            logger.info(f'[{self.name}] Временной интервал не указан, дата не изменена.')

    @transactional
    def run(self, steps: int, timedelta_per_step: timedelta = None, return_actions: bool = False) -> list | None:
        """
        Запускает симуляцию на заданное количество шагов.

        :param steps: Количество шагов для запуска симуляции.
        :type steps: int
        :param timedelta_per_step: Временной интервал между шагами.
        :type timedelta_per_step: timedelta, optional
        :param return_actions: Флаг возврата действий агентов.
        :type return_actions: bool, optional
        :return: Список действий агентов за все шаги, если return_actions = True.
        :rtype: list, optional
        """
        agents_actions_over_time = []
        for i in range(steps):
            logger.info(f'[{self.name}] Запуск шага {i + 1} из {steps}.')

            if TinyWorld.communication_display:
                self._display_communication(cur_step=i + 1, total_steps=steps, kind='step',
                                            timedelta_per_step=timedelta_per_step)

            agents_actions = self._step(timedelta_per_step=timedelta_per_step)
            agents_actions_over_time.append(agents_actions)

        if return_actions:
            return agents_actions_over_time
        return None

    @transactional
    def skip(self, steps: int, timedelta_per_step: timedelta = None) -> None:
        """
        Пропускает заданное количество шагов в окружении.

        Время проходит, но никаких действий не выполняется.

        :param steps: Количество шагов для пропуска.
        :type steps: int
        :param timedelta_per_step: Временной интервал между шагами.
        :type timedelta_per_step: timedelta, optional
        """
        self._advance_datetime(steps * timedelta_per_step)

    def run_minutes(self, minutes: int) -> None:
        """
        Запускает симуляцию на заданное количество минут.

        :param minutes: Количество минут для запуска симуляции.
        :type minutes: int
        """
        self.run(steps=minutes, timedelta_per_step=timedelta(minutes=1))

    def skip_minutes(self, minutes: int) -> None:
        """
        Пропускает заданное количество минут в окружении.

        :param minutes: Количество минут для пропуска.
        :type minutes: int
        """
        self.skip(steps=minutes, timedelta_per_step=timedelta(minutes=1))

    def run_hours(self, hours: int) -> None:
        """
        Запускает симуляцию на заданное количество часов.

        :param hours: Количество часов для запуска симуляции.
        :type hours: int
        """
        self.run(steps=hours, timedelta_per_step=timedelta(hours=1))

    def skip_hours(self, hours: int) -> None:
        """
        Пропускает заданное количество часов в окружении.

        :param hours: Количество часов для пропуска.
        :type hours: int
        """
        self.skip(steps=hours, timedelta_per_step=timedelta(hours=1))

    def run_days(self, days: int) -> None:
        """
        Запускает симуляцию на заданное количество дней.

        :param days: Количество дней для запуска симуляции.
        :type days: int
        """
        self.run(steps=days, timedelta_per_step=timedelta(days=1))

    def skip_days(self, days: int) -> None:
        """
        Пропускает заданное количество дней в окружении.

        :param days: Количество дней для пропуска.
        :type days: int
        """
        self.skip(steps=days, timedelta_per_step=timedelta(days=1))

    def run_weeks(self, weeks: int) -> None:
        """
        Запускает симуляцию на заданное количество недель.

        :param weeks: Количество недель для запуска симуляции.
        :type weeks: int
        """
        self.run(steps=weeks, timedelta_per_step=timedelta(weeks=1))

    def skip_weeks(self, weeks: int) -> None:
        """
        Пропускает заданное количество недель в окружении.

        :param weeks: Количество недель для пропуска.
        :type weeks: int
        """
        self.skip(steps=weeks, timedelta_per_step=timedelta(weeks=1))

    def run_months(self, months: int) -> None:
        """
        Запускает симуляцию на заданное количество месяцев.

        :param months: Количество месяцев для запуска симуляции.
        :type months: int
        """
        self.run(steps=months, timedelta_per_step=timedelta(weeks=4))

    def skip_months(self, months: int) -> None:
        """
        Пропускает заданное количество месяцев в окружении.

        :param months: Количество месяцев для пропуска.
        :type months: int
        """
        self.skip(steps=months, timedelta_per_step=timedelta(weeks=4))

    def run_years(self, years: int) -> None:
        """
        Запускает симуляцию на заданное количество лет.

        :param years: Количество лет для запуска симуляции.
        :type years: int
        """
        self.run(steps=years, timedelta_per_step=timedelta(days=365))

    def skip_years(self, years: int) -> None:
        """
        Пропускает заданное количество лет в окружении.

        :param years: Количество лет для пропуска.
        :type years: int
        """
        self.skip(steps=years, timedelta_per_step=timedelta(days=365))

    #######################################################################
    # Методы управления агентами
    #######################################################################
    def add_agents(self, agents: list) -> "TinyWorld":
        """
        Добавляет список агентов в окружение.

        :param agents: Список агентов для добавления.
        :type agents: list
        :return: self для возможности вызова цепочки.
        :rtype: TinyWorld
        """
        for agent in agents:
            self.add_agent(agent)

        return self  # для цепочки

    def add_agent(self, agent: TinyPerson) -> "TinyWorld":
        """
        Добавляет агента в окружение.

        Имя агента должно быть уникальным в пределах окружения.

        :param agent: Агент для добавления.
        :type agent: TinyPerson
        :raises ValueError: Если имя агента не уникально.
        :return: self для возможности вызова цепочки.
        :rtype: TinyWorld
        """

        # проверка, что агент еще не в окружении
        if agent not in self.agents:
            logger.debug(f'Добавление агента {agent.name} в окружение.')

            # Имена агентов должны быть уникальными в окружении.
            # проверка, есть ли уже агент с таким именем.
            if agent.name not in self.name_to_agent:
                agent.environment = self
                self.agents.append(agent)
                self.name_to_agent[agent.name] = agent
            else:
                raise ValueError(f'Имена агентов должны быть уникальными, но \'{agent.name}\' уже есть в окружении.')
        else:
            logger.warning(f'Агент {agent.name} уже в окружении.')

        return self  # для цепочки

    def remove_agent(self, agent: TinyPerson) -> "TinyWorld":
        """
        Удаляет агента из окружения.

        :param agent: Агент для удаления.
        :type agent: TinyPerson
        :return: self для возможности вызова цепочки.
        :rtype: TinyWorld
        """
        logger.debug(f'Удаление агента {agent.name} из окружения.')
        self.agents.remove(agent)
        del self.name_to_agent[agent.name]

        return self  # для цепочки

    def remove_all_agents(self) -> "TinyWorld":
        """
        Удаляет всех агентов из окружения.
        :return: self для возможности вызова цепочки.
        :rtype: TinyWorld
        """
        logger.debug(f'Удаление всех агентов из окружения.')
        self.agents = []
        self.name_to_agent = {}

        return self  # для цепочки

    def get_agent_by_name(self, name: str) -> TinyPerson | None:
        """
        Возвращает агента по имени.

        :param name: Имя агента.
        :type name: str
        :return: Агент с указанным именем или None, если такого агента нет.
        :rtype: TinyPerson, optional
        """
        if name in self.name_to_agent:
            return self.name_to_agent[name]
        else:
            return None

    #######################################################################
    # Обработчики действий
    #
    # Действия агентов обрабатываются окружением,
    # так как они имеют эффект за пределами агента.
    #######################################################################
    @transactional
    def _handle_actions(self, source: TinyPerson, actions: list) -> None:
        """
        Обрабатывает действия, выполненные агентами.

        :param source: Агент, выполнивший действие.
        :type source: TinyPerson
        :param actions: Список действий, выполненных агентом.
        :type actions: list
        """
        for action in actions:
            action_type = action['type']  # это единственное обязательное поле
            content = action['content'] if 'content' in action else None
            target = action['target'] if 'target' in action else None

            logger.debug(
                f'[{self.name}] Обработка действия {action_type} от агента {name_or_empty(source)}. Содержание: {content}, цель: {target}.')

            # только некоторые действия требуют вмешательства окружения
            if action_type == 'REACH_OUT':
                self._handle_reach_out(source, content, target)
            elif action_type == 'TALK':
                self._handle_talk(source, content, target)

    @transactional
    def _handle_reach_out(self, source_agent: TinyPerson, content: str, target: str) -> None:
        """
        Обрабатывает действие REACH_OUT.

        :param source_agent: Агент, выполнивший действие.
        :type source_agent: TinyPerson
        :param content: Содержание сообщения.
        :type content: str
        :param target: Цель сообщения.
        :type target: str
        """

        # реализация по умолчанию всегда позволяет REACH_OUT выполниться.
        target_agent = self.get_agent_by_name(target)

        source_agent.make_agent_accessible(target_agent)
        target_agent.make_agent_accessible(source_agent)

        source_agent.socialize(f'{name_or_empty(target_agent)} был успешно достигнут, и теперь доступен для взаимодействия.',
                               source=self)
        target_agent.socialize(f'{name_or_empty(source_agent)} обратился к вам, и теперь доступен для взаимодействия.',
                               source=self)

    @transactional
    def _handle_talk(self, source_agent: TinyPerson, content: str, target: str) -> None:
        """
        Обрабатывает действие TALK.

        Доставляет сообщение указанному агенту.

        :param source_agent: Агент, выполнивший действие.
        :type source_agent: TinyPerson
        :param content: Содержание сообщения.
        :type content: str
        :param target: Цель сообщения.
        :type target: str
        """
        target_agent = self.get_agent_by_name(target)

        logger.debug(
            f'[{self.name}] Доставка сообщения от {name_or_empty(source_agent)} к {name_or_empty(target_agent)}.')

        if target_agent is not None:
            target_agent.listen(content, source=source_agent)
        elif self.broadcast_if_no_target:
            self.broadcast(content, source=source_agent)

    #######################################################################
    # Методы взаимодействия
    #######################################################################
    @transactional
    def broadcast(self, speech: str, source: AgentOrWorld = None) -> None:
        """
        Доставляет сообщение всем агентам в окружении.

        :param speech: Содержание сообщения.
        :type speech: str
        :param source: Источник сообщения.
        :type source: AgentOrWorld, optional
        """
        logger.debug(f'[{self.name}] Широковещательное сообщение: \'{speech}\'.')

        for agent in self.agents:
            # не доставлять сообщение источнику
            if agent != source:
                agent.listen(speech, source=source)

    @transactional
    def broadcast_thought(self, thought: str, source: AgentOrWorld = None) -> None:
        """
        Распространяет мысль среди всех агентов в окружении.

        :param thought: Содержание мысли.
        :type thought: str
        """
        logger.debug(f'[{self.name}] Широковещательная мысль: \'{thought}\'.')

        for agent in self.agents:
            agent.think(thought)

    @transactional
    def broadcast_internal_goal(self, internal_goal: str) -> None:
        """
        Распространяет внутреннюю цель среди всех агентов в окружении.

        :param internal_goal: Содержание внутренней цели.
        :type internal_goal: str
        """
        logger.debug(f'[{self.name}] Широковещательная внутренняя цель: \'{internal_goal}\'.')

        for agent in self.agents:
            agent.internalize_goal(internal_goal)

    @transactional
    def broadcast_context_change(self, context: list) -> None:
        """
        Распространяет изменение контекста среди всех агентов в окружении.

        :param context: Содержание изменения контекста.
        :type context: list
        """
        logger.debug(f'[{self.name}] Широковещательное изменение контекста: \'{context}\'.')

        for agent in self.agents:
            agent.change_context(context)

    def make_everyone_accessible(self) -> None:
        """
        Делает всех агентов в окружении доступными друг другу.
        """
        for agent_1 in self.agents:
            for agent_2 in self.agents:
                if agent_1 != agent_2:
                    agent_1.make_agent_accessible(agent_2)

    ###########################################################
    # Удобства форматирования
    ###########################################################

    def _display_communication(self, cur_step: int, total_steps: int, kind: str,
                              timedelta_per_step: timedelta = None) -> None:
        """
        Отображает текущую коммуникацию и сохраняет ее в буфере.

        :param cur_step: Текущий шаг.
        :type cur_step: int
        :param total_steps: Общее количество шагов.
        :type total_steps: int
        :param kind: Тип коммуникации.
        :type kind: str
        :param timedelta_per_step: Временной интервал шага.
        :type timedelta_per_step: timedelta, optional
        """
        if kind == 'step':
            rendering = self._pretty_step(cur_step=cur_step, total_steps=total_steps,
                                          timedelta_per_step=timedelta_per_step)
        else:
            raise ValueError(f'Неизвестный тип коммуникации: {kind}')

        self._push_and_display_latest_communication({'content': rendering, 'kind': kind})

    def _push_and_display_latest_communication(self, rendering: dict) -> None:
        """
        Добавляет последние коммуникации в буфер.

        :param rendering: Данные коммуникации.
        :type rendering: dict
        """
        self._displayed_communications_buffer.append(rendering)
        self._display(rendering)

    def pop_and_display_latest_communications(self) -> list:
        """
        Извлекает последние коммуникации из буфера и отображает их.

        :return: Список извлеченных коммуникаций.
        :rtype: list
        """
        communications = self._displayed_communications_buffer
        self._displayed_communications_buffer = []

        for communication in communications:
            self._display(communication)

        return communications

    def _display(self, communication: dict | str) -> None:
        """
        Отображает коммуникацию в консоли.

        :param communication: Данные коммуникации.
        :type communication: dict | str
        """
        # извлекаем данные для отображения
        if isinstance(communication, dict):
            content = communication['content']
            kind = communication['kind']
        else:
            content = communication
            kind = None

        # отображаем в зависимости от типа
        if kind == 'step':
            self.console.rule(content)
        else:
            self.console.print(content)

    def clear_communications_buffer(self) -> None:
        """
        Очищает буфер коммуникаций.
        """
        self._displayed_communications_buffer = []

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта.

        :return: Строковое представление объекта.
        :rtype: str
        """
        return f'TinyWorld(name=\'{self.name}\')'

    def _pretty_step(self, cur_step: int, total_steps: int, timedelta_per_step: timedelta = None) -> str:
        """
        Форматирует строку для отображения шага.

        :param cur_step: Текущий шаг.
        :type cur_step: int
        :param total_steps: Общее количество шагов.
        :type total_steps: int
        :param timedelta_per_step: Временной интервал шага.
        :type timedelta_per_step: timedelta, optional
        :return: Отформатированная строка.
        :rtype: str
        """
        rendering = f'{self.name} шаг {cur_step} из {total_steps}'
        if timedelta_per_step is not None:
            rendering += f' ({pretty_datetime(self.current_datetime)})'

        return rendering

    def pp_current_interactions(self, simplified: bool = True, skip_system: bool = True) -> None:
        """
        Выводит в консоль текущие сообщения агентов в окружении.

        :param simplified: Флаг упрощенного вывода.
        :type simplified: bool, optional
        :param skip_system: Флаг пропуска системных сообщений.
        :type skip_system: bool, optional
        """
        print(self.pretty_current_interactions(simplified=simplified, skip_system=skip_system))

    def pretty_current_interactions(self, simplified: bool = True, skip_system: bool = True,
                                   max_content_length: int = 1000, first_n: int = None, last_n: int = None,
                                   include_omission_info: bool = True) -> str:
        """
        Возвращает форматированную строку с текущими сообщениями агентов в окружении.

        :param simplified: Флаг упрощенного вывода.
        :type simplified: bool, optional
        :param skip_system: Флаг пропуска системных сообщений.
        :type skip_system: bool, optional
        :param max_content_length: Максимальная длина содержимого сообщения.
        :type max_content_length: int, optional
        :param first_n: Вывести первые N сообщений.
        :type first_n: int, optional
        :param last_n: Вывести последние N сообщений.
        :type last_n: int, optional
        :param include_omission_info: Включить информацию о пропущенных сообщениях.
        :type include_omission_info: bool, optional
        :return: Отформатированная строка.
        :rtype: str
        """
        agent_contents = []

        for agent in self.agents:
            agent_content = f'#### Взаимодействия с точки зрения агента {agent.name}:\\n'
            agent_content += f'**НАЧАЛО ИСТОРИИ АГЕНТА {agent.name}.**\\n '
            agent_content += agent.pretty_current_interactions(simplified=simplified, skip_system=skip_system,
                                                              max_content_length=max_content_length, first_n=first_n,
                                                              last_n=last_n,
                                                              include_omission_info=include_omission_info) + '\\n'
            agent_content += f'**КОНЕЦ ИСТОРИИ АГЕНТА {agent.name}.**\\n\\n'
            agent_contents.append(agent_content)

        return '\\n'.join(agent_contents)

    #######################################################################
    # IO
    #######################################################################

    def encode_complete_state(self) -> dict:
        """
        Кодирует полное состояние окружения в словарь.

        :return: Словарь с полным состоянием окружения.
        :rtype: dict
        """
        to_copy = copy.copy(self.__dict__)

        # удаление ненужных полей
        del to_copy['console']
        del to_copy['agents']
        del to_copy['name_to_agent']
        del to_copy['current_datetime']

        state = copy.deepcopy(to_copy)

        # агенты кодируются отдельно
        state['agents'] = [agent.encode_complete_state() for agent in self.agents]

        # дата тоже кодируется отдельно
        state['current_datetime'] = self.current_datetime.isoformat()

        return state

    def decode_complete_state(self, state: dict) -> "TinyWorld":
        """
        Декодирует полное состояние окружения из словаря.

        :param state: Словарь с полным состоянием окружения.
        :type state: dict
        :return: Объект окружения.
        :rtype: TinyWorld
        """
        state = copy.deepcopy(state)

        #################################
        # восстановление агентов
        #################################
        self.remove_all_agents()
        for agent_state in state['agents']:
            try:
                try:
                    agent = TinyPerson.get_agent_by_name(agent_state['name'])
                except Exception as e:
                    raise ValueError(f'Не удалось найти агента {agent_state["name"]} для окружения {self.name}.') from e

                agent.decode_complete_state(agent_state)
                self.add_agent(agent)

            except Exception as e:
                raise ValueError(f'Не удалось декодировать агента {agent_state["name"]} для окружения {self.name}.') from e

        # удаление агентов, чтобы обновить остальное состояние
        del state['agents']

        # восстановление даты
        state['current_datetime'] = datetime.fromisoformat(state['current_datetime'])

        # восстановление остальных полей
        self.__dict__.update(state)

        return self

    @staticmethod
    def add_environment(environment: "TinyWorld") -> None:
        """
        Добавляет окружение в список всех окружений.

        Имена окружений должны быть уникальными.

        :param environment: Окружение для добавления.
        :type environment: TinyWorld
        :raises ValueError: Если имя окружения не уникально.
        """
        if environment.name in TinyWorld.all_environments:
            raise ValueError(f'Имена окружений должны быть уникальными, но \'{environment.name}\' уже определено.')
        else:
            TinyWorld.all_environments[environment.name] = environment

    @staticmethod
    def set_simulation_for_free_environments(simulation) -> None:
        """
        Устанавливает симуляцию, если она None.

        Позволяет свободным окружениям быть захваченными в рамках симуляции.

        :param simulation: Объект симуляции.
        :type simulation: Simulation
        """
        for environment in TinyWorld.all_environments.values():
            if environment.simulation_id is None:
                simulation.add_environment(environment)

    @staticmethod
    def get_environment_by_name(name: str) -> "TinyWorld" | None:
        """
        Возвращает окружение по имени.

        :param name: Имя окружения.
        :type name: str
        :return: Окружение с указанным именем или None, если такого окружения нет.
        :rtype: TinyWorld, optional
        """
        if name in TinyWorld.all_environments:
            return TinyWorld.all_environments[name]
        else:
            return None

    @staticmethod
    def clear_environments() -> None:
        """
        Очищает список всех окружений.
        """
        TinyWorld.all_environments = {}


class TinySocialNetwork(TinyWorld):
    """
    Класс для моделирования социальной сети.

    :ivar relations: Словарь связей между агентами.
    :vartype relations: dict
    """
    def __init__(self, name: str, broadcast_if_no_target: bool = True):
        """
        Создает новую социальную сеть.

        :param name: Имя окружения.
        :type name: str
        :param broadcast_if_no_target: Флаг трансляции действий.
        :type broadcast_if_no_target: bool
        """

        super().__init__(name, broadcast_if_no_target=broadcast_if_no_target)

        self.relations = {}

    @transactional
    def add_relation(self, agent_1: TinyPerson, agent_2: TinyPerson, name: str = 'default') -> "TinySocialNetwork":
        """
        Добавляет связь между двумя агентами.

        :param agent_1: Первый агент.
        :type agent_1: TinyPerson
        :param agent_2: Второй агент.
        :type agent_2: TinyPerson
        :param name: Имя связи.
        :type name: str, optional
        :return: self для возможности вызова цепочки.
        :rtype: TinySocialNetwork
        """
        logger.debug(f'Добавление связи {name} между {agent_1.name} и {agent_2.name}.')

        # агенты должны быть в окружении, если нет, они добавляются
        if agent_1 not in self.agents:
            self.agents.append(agent_1)
        if agent_2 not in self.agents:
            self.agents.append(