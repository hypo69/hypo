# Модуль `tinytroupe.agent`

## Обзор

Данный модуль предоставляет основные классы и функции для агентов TinyTroupe. Агенты являются ключевым абстракцией в TinyTroupe.  Агент — это симулированный человек или сущность, которая может взаимодействовать с другими агентами и окружением, получая стимулы и производя действия. Агенты имеют когнитивные состояния, которые обновляются по мере взаимодействия с окружением и другими агентами. Агенты также могут хранить и извлекать информацию из памяти и выполнять действия в окружении. В отличие от агентов, чья цель — предоставить поддержку для ИИ-ассистентов или других инструментов повышения продуктивности, агенты TinyTroupe нацелены на представление человекоподобного поведения, которое включает особенности, эмоции и другие человеческие черты, которых не следует ожидать от инструмента повышения продуктивности.

Основной дизайн вдохновлен когнитивной психологией, поэтому у агентов есть различные внутренние когнитивные состояния, такие как внимание, эмоции и цели.  Также именно поэтому память агента, в отличие от других платформ агентов на базе больших языковых моделей, имеет тонкие внутренние разделения, особенно между эпизодической и семантической памятью.  Также присутствуют некоторые концепции бихевиоризма, такие как понятие «стимула» и «отклика» в методах `listen` и `act`, которые являются ключевыми абстракциями для понимания того, как агенты взаимодействуют с окружением и другими агентами.

## Классы

### `TinyPerson`

**Описание**: Симулированный человек во вселенной TinyTroupe.

**Атрибуты**:

* `name` (str): Имя TinyPerson.
* `episodic_memory` (object): Реализация памяти (по умолчанию `EpisodicMemory`).
* `semantic_memory` (object): Реализация семантической памяти (по умолчанию `SemanticMemory`).
* `_mental_faculties` (list): Список когнитивных способностей агента.
* `_configuration` (dict): Настройки агента.


**Методы**:

- `__init__(self, name: str = None, episodic_memory=None, semantic_memory=None, mental_faculties: list = None)`: Создает объект `TinyPerson`.
    * `name` (str): Имя TinyPerson. Требуется.
    * `episodic_memory` (object, optional): Реализация эпизодической памяти.
    * `semantic_memory` (object, optional): Реализация семантической памяти.
    * `mental_faculties` (list, optional): Список когнитивных способностей.
