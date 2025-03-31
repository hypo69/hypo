# Модуль агента

## Обзор

Модуль предоставляет основные классы и функции для агентов TinyTroupe.

Агенты - это ключевая абстракция, используемая в TinyTroupe. Агент - это имитируемый человек или сущность, которая может взаимодействовать с другими агентами и средой, получая стимулы и производя действия. Агенты имеют когнитивные состояния, которые обновляются по мере их взаимодействия со средой и другими агентами. Агенты также могут хранить и извлекать информацию из памяти и могут выполнять действия в среде. В отличие от агентов, чья цель - обеспечить поддержку помощников на базе ИИ или других инструментов повышения производительности, **агенты TinyTroupe стремятся представлять человекоподобное поведение**, которое включает в себя идиосинкразии, эмоции и другие человекоподобные черты, которых не ожидаешь от инструмента повышения производительности.

Общая базовая конструкция вдохновлена в основном когнитивной психологией, поэтому агенты имеют различные внутренние когнитивные состояния, такие как внимание, эмоции и цели. Именно поэтому память агента, в отличие от других платформ агентов на основе LLM, имеет тонкие внутренние разделения, особенно между эпизодической и семантической памятью. Также присутствуют некоторые бихевиористские концепции, такие как идея "стимула" и "реакции" в методах `listen` и `act`, которые являются ключевыми абстракциями для понимания того, как агенты взаимодействуют со средой и другими агентами.

## Содержание

