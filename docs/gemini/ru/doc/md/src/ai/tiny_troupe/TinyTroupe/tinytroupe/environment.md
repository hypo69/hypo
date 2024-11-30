# Модуль `environment`

## Обзор

Данный модуль предоставляет базовый класс `TinyWorld` для создания и управления средами, в которых взаимодействуют агенты. Он позволяет определять время, добавлять агентов, обрабатывать их действия и осуществлять коммуникацию между агентами. Модуль также содержит вспомогательные методы для управления списком всех созданных сред и вывода сообщений в консоль.

## Оглавление

- [TinyWorld](#tinyworld)
- [TinySocialNetwork](#tinysocialnetwork)


## Классы

### `TinyWorld`

**Описание**: Базовый класс для определения сред взаимодействия агентов. Хранит информацию о текущих агентах, временной отметке и позволяет управлять действиями агентов.

**Методы**:

- [`__init__`](#init): Инициализирует среду.
- [`_step`](#step): Выполняет один шаг симуляции в среде.
- [`run`](#run): Запускает симуляцию на заданное количество шагов.
- [`skip`](#skip): Пропускает заданное количество шагов симуляции, не выполняя действий агентов.
- [`run_minutes`](#run_minutes): Запускает симуляцию на заданное количество минут.
- [`skip_minutes`](#skip_minutes): Пропускает заданное количество минут симуляции.
- [`run_hours`](#run_hours): Запускает симуляцию на заданное количество часов.
- [`skip_hours`](#skip_hours): Пропускает заданное количество часов симуляции.
- [`run_days`](#run_days): Запускает симуляцию на заданное количество дней.
- [`skip_days`](#skip_days): Пропускает заданное количество дней симуляции.
- [`run_weeks`](#run_weeks): Запускает симуляцию на заданное количество недель.
- [`skip_weeks`](#skip_weeks): Пропускает заданное количество недель симуляции.
- [`run_months`](#run_months): Запускает симуляцию на заданное количество месяцев.
- [`skip_months`](#skip_months): Пропускает заданное количество месяцев симуляции.
- [`run_years`](#run_years): Запускает симуляцию на заданное количество лет.
- [`skip_years`](#skip_years): Пропускает заданное количество лет симуляции.
- [`add_agents`](#add_agents): Добавляет список агентов в среду.
- [`add_agent`](#add_agent): Добавляет одного агента в среду.
- [`remove_agent`](#remove_agent): Удаляет агента из среды.
- [`remove_all_agents`](#remove_all_agents): Удаляет всех агентов из среды.
- [`get_agent_by_name`](#get_agent_by_name): Возвращает агента по имени.
- [`_handle_actions`](#handle_actions): Обрабатывает действия агентов в среде.
- [`_handle_reach_out`](#handle_reach_out): Обрабатывает действие "REACH_OUT".
- [`_handle_talk`](#handle_talk): Обрабатывает действие "TALK".
- [`broadcast`](#broadcast): Передает сообщение всем агентам в среде.
- [`broadcast_thought`](#broadcast_thought): Передает мысль всем агентам в среде.
- [`broadcast_internal_goal`](#broadcast_internal_goal): Передает внутреннюю цель всем агентам в среде.
- [`broadcast_context_change`](#broadcast_context_change): Передает изменение контекста всем агентам в среде.
- [`make_everyone_accessible`](#make_everyone_accessible): Делает всех агентов доступными друг для друга.
- [`_display_communication`](#display_communication): Отображает текущую коммуникацию и сохраняет ее в буфере.
- [`_push_and_display_latest_communication`](#push_and_display_latest_communication): Добавляет сообщения в буфер и отображает их.
- [`pop_and_display_latest_communications`](#pop_and_display_latest_communications): Извлекает сообщения из буфера и отображает их.
- [`_display`](#display): Отображает сообщение в консоли.
- [`clear_communications_buffer`](#clear_communications_buffer): Очищает буфер коммуникаций.
- [`encode_complete_state`](#encode_complete_state): Кодирует полное состояние среды в словарь.
- [`decode_complete_state`](#decode_complete_state): Декодирует полное состояние среды из словаря.
- [`add_environment`](#add_environment): Добавляет среду в список всех сред.
- [`set_simulation_for_free_environments`](#set_simulation_for_free_environments): Устанавливает симуляцию для свободных сред.
- [`get_environment_by_name`](#get_environment_by_name): Возвращает среду по имени.
- [`clear_environments`](#clear_environments): Очищает список всех сред.
- [`__repr__`](#repr): Возвращает строковое представление объекта среды.
- [`_pretty_step`](#pretty_step): Создает отформатированную строку для отображения шага симуляции.
- [`pp_current_interactions`](#pp_current_interactions): Красиво выводит текущие взаимодействия агентов в среде.
- [`pretty_current_interactions`](#pretty_current_interactions): Возвращает красивую строку с текущими взаимодействиями агентов в среде.


### `TinySocialNetwork`

**Описание**: Наследуется от `TinyWorld`, добавляя возможности для управления социальными связями между агентами.

**Методы**:

- [`__init__`](#init): Инициализирует социальную сеть.
- [`add_relation`](#add_relation): Добавляет связь между двумя агентами.
- [`_update_agents_contexts`](#update_agents_contexts): Обновляет контексты агентов, учитывая связи.
- [`_step`](#step): Переопределяет метод `_step` для обновления контекстов агентов.
- [`_handle_reach_out`](#handle_reach_out): Переопределяет метод `_handle_reach_out` для учета связей.
- [`is_in_relation_with`](#is_in_relation_with): Проверяет наличие связи между двумя агентами.



```

**(В следующих разделах будут подробные описания для каждого метода, включая аргументы, возвращаемые значения и исключения.)**