# Модуль tinytroupe.agent

## Обзор

Данный модуль предоставляет основные классы и функции для агентов TinyTroupe. Агенты представляют собой имитацию людей или сущностей, способных взаимодействовать с другими агентами и окружающей средой, получая стимулы и производя действия. Агенты имеют когнитивные состояния, которые обновляются в процессе взаимодействия с окружающей средой и другими агентами. Они могут хранить и извлекать информацию из памяти и выполнять действия в среде.  В отличие от агентов, цель которых - обеспечить поддержку AI-ассистентов или других инструментов повышения продуктивности, агенты TinyTroupe нацелены на **представление человекоподобного поведения**, включая особенности, эмоции и другие человеческие черты, которые не ожидаются от инструмента продуктивности.

Основой дизайна является когнитивная психология, поэтому агенты имеют различные внутренние когнитивные состояния, такие как внимание, эмоции и цели.  Это также объясняет тонкие внутренние разделения в памяти агентов, в частности, между эпизодической и семантической памятью.  Также присутствуют некоторые концепции бихевиоризма, такие как «стимул» и «ответ» в методах `listen` и `act`, которые являются ключевыми абстракциями для понимания того, как агенты взаимодействуют с окружающей средой и другими агентами.

## Классы

### `TinyPerson`

**Описание**:  Класс, представляющий симулированного человека в вселенной TinyTroupe.  Он является основой для взаимодействия агентов с окружающей средой и друг с другом.

**Атрибуты**:

- `name` (str): Имя TinyPerson.
- `episodic_memory` (объект `EpisodicMemory`, по умолчанию `EpisodicMemory()`): Реализация эпизодической памяти.
- `semantic_memory` (объект `SemanticMemory`, по умолчанию `SemanticMemory()`): Реализация семантической памяти.
- `_mental_faculties` (list, по умолчанию None): Список ментальных способностей агента.


**Методы**:

- `__init__(self, name: str=None, episodic_memory=None, semantic_memory=None, mental_faculties: list=None)`: Инициализирует TinyPerson.
- `_post_init(self, **kwargs)`: Метод, вызываемый после `__init__`, используется для дополнительной инициализации, например, после десериализации.
- `generate_agent_prompt(self)`: Генерирует подсказку для агента.
- `reset_prompt(self)`: Сбрасывает подсказку для агента.
- `get(self, key)`: Возвращает значение ключа из конфигурации агента.
- `define(self, key, value, group=None)`: Определяет значение в конфигурации агента.
- `define_several(self, group, records)`: Определяет несколько значений в конфигурации агента для заданной группы.
- `define_relationships(self, relationships, replace=True)`: Определяет или обновляет отношения между агентами.
- `clear_relationships(self)`: Очищает список отношений.
- `related_to(self, other_agent, description, symmetric_description=None)`: Определяет взаимоотношение между этим агентом и другим агентом.
- `add_mental_faculties(self, mental_faculties)`: Добавляет список ментальных способностей к агенту.
- `add_mental_faculty(self, faculty)`: Добавляет ментальную способность к агенту.
- `act(self, until_done=True, n=None, return_actions=False, max_content_length=...)`: Действует в среде и обновляет внутреннее когнитивное состояние.
- `listen(self, speech, source: AgentOrWorld = None, max_content_length=...)`: Слушает другого агента.
- `socialize(self, social_description, source: AgentOrWorld = None, max_content_length=...)`: Воспринимает социальный стимул по описанию.
- `see(self, visual_description, source: AgentOrWorld = None, max_content_length=...)`: Воспринимает визуальный стимул по описанию.
- `think(self, thought, max_content_length=...)`: Заставляет агента подумать о чем-то.
- `internalize_goal(self, goal, max_content_length=...)`: Внутренне интегрирует цель.
- `_observe(self, stimulus, max_content_length=...)`: Метод обработки стимулов.
- `listen_and_act(self, speech, return_actions=False, max_content_length=...)`: Удобный метод, объединяющий методы `listen` и `act`.
- `see_and_act(self, visual_description, return_actions=False, max_content_length=...)`: Удобный метод, объединяющий методы `see` и `act`.
- `think_and_act(self, thought, return_actions=False, max_content_length=...)`: Удобный метод, объединяющий методы `think` и `act`.
- `read_documents_from_folder(self, documents_path: str)`: Читает документы из папки.
- `read_documents_from_web(self, web_urls: list)`: Читает документы из веб-ссылок.
- `move_to(self, location, context=[])`: Перемещает агента в новое место.
- `change_context(self, context: list)`: Изменяет контекст агента.
- `make_agent_accessible(self, agent: Self, relation_description: str = ...)`: Делает агента доступным.
- `make_agent_inaccessible(self, agent: Self)`: Делает агента недоступным.
- `make_all_agents_inaccessible(self)`: Делает всех агентов недоступными.
- `_produce_message(self)`: Создает сообщение для отправки в OpenAI.
- `_update_cognitive_state(self, goals=None, context=None, attention=None, emotions=None)`: Обновляет когнитивное состояние.
- `_display_communication(...)`: Отображает коммуникацию.
- `_push_and_display_latest_communication(self, rendering)`: Выводит текущую коммуникацию на консоль и добавляет ее в буфер.
- `pop_and_display_latest_communications(self)`: Выводит накопленные сообщения из буфера и очищает его.
- `clear_communications_buffer(self)`: Очищает буфер коммуникаций.
- `pop_latest_actions(self) -> list`: Возвращает последние действия агента.
- `pop_actions_and_get_contents_for(self, action_type: str, only_last_action: bool = True) -> list`: Возвращает содержание действий заданного типа.
- `__repr__(self)`: Возвращает строковое представление объекта.
- `minibio(self)`: Возвращает краткую биографию агента.
- `pp_current_interactions(...)`: Выводит текущие взаимодействия в читаемом формате.
- `pretty_current_interactions(...)`: Возвращает строку с текущими взаимодействиями в читаемом формате.
- `_pretty_stimuli(...)`: Возвращает отформатированное представление стимулов.
- `_pretty_action(...)`: Возвращает отформатированное представление действия.
- `_pretty_timestamp(...)`: Возвращает отформатированное представление временной метки.
- `iso_datetime(self) -> str`: Возвращает текущее время в формате ISO, если среда определена.
- `save_spec(self, path, include_mental_faculties=True, include_memory=False)`: Сохраняет текущую конфигурацию в JSON-файл.
- `load_spec(path, suppress_mental_faculties=False, suppress_memory=False, auto_rename_agent=False, new_agent_name=None)`: Загружает JSON-спецификацию агента.
- `encode_complete_state(self) -> dict`: Кодирует полное состояние TinyPerson для сериализации.
- `decode_complete_state(self, state: dict) -> Self`: Восстанавливает TinyPerson из закодированного состояния.
- `create_new_agent_from_current_spec(self, new_name: str) -> Self`: Создает нового агента на основе текущей спецификации.
- `add_agent(agent)`: Добавляет агента в глобальный список агентов.
- `has_agent(agent_name: str)`: Проверяет наличие агента по имени.
- `set_simulation_for_free_agents(simulation)`: Устанавливает симуляцию для свободных агентов.
- `get_agent_by_name(name)`: Возвращает агента по имени.
- `clear_agents()`: Очищает глобальный список агентов.


### `TinyMentalFaculty`

**Описание**: Базовый класс для ментальных способностей агента.

**Методы**:
- `__init__(self, name: str, requires_faculties: list=None)`: Инициализирует ментальную способность.
- `process_action(self, agent, action: dict) -> bool`: Обрабатывает действие, связанное с этой способностью.
- `actions_definitions_prompt(self) -> str`: Возвращает prompt для определения действий.
- `actions_constraints_prompt(self) -> str`: Возвращает prompt для определения ограничений на действия.


### `RecallFaculty`
### `FilesAndWebGroundingFaculty`
### `TinyToolUse`
### `TinyMemory`
### `EpisodicMemory`
### `SemanticMemory`

**Описание**:  Классы, реализующие различные типы памяти.

**Методы**: Каждый из классов имеет методы `store`, `retrieve`, `retrieve_recent`, `retrieve_all`, `retrieve_relevant` с различными функциональными особенностями.  Подробные описания этих методов содержатся в коде.


## Функции

###  `utils.read_config_file()`


**Описание**: Читает файл конфигурации.

**Возвращает**: Словарь с настройками конфигурации.


##  `default`

**Описание**: Словарь с параметрами по умолчанию.


##  `OpenAIEmbedding`


**Описание**: Определяет встраивание OpenAI.

**Методы**:  Подробные описания методов содержатся в коде.


##  `Settings.embed_model`


**Описание**: Настройка модели встраивания.



Этот раздел содержит подробные описания для остальных классов и функций, которые требуют более подробного раскрытия.  Для этого можно использовать Markdown с дополнительными уровнями заголовков.