# Модуль `agent.py`

## Обзор

Модуль `agent.py` содержит основные классы и функции для агентов TinyTroupe. Агенты - это ключевая абстракция, используемая в TinyTroupe. Агент - это имитированный человек или сущность, которая может взаимодействовать с другими агентами и окружающей средой, получая стимулы и производя действия. Агенты имеют когнитивные состояния, которые обновляются по мере их взаимодействия с окружающей средой и другими агентами. Агенты также могут хранить и извлекать информацию из памяти, а также могут выполнять действия в окружающей среде. В отличие от агентов, целью которых является обеспечение поддержки для ассистентов на базе ИИ или других подобных инструментов повышения производительности, **агенты TinyTroupe нацелены на представление человеческого поведения**, которое включает в себя идиосинкразии, эмоции и другие человеческие черты, которых не ожидают от инструмента повышения производительности.

Общая базовая конструкция вдохновлена в основном когнитивной психологией, поэтому агенты имеют различные внутренние когнитивные состояния, такие как внимание, эмоции и цели. Именно поэтому память агента, в отличие от других платформ агентов на основе LLM, имеет тонкие внутренние разделения, особенно между эпизодической и семантической памятью. Также присутствуют некоторые бихевиористские концепции, такие как идея "стимула" и "ответа" в методах `listen` и `act`, которые являются ключевыми абстракциями для понимания того, как агенты взаимодействуют с окружающей средой и другими агентами.

## Содержание

