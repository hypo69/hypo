# Модуль `environment`

## Обзор

Модуль `environment` предоставляет структуру для определения мира, в котором агенты взаимодействуют друг с другом, а также с внешними сущностями, такими как поисковые системы. Он содержит классы для моделирования окружения (`TinyWorld`) и социальных сетей (`TinySocialNetwork`), а также вспомогательные функции для управления агентами и их взаимодействиями.

## Подробнее

Этот модуль является основой для создания симуляций, в которых агенты (представленные классом `TinyPerson` из модуля `agent`) могут взаимодействовать друг с другом и с окружением. Он предоставляет инструменты для управления временем, добавления и удаления агентов, обработки действий агентов и моделирования социальных связей между ними.

## Классы

### `TinyWorld`

**Описание**: Базовый класс для создания окружений.

**Принцип работы**: Класс `TinyWorld` предоставляет основные методы для управления агентами, временем и взаимодействиями в симулируемой среде. Он содержит методы для добавления и удаления агентов, запуска симуляции на определенное количество шагов, обработки действий агентов и ведения журнала коммуникаций.

**Аттрибуты**:

-   `all_environments` (dict): Словарь, содержащий все созданные окружения (`name -> environment`).
-   `communication_display` (bool): Флаг, определяющий, отображать ли коммуникации в окружении.
-   `name` (str): Название окружения.
-   `current_datetime` (datetime): Текущее время в окружении.
-   `broadcast_if_no_target` (bool): Флаг, определяющий, транслировать ли действия, если цель не найдена.
-   `simulation_id` (Any): Идентификатор симуляции, к которой принадлежит окружение.
-   `agents` (list): Список агентов в окружении.
-   `name_to_agent` (dict): Словарь, связывающий имена агентов с их экземплярами (`{agent_name: agent, agent_name_2: agent_2, ...}`).
-   `_displayed_communications_buffer` (list): Буфер отображенных коммуникаций.
-   `console` (Console): Консоль для вывода информации.

**Методы**:

