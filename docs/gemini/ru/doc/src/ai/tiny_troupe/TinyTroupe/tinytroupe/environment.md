# Модуль `environment.py`

## Обзор

Данный модуль определяет базовые классы для работы со средами (environments) в системе TinyTroupe. Он предоставляет возможность моделирования взаимодействия агентов друг с другом и внешними сущностями.  Реализованы методы для управления временем симуляции, добавления и удаления агентов, а также для обработки различных типов взаимодействий.  Модуль содержит классы `TinyWorld` и `TinySocialNetwork`, наследующие от `TinyWorld`.

## Классы

### `TinyWorld`

**Описание**: Базовый класс для определения сред.  Представляет собой структурированное пространство для взаимодействия агентов.

**Атрибуты**:

- `all_environments`: Словарь, хранящий все созданные среды (ключ - имя среды, значение - экземпляр среды).
- `communication_display`: Флаг, определяющий, выводить ли сообщения о взаимодействиях.
- `name`: Имя среды.
- `current_datetime`: Текущая дата и время симуляции.
- `broadcast_if_no_target`: Флаг, определяет, нужно ли транслировать действие, если целевой объект не найден.
- `simulation_id`: Идентификатор симуляции, по умолчанию None.
- `agents`: Список агентов в среде.
- `name_to_agent`: Словарь, связывающий имена агентов с их экземплярами.
- `_displayed_communications_buffer`: Буфер для хранения сообщений, отображаемых в среде.
- `console`: Объект для отображения вывода в консоли.

**Методы**:

- `__init__(name: str="A TinyWorld", agents=[], initial_datetime=datetime.datetime.now(), broadcast_if_no_target=True)`: Инициализирует среду.
    - `name` (str): Название среды.
    - `agents` (list): Список агентов для добавления.
    - `initial_datetime` (datetime): Начальная дата и время среды (по умолчанию текущая дата).
    - `broadcast_if_no_target` (bool): Транслировать действия, если целевой объект не найден.
- `_step(timedelta_per_step=None)`: Выполняет один шаг симуляции.
    - `timedelta_per_step` (timedelta, optional): Интервал времени между шагами симуляции.
- `_advance_datetime(timedelta)`: Передвигает текущую дату и время симуляции на указанный интервал времени.
    - `timedelta` (timedelta): Интервал времени для перемещения.
- `run(steps: int, timedelta_per_step=None, return_actions=False)`: Запускает симуляцию на заданное количество шагов.
    - `steps` (int): Количество шагов.
    - `timedelta_per_step` (timedelta, optional): Интервал времени между шагами симуляции.
    - `return_actions` (bool, optional): Возвращать ли действия агентов.
- `skip(steps: int, timedelta_per_step=None)`: Пропускает заданное количество шагов симуляции.
- `run_minutes(minutes: int)`, `skip_minutes(minutes: int)`, `run_hours(hours: int)`, `skip_hours(hours: int)`, `run_days(days: int)`, `skip_days(days: int)`, `run_weeks(weeks: int)`, `skip_weeks(weeks: int)`, `run_months(months: int)`, `skip_months(months: int)`, `run_years(years: int)`, `skip_years(years: int)`: Запускает/пропускает симуляцию на заданное количество единиц времени.
- `add_agents(agents: list)`: Добавляет список агентов в среду.
    - `agents` (list): Список агентов.
- `add_agent(agent: TinyPerson)`: Добавляет агента в среду.
    - `agent` (TinyPerson): Агент для добавления.
- `remove_agent(agent: TinyPerson)`: Удаляет агента из среды.
    - `agent` (TinyPerson): Агент для удаления.
- `remove_all_agents()`: Удаляет всех агентов из среды.
- `get_agent_by_name(name: str) -> TinyPerson`: Возвращает агента по имени.
    - `name` (str): Имя агента.
- `_handle_actions(source: TinyPerson, actions: list)`: Обрабатывает действия агентов.
- `_handle_reach_out(source_agent: TinyPerson, content: str, target: str)`: Обрабатывает действие "REACH_OUT".
- `_handle_talk(source_agent: TinyPerson, content: str, target: str)`: Обрабатывает действие "TALK".
- `broadcast(speech: str, source: AgentOrWorld=None)`: Транслирует сообщение всем агентам.
- `broadcast_thought(thought: str, source: AgentOrWorld=None)`: Транслирует мысль всем агентам.
- `broadcast_internal_goal(internal_goal: str)`: Транслирует внутреннюю цель всем агентам.
- `broadcast_context_change(context:list)`: Транслирует изменение контекста всем агентам.
- `make_everyone_accessible()`: Делает всех агентов доступными друг для друга.
- `_display_communication(cur_step, total_steps, kind, timedelta_per_step=None)`: Отображает и буферизует коммуникации.
- `_push_and_display_latest_communication(rendering)`: Добавляет и отображает последнюю коммуникацию.
- `pop_and_display_latest_communications()`: Возвращает и отображает все накопленные коммуникации, очищая буфер.
- `_display(communication)`: Отображает коммуникации в консоли.
- `clear_communications_buffer()`: Очищает буфер коммуникаций.
- `__repr__()`: Строковое представление объекта.
- `_pretty_step(cur_step, total_steps, timedelta_per_step=None)`: Форматирует вывод о шаге симуляции.
- `pp_current_interactions(simplified=True, skip_system=True)`, `pretty_current_interactions(...)`: Методы для красивого вывода текущих взаимодействий.
- `encode_complete_state()`: Кодирует полное состояние среды в словарь.
- `decode_complete_state(state:dict) -> Self`: Декодирует полное состояние среды из словаря.
- `add_environment(environment)`: Статический метод для добавления среды в список всех сред.
- `set_simulation_for_free_environments(simulation)`: Статический метод для установки симуляции для свободных сред.
- `get_environment_by_name(name: str)`: Статический метод для получения среды по имени.
- `clear_environments()`: Статический метод для очистки списка всех сред.


### `TinySocialNetwork`

**Описание**: Наследуемый класс для моделирования социальных сетей.

**Атрибуты**:

- `relations`: Словарь, хранящий отношения между агентами.

**Методы**:

- `__init__(name, broadcast_if_no_target=True)`: Инициализирует среду `TinySocialNetwork`.
- `add_relation(agent_1, agent_2, name="default")`: Добавляет отношение между агентами.
- `_update_agents_contexts()`: Обновляет контексты агентов на основе текущего состояния мира.
- `_step()`: Выполняет шаг симуляции, обновляя контексты.
- `_handle_reach_out(source_agent, content, target)`: Обрабатывает действие "REACH_OUT", учитывая отношения в сети.
- `is_in_relation_with(agent_1, agent_2, relation_name=None)`: Проверяет, находятся ли два агента в отношении.


## Функции


(Нет функций на уровне модуля)

##  Комментарии

Комментарии в коде полностью соответствуют заданным требованиям.