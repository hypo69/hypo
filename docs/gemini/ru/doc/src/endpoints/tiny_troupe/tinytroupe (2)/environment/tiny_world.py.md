# Модуль `tiny_world`

## Обзор

Модуль `tiny_world.py` предоставляет базовый класс `TinyWorld` для моделирования виртуальных сред, в которых взаимодействуют агенты (`TinyPerson`). Он включает в себя управление агентами, обработку действий, взаимодействие между агентами и сохранение/восстановление состояния среды. Модуль также содержит методы для запуска симуляций на определенное количество шагов или временных интервалов.

## Подробней

Этот модуль является центральным элементом для создания симуляций, в которых агенты взаимодействуют друг с другом и с окружающей средой. Он предоставляет инструменты для управления временем, добавления и удаления агентов, обработки действий агентов и трансляции сообщений между ними. Класс `TinyWorld` служит основой для создания более сложных и специализированных сред.

## Классы

### `TinyWorld`

**Описание**: Базовый класс для моделирования виртуальных сред.

**Принцип работы**:
Класс `TinyWorld` управляет агентами, временем и взаимодействиями в виртуальной среде. Он позволяет добавлять агентов, запускать симуляции, обрабатывать действия агентов и транслировать сообщения между ними. Состояние среды можно сохранять и восстанавливать.

**Аттрибуты**:

- `name` (str): Имя среды.
- `current_datetime` (datetime): Текущая дата и время среды.
- `broadcast_if_no_target` (bool): Если `True`, действия транслируются, если цель действия не найдена.
- `simulation_id` (None): Идентификатор симуляции, к которой принадлежит среда.
- `agents` (list): Список агентов в среде.
- `name_to_agent` (dict): Словарь, сопоставляющий имена агентов с объектами агентов.
- `_interventions` (list): Список интервенций, применяемых в среде на каждом шаге симуляции.
- `_displayed_communications_buffer` (list): Буфер для хранения отображаемых коммуникаций.
- `_target_display_communications_buffer` (list): Временный буфер для целей коммуникаций.
- `_max_additional_targets_to_display` (int): Максимальное количество дополнительных целей для отображения в коммуникации.
- `console` (Console): Объект консоли для отображения информации.
- `all_environments` (dict): Словарь всех созданных сред.
- `communication_display` (bool): Флаг, определяющий, отображать ли коммуникации среды.

**Методы**:

