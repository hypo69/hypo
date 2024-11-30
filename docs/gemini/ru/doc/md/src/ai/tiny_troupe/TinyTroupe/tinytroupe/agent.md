# Модуль `tinytroupe.agent`

## Обзор

Этот модуль предоставляет основные классы и функции для агентов TinyTroupe. Агенты — ключевая абстракция в TinyTroupe. Это моделируемые люди или сущности, которые могут взаимодействовать с другими агентами и окружением, получая стимулы и производя действия. У агентов есть внутреннее состояние, которое обновляется по мере их взаимодействия с окружением и другими агентами. Агенты также могут хранить и извлекать информацию из памяти и выполнять действия в окружении. В отличие от агентов, цель которых — предоставить поддержку для AI-ассистентов или других инструментов повышения производительности, **агенты TinyTroupe нацелены на представление человеческого поведения**, которое включает особенности, эмоции и другие человеческие черты, которых нельзя ожидать от инструмента повышения производительности.

Основной дизайн вдохновлен главным образом когнитивной психологией, поэтому агенты имеют различные внутренние когнитивные состояния, такие как внимание, эмоции и цели.  Это также объясняет, почему память агента, в отличие от других платформ агентов на основе LLMs, имеет тонкие внутренние разделения, в частности между эпизодической и семантической памятью. Некоторые концепции бихевиоризма также присутствуют, такие как идея «стимула» и «отклика» в методах `listen` и `act`, которые являются ключевыми абстракциями для понимания того, как агенты взаимодействуют с окружением и другими агентами.


## Классы

### `TinyPerson`

**Описание**: Моделирует человека в вселенной TinyTroupe.

**Атрибуты**:

* `name` (str): Имя TinyPerson. Нужно указать либо его, либо `spec_path`.
* `episodic_memory` (EpisodicMemory, optional): Реализация памяти. По умолчанию `EpisodicMemory()`.
* `semantic_memory` (SemanticMemory, optional): Реализация семантической памяти. По умолчанию `SemanticMemory()`.
* `_mental_faculties` (list, optional): Список ментальных способностей агента. По умолчанию `None`.
* `_configuration` (dict): Словарь конфигурации агента.

**Методы**:

