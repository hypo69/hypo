# Модуль `tinytroupe.agent`

## Обзор

Этот модуль предоставляет основные классы и функции для агентов TinyTroupe. Агенты – это ключевая абстракция в TinyTroupe, имитирующие людей или сущности, способные взаимодействовать с другими агентами и окружением, получая стимулы и производя действия. У агентов есть когнитивные состояния, которые обновляются по мере их взаимодействия с окружением и другими агентами. Агенты также могут хранить и извлекать информацию из памяти и выполнять действия в окружении. В отличие от агентов, цель которых – предоставить поддержку для основанных на ИИ помощников или других подобных инструментах повышения производительности, **агенты TinyTroupe нацелены на представление человеческого поведения**, включая особенности, эмоции и другие человеческие черты, которых нельзя ожидать от инструмента повышения производительности.

Основной дизайн вдохновлен в основном когнитивной психологией, поэтому агенты обладают различными внутренними когнитивными состояниями, такими как внимание, эмоции и цели. Также именно поэтому память агентов, в отличие от других платформ агентов на основе LLMs, имеет тонкие внутренние подразделения, в частности, между эпизодической и семантической памятью. Некоторые концепции бихевиоризма также присутствуют, такие как идея «стимула» и «отклика» в методах `listen` и `act`, которые являются ключевыми абстракциями для понимания того, как агенты взаимодействуют с окружением и другими агентами.

## Классы

### `TinyPerson`

**Описание**: Симулирует человека во вселенной TinyTroupe.

**Атрибуты**:

- `MAX_ACTIONS_BEFORE_DONE`: Максимальное количество действий, которые агент может выполнить до состояния `DONE`.
- `PP_TEXT_WIDTH`: Ширина текста для вывода в консоли.
- `serializable_attributes`: Список атрибутов, которые должны сериализоваться.
- `all_agents`: Словарь, хранящий всех созданных агентов.
- `communication_style`: Стиль общения агентов ("simplified" или "full"). По умолчанию "simplified".
- `communication_display`: Флаг, определяющий отображение коммуникации. По умолчанию True.
- `current_messages`: Список текущих сообщений для взаимодействия.
- `environment`: Текущая среда, в которой действует агент.
- `_actions_buffer`: Буфер действий, которые агент выполнил, но еще не были обработаны средой.
- `_accessible_agents`: Список доступных агентов для взаимодействия.
- `_displayed_communications_buffer`: Буфер отображенных сообщений для последующей обработки.
- `episodic_memory`: Объект класса `EpisodicMemory`, представляющий эпизодическую память агента. По умолчанию создается новый экземпляр.
- `semantic_memory`: Объект класса `SemanticMemory`, представляющий семантическую память агента. По умолчанию создается новый экземпляр.
- `_mental_faculties`: Список ментальных способностей агента. По умолчанию пустой список.
- `_configuration`: Словарь конфигурации агента.
- `_prompt_template_path`: Путь к шаблону запроса для агента.
- `_init_system_message`: Системное сообщение для агента.


**Методы**:

