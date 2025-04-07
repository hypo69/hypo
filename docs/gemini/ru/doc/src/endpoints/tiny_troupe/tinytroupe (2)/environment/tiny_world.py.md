# Модуль `tiny_world.py`

## Обзор

Модуль определяет класс `TinyWorld`, который является базовым классом для моделирования окружения, в котором действуют агенты. Он предоставляет функциональность для управления агентами, выполнения шагов симуляции, обработки действий агентов и взаимодействия между агентами.

## Подробнее

Этот модуль играет центральную роль в создании симуляций, где агенты взаимодействуют друг с другом и с окружающей средой. Он позволяет моделировать различные сценарии и анализировать поведение агентов в этих сценариях. Класс `TinyWorld` предоставляет методы для добавления, удаления и управления агентами, а также для выполнения шагов симуляции и обработки действий агентов.

## Классы

### `TinyWorld`

**Описание**: Базовый класс для окружений.

**Принцип работы**: Класс `TinyWorld` представляет собой окружение, в котором находятся и действуют агенты. Он управляет временем, агентами и их взаимодействиями. Класс предоставляет методы для выполнения шагов симуляции, обработки действий агентов и взаимодействия между агентами.

**Атрибуты**:

- `all_environments` (dict): Словарь, содержащий все созданные окружения. Ключ - имя окружения, значение - экземпляр `TinyWorld`.
- `communication_display` (bool): Флаг, определяющий, следует ли отображать сообщения окружения.
- `name` (str): Имя окружения.
- `current_datetime` (datetime): Текущая дата и время в окружении.
- `broadcast_if_no_target` (bool): Флаг, определяющий, следует ли широковещательно рассылать действия, если цель действия не найдена.
- `simulation_id` (Any): Идентификатор симуляции, к которой принадлежит окружение.
- `agents` (list): Список агентов в окружении.
- `name_to_agent` (dict): Словарь, сопоставляющий имена агентов с их экземплярами.
- `_interventions` (list): Список интервенций, применяемых в окружении на каждом шаге симуляции.
- `_displayed_communications_buffer` (list): Буфер сообщений, отображенных на данный момент.
- `_target_display_communications_buffer` (list): Временный буфер для упрощения отображения сообщений.
- `_max_additional_targets_to_display` (int): Максимальное количество дополнительных целей для отображения в сообщении.
- `console` (Console): Объект консоли для вывода сообщений.

**Методы**:

- `__init__`: Инициализирует окружение.
- `_step`: Выполняет один шаг в окружении.
- `_advance_datetime`: Продвигает текущую дату и время в окружении на заданный интервал.
- `run`: Запускает окружение на заданное количество шагов.
- `skip`: Пропускает заданное количество шагов в окружении.
- `run_minutes`: Запускает окружение на заданное количество минут.
- `skip_minutes`: Пропускает заданное количество минут в окружении.
- `run_hours`: Запускает окружение на заданное количество часов.
- `skip_hours`: Пропускает заданное количество часов в окружении.
- `run_days`: Запускает окружение на заданное количество дней.
- `skip_days`: Пропускает заданное количество дней в окружении.
- `run_weeks`: Запускает окружение на заданное количество недель.
- `skip_weeks`: Пропускает заданное количество недель в окружении.
- `run_months`: Запускает окружение на заданное количество месяцев.
- `skip_months`: Пропускает заданное количество месяцев в окружении.
- `run_years`: Запускает окружение на заданное количество лет.
- `skip_years`: Пропускает заданное количество лет в окружении.
- `add_agents`: Добавляет список агентов в окружение.
- `add_agent`: Добавляет агента в окружение.
- `remove_agent`: Удаляет агента из окружения.
- `remove_all_agents`: Удаляет всех агентов из окружения.
- `get_agent_by_name`: Возвращает агента с указанным именем.
- `add_intervention`: Добавляет интервенцию в окружение.
- `_handle_actions`: Обрабатывает действия, выданные агентами.
- `_handle_reach_out`: Обрабатывает действие `REACH_OUT`.
- `_handle_talk`: Обрабатывает действие `TALK`.
- `broadcast`: Отправляет сообщение всем агентам в окружении.
- `broadcast_thought`: Отправляет мысль всем агентам в окружении.
- `broadcast_internal_goal`: Отправляет внутреннюю цель всем агентам в окружении.
- `broadcast_context_change`: Отправляет изменение контекста всем агентам в окружении.
- `make_everyone_accessible`: Делает всех агентов в окружении доступными друг для друга.
- `_display_step_communication`: Отображает сообщение о шаге симуляции.
- `_display_intervention_communication`: Отображает сообщение об интервенции.
- `_push_and_display_latest_communication`: Добавляет сообщение в буфер и отображает его.
- `pop_and_display_latest_communications`: Извлекает сообщения из буфера и отображает их.
- `_display`: Отображает сообщение в консоли.
- `clear_communications_buffer`: Очищает буфер сообщений.
- `__repr__`: Возвращает строковое представление объекта `TinyWorld`.
- `_pretty_step`: Форматирует сообщение о шаге симуляции.
- `_pretty_intervention`: Форматирует сообщение об интервенции.
- `pp_current_interactions`: Выводит текущие сообщения агентов в окружении в консоль.
- `pretty_current_interactions`: Возвращает отформатированную строку с текущими сообщениями агентов в этом окружении.
- `encode_complete_state`: Кодирует полное состояние окружения в словарь.
- `decode_complete_state`: Декодирует полное состояние окружения из словаря.
- `add_environment`: Добавляет окружение в список всех окружений.
- `set_simulation_for_free_environments`: Задает симуляцию для свободных окружений.
- `get_environment_by_name`: Возвращает окружение с указанным именем.
- `clear_environments`: Очищает список всех окружений.

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
```

**Назначение**: Выполняет один шаг в окружении.

**Параметры**:

- `timedelta_per_step` (timedelta, optional): Временной интервал для продвижения текущей даты и времени. По умолчанию `None`.

**Возвращает**:

- `dict`: Словарь, содержащий действия, выполненные агентами на этом шаге. Формат словаря: `{agent_name: [action_1, action_2, ...], ...}`.

**Как работает функция**:

1. Продвигает текущую дату и время в окружении на заданный интервал, если он указан.
2. Применяет интервенции, если они удовлетворяют условиям.
3. Даёт каждому агенту возможность совершить действие (`agent.act()`).
4. Обрабатывает действия, выполненные каждым агентом, с помощью `self._handle_actions()`.

```
Начало
 |
 | timedelta_per_step?
 |  Да: Продвинуть время
 |  Нет: Пропустить
 |
 | Применить интервенции
 |
 | Агенты действуют
 |
 | Обработка действий
 |
Конец
```

**Примеры**:

```python
# Пример вызова функции _step без указания timedelta_per_step
world = TinyWorld(name='TestWorld')
actions = world._step()
print(actions)  # Вывод: {} (если в мире нет агентов)

# Пример вызова функции _step с указанием timedelta_per_step
from datetime import timedelta
world = TinyWorld(name='TestWorld')
actions = world._step(timedelta_per_step=timedelta(minutes=10))
print(actions)  # Вывод: {} (если в мире нет агентов)
```

### `_advance_datetime`

```python
def _advance_datetime(self, timedelta):
    """
    Advances the current datetime of the environment by the specified timedelta.

    Args:
        timedelta (timedelta): The timedelta to advance the current datetime by.
    """
```

**Назначение**: Продвигает текущую дату и время в окружении на заданный интервал.

**Параметры**:

- `timedelta` (timedelta): Временной интервал для продвижения текущей даты и времени.

**Как работает функция**:

1. Если `timedelta` не равен `None`, добавляет его к `self.current_datetime`.
2. Если `timedelta` равен `None`, логирует информационное сообщение о том, что время не было продвинуто.

```
Начало
 |
 | timedelta?
 |  Да: Продвинуть время
 |  Нет: Логировать сообщение
 |