* `__init__(self, name: str=None, episodic_memory=None, semantic_memory=None, mental_faculties: list=None)`: Создает экземпляр `TinyPerson`.
* `_post_init(self, **kwargs)`: Метод, вызываемый после `__init__`. Используется для настройки параметров агента по умолчанию.
* `generate_agent_prompt(self)`: Генерирует запрос для агента.
* `reset_prompt(self)`: Сбрасывает внутренний запрос агента.
* `get(self, key)`: Возвращает значение параметра в конфигурации.
* `define(self, key, value, group=None)`: Определяет значение для параметра в конфигурации.
* `define_several(self, group, records)`: Определяет несколько значений в конфигурации для одной группы.
* `define_relationships(self, relationships, replace=True)`: Определяет или обновляет отношения TinyPerson.
* `clear_relationships(self)`: Очищает отношения TinyPerson.
* `related_to(self, other_agent, description, symmetric_description=None)`: Определяет отношения между агентами.
* `add_mental_faculties(self, mental_faculties)`: Добавляет список ментальных способностей агенту.
* `add_mental_faculty(self, faculty)`: Добавляет ментальную способность агенту.
* `act(self, until_done=True, n=None, return_actions=False, max_content_length=default["max_content_display_length"])`: Выполняет действия в среде.
* `listen(self, speech, source: AgentOrWorld = None, max_content_length=default["max_content_display_length"])`: Слушает другого агента.
* `socialize(self, social_description, source: AgentOrWorld = None, max_content_length=default["max_content_display_length"])`: Воспринимает социальный стимул.
* `see(self, visual_description, source: AgentOrWorld = None, max_content_length=default["max_content_display_length"])`: Воспринимает визуальный стимул.
* `think(self, thought, max_content_length=default["max_content_display_length"])`: Заставляет агента думать о чем-то.
* `internalize_goal(self, goal, max_content_length=default["max_content_display_length"])`: Внутреннее усвоение цели.
* `_observe(self, stimulus, max_content_length=default["max_content_display_length"])`: Общий метод для обработки различных типов стимулов.
* `listen_and_act(self, speech, return_actions=False, max_content_length=default["max_content_display_length"])`: Сочетает `listen` и `act`.
* `see_and_act(self, visual_description, return_actions=False, max_content_length=default["max_content_display_length"])`: Сочетает `see` и `act`.
* `think_and_act(self, thought, return_actions=False, max_content_length=default["max_content_display_length"])`: Сочетает `think` и `act`.
* `read_documents_from_folder(self, documents_path: str)`: Читает документы из папки и загружает их в семантическую память.
* `read_documents_from_web(self, web_urls: list)`: Читает документы с веб-страниц и загружает их в семантическую память.
* `move_to(self, location, context=[])`: Перемещает агента в новое место.
* `change_context(self, context: list)`: Изменяет контекст агента.
* `make_agent_accessible(self, agent: Self, relation_description: str = "An agent I can currently interact with.")`: Делает агента доступным.
* `make_agent_inaccessible(self, agent: Self)`: Делает агента недоступным.
* `make_all_agents_inaccessible(self)`: Делает всех агентов недоступными.
* `_produce_message(self)`: Используется для отправки сообщений в OpenAI API.
* `_update_cognitive_state(self, goals=None, context=None, attention=None, emotions=None)`: Обновляет когнитивное состояние TinyPerson.
* `_display_communication(self, role, content, kind, simplified=True, max_content_length=default["max_content_display_length"])`: Отображает коммуникацию.
* `_push_and_display_latest_communication(self, rendering)`: Отправляет коммуникацию в буфер и отображает ее.
* `pop_and_display_latest_communications(self)`: Возвращает и отображает сообщения из буфера.
* `clear_communications_buffer(self)`: Очищает буфер коммуникаций.
* `pop_latest_actions(self) -> list`: Возвращает последние действия агента.
* `pop_actions_and_get_contents_for(self, action_type: str, only_last_action: bool = True) -> list`: Возвращает содержимое действий определенного типа.
* `__repr__(self)`: Строковое представление TinyPerson.
* `minibio(self)`: Возвращает мини-биографию TinyPerson.
* `pp_current_interactions(self, simplified=True, skip_system=True, max_content_length=default["max_content_display_length"])`: Отображает текущие взаимодействия в формате `Rich`.
* `pretty_current_interactions(self, simplified=True, skip_system=True, max_content_length=default["max_content_display_length"], first_n=None, last_n=None, include_omission_info:bool=True)`: Возвращает строку с текущими взаимодействиями.
* `_pretty_stimuli(self, role, content, simplified=True, max_content_length=default["max_content_display_length"])`: Отображает стимулы.
* `_pretty_action(self, role, content, simplified=True, max_content_length=default["max_content_display_length"])`: Отображает действие.
* `_pretty_timestamp(self, role, timestamp)`: Отображает отметку времени.
* `iso_datetime(self)`: Возвращает текущую дату и время среды в формате ISO.
* `save_spec(self, path, include_mental_faculties=True, include_memory=False)`: Сохраняет текущую конфигурацию в JSON-файл.
* `load_spec(self, path, suppress_mental_faculties=False, suppress_memory=False, auto_rename_agent=False, new_agent_name=None)`: Загружает JSON-спецификацию агента.
* `encode_complete_state(self) -> dict`: Кодирует полное состояние TinyPerson для сериализации.
* `decode_complete_state(self, state: dict) -> Self`: Восстанавливает полное состояние TinyPerson из сериализованного словаря.
* `create_new_agent_from_current_spec(self, new_name: str) -> Self`: Создает нового агента из спецификации текущего агента.
* `add_agent(self, agent)`: Добавляет агента в глобальный список агентов.
* `has_agent(agent_name: str)`: Проверяет, зарегистрирован ли агент.
* `set_simulation_for_free_agents(simulation)`: Устанавливает симуляцию для свободных агентов.
* `get_agent_by_name(name)`: Возвращает агента по имени.
* `clear_agents()`: Очищает глобальный список агентов.

### `TinyMentalFaculty`

**Описание**: Представляет ментальную способность агента.

**Методы**:

* `__init__(self, name: str, requires_faculties: list=None)`: Инициализирует ментальную способность.
* `process_action(self, agent, action: dict) -> bool`: Обрабатывает действие, связанное с этой способностью.
* `actions_definitions_prompt(self) -> str`: Возвращает запрос для определения действий, связанных с этой способностью.
* `actions_constraints_prompt(self) -> str`: Возвращает запрос для определения ограничений на действия, связанные с этой способностью.


### `RecallFaculty`
### `FilesAndWebGroundingFaculty`
### `TinyToolUse`
### `TinyMemory`
### `EpisodicMemory`
### `SemanticMemory`

(Подробные описания для других классов и методов аналогичным образом можно сгенерировать, используя описанные выше принципы)


## Функции

(Список функций и их описания)