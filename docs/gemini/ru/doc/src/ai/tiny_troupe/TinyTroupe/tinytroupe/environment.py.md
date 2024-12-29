# Модуль `environment`

## Обзор

Модуль `environment` предоставляет структуру для определения мира, в котором агенты взаимодействуют друг с другом, а также с внешними сущностями (например, поисковыми системами).

## Содержание

- [Классы](#классы)
  - [`TinyWorld`](#tinyworld)
  - [`TinySocialNetwork`](#tinysocialnetwork)
- [Функции](#функции)
  - [`add_environment`](#add_environment)
  - [`set_simulation_for_free_environments`](#set_simulation_for_free_environments)
  - [`get_environment_by_name`](#get_environment_by_name)
  - [`clear_environments`](#clear_environments)

## Классы

### `TinyWorld`

**Описание**: Базовый класс для окружений.

**Атрибуты**:
- `all_environments` (dict): Словарь всех созданных окружений (`name -> environment`).
- `communication_display` (bool): Определяет, отображать ли сообщения окружения (для всех окружений).

**Методы**:
- `__init__`: Инициализирует окружение.
- `_step`: Выполняет один шаг в окружении.
- `_advance_datetime`: Устанавливает текущее время окружения.
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
- `_handle_actions`: Обрабатывает действия, предпринятые агентами.
- `_handle_reach_out`: Обрабатывает действие `REACH_OUT`.
- `_handle_talk`: Обрабатывает действие `TALK`.
- `broadcast`: Доставляет сообщение всем агентам в окружении.
- `broadcast_thought`: Отправляет мысль всем агентам в окружении.
- `broadcast_internal_goal`: Рассылает внутреннюю цель всем агентам в окружении.
- `broadcast_context_change`: Рассылает изменения контекста всем агентам в окружении.
- `make_everyone_accessible`: Делает всех агентов в окружении доступными друг для друга.
- `_display_communication`: Отображает текущее общение и сохраняет его в буфере.
- `_push_and_display_latest_communication`: Помещает последние сообщения в буфер агента.
- `pop_and_display_latest_communications`: Извлекает последние сообщения и отображает их.
- `_display`: Отображает сообщение.
- `clear_communications_buffer`: Очищает буфер коммуникаций.
- `__repr__`: Возвращает строковое представление объекта.
- `_pretty_step`: Форматирует шаг симуляции для отображения.
- `pp_current_interactions`: Выводит текущие сообщения агентов в этом окружении.
- `pretty_current_interactions`: Возвращает отформатированную строку текущих сообщений агентов.
- `encode_complete_state`: Кодирует полное состояние окружения в словарь.
- `decode_complete_state`: Декодирует полное состояние окружения из словаря.

#### `__init__`
```python
def __init__(self, name: str="A TinyWorld", agents=[], 
                 initial_datetime=datetime.datetime.now(),
                 broadcast_if_no_target=True)
```
**Описание**: Инициализирует окружение.

**Параметры**:
- `name` (str): Имя окружения. По умолчанию `"A TinyWorld"`.
- `agents` (list): Список агентов для добавления в окружение. По умолчанию `[]`.
- `initial_datetime` (datetime): Начальная дата и время окружения. По умолчанию текущее время.
- `broadcast_if_no_target` (bool): Если `True`, транслирует действия, если цель действия не найдена. По умолчанию `True`.

#### `_step`
```python
def _step(self, timedelta_per_step=None)
```
**Описание**: Выполняет один шаг в окружении.

**Параметры**:
- `timedelta_per_step` (timedelta, optional): Временной интервал для продвижения времени на каждом шаге. По умолчанию `None`.

#### `_advance_datetime`
```python
def _advance_datetime(self, timedelta)
```
**Описание**: Продвигает текущую дату и время окружения на заданное значение.

**Параметры**:
- `timedelta` (timedelta): Временной интервал для продвижения времени.

#### `run`
```python
def run(self, steps: int, timedelta_per_step=None, return_actions=False)
```
**Описание**: Запускает окружение на заданное количество шагов.

**Параметры**:
- `steps` (int): Количество шагов для запуска окружения.
- `timedelta_per_step` (timedelta, optional): Временной интервал между шагами. По умолчанию `None`.
- `return_actions` (bool, optional): Если `True`, возвращает действия, выполненные агентами. По умолчанию `False`.

**Возвращает**:
- `list` : Список действий, предпринятых агентами, если `return_actions` имеет значение `True`.

#### `skip`
```python
def skip(self, steps: int, timedelta_per_step=None)
```
**Описание**: Пропускает заданное количество шагов в окружении.

**Параметры**:
- `steps` (int): Количество шагов для пропуска.
- `timedelta_per_step` (timedelta, optional): Временной интервал между шагами. По умолчанию `None`.

#### `run_minutes`
```python
def run_minutes(self, minutes: int)
```
**Описание**: Запускает окружение на заданное количество минут.

**Параметры**:
- `minutes` (int): Количество минут для запуска окружения.

#### `skip_minutes`
```python
def skip_minutes(self, minutes: int)
```
**Описание**: Пропускает заданное количество минут в окружении.

**Параметры**:
- `minutes` (int): Количество минут для пропуска.

#### `run_hours`
```python
def run_hours(self, hours: int)
```
**Описание**: Запускает окружение на заданное количество часов.

**Параметры**:
- `hours` (int): Количество часов для запуска окружения.

#### `skip_hours`
```python
def skip_hours(self, hours: int)
```
**Описание**: Пропускает заданное количество часов в окружении.

**Параметры**:
- `hours` (int): Количество часов для пропуска.

#### `run_days`
```python
def run_days(self, days: int)
```
**Описание**: Запускает окружение на заданное количество дней.

**Параметры**:
- `days` (int): Количество дней для запуска окружения.

#### `skip_days`
```python
def skip_days(self, days: int)
```
**Описание**: Пропускает заданное количество дней в окружении.

**Параметры**:
- `days` (int): Количество дней для пропуска.

#### `run_weeks`
```python
def run_weeks(self, weeks: int)
```
**Описание**: Запускает окружение на заданное количество недель.

**Параметры**:
- `weeks` (int): Количество недель для запуска окружения.

#### `skip_weeks`
```python
def skip_weeks(self, weeks: int)
```
**Описание**: Пропускает заданное количество недель в окружении.

**Параметры**:
- `weeks` (int): Количество недель для пропуска.

#### `run_months`
```python
def run_months(self, months: int)
```
**Описание**: Запускает окружение на заданное количество месяцев.

**Параметры**:
- `months` (int): Количество месяцев для запуска окружения.

#### `skip_months`
```python
def skip_months(self, months: int)
```
**Описание**: Пропускает заданное количество месяцев в окружении.

**Параметры**:
- `months` (int): Количество месяцев для пропуска.

#### `run_years`
```python
def run_years(self, years: int)
```
**Описание**: Запускает окружение на заданное количество лет.

**Параметры**:
- `years` (int): Количество лет для запуска окружения.

#### `skip_years`
```python
def skip_years(self, years: int)
```
**Описание**: Пропускает заданное количество лет в окружении.

**Параметры**:
- `years` (int): Количество лет для пропуска.

#### `add_agents`
```python
def add_agents(self, agents: list)
```
**Описание**: Добавляет список агентов в окружение.

**Параметры**:
- `agents` (list): Список агентов для добавления.

**Возвращает**:
- `self`: Для возможности вызова в цепочке.

#### `add_agent`
```python
def add_agent(self, agent: TinyPerson)
```
**Описание**: Добавляет агента в окружение. Имя агента должно быть уникальным в пределах окружения.

**Параметры**:
- `agent` (TinyPerson): Агент для добавления.

**Вызывает исключения**:
- `ValueError`: Если имя агента уже существует в окружении.

**Возвращает**:
- `self`: Для возможности вызова в цепочке.

#### `remove_agent`
```python
def remove_agent(self, agent: TinyPerson)
```
**Описание**: Удаляет агента из окружения.

**Параметры**:
- `agent` (TinyPerson): Агент для удаления.

**Возвращает**:
- `self`: Для возможности вызова в цепочке.

#### `remove_all_agents`
```python
def remove_all_agents(self)
```
**Описание**: Удаляет всех агентов из окружения.

**Возвращает**:
- `self`: Для возможности вызова в цепочке.

#### `get_agent_by_name`
```python
def get_agent_by_name(self, name: str) -> TinyPerson
```
**Описание**: Возвращает агента с указанным именем.

**Параметры**:
- `name` (str): Имя агента для поиска.

**Возвращает**:
- `TinyPerson`: Агент с указанным именем или `None`, если агент не найден.

#### `_handle_actions`
```python
def _handle_actions(self, source: TinyPerson, actions: list)
```
**Описание**: Обрабатывает действия, предпринятые агентами.

**Параметры**:
- `source` (TinyPerson): Агент, выполнивший действие.
- `actions` (list): Список действий для обработки.

#### `_handle_reach_out`
```python
def _handle_reach_out(self, source_agent: TinyPerson, content: str, target: str)
```
**Описание**: Обрабатывает действие `REACH_OUT`.

**Параметры**:
- `source_agent` (TinyPerson): Агент, выполнивший действие `REACH_OUT`.
- `content` (str): Содержание сообщения.
- `target` (str): Цель сообщения.

#### `_handle_talk`
```python
def _handle_talk(self, source_agent: TinyPerson, content: str, target: str)
```
**Описание**: Обрабатывает действие `TALK`, доставляя сообщение указанной цели.

**Параметры**:
- `source_agent` (TinyPerson): Агент, выполнивший действие `TALK`.
- `content` (str): Содержание сообщения.
- `target` (str): Цель сообщения.

#### `broadcast`
```python
def broadcast(self, speech: str, source: AgentOrWorld=None)
```
**Описание**: Доставляет сообщение всем агентам в окружении.

**Параметры**:
- `speech` (str): Содержание сообщения.
- `source` (AgentOrWorld, optional): Агент или окружение, отправившее сообщение. По умолчанию `None`.

#### `broadcast_thought`
```python
def broadcast_thought(self, thought: str, source: AgentOrWorld=None)
```
**Описание**: Отправляет мысль всем агентам в окружении.

**Параметры**:
- `thought` (str): Содержание мысли.
- `source` (AgentOrWorld, optional): Агент или окружение, отправившее мысль. По умолчанию `None`.

#### `broadcast_internal_goal`
```python
def broadcast_internal_goal(self, internal_goal: str)
```
**Описание**: Рассылает внутреннюю цель всем агентам в окружении.

**Параметры**:
- `internal_goal` (str): Содержание внутренней цели.

#### `broadcast_context_change`
```python
def broadcast_context_change(self, context:list)
```
**Описание**: Рассылает изменения контекста всем агентам в окружении.

**Параметры**:
- `context` (list): Содержание изменения контекста.

#### `make_everyone_accessible`
```python
def make_everyone_accessible(self)
```
**Описание**: Делает всех агентов в окружении доступными друг для друга.

#### `_display_communication`
```python
def _display_communication(self, cur_step, total_steps, kind, timedelta_per_step=None)
```
**Описание**: Отображает текущее общение и сохраняет его в буфере для последующего использования.

**Параметры**:
- `cur_step` (int): Текущий шаг.
- `total_steps` (int): Общее количество шагов.
- `kind` (str): Тип сообщения ('step').
- `timedelta_per_step` (timedelta, optional): Временной интервал между шагами. По умолчанию `None`.

#### `_push_and_display_latest_communication`
```python
def _push_and_display_latest_communication(self, rendering)
```
**Описание**: Помещает последние сообщения в буфер агента.

**Параметры**:
- `rendering` (dict): Словарь с содержимым и типом сообщения.

#### `pop_and_display_latest_communications`
```python
def pop_and_display_latest_communications(self)
```
**Описание**: Извлекает последние сообщения из буфера и отображает их.

**Возвращает**:
- `list`: Список извлеченных сообщений.

#### `_display`
```python
def _display(self, communication)
```
**Описание**: Отображает сообщение.

**Параметры**:
- `communication` (dict | str): Сообщение для отображения. Может быть словарем или строкой.

#### `clear_communications_buffer`
```python
def clear_communications_buffer(self)
```
**Описание**: Очищает буфер коммуникаций.

#### `__repr__`
```python
def __repr__(self)
```
**Описание**: Возвращает строковое представление объекта.

**Возвращает**:
- `str`: Строковое представление объекта.

#### `_pretty_step`
```python
def _pretty_step(self, cur_step, total_steps, timedelta_per_step=None)
```
**Описание**: Форматирует шаг симуляции для отображения.

**Параметры**:
- `cur_step` (int): Текущий шаг.
- `total_steps` (int): Общее количество шагов.
- `timedelta_per_step` (timedelta, optional): Временной интервал между шагами. По умолчанию `None`.

**Возвращает**:
- `str`: Отформатированная строка.

#### `pp_current_interactions`
```python
def pp_current_interactions(self, simplified=True, skip_system=True)
```
**Описание**: Выводит текущие сообщения агентов в этом окружении.

**Параметры**:
- `simplified` (bool, optional): Если `True`, выводит упрощенные сообщения. По умолчанию `True`.
- `skip_system` (bool, optional): Если `True`, пропускает системные сообщения. По умолчанию `True`.

#### `pretty_current_interactions`
```python
def pretty_current_interactions(self, simplified=True, skip_system=True, max_content_length=default["max_content_display_length"], first_n=None, last_n=None, include_omission_info:bool=True)
```
**Описание**: Возвращает отформатированную строку текущих сообщений агентов в этом окружении.

**Параметры**:
- `simplified` (bool, optional): Если `True`, выводит упрощенные сообщения. По умолчанию `True`.
- `skip_system` (bool, optional): Если `True`, пропускает системные сообщения. По умолчанию `True`.
- `max_content_length` (int, optional): Максимальная длина содержимого сообщений.
- `first_n` (int, optional): Количество первых сообщений для вывода.
- `last_n` (int, optional): Количество последних сообщений для вывода.
- `include_omission_info` (bool, optional): Если `True`, включает информацию об упущенных сообщениях. По умолчанию `True`.

**Возвращает**:
- `str`: Отформатированная строка сообщений.

#### `encode_complete_state`
```python
def encode_complete_state(self) -> dict
```
**Описание**: Кодирует полное состояние окружения в словарь.

**Возвращает**:
- `dict`: Словарь, представляющий состояние окружения.

#### `decode_complete_state`
```python
def decode_complete_state(self, state:dict) -> Self
```
**Описание**: Декодирует полное состояние окружения из словаря.

**Параметры**:
- `state` (dict): Словарь, содержащий состояние окружения.

**Возвращает**:
- `Self`: Восстановленное окружение.

### `TinySocialNetwork`

**Описание**: Подкласс `TinyWorld`, представляющий собой социальную сеть.

**Атрибуты**:
- `relations` (dict): Словарь отношений между агентами.

**Методы**:
- `__init__`: Инициализирует социальную сеть.
- `add_relation`: Добавляет отношение между двумя агентами.
- `_update_agents_contexts`: Обновляет контексты агентов на основе отношений.
- `_step`: Выполняет шаг в социальной сети.
- `_handle_reach_out`: Обрабатывает действие `REACH_OUT` с учетом отношений.
- `is_in_relation_with`: Проверяет, находятся ли два агента в отношении.

#### `__init__`
```python
def __init__(self, name, broadcast_if_no_target=True)
```
**Описание**: Создает новую социальную сеть.

**Параметры**:
- `name` (str): Имя окружения.
- `broadcast_if_no_target` (bool): Если `True`, то транслирует действия по доступным связям, если цель действия не найдена.

#### `add_relation`
```python
def add_relation(self, agent_1, agent_2, name="default")
```
**Описание**: Добавляет отношение между двумя агентами.

**Параметры**:
- `agent_1` (TinyPerson): Первый агент.
- `agent_2` (TinyPerson): Второй агент.
- `name` (str, optional): Имя отношения. По умолчанию `"default"`.

**Возвращает**:
- `self`: Для возможности вызова в цепочке.

#### `_update_agents_contexts`
```python
def _update_agents_contexts(self)
```
**Описание**: Обновляет наблюдения агентов на основе текущего состояния мира.

#### `_step`
```python
def _step(self)
```
**Описание**: Выполняет шаг в социальной сети.

#### `_handle_reach_out`
```python
def _handle_reach_out(self, source_agent: TinyPerson, content: str, target: str)
```
**Описание**: Обрабатывает действие `REACH_OUT`, позволяя связаться только с агентами в отношениях.

**Параметры**:
- `source_agent` (TinyPerson): Агент, отправивший запрос.
- `content` (str): Содержание сообщения.
- `target` (str): Цель сообщения.

#### `is_in_relation_with`
```python
def is_in_relation_with(self, agent_1:TinyPerson, agent_2:TinyPerson, relation_name=None) -> bool
```
**Описание**: Проверяет, находятся ли два агента в отношениях.

**Параметры**:
- `agent_1` (TinyPerson): Первый агент.
- `agent_2` (TinyPerson): Второй агент.
- `relation_name` (str, optional): Имя отношения для проверки.

**Возвращает**:
- `bool`: `True`, если агенты находятся в указанном отношении или в любом отношении, если `relation_name` не указан, `False` в противном случае.

## Функции

### `add_environment`
```python
@staticmethod
def add_environment(environment)
```
**Описание**: Добавляет окружение в список всех окружений. Имена окружений должны быть уникальными.

**Параметры**:
- `environment` (TinyWorld): Окружение для добавления.

**Вызывает исключения**:
- `ValueError`: Если окружение с таким именем уже существует.

### `set_simulation_for_free_environments`
```python
@staticmethod
def set_simulation_for_free_environments(simulation)
```
**Описание**: Устанавливает симуляцию, если она не была установлена. Позволяет свободным окружениям быть захваченными определенными симуляциями.

**Параметры**:
- `simulation`: Симуляция для установки.

### `get_environment_by_name`
```python
@staticmethod
def get_environment_by_name(name: str)
```
**Описание**: Возвращает окружение с указанным именем.

**Параметры**:
- `name` (str): Имя окружения для поиска.

**Возвращает**:
- `TinyWorld`: Окружение с указанным именем или `None`, если окружение не найдено.

### `clear_environments`
```python
@staticmethod
def clear_environments()
```
**Описание**: Очищает список всех окружений.