- `__init__(self, name: str="A TinyWorld", agents=[], initial_datetime=datetime.now(), interventions=[], broadcast_if_no_target=True, max_additional_targets_to_display=3)`: Инициализирует среду.
- `_step(self, timedelta_per_step=None)`: Выполняет один шаг в среде.
- `_advance_datetime(self, timedelta)`: Продвигает текущую дату и время среды на указанный интервал.
- `run(self, steps: int, timedelta_per_step=None, return_actions=False)`: Запускает среду на заданное количество шагов.
- `skip(self, steps: int, timedelta_per_step=None)`: Пропускает заданное количество шагов в среде.
- `run_minutes(self, minutes: int)`: Запускает среду на заданное количество минут.
- `skip_minutes(self, minutes: int)`: Пропускает заданное количество минут в среде.
- `run_hours(self, hours: int)`: Запускает среду на заданное количество часов.
- `skip_hours(self, hours: int)`: Пропускает заданное количество часов в среде.
- `run_days(self, days: int)`: Запускает среду на заданное количество дней.
- `skip_days(self, days: int)`: Пропускает заданное количество дней в среде.
- `run_weeks(self, weeks: int)`: Запускает среду на заданное количество недель.
- `skip_weeks(self, weeks: int)`: Пропускает заданное количество недель в среде.
- `run_months(self, months: int)`: Запускает среду на заданное количество месяцев.
- `skip_months(self, months: int)`: Пропускает заданное количество месяцев в среде.
- `run_years(self, years: int)`: Запускает среду на заданное количество лет.
- `skip_years(self, years: int)`: Пропускает заданное количество лет в среде.
- `add_agents(self, agents: list)`: Добавляет список агентов в среду.
- `add_agent(self, agent: TinyPerson)`: Добавляет агента в среду.
- `remove_agent(self, agent: TinyPerson)`: Удаляет агента из среды.
- `remove_all_agents(self)`: Удаляет всех агентов из среды.
- `get_agent_by_name(self, name: str) -> TinyPerson`: Возвращает агента с указанным именем.
- `add_intervention(self, intervention)`: Добавляет интервенцию в среду.
- `_handle_actions(self, source: TinyPerson, actions: list)`: Обрабатывает действия, совершенные агентами.
- `_handle_reach_out(self, source_agent: TinyPerson, content: str, target: str)`: Обрабатывает действие `REACH_OUT`.
- `_handle_talk(self, source_agent: TinyPerson, content: str, target: str)`: Обрабатывает действие `TALK`.
- `broadcast(self, speech: str, source: AgentOrWorld=None)`: Отправляет сообщение всем агентам в среде.
- `broadcast_thought(self, thought: str, source: AgentOrWorld=None)`: Транслирует мысль всем агентам в среде.
- `broadcast_internal_goal(self, internal_goal: str)`: Транслирует внутреннюю цель всем агентам в среде.
- `broadcast_context_change(self, context: list)`: Транслирует изменение контекста всем агентам в среде.
- `make_everyone_accessible(self)`: Делает всех агентов в среде доступными друг для друга.
- `_display_step_communication(self, cur_step, total_steps, timedelta_per_step=None)`: Отображает информацию о текущем шаге.
- `_display_intervention_communication(self, intervention)`: Отображает информацию об интервенции.
- `_push_and_display_latest_communication(self, communication)`: Добавляет коммуникацию в буфер и отображает ее.
- `pop_and_display_latest_communications(self)`: Извлекает коммуникации из буфера и отображает их.
- `_display(self, communication: dict)`: Отображает коммуникацию.
- `clear_communications_buffer(self)`: Очищает буфер коммуникаций.
- `__repr__(self)`: Возвращает строковое представление объекта `TinyWorld`.
- `_pretty_step(self, cur_step, total_steps, timedelta_per_step=None)`: Форматирует информацию о шаге для отображения.
- `_pretty_intervention(self, intervention)`: Форматирует информацию об интервенции для отображения.
- `pp_current_interactions(self, simplified=True, skip_system=True)`: Выводит на экран текущие взаимодействия агентов в удобочитаемом формате.
- `pretty_current_interactions(self, simplified=True, skip_system=True, max_content_length=default["max_content_display_length"], first_n=None, last_n=None, include_omission_info: bool = True)`: Возвращает строку с текущими взаимодействиями агентов в удобочитаемом формате.
- `encode_complete_state(self) -> dict`: Кодирует полное состояние среды в словарь.
- `decode_complete_state(self, state: dict)`: Декодирует полное состояние среды из словаря.
- `add_environment(environment)`: Добавляет среду в список всех сред.
- `set_simulation_for_free_environments(simulation)`: Устанавливает симуляцию для свободных сред.
- `get_environment_by_name(name: str)`: Возвращает среду с указанным именем.
- `clear_environments()`: Очищает список всех сред.

## Функции

### `_step`

```python
@transactional
def _step(self, timedelta_per_step=None) -> dict:
    """
    Выполняет один шаг в среде. Эта реализация по умолчанию просто заставляет всех агентов в среде действовать и должным образом обрабатывает resulting actions. Подклассы могут переопределить этот метод для реализации различных политик.

    Args:
        timedelta_per_step (timedelta, optional): Временной интервал для каждого шага. По умолчанию `None`.

    Returns:
        dict: Словарь действий агентов. Формат: `{agent_name: [action_1, action_2, ...], ...}`.
    """
    ...
```

**Как работает функция**:

1. **Продвижение времени**: Если указан `timedelta_per_step`, текущее время в среде увеличивается на этот интервал.
2. **Применение интервенций**: Проверяется предусловие каждой интервенции. Если предусловие выполняется, применяется эффект интервенции. Информация об интервенции отображается, если включен режим отображения коммуникаций.
3. **Действия агентов**: Каждый агент в среде выполняет действие. Результаты действий сохраняются в словаре `agents_actions`.
4. **Обработка действий**: Вызывается метод `_handle_actions` для обработки действий, выполненных агентами.

**ASCII flowchart**:

