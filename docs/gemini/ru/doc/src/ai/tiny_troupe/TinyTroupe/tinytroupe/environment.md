# Модуль `environment`

## Обзор

Этот модуль предоставляет классы для создания и управления средами, в которых агенты взаимодействуют друг с другом и внешними сущностями.  Он определяет базовый класс `TinyWorld` и специализированный подкласс `TinySocialNetwork` для моделирования социальных сетей.  Модуль включает методы для добавления, удаления агентов, управления временем симуляции, отправки сообщений и обработки взаимодействий между агентами.

## Оглавление

- [Модуль `environment`](#модуль-environment)
- [Обзор](#обзор)
- [Класс `TinyWorld`](#класс-tinyworld)
    - [`__init__`](#__init__)
    - [`_step`](#_step)
    - [`_advance_datetime`](#_advance_datetime)
    - [`run`](#run)
    - [`skip`](#skip)
    - [`run_minutes`](#run_minutes)
    - [`skip_minutes`](#skip_minutes)
    - [`run_hours`](#run_hours)
    - [`skip_hours`](#skip_hours)
    - [`run_days`](#run_days)
    - [`skip_days`](#skip_days)
    - [`run_weeks`](#run_weeks)
    - [`skip_weeks`](#skip_weeks)
    - [`run_months`](#run_months)
    - [`skip_months`](#skip_months)
    - [`run_years`](#run_years)
    - [`skip_years`](#skip_years)
    - [`add_agents`](#add_agents)
    - [`add_agent`](#add_agent)
    - [`remove_agent`](#remove_agent)
    - [`remove_all_agents`](#remove_all_agents)
    - [`get_agent_by_name`](#get_agent_by_name)
    - [`_handle_actions`](#_handle_actions)
    - [`_handle_reach_out`](#_handle_reach_out)
    - [`_handle_talk`](#_handle_talk)
    - [`broadcast`](#broadcast)
    - [`broadcast_thought`](#broadcast_thought)
    - [`broadcast_internal_goal`](#broadcast_internal_goal)
    - [`broadcast_context_change`](#broadcast_context_change)
    - [`make_everyone_accessible`](#make_everyone_accessible)
    - [`_display_communication`](#_display_communication)
    - [`_push_and_display_latest_communication`](#_push_and_display_latest_communication)
    - [`pop_and_display_latest_communications`](#pop_and_display_latest_communications)
    - [`_display`](#_display)
    - [`clear_communications_buffer`](#clear_communications_buffer)
    - [`__repr__`](#__repr__)
    - [`_pretty_step`](#_pretty_step)
    - [`pp_current_interactions`](#pp_current_interactions)
    - [`pretty_current_interactions`](#pretty_current_interactions)
    - [`encode_complete_state`](#encode_complete_state)
    - [`decode_complete_state`](#decode_complete_state)
    - [`add_environment`](#add_environment)
    - [`set_simulation_for_free_environments`](#set_simulation_for_free_environments)
    - [`get_environment_by_name`](#get_environment_by_name)
    - [`clear_environments`](#clear_environments)
- [Класс `TinySocialNetwork`](#класс-tinysocialnetwork)
    - [`__init__`](#__init-1)
    - [`add_relation`](#add_relation)
    - [`_update_agents_contexts`](#_update_agents_contexts)
    - [`_step`](#_step-1)
    - [`_handle_reach_out`](#_handle_reach_out-1)
    - [`is_in_relation_with`](#is_in_relation_with)


## Класс `TinyWorld`

**Описание**: Базовый класс для окружений. Предназначен для определения мира, в котором агенты взаимодействуют друг с другом и внешними сущностями.

### `__init__`

**Описание**: Инициализирует окружение.

**Параметры**:
- `name` (str): Имя окружения.
- `agents` (list): Список агентов, добавляемых в окружение.
- `initial_datetime` (datetime): Начальная дата и время окружения. По умолчанию - текущее время.
- `broadcast_if_no_target` (bool): Если True, действия транслируются, если целевой агент не найден.

**Возвращает**:
- `None`


(И другие методы класса TinyWorld с подробными описаниями параметров, возвращаемых значений и исключений)


## Класс `TinySocialNetwork`

**Описание**:  Специализированное окружение для моделирования социальных сетей.

### `__init__`

**Описание**: Создает новое окружение `TinySocialNetwork`.

**Параметры**:
- `name` (str): Имя окружения.
- `broadcast_if_no_target` (bool): Если True, действия транслируются, если целевой агент не найден.


### `add_relation`

**Описание**: Добавляет отношение между двумя агентами.

**Параметры**:
- `agent_1` (TinyPerson): Первый агент.
- `agent_2` (TinyPerson): Второй агент.
- `name` (str): Имя отношения.


(И другие методы класса TinySocialNetwork с подробными описаниями параметров, возвращаемых значений и исключений)