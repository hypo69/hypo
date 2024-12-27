# Анализ кода модуля `environment.py`

**Качество кода: 7/10**

*   **Плюсы:**
    *   Хорошая структура классов `TinyWorld` и `TinySocialNetwork`.
    *   Используется `logger` для логирования.
    *   Присутствуют методы для управления временем (`run`, `skip` с разными единицами времени).
    *   Есть методы для добавления, удаления и получения агентов.
    *   Реализовано сохранение и восстановление состояния среды.
    *   Использование `transactional` для управления состоянием.
    *   `TinySocialNetwork` наследуется от `TinyWorld` и расширяет его функциональность.

*   **Минусы:**
    *   Отсутствуют docstring для многих методов и классов.
    *   Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    *   Некоторые комментарии не соответствуют RST.
    *   Используются стандартные блоки `try-except`, где можно было бы использовать `logger.error`.
    *   Методы `_display_communication` и `_push_and_display_latest_communication` можно переименовать.
    *   В `add_relation` проверка на наличие агентов может быть более лаконичной.

**Рекомендации по улучшению**

1.  **Документация:**
    *   Добавить docstring в формате RST ко всем классам, методам и функциям.
    *   Переписать существующие комментарии в формате RST.

2.  **Обработка данных:**
    *   В данном файле нет необходимости использовать `j_loads` или `j_loads_ns`, поскольку нет загрузки данных из файла.

3.  **Логирование:**
    *   Избегать `try-except` блоков, используя `logger.error` для обработки ошибок.
    *   Добавить логирование в `add_relation`.

4.  **Рефакторинг:**
    *   Переименовать методы `_display_communication` и `_push_and_display_latest_communication` в более понятные имена.
    *   Упростить добавление агентов в `add_relation`.
    *   Добавить проверки на корректность входных данных в некоторых методах.

5.  **Структура:**
    *   Разделить длинные методы на более мелкие, если это уместно.

6.  **Улучшения:**
    *   Добавить `TypeVar` для `Self` в методах, где возвращается экземпляр класса.
    *   Улучшить обработку ошибок в `decode_complete_state`.
    *   Добавить возможность сохранения коммуникаций в файл.

**Оптимизированный код**

