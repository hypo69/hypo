# Модуль tinytroupe.agent

## Обзор

Этот модуль предоставляет основные классы и функции для агентов TinyTroupe.

Агенты являются ключевой абстракцией в TinyTroupe. Агент — это симулированный человек или сущность, которая может взаимодействовать с другими агентами и окружением, получая стимулы и производя действия. У агентов есть когнитивные состояния, которые обновляются по мере их взаимодействия с окружением и другими агентами. Агенты также могут хранить и извлекать информацию из памяти и выполнять действия в окружении. В отличие от агентов, цель которых заключается в предоставлении поддержки для основанных на ИИ помощников или других подобных инструментов повышения производительности, **агенты TinyTroupe нацелены на представление человеческого поведения**, которое включает особенности, эмоции и другие человеческие черты, которых нельзя ожидать от инструмента повышения производительности.

Общий базовый дизайн в основном вдохновлен когнитивной психологией, поэтому у агентов есть различные внутренние когнитивные состояния, такие как внимание, эмоции и цели. Также именно поэтому память агентов, в отличие от других платформ агентов на основе ИИ, имеет тонкие внутренние разделения, в частности, между эпизодической и семантической памятью. Некоторые концепции бихевиоризма также присутствуют, например, идея «стимула» и «отклика» в методах `listen` и `act`, которые являются ключевыми абстракциями для понимания того, как агенты взаимодействуют с окружением и другими агентами.

## Параметры по умолчанию

### `default`

Словарь, содержащий значения параметров по умолчанию для различных компонентов, таких как модель встраивания и максимальная длина отображаемого содержимого. Значения извлекаются из файла конфигурации `utils.read_config_file()`.

## Классы

### `TinyPerson`

**Описание**: Симулированный человек во вселенной TinyTroupe. Представляет собой агента, способного взаимодействовать с окружением и другими агентами.

**Атрибуты**:
- `MAX_ACTIONS_BEFORE_DONE`: Максимальное количество действий, которое агент может выполнить до состояния `DONE`.
- `PP_TEXT_WIDTH`: Ширина текста для красивой печати.
- `serializable_attributes`: Список атрибутов, которые должны сериализоваться при сохранении агента.
- `all_agents`: Словарь, содержащий всех агентов, созданных до настоящего момента. Ключ - имя агента.
- `communication_style`: Стиль коммуникации для всех агентов (по умолчанию "simplified").
- `communication_display`: Флаг, отображать ли коммуникацию (по умолчанию True).


**Методы**:

- `__init__(name: str = None, episodic_memory=None, semantic_memory=None, mental_faculties: list = None)`: Инициализирует TinyPerson.
- `_post_init(**kwargs)`: Метод, вызываемый после `__init__`. Используется для завершения инициализации.
- `generate_agent_prompt()`: Возвращает строку запроса для агента, сформированную из шаблона.
- `reset_prompt()`: Сбрасывает текущий запрос для агента, обновляя внутренние сообщения.
- `get(self, key)`: Возвращает значение ключа из конфигурации агента.
- `define(self, key, value, group=None)`: Задает значение ключу в конфигурации.
- `define_several(self, group, records)`: Определяет несколько значений в конфигурации, относящихся к одной группе.
- `define_relationships(self, relationships, replace=True)`: Определяет или обновляет отношения между агентами.
- `clear_relationships()`: Очищает отношения между агентами.
- `related_to(self, other_agent, description, symmetric_description=None)`: Определяет отношение между этим агентом и другим агентом.
- `add_mental_faculties(self, mental_faculties)`: Добавляет список когнитивных способностей к агенту.
- `add_mental_faculty(self, faculty)`: Добавляет когнитивную способность к агенту.
- `act(until_done=True, n=None, return_actions=False, max_content_length=default["max_content_display_length"])`: Выполняет действия в окружении.
- `listen(self, speech, source: AgentOrWorld = None, max_content_length=default["max_content_display_length"])`: Слушает другого агента.
- `socialize(self, social_description, source: AgentOrWorld = None, max_content_length=default["max_content_display_length"])`: Воспринимает социальный стимул.
- `see(self, visual_description, source: AgentOrWorld = None, max_content_length=default["max_content_display_length"])`: Воспринимает визуальный стимул.
- `think(self, thought, max_content_length=default["max_content_display_length"])`: Заставляет агента думать о чем-то.
- `internalize_goal(self, goal, max_content_length=default["max_content_display_length"])`: Внутренне реализует цель.
- `_observe(self, stimulus, max_content_length=default["max_content_display_length"])`: Наблюдает за стимулом.
- `listen_and_act(self, speech, return_actions=False, max_content_length=default["max_content_display_length"])`: Объединенный метод для прослушивания и действия.
- `see_and_act(self, visual_description, return_actions=False, max_content_length=default["max_content_display_length"])`: Объединенный метод для просмотра и действия.
- `think_and_act(self, thought, return_actions=False, max_content_length=default["max_content_display_length"])`: Объединенный метод для размышлений и действия.
- `read_documents_from_folder(self, documents_path: str)`: Читает документы из папки и загружает их в семантическую память.
- `read_documents_from_web(self, web_urls: list)`: Читает документы из веб-ссылок и загружает их в семантическую память.
- `move_to(self, location, context=[])`: Перемещает агента в новую локацию.
- `change_context(self, context: list)`: Изменяет контекст.
- `make_agent_accessible(self, agent: Self, relation_description: str = "An agent I can currently interact with.")`: Делает агента доступным для этого агента.
- `make_agent_inaccessible(self, agent: Self)`: Делает агента недоступным для этого агента.
- `make_all_agents_inaccessible(self)`: Делает всех агентов недоступными для этого агента.
- `_produce_message(self)`: Генерирует сообщение с помощью OpenAI.
- `_update_cognitive_state(self, goals=None, context=None, attention=None, emotions=None)`: Обновляет когнитивное состояние агента.
- `_display_communication(self, role, content, kind, simplified=True, max_content_length=default["max_content_display_length"])`: Отображает и сохраняет текущую коммуникацию.
- `_push_and_display_latest_communication(self, rendering)`: Добавляет последнюю коммуникацию в буфер и отображает её.
- `pop_and_display_latest_communications(self)`: Возвращает и отображает сохранённые коммуникации.
- `clear_communications_buffer(self)`: Очищает буфер коммуникаций.
- `pop_latest_actions(self) -> list`: Возвращает последние действия агента.
- `pop_actions_and_get_contents_for(self, action_type: str, only_last_action: bool = True) -> list`: Возвращает содержимое действий определенного типа.
- `__repr__(self)`: Возвращает строковое представление объекта.
- `minibio(self)`: Возвращает краткую биографию агента.
- `pp_current_interactions(self, simplified=True, skip_system=True, max_content_length=default["max_content_display_length"])`: Красиво печатает текущие взаимодействия.
- `pretty_current_interactions(self, simplified=True, skip_system=True, max_content_length=default["max_content_display_length"], first_n=None, last_n=None, include_omission_info:bool=True)`: Возвращает красиво отформатированную строку с текущими сообщениями.
- `_pretty_stimuli(self, role, content, simplified=True, max_content_length=default["max_content_display_length"])`: Красиво отображает стимулы.
- `_pretty_action(self, role, content, simplified=True, max_content_length=default["max_content_display_length"])`: Красиво отображает действие.
- `_pretty_timestamp(self, role, timestamp)`: Красиво отображает отметку времени.
- `iso_datetime(self) -> str`: Возвращает текущую дату и время в формате ISO.
- `save_spec(self, path, include_mental_faculties=True, include_memory=False)`: Сохраняет текущую конфигурацию в JSON-файл.
- `load_spec(path, suppress_mental_faculties=False, suppress_memory=False, auto_rename_agent=False, new_agent_name=None)`: Загружает спецификацию агента из JSON.
- `encode_complete_state(self) -> dict`: Кодирует полное состояние TinyPerson для сериализации.
- `decode_complete_state(self, state: dict) -> Self`: Декодирует полное состояние TinyPerson и создает новый экземпляр TinyPerson.
- `create_new_agent_from_current_spec(self, new_name:str) -> Self`: Создаёт нового агента на основе текущей спецификации.
- `add_agent(agent)`: Добавляет агента в глобальный список агентов.
- `has_agent(agent_name: str)`: Проверяет, зарегистрирован ли агент.
- `set_simulation_for_free_agents(simulation)`: Устанавливает симуляцию для свободных агентов.
- `get_agent_by_name(name)`: Получает агента по имени.
- `clear_agents()`: Очищает глобальный список агентов.


### `TinyMentalFaculty`

**Описание**: Представляет когнитивную способность агента.

**Методы**:
- `__init__(self, name: str, requires_faculties: list=None)`: Инициализирует когнитивную способность.
- `__str__(self) -> str`: Возвращает строковое представление объекта.
- `__eq__(self, other)`: Сравнивает две когнитивные способности.
- `process_action(self, agent, action: dict) -> bool`: Обрабатывает действие, относящееся к этой способности.
- `actions_definitions_prompt(self) -> str`: Возвращает запрос для определения действий, связанных с этой способностью.
- `actions_constraints_prompt(self) -> str`: Возвращает запрос для определения ограничений на действия, связанные с этой способностью.


### `RecallFaculty`, `FilesAndWebGroundingFaculty`, `TinyToolUse` (и другие)


**Описание**: Подклассы `TinyMentalFaculty`, реализующие конкретные когнитивные способности агентов.


### `TinyMemory`, `EpisodicMemory`, `SemanticMemory`


**Описание**: Базовые классы и классы для представления разных типов памяти агента.

**Методы**:


- `store(self, value: Any) -> None`: Хранит значение в памяти.
- `retrieve(self, first_n: int, last_n: int, include_omission_info:bool=True) -> list`: Извлекает значения из памяти.
- `retrieve_recent(self) -> list`: Извлекает последние значения из памяти.
- `retrieve_all(self) -> list`: Извлекает все значения из памяти.
- `retrieve_relevant(self, relevance_target:str, top_k=5) -> list`: Извлекает релевантные значения.


## Функции

### `utils.read_config_file()`


**Описание**: Читает конфигурационный файл.


## Другие

### Модули

- `os`, `csv`, `json`, `ast`, `textwrap`, `datetime`, `chevron`, `logging`, `tinytroupe.utils`, `tinytroupe.control`
- `rich` (для красивой печати)


Этот список не является исчерпывающим и может быть дополнен деталями о классах и функциях, если необходимо.