- `_post_init(self, **kwargs)`: Метод, вызываемый после инициализации (`__init__`)
- `generate_agent_prompt(self)`: Генерирует запрос для агента.
- `reset_prompt(self)`: Сбрасывает запрос для агента.
- `get(self, key)`: Возвращает значение ключа из конфигурации.
- `define(self, key, value, group=None)`: Определяет значение для ключа в конфигурации.
- `define_several(self, group, records)`: Определяет несколько значений для ключей в группе конфигурации.
- `define_relationships(self, relationships, replace=True)`: Определяет или обновляет отношения агента.
- `clear_relationships(self)`: Очищает отношения агента.
- `related_to(self, other_agent, description, symmetric_description=None)`: Определяет отношение между агентами.
- `add_mental_faculties(self, mental_faculties)`: Добавляет список когнитивных способностей.
- `add_mental_faculty(self, faculty)`: Добавляет одну когнитивную способность.
- `act(self, until_done=True, n=None, return_actions=False, max_content_length=default["max_content_display_length"])`: Выполняет действия в окружении.
- `listen(self, speech, source: AgentOrWorld = None, max_content_length=default["max_content_display_length"])`: Слушает другого агента.
- `socialize(self, social_description: str, source: AgentOrWorld = None, max_content_length=default["max_content_display_length"])`: Обрабатывает социальный стимул.
- `see(self, visual_description, source: AgentOrWorld = None, max_content_length=default["max_content_display_length"])`: Обрабатывает визуальный стимул.
- `think(self, thought, max_content_length=default["max_content_display_length"])`: Заставляет агента думать о чем-то.
- `internalize_goal(self, goal, max_content_length=default["max_content_display_length"])`: Внутреннее понимание цели.
- `_observe(self, stimulus, max_content_length=default["max_content_display_length"])`: Наблюдение стимула.
- `listen_and_act(self, speech, return_actions=False, max_content_length=default["max_content_display_length"])`: Объединение `listen` и `act`.
- `see_and_act(self, visual_description, return_actions=False, max_content_length=default["max_content_display_length"])`: Объединение `see` и `act`.
- `think_and_act(self, thought, return_actions=False, max_content_length=default["max_content_display_length"])`: Объединение `think` и `act`.
- `read_documents_from_folder(self, documents_path: str)`: Читает документы из папки.
- `read_documents_from_web(self, web_urls: list)`: Читает документы из веб-ссылок.
- `move_to(self, location, context=[])`: Перемещение в новое место.
- `change_context(self, context: list)`: Изменение контекста.
- `make_agent_accessible(self, agent: Self, relation_description: str = "An agent I can currently interact with.")`: Делает агента доступным.
- `make_agent_inaccessible(self, agent: Self)`: Делает агента недоступным.
- `make_all_agents_inaccessible(self)`: Делает всех агентов недоступными.
- `_produce_message(self)`: Генерирует ответ от агента.
- `_update_cognitive_state(self, goals=None, context=None, attention=None, emotions=None)`: Обновляет когнитивное состояние агента.
- `_display_communication(self, role, content, kind, simplified=True, max_content_length=default["max_content_display_length"])`: Отображение коммуникации.
- `_push_and_display_latest_communication(self, rendering)`: Добавляет коммуникацию в буфер и отображает её.
- `pop_and_display_latest_communications(self)`: Извлекает и отображает сообщения из буфера.
- `clear_communications_buffer(self)`: Очищает буфер коммуникации.
- `pop_latest_actions(self) -> list`: Возвращает последние действия агента.
- `pop_actions_and_get_contents_for(self, action_type: str, only_last_action: bool = True) -> list`: Возвращает содержимое действий определённого типа.
- `__repr__(self)`: Строковое представление объекта.
- `minibio(self)`: Возвращает краткую биографию.
- `pp_current_interactions(self, simplified=True, skip_system=True, max_content_length=default["max_content_display_length"])`: Отображение текущих взаимодействий.
- `pretty_current_interactions(self, simplified=True, skip_system=True, max_content_length=default["max_content_display_length"])`: Возвращает строку с текущими взаимодействиями в читаемом формате.
- `_pretty_stimuli(self, role, content, simplified=True, max_content_length=default["max_content_display_length"])`: Отображение стимулов.
- `_pretty_action(self, role, content, simplified=True, max_content_length=default["max_content_display_length"])`: Отображение действия.
- `_pretty_timestamp(self, role, timestamp)`: Отображение временной метки.
- `iso_datetime(self) -> str`: Возвращает текущую дату и время среды, если таковая имеется.
- `save_spec(self, path, include_mental_faculties=True, include_memory=False)`: Сохранение конфигурации.
- `load_spec(self, path, suppress_mental_faculties=False, suppress_memory=False, auto_rename_agent=False, new_agent_name=None)`: Загрузка конфигурации.
- `encode_complete_state(self) -> dict`: Кодирует полное состояние TinyPerson.
- `decode_complete_state(self, state: dict) -> Self`: Восстанавливает полное состояние TinyPerson.
- `create_new_agent_from_current_spec(self, new_name: str) -> Self`: Создает нового агента на основе текущего.
- `add_agent(agent)`: Добавление агента в глобальный список.
- `has_agent(agent_name: str)`: Проверка наличия агента.
- `set_simulation_for_free_agents(simulation)`: Установка симуляции для свободных агентов.
- `get_agent_by_name(name)`: Получение агента по имени.
- `clear_agents()`: Очистка глобального списка агентов.


### `TinyMentalFaculty`

**Описание**: Представляет когнитивную способность агента.

**Методы**:
- `__init__(self, name: str, requires_faculties: list = None)`: Инициализация когнитивной способности.
- `__str__(self)`: Строковое представление.
- `__eq__(self, other)`: Операция сравнения.
- `process_action(self, agent, action: dict) -> bool`: Обработка действия.
- `actions_definitions_prompt(self) -> str`:  Получение подсказки для определения действий.
- `actions_constraints_prompt(self) -> str`:  Получение подсказки для ограничений на действия.



### `RecallFaculty`

**Описание**: Когнитивная способность агента, связанная с извлечением информации из памяти.


### `FilesAndWebGroundingFaculty`

**Описание**: Когнитивная способность агента, позволяющая получать информацию из локальных файлов и веб-страниц.

### `TinyToolUse`


### `TinyMemory`

**Описание**: Базовый класс для разных типов памяти.

### `EpisodicMemory`

**Описание**: Предоставляет возможности эпизодической памяти агенту.

### `SemanticMemory`

**Описание**: Предоставляет возможности семантической памяти.

## Функции

(Список функций приведён в коде и их описания взяты из комментариев)


## Операции

(Описание операций, если имеются)