-   `__init__(self, name: str="A TinyWorld", agents=[], initial_datetime=datetime.datetime.now(), broadcast_if_no_target=True)`: Инициализирует окружение.
-   `_step(self, timedelta_per_step=None)`: Выполняет один шаг симуляции.
-   `_advance_datetime(self, timedelta)`: Изменяет текущую дату и время окружения на заданный промежуток времени.
-   `run(self, steps: int, timedelta_per_step=None, return_actions=False)`: Запускает симуляцию на заданное количество шагов.
-   `skip(self, steps: int, timedelta_per_step=None)`: Пропускает заданное количество шагов в симуляции.
-   `run_minutes(self, minutes: int)`: Запускает симуляцию на заданное количество минут.
-   `skip_minutes(self, minutes: int)`: Пропускает заданное количество минут в симуляции.
-   `run_hours(self, hours: int)`: Запускает симуляцию на заданное количество часов.
-   `skip_hours(self, hours: int)`: Пропускает заданное количество часов в симуляции.
-   `run_days(self, days: int)`: Запускает симуляцию на заданное количество дней.
-   `skip_days(self, days: int)`: Пропускает заданное количество дней в симуляции.
-   `run_weeks(self, weeks: int)`: Запускает симуляцию на заданное количество недель.
-   `skip_weeks(self, weeks: int)`: Пропускает заданное количество недель в симуляции.
-   `run_months(self, months: int)`: Запускает симуляцию на заданное количество месяцев.
-   `skip_months(self, months: int)`: Пропускает заданное количество месяцев в симуляции.
-   `run_years(self, years: int)`: Запускает симуляцию на заданное количество лет.
-   `skip_years(self, years: int)`: Пропускает заданное количество лет в симуляции.
-   `add_agents(self, agents: list)`: Добавляет список агентов в окружение.
-   `add_agent(self, agent: TinyPerson)`: Добавляет агента в окружение.
-   `remove_agent(self, agent: TinyPerson)`: Удаляет агента из окружения.
-   `remove_all_agents(self)`: Удаляет всех агентов из окружения.
-   `get_agent_by_name(self, name: str) -> TinyPerson`: Возвращает агента по имени.
-   `_handle_actions(self, source: TinyPerson, actions: list)`: Обрабатывает действия, инициированные агентами.
-   `_handle_reach_out(self, source_agent: TinyPerson, content: str, target: str)`: Обрабатывает действие `REACH_OUT`.
-   `_handle_talk(self, source_agent: TinyPerson, content: str, target: str)`: Обрабатывает действие `TALK`.
-   `broadcast(self, speech: str, source: AgentOrWorld=None)`: Отправляет сообщение всем агентам в окружении.
-   `broadcast_thought(self, thought: str, source: AgentOrWorld=None)`: Отправляет мысль всем агентам в окружении.
-   `broadcast_internal_goal(self, internal_goal: str)`: Отправляет внутреннюю цель всем агентам в окружении.
-   `broadcast_context_change(self, context:list)`: Отправляет изменение контекста всем агентам в окружении.
-   `make_everyone_accessible(self)`: Делает всех агентов доступными друг для друга.
-   `_display_communication(self, cur_step, total_steps, kind, timedelta_per_step=None)`: Отображает текущую коммуникацию и сохраняет её в буфере.
-   `_push_and_display_latest_communication(self, rendering)`: Добавляет последнюю коммуникацию в буфер и отображает её.
-   `pop_and_display_latest_communications(self)`: Извлекает последние коммуникации из буфера и отображает их.
-   `_display(self, communication)`: Отображает коммуникацию.
-   `clear_communications_buffer(self)`: Очищает буфер коммуникаций.
-   `__repr__(self)`: Возвращает строковое представление объекта.
-   `_pretty_step(self, cur_step, total_steps, timedelta_per_step=None)`: Форматирует сообщение о шаге симуляции.
-   `pp_current_interactions(self, simplified=True, skip_system=True)`: Выводит в консоль текущие сообщения агентов в окружении.
-   `pretty_current_interactions(self, simplified=True, skip_system=True, max_content_length=default["max_content_display_length"], first_n=None, last_n=None, include_omission_info:bool=True)`: Возвращает отформатированную строку с текущими сообщениями агентов в окружении.
-   `encode_complete_state(self) -> dict`: Кодирует полное состояние окружения в словарь.
-   `decode_complete_state(self, state:dict) -> Self`: Декодирует полное состояние окружения из словаря.
-   `add_environment(environment)`: Добавляет окружение в список всех окружений.
    -   Статический метод.
-   `set_simulation_for_free_environments(simulation)`: Устанавливает симуляцию для свободных окружений.
    -   Статический метод.
-   `get_environment_by_name(name: str)`: Возвращает окружение по имени.
    -   Статический метод.
-   `clear_environments()`: Очищает список всех окружений.
    -   Статический метод.

### `TinySocialNetwork(TinyWorld)`

**Описание**: Класс для моделирования социальных сетей.

**Наследует**:

-   `TinyWorld`: Наследует базовый класс для окружений.

**Принцип работы**: Класс `TinySocialNetwork` расширяет функциональность `TinyWorld`, добавляя возможность моделировать социальные связи между агентами. Он позволяет определять отношения между агентами и управлять их доступностью друг для друга на основе этих отношений.

**Аттрибуты**:

-   `relations` (dict): Словарь, содержащий отношения между агентами.

**Методы**:

-   `__init__(self, name, broadcast_if_no_target=True)`: Инициализирует социальную сеть.
-   `add_relation(self, agent_1, agent_2, name="default")`: Добавляет отношение между двумя агентами.
-   `_update_agents_contexts(self)`: Обновляет контексты агентов на основе текущего состояния мира.
-   `_step(self)`: Выполняет один шаг симуляции в социальной сети.
-   `_handle_reach_out(self, source_agent: TinyPerson, content: str, target: str)`: Обрабатывает действие `REACH_OUT` в контексте социальных связей.
-   `is_in_relation_with(self, agent_1:TinyPerson, agent_2:TinyPerson, relation_name=None) -> bool`: Проверяет, находятся ли два агента в отношении друг с другом.