Конец
```

**Примеры**:

```python
# Пример вызова функции _advance_datetime с указанием timedelta
from datetime import timedelta
world = TinyWorld(name='TestWorld')
world._advance_datetime(timedelta(days=1))
print(world.current_datetime)  # Вывод: текущая дата + 1 день

# Пример вызова функции _advance_datetime без указания timedelta
world = TinyWorld(name='TestWorld')
world._advance_datetime(None)  # В консоль будет выведено сообщение о том, что время не было продвинуто
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
```

**Назначение**: Запускает окружение на заданное количество шагов.

**Параметры**:

- `steps` (int): Количество шагов для выполнения симуляции.
- `timedelta_per_step` (timedelta, optional): Временной интервал между шагами. По умолчанию `None`.
- `return_actions` (bool, optional): Флаг, определяющий, следует ли возвращать действия, выполненные агентами. По умолчанию `False`.

**Возвращает**:

- `list`: Список действий, выполненных агентами в течение времени, если `return_actions` равен `True`. Список имеет формат: `[{agent_name: [action_1, action_2, ...]}, {agent_name_2: [action_1, action_2, ...]}, ...]`

**Как работает функция**:

1. Выполняет цикл `steps` раз.
2. На каждом шаге логирует информацию о текущем шаге симуляции.
3. Отображает сообщение о шаге симуляции, если включен `TinyWorld.communication_display`.
4. Выполняет один шаг симуляции с помощью `self._step(timedelta_per_step=timedelta_per_step)`.
5. Если `return_actions` равен `True`, добавляет действия агентов в список `agents_actions_over_time`.
6. Возвращает список `agents_actions_over_time`, если `return_actions` равен `True`.

```
Начало
 |
 | Цикл steps раз
 |  |
 |  | Логировать информацию о шаге
 |  |
 |  | Отобразить сообщение о шаге
 |  |
 |  | Выполнить шаг симуляции
 |  |
 |  | return_actions?
 |  |  Да: Добавить действия в список
 |  |  Нет: Пропустить
 |
 | return_actions?
 |  Да: Вернуть список действий
 |  Нет: Завершить
 |
Конец
```

**Примеры**:

```python
# Пример вызова функции run без указания timedelta_per_step и return_actions
world = TinyWorld(name='TestWorld')
world.run(steps=10)

# Пример вызова функции run с указанием timedelta_per_step и return_actions
from datetime import timedelta
world = TinyWorld(name='TestWorld')
actions = world.run(steps=10, timedelta_per_step=timedelta(minutes=5), return_actions=True)
print(actions)  # Вывод: список действий, выполненных агентами
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
```

**Назначение**: Пропускает заданное количество шагов в окружении.

**Параметры**:

- `steps` (int): Количество шагов для пропуска.
- `timedelta_per_step` (timedelta, optional): Временной интервал между шагами. По умолчанию `None`.

**Как работает функция**:

1. Продвигает текущую дату и время в окружении на `steps * timedelta_per_step` с помощью `self._advance_datetime()`.

```
Начало
 |
 | Продвинуть время на steps * timedelta_per_step
 |
Конец
```

**Примеры**:

```python
# Пример вызова функции skip без указания timedelta_per_step
world = TinyWorld(name='TestWorld')
world.skip(steps=5)

# Пример вызова функции skip с указанием timedelta_per_step
from datetime import timedelta
world = TinyWorld(name='TestWorld')
world.skip(steps=5, timedelta_per_step=timedelta(hours=1))
```

### `run_minutes`

```python
def run_minutes(self, minutes: int):
    """
    Runs the environment for a given number of minutes.

    Args:
        minutes (int): The number of minutes to run the environment for.
    """
