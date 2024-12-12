# Модуль `tinytroupe.environment`

## Обзор

Этот модуль содержит определение классов для работы с окружениями, в которых взаимодействуют агенты.  Классы позволяют структурировать мир, в котором агенты взаимодействуют друг с другом и внешними сущностями.  Модуль предоставляет базовый класс `TinyWorld` и наследника `TinySocialNetwork` для более сложных социальных взаимодействий.  Он включает функции для управления агентами, проведения симуляции и взаимодействия.

## Оглавление

* [Модуль `tinytroupe.environment`](#модуль-tinytroupe-environment)
* [Обзор](#обзор)
* [Классы](#классы)
    * [`TinyWorld`](#tinyworld)
    * [`TinySocialNetwork`](#tinysocialnetwork)
* [Функции](#функции)
    * [`TinyWorld.add_environment`](#tinyworldadd-environment)
    * [`TinyWorld.set_simulation_for_free_environments`](#tinyworldset-simulation-for-free-environments)
    * [`TinyWorld.get_environment_by_name`](#tinyworldget-environment-by-name)
    * [`TinyWorld.clear_environments`](#tinyworldclear-environments)
    * [`TinySocialNetwork.add_relation`](#tinysocialnetworkadd-relation)
    *  [... другие методы и функции ...]


## Классы

### `TinyWorld`

**Описание**: Базовый класс для окружений.  Представляет собой структуру для описания среды, в которой действуют агенты.

**Атрибуты**:
- `all_environments`: Словарь, хранящий все созданные окружения (имя -> окружение).
- `communication_display`: Флаг, определяющий, отображаются ли сообщения об обмене информацией.
- `name`: Имя окружения.
- `current_datetime`: Текущая дата и время симуляции.
- `broadcast_if_no_target`: Флаг, определяющий, транслируются ли действия, если целевой объект не найден.
- `simulation_id`: Идентификатор симуляции, в которой используется агент.

**Методы**:

- `__init__(self, name: str="A TinyWorld", agents=[], initial_datetime=datetime.datetime.now(), broadcast_if_no_target=True)`: Инициализирует окружение.  Устанавливает имя, список агентов, начальное время симуляции, флаги трансляции действий.
- `_step(self, timedelta_per_step=None)`: Выполняет один шаг в симуляции, обрабатывает действия агентов.
- `_advance_datetime(self, timedelta)`: Увеличивает текущее время симуляции на заданное значение.
- `run(self, steps: int, timedelta_per_step=None, return_actions=False)`: Запускает симуляцию на заданное количество шагов. Возвращает список действий агентов.
- `skip(self, steps: int, timedelta_per_step=None)`: Пропускает заданное количество шагов в симуляции, продвигается вперед во времени, не выполняя действия.
- `run_minutes(self, minutes: int)`, `skip_minutes(self, minutes: int)`, `run_hours(self, hours: int)`, `skip_hours(self, hours: int)`, `run_days(self, days: int)`, `skip_days(self, days: int)`, `run_weeks(self, weeks: int)`, `skip_weeks(self, weeks: int)`, `run_months(self, months: int)`, `skip_months(self, months: int)`, `run_years(self, years: int)`, `skip_years(self, years: int)`: Запускают или пропускают симуляцию в течение заданного интервала времени.
- `add_agents(self, agents: list)`: Добавляет список агентов в окружение.
- `add_agent(self, agent: TinyPerson)`: Добавляет агента в окружение. Возможна ошибка ValueError, если имя агента не уникально.
- `remove_agent(self, agent: TinyPerson)`: Удаляет агента из окружения.
- `remove_all_agents(self)`: Удаляет всех агентов из окружения.
- `get_agent_by_name(self, name: str) -> TinyPerson`: Возвращает агента по имени или None.
- `_handle_actions(self, source: TinyPerson, actions: list)`: Обрабатывает действия агентов.
- `_handle_reach_out(self, source_agent: TinyPerson, content: str, target: str)`: Обрабатывает действие REACH_OUT.
- `_handle_talk(self, source_agent: TinyPerson, content: str, target: str)`: Обрабатывает действие TALK.
- `broadcast(self, speech: str, source: AgentOrWorld=None)`: Транслирует сообщение всем агентам в окружении.
- `broadcast_thought(self, thought: str, source: AgentOrWorld=None)`: Транслирует мысль всем агентам.
- `broadcast_internal_goal(self, internal_goal: str)`: Транслирует внутреннюю цель всем агентам.
- `broadcast_context_change(self, context:list)`: Транслирует изменение контекста всем агентам.
- `make_everyone_accessible(self)`: Делает всех агентов доступными друг для друга.
- `_display_communication(self, cur_step, total_steps, kind, timedelta_per_step=None)`: Отображает текущую коммуникацию и сохраняет ее в буфере.
- `_push_and_display_latest_communication(self, rendering)`: Добавляет последнюю коммуникацию в буфер и отображает ее.
- `pop_and_display_latest_communications(self)`: Извлекает и отображает все сохраненные коммуникации из буфера.
- `clear_communications_buffer(self)`: Очищает буфер коммуникаций.
- `__repr__(self)`: Возвращает строковое представление объекта.
- `_pretty_step(self, cur_step, total_steps, timedelta_per_step=None)`: Форматирует строку для отображения шага симуляции.
- `pp_current_interactions(self, simplified=True, skip_system=True)`:  Красиво отображает текущие взаимодействия агентов.
- `pretty_current_interactions(self, simplified=True, skip_system=True, ...)`: Возвращает строку с красивым отображением взаимодействий агентов.
- `encode_complete_state(self) -> dict`: Кодирует полное состояние окружения в словарь.
- `decode_complete_state(self, state:dict) -> Self`: Декодирует полное состояние окружения из словаря.
- `TinyWorld.add_environment(environment)`: Добавляет окружение в список всех окружений.
- `TinyWorld.set_simulation_for_free_environments(simulation)`: Устанавливает симуляцию для свободных окружений.
- `TinyWorld.get_environment_by_name(name: str)`: Возвращает окружение по имени или None.
- `TinyWorld.clear_environments()`: Очищает список всех окружений.


### `TinySocialNetwork`

**Описание**: Наследник `TinyWorld`, добавляющий возможность моделирования социальных сетей.

**Атрибуты**:
- `relations`: Словарь, хранящий отношения между агентами.

**Методы**:

- `__init__(self, name, broadcast_if_no_target=True)`: Инициализирует социальную сеть.
- `add_relation(self, agent_1, agent_2, name="default")`: Добавляет отношение между агентами.
- `_update_agents_contexts(self)`: Обновляет контексты агентов на основе текущего состояния сети.
- `_step(self)`: Выполняет шаг симуляции с обновлением контекстов агентов.
- `_handle_reach_out(self, source_agent: TinyPerson, content: str, target: str)`: Обрабатывает REACH_OUT, учитывая наличие связи между агентами.
- `is_in_relation_with(self, agent_1: TinyPerson, agent_2: TinyPerson, relation_name=None) -> bool`: Проверяет, находятся ли агенты в отношении.


## Функции

### `TinyWorld.add_environment`

**Описание**: Добавляет окружение в глобальный список.

### `TinyWorld.set_simulation_for_free_environments`

**Описание**: Устанавливает симуляцию для свободных окружений.

### `TinyWorld.get_environment_by_name`

**Описание**: Возвращает окружение по имени.

### `TinyWorld.clear_environments`

**Описание**: Очищает глобальный список окружений.

[... другие функции, описанные аналогично ...]