```
Начало
|
V
[Продвижение времени]
|
V
[Применение интервенций]
|
V
[Действия агентов]
|
V
[Обработка действий]
|
V
Конец
```

**Примеры**:

```python
# Пример вызова _step без указания временного интервала
actions = world._step()

# Пример вызова _step с указанием временного интервала
actions = world._step(timedelta_per_step=timedelta(minutes=10))
```

### `_advance_datetime`

```python
def _advance_datetime(self, timedelta: timedelta):
    """
    Продвигает текущую дату и время среды на указанный интервал.

    Args:
        timedelta (timedelta): Временной интервал, на который нужно продвинуть текущую дату и время.
    """
    ...
```

**Как работает функция**:

1. **Проверка наличия интервала**: Проверяется, был ли передан аргумент `timedelta`.
2. **Продвижение времени**: Если `timedelta` не равен `None`, текущее время среды (`self.current_datetime`) увеличивается на значение `timedelta`. Если `timedelta` равен `None`, в лог записывается информационное сообщение о том, что время не было продвинуто.

**ASCII flowchart**:

```
Начало
|
V
[Проверка наличия интервала]
|
V
[Продвижение времени]
|
V
Конец
```

**Примеры**:

```python
# Пример вызова _advance_datetime с указанием временного интервала в 30 минут
world._advance_datetime(timedelta=timedelta(minutes=30))

# Пример вызова _advance_datetime без указания временного интервала
world._advance_datetime(timedelta=None)
```

### `run`

```python
@transactional
def run(self, steps: int, timedelta_per_step=None, return_actions=False) -> list | None:
    """
    Запускает среду на заданное количество шагов.

    Args:
        steps (int): Количество шагов для запуска среды.
        timedelta_per_step (timedelta, optional): Временной интервал между шагами. По умолчанию `None`.
        return_actions (bool, optional): Если `True`, возвращает действия, предпринятые агентами. По умолчанию `False`.

    Returns:
        list: Список действий, предпринятых агентами с течением времени, если `return_actions` имеет значение `True`. Список имеет следующий формат:
              `[{agent_name: [action_1, action_2, ...]}, {agent_name_2: [action_1, action_2, ...]}, ...]`
        None: Если `return_actions` имеет значение `False`.
    """
    ...
```

**Как работает функция**:

1. **Инициализация**: Создается пустой список `agents_actions_over_time` для хранения действий агентов на каждом шаге, если `return_actions` имеет значение `True`.
2. **Цикл по шагам**: Выполняется цикл `steps` раз.
3. **Отображение информации о шаге**: Если `TinyWorld.communication_display` имеет значение `True`, отображается информация о текущем шаге симуляции.
4. **Выполнение шага**: Вызывается метод `_step` для выполнения одного шага симуляции. Результаты действий агентов сохраняются в `agents_actions`.
5. **Сохранение действий**: Если `return_actions` имеет значение `True`, действия агентов добавляются в список `agents_actions_over_time`.
6. **Возврат результатов**: Если `return_actions` имеет значение `True`, возвращается список `agents_actions_over_time`.

**ASCII flowchart**:

```
Начало
|
V
[Инициализация]
|
V
[Цикл по шагам]
|
V
[Отображение информации о шаге]
|
V
[Выполнение шага]
|
V
[Сохранение действий]
|
V
[Возврат результатов]
|
V
Конец
```

**Примеры**:

```python
# Пример запуска среды на 10 шагов без указания временного интервала и без возврата действий
world.run(steps=10)

# Пример запуска среды на 5 шагов с временным интервалом в 1 час и с возвратом действий
actions = world.run(steps=5, timedelta_per_step=timedelta(hours=1), return_actions=True)
```

### `skip`

```python
@transactional
def skip(self, steps: int, timedelta_per_step=None):
    """
    Пропускает заданное количество шагов в среде. То есть время должно пройти, но никакие действия не будут предприняты агентами или какой-либо другой сущностью в среде.

    Args:
        steps (int): Количество шагов для пропуска.
        timedelta_per_step (timedelta, optional): Временной интервал между шагами. По умолчанию `None`.
    """
    ...
```

**Как работает функция**:

1. **Продвижение времени**: Вызывается метод `_advance_datetime` для продвижения времени на `steps * timedelta_per_step`.