```

**Назначение**: Запускает окружение на заданное количество минут.

**Параметры**:

- `minutes` (int): Количество минут для выполнения симуляции.

**Как работает функция**:

1. Вызывает функцию `self.run()` с параметрами `steps=minutes` и `timedelta_per_step=timedelta(minutes=1)`.

**Примеры**:

```python
# Пример вызова функции run_minutes
world = TinyWorld(name='TestWorld')
world.run_minutes(minutes=30)
```

### `skip_minutes`

```python
def skip_minutes(self, minutes: int):
    """
    Skips a given number of minutes in the environment.

    Args:
        minutes (int): The number of minutes to skip.
    """
```

**Назначение**: Пропускает заданное количество минут в окружении.

**Параметры**:

- `minutes` (int): Количество минут для пропуска.

**Как работает функция**:

1. Вызывает функцию `self.skip()` с параметрами `steps=minutes` и `timedelta_per_step=timedelta(minutes=1)`.

**Примеры**:

```python
# Пример вызова функции skip_minutes
world = TinyWorld(name='TestWorld')
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
```

**Назначение**: Запускает окружение на заданное количество часов.

**Параметры**:

- `hours` (int): Количество часов для выполнения симуляции.

**Как работает функция**:

1. Вызывает функцию `self.run()` с параметрами `steps=hours` и `timedelta_per_step=timedelta(hours=1)`.

**Примеры**:

```python
# Пример вызова функции run_hours
world = TinyWorld(name='TestWorld')
world.run_hours(hours=5)
```

### `skip_hours`

```python
def skip_hours(self, hours: int):
    """
    Skips a given number of hours in the environment.

    Args:
        hours (int): The number of hours to skip.
    """
```

**Назначение**: Пропускает заданное количество часов в окружении.

**Параметры**:

- `hours` (int): Количество часов для пропуска.

**Как работает функция**:

1. Вызывает функцию `self.skip()` с параметрами `steps=hours` и `timedelta_per_step=timedelta(hours=1)`.

**Примеры**:

```python
# Пример вызова функции skip_hours
world = TinyWorld(name='TestWorld')
world.skip_hours(hours=5)
```

### `run_days`

```python
def run_days(self, days: int):
    """
    Runs the environment for a given number of days.

    Args:
        days (int): The number of days to run the environment for.
    """
```

**Назначение**: Запускает окружение на заданное количество дней.

**Параметры**:

- `days` (int): Количество дней для выполнения симуляции.

**Как работает функция**:

1. Вызывает функцию `self.run()` с параметрами `steps=days` и `timedelta_per_step=timedelta(days=1)`.

**Примеры**:

```python
# Пример вызова функции run_days
world = TinyWorld(name='TestWorld')
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
```

**Назначение**: Пропускает заданное количество дней в окружении.

**Параметры**:

- `days` (int): Количество дней для пропуска.

**Как работает функция**:

1. Вызывает функцию `self.skip()` с параметрами `steps=days` и `timedelta_per_step=timedelta(days=1)`.

**Примеры**:

```python
# Пример вызова функции skip_days
world = TinyWorld(name='TestWorld')
world.skip_days(days=7)
```

### `run_weeks`

```python
def run_weeks(self, weeks: int):
    """
    Runs the environment for a given number of weeks.

    Args:
        weeks (int): The number of weeks to run the environment for.
    """
```

**Назначение**: Запускает окружение на заданное количество недель.

**Параметры**:

- `weeks` (int): Количество недель для выполнения симуляции.

**Как работает функция**:

1. Вызывает функцию `self.run()` с параметрами `steps=weeks` и `timedelta_per_step=timedelta(weeks=1)`.

**Примеры**:

```python
# Пример вызова функции run_weeks
world = TinyWorld(name='TestWorld')
world.run_weeks(weeks=4)
```

### `skip_weeks`

```python
def skip_weeks(self, weeks: int):
    """
    Skips a given number of weeks in the environment.

    Args:
        weeks (int): The number of weeks to skip.
    """
