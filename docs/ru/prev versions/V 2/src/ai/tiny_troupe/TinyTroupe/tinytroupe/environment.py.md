# Модуль `environment`

## Обзор

Модуль `environment` предоставляет классы для создания и управления окружениями, в которых взаимодействуют агенты. Окружения могут моделировать различные сценарии, от простых до сложных социальных сетей, с возможностью настройки поведения агентов, управления временем и обработкой действий.

## Оглавление

1.  [Классы](#классы)
    *   [TinyWorld](#tinyworld)
    *   [TinySocialNetwork](#tinysocialnetwork)
2.  [Функции](#функции)
    *  [Нет функций](#нет-функций)

## Классы

### `TinyWorld`

**Описание**:
Базовый класс для окружений.

**Методы**:

*   `__init__`: Инициализирует окружение.
*   `_step`: Выполняет один шаг в окружении, позволяя всем агентам действовать.
*   `_advance_datetime`: Увеличивает текущее время в окружении.
*   `run`: Запускает окружение на заданное количество шагов.
*   `skip`: Пропускает заданное количество шагов в окружении без выполнения действий агентов.
*   `run_minutes`: Запускает окружение на заданное количество минут.
*   `skip_minutes`: Пропускает заданное количество минут в окружении.
*   `run_hours`: Запускает окружение на заданное количество часов.
*  `skip_hours`: Пропускает заданное количество часов в окружении.
*   `run_days`: Запускает окружение на заданное количество дней.
*   `skip_days`: Пропускает заданное количество дней в окружении.
*   `run_weeks`: Запускает окружение на заданное количество недель.
*   `skip_weeks`: Пропускает заданное количество недель в окружении.
*   `run_months`: Запускает окружение на заданное количество месяцев.
*   `skip_months`: Пропускает заданное количество месяцев в окружении.
*   `run_years`: Запускает окружение на заданное количество лет.
*  `skip_years`: Пропускает заданное количество лет в окружении.
*   `add_agents`: Добавляет список агентов в окружение.
*   `add_agent`: Добавляет агента в окружение.
*   `remove_agent`: Удаляет агента из окружения.
*   `remove_all_agents`: Удаляет всех агентов из окружения.
*   `get_agent_by_name`: Возвращает агента по имени.
*   `_handle_actions`: Обрабатывает действия, предпринятые агентами.
*   `_handle_reach_out`: Обрабатывает действие `REACH_OUT`.
*   `_handle_talk`: Обрабатывает действие `TALK`.
*   `broadcast`: Рассылает сообщение всем агентам в окружении.
*   `broadcast_thought`: Рассылает мысль всем агентам в окружении.
*  `broadcast_internal_goal`: Рассылает внутреннюю цель всем агентам в окружении.
*  `broadcast_context_change`: Рассылает изменение контекста всем агентам в окружении.
*   `make_everyone_accessible`: Делает всех агентов доступными друг для друга.
*   `_display_communication`: Отображает текущую коммуникацию и сохраняет её в буфере.
*  `_push_and_display_latest_communication`: Добавляет последние коммуникации в буфер агента.
*  `pop_and_display_latest_communications`: Извлекает и отображает последние сообщения из буфера.
*   `_display`: Отображает сообщение.
*   `clear_communications_buffer`: Очищает буфер сообщений.
*   `__repr__`: Возвращает строковое представление объекта.
*   `_pretty_step`: Форматирует сообщение о шаге симуляции.
*   `pp_current_interactions`: Выводит текущие взаимодействия агентов в отформатированном виде.
*   `pretty_current_interactions`: Возвращает строку с текущими взаимодействиями агентов в отформатированном виде.
*   `encode_complete_state`: Кодирует полное состояние окружения в словарь.
*   `decode_complete_state`: Декодирует полное состояние окружения из словаря.
*    `add_environment`: Добавляет окружение в список всех окружений.
*    `set_simulation_for_free_environments`: Устанавливает симуляцию для свободных окружений.
*    `get_environment_by_name`: Возвращает окружение по имени.
*    `clear_environments`: Очищает список всех окружений.

#### `__init__`

```python
def __init__(self, name: str="A TinyWorld", agents=[],
                 initial_datetime=datetime.datetime.now(),
                 broadcast_if_no_target=True)
```
**Описание**:
Инициализирует окружение.

**Параметры**:
*   `name` (str): Имя окружения. По умолчанию "A TinyWorld".
*   `agents` (list): Список агентов, которых нужно добавить в окружение. По умолчанию пустой список.
*   `initial_datetime` (datetime): Начальное время окружения. По умолчанию текущее время.
*  `broadcast_if_no_target` (bool): Если True, то действия будут транслироваться, если цель действия не найдена. По умолчанию `True`.

#### `_step`
```python
@transactional
def _step(self, timedelta_per_step=None)
```
**Описание**:
Выполняет один шаг в окружении.

**Параметры**:
*  `timedelta_per_step` (timedelta, optional): Временной интервал между шагами. По умолчанию `None`.

**Возвращает**:
*   `dict`: Словарь действий агентов на этом шаге в формате `{agent_name: [action_1, action_2, ...], ...}`.

#### `_advance_datetime`
```python
def _advance_datetime(self, timedelta)
```
**Описание**:
Увеличивает текущее время в окружении на заданный интервал.

**Параметры**:
*   `timedelta` (timedelta): Временной интервал, на который нужно увеличить текущее время.

#### `run`
```python
@transactional
def run(self, steps: int, timedelta_per_step=None, return_actions=False)
```
**Описание**:
Запускает окружение на заданное количество шагов.

**Параметры**:
*   `steps` (int): Количество шагов, на которое нужно запустить окружение.
*   `timedelta_per_step` (timedelta, optional): Временной интервал между шагами. По умолчанию `None`.
*   `return_actions` (bool, optional): Если `True`, то возвращает действия, выполненные агентами. По умолчанию `False`.

**Возвращает**:
*   `list` : Список действий, выполненных агентами с течением времени, если `return_actions` равен `True`. Список имеет формат: `[{agent_name: [action_1, action_2, ...]}, {agent_name_2: [action_1, action_2, ...]}, ...]`.

#### `skip`
```python
@transactional
def skip(self, steps: int, timedelta_per_step=None)
```
**Описание**:
Пропускает заданное количество шагов в окружении.

**Параметры**:
*   `steps` (int): Количество шагов, которое нужно пропустить.
*   `timedelta_per_step` (timedelta, optional): Временной интервал между шагами. По умолчанию `None`.

#### `run_minutes`
```python
def run_minutes(self, minutes: int)
```
**Описание**:
Запускает окружение на заданное количество минут.

**Параметры**:
*   `minutes` (int): Количество минут для запуска.

#### `skip_minutes`
```python
def skip_minutes(self, minutes: int)
```
**Описание**:
Пропускает заданное количество минут в окружении.

**Параметры**:
*   `minutes` (int): Количество минут для пропуска.

#### `run_hours`
```python
def run_hours(self, hours: int)
```
**Описание**:
Запускает окружение на заданное количество часов.

**Параметры**:
*   `hours` (int): Количество часов для запуска.

#### `skip_hours`
```python
def skip_hours(self, hours: int)
```
**Описание**:
Пропускает заданное количество часов в окружении.

**Параметры**:
*   `hours` (int): Количество часов для пропуска.

#### `run_days`
```python
def run_days(self, days: int)
```
**Описание**:
Запускает окружение на заданное количество дней.

**Параметры**:
*   `days` (int): Количество дней для запуска.

#### `skip_days`
```python
def skip_days(self, days: int)
```
**Описание**:
Пропускает заданное количество дней в окружении.

**Параметры**:
*   `days` (int): Количество дней для пропуска.

#### `run_weeks`
```python
def run_weeks(self, weeks: int)
```
**Описание**:
Запускает окружение на заданное количество недель.

**Параметры**:
*   `weeks` (int): Количество недель для запуска.

#### `skip_weeks`
```python
def skip_weeks(self, weeks: int)
```
**Описание**:
Пропускает заданное количество недель в окружении.

**Параметры**:
*   `weeks` (int): Количество недель для пропуска.

#### `run_months`
```python
def run_months(self, months: int)
```
**Описание**:
Запускает окружение на заданное количество месяцев.

**Параметры**:
*   `months` (int): Количество месяцев для запуска.

#### `skip_months`
```python
def skip_months(self, months: int)
```
**Описание**:
Пропускает заданное количество месяцев в окружении.

**Параметры**:
*   `months` (int): Количество месяцев для пропуска.

#### `run_years`
```python
def run_years(self, years: int)
```
**Описание**:
Запускает окружение на заданное количество лет.

**Параметры**:
*   `years` (int): Количество лет для запуска.

#### `skip_years`
```python
def skip_years(self, years: int)
```
**Описание**:
Пропускает заданное количество лет в окружении.

**Параметры**:
*   `years` (int): Количество лет для пропуска.

#### `add_agents`
```python
def add_agents(self, agents: list)
```
**Описание**:
Добавляет список агентов в окружение.

**Параметры**:
*   `agents` (list): Список агентов для добавления.

**Возвращает**:
*   `Self`: Возвращает экземпляр окружения для возможности цепочного вызова.

#### `add_agent`
```python
def add_agent(self, agent: TinyPerson)
```
**Описание**:
Добавляет агента в окружение.

**Параметры**:
*   `agent` (TinyPerson): Агент для добавления.

**Возвращает**:
*   `Self`: Возвращает экземпляр окружения для возможности цепочного вызова.

**Вызывает исключения**:
*   `ValueError`: Если имя агента не уникально в окружении.

#### `remove_agent`
```python
def remove_agent(self, agent: TinyPerson)
```
**Описание**:
Удаляет агента из окружения.

**Параметры**:
*   `agent` (TinyPerson): Агент для удаления.

**Возвращает**:
*   `Self`: Возвращает экземпляр окружения для возможности цепочного вызова.

#### `remove_all_agents`
```python
def remove_all_agents(self)
```
**Описание**:
Удаляет всех агентов из окружения.

**Возвращает**:
*   `Self`: Возвращает экземпляр окружения для возможности цепочного вызова.

#### `get_agent_by_name`
```python
def get_agent_by_name(self, name: str) -> TinyPerson
```
**Описание**:
Возвращает агента по его имени.

**Параметры**:
*   `name` (str): Имя агента для поиска.

**Возвращает**:
*   `TinyPerson | None`: Агент с заданным именем или None, если агент не найден.

#### `_handle_actions`
```python
@transactional
def _handle_actions(self, source: TinyPerson, actions: list)
```
**Описание**:
Обрабатывает действия, предпринятые агентами.

**Параметры**:
*   `source` (TinyPerson): Агент, который предпринял действие.
*   `actions` (list): Список действий, которые нужно обработать.

#### `_handle_reach_out`
```python
@transactional
def _handle_reach_out(self, source_agent: TinyPerson, content: str, target: str)
```
**Описание**:
Обрабатывает действие `REACH_OUT`.

**Параметры**:
*   `source_agent` (TinyPerson): Агент, который предпринял действие.
*   `content` (str): Содержание сообщения.
*   `target` (str): Цель сообщения.

#### `_handle_talk`
```python
@transactional
def _handle_talk(self, source_agent: TinyPerson, content: str, target: str)
```
**Описание**:
Обрабатывает действие `TALK`, доставляя сообщение указанному агенту.

**Параметры**:
*   `source_agent` (TinyPerson): Агент, который предпринял действие.
*   `content` (str): Содержание сообщения.
*   `target` (str): Цель сообщения.

#### `broadcast`
```python
@transactional
def broadcast(self, speech: str, source: AgentOrWorld=None)
```
**Описание**:
Рассылает сообщение всем агентам в окружении.

**Параметры**:
*   `speech` (str): Содержание сообщения.
*   `source` (AgentOrWorld, optional): Агент или окружение, которое отправило сообщение. По умолчанию `None`.

#### `broadcast_thought`
```python
@transactional
def broadcast_thought(self, thought: str, source: AgentOrWorld=None)
```
**Описание**:
Рассылает мысль всем агентам в окружении.

**Параметры**:
*   `thought` (str): Содержание мысли.
*   `source` (AgentOrWorld, optional): Агент или окружение, которое отправило мысль. По умолчанию `None`.

#### `broadcast_internal_goal`
```python
@transactional
def broadcast_internal_goal(self, internal_goal: str)
```
**Описание**:
Рассылает внутреннюю цель всем агентам в окружении.

**Параметры**:
*   `internal_goal` (str): Содержание внутренней цели.

#### `broadcast_context_change`
```python
@transactional
def broadcast_context_change(self, context:list)
```
**Описание**:
Рассылает изменение контекста всем агентам в окружении.

**Параметры**:
*   `context` (list): Изменения контекста.

#### `make_everyone_accessible`
```python
def make_everyone_accessible(self)
```
**Описание**:
Делает всех агентов в окружении доступными друг для друга.

#### `_display_communication`
```python
def _display_communication(self, cur_step, total_steps, kind, timedelta_per_step=None)
```
**Описание**:
Отображает текущую коммуникацию и сохраняет её в буфере.

**Параметры**:
*  `cur_step` (int): Номер текущего шага.
*  `total_steps` (int): Общее количество шагов.
*   `kind` (str): Тип коммуникации.
*   `timedelta_per_step` (timedelta, optional): Временной интервал между шагами. По умолчанию `None`.

#### `_push_and_display_latest_communication`
```python
def _push_and_display_latest_communication(self, rendering)
```
**Описание**:
Добавляет последние коммуникации в буфер агента.

**Параметры**:
*   `rendering` (dict): Словарь с содержимым коммуникации.

#### `pop_and_display_latest_communications`
```python
def pop_and_display_latest_communications(self)
```
**Описание**:
Извлекает и отображает последние сообщения из буфера.

**Возвращает**:
*   `list`: Список сообщений из буфера.

#### `_display`
```python
def _display(self, communication)
```
**Описание**:
Отображает сообщение.

**Параметры**:
*   `communication` (dict | str): Сообщение для отображения.

#### `clear_communications_buffer`
```python
def clear_communications_buffer(self)
```
**Описание**:
Очищает буфер сообщений.

#### `__repr__`
```python
def __repr__(self)
```
**Описание**:
Возвращает строковое представление объекта.

**Возвращает**:
*   `str`: Строковое представление окружения.

#### `_pretty_step`
```python
def _pretty_step(self, cur_step, total_steps, timedelta_per_step=None)
```
**Описание**:
Форматирует сообщение о шаге симуляции.

**Параметры**:
*   `cur_step` (int): Номер текущего шага.
*   `total_steps` (int): Общее количество шагов.
*   `timedelta_per_step` (timedelta, optional): Временной интервал между шагами. По умолчанию `None`.

**Возвращает**:
*   `str`: Отформатированное сообщение о шаге симуляции.

#### `pp_current_interactions`
```python
def pp_current_interactions(self, simplified=True, skip_system=True)
```
**Описание**:
Выводит текущие взаимодействия агентов в отформатированном виде.

**Параметры**:
*  `simplified` (bool, optional): Упрощенный вывод. По умолчанию `True`.
*  `skip_system` (bool, optional): Пропустить системные сообщения. По умолчанию `True`.

#### `pretty_current_interactions`
```python
def pretty_current_interactions(self, simplified=True, skip_system=True, max_content_length=default["max_content_display_length"], first_n=None, last_n=None, include_omission_info:bool=True)
```
**Описание**:
Возвращает строку с текущими взаимодействиями агентов в отформатированном виде.

**Параметры**:
*  `simplified` (bool, optional): Упрощенный вывод. По умолчанию `True`.
*  `skip_system` (bool, optional): Пропустить системные сообщения. По умолчанию `True`.
* `max_content_length` (int, optional): Максимальная длинна контента для отображения. По умолчанию `default["max_content_display_length"]`.
* `first_n` (int, optional):  Показать первые N сообщений. По умолчанию `None`.
* `last_n` (int, optional):  Показать последние N сообщений. По умолчанию `None`.
* `include_omission_info` (bool, optional): Включать ли информацию об пропусках в выводе. По умолчанию `True`.

**Возвращает**:
* `str`: Строка с отформатированными взаимодействиями агентов.

#### `encode_complete_state`
```python
def encode_complete_state(self) -> dict
```
**Описание**:
Кодирует полное состояние окружения в словарь.

**Возвращает**:
*   `dict`: Словарь, представляющий полное состояние окружения.

#### `decode_complete_state`
```python
def decode_complete_state(self, state:dict) -> Self
```
**Описание**:
Декодирует полное состояние окружения из словаря.

**Параметры**:
*   `state` (dict): Словарь, содержащий состояние окружения.

**Возвращает**:
*   `Self`: Восстановленное окружение.

**Вызывает исключения**:
*   `ValueError`: Если не удалось декодировать агента.

#### `add_environment`
```python
@staticmethod
def add_environment(environment)
```
**Описание**:
Добавляет окружение в список всех окружений.

**Параметры**:
*   `environment` (TinyWorld): Окружение для добавления.

**Вызывает исключения**:
*   `ValueError`: Если имя окружения не уникально.

#### `set_simulation_for_free_environments`
```python
@staticmethod
def set_simulation_for_free_environments(simulation)
```
**Описание**:
Устанавливает симуляцию для свободных окружений.

**Параметры**:
*   `simulation` (Simulation): Симуляция для установки.

#### `get_environment_by_name`
```python
@staticmethod
def get_environment_by_name(name: str)
```
**Описание**:
Возвращает окружение по его имени.

**Параметры**:
*   `name` (str): Имя окружения.

**Возвращает**:
*   `TinyWorld | None`: Окружение с заданным именем или None, если окружение не найдено.

#### `clear_environments`
```python
@staticmethod
def clear_environments()
```
**Описание**:
Очищает список всех окружений.

### `TinySocialNetwork`
**Описание**:
Класс для создания окружений, моделирующих социальные сети.

**Методы**:

*   `__init__`: Инициализирует социальную сеть.
*   `add_relation`: Добавляет связь между двумя агентами.
*   `_update_agents_contexts`: Обновляет контексты агентов на основе текущих связей.
*   `_step`: Выполняет один шаг в социальной сети.
*   `_handle_reach_out`: Обрабатывает действие `REACH_OUT` в контексте социальной сети.
*   `is_in_relation_with`: Проверяет, находятся ли два агента в каких-либо отношениях.

#### `__init__`
```python
def __init__(self, name, broadcast_if_no_target=True)
```
**Описание**:
Создает новую социальную сеть.

**Параметры**:
*   `name` (str): Имя социальной сети.
*  `broadcast_if_no_target` (bool): Если True, то действия будут транслироваться через доступные связи агента, если цель действия не найдена. По умолчанию `True`.

#### `add_relation`
```python
@transactional
def add_relation(self, agent_1, agent_2, name="default")
```
**Описание**:
Добавляет связь между двумя агентами.

**Параметры**:
*   `agent_1` (TinyPerson): Первый агент.
*   `agent_2` (TinyPerson): Второй агент.
*   `name` (str, optional): Имя связи. По умолчанию `default`.

**Возвращает**:
*   `Self`: Возвращает экземпляр социальной сети для возможности цепочного вызова.

#### `_update_agents_contexts`
```python
@transactional
def _update_agents_contexts(self)
```
**Описание**:
Обновляет контексты агентов на основе текущих связей.

#### `_step`
```python
@transactional
def _step(self)
```
**Описание**:
Выполняет один шаг в социальной сети.

#### `_handle_reach_out`
```python
@transactional
def _handle_reach_out(self, source_agent: TinyPerson, content: str, target: str)
```
**Описание**:
Обрабатывает действие `REACH_OUT` в контексте социальной сети.

**Параметры**:
*   `source_agent` (TinyPerson): Агент, который предпринял действие.
*   `content` (str): Содержание сообщения.
*   `target` (str): Цель сообщения.

#### `is_in_relation_with`
```python
def is_in_relation_with(self, agent_1:TinyPerson, agent_2:TinyPerson, relation_name=None) -> bool
```
**Описание**:
Проверяет, находятся ли два агента в каких-либо отношениях.

**Параметры**:
*   `agent_1` (TinyPerson): Первый агент.
*   `agent_2` (TinyPerson): Второй агент.
*   `relation_name` (str, optional): Имя отношения для проверки. Если None, проверяет наличие любой связи. По умолчанию `None`.

**Возвращает**:
*   `bool`: True, если агенты находятся в указанном или любом отношении, False в противном случае.

## Функции

### Нет функций
В данном файле отсутствуют функции вне классов.