- [Классы](#классы)
  - [`TinyPerson`](#tinyperson)
  - [`TinyMentalFaculty`](#tinymentalfaculty)
  - [`RecallFaculty`](#recallfaculty)
  - [`FilesAndWebGroundingFaculty`](#filesandwebgroundingfaculty)
  - [`TinyToolUse`](#tinytooluse)
  - [`TinyMemory`](#tinymemory)
  - [`EpisodicMemory`](#episodicmemory)
  - [`SemanticMemory`](#semanticmemory)
- [Переменные](#переменные)
  - [`default`](#default)
  - [`llmaindex_openai_embed_model`](#llmaindex_openai_embed_model)

## Классы

### `TinyPerson`

**Описание**: Имитированный персонаж во вселенной TinyTroupe.

**Атрибуты**:

- `MAX_ACTIONS_BEFORE_DONE` (int): Максимальное количество действий, которое агенту разрешено выполнить до состояния DONE.
- `PP_TEXT_WIDTH` (int): Ширина текста для pretty-print.
- `serializable_attributes` (list): Список атрибутов, которые должны быть сериализованы.
- `all_agents` (dict): Словарь всех созданных агентов (имя -> агент).
- `communication_style` (str): Стиль общения для всех агентов ("упрощенный" или "полный").
- `communication_display` (bool): Отображать ли общение.

**Методы**:

#### `__init__`

```python
def __init__(self, name: str = None, episodic_memory = None, semantic_memory = None, mental_faculties: list = None) -> None
```

**Описание**: Создает экземпляр `TinyPerson`.

**Параметры**:

- `name` (str, optional): Имя `TinyPerson`. Должно быть указано либо это, либо `spec_path`.
- `episodic_memory` (EpisodicMemory, optional): Реализация памяти для использования. По умолчанию `EpisodicMemory()`.
- `semantic_memory` (SemanticMemory, optional): Реализация памяти для использования. По умолчанию `SemanticMemory()`.
- `mental_faculties` (list, optional): Список ментальных способностей для добавления агенту. По умолчанию `None`.

#### `_post_init`

```python
def _post_init(self, **kwargs) -> None
```

**Описание**: Выполняется после `__init__`, так как класс имеет декоратор `@post_init`. Удобно отделять некоторые процессы инициализации, чтобы упростить десериализацию.

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

**Описание**: Генерирует промпт для агента, используя шаблон Mustache.

**Возвращает**:

- `str`: Сгенерированный промпт.

#### `reset_prompt`

```python
def reset_prompt(self) -> None
```

**Описание**: Сбрасывает промпт агента, используя текущую конфигурацию.

#### `get`

```python
def get(self, key) -> Any
```

**Описание**: Возвращает значение ключа из конфигурации `TinyPerson`.

**Параметры**:

- `key` (Any): Ключ для получения.

**Возвращает**:

- `Any`: Значение, связанное с ключом, или `None`, если ключ не найден.

#### `define`

```python
@transactional
def define(self, key, value, group=None) -> None
```

**Описание**: Определяет значение в конфигурации `TinyPerson`.

**Параметры**:

- `key` (Any): Ключ для определения.
- `value` (Any): Значение для определения.
- `group` (Any, optional): Группа, в которой нужно определить значение. По умолчанию `None`.

#### `define_several`

```python
def define_several(self, group, records) -> None
```

**Описание**: Определяет несколько значений в конфигурации `TinyPerson`, все в одной группе.

**Параметры**:

- `group` (Any): Группа, в которой нужно определить значения.
- `records` (list): Список записей для определения.

#### `define_relationships`

```python
@transactional
def define_relationships(self, relationships, replace=True) -> None
```

**Описание**: Определяет или обновляет отношения `TinyPerson`.

**Параметры**:

- `relationships` (list or dict): Отношения для добавления или замены.
- `replace` (bool, optional): Заменять ли текущие отношения или добавлять к ним. По умолчанию `True`.

#### `clear_relationships`

```python
@transactional
def clear_relationships(self) -> TinyPerson
```

**Описание**: Очищает отношения `TinyPerson`.

**Возвращает**:

- `TinyPerson`: Сам агент, для облегчения цепочки вызовов.

#### `related_to`

```python
@transactional
def related_to(self, other_agent: Self, description: str, symmetric_description: str = None) -> TinyPerson
```

**Описание**: Определяет отношения между этим агентом и другим агентом.

**Параметры**:

- `other_agent` (TinyPerson): Другой агент.
- `description` (str): Описание отношений.
- `symmetric_description` (str, optional): Симметричное описание отношений.

**Возвращает**:

- `TinyPerson`: Сам агент, для облегчения цепочки вызовов.

#### `add_mental_faculties`

```python
def add_mental_faculties(self, mental_faculties) -> TinyPerson
```

**Описание**: Добавляет список ментальных способностей к агенту.

**Параметры**:

- `mental_faculties` (list): Список ментальных способностей для добавления.

**Возвращает**:

- `TinyPerson`: Сам агент, для облегчения цепочки вызовов.

#### `add_mental_faculty`

```python
def add_mental_faculty(self, faculty) -> TinyPerson
```

**Описание**: Добавляет ментальную способность к агенту.

**Параметры**:

- `faculty` (Any): Ментальная способность для добавления.

**Возвращает**:

- `TinyPerson`: Сам агент, для облегчения цепочки вызовов.

#### `act`

```python
@transactional
def act(self, until_done=True, n=None, return_actions=False, max_content_length=default["max_content_display_length"]) -> Optional[list]
```

**Описание**: Действует в окружающей среде и обновляет свое внутреннее когнитивное состояние.

**Параметры**:

- `until_done` (bool, optional): Продолжать действовать, пока агент не закончит и не потребует дополнительных стимулов. По умолчанию `True`.
- `n` (int, optional): Количество действий для выполнения. По умолчанию `None`.
- `return_actions` (bool, optional): Возвращать ли действия. По умолчанию `False`.
- `max_content_length` (int, optional): Максимальная длина отображаемого контента.

**Возвращает**:

- `Optional[list]`: Список действий, если `return_actions` равно `True`.

#### `listen`

```python
@transactional
def listen(self, speech, source: AgentOrWorld = None, max_content_length=default["max_content_display_length"]) -> TinyPerson
```

**Описание**: Слушает другого агента и обновляет свое внутреннее когнитивное состояние.

**Параметры**:

- `speech` (str): Речь для прослушивания.
- `source` (AgentOrWorld, optional): Источник речи. По умолчанию `None`.
- `max_content_length` (int, optional): Максимальная длина отображаемого контента.

**Возвращает**:

- `TinyPerson`: Сам агент, для облегчения цепочки вызовов.

#### `socialize`

```python
def socialize(self, social_description: str, source: AgentOrWorld = None, max_content_length=default["max_content_display_length"]) -> TinyPerson
```

**Описание**: Воспринимает социальный стимул через описание и обновляет свое внутреннее когнитивное состояние.

**Параметры**:

- `social_description` (str): Описание социального стимула.
- `source` (AgentOrWorld, optional): Источник социального стимула. По умолчанию `None`.
- `max_content_length` (int, optional): Максимальная длина отображаемого контента.

**Возвращает**:

- `TinyPerson`: Сам агент, для облегчения цепочки вызовов.

#### `see`

```python
def see(self, visual_description, source: AgentOrWorld = None, max_content_length=default["max_content_display_length"]) -> TinyPerson
```

**Описание**: Воспринимает визуальный стимул через описание и обновляет свое внутреннее когнитивное состояние.

**Параметры**:

- `visual_description` (str): Описание визуального стимула.
- `source` (AgentOrWorld, optional): Источник визуального стимула. По умолчанию `None`.
- `max_content_length` (int, optional): Максимальная длина отображаемого контента.

**Возвращает**:

- `TinyPerson`: Сам агент, для облегчения цепочки вызовов.

#### `think`

```python
def think(self, thought, max_content_length=default["max_content_display_length"]) -> TinyPerson
```

**Описание**: Заставляет агента думать о чем-то и обновляет свое внутреннее когнитивное состояние.

**Параметры**:

- `thought` (str): Мысль для обдумывания.
- `max_content_length` (int, optional): Максимальная длина отображаемого контента.

**Возвращает**:

- `TinyPerson`: Сам агент, для облегчения цепочки вызовов.

#### `internalize_goal`

```python
def internalize_goal(self, goal, max_content_length=default["max_content_display_length"]) -> TinyPerson
```

**Описание**: Интериоризирует цель и обновляет свое внутреннее когнитивное состояние.

**Параметры**:

- `goal` (str): Цель для интериоризации.
- `max_content_length` (int, optional): Максимальная длина отображаемого контента.

**Возвращает**:

- `TinyPerson`: Сам агент, для облегчения цепочки вызовов.

#### `_observe`

```python
@transactional
def _observe(self, stimulus, max_content_length=default["max_content_display_length"]) -> TinyPerson
```

**Описание**: Наблюдает за стимулом и обновляет свое внутреннее когнитивное состояние.

**Параметры**:

- `stimulus` (dict): Стимул для наблюдения.
- `max_content_length` (int, optional): Максимальная длина отображаемого контента.

**Возвращает**:

- `TinyPerson`: Сам агент, для облегчения цепочки вызовов.

#### `listen_and_act`

```python
@transactional
def listen_and_act(self, speech, return_actions=False, max_content_length=default["max_content_display_length"]) -> Optional[list]
```

**Описание**: Удобный метод, который объединяет методы `listen` и `act`.

**Параметры**:

- `speech` (str): Речь для прослушивания.
- `return_actions` (bool, optional): Возвращать ли действия. По умолчанию `False`.
- `max_content_length` (int, optional): Максимальная длина отображаемого контента.

**Возвращает**:

- `Optional[list]`: Список действий, если `return_actions` равно `True`.

#### `see_and_act`

```python
@transactional
def see_and_act(self, visual_description, return_actions=False, max_content_length=default["max_content_display_length"]) -> Optional[list]
```

**Описание**: Удобный метод, который объединяет методы `see` и `act`.

**Параметры**:

- `visual_description` (str): Описание визуального стимула.
- `return_actions` (bool, optional): Возвращать ли действия. По умолчанию `False`.
- `max_content_length` (int, optional): Максимальная длина отображаемого контента.

**Возвращает**:

- `Optional[list]`: Список действий, если `return_actions` равно `True`.

#### `think_and_act`

```python
@transactional
def think_and_act(self, thought, return_actions=False, max_content_length=default["max_content_display_length"]) -> Optional[list]
```

**Описание**: Удобный метод, который объединяет методы `think` и `act`.

**Параметры**:

- `thought` (str): Мысль для обдумывания.
- `return_actions` (bool, optional): Возвращать ли действия. По умолчанию `False`.
- `max_content_length` (int, optional): Максимальная длина отображаемого контента.

**Возвращает**:

- `Optional[list]`: Список действий, если `return_actions` равно `True`.

#### `read_documents_from_folder`

```python
def read_documents_from_folder(self, documents_path: str) -> None
```

**Описание**: Читает документы из каталога и загружает их в семантическую память.

**Параметры**:

- `documents_path` (str): Путь к каталогу с документами.

#### `read_documents_from_web`

```python
def read_documents_from_web(self, web_urls: list) -> None
```

**Описание**: Читает документы из веб-адресов и загружает их в семантическую память.

**Параметры**:

- `web_urls` (list): Список веб-адресов.

#### `move_to`

```python
@transactional
def move_to(self, location, context: list = []) -> None
```

**Описание**: Перемещается в новое место и обновляет свое внутреннее когнитивное состояние.

**Параметры**:

- `location` (Any): Новое местоположение.
- `context` (list, optional): Контекст нового местоположения. По умолчанию `[]`.

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

- `agent` (TinyPerson): Агент, который становится доступным.
- `relation_description` (str, optional): Описание отношений. По умолчанию "An agent I can currently interact with.".

#### `make_agent_inaccessible`

```python
@transactional
def make_agent_inaccessible(self, agent: Self) -> None
```

**Описание**: Делает агента недоступным для этого агента.

**Параметры**:

- `agent` (TinyPerson): Агент, который становится недоступным.

#### `make_all_agents_inaccessible`

```python
@transactional
def make_all_agents_inaccessible(self) -> None
```

**Описание**: Делает всех агентов недоступными для этого агента.

#### `_produce_message`

```python
@transactional
def _produce_message(self) -> tuple
```

**Описание**: Создает следующее сообщение, используя OpenAI API.

**Возвращает**:

- `tuple`: Роль и содержимое сообщения.

#### `_update_cognitive_state`

```python
@transactional
def _update_cognitive_state(self, goals=None, context=None, attention=None, emotions=None) -> None
```

**Описание**: Обновляет когнитивное состояние `TinyPerson`.

**Параметры**:

- `goals` (list, optional): Новые цели. По умолчанию `None`.
- `context` (list, optional): Новый контекст. По умолчанию `None`.
- `attention` (str, optional): Новое внимание. По умолчанию `None`.
- `emotions` (str, optional): Новые эмоции. По умолчанию `None`.

#### `_display_communication`

```python
def _display_communication(self, role, content, kind, simplified=True, max_content_length=default["max_content_display_length"]) -> None
```

**Описание**: Отображает текущее сообщение и сохраняет его в буфере для последующего использования.

**Параметры**:

- `role` (str): Роль отправителя сообщения.
- `content` (dict): Содержание сообщения.
- `kind` (str): Тип сообщения.
- `simplified` (bool, optional): Упрощенное отображение. По умолчанию `True`.
- `max_content_length` (int, optional): Максимальная длина отображаемого контента.

#### `_push_and_display_latest_communication`

```python
def _push_and_display_latest_communication(self, rendering) -> None
```

**Описание**: Добавляет последние сообщения в буфер агента.

**Параметры**:

- `rendering` (str): Отображаемое сообщение.

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

**Описание**: Возвращает последние действия, выполненные этим агентом.

**Возвращает**:

- `list`: Список последних действий.

#### `pop_actions_and_get_contents_for`

```python
@transactional
def pop_actions_and_get_contents_for(self, action_type: str, only_last_action: bool = True) -> list
```

**Описание**: Возвращает содержимое действий заданного типа, выполненных этим агентом.

**Параметры**:

- `action_type` (str): Тип действия для поиска.
- `only_last_action` (bool, optional): Возвращать ли только последнее действие. По умолчанию `True`.

**Возвращает**:

- `list`: Содержимое действий.

#### `__repr__`

```python
def __repr__(self) -> str
```

**Описание**: Возвращает строковое представление объекта.

**Возвращает**:

- `str`: Строковое представление объекта.

#### `minibio`

```python
def minibio(self) -> str
```

**Описание**: Возвращает мини-биографию `TinyPerson`.

**Возвращает**:

- `str`: Мини-биография агента.

#### `pp_current_interactions`

```python
def pp_current_interactions(self, simplified=True, skip_system=True, max_content_length=default["max_content_display_length"]) -> None
```

**Описание**: Выводит текущие сообщения в красивом формате.

**Параметры**:

- `simplified` (bool, optional): Упрощенное отображение. По умолчанию `True`.
- `skip_system` (bool, optional): Пропускать системные сообщения. По умолчанию `True`.
- `max_content_length` (int, optional): Максимальная длина отображаемого контента.

#### `pretty_current_interactions`

```python
def pretty_current_interactions(self, simplified=True, skip_system=True, max_content_length=default["max_content_display_length"], first_n=None, last_n=None, include_omission_info:bool=True) -> str
```

**Описание**: Возвращает текущие сообщения в красивом, читаемом формате в виде строки.

**Параметры**:

- `simplified` (bool, optional): Упрощенное отображение. По умолчанию `True`.
- `skip_system` (bool, optional): Пропускать системные сообщения. По умолчанию `True`.
- `max_content_length` (int, optional): Максимальная длина отображаемого контента.
- `first_n` (int, optional): Количество первых сообщений для отображения. По умолчанию `None`.
- `last_n` (int, optional): Количество последних сообщений для отображения. По умолчанию `None`.
- `include_omission_info` (bool, optional): Включать ли информацию об опущенных сообщениях. По умолчанию `True`.

**Возвращает**:

- `str`: Красивая, читаемая строка с текущими сообщениями.

#### `_pretty_stimuli`

```python
def _pretty_stimuli(self, role, content, simplified=True, max_content_length=default["max_content_display_length"]) -> str
```

**Описание**: Выводит стимулы в красивом формате.

**Параметры**:

- `role` (str): Роль отправителя сообщения.
- `content` (dict): Содержание сообщения.
- `simplified` (bool, optional): Упрощенное отображение. По умолчанию `True`.
- `max_content_length` (int, optional): Максимальная длина отображаемого контента.

**Возвращает**:

- `str`: Строка отформатированного стимула.

#### `_pretty_action`

```python
def _pretty_action(self, role, content, simplified=True, max_content_length=default["max_content_display_length"]) -> str
```

**Описание**: Выводит действие в красивом формате.

**Параметры**:

- `role` (str): Роль отправителя сообщения.
- `content` (dict): Содержание сообщения.
- `simplified` (bool, optional): Упрощенное отображение. По умолчанию `True`.
- `max_content_length` (int, optional): Максимальная длина отображаемого контента.

**Возвращает**:

- `str`: Строка отформатированного действия.

#### `_pretty_timestamp`

```python
def _pretty_timestamp(self, role, timestamp) -> str
```

**Описание**: Выводит метку времени в красивом формате.

**Параметры**:

- `role` (str): Роль сообщения.
- `timestamp` (str): Метка времени.

**Возвращает**:

- `str`: Строка отформатированной метки времени.

#### `iso_datetime`

```python
def iso_datetime(self) -> Optional[str]
```

**Описание**: Возвращает текущее время окружения в формате ISO.

**Возвращает**:

- `Optional[str]`: Текущее время окружения в формате ISO или `None`, если нет окружения.

#### `save_spec`

```python
def save_spec(self, path, include_mental_faculties=True, include_memory=False) -> None
```

**Описание**: Сохраняет текущую конфигурацию в JSON-файл.

**Параметры**:

- `path` (str): Путь к JSON-файлу.
- `include_mental_faculties` (bool, optional): Включать ли ментальные способности. По умолчанию `True`.
- `include_memory` (bool, optional): Включать ли память. По умолчанию `False`.

#### `load_spec`

```python
@staticmethod
def load_spec(path, suppress_mental_faculties=False, suppress_memory=False, auto_rename_agent=False, new_agent_name=None) -> Self
```

**Описание**: Загружает спецификацию агента из JSON-файла.

**Параметры**:

- `path` (str): Путь к JSON-файлу.
- `suppress_mental_faculties` (bool, optional): Подавлять ли загрузку ментальных способностей. По умолчанию `False`.
- `suppress_memory` (bool, optional): Подавлять ли загрузку памяти. По умолчанию `False`.
- `auto_rename_agent` (bool, optional): Автоматически переименовывать ли агента. По умолчанию `False`.
- `new_agent_name` (str, optional): Новое имя агента. По умолчанию `None`.

**Возвращает**:

- `Self`: Новый экземпляр `TinyPerson`.

#### `encode_complete_state`

```python
def encode_complete_state(self) -> dict
```

**Описание**: Кодирует полное состояние `TinyPerson`, включая текущие сообщения, доступных агентов и т.д.

**Возвращает**:

- `dict`: Полное состояние агента.

#### `decode_complete_state`

```python
def decode_complete_state(self, state: dict) -> Self
```

**Описание**: Загружает полное состояние `TinyPerson`, включая текущие сообщения, и создает новый экземпляр `TinyPerson`.

**Параметры**:

- `state` (dict): Полное состояние агента.

**Возвращает**:

- `Self`: Новый экземпляр `TinyPerson`.

#### `create_new_agent_from_current_spec`

```python
def create_new_agent_from_current_spec(self, new_name: str) -> Self
```

**Описание**: Создает нового агента на основе текущей спецификации.

**Параметры**:

- `new_name` (str): Имя нового агента.

**Возвращает**:

- `Self`: Новый экземпляр `TinyPerson`.

#### `add_agent`

```python
@staticmethod
def add_agent(agent) -> None
```

**Описание**: Добавляет агента в глобальный список агентов.

**Параметры**:

- `agent` (TinyPerson): Агент для добавления.

**Вызывает исключения**:

- `ValueError`: Если имя агента уже используется.

#### `has_agent`

```python
@staticmethod
def has_agent(agent_name: str) -> bool
```

**Описание**: Проверяет, зарегистрирован ли агент.

**Параметры**:

- `agent_name` (str): Имя агента.

**Возвращает**:

- `bool`: `True`, если агент зарегистрирован, `False` иначе.

#### `set_simulation_for_free_agents`

```python
@staticmethod
def set_simulation_for_free_agents(simulation) -> None
```

**Описание**: Устанавливает симуляцию для свободных агентов.

**Параметры**:

- `simulation` (Any): Симуляция.

#### `get_agent_by_name`

```python
@staticmethod
def get_agent_by_name(name) -> Optional[TinyPerson]
```

**Описание**: Получает агента по имени.

**Параметры**:

- `name` (str): Имя агента.

**Возвращает**:

- `Optional[TinyPerson]`: Экземпляр агента или `None`, если агент не найден.

#### `clear_agents`

```python
@staticmethod
def clear_agents() -> None
```

**Описание**: Очищает глобальный список агентов.

### `TinyMentalFaculty`

**Описание**: Представляет ментальную способность агента.

**Методы**:

#### `__init__`

```python
def __init__(self, name: str, requires_faculties: list = None) -> None
```

**Описание**: Инициализирует ментальную способность.

**Параметры**:

- `name` (str): Имя ментальной способности.
- `requires_faculties` (list, optional): Список ментальных способностей, необходимых для корректной работы этой способности. По умолчанию `None`.

#### `__str__`

```python
def __str__(self) -> str
```

**Описание**: Возвращает строковое представление объекта.

**Возвращает**:

- `str`: Строковое представление объекта.

#### `__eq__`

```python
def __eq__(self, other) -> bool
```

**Описание**: Проверяет равенство ментальных способностей.

**Параметры**:

- `other` (TinyMentalFaculty): Другая ментальная способность.

**Возвращает**:

- `bool`: `True`, если способности равны, `False` иначе.

#### `process_action`

```python
def process_action(self, agent, action: dict) -> bool
```

**Описание**: Обрабатывает действие, связанное с этой способностью.

**Параметры**:

- `agent` (TinyPerson): Агент.
- `action` (dict): Действие для обработки.

**Возвращает**:

- `bool`: `True`, если действие было успешно обработано, `False` иначе.

**Вызывает исключения**:

- `NotImplementedError`: Если подкласс не реализует этот метод.

#### `actions_definitions_prompt`

```python
def actions_definitions_prompt(self) -> str
```

**Описание**: Возвращает промпт для определения действий, связанных с этой способностью.

**Возвращает**:

- `str`: Промпт для определения действий.

**Вызывает исключения**:

- `NotImplementedError`: Если подкласс не реализует этот метод.

#### `actions_constraints_prompt`

```python
def actions_constraints_prompt(self) -> str
```

**Описание**: Возвращает промпт для определения ограничений на действия, связанные с этой способностью.

**Возвращает**:

- `str`: Промпт для определения ограничений на действия.

**Вызывает исключения**:

- `NotImplementedError`: Если подкласс не реализует этот метод.

### `RecallFaculty`

**Описание**: Ментальная способность для извлечения информации из памяти.

**Методы**:

#### `__init__`

```python
def __init__(self) -> None
```

**Описание**: Инициализирует способность извлечения памяти.

#### `process_action`

```python
def process_action(self, agent, action: dict) -> bool
```

**Описание**: Обрабатывает действие, связанное с извлечением памяти.

**Параметры**:

- `agent` (TinyPerson): Агент.
- `action` (dict): Действие для обработки.

**Возвращает**:

- `bool`: `True`, если действие было успешно обработано, `False` иначе.

#### `actions_definitions_prompt`

```python
def actions_definitions_prompt(self) -> str
```

**Описание**: Возвращает промпт для определения действий извлечения памяти.

**Возвращает**:

- `str`: Промпт для определения действий извлечения памяти.

#### `actions_constraints_prompt`

```python
def actions_constraints_prompt(self) -> str
```

**Описание**: Возвращает промпт для определения ограничений на действия извлечения памяти.

**Возвращает**:

- `str`: Промпт для определения ограничений на действия извлечения памяти.

### `FilesAndWebGroundingFaculty`

**Описание**: Ментальная способность для доступа к локальным файлам и веб-страницам.

**Методы**:

#### `__init__`

```python
def __init__(self) -> None
```

**Описание**: Инициализирует способность доступа к файлам и веб-страницам.

#### `process_action`

```python
def process_action(self, agent, action: dict) -> bool
```

**Описание**: Обрабатывает действие, связанное с доступом к файлам и веб-страницам.

**Параметры**:

- `agent` (TinyPerson): Агент.
- `action` (dict): Действие для обработки.

**Возвращает**:

- `bool`: `True`, если действие было успешно обработано, `False` иначе.

#### `actions_definitions_prompt`

```python
def actions_definitions_prompt(self) -> str
```

**Описание**: Возвращает промпт для определения действий доступа к файлам и веб-страницам.

**Возвращает**:

- `str`: Промпт для определения действий доступа к файлам и веб-страницам.

#### `actions_constraints_prompt`

```python
def actions_constraints_prompt(self) -> str
```

**Описание**: Возвращает промпт для определения ограничений на действия доступа к файлам и веб-страницам.

**Возвращает**:

- `str`: Промпт для определения ограничений на действия доступа к файлам и веб-страницам.

### `TinyToolUse`

**Описание**: Ментальная способность для использования инструментов.

**Методы**:

#### `__init__`

```python
def __init__(self, tools: list) -> None
```

**Описание**: Инициализирует способность