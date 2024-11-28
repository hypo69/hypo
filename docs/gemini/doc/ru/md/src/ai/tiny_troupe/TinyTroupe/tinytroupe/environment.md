# Модуль `environment.py`

## Обзор

Этот модуль предоставляет классы для создания и управления средами взаимодействия агентов, таких как `TinyPerson` в рамках `TinyTroupe`. Он позволяет определять и управлять временем симуляции, обрабатывать действия агентов, управлять списками агентов и осуществлять взаимодействие агентов через методы вещания.

## Оглавление

* [Модуль `environment.py`](#модуль-environmentpy)
* [Класс `TinyWorld`](#класс-tinyworld)
    * [Метод `__init__`](#метод-init)
    * [Метод `_step`](#метод-step)
    * [Метод `_advance_datetime`](#метод-advance_datetime)
    * [Метод `run`](#метод-run)
    * [Метод `skip`](#метод-skip)
    * [Методы `run_*`, `skip_*` (минуты, часы, дни, недели, месяцы, годы)](#методы-run-skip-минуты-часы-дни-недели-месяцы-годы)
    * [Метод `add_agents`](#метод-add_agents)
    * [Метод `add_agent`](#метод-add_agent)
    * [Метод `remove_agent`](#метод-remove_agent)
    * [Метод `remove_all_agents`](#метод-remove_all_agents)
    * [Метод `get_agent_by_name`](#метод-get_agent_by_name)
    * [Метод `_handle_actions`](#метод-handle_actions)
    * [Метод `_handle_reach_out`](#метод-handle_reach_out)
    * [Метод `_handle_talk`](#метод-handle_talk)
    * [Метод `broadcast`](#метод-broadcast)
    * [Метод `broadcast_thought`](#метод-broadcast_thought)
    * [Метод `broadcast_internal_goal`](#метод-broadcast_internal_goal)
    * [Метод `broadcast_context_change`](#метод-broadcast_context_change)
    * [Метод `make_everyone_accessible`](#метод-make_everyone_accessible)
    * [Метод `_display_communication`](#метод-display_communication)
    * [Метод `_push_and_display_latest_communication`](#метод-push_and_display_latest_communication)
    * [Метод `pop_and_display_latest_communications`](#метод-pop_and_display_latest_communications)
    * [Метод `_display`](#метод-display)
    * [Метод `clear_communications_buffer`](#метод-clear_communications_buffer)
    * [Метод `__repr__`](#метод-repr)
    * [Метод `_pretty_step`](#метод-pretty_step)
    * [Метод `pp_current_interactions`](#метод-pp_current_interactions)
    * [Метод `pretty_current_interactions`](#метод-pretty_current_interactions)
    * [Метод `encode_complete_state`](#метод-encode_complete_state)
    * [Метод `decode_complete_state`](#метод-decode_complete_state)
    * [Статический метод `add_environment`](#статический-метод-add_environment)
    * [Статический метод `set_simulation_for_free_environments`](#статический-метод-set_simulation_for_free_environments)
    * [Статический метод `get_environment_by_name`](#статический-метод-get_environment_by_name)
    * [Статический метод `clear_environments`](#статический-метод-clear_environments)
* [Класс `TinySocialNetwork`](#класс-tinysocialnetwork)
    * [Метод `__init__`](#метод-init-tinySocialNetwork)
    * [Метод `add_relation`](#метод-add_relation)
    * [Метод `_update_agents_contexts`](#метод-update_agents_contexts)
    * [Метод `_step` (переопределенный)](#метод-step-переопределенный)
    * [Метод `_handle_reach_out` (переопределенный)](#метод-handle_reach_out-переопределенный)
    * [Метод `is_in_relation_with`](#метод-is_in_relation_with)


## Классы

### `TinyWorld`

**Описание**: Базовый класс для окружений.  Представляет собой основу для создания симуляционных сред, в которых агенты взаимодействуют друг с другом и с внешними сущностями.

### `TinySocialNetwork`

**Описание**: Наследуется от `TinyWorld` и добавляет поддержку социальных отношений между агентами.


## Функции

(Здесь будут описаны статические методы, если они есть)


**(Подробные описания методов см. в соответствующих разделах выше)**