## Функции

### `_step`

```python
@transactional
def _step(self, timedelta_per_step=None):
    """
    Performs a single step in the environment. This default implementation
    simply calls makes all agents in the environment act and properly
    handle the resulting actions. Subclasses might override this method to implement 
    different policies.
    """
    # increase current datetime if timedelta is given. This must happen before
    # any other simulation updates, to make sure that the agents are acting
    # in the correct time, particularly if only one step is being run.
    self._advance_datetime(timedelta_per_step)

    # agents can act
    agents_actions = {}
    for agent in self.agents:
        logger.debug(f"[{self.name}] Agent {name_or_empty(agent)} is acting.")
        actions = agent.act(return_actions=True)
        agents_actions[agent.name] = actions

        self._handle_actions(agent, agent.pop_latest_actions())
    
    return agents_actions
```

**Назначение**: Выполняет один шаг в окружении.

**Параметры**:

-   `timedelta_per_step` (timedelta, optional): Временной интервал для каждого шага. По умолчанию `None`.

**Возвращает**:

-   `agents_actions` (dict): Словарь, содержащий действия, выполненные агентами на этом шаге.

**Как работает функция**:

1.  Функция увеличивает текущее время окружения, если предоставлен `timedelta_per_step`.
2.  Затем, для каждого агента в окружении, вызывается метод `act`, чтобы получить действия агента.
3.  Полученные действия обрабатываются с помощью метода `_handle_actions`.

```ascii
Начало --> Увеличение времени (если timedelta_per_step есть) -->
    Для каждого агента:
        --> Агент действует (agent.act()) --> Обработка действий (_handle_actions())
    Конец
```

**Примеры**:

```python
# Пример вызова функции _step с заданным timedelta_per_step
world = TinyWorld(name='MyWorld')
actions = world._step(timedelta_per_step=timedelta(minutes=10))

# Пример вызова функции _step без timedelta_per_step
world = TinyWorld(name='MyWorld')
actions = world._step()
```

### `_advance_datetime`

```python
def _advance_datetime(self, timedelta):
    """
    Advances the current datetime of the environment by the specified timedelta.

    Args:
        timedelta (timedelta): The timedelta to advance the current datetime by.
    """
    if timedelta is not None:
        self.current_datetime += timedelta
    else:
        logger.info(f"[{self.name}] No timedelta provided, so the datetime was not advanced.")
```

**Назначение**: Увеличивает текущее время окружения на заданный временной интервал.

**Параметры**:

-   `timedelta` (timedelta): Временной интервал, на который нужно увеличить текущее время.

**Как работает функция**:

1.  Проверяет, предоставлен ли `timedelta`.
2.  Если `timedelta` предоставлен, увеличивает `self.current_datetime` на `timedelta`.
3.  Если `timedelta` не предоставлен, записывает информационное сообщение в лог.

```ascii
Начало --> Проверка наличия timedelta -->
    Если timedelta есть:
        --> Увеличение current_datetime на timedelta
    Иначе:
        --> Запись информационного сообщения в лог
    Конец
```

**Примеры**:

```python
# Пример вызова функции _advance_datetime с заданным timedelta
import datetime
world = TinyWorld(name='MyWorld', initial_datetime=datetime.datetime(2024, 1, 1))
world._advance_datetime(timedelta=datetime.timedelta(days=1))
print(world.current_datetime)  # Вывод: 2024-01-02 00:00:00

# Пример вызова функции _advance_datetime без timedelta
world = TinyWorld(name='MyWorld')
world._advance_datetime(timedelta=None)  # Вывод: Запись в лог "No timedelta provided, so the datetime was not advanced."
```

### `run`

```python
@transactional
def run(self, steps: int, timedelta_per_step=None, return_actions=False):
    """
    Runs the environment for a given number of steps.

    Args:
        steps (int): The number of steps to run the environment for.
        timedelta_per_step (timedelta, optional): The time interval between steps. Defaults to None.
        return_actions (bool, optional): If True, returns the actions taken by the agents. Defaults to False.
    
    Returns:
        list: A list of actions taken by the agents over time, if return_actions is True. The list has this format:
              [{agent_name: [action_1, action_2, ...]}, {agent_name_2: [action_1, action_2, ...]}, ...]
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
```