**ASCII flowchart**:

```
Начало
|
V
[Продвижение времени]
|
V
Конец
```

**Примеры**:

```python
# Пример пропуска 10 шагов без указания временного интервала
world.skip(steps=10)

# Пример пропуска 5 шагов с временным интервалом в 1 час
world.skip(steps=5, timedelta_per_step=timedelta(hours=1))
```

### `run_minutes`

```python
def run_minutes(self, minutes: int):
    """
    Запускает среду на заданное количество минут.

    Args:
        minutes (int): Количество минут для запуска среды.
    """
    ...
```

**Как работает функция**:

1. **Запуск среды**: Вызывается метод `run` с параметрами `steps=minutes` и `timedelta_per_step=timedelta(minutes=1)`.

**ASCII flowchart**:

```
Начало
|
V
[Запуск среды]
|
V
Конец
```

**Примеры**:

```python
# Пример запуска среды на 60 минут
world.run_minutes(minutes=60)
```

### `skip_minutes`

```python
def skip_minutes(self, minutes: int):
    """
    Пропускает заданное количество минут в среде.

    Args:
        minutes (int): Количество минут для пропуска.
    """
    ...
```

**Как работает функция**:

1. **Пропуск времени**: Вызывается метод `skip` с параметрами `steps=minutes` и `timedelta_per_step=timedelta(minutes=1)`.

**ASCII flowchart**:

```
Начало
|
V
[Пропуск времени]
|
V
Конец
```

**Примеры**:

```python
# Пример пропуска 60 минут
world.skip_minutes(minutes=60)
```

### `run_hours`

```python
def run_hours(self, hours: int):
    """
    Запускает среду на заданное количество часов.

    Args:
        hours (int): Количество часов для запуска среды.
    """
    ...
```

**Как работает функция**:

1. **Запуск среды**: Вызывается метод `run` с параметрами `steps=hours` и `timedelta_per_step=timedelta(hours=1)`.

**ASCII flowchart**:

```
Начало
|
V
[Запуск среды]
|
V
Конец
```

**Примеры**:

```python
# Пример запуска среды на 24 часа
world.run_hours(hours=24)
```

### `skip_hours`

```python
def skip_hours(self, hours: int):
    """
    Пропускает заданное количество часов в среде.

    Args:
        hours (int): Количество часов для пропуска.
    """
    ...
```

**Как работает функция**:

1. **Пропуск времени**: Вызывается метод `skip` с параметрами `steps=hours` и `timedelta_per_step=timedelta(hours=1)`.

**ASCII flowchart**:

```
Начало
|
V
[Пропуск времени]
|
V
Конец
```

**Примеры**:

```python
# Пример пропуска 24 часов
world.skip_hours(hours=24)
```

### `run_days`

```python
def run_days(self, days: int):
    """
    Запускает среду на заданное количество дней.

    Args:
        days (int): Количество дней для запуска среды.
    """
    ...
```

**Как работает функция**:

1. **Запуск среды**: Вызывается метод `run` с параметрами `steps=days` и `timedelta_per_step=timedelta(days=1)`.

**ASCII flowchart**:

```
Начало
|
V
[Запуск среды]
|
V
Конец
```

**Примеры**:

```python
# Пример запуска среды на 7 дней
world.run_days(days=7)
```

### `skip_days`

```python
def skip_days(self, days: int):
    """
    Пропускает заданное количество дней в среде.

    Args:
        days (int): Количество дней для пропуска.
    """
    ...
```

**Как работает функция**:

1. **Пропуск времени**: Вызывается метод `skip` с параметрами `steps=days` и `timedelta_per_step=timedelta(days=1)`.

**ASCII flowchart**:

```
Начало
|
V
[Пропуск времени]
|
V
Конец
```

**Примеры**:

```python
# Пример пропуска 7 дней
world.skip_days(days=7)
```

### `run_weeks`

```python
def run_weeks(self, weeks: int):
    """
    Запускает среду на заданное количество недель.

    Args:
        weeks (int): Количество недель для запуска среды.
    """
    ...
```

**Как работает функция**:

1. **Запуск среды**: Вызывается метод `run` с параметрами `steps=weeks` и `timedelta_per_step=timedelta(weeks=1)`.