```

**Назначение**: Пропускает заданное количество недель в окружении.

**Параметры**:

- `weeks` (int): Количество недель для пропуска.

**Как работает функция**:

1. Вызывает функцию `self.skip()` с параметрами `steps=weeks` и `timedelta_per_step=timedelta(weeks=1)`.

**Примеры**:

```python
# Пример вызова функции skip_weeks
world = TinyWorld(name='TestWorld')
world.skip_weeks(weeks=4)
```

### `run_months`

```python
def run_months(self, months: int):
    """
    Runs the environment for a given number of months.

    Args:
        months (int): The number of months to run the environment for.
    """
```

**Назначение**: Запускает окружение на заданное количество месяцев.

**Параметры**:

- `months` (int): Количество месяцев для выполнения симуляции.

**Как работает функция**:

1. Вызывает функцию `self.run()` с параметрами `steps=months` и `timedelta_per_step=timedelta(weeks=4)`.

**Примеры**:

```python
# Пример вызова функции run_months
world = TinyWorld(name='TestWorld')
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
```

**Назначение**: Пропускает заданное количество месяцев в окружении.

**Параметры**:

- `months` (int): Количество месяцев для пропуска.

**Как работает функция**:

1. Вызывает функцию `self.skip()` с параметрами `steps=months` и `timedelta_per_step=timedelta(weeks=4)`.

**Примеры**:

```python
# Пример вызова функции skip_months
world = TinyWorld(name='TestWorld')
world.skip_months(months=6)
```

### `run_years`

```python
def run_years(self, years: int):
    """
    Runs the environment for a given number of years.

    Args:
        years (int): The number of years to run the environment for.
    """
```

**Назначение**: Запускает окружение на заданное количество лет.

**Параметры**:

- `years` (int): Количество лет для выполнения симуляции.

**Как работает функция**:

1. Вызывает функцию `self.run()` с параметрами `steps=years` и `timedelta_per_step=timedelta(days=365)`.

**Примеры**:

```python
# Пример вызова функции run_years
world = TinyWorld(name='TestWorld')
world.run_years(years=2)
```

### `skip_years`

```python
def skip_years(self, years: int):
    """
    Skips a given number of years in the environment.

    Args:
        years (int): The number of years to skip.
    """
```

**Назначение**: Пропускает заданное количество лет в окружении.

**Параметры**:

- `years` (int): Количество лет для пропуска.

**Как работает функция**:

1. Вызывает функцию `self.skip()` с параметрами `steps=years` и `timedelta_per_step=timedelta(days=365)`.

**Примеры**:

```python
# Пример вызова функции skip_years
world = TinyWorld(name='TestWorld')
world.skip_years(years=2)
```

### `add_agents`

```python
def add_agents(self, agents: list):
    """
    Adds a list of agents to the environment.

    Args:
        agents (list): A list of agents to add to the environment.
    """
```

**Назначение**: Добавляет список агентов в окружение.

**Параметры**:

- `agents` (list): Список агентов для добавления в окружение.

**Возвращает**:

- `self`: Возвращает текущий экземпляр `TinyWorld` для возможности chaining.

**Как работает функция**:

1. Перебирает список `agents`.
2. Для каждого агента вызывает функцию `self.add_agent(agent)`.
3. Возвращает `self`.

```
Начало
 |
 | Цикл по агентам в agents
 |  |
 |  | Добавить агента в окружение (self.add_agent(agent))
 |
 | Вернуть self
 |