**Назначение**: Запускает окружение на заданное количество шагов.

**Параметры**:

-   `steps` (int): Количество шагов для запуска окружения.
-   `timedelta_per_step` (timedelta, optional): Временной интервал между шагами. По умолчанию `None`.
-   `return_actions` (bool, optional): Если `True`, возвращает действия, предпринятые агентами. По умолчанию `False`.

**Возвращает**:

-   `list`: Список действий, предпринятых агентами во времени, если `return_actions` установлен в `True`.

**Как работает функция**:

1.  Инициализирует пустой список `agents_actions_over_time` для хранения действий агентов.
2.  Запускает цикл на `steps` итераций.
3.  На каждой итерации записывает информационное сообщение в лог.
4.  Если `TinyWorld.communication_display` установлен в `True`, отображает информацию о текущем шаге.
5.  Вызывает метод `_step` для выполнения одного шага симуляции.
6.  Добавляет действия агентов, возвращенные методом `_step`, в список `agents_actions_over_time`.
7.  Если `return_actions` установлен в `True`, возвращает список `agents_actions_over_time`.

```ascii
Начало --> Инициализация agents_actions_over_time -->
    Для i от 0 до steps:
        --> Запись информационного сообщения в лог -->
        Если TinyWorld.communication_display:
            --> Отображение информации о шаге
        --> Выполнение шага симуляции (_step()) -->
        Добавление действий агентов в agents_actions_over_time
    Если return_actions:
        --> Возврат agents_actions_over_time
    Конец
```

**Примеры**:

```python
# Пример запуска окружения на 10 шагов с возвратом действий агентов
world = TinyWorld(name='MyWorld')
actions = world.run(steps=10, return_actions=True)

# Пример запуска окружения на 5 шагов с временным интервалом в 1 минуту
world = TinyWorld(name='MyWorld')
world.run(steps=5, timedelta_per_step=datetime.timedelta(minutes=1))
```

### `skip`

```python
@transactional
def skip(self, steps: int, timedelta_per_step=None):
    """
    Skips a given number of steps in the environment. That is to say, time shall pass, but no actions will be taken
    by the agents or any other entity in the environment.

    Args:
        steps (int): The number of steps to skip.
        timedelta_per_step (timedelta, optional): The time interval between steps. Defaults to None.
    """
    self._advance_datetime(steps * timedelta_per_step)
```

**Назначение**: Пропускает заданное количество шагов в окружении.

**Параметры**:

-   `steps` (int): Количество шагов для пропуска.
-   `timedelta_per_step` (timedelta, optional): Временной интервал между шагами. По умолчанию `None`.

**Как работает функция**:

1.  Вызывает метод `_advance_datetime` для увеличения текущего времени окружения на `steps * timedelta_per_step`.

```ascii
Начало --> Увеличение времени на steps * timedelta_per_step (_advance_datetime()) --> Конец
```

**Примеры**:

```python
# Пример пропуска 10 шагов с временным интервалом в 1 минуту
world = TinyWorld(name='MyWorld')
world.skip(steps=10, timedelta_per_step=datetime.timedelta(minutes=1))

# Пример пропуска 5 шагов без временного интервала
world = TinyWorld(name='MyWorld')
world.skip(steps=5)
```

### `run_minutes`

```python
def run_minutes(self, minutes: int):
    """
    Runs the environment for a given number of minutes.

    Args:
        minutes (int): The number of minutes to run the environment for.
    """
    self.run(steps=minutes, timedelta_per_step=timedelta(minutes=1))
```

**Назначение**: Запускает окружение на заданное количество минут.

**Параметры**:

-   `minutes` (int): Количество минут для запуска окружения.

**Как работает функция**:

1.  Вызывает метод `run` с параметрами `steps=minutes` и `timedelta_per_step=timedelta(minutes=1)`.