**ASCII flowchart**:

```
Начало
|
V
[Запуск среды]
|
V
Конец
```

**Примеры**:

```python
# Пример запуска среды на 4 недели
world.run_weeks(weeks=4)
```

### `skip_weeks`

```python
def skip_weeks(self, weeks: int):
    """
    Пропускает заданное количество недель в среде.

    Args:
        weeks (int): Количество недель для пропуска.
    """
    ...
```

**Как работает функция**:

1. **Пропуск времени**: Вызывается метод `skip` с параметрами `steps=weeks` и `timedelta_per_step=timedelta(weeks=1)`.

**ASCII flowchart**:

```
Начало
|
V
[Пропуск времени]
|
V
Конец
```

**Примеры**:

```python
# Пример пропуска 4 недель
world.skip_weeks(weeks=4)
```

### `run_months`

```python
def run_months(self, months: int):
    """
    Запускает среду на заданное количество месяцев.

    Args:
        months (int): Количество месяцев для запуска среды.
    """
    ...
```

**Как работает функция**:

1. **Запуск среды**: Вызывается метод `run` с параметрами `steps=months` и `timedelta_per_step=timedelta(weeks=4)`.

**ASCII flowchart**:

```
Начало
|
V
[Запуск среды]
|
V
Конец
```

**Примеры**:

```python
# Пример запуска среды на 12 месяцев
world.run_months(months=12)
```

### `skip_months`

```python
def skip_months(self, months: int):
    """
    Пропускает заданное количество месяцев в среде.

    Args:
        months (int): Количество месяцев для пропуска.
    """
    ...
```

**Как работает функция**:

1. **Пропуск времени**: Вызывается метод `skip` с параметрами `steps=months` и `timedelta_per_step=timedelta(weeks=4)`.

**ASCII flowchart**:

```
Начало
|
V
[Пропуск времени]
|
V
Конец
```

**Примеры**:

```python
# Пример пропуска 12 месяцев
world.skip_months(months=12)
```

### `run_years`

```python
def run_years(self, years: int):
    """
    Запускает среду на заданное количество лет.

    Args:
        years (int): Количество лет для запуска среды.
    """
    ...
```

**Как работает функция**:

1. **Запуск среды**: Вызывается метод `run` с параметрами `steps=years` и `timedelta_per_step=timedelta(days=365)`.

**ASCII flowchart**:

```
Начало
|
V
[Запуск среды]
|
V
Конец
```

**Примеры**:

```python
# Пример запуска среды на 10 лет
world.run_years(years=10)
```

### `skip_years`

```python
def skip_years(self, years: int):
    """
    Пропускает заданное количество лет в среде.

    Args:
        years (int): Количество лет для пропуска.
    """
    ...
```

**Как работает функция**:

1. **Пропуск времени**: Вызывается метод `skip` с параметрами `steps=years` и `timedelta_per_step=timedelta(days=365)`.

**ASCII flowchart**:

```
Начало
|
V
[Пропуск времени]
|
V
Конец
```

**Примеры**:

```python
# Пример пропуска 10 лет
world.skip_years(years=10)
```

### `add_agents`

```python
def add_agents(self, agents: list) -> "TinyWorld":
    """
    Добавляет список агентов в среду.

    Args:
        agents (list): Список агентов для добавления в среду.

    Returns:
        TinyWorld: Среда (self) для поддержки цепочки вызовов.
    """
    ...
```

**Как работает функция**:

1. **Перебор агентов**: Проходит по списку агентов, переданных в аргументе `agents`.
2. **Добавление агента**: Для каждого агента вызывается метод `add_agent` для добавления его в среду.
3. **Возврат среды**: Возвращает текущий объект среды (`self`) для обеспечения возможности chaining.

**ASCII flowchart**:

```
Начало
|
V
[Перебор агентов]
|
V
[Добавление агента]
|
V
Конец
```

**Примеры**:

```python
# Создание списка агентов
agents = [TinyPerson(name='Alice'), TinyPerson(name='Bob')]

# Добавление агентов в среду
world.add_agents(agents)
```

### `add_agent`