Конец
```

**Примеры**:

```python
# Пример вызова функции add_agents
agent1 = TinyPerson(name='Agent1')
agent2 = TinyPerson(name='Agent2')
world = TinyWorld(name='TestWorld')
world.add_agents([agent1, agent2])
print(len(world.agents))  # Вывод: 2
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
```

**Назначение**: Добавляет агента в окружение.

**Параметры**:

- `agent` (TinyPerson): Агент для добавления в окружение.

**Вызывает исключения**:

- `ValueError`: Если имя агента не является уникальным в окружении.

**Возвращает**:

- `self`: Возвращает текущий экземпляр `TinyWorld` для возможности chaining.

**Как работает функция**:

1. Проверяет, что агента еще нет в списке агентов окружения.
2. Проверяет, что имя агента уникально в окружении.
3. Если все проверки пройдены, добавляет агента в список `self.agents`, сопоставляет имя агента с его экземпляром в `self.name_to_agent` и устанавливает `agent.environment = self`.
4. Если имя агента не уникально, выбрасывает исключение `ValueError`.
5. Возвращает `self`.

```
Начало
 |
 | Агент уже в окружении?
 |  Да: Логировать предупреждение, Вернуть self
 |  Нет: Продолжить
 |
 | Имя агента уникально?
 |  Да: Добавить агента в окружение
 |  Нет: Выбросить ValueError
 |
 | Вернуть self
 |
Конец
```

**Примеры**:

```python
# Пример вызова функции add_agent
agent = TinyPerson(name='Agent1')
world = TinyWorld(name='TestWorld')
world.add_agent(agent)
print(len(world.agents))  # Вывод: 1

# Пример вызова функции add_agent с неуникальным именем
agent1 = TinyPerson(name='Agent1')
agent2 = TinyPerson(name='Agent1')
world = TinyWorld(name='TestWorld')
world.add_agent(agent1)
try:
    world.add_agent(agent2)
except ValueError as ex:
    print(f"Ошибка: {ex}")  # Вывод: Ошибка: Agent names must be unique, but 'Agent1' is already in the environment.
```

### `remove_agent`

```python
def remove_agent(self, agent: TinyPerson):
    """
    Removes an agent from the environment.

    Args:
        agent (TinyPerson): The agent to remove from the environment.
    """
```

**Назначение**: Удаляет агента из окружения.

**Параметры**:

- `agent` (TinyPerson): Агент для удаления из окружения.

**Возвращает**:

- `self`: Возвращает текущий экземпляр `TinyWorld` для возможности chaining.

**Как работает функция**:

1. Логирует информацию об удалении агента.
2. Удаляет агента из списка `self.agents`.
3. Удаляет агента из словаря `self.name_to_agent`.
4. Возвращает `self`.

```
Начало
 |
 | Логировать информацию об удалении агента
 |
 | Удалить агента из списка agents
 |
 | Удалить агента из словаря name_to_agent
 |
 | Вернуть self
 |
Конец
```

**Примеры**:

```python
# Пример вызова функции remove_agent
agent = TinyPerson(name='Agent1')
world = TinyWorld(name='TestWorld')
world.add_agent(agent)
print(len(world.agents))  # Вывод: 1
world.remove_agent(agent)
print(len(world.agents))  # Вывод: 0
```

### `remove_all_agents`

```python
def remove_all_agents(self):
    """
    Removes all agents from the environment.
    """
```

**Назначение**: Удаляет всех агентов из окружения.

**Возвращает**:

- `self`: Возвращает текущий экземпляр `TinyWorld` для возможности chaining.

**Как работает функция**:

1. Логирует информацию об удалении всех агентов.
2. Очищает список `self.agents`.
3. Очищает словарь `self.name_to_agent`.
4. Возвращает `self`.

```
Начало
 |
 | Логировать информацию об удалении всех агентов
 |
 | Очистить список agents
 |
 | Очистить словарь name_to_agent
 |
 | Вернуть self
 |