```ascii
Начало --> Вызов run(steps=minutes, timedelta_per_step=timedelta(minutes=1)) --> Конец
```

**Примеры**:

```python
# Пример запуска окружения на 60 минут
world = TinyWorld(name='MyWorld')
world.run_minutes(minutes=60)
```

### `skip_minutes`

```python
def skip_minutes(self, minutes: int):
    """
    Skips a given number of minutes in the environment.

    Args:
        minutes (int): The number of minutes to skip.
    """
    self.skip(steps=minutes, timedelta_per_step=timedelta(minutes=1))
```

**Назначение**: Пропускает заданное количество минут в окружении.

**Параметры**:

-   `minutes` (int): Количество минут для пропуска.

**Как работает функция**:

1.  Вызывает метод `skip` с параметрами `steps=minutes` и `timedelta_per_step=timedelta(minutes=1)`.

```ascii
Начало --> Вызов skip(steps=minutes, timedelta_per_step=timedelta(minutes=1)) --> Конец
```

**Примеры**:

```python
# Пример пропуска 30 минут
world = TinyWorld(name='MyWorld')
world.skip_minutes(minutes=30)
```

### `run_hours`

```python
def run_hours(self, hours: int):
    """
    Runs the environment for a given number of hours.

    Args:
        hours (int): The number of hours to run the environment for.
    """
    self.run(steps=hours, timedelta_per_step=timedelta(hours=1))
```

**Назначение**: Запускает окружение на заданное количество часов.

**Параметры**:

-   `hours` (int): Количество часов для запуска окружения.

**Как работает функция**:

1.  Вызывает метод `run` с параметрами `steps=hours` и `timedelta_per_step=timedelta(hours=1)`.

```ascii
Начало --> Вызов run(steps=hours, timedelta_per_step=timedelta(hours=1)) --> Конец
```

**Примеры**:

```python
# Пример запуска окружения на 24 часа
world = TinyWorld(name='MyWorld')
world.run_hours(hours=24)
```

### `skip_hours`

```python
def skip_hours(self, hours: int):
    """
    Skips a given number of hours in the environment.

    Args:
        hours (int): The number of hours to skip.
    """
    self.skip(steps=hours, timedelta_per_step=timedelta(hours=1))
```

**Назначение**: Пропускает заданное количество часов в окружении.

**Параметры**:

-   `hours` (int): Количество часов для пропуска.

**Как работает функция**:

1.  Вызывает метод `skip` с параметрами `steps=hours` и `timedelta_per_step=timedelta(hours=1)`.

```ascii
Начало --> Вызов skip(steps=hours, timedelta_per_step=timedelta(hours=1)) --> Конец
```

**Примеры**:

```python
# Пример пропуска 12 часов
world = TinyWorld(name='MyWorld')
world.skip_hours(hours=12)
```

### `run_days`

```python
def run_days(self, days: int):
    """
    Runs the environment for a given number of days.

    Args:
        days (int): The number of days to run the environment for.
    """
    self.run(steps=days, timedelta_per_step=timedelta(days=1))
```

**Назначение**: Запускает окружение на заданное количество дней.

**Параметры**:

-   `days` (int): Количество дней для запуска окружения.

**Как работает функция**:

1.  Вызывает метод `run` с параметрами `steps=days` и `timedelta_per_step=timedelta(days=1)`.

```ascii
Начало --> Вызов run(steps=days, timedelta_per_step=timedelta(days=1)) --> Конец
```

**Примеры**:

```python
# Пример запуска окружения на 7 дней
world = TinyWorld(name='MyWorld')
world.run_days(days=7)
```

### `skip_days`

```python
def skip_days(self, days: int):
    """
    Skips a given number of days in the environment.

    Args:
        days (int): The number of days to skip.
    """
    self.skip(steps=days, timedelta_per_step=timedelta(days=1))
```

**Назначение**: Пропускает заданное количество дней в окружении.

**Параметры**:

-   `days` (int): Количество дней для пропуска.

**Как работает функция**:

1.  Вызывает метод `skip` с параметрами `steps=days` и `timedelta_per_step=timedelta(days=1)`.