```python
def add_agent(self, agent: TinyPerson) -> "TinyWorld":
    """
    Добавляет агента в среду. Имя агента должно быть уникальным в пределах среды.

    Args:
        agent (TinyPerson): Агент для добавления в среду.

    Raises:
        ValueError: Если имя агента не является уникальным в пределах среды.

    Returns:
        TinyWorld: Среда (self) для поддержки цепочки вызовов.
    """
    ...
```

**Как работает функция**:

1. **Проверка наличия агента**: Проверяется, не находится ли уже агент в списке агентов среды (`self.agents`).
2. **Проверка уникальности имени**: Если агент еще не добавлен, проверяется, не существует ли уже агент с таким же именем в словаре `self.name_to_agent`.
3. **Добавление агента**: Если имя уникально, агенту присваивается ссылка на текущую среду (`agent.environment = self`), агент добавляется в список `self.agents` и в словарь `self.name_to_agent`.
4. **Обработка исключения**: Если имя агента не уникально, вызывается исключение `ValueError`.
5. **Возврат среды**: Возвращает текущий объект среды (`self`) для обеспечения возможности chaining.

**ASCII flowchart**:

```
Начало
|
V
[Проверка наличия агента]
|
V
[Проверка уникальности имени]
|
V
[Добавление агента]
|
V
Конец
```

**Примеры**:

```python
# Создание агента
agent = TinyPerson(name='Charlie')

# Добавление агента в среду
world.add_agent(agent)
```

### `remove_agent`

```python
def remove_agent(self, agent: TinyPerson) -> "TinyWorld":
    """
    Удаляет агента из среды.

    Args:
        agent (TinyPerson): Агент для удаления из среды.

    Returns:
        TinyWorld: Среда (self) для поддержки цепочки вызовов.
    """
    ...
```

**Как работает функция**:

1. **Удаление агента**: Удаляет агента из списка `self.agents` и из словаря `self.name_to_agent`.
2. **Возврат среды**: Возвращает текущий объект среды (`self`) для обеспечения возможности chaining.

**ASCII flowchart**:

```
Начало
|
V
[Удаление агента]
|
V
Конец
```

**Примеры**:

```python
# Создание агента
agent = TinyPerson(name='Charlie')

# Добавление агента в среду
world.add_agent(agent)

# Удаление агента из среды
world.remove_agent(agent)
```

### `remove_all_agents`

```python
def remove_all_agents(self) -> "TinyWorld":
    """
    Удаляет всех агентов из среды.

    Returns:
        TinyWorld: Среда (self) для поддержки цепочки вызовов.
    """
    ...
```

**Как работает функция**:

1. **Удаление всех агентов**: Очищает список `self.agents` и словарь `self.name_to_agent`.
2. **Возврат среды**: Возвращает текущий объект среды (`self`) для обеспечения возможности chaining.

**ASCII flowchart**:

```
Начало
|
V
[Удаление всех агентов]
|
V
Конец
```

**Примеры**:

```python
# Удаление всех агентов из среды
world.remove_all_agents()
```

### `get_agent_by_name`

```python
def get_agent_by_name(self, name: str) -> TinyPerson | None:
    """
    Возвращает агента с указанным именем. Если в среде не существует агента с таким именем, возвращает `None`.

    Args:
        name (str): Имя агента для возврата.

    Returns:
        TinyPerson | None: Агент с указанным именем или `None`, если агент не найден.
    """
    ...
```

**Как работает функция**:

1. **Поиск агента**: Проверяет, существует ли агент с указанным именем в словаре `self.name_to_agent`.
2. **Возврат агента**: Если агент найден, возвращает объект агента. Если агент не найден, возвращает `None`.

**ASCII flowchart**:

```
Начало
|
V
[Поиск агента]
|
V
[Возврат агента]
|
V
Конец
```

**Примеры**:

```python
# Получение агента по имени
agent = world.get_agent_by_name('Alice')

# Если агент не найден, agent будет равен None
if agent is None:
    print('Агент не найден')
```

### `add_intervention`

```python
def add_intervention(self, intervention):
    """
    Добавляет интервенцию в среду.

    Args:
        intervention: Интервенция для добавления в среду.
    """
    ...
```

**Как работает функция**:

1. **Добавление интервенции**: Добавляет переданную интервенцию в список `self._interventions`.