Конец
```

**Примеры**:

```python
# Пример вызова функции remove_all_agents
agent1 = TinyPerson(name='Agent1')
agent2 = TinyPerson(name='Agent2')
world = TinyWorld(name='TestWorld')
world.add_agents([agent1, agent2])
print(len(world.agents))  # Вывод: 2
world.remove_all_agents()
print(len(world.agents))  # Вывод: 0
```

### `get_agent_by_name`

```python
def get_agent_by_name(self, name: str) -> TinyPerson:
    """
    Returns the agent with the specified name. If no agent with that name exists in the environment, 
    returns None.

    Args:
        name (str): The name of the agent to return.

    Returns:
        TinyPerson: The agent with the specified name.
    """
```

**Назначение**: Возвращает агента с указанным именем.

**Параметры**:

- `name` (str): Имя агента для поиска.

**Возвращает**:

- `TinyPerson`: Агент с указанным именем, или `None`, если агент не найден.

**Как работает функция**:

1. Проверяет, существует ли агент с указанным именем в словаре `self.name_to_agent`.
2. Если агент существует, возвращает его.
3. Если агент не существует, возвращает `None`.

```
Начало
 |
 | Агент с именем name существует в name_to_agent?
 |  Да: Вернуть агента
 |  Нет: Вернуть None
 |
Конец
```

**Примеры**:

```python
# Пример вызова функции get_agent_by_name
agent = TinyPerson(name='Agent1')
world = TinyWorld(name='TestWorld')
world.add_agent(agent)
found_agent = world.get_agent_by_name('Agent1')
print(found_agent)  # Вывод: <tinytroupe.agent.TinyPerson object at ...>
not_found_agent = world.get_agent_by_name('Agent2')
print(not_found_agent)  # Вывод: None
```

### `add_intervention`

```python
def add_intervention(self, intervention):
    """
    Adds an intervention to the environment.

    Args:
        intervention: The intervention to add to the environment.
    """
```

**Назначение**: Добавляет интервенцию в окружение.

**Параметры**:

- `intervention`: Интервенция для добавления в окружение.

**Как работает функция**:

1. Добавляет интервенцию в список `self._interventions`.

```
Начало
 |
 | Добавить intervention в список _interventions
 |
Конец
```

**Примеры**:

```python
# Пример вызова функции add_intervention
class Intervention:
    pass
intervention = Intervention()
world = TinyWorld(name='TestWorld')
world.add_intervention(intervention)
print(len(world._interventions))  # Вывод: 1
```

### `_handle_actions`

```python
@transactional
def _handle_actions(self, source: TinyPerson, actions: list):
    """ 
    Handles the actions issued by the agents.

    Args:
        source (TinyPerson): The agent that issued the actions.
        actions (list): A list of actions issued by the agents. Each action is actually a
          JSON specification.
        
    """
```

**Назначение**: Обрабатывает действия, выданные агентами.

**Параметры**:

- `source` (TinyPerson): Агент, выдавший действия.
- `actions` (list): Список действий, выданных агентами. Каждое действие является JSON-спецификацией.

**Как работает функция**:

1. Перебирает список действий `actions`.
2. Для каждого действия определяет тип действия (`action_type`) и его содержимое (`content`) и цель (`target`).
3. Логирует информацию об обрабатываемом действии.
4. В зависимости от типа действия вызывает соответствующий обработчик:
   - Если `action_type == "REACH_OUT"`, вызывает `self._handle_reach_out(source, content, target)`.
   - Если `action_type == "TALK"`, вызывает `self._handle_talk(source, content, target)`.

```
Начало
 |
 | Цикл по действиям в actions
 |  |
 |  | Определить тип действия, содержимое и цель
 |  |
 |  | Логировать информацию о действии
 |  |
 |  | Тип действия?
 |  |  REACH_OUT: Обработать REACH_OUT
 |  |  TALK: Обработать TALK
 |  |  Другое: Пропустить
 |
Конец
```

**Примеры**:

```python
# Пример вызова функции _handle_actions
class MockAgent(TinyPerson):
    def __init__(self