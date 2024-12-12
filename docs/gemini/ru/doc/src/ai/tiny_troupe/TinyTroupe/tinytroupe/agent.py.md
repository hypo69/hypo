# Модуль `agent.py`

## Обзор

Этот модуль предоставляет основные классы и функции для агентов TinyTroupe.

Агенты — это ключевая абстракция, используемая в TinyTroupe. Агент — это моделируемый человек или сущность, которая может взаимодействовать с другими агентами и окружающей средой, получая стимулы и производя действия. Агенты имеют когнитивные состояния, которые обновляются по мере их взаимодействия с окружающей средой и другими агентами. Они также могут хранить и извлекать информацию из памяти, а также выполнять действия в окружающей среде. В отличие от агентов, целью которых является поддержка помощников на основе ИИ или других подобных инструментов повышения производительности, **агенты TinyTroupe нацелены на представление человекоподобного поведения**, которое включает идиосинкразии, эмоции и другие человекоподобные черты, которые не ожидаются от инструмента повышения производительности.

Общий лежащий в основе дизайн вдохновлен в основном когнитивной психологией, поэтому агенты имеют различные внутренние когнитивные состояния, такие как внимание, эмоции и цели. Именно поэтому память агента, в отличие от других платформ агентов на основе LLM, имеет тонкие внутренние разделения, особенно между эпизодической и семантической памятью. Также присутствуют некоторые бихевиористские концепции, такие как идея «стимула» и «реакции» в методах `listen` и `act`, которые являются ключевыми абстракциями для понимания того, как агенты взаимодействуют с окружающей средой и другими агентами.

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
- [Функции](#функции)
    - [`default`](#default)

## Классы

### `TinyPerson`

**Описание**: Симулируемый человек во вселенной TinyTroupe.

**Атрибуты**:
- `MAX_ACTIONS_BEFORE_DONE` (int): Максимальное количество действий, которые агент может выполнить перед завершением.
- `PP_TEXT_WIDTH` (int): Ширина текста для отображения.
- `serializable_attributes` (list): Список атрибутов, которые можно сериализовать.
- `all_agents` (dict): Словарь всех созданных агентов (`name` -> `agent`).
- `communication_style` (str): Стиль общения агентов.
- `communication_display` (bool): Флаг отображения общения.

**Методы**:

#### `__init__`

```python
def __init__(self, name: str = None, episodic_memory=None, semantic_memory=None, mental_faculties: list = None) -> None:
    """
    Args:
        name (str): Имя TinyPerson. Либо это, либо spec_path должны быть указаны.
        episodic_memory (EpisodicMemory, optional): Реализация памяти для использования. По умолчанию `EpisodicMemory()`.
        semantic_memory (SemanticMemory, optional): Реализация памяти для использования. По умолчанию `SemanticMemory()`.
        mental_faculties (list, optional): Список умственных способностей для добавления агенту. По умолчанию `None`.
    """
```
**Описание**: Создает `TinyPerson`.

#### `_post_init`

```python
def _post_init(self, **kwargs):
    """
    Args:
        kwargs (dict):  Произвольные именованные аргументы.
    """
```
**Описание**: Этот метод выполняется после `__init__`, так как класс имеет декоратор `@post_init`. Он удобен для разделения некоторых процессов инициализации, чтобы упростить десериализацию.

#### `_rename`

```python
def _rename(self, new_name: str) -> None:
    """
    Args:
        new_name (str):  Новое имя агента.
    """
```
**Описание**: Переименовывает агента.

#### `generate_agent_prompt`
```python
def generate_agent_prompt(self) -> str:
    """
    Returns:
        str: Шаблон промпта агента.
    """
```
**Описание**: Генерирует промпт агента на основе шаблона.

#### `reset_prompt`
```python
def reset_prompt(self) -> None:
    """
    Resets the agent's prompt.
    """
```
**Описание**: Сбрасывает промпт агента.

#### `get`
```python
def get(self, key) -> Any:
    """
    Args:
        key (Any): ключ для получения значения.

    Returns:
        Any: Значение ключа в конфигурации `TinyPerson`.
    """
```
**Описание**: Возвращает определение ключа в конфигурации `TinyPerson`.

#### `define`
```python
def define(self, key, value, group=None) -> None:
    """
    Args:
        key (Any): ключ, который нужно определить.
        value (Any): значение, которое нужно определить.
        group (Any, optional): Группа, к которой относится ключ. Defaults to None.
    """
```
**Описание**: Определяет значение в конфигурации `TinyPerson`.

#### `define_several`
```python
def define_several(self, group, records) -> None:
    """
    Args:
        group (Any): группа, к которой принадлежат значения.
        records (list): список записей для определения.
    """
```
**Описание**: Определяет несколько значений в конфигурации `TinyPerson`, принадлежащих к одной группе.

#### `define_relationships`
```python
def define_relationships(self, relationships, replace=True) -> None:
    """
    Args:
        relationships (list or dict): Отношения, которые нужно добавить или заменить. Либо список словарей, отображающих имена агентов на описания отношений, или один словарь, отображающий одно имя агента на описание его отношения.
        replace (bool, optional): Следует ли заменить текущие отношения или просто добавить к ним. Defaults to True.

    Raises:
        Exception: если аргументы недействительны.
    """
```
**Описание**: Определяет или обновляет отношения `TinyPerson`.

#### `clear_relationships`
```python
def clear_relationships(self) -> Self:
    """
    Returns:
        Self: Сам агент для упрощения связывания.
    """
```
**Описание**: Очищает отношения `TinyPerson`.

#### `related_to`
```python
def related_to(self, other_agent: Self, description: str, symmetric_description: str = None) -> Self:
    """
    Args:
        other_agent (TinyPerson): другой агент.
        description (str): описание отношения.
        symmetric_description (str, optional): Описание симметричного отношения. Defaults to None.

    Returns:
        Self: сам агент для упрощения связывания.
    """
```
**Описание**: Определяет отношение между этим агентом и другим агентом.

#### `add_mental_faculties`
```python
def add_mental_faculties(self, mental_faculties) -> Self:
    """
    Args:
        mental_faculties (list): список умственных способностей для добавления агенту.

    Returns:
        Self: сам агент для упрощения связывания.
    """
```
**Описание**: Добавляет список ментальных способностей агенту.

#### `add_mental_faculty`
```python
def add_mental_faculty(self, faculty) -> Self:
    """
    Args:
        faculty (Any): Ментальная способность для добавления агенту.

    Returns:
       Self: сам агент для упрощения связывания.

    Raises:
        Exception: если ментальная способность уже присутствует у агента.
    """
```
**Описание**: Добавляет ментальную способность агенту.

#### `act`
```python
def act(self, until_done=True, n=None, return_actions=False, max_content_length=default["max_content_display_length"]) -> list | None:
    """
    Args:
        until_done (bool, optional): Следует ли продолжать действие, пока агент не будет завершен и не потребуются дополнительные стимулы. Defaults to True.
        n (int, optional): Количество действий для выполнения. Defaults to None.
        return_actions (bool, optional): Следует ли возвращать действия или нет. Defaults to False.
        max_content_length (int, optional): Максимальная длина контента для отображения. Defaults to `default["max_content_display_length"]`.

    Returns:
        list | None: Список действий, если `return_actions` равен True, иначе `None`.

    Raises:
        AssertionError: если и `until_done`, и `n` определены, или `n` больше чем `TinyPerson.MAX_ACTIONS_BEFORE_DONE`.
    """
```
**Описание**: Действует в окружающей среде и обновляет свое внутреннее когнитивное состояние. Либо действует до тех пор, пока агент не завершит работу и не потребуются дополнительные стимулы, либо действует фиксированное количество раз, но не оба варианта.

#### `listen`
```python
def listen(self, speech, source: AgentOrWorld = None, max_content_length=default["max_content_display_length"]) -> Self:
    """
    Args:
        speech (str): Речь для прослушивания.
        source (AgentOrWorld, optional): Источник речи. По умолчанию `None`.
        max_content_length (int, optional): Максимальная длина контента для отображения. Defaults to `default["max_content_display_length"]`.

    Returns:
        Self: сам агент для упрощения связывания.
    """
```
**Описание**: Слушает другого агента (искусственного или человека) и обновляет свое внутреннее когнитивное состояние.

#### `socialize`
```python
def socialize(self, social_description: str, source: AgentOrWorld = None, max_content_length=default["max_content_display_length"]) -> Self:
    """
    Args:
        social_description (str): описание социального стимула.
        source (AgentOrWorld, optional): источник социального стимула. По умолчанию `None`.
        max_content_length (int, optional): Максимальная длина контента для отображения. Defaults to `default["max_content_display_length"]`.

    Returns:
       Self: сам агент для упрощения связывания.
    """
```
**Описание**: Воспринимает социальный стимул через описание и обновляет свое внутреннее когнитивное состояние.

#### `see`
```python
def see(self, visual_description: str, source: AgentOrWorld = None, max_content_length=default["max_content_display_length"]) -> Self:
    """
    Args:
        visual_description (str): описание визуального стимула.
        source (AgentOrWorld, optional): источник визуального стимула. По умолчанию `None`.
        max_content_length (int, optional): Максимальная длина контента для отображения. Defaults to `default["max_content_display_length"]`.
    
    Returns:
        Self: сам агент для упрощения связывания.
    """
```
**Описание**: Воспринимает визуальный стимул через описание и обновляет свое внутреннее когнитивное состояние.

#### `think`
```python
def think(self, thought: str, max_content_length=default["max_content_display_length"]) -> Self:
    """
    Args:
        thought (str): мысль агента.
        max_content_length (int, optional): Максимальная длина контента для отображения. Defaults to `default["max_content_display_length"]`.

    Returns:
        Self: сам агент для упрощения связывания.
    """
```
**Описание**: Заставляет агента подумать о чем-то и обновляет его внутреннее когнитивное состояние.

#### `internalize_goal`
```python
def internalize_goal(self, goal: str, max_content_length=default["max_content_display_length"]) -> Self:
    """
    Args:
        goal (str): цель агента.
        max_content_length (int, optional): Максимальная длина контента для отображения. Defaults to `default["max_content_display_length"]`.

    Returns:
        Self: сам агент для упрощения связывания.
    """
```
**Описание**: Внушает цель и обновляет внутреннее когнитивное состояние.

#### `_observe`
```python
def _observe(self, stimulus, max_content_length=default["max_content_display_length"]) -> Self:
    """
    Args:
        stimulus (dict): стимул для наблюдения.
        max_content_length (int, optional): Максимальная длина контента для отображения. Defaults to `default["max_content_display_length"]`.

    Returns:
        Self: сам агент для упрощения связывания.
    """
```
**Описание**: Наблюдает за стимулом и обновляет свое внутреннее когнитивное состояние.

#### `listen_and_act`
```python
def listen_and_act(self, speech, return_actions=False, max_content_length=default["max_content_display_length"]) -> list | None:
    """
    Args:
        speech (str): Речь для прослушивания.
        return_actions (bool, optional): Следует ли возвращать действия или нет. Defaults to False.
        max_content_length (int, optional): Максимальная длина контента для отображения. Defaults to `default["max_content_display_length"]`.

    Returns:
        list | None:  Список действий, если `return_actions` равен True, иначе `None`.
    """
```
**Описание**: Удобный метод, который объединяет методы `listen` и `act`.

#### `see_and_act`
```python
def see_and_act(self, visual_description, return_actions=False, max_content_length=default["max_content_display_length"]) -> list | None:
    """
    Args:
        visual_description (str): описание визуального стимула.
        return_actions (bool, optional): Следует ли возвращать действия или нет. Defaults to False.
        max_content_length (int, optional): Максимальная длина контента для отображения. Defaults to `default["max_content_display_length"]`.

    Returns:
        list | None: Список действий, если `return_actions` равен True, иначе `None`.
    """
```
**Описание**: Удобный метод, который объединяет методы `see` и `act`.

#### `think_and_act`
```python
def think_and_act(self, thought, return_actions=False, max_content_length=default["max_content_display_length"]) -> list | None:
    """
    Args:
        thought (str): мысль агента.
        return_actions (bool, optional): Следует ли возвращать действия или нет. Defaults to False.
        max_content_length (int, optional): Максимальная длина контента для отображения. Defaults to `default["max_content_display_length"]`.
    
    Returns:
        list | None: Список действий, если `return_actions` равен True, иначе `None`.
    """
```
**Описание**: Удобный метод, который объединяет методы `think` и `act`.

#### `read_documents_from_folder`
```python
def read_documents_from_folder(self, documents_path: str) -> None:
    """
    Args:
        documents_path (str): Путь к папке с документами.
    """
```
**Описание**: Читает документы из каталога и загружает их в семантическую память.

#### `read_documents_from_web`
```python
def read_documents_from_web(self, web_urls: list) -> None:
    """
    Args:
        web_urls (list): Список веб-URL.
    """
```
**Описание**: Читает документы с веб-URL-адресов и загружает их в семантическую память.

#### `move_to`
```python
def move_to(self, location, context=[]) -> None:
    """
    Args:
        location (Any): Новое местоположение агента.
        context (list, optional): Контекст местоположения. Defaults to [].
    """
```
**Описание**: Перемещается в новое местоположение и обновляет свое внутреннее когнитивное состояние.

#### `change_context`
```python
def change_context(self, context: list) -> None:
    """
    Args:
        context (list): контекст, который нужно установить.
    """
```
**Описание**: Изменяет контекст и обновляет свое внутреннее когнитивное состояние.

#### `make_agent_accessible`
```python
def make_agent_accessible(self, agent: Self, relation_description: str = "An agent I can currently interact with.") -> None:
    """
    Args:
        agent (Self): Агент, который должен стать доступным.
        relation_description (str, optional): Описание отношения между агентами. Defaults to "An agent I can currently interact with.".
    """
```
**Описание**: Делает агента доступным для этого агента.

#### `make_agent_inaccessible`
```python
def make_agent_inaccessible(self, agent: Self) -> None:
    """
    Args:
        agent (Self): Агент, который должен стать недоступным.
    """
```
**Описание**: Делает агента недоступным для этого агента.

#### `make_all_agents_inaccessible`
```python
def make_all_agents_inaccessible(self) -> None:
    """
    Makes all agents inaccessible to this agent.
    """
```
**Описание**: Делает всех агентов недоступными для этого агента.

#### `_produce_message`
```python
def _produce_message(self) -> tuple[str, dict]:
    """
    Returns:
        tuple[str, dict]: Роль и содержимое следующего сообщения.
    """
```
**Описание**: Создает следующее сообщение, используя OpenAI API.

#### `_update_cognitive_state`
```python
def _update_cognitive_state(self, goals=None, context=None, attention=None, emotions=None) -> None:
    """
    Args:
        goals (list, optional): Цели агента. Defaults to None.
        context (list, optional): Контекст агента. Defaults to None.
        attention (str, optional): Внимание агента. Defaults to None.
        emotions (str, optional): Эмоции агента. Defaults to None.
    """
```
**Описание**: Обновляет когнитивное состояние `TinyPerson`.

#### `_display_communication`
```python
def _display_communication(self, role, content, kind, simplified=True, max_content_length=default["max_content_display_length"]) -> None:
    """
    Args:
        role (str): Роль коммуникатора.
        content (dict): Содержание общения.
        kind (str): Тип общения.
        simplified (bool, optional): Следует ли упрощать общение. Defaults to True.
        max_content_length (int, optional): Максимальная длина контента для отображения. Defaults to `default["max_content_display_length"]`.
    
    Raises:
        ValueError: если `kind` неизвестен.
    """
```
**Описание**: Отображает текущее общение и сохраняет его в буфере для последующего использования.

#### `_push_and_display_latest_communication`
```python
def _push_and_display_latest_communication(self, rendering) -> None:
    """
    Args:
        rendering (str): текст коммуникации.
    """
```
**Описание**: Добавляет последние сообщения в буфер агента.

#### `pop_and_display_latest_communications`
```python
def pop_and_display_latest_communications(self) -> list:
    """
    Returns:
        list: Последние коммуникации.
    """
```
**Описание**: Извлекает последние сообщения и отображает их.

#### `clear_communications_buffer`
```python
def clear_communications_buffer(self) -> None:
    """
    Clears the communications buffer.
    """
```
**Описание**: Очищает буфер сообщений.

#### `pop_latest_actions`
```python
def pop_latest_actions(self) -> list:
    """
    Returns:
        list: Последние действия, выполненные этим агентом.
    """
```
**Описание**: Возвращает последние действия, выполненные этим агентом.

#### `pop_actions_and_get_contents_for`
```python
def pop_actions_and_get_contents_for(self, action_type: str, only_last_action: bool = True) -> list | str:
    """
    Args:
        action_type (str): Тип действия для поиска.
        only_last_action (bool, optional): Следует ли возвращать только содержимое последнего действия. Defaults to True.

    Returns:
        list | str: Содержимое действий заданного типа.
    """
```
**Описание**: Возвращает содержимое действий заданного типа, выполненных этим агентом.

#### `__repr__`
```python
def __repr__(self) -> str:
    """
    Returns:
        str: Представление агента.
    """
```
**Описание**: Возвращает строковое представление `TinyPerson`.

#### `minibio`
```python
def minibio(self) -> str:
    """
    Returns:
        str: Мини-биография агента.
    """
```
**Описание**: Возвращает мини-биографию `TinyPerson`.

#### `pp_current_interactions`
```python
def pp_current_interactions(self, simplified=True, skip_system=True, max_content_length=default["max_content_display_length"]) -> None:
    """
    Args:
        simplified (bool, optional): Следует ли упрощать сообщения. Defaults to True.
        skip_system (bool, optional): Следует ли пропускать системные сообщения. Defaults to True.
        max_content_length (int, optional): Максимальная длина контента для отображения. Defaults to `default["max_content_display_length"]`.
    """
```
**Описание**: Выводит текущие сообщения в удобном для чтения формате.

#### `pretty_current_interactions`
```python
def pretty_current_interactions(self, simplified=True, skip_system=True, max_content_length=default["max_content_display_length"], first_n=None, last_n=None, include_omission_info: bool = True) -> str:
    """
    Args:
        simplified (bool, optional): Следует ли упрощать сообщения. Defaults to True.
        skip_system (bool, optional): Следует ли пропускать системные сообщения. Defaults to True.
        max_content_length (int, optional): Максимальная длина контента для отображения. Defaults to `default["max_content_display_length"]`.
        first_n (int, optional): Первые n сообщений для извлечения. Defaults to None.
        last_n (int, optional): Последние n сообщений для извлечения. Defaults to None.
        include_omission_info (bool, optional): Включать ли информацию об опущенных сообщениях. Defaults to True.

    Returns:
        str: Строка с отформатированными текущими сообщениями.
    """
```
**Описание**: Возвращает строку с текущими сообщениями в удобном для чтения формате.

#### `_pretty_stimuli`
```python
def _pretty_stimuli(self, role, content, simplified=True, max_content_length=default["max_content_display_length"]) -> str:
    """
    Args:
        role (str): Роль отправителя стимула.
        content (dict): Содержание стимула.
        simplified (bool, optional): Следует ли упрощать отображение. Defaults to True.
        max_content_length (int, optional): Максимальная длина контента для отображения. Defaults to `default["max_content_display_length"]`.

    Returns:
        str: Строка с отформатированным стимулом.
    """
```
**Описание**: Отображает стимулы в удобном для чтения формате.

#### `_pretty_action`
```python
def _pretty_action(self, role, content, simplified=True, max_content_length=default["max_content_display_length"]) -> str:
    """
    Args:
        role (str): Роль отправителя действия.
        content (dict): Содержание действия.
        simplified (bool, optional): Следует ли упрощать отображение. Defaults to True.
        max_content_length (int, optional): Максимальная длина контента для отображения. Defaults to `default["max_content_display_length"]`.

    Returns:
        str: Строка с отформатированным действием.
    """
```
**Описание**: Отображает действие в удобном для чтения формате.

#### `_pretty_timestamp`
```python
def _pretty_timestamp(self, role, timestamp) -> str:
    """
    Args:
        role (str): роль отправителя.
        timestamp (Any): Время события.

    Returns:
        str: Строка с отформатированной меткой времени.
    """
```
**Описание**: Отображает временную метку в удобном для чтения формате.

#### `iso_datetime`
```python
def iso_datetime(self) -> str | None:
    """
    Returns:
        str | None: Текущая дата и время среды в формате ISO.
    """
```
**Описание**: Возвращает текущую дату и время среды, если они есть.

#### `save_spec`
```python
def save_spec(self, path, include_mental_faculties=True, include_memory=False) -> None:
    """
    Args:
        path (str): Путь к файлу для сохранения спецификации.
        include_mental_faculties (bool, optional): Следует ли включать ментальные способности. Defaults to True.
        include_memory (bool, optional): Следует ли включать память. Defaults to False.
    """
```
**Описание**: Сохраняет текущую конфигурацию в файл JSON.

#### `load_spec`
```python
@staticmethod
def load_spec(path, suppress_mental_faculties=False, suppress_memory=False, auto_rename_agent=False, new_agent_name=None) -> Self:
    """
    Args:
        path (str): Путь к файлу JSON, содержащему спецификацию агента.
        suppress_mental_faculties (bool, optional): Следует ли подавлять загрузку умственных способностей. Defaults to False.
        suppress_memory (bool, optional): Следует ли подавлять загрузку памяти. Defaults to False.
        auto_rename_agent (bool, optional): Следует ли автоматически переименовывать агента. Defaults to False.
        new_agent_name (str, optional): Новое имя агента. Defaults to None.
    
    Returns:
        Self: Загруженная спецификация агента.
    """
```
**Описание**: Загружает спецификацию агента из JSON.

#### `encode_complete_state`
```python
def encode_complete_state(self) -> dict:
    """
    Returns:
        dict: Закодированное полное состояние TinyPerson.
    """
```
**Описание**: Кодирует полное состояние TinyPerson, включая текущие сообщения, доступных агентов и т.д.

#### `decode_complete_state`
```python
def decode_complete_state(self, state: dict) -> Self:
    """
    Args:
        state (dict): Состояние TinyPerson для декодирования.
    
    Returns:
        Self: Новый экземпляр `TinyPerson`.
    """
```
**Описание**: Загружает полное состояние `TinyPerson`, включая текущие сообщения, и создает новый экземпляр `TinyPerson`.

#### `create_new_agent_from_current_spec`
```python
def create_new_agent_from_current_spec(self, new_name: str) -> Self:
    """
    Args:
        new_name (str): Имя нового агента.
    
    Returns:
        Self: Новый агент.
    """
```
**Описание**: Создает нового агента из спецификации текущего агента.

#### `add_agent`
```python
@staticmethod
def add_agent(agent) -> None:
    """
    Args:
        agent (TinyPerson): Агент, который нужно добавить.

    Raises:
        ValueError: Если имя агента уже используется.
    """
```
**Описание**: Добавляет агента в глобальный список агентов.

#### `has_agent`
```python
@staticmethod
def has_agent(agent_name: str) -> bool:
    """
    Args:
        agent_name (str): Имя агента для проверки.
    
    Returns:
        bool: `True` если агент существует, иначе `False`.
    """
```
**Описание**: Проверяет, зарегистрирован ли уже агент.

#### `set_simulation_for_free_agents`
```python
@staticmethod
def set_simulation_for_free_agents(simulation) -> None:
    """
    Args:
        simulation (Any): Симуляция.
    """
```
**Описание**: Устанавливает симуляцию, если она равна `None`.

#### `get_agent_by_name`
```python
@staticmethod
def get_agent_by_name(name: str) -> Self | None:
    """
    Args:
        name (str): Имя агента.
    
    Returns:
        Self | None: Агент, если найден, иначе `None`.
    """
```
**Описание**: Возвращает агента по имени.

#### `clear_agents`
```python
@staticmethod
def clear_agents() -> None:
    """
    Clears the global list of agents.
    """
```
**Описание**: Очищает глобальный список агентов.

### `TinyMentalFaculty`

**Описание**: Представляет ментальную способность агента.

**Методы**:

#### `__init__`
```python
def __init__(self, name: str, requires_faculties: list = None) -> None:
    """
    Args:
        name (str): Имя ментальной способности.
        requires_faculties (list, optional): Список ментальных способностей, необходимых для работы этой способности. Defaults to None.
    """
```
**Описание**: Инициализирует ментальную способность.

#### `__str__`
```python
def __str__(self) -> str:
    """
    Returns:
        str: Строковое представление ментальной способности.
    """
```
**Описание**: Возвращает строковое представление ментальной способности.

#### `__eq__`
```python
def __eq__(self, other) -> bool:
    """
    Args:
        other (Any): Объект для сравнения.

    Returns:
        bool: True, если способности равны, иначе False.
    """
```
**Описание**: Проверяет равенство ментальных способностей.

#### `process_action`
```python
def process_action(self, agent, action: dict) -> bool:
    """
    Args:
        agent (TinyPerson): агент, выполняющий действие.
        action (dict): действие для обработки.
    
    Returns:
        bool: True, если действие было успешно обработано, иначе False.

    Raises:
        NotImplementedError: если метод не переопределен в подклассе.
    """
```
**Описание**: Обрабатывает действие, связанное с этой способностью.

#### `actions_definitions_prompt`
```python
def actions_definitions_prompt(self) -> str:
    """
    Returns:
        str: Промпт для определения действий, связанных с этой способностью.

    Raises:
        NotImplementedError: если метод не переопределен в подклассе.
    """
```
**Описание**: Возвращает промпт для определения действий, связанных с этой способностью.

#### `actions_constraints_prompt`
```python
def actions_constraints_prompt(self) -> str:
    """
    Returns:
        str: Промпт для определения ограничений на действия, связанные с этой способностью.

    Raises:
        NotImplementedError: если метод не переопределен в подклассе.
    """
```
**Описание**: Возвращает промпт для определения ограничений на действия, связанные с этой способностью.

### `RecallFaculty`

**Описание**: Ментальная способность для вспоминания информации.

**Методы**:

#### `__init__`
```python
def __init__(self) -> None:
    """
    Initializes the RecallFaculty.
    """
```
**Описание**: Инициализирует способность вспоминания.

#### `process_action`
```python
def process_action(self, agent, action: dict) -> bool:
    """
    Args:
        agent (TinyPerson): Агент, выполняющий действие.
        action (dict): Действие для обработки.

    Returns:
        bool: True, если действие было успешно обработано, иначе False.
    """
```
**Описание**: Обрабатывает действие для вызова воспоминаний.

#### `actions_definitions_prompt`
```python
def actions_definitions_prompt(self) -> str:
    """
    Returns:
        str: Промпт для определения действий, связанных с этой способностью.
    """
```
**Описание**: Возвращает промпт для определения действий, связанных с этой способностью.

#### `actions_constraints_prompt`
```python
def actions_constraints_prompt(self) -> str:
    """
    Returns:
        str: Промпт для определения ограничений на действия, связанные с этой способностью.
    """
```
**Описание**: Возвращает промпт для определения ограничений на действия, связанные с этой способностью.

### `FilesAndWebGroundingFaculty`

**Описание**: Ментальная способность для доступа к локальным файлам и веб-страницам.

**Методы**:

#### `__init__`
```python
def __init__(self) -> None:
    """
    Initializes the FilesAndWebGroundingFaculty.
    """
```
**Описание**: Инициализирует способность доступа к файлам и веб-страницам.

#### `process_action`
```python
def process_action