**ASCII flowchart**:

```
Начало
|
V
[Добавление интервенции]
|
V
Конец
```

**Примеры**:

```python
# Создание объекта интервенции (предположим, что класс Intervention уже определен)
intervention = Intervention(name='IncreaseFoodSupply', precondition=lambda: True, effect=lambda: print('Food supply increased'))

# Добавление интервенции в среду
world.add_intervention(intervention)
```

### `_handle_actions`

```python
@transactional
def _handle_actions(self, source: TinyPerson, actions: list):
    """
    Обрабатывает действия, совершенные агентами.

    Args:
        source (TinyPerson): Агент, совершивший действия.
        actions (list): Список действий, совершенных агентами. Каждое действие является спецификацией JSON.
    """
    ...
```

**Как работает функция**:

1. **Перебор действий**: Перебирает список действий (`actions`), совершенных агентом (`source`).
2. **Определение типа действия**: Для каждого действия определяет его тип (`action_type`) и содержимое (`content`), если оно есть.
3. **Обработка действия**: В зависимости от типа действия вызывается соответствующий обработчик:
   - Если `action_type` равен `'REACH_OUT'`, вызывается метод `_handle_reach_out`.
   - Если `action_type` равен `'TALK'`, вызывается метод `_handle_talk`.

**ASCII flowchart**:

```
Начало
|
V
[Перебор действий]
|
V
[Определение типа действия]
|
V
[Обработка действия]
|
V
Конец
```

**Примеры**:

```python
# Пример списка действий
actions = [
    {'type': 'REACH_OUT', 'content': 'Hello', 'target': 'Bob'},
    {'type': 'TALK', 'content': 'How are you?', 'target': 'Bob'}
]

# Обработка действий агентом Alice
world._handle_actions(source=alice, actions=actions)
```

### `_handle_reach_out`

```python
@transactional
def _handle_reach_out(self, source_agent: TinyPerson, content: str, target: str):
    """
    Обрабатывает действие `REACH_OUT`. Эта реализация по умолчанию всегда позволяет `REACH_OUT` завершиться успешно. Подклассы могут переопределить этот метод для реализации различных политик.

    Args:
        source_agent (TinyPerson): Агент, совершивший действие `REACH_OUT`.
        content (str): Содержимое сообщения.
        target (str): Цель сообщения.
    """
    ...
```

**Как работает функция**:

1. **Поиск целевого агента**: Ищет целевого агента (`target_agent`) по имени в среде.
2. **Установление доступности**: Если целевой агент найден, устанавливает взаимную доступность между исходным (`source_agent`) и целевым агентами.
3. **Социализация**: Агенты уведомляются об успешном установлении контакта.
4. **Обработка ошибки**: Если целевой агент не найден, в лог записывается отладочное сообщение об ошибке.

**ASCII flowchart**:

```
Начало
|
V
[Поиск целевого агента]
|
V
[Установление доступности]
|
V
[Социализация]
|
V
Конец
```

**Примеры**:

```python
# Агент Alice пытается установить контакт с агентом Bob
world._handle_reach_out(source_agent=alice, content='Hello', target='Bob')
```

### `_handle_talk`

```python
@transactional
def _handle_talk(self, source_agent: TinyPerson, content: str, target: str):
    """
    Обрабатывает действие `TALK`, доставляя указанное содержимое указанной цели.

    Args:
        source_agent (TinyPerson): Агент, совершивший действие `TALK`.
        content (str): Содержимое сообщения.
        target (str, optional): Цель сообщения.
    """
    ...
```

**Как работает функция**:

1. **Поиск целевого агента**: Ищет целевого агента (`target_agent`) по имени в среде.
2. **Доставка сообщения**: Если целевой агент найден, сообщение (`content`) доставляется целевому агенту.
3. **Широковещательная передача**: Если целевой агент не найден и включена широковещательная передача (`self.broadcast_if_no_target`), сообщение транслируется всем агентам в среде.

**ASCII flowchart**:

```
Начало
|
V
[Поиск целевого агента]
|
V
[Доставка сообщения]
|
V
[Широковещательная передача]
|
V
Конец
```

**Примеры**:

```python
# Агент Alice говорит с агентом Bob
world._handle