```ascii
Начало --> Вызов skip(steps=days, timedelta_per_step=timedelta(days=1)) --> Конец
```

**Примеры**:

```python
# Пример пропуска 3 дня
world = TinyWorld(name='MyWorld')
world.skip_days(days=3)
```

### `run_weeks`

```python
def run_weeks(self, weeks: int):
    """
    Runs the environment for a given number of weeks.

    Args:
        weeks (int): The number of weeks to run the environment for.
    """
    self.run(steps=weeks, timedelta_per_step=timedelta(weeks=1))
```

**Назначение**: Запускает окружение на заданное количество недель.

**Параметры**:

-   `weeks` (int): Количество недель для запуска окружения.

**Как работает функция**:

1.  Вызывает метод `run` с параметрами `steps=weeks` и `timedelta_per_step=timedelta(weeks=1)`.

```ascii
Начало --> Вызов run(steps=weeks, timedelta_per_step=timedelta(weeks=1)) --> Конец
```

**Примеры**:

```python
# Пример запуска окружения на 2 недели
world = TinyWorld(name='MyWorld')
world.run_weeks(weeks=2)
```

### `skip_weeks`

```python
def skip_weeks(self, weeks: int):
    """
    Skips a given number of weeks in the environment.

    Args:
        weeks (int): The number of weeks to skip.
    """
    self.skip(steps=weeks, timedelta_per_step=timedelta(weeks=1))
```

**Назначение**: Пропускает заданное количество недель в окружении.

**Параметры**:

-   `weeks` (int): Количество недель для пропуска.

**Как работает функция**:

1.  Вызывает метод `skip` с параметрами `steps=weeks` и `timedelta_per_step=timedelta(weeks=1)`.

```ascii
Начало --> Вызов skip(steps=weeks, timedelta_per_step=timedelta(weeks=1)) --> Конец
```

**Примеры**:

```python
# Пример пропуска 1 недели
world = TinyWorld(name='MyWorld')
world.skip_weeks(weeks=1)
```

### `run_months`

```python
def run_months(self, months: int):
    """
    Runs the environment for a given number of months.

    Args:
        months (int): The number of months to run the environment for.
    """
    self.run(steps=months, timedelta_per_step=timedelta(weeks=4))
```

**Назначение**: Запускает окружение на заданное количество месяцев.

**Параметры**:

-   `months` (int): Количество месяцев для запуска окружения.

**Как работает функция**:

1.  Вызывает метод `run` с параметрами `steps=months` и `timedelta_per_step=timedelta(weeks=4)`.

```ascii
Начало --> Вызов run(steps=months, timedelta_per_step=timedelta(weeks=4)) --> Конец
```

**Примеры**:

```python
# Пример запуска окружения на 6 месяцев
world = TinyWorld(name='MyWorld')
world.run_months(months=6)
```

### `skip_months`

```python
def skip_months(self, months: int):
    """
    Skips a given number of months in the environment.

    Args:
        months (int): The number of months to skip.
    """
    self.skip(steps=months, timedelta_per_step=timedelta(weeks=4))
```

**Назначение**: Пропускает заданное количество месяцев в окружении.

**Параметры**:

-   `months` (int): Количество месяцев для пропуска.

**Как работает функция**:

1.  Вызывает метод `skip` с параметрами `steps=months` и `timedelta_per_step=timedelta(weeks=4)`.

```ascii
Начало --> Вызов skip(steps=months, timedelta_per_step=timedelta(weeks=4)) --> Конец
```

**Примеры**:

```python
# Пример пропуска 3 месяца
world = TinyWorld(name='MyWorld')
world.skip_months(months=3)
```

### `run_years`

```python
def run_years(self, years: int):
    """
    Runs the environment for a given number of years.

    Args:
        years (int): The number of years to run the environment for.
    """
    self.run(steps=years, timedelta_per_step=timedelta(days=365))
```

**Назначение**: Запускает окружение на заданное количество лет.

**Параметры**:

-   `years` (int): Количество лет для запуска окружения.

**Как работает функция**:

1.  Вызывает метод `run` с параметрами `steps=years` и `timedelta_per_step=timedelta(days=365)`.

```ascii
Начало --> Вызов run(steps=years, timedelta_per_step=timedelta(days=365)) --> Конец
```

**Примеры**:

```python
# Пример запуска окружения на 1 год
world = TinyWorld(name='MyWorld')
world.run_years(years=1)
```

### `skip_years`

```python
def skip_years(self, years: int):
    """
    Skips a given number of years in the environment.

    Args:
        years (int): The number of years to skip.
    """
    self.skip(steps=years, timedelta_per_step=timedelta(days=365))
```

**Назначение**: Пропускает заданное количество лет в окружении.

**Параметры**:

-   `years` (int): Количество лет для пропуска.

**Как работает функция**:

1.  Вызывает метод `skip` с параметрами `steps=years` и `timedelta_per_step=timedelta(days=365)`.

```ascii
Начало --> Вызов skip(steps=years, timedelta_per_step=timedelta(days=365)) --> Конец
```

**Примеры**:

```python
# Пример пропуска 5 лет
world = TinyWorld(name='MyWorld')
world.skip_years(years=5)
```

### `add_agents`

```python
def add_agents(self, agents: list):
    """
    Adds a list of agents to the environment.

    Args:
        agents (list): A list of agents to add to the environment.
    """
    for agent in agents:
        self.add_agent(agent)
    
    return self # for chaining
```

**Назначение**: Добавляет список агентов в окружение.

**Параметры**:

-   `agents` (list): Список агентов для добавления в окружение.

**Возвращает**:

-   `self`: Объект `TinyWorld` для возможности chaining.

**Как работает функция**:

1.  Перебирает список `agents`.
2.  Для каждого агента в списке вызывает метод `add_agent`.
3.  Возвращает `self` для chaining.

```ascii
Начало --> Для каждого agent в agents:
    --> Вызов add_agent(agent)
Конец --> Возврат self
```

**Примеры**:

```python
# Пример добавления списка агентов в окружение
world = TinyWorld(name='MyWorld')
agent1 = TinyPerson(name='Agent1')
agent2 = TinyPerson(name='Agent2')
world.add_agents([agent1, agent2])
```

### `add_agent`

```python
def add_agent(self, agent: TinyPerson):
    """
    Adds an agent to the environment. The agent must have a unique name within the environment.

    Args:
        agent (TinyPerson): The agent to add to the environment.
    
    Raises:
        ValueError: If the agent name is not unique within the environment.
    """

    # check if the agent is not already in the environment
    if agent not in self.agents:
        logger.debug(f"Adding agent {agent.name} to the environment.")
        
        # Agent names must be unique in the environment. 
        # Check if the agent name is already there.
        if agent.name not in self.name_to_agent:
            agent.environment = self
            self.agents.append(agent)
            self.name_to_agent[agent.name] = agent
        else:
            raise ValueError(f"Agent names must be unique, but '{agent.name}' is already in the environment.")
    else:
        logger.warn(f"Agent {agent.name} is already in the environment.")
    
    return self # for chaining
```

**Назначение**: Добавляет агента в окружение. Имя агента должно быть уникальным в пределах окружения.

**Параметры**:

-   `agent` (TinyPerson): Агент для добавления в окружение.

**Возвращает**:

-   `self`: Объект `TinyWorld` для возможности chaining.

**Вызывает исключения**:

-   `ValueError`: Если имя агента не уникально в пределах окружения.

**Как работает функция**:

1.  Проверяет, есть ли уже агент в `self.agents`.
2.  Если агента нет в `self.agents`, проверяет имя агента в `self.name_to_agent`.
3.  Если имя агента уникально, устанавливает `agent.environment = self`, добавляет агента в `self.agents` и `self.name_to_agent`.
4.  Если имя агента не уникально, вызывает исключение `ValueError`.
5.  Если агент уже есть в `self.agents`, записывает предупреждение в лог.
6.  Возвращает `self` для chaining.

```ascii
Начало --> Проверка наличия агента в self.agents -->
    Если агента нет:
        --> Проверка имени агента в self.name_to