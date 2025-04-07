# Модуль для работы с агентами TinyTroupe
=================================================

Модуль содержит класс :class:`TinyPerson`, который представляет собой симулированного персонажа или сущность, способную взаимодействовать с другими агентами и окружающей средой.
Агенты имеют когнитивные состояния, которые обновляются по мере их взаимодействия с окружающей средой и другими агентами.
Агенты также могут хранить и извлекать информацию из памяти и выполнять действия в окружающей среде.

Пример использования
----------------------

```python
from tinytroupe.agent import TinyPerson, EpisodicMemory, SemanticMemory

# Создание агента
agent = TinyPerson(name='Alice', episodic_memory=EpisodicMemory(), semantic_memory=SemanticMemory())

# Определение характеристик агента
agent.define('age', 25)
agent.define('occupation', 'Software Engineer')

# Агент слушает речь
agent.listen('Hello, how are you?')

# Агент действует
agent.act()
```

## Оглавление

- [Обзор](#обзор)
- [Подробнее](#подробнее)
- [Классы](#классы)
    - [TinyPerson](#tinyperson)
    - [TinyMentalFaculty](#tinymenfalfaculty)
    - [RecallFaculty](#recallfaculty)
    - [FilesAndWebGroundingFaculty](#filesandwebgroundingfaculty)
    - [TinyToolUse](#tinytooluse)
    - [TinyMemory](#tinymemory)
    - [EpisodicMemory](#episodicmemory)
    - [SemanticMemory](#semanticmemory)
- [Функции](#функции)

## Обзор

Этот модуль предоставляет основные классы и функции для создания агентов TinyTroupe. Агенты - это ключевая абстракция, используемая в TinyTroupe. Они имитируют поведение человека, включая идиосинкразии, эмоции и другие человеческие черты.

## Подробнее

В основе дизайна лежит когнитивная психология, поэтому агенты имеют различные внутренние когнитивные состояния, такие как внимание, эмоции и цели. Память агента, в отличие от других платформ агентов на основе LLM, имеет внутренние разделения, в частности, между эпизодической и семантической памятью. Также присутствуют некоторые бихевиористские концепции, такие как идея "стимула" и "ответа" в методах `listen` и `act`, которые являются ключевыми абстракциями для понимания того, как агенты взаимодействуют с окружающей средой и другими агентами.

## Классы

### `TinyPerson`

**Описание**: Симулированный персонаж во вселенной TinyTroupe.

**Принцип работы**: Класс `TinyPerson` представляет собой агента, который может взаимодействовать с другими агентами и окружающей средой. Он имеет когнитивные состояния, такие как внимание, эмоции и цели, а также эпизодическую и семантическую память. Агент может выполнять действия, слушать других агентов и воспринимать стимулы из окружающей среды.

**Аттрибуты**:
- `name` (str): Имя агента.
- `episodic_memory` (EpisodicMemory): Эпизодическая память агента.
- `semantic_memory` (SemanticMemory): Семантическая память агента.
- `_mental_faculties` (list): Список ментальных способностей агента.
- `_configuration` (dict): Конфигурация агента.
- `MAX_ACTIONS_BEFORE_DONE` (int): Максимальное количество действий, которое агент может выполнить до завершения.
- `PP_TEXT_WIDTH` (int): Ширина текста для красивого вывода.
- `serializable_attributes` (list): Список сериализуемых атрибутов.
- `all_agents` (dict): Словарь всех созданных агентов (имя -> агент).
- `communication_style` (str): Стиль общения для всех агентов ("simplified" или "full").
- `communication_display` (bool): Определяет, отображать ли общение.

**Методы**:
- `__init__(self, name: str = None, episodic_memory = None, semantic_memory = None, mental_faculties: list = None)`: Создает экземпляр класса `TinyPerson`.
- `_post_init(self, **kwargs)`: Выполняет постобработку инициализации после `__init__`.
- `generate_agent_prompt(self)`: Генерирует prompt для агента на основе шаблона.
- `reset_prompt(self)`: Сбрасывает prompt агента.
- `get(self, key)`: Возвращает значение ключа из конфигурации агента.
- `define(self, key, value, group=None)`: Определяет значение в конфигурации агента.
- `define_several(self, group, records)`: Определяет несколько значений в конфигурации агента, принадлежащих к одной группе.
- `define_relationships(self, relationships, replace=True)`: Определяет или обновляет отношения агента.
- `clear_relationships(self)`: Очищает отношения агента.
- `related_to(self, other_agent, description, symmetric_description=None)`: Определяет отношение между этим агентом и другим агентом.
- `add_mental_faculties(self, mental_faculties)`: Добавляет список ментальных способностей агенту.
- `add_mental_faculty(self, faculty)`: Добавляет ментальную способность агенту.
- `act(self, until_done=True, n=None, return_actions=False, max_content_length=default["max_content_display_length"])`: Агент действует в окружающей среде и обновляет свое внутреннее когнитивное состояние.
- `listen(self, speech, source: AgentOrWorld = None, max_content_length=default["max_content_display_length"])`: Агент слушает другого агента и обновляет свое внутреннее когнитивное состояние.
- `socialize(self, social_description: str, source: AgentOrWorld = None, max_content_length=default["max_content_display_length"])`: Агент воспринимает социальный стимул через описание и обновляет свое внутреннее когнитивное состояние.
- `see(self, visual_description, source: AgentOrWorld = None, max_content_length=default["max_content_display_length"])`: Агент воспринимает визуальный стимул через описание и обновляет свое внутреннее когнитивное состояние.
- `think(self, thought, max_content_length=default["max_content_display_length"])`: Агент думает о чем-то и обновляет свое внутреннее когнитивное состояние.
- `internalize_goal(self, goal, max_content_length=default["max_content_display_length"])`: Агент интернализует цель и обновляет свое внутреннее когнитивное состояние.
- `_observe(self, stimulus, max_content_length=default["max_content_display_length"])`: Агент наблюдает за стимулом и обновляет свое внутреннее когнитивное состояние.
- `listen_and_act(self, speech, return_actions=False, max_content_length=default["max_content_display_length"])`: Комбинированный метод `listen` и `act`.
- `see_and_act(self, visual_description, return_actions=False, max_content_length=default["max_content_display_length"])`: Комбинированный метод `see` и `act`.
- `think_and_act(self, thought, return_actions=False, max_content_length=default["max_content_display_length"])`: Комбинированный метод `think` и `act`.
- `read_documents_from_folder(self, documents_path: str)`: Считывает документы из каталога и загружает их в семантическую память.
- `read_documents_from_web(self, web_urls: list)`: Считывает документы с веб-страниц и загружает их в семантическую память.
- `move_to(self, location, context=[])`: Перемещается в новое местоположение и обновляет свое внутреннее когнитивное состояние.
- `change_context(self, context: list)`: Изменяет контекст и обновляет свое внутреннее когнитивное состояние.
- `make_agent_accessible(self, agent: Self, relation_description: str = "An agent I can currently interact with.")`: Делает агента доступным для этого агента.
- `make_agent_inaccessible(self, agent: Self)`: Делает агента недоступным для этого агента.
- `make_all_agents_inaccessible(self)`: Делает всех агентов недоступными для этого агента.
- `_produce_message(self)`: Генерирует сообщение на основе текущего состояния агента.
- `_update_cognitive_state(self, goals=None, context=None, attention=None, emotions=None)`: Обновляет когнитивное состояние `TinyPerson`.
- `_display_communication(self, role, content, kind, simplified=True, max_content_length=default["max_content_display_length"])`: Отображает текущее общение и сохраняет его в буфере для последующего использования.
- `_push_and_display_latest_communication(self, rendering)`: Добавляет последнее сообщение в буфер агента.
- `pop_and_display_latest_communications(self)`: Извлекает последние сообщения из буфера и отображает их.
- `clear_communications_buffer(self)`: Очищает буфер сообщений.
- `pop_latest_actions(self) -> list`: Возвращает последние действия, выполненные этим агентом.
- `pop_actions_and_get_contents_for(self, action_type: str, only_last_action: bool = True) -> list`: Возвращает содержимое действий заданного типа, выполненных этим агентом.
- `minibio(self)`: Возвращает мини-биографию TinyPerson.
- `pp_current_interactions(self, simplified=True, skip_system=True, max_content_length=default["max_content_display_length"])`: Выводит в консоль текущие взаимодействия.
- `pretty_current_interactions(self, simplified=True, skip_system=True, max_content_length=default["max_content_display_length"], first_n=None, last_n=None, include_omission_info: bool = True)`: Возвращает текущие взаимодействия в виде отформатированной строки.
- `_pretty_stimuli(self, role, content, simplified=True, max_content_length=default["max_content_display_length"]) -> list`: Форматирует стимулы для вывода.
- `_pretty_action(self, role, content, simplified=True, max_content_length=default["max_content_display_length"]) -> str`: Форматирует действия для вывода.
- `_pretty_timestamp(self, role, timestamp) -> str`: Форматирует временную метку для вывода.
- `iso_datetime(self) -> str`: Возвращает текущую дату и время среды, если таковая имеется.
- `save_spec(self, path, include_mental_faculties=True, include_memory=False)`: Сохраняет текущую конфигурацию в JSON-файл.
- `load_spec(path, suppress_mental_faculties=False, suppress_memory=False, auto_rename_agent=False, new_agent_name=None)`: Загружает спецификацию агента из JSON-файла.
- `encode_complete_state(self) -> dict`: Кодирует полное состояние `TinyPerson`, включая текущие сообщения, доступных агентов и т.д.
- `decode_complete_state(self, state: dict) -> Self`: Загружает полное состояние `TinyPerson`, включая текущие сообщения, и создает новый экземпляр `TinyPerson`.
- `create_new_agent_from_current_spec(self, new_name: str) -> Self`: Создает нового агента из спецификации текущего агента.
- `add_agent(agent)`: Добавляет агента в глобальный список агентов.
- `has_agent(agent_name: str)`: Проверяет, зарегистрирован ли уже агент.
- `set_simulation_for_free_agents(simulation)`: Устанавливает симуляцию, если она None.
- `get_agent_by_name(name)`: Возвращает агента по имени.
- `clear_agents()`: Очищает глобальный список агентов.

**Примеры**:

```python
from tinytroupe.agent import TinyPerson, EpisodicMemory, SemanticMemory

# Создание агента
agent = TinyPerson(name='Alice', episodic_memory=EpisodicMemory(), semantic_memory=SemanticMemory())

# Определение характеристик агента
agent.define('age', 25)
agent.define('occupation', 'Software Engineer')

# Агент слушает речь
agent.listen('Hello, how are you?')

# Агент действует
agent.act()
```
### `TinyMentalFaculty`

**Описание**: Представляет собой ментальную способность агента.

**Принцип работы**: Базовый класс для различных ментальных способностей. Ментальные способности - это когнитивные возможности, которые есть у агента.

**Аттрибуты**:
- `name` (str): Имя ментальной способности.
- `requires_faculties` (list): Список ментальных способностей, которые требуются для правильной работы этой способности.

**Методы**:
- `__init__(self, name: str, requires_faculties: list=None)`: Инициализирует ментальную способность.
- `process_action(self, agent, action: dict) -> bool`: Обрабатывает действие, связанное с этой способностью.
- `actions_definitions_prompt(self) -> str`: Возвращает prompt для определения действий, связанных с этой способностью.
- `actions_constraints_prompt(self) -> str`: Возвращает prompt для определения ограничений на действия, связанные с этой способностью.

**Примеры**:
```python
from tinytroupe.agent import TinyMentalFaculty

# Создание ментальной способности
faculty = TinyMentalFaculty(name='Planning')
```

### `RecallFaculty`

**Описание**: Ментальная способность для вспоминания информации из памяти.

**Принцип работы**: Позволяет агенту вспоминать информацию из своей семантической памяти.

**Аттрибуты**:
- `name` (str): Имя ментальной способности ("Memory Recall").

**Методы**:
- `__init__(self)`: Инициализирует способность вспоминания.
- `process_action(self, agent, action: dict) -> bool`: Обрабатывает действие "RECALL".
- `actions_definitions_prompt(self) -> str`: Возвращает prompt для определения действия "RECALL".
- `actions_constraints_prompt(self) -> str`: Возвращает prompt для определения ограничений на действие "RECALL".

**Примеры**:
```python
from tinytroupe.agent import RecallFaculty

# Создание способности вспоминания
recall_faculty = RecallFaculty()
```

### `FilesAndWebGroundingFaculty`

**Описание**: Ментальная способность, позволяющая агенту получать доступ к локальным файлам и веб-страницам.

**Принцип работы**: Обеспечивает агенту возможность доступа к локальным файлам и веб-страницам для обоснования своих знаний.

**Аттрибуты**:
- `name` (str): Имя ментальной способности ("Local Grounding").

**Методы**:
- `__init__(self)`: Инициализирует способность доступа к файлам и веб-страницам.
- `process_action(self, agent, action: dict) -> bool`: Обрабатывает действия "CONSULT" и "LIST_DOCUMENTS".
- `actions_definitions_prompt(self) -> str`: Возвращает prompt для определения действий "CONSULT" и "LIST_DOCUMENTS".
- `actions_constraints_prompt(self) -> str`: Возвращает prompt для определения ограничений на действия "CONSULT" и "LIST_DOCUMENTS".

**Примеры**:
```python
from tinytroupe.agent import FilesAndWebGroundingFaculty

# Создание способности доступа к файлам и веб-страницам
grounding_faculty = FilesAndWebGroundingFaculty()
```

### `TinyToolUse`

**Описание**: Ментальная способность, позволяющая агенту использовать инструменты для выполнения задач.

**Принцип работы**: Позволяет агенту использовать инструменты для выполнения задач. Использование инструментов является одним из наиболее важных когнитивных навыков людей и приматов.

**Аттрибуты**:
- `name` (str): Имя ментальной способности ("Tool Use").
- `tools` (list): Список доступных инструментов.

**Методы**:
- `__init__(self, tools: list) -> None`: Инициализирует способность использования инструментов.
- `process_action(self, agent, action: dict) -> bool`: Обрабатывает действие с использованием инструментов.
- `actions_definitions_prompt(self) -> str`: Возвращает prompt для определения действий с использованием инструментов.
- `actions_constraints_prompt(self) -> str`: Возвращает prompt для определения ограничений на действия с использованием инструментов.

**Примеры**:
```python
from tinytroupe.agent import TinyToolUse

# Создание способности использования инструментов
tool_use_faculty = TinyToolUse(tools=[])
```

### `TinyMemory`

**Описание**: Базовый класс для различных типов памяти.

**Принцип работы**: Абстрактный базовый класс для различных типов памяти, используемых агентами.

**Аттрибуты**:
- Отсутствуют.

**Методы**:
- `store(self, value: Any) -> None`: Сохраняет значение в памяти.
- `retrieve(self, first_n: int, last_n: int, include_omission_info:bool=True) -> list`: Извлекает первые n и/или последние n значений из памяти.
- `retrieve_recent(self) -> list`: Извлекает n самых последних значений из памяти.
- `retrieve_all(self) -> list`: Извлекает все значения из памяти.
- `retrieve_relevant(self, relevance_target: str, top_k=5) -> list`: Извлекает все значения из памяти, которые относятся к заданной цели.

**Примеры**:
```python
from tinytroupe.agent import TinyMemory

# Создание экземпляра TinyMemory напрямую не имеет смысла, так как это базовый класс.
```

### `EpisodicMemory`

**Описание**: Предоставляет агенту возможность эпизодической памяти.

**Принцип работы**: Эпизодическая память - это способность помнить конкретные события или эпизоды в прошлом.

**Аттрибуты**:
- `fixed_prefix_length` (int): Фиксированная длина префикса.
- `lookback_length` (int): Длина ретроспективы.
- `memory` (list): Список сохраненных значений.

**Методы**:
- `__init__(self, fixed_prefix_length: int = 100, lookback_length: int = 100) -> None`: Инициализирует память.
- `store(self, value: Any) -> None`: Сохраняет значение в памяти.
- `count(self) -> int`: Возвращает количество значений в памяти.
- `retrieve(self, first_n: int, last_n: int, include_omission_info:bool=True) -> list`: Извлекает первые n и/или последние n значения из памяти.
- `retrieve_recent(self, include_omission_info:bool=True) -> list`: Извлекает n самых последних значений из памяти.
- `retrieve_all(self) -> list`: Извлекает все значения из памяти.
- `retrieve_relevant(self, relevance_target: str) -> list`: Извлекает все значения из памяти, которые относятся к заданной цели.
- `retrieve_first(self, n: int, include_omission_info:bool=True) -> list`: Извлекает первые n значений из памяти.
- `retrieve_last(self, n: int, include_omission_info:bool=True) -> list`: Извлекает последние n значений из памяти.

**Примеры**:
```python
from tinytroupe.agent import EpisodicMemory

# Создание эпизодической памяти
episodic_memory = EpisodicMemory()

# Сохранение значения в памяти
episodic_memory.store({'role': 'user', 'content': 'Hello'})

# Извлечение последних значений из памяти
recent_values = episodic_memory.retrieve_recent()
```

### `SemanticMemory`

**Описание**: Семантическая память - это память значений, пониманий и других знаний, основанных на понятиях, не связанных с конкретным опытом.

**Принцип работы**: В отличие от эпизодической памяти, она не упорядочена во времени и не связана с запоминанием конкретных событий или эпизодов. Этот класс обеспечивает простую реализацию семантической памяти, где агент может хранить и извлекать семантическую информацию.

**Аттрибуты**:
- `index` (obj): Индекс для быстрого поиска релевантной информации.
- `documents_paths` (list): Список путей к папкам с документами.
- `documents_web_urls` (list): Список веб-адресов документов.
- `documents` (list): Список документов.
- `filename_to_document` (dict): Соответствие между именем файла и документом.
- `suppress_attributes_from_serialization` (list): Атрибуты, которые не нужно сериализовать.

**Методы**:
- `__init__(self, documents_paths: list=None, web_urls: list=None) -> None`: Инициализирует память.
- `retrieve_relevant(self, relevance_target: str, top_k=5) -> list`: Извлекает все значения из памяти, которые относятся к заданной цели.
- `retrieve_document_content_by_name(self, document_name: str) -> str`: Извлекает документ по имени.
- `list_documents_names(self) -> list`: Перечисляет имена документов в памяти.
- `add_documents_paths(self, documents_paths: list) -> None`: Добавляет путь к папке с документами, используемыми для семантической памяти.
- `add_documents_path(self, documents_path: str) -> None`: Добавляет путь к папке с документами, используемыми для семантической памяти.
- `add_web_urls(self, web_urls: list) -> None`: Добавляет данные, полученные из указанных URL-адресов, в документы, используемые для семантической памяти.
- `add_web_url(self, web_url: str) -> None`: Добавляет данные, полученные из указанного URL-адреса, в документы, используемые для семантической памяти.
- `_add_documents(self, new_documents, doc_to_name_func) -> list`: Добавляет документы в семантическую память.

**Примеры**:
```python
from tinytroupe.agent import SemanticMemory

# Создание семантической памяти
semantic_memory = SemanticMemory(documents_paths=['./documents'], web_urls=['http://example.com'])

# Извлечение релевантной информации
relevant_values = semantic_memory.retrieve_relevant(relevance_target='example')
```

## Функции

В данном файле отсутствуют отдельные функции, не принадлежащие классам.