- `__init__(name: str = None, episodic_memory=None, semantic_memory=None, mental_faculties: list = None)`: Создает экземпляр класса `TinyPerson`.
- `_post_init(**kwargs)`: Метод, вызываемый после `__init__` для завершения инициализации.
- `generate_agent_prompt()`: Генерирует запрос для агента на основе шаблона.
- `reset_prompt()`: Сбрасывает запрос для агента.
- `get(key)`: Возвращает значение атрибута `key` из конфигурации.
- `define(key, value, group=None)`: Определяет значение атрибута `key` в конфигурации.
- `define_several(group, records)`: Определяет несколько значений атрибутов в конфигурации.
- `define_relationships(relationships, replace=True)`: Определяет или обновляет отношения агента.
- `clear_relationships()`: Очищает отношения агента.
- `related_to(other_agent, description, symmetric_description=None)`: Определяет отношения между агентом и другим агентом.
- `add_mental_faculties(mental_faculties)`: Добавляет список ментальных способностей.
- `add_mental_faculty(faculty)`: Добавляет ментальную способность.
- `act(until_done=True, n=None, return_actions=False, max_content_length=default["max_content_display_length"])`: Действует в окружении.
- `listen(speech, source=None, max_content_length=default["max_content_display_length"])`: Слушает другого агента.
- `socialize(social_description, source=None, max_content_length=default["max_content_display_length"])`: Обрабатывает социальный стимул.
- `see(visual_description, source=None, max_content_length=default["max_content_display_length"])`: Обрабатывает визуальный стимул.
- `think(thought, max_content_length=default["max_content_display_length"])`: Заставляет агента думать.
- `internalize_goal(goal, max_content_length=default["max_content_display_length"])`: Внутренне обрабатывает цель.
- `_observe(stimulus, max_content_length=default["max_content_display_length"])`: Наблюдает стимул.
- `listen_and_act(speech, return_actions=False, max_content_length=default["max_content_display_length"])`: Комбинирует `listen` и `act`.
- `see_and_act(visual_description, return_actions=False, max_content_length=default["max_content_display_length"])`: Комбинирует `see` и `act`.
- `think_and_act(thought, return_actions=False, max_content_length=default["max_content_display_length"])`: Комбинирует `think` и `act`.
- `read_documents_from_folder(documents_path: str)`: Загружает документы из папки в семантическую память.
- `read_documents_from_web(web_urls: list)`: Загружает документы из веб-ссылок в семантическую память.
- `move_to(location, context=[])`: Перемещает агента в новое место.
- `change_context(context: list)`: Изменяет контекст.
- `make_agent_accessible(agent, relation_description="An agent I can currently interact with.")`: Делает агента доступным.
- `make_agent_inaccessible(agent)`: Делает агента недоступным.
- `make_all_agents_inaccessible()`: Делает всех агентов недоступными.
- `_produce_message()`: Получает сообщение от OpenAI.
- `_update_cognitive_state(goals=None, context=None, attention=None, emotions=None)`: Обновляет когнитивное состояние агента.
- `_display_communication(role, content, kind, simplified=True, max_content_length=default["max_content_display_length"])`: Отображает коммуникацию.
- `_push_and_display_latest_communication(rendering)`: Добавляет сообщение в буфер и отображает его.
- `pop_and_display_latest_communications()`: Извлекает и отображает сообщения из буфера.
- `clear_communications_buffer()`: Очищает буфер сообщений.
- `pop_latest_actions()`: Возвращает список последних действий агента.
- `pop_actions_and_get_contents_for(action_type: str, only_last_action: bool = True)`: Возвращает содержимое действий определенного типа.
- `__repr__()`: Строковое представление класса.
- `minibio()`: Возвращает краткую биографию.
- `pp_current_interactions(simplified=True, skip_system=True, max_content_length=default["max_content_display_length"])`: Красивый вывод текущих взаимодействий.
- `pretty_current_interactions(...)`: Возвращает красивую строку с текущими взаимодействиями.
- `_pretty_stimuli(...)`: Красивый вывод стимулов.
- `_pretty_action(...)`: Красивый вывод действий.
- `_pretty_timestamp(...)`: Красивый вывод временной метки.
- `iso_datetime()`: Возвращает текущую дату и время в формате ISO.
- `save_spec(path, include_mental_faculties=True, include_memory=False)`: Сохраняет конфигурацию в JSON-файл.
- `load_spec(path, suppress_mental_faculties=False, suppress_memory=False, auto_rename_agent=False, new_agent_name=None)`: Загружает конфигурацию из JSON-файла.
- `encode_complete_state()`: Кодирует полное состояние агента для сериализации.
- `decode_complete_state(state: dict) -> Self`: Декодирует полное состояние агента.
- `create_new_agent_from_current_spec(new_name: str) -> Self`: Создает нового агента на основе текущей спецификации.
- `add_agent(agent)`: Добавляет агента в глобальный список.
- `has_agent(agent_name: str)`: Проверяет наличие агента по имени.
- `set_simulation_for_free_agents(simulation)`: Устанавливает симуляцию для свободных агентов.
- `get_agent_by_name(name)`: Возвращает агента по имени.
- `clear_agents()`: Очищает глобальный список агентов.


### `TinyMentalFaculty`

**Описание**: Представляет ментальную способность агента.

**Методы**:

- `__init__(name: str, requires_faculties: list=None)`: Инициализирует ментальную способность.
- `__str__()`: Строковое представление класса.
- `__eq__(other)`: Операция сравнения.
- `process_action(agent, action: dict) -> bool`: Обрабатывает действие, связанное с этой способностью.
- `actions_definitions_prompt()`: Возвращает запрос для определения действий.
- `actions_constraints_prompt()`: Возвращает запрос для определения ограничений на действия.


### `RecallFaculty`
### `FilesAndWebGroundingFaculty`
### `TinyToolUse`
### `TinyMemory`
### `EpisodicMemory`
### `SemanticMemory`


## Функции

### `default`

**Описание**: Словарь с параметрами по умолчанию.

**Использование**: Используется для настройки параметров агентов.


## Содержание (TOC)

[Назад к началу](#модуль-tinytroupe-agent)