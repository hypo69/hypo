# Модуль `environment`

## Обзор

Данный модуль предоставляет классы для определения сред, в которых агенты взаимодействуют друг с другом и внешними сущностями.  Он определяет базовый класс `TinyWorld` и расширение `TinySocialNetwork`, моделирующие социальные сети.

## Оглавление

- [Модуль `environment`](#модуль-environment)
- [Обзор](#обзор)
- [Классы](#классы)
    - [`TinyWorld`](#tinyworld)
        - [`__init__`](#init)
        - [\_step](#_step)
        - [\_advance\_datetime](#_advance_datetime)
        - [run](#run)
        - [skip](#skip)
        - [run\_minutes](#run_minutes)
        - [skip\_minutes](#skip_minutes)
        - [run\_hours](#run_hours)
        - [skip\_hours](#skip_hours)
        - [run\_days](#run_days)
        - [skip\_days](#skip_days)
        - [run\_weeks](#run_weeks)
        - [skip\_weeks](#skip_weeks)
        - [run\_months](#run_months)
        - [skip\_months](#skip_months)
        - [run\_years](#run_years)
        - [skip\_years](#skip_years)
        - [add\_agents](#add_agents)
        - [add\_agent](#add_agent)
        - [remove\_agent](#remove_agent)
        - [remove\_all\_agents](#remove_all_agents)
        - [get\_agent\_by\_name](#get_agent_by_name)
        - [\_handle\_actions](#_handle_actions)
        - [\_handle\_reach\_out](#_handle_reach_out)
        - [\_handle\_talk](#_handle_talk)
        - [broadcast](#broadcast)
        - [broadcast\_thought](#broadcast_thought)
        - [broadcast\_internal\_goal](#broadcast_internal_goal)
        - [broadcast\_context\_change](#broadcast_context_change)
        - [make\_everyone\_accessible](#make_everyone_accessible)
        - [\_display\_communication](#_display_communication)
        - [\_push\_and\_display\_latest\_communication](#_push_and_display_latest_communication)
        - [pop\_and\_display\_latest\_communications](#pop_and_display_latest_communications)
        - [\_display](#_display)
        - [clear\_communications\_buffer](#clear_communications_buffer)
        - [\_\_repr\_\_](#__repr__)
        - [\_pretty\_step](#_pretty_step)
        - [pp\_current\_interactions](#pp_current_interactions)
        - [pretty\_current\_interactions](#pretty_current_interactions)
        - [encode\_complete\_state](#encode_complete_state)
        - [decode\_complete\_state](#decode_complete_state)
        - [add\_environment](#add_environment)
        - [set\_simulation\_for\_free\_environments](#set_simulation_for_free_environments)
        - [get\_environment\_by\_name](#get_environment_by_name)
        - [clear\_environments](#clear_environments)
    - [`TinySocialNetwork`](#tinysocialnetwork)
        - [`__init__`](#init-1)
        - [add\_relation](#add_relation)
        - [\_update\_agents\_contexts](#_update_agents_contexts)
        - [\_step](#_step-1)
        - [\_handle\_reach\_out](#_handle_reach_out-1)
        - [is\_in\_relation\_with](#is_in_relation_with)


## Классы

### `TinyWorld`

**Описание**: Базовый класс для окружений. Управляет агентами, временем и взаимодействиями в среде.

#### `__init__`

**Описание**: Инициализирует окружение.

**Параметры**:
- `name` (str): Имя окружения.
- `agents` (list): Список агентов, добавляемых в окружение.
- `initial_datetime` (datetime): Начальная дата и время окружения. По умолчанию текущая дата и время.
- `broadcast_if_no_target` (bool): Если True, действия будут транслироваться, если целевой объект не найден.


#### `_step`

**Описание**: Выполняет один шаг в среде. По умолчанию выполняет действия всех агентов и обрабатывает результаты. Подклассы могут переопределять этот метод для реализации различных политик.

#### `_advance_datetime`

**Описание**: Передвигает текущую дату и время среды на указанное количество времени.

**Параметры**:
- `timedelta` (timedelta): Время для продвижения.


#### `run`

**Описание**: Запускает окружение на заданное количество шагов.

**Параметры**:
- `steps` (int): Количество шагов для запуска.
- `timedelta_per_step` (timedelta, optional): Время между шагами.
- `return_actions` (bool, optional): Если True, возвращает действия агентов.


#### `skip`

**Описание**: Пропускает заданное количество шагов в среде. Время пройдет, но действия агентов не будут выполняться.

**Параметры**:
- `steps` (int): Количество шагов для пропуска.
- `timedelta_per_step` (timedelta, optional): Время между шагами.


(Остальные методы `TinyWorld` и `TinySocialNetwork` документированы аналогично)

```