```python
"""
Модуль для определения окружений, в которых агенты взаимодействуют.
=========================================================================================

Этот модуль предоставляет классы ``TinyWorld`` и ``TinySocialNetwork`` для создания и управления
виртуальными средами, в которых агенты могут взаимодействовать друг с другом, а также с внешними
сущностями.

Пример использования
--------------------

Пример создания и запуска симуляции в среде TinyWorld:

.. code-block:: python

    from datetime import datetime, timedelta
    from tinytroupe.environment import TinyWorld
    from tinytroupe.agent import TinyPerson
    
    world = TinyWorld(name='MyWorld')
    agent1 = TinyPerson(name='Agent1')
    agent2 = TinyPerson(name='Agent2')
    world.add_agents([agent1, agent2])
    world.run(steps=10, timedelta_per_step=timedelta(minutes=1))
"""
import copy
from datetime import datetime, timedelta
from typing import Any, TypeVar, Union

from rich.console import Console

from tinytroupe.agent import TinyPerson
from tinytroupe.utils import name_or_empty, pretty_datetime
import tinytroupe.control as control  # type: ignore
from tinytroupe.control import transactional
from src.logger.logger import logger # type: ignore


AgentOrWorld = Union["TinyPerson", "TinyWorld"]
Self = TypeVar("Self", bound="TinyWorld")


class TinyWorld:
    """
    Базовый класс для создания виртуальных окружений.
    
    Предоставляет основные методы для управления агентами, временем и действиями.

    :ivar all_environments: Словарь всех созданных окружений.
    :vartype all_environments: dict[str, TinyWorld]
    :ivar communication_display: Флаг отображения коммуникаций в консоли.
    :vartype communication_display: bool
    """

    # Словарь всех созданных окружений.
    all_environments = {} # name -> environment

    # Флаг отображения коммуникаций в консоли.
    communication_display = True

    def __init__(self, name: str="A TinyWorld", agents:list =[],
                 initial_datetime: datetime = datetime.now(),
                 broadcast_if_no_target: bool =True):
        """
        Инициализирует окружение.

        :param name: Имя окружения.
        :type name: str
        :param agents: Список агентов для добавления в окружение.
        :type agents: list
        :param initial_datetime: Начальная дата и время окружения.
        :type initial_datetime: datetime
        :param broadcast_if_no_target: Флаг широковещательной рассылки действий, если цель не найдена.
        :type broadcast_if_no_target: bool
        """

        self.name = name
        self.current_datetime = initial_datetime
        self.broadcast_if_no_target = broadcast_if_no_target
        self.simulation_id = None # будет сброшен позже, если агент используется в определенной области моделирования
        
        
        self.agents = []
        self.name_to_agent = {} # {agent_name: agent, agent_name_2: agent_2, ...}

        # буфер коммуникаций, которые уже были отображены, используется для
        # сохранения этих коммуникаций в другой выходной форме позже (например, кэширование)
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

        Эта реализация по умолчанию вызывает действия всех агентов в окружении.
        Подклассы могут переопределить этот метод для реализации других политик.

        :param timedelta_per_step: Временной интервал между шагами.
        :type timedelta_per_step: timedelta, optional
        :return: Словарь действий агентов.
        :rtype: dict
        """
        # увеличивает текущую дату и время, если задано timedelta. Это должно произойти до
        # любых других обновлений симуляции, чтобы убедиться, что агенты действуют
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

    def _advance_datetime(self, timedelta: timedelta = None):
        """
        Увеличивает текущее время окружения на заданный интервал.

        :param timedelta: Временной интервал.
        :type timedelta: timedelta, optional
        """
        if timedelta is not None:
            self.current_datetime += timedelta
        else:
            logger.info(f"[{self.name}] No timedelta provided, so the datetime was not advanced.")

    @transactional
    def run(self, steps: int, timedelta_per_step: timedelta = None, return_actions: bool = False) -> Union[list, None]:
        """
        Запускает окружение на заданное количество шагов.

        :param steps: Количество шагов.
        :type steps: int
        :param timedelta_per_step: Временной интервал между шагами.
        :type timedelta_per_step: timedelta, optional
        :param return_actions: Флаг возврата действий агентов.
        :type return_actions: bool, optional
        :return: Список действий агентов, если `return_actions` равен `True`.
        :rtype: list, optional
        """
        agents_actions_over_time = []
        for i in range(steps):
            logger.info(f"[{self.name}] Running world simulation step {i+1} of {steps}.")

            if TinyWorld.communication_display:
                self._display_communication(cur_step=i+1, total_steps=steps, kind='step', timedelta_per_step=timedelta_per_step)

            agents_actions = self._step(timedelta_per_step=timedelta_per_step)
            agents_actions_over_time.append(agents_actions)
        
        if return_actions:
            return agents_actions_over_time
        return None
    
    @transactional
    def skip(self, steps: int, timedelta_per_step: timedelta = None):
        """
        Пропускает заданное количество шагов в окружении.

        Время проходит, но никаких действий агентами не выполняется.

        :param steps: Количество шагов для пропуска.
        :type steps: int
        :param timedelta_per_step: Временной интервал между шагами.
        :type timedelta_per_step: timedelta, optional
        """
        self._advance_datetime(steps * timedelta_per_step)

    def run_minutes(self, minutes: int):
        """
        Запускает окружение на заданное количество минут.

        :param minutes: Количество минут для запуска.
        :type minutes: int
        """
        self.run(steps=minutes, timedelta_per_step=timedelta(minutes=1))
    
    def skip_minutes(self, minutes: int):
        """
        Пропускает заданное количество минут в окружении.

        :param minutes: Количество минут для пропуска.
        :type minutes: int
        """
        self.skip(steps=minutes, timedelta_per_step=timedelta(minutes=1))
    
    def run_hours(self, hours: int):
        """
        Запускает окружение на заданное количество часов.

        :param hours: Количество часов для запуска.
        :type hours: int
        """
        self.run(steps=hours, timedelta_per_step=timedelta(hours=1))
    
    def skip_hours(self, hours: int):
        """
        Пропускает заданное количество часов в окружении.

        :param hours: Количество часов для пропуска.
        :type hours: int
        """
        self.skip(steps=hours, timedelta_per_step=timedelta(hours=1))
    
    def run_days(self, days: int):
        """
        Запускает окружение на заданное количество дней.

        :param days: Количество дней для запуска.
        :type days: int
        """
        self.run(steps=days, timedelta_per_step=timedelta(days=1))
    
    def skip_days(self, days: int):
        """
        Пропускает заданное количество дней в окружении.

        :param days: Количество дней для пропуска.
        :type days: int
        """
        self.skip(steps=days, timedelta_per_step=timedelta(days=1))
    
    def run_weeks(self, weeks: int):
        """
        Запускает окружение на заданное количество недель.

        :param weeks: Количество недель для запуска.
        :type weeks: int
        """
        self.run(steps=weeks, timedelta_per_step=timedelta(weeks=1))
    
    def skip_weeks(self, weeks: int):
        """
        Пропускает заданное количество недель в окружении.

        :param weeks: Количество недель для пропуска.
        :type weeks: int
        """
        self.skip(steps=weeks, timedelta_per_step=timedelta(weeks=1))
    
    def run_months(self, months: int):
        """
        Запускает окружение на заданное количество месяцев.

        :param months: Количество месяцев для запуска.
        :type months: int
        """
        self.run(steps=months, timedelta_per_step=timedelta(weeks=4))
    
    def skip_months(self, months: int):
        """
        Пропускает заданное количество месяцев в окружении.

        :param months: Количество месяцев для пропуска.
        :type months: int
        """
        self.skip(steps=months, timedelta_per_step=timedelta(weeks=4))
    
    def run_years(self, years: int):
        """
        Запускает окружение на заданное количество лет.

        :param years: Количество лет для запуска.
        :type years: int
        """
        self.run(steps=years, timedelta_per_step=timedelta(days=365))
    
    def skip_years(self, years: int):
        """
        Пропускает заданное количество лет в окружении.

        :param years: Количество лет для пропуска.
        :type years: int
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
        :return: Текущий экземпляр окружения.
        :rtype: Self
        """
        for agent in agents:
            self.add_agent(agent)
        
        return self # for chaining

    def add_agent(self, agent: TinyPerson) -> Self:
        """
        Добавляет агента в окружение.

        Имена агентов должны быть уникальными в пределах окружения.

        :param agent: Агент для добавления.
        :type agent: TinyPerson
        :raises ValueError: Если имя агента не уникально в окружении.
        :return: Текущий экземпляр окружения.
        :rtype: Self
        """

        # проверка, если агент еще не в окружении
        if agent not in self.agents:
            logger.debug(f"Adding agent {agent.name} to the environment.")
            
            # Имена агентов должны быть уникальными в окружении.
            # Проверка, если имя агента уже есть.
            if agent.name not in self.name_to_agent:
                agent.environment = self
                self.agents.append(agent)
                self.name_to_agent[agent.name] = agent
            else:
                raise ValueError(f"Agent names must be unique, but '{agent.name}' is already in the environment.")
        else:
            logger.warn(f"Agent {agent.name} is already in the environment.")
        
        return self # for chaining

    def remove_agent(self, agent: TinyPerson) -> Self:
        """
        Удаляет агента из окружения.

        :param agent: Агент для удаления.
        :type agent: TinyPerson
        :return: Текущий экземпляр окружения.
        :rtype: Self
        """
        logger.debug(f"Removing agent {agent.name} from the environment.")
        self.agents.remove(agent)
        del self.name_to_agent[agent.name]

        return self # for chaining
    
    def remove_all_agents(self) -> Self:
        """
        Удаляет всех агентов из окружения.

        :return: Текущий экземпляр окружения.
        :rtype: Self
        """
        logger.debug(f"Removing all agents from the environment.")
        self.agents = []
        self.name_to_agent = {}

        return self # for chaining

    def get_agent_by_name(self, name: str) -> Union[TinyPerson, None]:
        """
        Возвращает агента с заданным именем.

        Если агент с таким именем не существует в окружении, возвращает `None`.

        :param name: Имя агента для поиска.
        :type name: str
        :return: Агент с заданным именем или `None`.
        :rtype: TinyPerson, optional
        """
        if name in self.name_to_agent:
            return self.name_to_agent[name]
        else:
            return None
        

    #######################################################################
    # Обработчики действий
    #
    # Конкретные действия, инициированные агентами, обрабатываются окружением,
    # поскольку они имеют последствия за пределами самого агента.
    #######################################################################
    @transactional
    def _handle_actions(self, source: TinyPerson, actions: list):
        """
        Обрабатывает действия, инициированные агентами.

        :param source: Агент, инициировавший действия.
        :type source: TinyPerson
        :param actions: Список действий в формате JSON.
        :type actions: list
        """
        for action in actions:
            action_type = action["type"] # это единственное обязательное поле
            content = action["content"] if "content" in action else None
            target = action["target"] if "target" in action else None

            logger.debug(f"[{self.name}] Handling action {action_type} from agent {name_or_empty(source)}. Content: {content}, target: {target}.")

            # только некоторые действия требуют вмешательства среды
            if action_type == "REACH_OUT":
                self._handle_reach_out(source, content, target)
            elif action_type == "TALK":
                self._handle_talk(source, content, target)

    @transactional
    def _handle_reach_out(self, source_agent: TinyPerson, content: str, target: str):
        """
        Обрабатывает действие `REACH_OUT`.

        Эта реализация по умолчанию всегда позволяет `REACH_OUT` завершиться успешно.
        Подклассы могут переопределить этот метод для реализации других политик.

        :param source_agent: Агент, инициировавший действие `REACH_OUT`.
        :type source_agent: TinyPerson
        :param content: Содержание сообщения.
        :type content: str
        :param target: Цель сообщения.
        :type target: str
        """

        # Эта реализация по умолчанию всегда позволяет REACH_OUT завершиться успешно.
        target_agent = self.get_agent_by_name(target)
        
        source_agent.make_agent_accessible(target_agent)
        target_agent.make_agent_accessible(source_agent)

        source_agent.socialize(f"{name_or_empty(target_agent)} was successfully reached out, and is now available for interaction.", source=self)
        target_agent.socialize(f"{name_or_empty(source_agent)} reached out to you, and is now available for interaction.", source=self)

    @transactional
    def _handle_talk(self, source_agent: TinyPerson, content: str, target: str):
        """
        Обрабатывает действие `TALK`, доставляя сообщение указанной цели.

        :param source_agent: Агент, инициировавший действие `TALK`.
        :type source_agent: TinyPerson
        :param content: Содержание сообщения.
        :type content: str
        :param target: Цель сообщения.
        :type target: str
        """
        target_agent = self.get_agent_by_name(target)

        logger.debug(f"[{self.name}] Delivering message from {name_or_empty(source_agent)} to {name_or_empty(target_agent)}.")

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
        Доставляет сообщение всем агентам в окружении.

        :param speech: Содержание сообщения.
        :type speech: str
        :param source: Агент или окружение, инициировавшее сообщение.
        :type source: AgentOrWorld, optional
        """
        logger.debug(f"[{self.name}] Broadcasting message: '{speech}'.")

        for agent in self.agents:
            # не доставлять сообщение источнику
            if agent != source:
                agent.listen(speech, source=source)
    
    @transactional
    def broadcast_thought(self, thought: str, source: AgentOrWorld=None):
        """
        Широковещательная рассылка мысли всем агентам в окружении.

        :param thought: Содержание мысли.
        :type thought: str
        """
        logger.debug(f"[{self.name}] Broadcasting thought: '{thought}'.")

        for agent in self.agents:
            agent.think(thought)
    
    @transactional
    def broadcast_internal_goal(self, internal_goal: str):
        """
        Широковещательная рассылка внутренней цели всем агентам в окружении.

        :param internal_goal: Содержание внутренней цели.
        :type internal_goal: str
        """
        logger.debug(f"[{self.name}] Broadcasting internal goal: '{internal_goal}'.")

        for agent in self.agents:
            agent.internalize_goal(internal_goal)
    
    @transactional
    def broadcast_context_change(self, context:list):
        """
        Широковещательная рассылка изменения контекста всем агентам в окружении.

        :param context: Содержание изменения контекста.
        :type context: list
        """
        logger.debug(f"[{self.name}] Broadcasting context change: '{context}'.")

        for agent in self.agents:
            agent.change_context(context)

    def make_everyone_accessible(self):
        """
        Делает всех агентов в окружении доступными друг для друга.
        """
        for agent_1 in self.agents:
            for agent_2 in self.agents:
                if agent_1 != agent_2:
                    agent_1.make_agent_accessible(agent_2)
            

    ###########################################################
    # Удобства форматирования
    ###########################################################

    # TODO лучшие имена для этих методов "display"
    def _display_communication(self, cur_step: int, total_steps: int, kind: str, timedelta_per_step: timedelta = None):
        """
        Отображает текущее сообщение и сохраняет его в буфер для дальнейшего использования.

        :param cur_step: Текущий шаг симуляции.
        :type cur_step: int
        :param total_steps: Общее количество шагов симуляции.
        :type total_steps: int
        :param kind: Тип сообщения.
        :type kind: str
        :param timedelta_per_step: Временной интервал между шагами.
        :type timedelta_per_step: timedelta, optional
        :raises ValueError: Если тип сообщения неизвестен.
        """
        if kind == 'step':
            rendering = self._pretty_step(cur_step=cur_step, total_steps=total_steps, timedelta_per_step=timedelta_per_step)
        else:
            raise ValueError(f"Unknown communication kind: {kind}")

        self._push_and_display_latest_communication({"content": rendering, "kind": kind})
    
    def _push_and_display_latest_communication(self, rendering: dict):
        """
        Помещает последние сообщения в буфер агента.

        :param rendering: Сообщение для отображения.
        :type rendering: dict
        """
        self._displayed_communications_buffer.append(rendering)
        self._display(rendering)

    def pop_and_display_latest_communications(self) -> list:
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

    def _display(self, communication: Union[str, dict]):
        """
        Отображает сообщение в консоли.

        :param communication: Сообщение для отображения.
        :type communication: str, dict
        """
        # распаковка рендеринга для поиска дополнительной информации
        if isinstance(communication, dict):
            content = communication["content"]
            kind = communication["kind"]
        else:
            content = communication
            kind = None
            
        # рендеринг как положено
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
        """
        return f"TinyWorld(name='{self.name}')"

    def _pretty_step(self, cur_step: int, total_steps: int, timedelta_per_step: timedelta = None) -> str:
        """
        Форматирует информацию о текущем шаге.

        :param cur_step: Текущий шаг симуляции.
        :type cur_step: int
        :param total_steps: Общее количество шагов симуляции.
        :type total_steps: int
        :param timedelta_per_step: Временной интервал между шагами.
        :type timedelta_per_step: timedelta, optional
        :return: Отформатированная строка с информацией о шаге.
        :rtype: str
        """
        rendering = f"{self.name} step {cur_step} of {total_steps}"
        if timedelta_per_step is not None:
            rendering += f" ({pretty_datetime(self.current_datetime)})"

        return rendering

    def pp_current_interactions(self, simplified: bool = True, skip_system: bool = True):
        """
        Выводит в консоль текущие сообщения агентов в этом окружении.

        :param simplified: Флаг упрощенного вывода.
        :type simplified: bool, optional
        :param skip_system: Флаг пропуска системных сообщений.
        :type skip_system: bool, optional
        """
        print(self.pretty_current_interactions(simplified=simplified, skip_system=skip_system))

    def pretty_current_interactions(self, simplified: bool = True, skip_system: bool = True, 
                                    max_content_length: int = default["max_content_display_length"], # type: ignore
                                    first_n: int = None, last_n: int = None, include_omission_info: bool = True) -> str:
        """
        Возвращает отформатированную строку с текущими сообщениями агентов.

        :param simplified: Флаг упрощенного вывода.
        :type simplified: bool, optional
        :param skip_system: Флаг пропуска системных сообщений.
        :type skip_system: bool, optional
        :param max_content_length: Максимальная длина содержания сообщения.
        :type max_content_length: int, optional
        :param first_n: Количество первых сообщений для включения.
        :type first_n: int, optional
        :param last_n: Количество последних сообщений для включения.
        :type last_n: int, optional
        :param include_omission_info: Флаг включения информации о пропущенных сообщениях.
        :type include_omission_info: bool, optional
        :return: Отформатированная строка с сообщениями агентов.
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
        Кодирует полное состояние окружения в словарь.

        :return: Словарь, кодирующий полное состояние окружения.
        :rtype: dict
        """
        to_copy = copy.copy(self.__dict__)

        # удаление логгера и других полей
        del to_copy['console']
        del to_copy['agents']
        del to_copy['name_to_agent']
        del to_copy['current_datetime']

        state = copy.deepcopy(to_copy)

        # агенты кодируются отдельно
        state["agents"] = [agent.encode_complete_state() for agent in self.agents]

        # дата и время также должны быть закодированы отдельно
        state["current_datetime"] = self.current_datetime.isoformat()

        return state
    
    def decode_complete_state(self, state: dict) -> Self:
        """
        Декодирует полное состояние окружения из словаря.

        :param state: Словарь, кодирующий состояние окружения.
        :type state: dict
        :return: Окружение, декодированное из словаря.
        :rtype: Self
        """
        state = copy.deepcopy(state)

        #################################
        # восстановление агентов на месте
        #################################
        self.remove_all_agents()
        for agent_state in state["agents"]:
            try:
                try:
                    agent = TinyPerson.get_agent_by_name(agent_state["name"])
                except Exception as e:
                    raise ValueError(f"Could not find agent {agent_state['name']} for environment {self.name}.") from e
                
                agent.decode_complete_state(agent_state)
                self.add_agent(agent)
                
            except Exception as e:
               logger.error(f"Could not decode agent {agent_state['name']} for environment {self.name}.", exc_info=True)
               raise ValueError(f"Could not decode agent {agent_state['name']} for environment {self.name}.") from e
        
        # удаление состояний агентов для обновления остальной части окружения
        del state["agents"]

        # восстановление даты и времени
        state["current_datetime"] = datetime.fromisoformat(state["current_datetime"])

        # восстановление других полей
        self.__dict__.update(state)

        return self

    @staticmethod
    def add_environment(environment):
        """
        Добавляет окружение в список всех окружений.

        Имена окружений должны быть уникальными. Если окружение с таким именем уже существует, возникает ошибка.

        :param environment: Окружение для добавления.
        :type environment: TinyWorld
        :raises ValueError: Если имя окружения не уникально.
        """
        if environment.name in TinyWorld.all_environments:
            raise ValueError(f"Environment names must be unique, but '{environment.name}' is already defined.")
        else:
            TinyWorld.all_environments[environment.name] = environment
        

    @staticmethod
    def set_simulation_for_free_environments(simulation):
        """
        Устанавливает симуляцию, если она равна None.

        Это позволяет свободным окружениям быть захваченными конкретными областями моделирования, если это необходимо.

        :param simulation: Симуляция для установки.
        :type simulation: Simulation
        """
        for environment in TinyWorld.all_environments.values():
            if environment.simulation_id is None:
                simulation.add_environment(environment)
    
    @staticmethod
    def get_environment_by_name(name: str) -> Union["TinyWorld", None]:
        """
        Возвращает окружение с заданным именем.

        Если окружение с таким именем не существует, возвращает `None`.

        :param name: Имя окружения для поиска.
        :type name: str
        :return: Окружение с заданным именем или `None`.
        :rtype: TinyWorld, optional
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
    Класс для создания социальных сетей, основанных на отношениях между агентами.

    :ivar relations: Словарь отношений между агентами.
    :vartype relations: dict
    """

    def __init__(self, name: str, broadcast_if_no_target: bool=True):
        """
        Создает новое окружение `TinySocialNetwork`.

        :param name: Имя окружения.
        :type name: str
        :param broadcast_if_no_target: Флаг широковещательной рассылки действий через доступные отношения агента,
            если цель действия не найдена.
        :type broadcast_if_no_target: bool, optional
        """
        
        super().__init__(name, broadcast_if_no_target=broadcast_