- [Классы](#классы)
  - [`TinyPerson`](#tinyperson)
    - [`__init__`](#__init__)
    - [`_post_init`](#_post_init)
    - [`_rename`](#_rename)
    - [`generate_agent_prompt`](#generate_agent_prompt)
    - [`reset_prompt`](#reset_prompt)
    - [`get`](#get)
    - [`define`](#define)
    - [`define_several`](#define_several)
    - [`define_relationships`](#define_relationships)
    - [`clear_relationships`](#clear_relationships)
    - [`related_to`](#related_to)
    - [`add_mental_faculties`](#add_mental_faculties)
    - [`add_mental_faculty`](#add_mental_faculty)
    - [`act`](#act)
    - [`listen`](#listen)
    - [`socialize`](#socialize)
    - [`see`](#see)
    - [`think`](#think)
    - [`internalize_goal`](#internalize_goal)
    - [`_observe`](#_observe)
    - [`listen_and_act`](#listen_and_act)
    - [`see_and_act`](#see_and_act)
    - [`think_and_act`](#think_and_act)
    - [`read_documents_from_folder`](#read_documents_from_folder)
    - [`read_documents_from_web`](#read_documents_from_web)
    - [`move_to`](#move_to)
    - [`change_context`](#change_context)
    - [`make_agent_accessible`](#make_agent_accessible)
    - [`make_agent_inaccessible`](#make_agent_inaccessible)
    - [`make_all_agents_inaccessible`](#make_all_agents_inaccessible)
    - [`_produce_message`](#_produce_message)
    - [`_update_cognitive_state`](#_update_cognitive_state)
    - [`_display_communication`](#_display_communication)
    - [`_push_and_display_latest_communication`](#_push_and_display_latest_communication)
    - [`pop_and_display_latest_communications`](#pop_and_display_latest_communications)
    - [`clear_communications_buffer`](#clear_communications_buffer)
    - [`pop_latest_actions`](#pop_latest_actions)
    - [`pop_actions_and_get_contents_for`](#pop_actions_and_get_contents_for)
    - [`__repr__`](#__repr__)
    - [`minibio`](#minibio)
    - [`pp_current_interactions`](#pp_current_interactions)
    - [`pretty_current_interactions`](#pretty_current_interactions)
    - [`_pretty_stimuli`](#_pretty_stimuli)
    - [`_pretty_action`](#_pretty_action)
    - [`_pretty_timestamp`](#_pretty_timestamp)
    - [`iso_datetime`](#iso_datetime)
    - [`save_spec`](#save_spec)
    - [`load_spec`](#load_spec)
    - [`encode_complete_state`](#encode_complete_state)
    - [`decode_complete_state`](#decode_complete_state)
    - [`create_new_agent_from_current_spec`](#create_new_agent_from_current_spec)
    - [`add_agent`](#add_agent)
    - [`has_agent`](#has_agent)
    - [`set_simulation_for_free_agents`](#set_simulation_for_free_agents)
    - [`get_agent_by_name`](#get_agent_by_name)
    - [`clear_agents`](#clear_agents)
  - [`TinyMentalFaculty`](#tinymentalfaculty)
    - [`__init__`](#__init__-1)
    - [`__str__`](#__str__-1)
    - [`__eq__`](#__eq__)
    - [`process_action`](#process_action-1)
    - [`actions_definitions_prompt`](#actions_definitions_prompt-1)
    - [`actions_constraints_prompt`](#actions_constraints_prompt-1)
  - [`RecallFaculty`](#recallfaculty)
    - [`__init__`](#__init__-2)
    - [`process_action`](#process_action-2)
    - [`actions_definitions_prompt`](#actions_definitions_prompt-2)
    - [`actions_constraints_prompt`](#actions_constraints_prompt-2)
  - [`FilesAndWebGroundingFaculty`](#filesandwebgroundingfaculty)
    - [`__init__`](#__init__-3)
    - [`process_action`](#process_action-3)
    - [`actions_definitions_prompt`](#actions_definitions_prompt-3)
    - [`actions_constraints_prompt`](#actions_constraints_prompt-3)
  - [`TinyToolUse`](#tinytooluse)
    - [`__init__`](#__init__-4)
    - [`process_action`](#process_action-4)
    - [`actions_definitions_prompt`](#actions_definitions_prompt-4)
    - [`actions_constraints_prompt`](#actions_constraints_prompt-4)
  - [`TinyMemory`](#tinymemory)
    - [`store`](#store)
    - [`retrieve`](#retrieve)
    - [`retrieve_recent`](#retrieve_recent)
    - [`retrieve_all`](#retrieve_all)
    - [`retrieve_relevant`](#retrieve_relevant)
  - [`EpisodicMemory`](#episodicmemory)
    - [`__init__`](#__init__-5)
    - [`store`](#store-1)
    - [`count`](#count)
    - [`retrieve`](#retrieve-1)
    - [`retrieve_recent`](#retrieve_recent-1)
    - [`retrieve_all`](#retrieve_all-1)
    - [`retrieve_relevant`](#retrieve_relevant-1)
    - [`retrieve_first`](#retrieve_first)
    - [`retrieve_last`](#retrieve_last)
  - [`SemanticMemory`](#semanticmemory)
    - [`__init__`](#__init__-6)
    - [`retrieve_relevant`](#retrieve_relevant-2)
    - [`retrieve_document_content_by_name`](#retrieve_document_content_by_name)
    - [`list_documents_names`](#list_documents_names)
    - [`add_documents_paths`](#add_documents_paths)
    - [`add_documents_path`](#add_documents_path)
    - [`add_web_urls`](#add_web_urls)
    - [`add_web_url`](#add_web_url)
    - [`_add_documents`](#_add_documents)
    - [`_post_deserialization_init`](#_post_deserialization_init)
  
- [Переменные](#переменные)
  - [`default`](#default)
  - [`config`](#config)
  - [`llmaindex_openai_embed_model`](#llmaindex_openai_embed_model)
  - [`Self`](#self)
  - [`AgentOrWorld`](#agentorworld)
  - [`logger`](#logger)

## Классы

### `TinyPerson`

**Описание**: Имитируемый человек во вселенной TinyTroupe.

**Методы**:
- [`__init__`](#__init__)
- [`_post_init`](#_post_init)
- [`_rename`](#_rename)
- [`generate_agent_prompt`](#generate_agent_prompt)
- [`reset_prompt`](#reset_prompt)
- [`get`](#get)
- [`define`](#define)
- [`define_several`](#define_several)
- [`define_relationships`](#define_relationships)
- [`clear_relationships`](#clear_relationships)
- [`related_to`](#related_to)
- [`add_mental_faculties`](#add_mental_faculties)
- [`add_mental_faculty`](#add_mental_faculty)
- [`act`](#act)
- [`listen`](#listen)
- [`socialize`](#socialize)
- [`see`](#see)
- [`think`](#think)
- [`internalize_goal`](#internalize_goal)
- [`_observe`](#_observe)
- [`listen_and_act`](#listen_and_act)
- [`see_and_act`](#see_and_act)
- [`think_and_act`](#think_and_act)
- [`read_documents_from_folder`](#read_documents_from_folder)
- [`read_documents_from_web`](#read_documents_from_web)
- [`move_to`](#move_to)
- [`change_context`](#change_context)
- [`make_agent_accessible`](#make_agent_accessible)
- [`make_agent_inaccessible`](#make_agent_inaccessible)
- [`make_all_agents_inaccessible`](#make_all_agents_inaccessible)
- [`_produce_message`](#_produce_message)
- [`_update_cognitive_state`](#_update_cognitive_state)
- [`_display_communication`](#_display_communication)
- [`_push_and_display_latest_communication`](#_push_and_display_latest_communication)
- [`pop_and_display_latest_communications`](#pop_and_display_latest_communications)
- [`clear_communications_buffer`](#clear_communications_buffer)
- [`pop_latest_actions`](#pop_latest_actions)
- [`pop_actions_and_get_contents_for`](#pop_actions_and_get_contents_for)
- [`__repr__`](#__repr__)
- [`minibio`](#minibio)
- [`pp_current_interactions`](#pp_current_interactions)
- [`pretty_current_interactions`](#pretty_current_interactions)
- [`_pretty_stimuli`](#_pretty_stimuli)
- [`_pretty_action`](#_pretty_action)
- [`_pretty_timestamp`](#_pretty_timestamp)
- [`iso_datetime`](#iso_datetime)
- [`save_spec`](#save_spec)
- [`load_spec`](#load_spec)
- [`encode_complete_state`](#encode_complete_state)
- [`decode_complete_state`](#decode_complete_state)
- [`create_new_agent_from_current_spec`](#create_new_agent_from_current_spec)
- [`add_agent`](#add_agent)
- [`has_agent`](#has_agent)
- [`set_simulation_for_free_agents`](#set_simulation_for_free_agents)
- [`get_agent_by_name`](#get_agent_by_name)
- [`clear_agents`](#clear_agents)

#### `__init__`

```python
def __init__(self, name: str = None, episodic_memory=None, semantic_memory=None, mental_faculties: list = None) -> None
```

**Описание**: Создает TinyPerson.

**Параметры**:
- `name` (str): Имя TinyPerson. Либо это, либо `spec_path` должны быть указаны.
- `episodic_memory` (EpisodicMemory, optional): Используемая реализация памяти. По умолчанию `EpisodicMemory()`.
- `semantic_memory` (SemanticMemory, optional): Используемая реализация памяти. По умолчанию `SemanticMemory()`.
- `mental_faculties` (list, optional): Список ментальных способностей, которые нужно добавить агенту. По умолчанию `None`.

#### `_post_init`

```python
def _post_init(self, **kwargs) -> None
```

**Описание**: Выполняется после `__init__`, так как класс имеет декоратор `@post_init`. Удобно разделять некоторые процессы инициализации, чтобы упростить десериализацию.

#### `_rename`

```python
def _rename(self, new_name: str) -> None
```

**Описание**: Переименовывает агента.

**Параметры**:
- `new_name` (str): Новое имя агента.

#### `generate_agent_prompt`

```python
def generate_agent_prompt(self) -> str
```

**Описание**: Генерирует подсказку агента на основе шаблона.

**Возвращает**:
- `str`: Строка сгенерированной подсказки.

#### `reset_prompt`

```python
def reset_prompt(self) -> None
```

**Описание**: Сбрасывает подсказку агента, перегенерируя ее на основе текущей конфигурации и эпизодической памяти.

#### `get`

```python
def get(self, key) -> Any
```

**Описание**: Возвращает определение ключа в конфигурации TinyPerson.

**Параметры**:
- `key` (Any): Ключ, значение которого необходимо получить.

**Возвращает**:
- `Any`: Значение ключа или `None`, если ключ не найден.

#### `define`

```python
@transactional
def define(self, key: Any, value: Any, group: Any = None) -> None
```

**Описание**: Определяет значение в конфигурации TinyPerson.

**Параметры**:
- `key` (Any): Ключ значения.
- `value` (Any): Определяемое значение.
- `group` (Any, optional): Группа, к которой относится значение. Если `None`, значение добавляется на верхний уровень конфигурации.

#### `define_several`

```python
def define_several(self, group: Any, records: list) -> None
```

**Описание**: Определяет несколько значений в конфигурации TinyPerson, все принадлежащие одной группе.

**Параметры**:
- `group` (Any): Группа, к которой относятся значения.
- `records` (list): Список записей для определения.

#### `define_relationships`

```python
@transactional
def define_relationships(self, relationships: list | dict, replace: bool = True) -> None
```

**Описание**: Определяет или обновляет отношения TinyPerson.

**Параметры**:
- `relationships` (list or dict): Отношения, которые нужно добавить или заменить. Список словарей, сопоставляющих имена агентов с описаниями отношений, или один словарь, сопоставляющий имя одного агента с описанием его отношения.
- `replace` (bool, optional): Определяет, нужно ли заменять текущие отношения или добавлять к ним. По умолчанию `True`.

**Вызывает исключения**:
- `Exception`: Если аргументы недействительны.

#### `clear_relationships`

```python
@transactional
def clear_relationships(self) -> Self
```

**Описание**: Очищает отношения TinyPerson.

**Возвращает**:
- `Self`: Сам агент для упрощения цепочки вызовов.

#### `related_to`

```python
@transactional
def related_to(self, other_agent: Self, description: str, symmetric_description: str = None) -> Self
```

**Описание**: Определяет отношение между этим агентом и другим агентом.

**Параметры**:
- `other_agent` (TinyPerson): Другой агент.
- `description` (str): Описание отношения.
- `symmetric_description` (str, optional): Симметричное описание отношения для другого агента.

**Возвращает**:
- `TinyPerson`: Сам агент для упрощения цепочки вызовов.

#### `add_mental_faculties`

```python
def add_mental_faculties(self, mental_faculties: list) -> Self
```

**Описание**: Добавляет список ментальных способностей к агенту.

**Параметры**:
- `mental_faculties` (list): Список ментальных способностей.

**Возвращает**:
- `Self`: Сам агент для упрощения цепочки вызовов.

#### `add_mental_faculty`

```python
def add_mental_faculty(self, faculty: TinyMentalFaculty) -> Self
```

**Описание**: Добавляет ментальную способность к агенту.

**Параметры**:
- `faculty` (TinyMentalFaculty): Ментальная способность для добавления.

**Возвращает**:
- `Self`: Сам агент для упрощения цепочки вызовов.

**Вызывает исключения**:
- `Exception`: Если ментальная способность уже присутствует у агента.

#### `act`

```python
@transactional
def act(self, until_done: bool = True, n: int = None, return_actions: bool = False, max_content_length: int = default["max_content_display_length"]) -> list | None
```

**Описание**: Выполняет действия в среде и обновляет свое внутреннее когнитивное состояние.
Либо действует, пока агент не закончит и не потребует дополнительных стимулов, либо действует фиксированное количество раз, но не оба варианта одновременно.

**Параметры**:
- `until_done` (bool, optional): Определяет, нужно ли продолжать действовать, пока агент не закончит и не потребует дополнительных стимулов. По умолчанию `True`.
- `n` (int, optional): Количество действий для выполнения. По умолчанию `None`.
- `return_actions` (bool, optional): Определяет, нужно ли возвращать действия. По умолчанию `False`.
- `max_content_length` (int, optional): Максимальная длина контента для отображения. По умолчанию значение из `default["max_content_display_length"]`.

**Возвращает**:
- `list | None`: Список действий, если `return_actions` равен `True`, иначе `None`.

#### `listen`

```python
@transactional
def listen(self, speech: str, source: AgentOrWorld = None, max_content_length: int = default["max_content_display_length"]) -> Self
```

**Описание**: Слушает другого агента (искусственного или человека) и обновляет свое внутреннее когнитивное состояние.

**Параметры**:
- `speech` (str): Речь, которую нужно прослушать.
- `source` (AgentOrWorld, optional): Источник речи. По умолчанию `None`.
- `max_content_length` (int, optional): Максимальная длина контента для отображения. По умолчанию значение из `default["max_content_display_length"]`.

**Возвращает**:
- `Self`: Сам агент для упрощения цепочки вызовов.

#### `socialize`

```python
def socialize(self, social_description: str, source: AgentOrWorld = None, max_content_length: int = default["max_content_display_length"]) -> Self
```

**Описание**: Воспринимает социальный стимул через описание и обновляет свое внутреннее когнитивное состояние.

**Параметры**:
- `social_description` (str): Описание социального стимула.
- `source` (AgentOrWorld, optional): Источник социального стимула. По умолчанию `None`.
- `max_content_length` (int, optional): Максимальная длина контента для отображения. По умолчанию значение из `default["max_content_display_length"]`.

**Возвращает**:
- `Self`: Сам агент для упрощения цепочки вызовов.

#### `see`

```python
def see(self, visual_description: str, source: AgentOrWorld = None, max_content_length: int = default["max_content_display_length"]) -> Self
```

**Описание**: Воспринимает визуальный стимул через описание и обновляет свое внутреннее когнитивное состояние.

**Параметры**:
- `visual_description` (str): Описание визуального стимула.
- `source` (AgentOrWorld, optional): Источник визуального стимула. По умолчанию `None`.
- `max_content_length` (int, optional): Максимальная длина контента для отображения. По умолчанию значение из `default["max_content_display_length"]`.

**Возвращает**:
- `Self`: Сам агент для упрощения цепочки вызовов.

#### `think`

```python
def think(self, thought: str, max_content_length: int = default["max_content_display_length"]) -> Self
```

**Описание**: Заставляет агента думать о чем-то и обновляет его внутреннее когнитивное состояние.

**Параметры**:
- `thought` (str): О чем агент должен подумать.
- `max_content_length` (int, optional): Максимальная длина контента для отображения. По умолчанию значение из `default["max_content_display_length"]`.

**Возвращает**:
- `Self`: Сам агент для упрощения цепочки вызовов.

#### `internalize_goal`

```python
def internalize_goal(self, goal: str, max_content_length: int = default["max_content_display_length"]) -> Self
```

**Описание**: Интернализирует цель и обновляет свое внутреннее когнитивное состояние.

**Параметры**:
- `goal` (str): Цель, которую нужно интернализировать.
- `max_content_length` (int, optional): Максимальная длина контента для отображения. По умолчанию значение из `default["max_content_display_length"]`.

**Возвращает**:
- `Self`: Сам агент для упрощения цепочки вызовов.

#### `_observe`

```python
@transactional
def _observe(self, stimulus: dict, max_content_length: int = default["max_content_display_length"]) -> Self
```

**Описание**: Наблюдает за стимулом и обновляет внутреннее когнитивное состояние.

**Параметры**:
- `stimulus` (dict): Стимул для наблюдения.
- `max_content_length` (int, optional): Максимальная длина контента для отображения. По умолчанию значение из `default["max_content_display_length"]`.

**Возвращает**:
- `Self`: Сам агент для упрощения цепочки вызовов.

#### `listen_and_act`

```python
@transactional
def listen_and_act(self, speech: str, return_actions: bool = False, max_content_length: int = default["max_content_display_length"]) -> list | None
```

**Описание**: Удобный метод, объединяющий методы `listen` и `act`.

**Параметры**:
- `speech` (str): Речь, которую нужно прослушать.
- `return_actions` (bool, optional): Определяет, нужно ли возвращать действия. По умолчанию `False`.
- `max_content_length` (int, optional): Максимальная длина контента для отображения. По умолчанию значение из `default["max_content_display_length"]`.

**Возвращает**:
- `list | None`: Список действий, если `return_actions` равен `True`, иначе `None`.

#### `see_and_act`

```python
@transactional
def see_and_act(self, visual_description: str, return_actions: bool = False, max_content_length: int = default["max_content_display_length"]) -> list | None
```

**Описание**: Удобный метод, объединяющий методы `see` и `act`.

**Параметры**:
- `visual_description` (str): Описание визуального стимула.
- `return_actions` (bool, optional): Определяет, нужно ли возвращать действия. По умолчанию `False`.
- `max_content_length` (int, optional): Максимальная длина контента для отображения. По умолчанию значение из `default["max_content_display_length"]`.

**Возвращает**:
- `list | None`: Список действий, если `return_actions` равен `True`, иначе `None`.

#### `think_and_act`

```python
@transactional
def think_and_act(self, thought: str, return_actions: bool = False, max_content_length: int = default["max_content_display_length"]) -> list | None
```

**Описание**: Удобный метод, объединяющий методы `think` и `act`.

**Параметры**:
- `thought` (str): О чем агент должен подумать.
- `return_actions` (bool, optional): Определяет, нужно ли возвращать действия. По умолчанию `False`.
- `max_content_length` (int, optional): Максимальная длина контента для отображения. По умолчанию значение из `default["max_content_display_length"]`.

**Возвращает**:
- `list | None`: Список действий, если `return_actions` равен `True`, иначе `None`.

#### `read_documents_from_folder`

```python
def read_documents_from_folder(self, documents_path: str) -> None
```

**Описание**: Считывает документы из каталога и загружает их в семантическую память.

**Параметры**:
- `documents_path` (str): Путь к каталогу с документами.

#### `read_documents_from_web`

```python
def read_documents_from_web(self, web_urls: list) -> None
```

**Описание**: Считывает документы с веб-адресов и загружает их в семантическую память.

**Параметры**:
- `web_urls` (list): Список веб-адресов для чтения документов.

#### `move_to`

```python
@transactional
def move_to(self, location: str, context: list = []) -> None
```

**Описание**: Перемещается в новое место и обновляет свое внутреннее когнитивное состояние.

**Параметры**:
- `location` (str): Новое местоположение.
- `context` (list, optional): Новый контекст местоположения.

#### `change_context`

```python
@transactional
def change_context(self, context: list) -> None
```

**Описание**: Изменяет контекст и обновляет свое внутреннее когнитивное состояние.

**Параметры**:
- `context` (list): Новый контекст.

#### `make_agent_accessible`

```python
@transactional
def make_agent_accessible(self, agent: Self, relation_description: str = "An agent I can currently interact with.") -> None
```

**Описание**: Делает агента доступным для этого агента.

**Параметры**:
- `agent` (Self): Агент, которого нужно сделать доступным.
- `relation_description` (str, optional): Описание отношений с агентом. По умолчанию "An agent I can currently interact with.".

#### `make_agent_inaccessible`

```python
@transactional
def make_agent_inaccessible(self, agent: Self) -> None
```

**Описание**: Делает агента недоступным для этого агента.

**Параметры**:
- `agent` (Self): Агент, которого нужно сделать недоступным.

#### `make_all_agents_inaccessible`

```python
@transactional
def make_all_agents_inaccessible(self) -> None
```

**Описание**: Делает всех агентов недоступными для этого агента.

#### `_produce_message`

```python
def _produce_message(self) -> tuple[str, dict]
```

**Описание**: Генерирует сообщение на основе текущего когнитивного состояния агента.

**Возвращает**:
- `tuple[str, dict]`: Роль и содержимое сообщения.

#### `_update_cognitive_state`

```python
@transactional
def _update_cognitive_state(self, goals: list = None, context: list = None, attention: str = None, emotions: str = None) -> None
```

**Описание**: Обновляет когнитивное состояние TinyPerson.

**Параметры**:
- `goals` (list, optional): Текущие цели.
- `context` (list, optional): Текущий контекст.
- `attention` (str, optional): Текущее внимание.
- `emotions` (str, optional): Текущие эмоции.

#### `_display_communication`

```python
def _display_communication(self, role: str, content: dict, kind: str, simplified: bool = True, max_content_length: int = default["max_content_display_length"]) -> None
```

**Описание**: Отображает текущее сообщение и сохраняет его в буфер для последующего использования.

**Параметры**:
- `role` (str): Роль сообщения.
- `content` (dict): Содержание сообщения.
- `kind` (str): Тип сообщения ("stimuli" или "action").
- `simplified` (bool, optional): Определяет, нужно ли упрощать сообщение для отображения. По умолчанию `True`.
- `max_content_length` (int, optional): Максимальная длина контента для отображения. По умолчанию значение из `default["max_content_display_length"]`.

**Вызывает исключения**:
- `ValueError`: Если тип сообщения неизвестен.

#### `_push_and_display_latest_communication`

```python
def _push_and_display_latest_communication(self, rendering: str) -> None
```

**Описание**: Помещает последнее сообщение в буфер агента.

**Параметры**:
- `rendering` (str): Сообщение, которое нужно добавить в буфер.

#### `pop_and_display_latest_communications`

```python
def pop_and_display_latest_communications(self) -> list
```

**Описание**: Извлекает последние сообщения и отображает их.

**Возвращает**:
- `list`: Список извлеченных сообщений.

#### `clear_communications_buffer`

```python
def clear_communications_buffer(self) -> None
```

**Описание**: Очищает буфер сообщений.

#### `pop_latest_actions`

```python
@transactional
def pop_latest_actions(self) -> list
```

**Описание**: Возвращает последние действия, выполненные этим агентом. Обычно используется средой для использования действий и обеспечения соответствующей экологической семантики для них (т.е. эффектов на других агентов).

**Возвращает**:
- `list`: Список последних действий.

#### `pop_actions_and_get_contents_for`

```python
@transactional
def pop_actions_and_get_contents_for(self, action_type: str, only_last_action: bool = True) -> str | list
```

**Описание**: Возвращает содержимое действий заданного типа, выполненных этим агентом. Обычно используется для выполнения проверок и тестов.

**Параметры**:
- `action_type` (str): Тип действия для поиска.
- `only_last_action` (bool, optional): Определяет, нужно ли возвращать только содержимое последнего действия. По умолчанию `True`.

**Возвращает**:
- `str | list`: Содержимое последнего действия, если `only_last_action` равен `True`, иначе список всего содержимого действий.

#### `__repr__`

```python
def __repr__(self) -> str
```

**Описание**: Возвращает строковое представление объекта `TinyPerson`.

**Возвращает**:
- `str`: Строковое представление объекта `TinyPerson`.

#### `minibio`

```python
def minibio(self) -> str
```

**Описание**: Возвращает мини-биографию TinyPerson.

**Возвращает**:
- `str`: Мини-биография TinyPerson.

#### `pp_current_interactions`

```python
def pp_current_interactions(self, simplified: bool = True, skip_system: bool = True, max_content_length: int = default["max_content_display_length"]) -> None
```

**Описание**: Выводит текущие сообщения в удобочитаемом виде.

**Параметры**:
- `simplified` (bool, optional): Определяет, нужно ли упрощать сообщение для отображения. По умолчанию `True`.
- `skip_system` (bool, optional): Определяет, нужно ли пропускать системные сообщения. По умолчанию `True`.
- `max_content_length` (int, optional): Максимальная длина контента для отображения. По умолчанию значение из `default["max_content_display_length"]`.

#### `pretty_current_interactions`

```python
def pretty_current_interactions(self, simplified: bool = True, skip_system: bool = True, max_content_length: int = default["max_content_display_length"], first_n: int = None, last_n: int = None, include_omission_info: bool = True) -> str
```

**Описание**: Возвращает красивую, удобочитаемую строку с текущими сообщениями.

**Параметры**:
- `simplified` (bool, optional): Определяет, нужно ли упрощать сообщение для отображения. По умолчанию `True`.
- `skip_system` (bool, optional): Определяет, нужно ли пропускать системные сообщения. По умолчанию `True`.
- `max_content_length` (int, optional): Максимальная длина контента для отображения. По умолчанию значение из `default["max_content_display_length"]`.
- `first_n` (int, optional): Количество первых сообщений для отображения. По умолчанию `None`.
- `last_n` (int, optional): Количество последних сообщений для отображения. По умолчанию `None`.
- `include_omission_info` (bool, optional): Определяет, нужно ли включать сообщение об опускании. По умолчанию `True`.

**Возвращает**:
- `str`: Отформатированная строка с сообщениями