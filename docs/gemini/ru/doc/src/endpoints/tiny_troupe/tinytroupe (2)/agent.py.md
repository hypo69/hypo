# Модуль agent.py

## Обзор

Модуль предоставляет основные классы и функции для агентов TinyTroupe.
Агенты являются ключевой абстракцией, используемой в TinyTroupe. Агент - это смоделированный человек или сущность,
который может взаимодействовать с другими агентами и окружающей средой, получая стимулы и производя действия.
Агенты имеют когнитивные состояния, которые обновляются по мере их взаимодействия с окружающей средой и другими агентами.
Агенты также могут хранить и извлекать информацию из памяти и выполнять действия в окружающей среде. В отличие от агентов,
целью которых является предоставление поддержки для AI-ассистентов или других подобных инструментов повышения производительности,
**агенты TinyTroupe нацелены на представление человеческого поведения**, которое включает в себя идиосинкразии, эмоции и другие
человеческие черты, которые не следует ожидать от инструмента повышения производительности.

Общий основополагающий дизайн вдохновлен в основном когнитивной психологией, поэтому агенты имеют различные внутренние
когнитивные состояния, такие как внимание, эмоции и цели. Именно поэтому память агента, в отличие от других платформ агентов на основе LLM,
имеет тонкие внутренние разделения, особенно между эпизодической и семантической памятью.
Некоторые бихевиористские концепции также присутствуют, такие как идея "стимула" и "реакции" в методах `listen` и `act`,
которые являются ключевыми абстракциями для понимания того, как агенты взаимодействуют с окружающей средой и другими агентами.

## Подробнее

Этот модуль содержит класс `TinyPerson`, который представляет собой симуляцию человека в TinyTroupe.
`TinyPerson` может взаимодействовать с другими агентами и окружающей средой, имеет память (эпизодическую и семантическую),
когнитивные способности и может выполнять различные действия. Модуль также содержит класс `TinyMentalFaculty`, который
представляет собой умственную способность агента, такую как память, мышление и т.д.

## Классы

### `TinyPerson`

**Описание**: Симулированный человек во вселенной TinyTroupe.

**Принцип работы**:
Класс `TinyPerson` представляет собой агента, обладающего когнитивными способностями и памятью.
Он может взаимодействовать с другими агентами и окружающей средой, воспринимать стимулы и совершать действия.
Внутреннее состояние агента (эмоции, цели, внимание) обновляется в процессе взаимодействия.

**Атрибуты**:

- `MAX_ACTIONS_BEFORE_DONE` (int): Максимальное количество действий, которое агент может выполнить до завершения.
- `PP_TEXT_WIDTH` (int): Ширина текста для форматированного вывода.
- `serializable_attributes` (list): Список атрибутов, которые можно сериализовать в JSON.
- `all_agents` (dict): Словарь всех созданных агентов (имя -> агент).
- `communication_style` (str): Стиль общения для всех агентов ("simplified" или "full").
- `communication_display` (bool): Определяет, отображать ли коммуникации.

**Методы**:

- `__init__(self, name:str=None, episodic_memory=None, semantic_memory=None, mental_faculties:list=None)`:
    Создает экземпляр класса `TinyPerson`.
- `_post_init(self, **kwargs)`: Выполняет инициализацию после создания экземпляра класса.
- `generate_agent_prompt(self)`: Генерирует prompt для агента.
- `reset_prompt(self)`: Сбрасывает prompt агента.
- `get(self, key)`: Возвращает значение из конфигурации агента по ключу.
- `define(self, key, value, group=None)`: Определяет значение в конфигурации агента.
- `define_several(self, group, records)`: Определяет несколько значений в конфигурации агента в одной группе.
- `define_relationships(self, relationships, replace=True)`: Определяет или обновляет отношения агента с другими агентами.
- `clear_relationships(self)`: Очищает отношения агента.
- `related_to(self, other_agent, description, symmetric_description=None)`: Определяет отношение между агентом и другим агентом.
- `add_mental_faculties(self, mental_faculties)`: Добавляет список когнитивных способностей агенту.
- `add_mental_faculty(self, faculty)`: Добавляет когнитивную способность агенту.
- `act(self, until_done=True, n=None, return_actions=False, max_content_length=default["max_content_display_length"])`:
    Активирует агента в среде и обновляет его внутреннее когнитивное состояние.
- `listen(self, speech, source: AgentOrWorld = None, max_content_length=default["max_content_display_length"])`:
    Заставляет агента слушать другого агента (искусственного или человеческого) и обновляет его внутреннее когнитивное состояние.
- `socialize(self, social_description: str, source: AgentOrWorld = None, max_content_length=default["max_content_display_length"])`:
    Заставляет агента воспринимать социальный стимул и обновляет его внутреннее когнитивное состояние.
- `see(self, visual_description, source: AgentOrWorld = None, max_content_length=default["max_content_display_length"])`:
    Заставляет агента воспринимать визуальный стимул и обновляет его внутреннее когнитивное состояние.
- `think(self, thought, max_content_length=default["max_content_display_length"])`:
    Заставляет агента думать о чем-то и обновляет его внутреннее когнитивное состояние.
- `internalize_goal(self, goal, max_content_length=default["max_content_display_length"])`:
    Заставляет агента усвоить цель и обновляет его внутреннее когнитивное состояние.
- `_observe(self, stimulus, max_content_length=default["max_content_display_length"])`:
    Наблюдает за стимулом и обновляет внутреннее когнитивное состояние агента.
- `listen_and_act(self, speech, return_actions=False, max_content_length=default["max_content_display_length"])`:
    Комбинированный метод `listen` и `act`.
- `see_and_act(self, visual_description, return_actions=False, max_content_length=default["max_content_display_length"])`:
    Комбинированный метод `see` и `act`.
- `think_and_act(self, thought, return_actions=False, max_content_length=default["max_content_display_length"])`:
    Комбинированный метод `think` и `act`.
- `read_documents_from_folder(self, documents_path:str)`:
    Считывает документы из каталога и загружает их в семантическую память.
- `read_documents_from_web(self, web_urls:list)`:
    Считывает документы из веб-URL-адресов и загружает их в семантическую память.
- `move_to(self, location, context=[])`:
    Перемещает агента в новое местоположение и обновляет его внутреннее когнитивное состояние.
- `change_context(self, context: list)`:
    Изменяет контекст и обновляет внутреннее когнитивное состояние агента.
- `make_agent_accessible(self, agent: Self, relation_description: str = "An agent I can currently interact with.")`:
    Делает агента доступным для взаимодействия.
- `make_agent_inaccessible(self, agent: Self)`:
    Делает агента недоступным для взаимодействия.
- `make_all_agents_inaccessible(self)`:
    Делает всех агентов недоступными для взаимодействия.
- `_produce_message(self)`: Генерирует сообщение от агента.
- `_update_cognitive_state(self, goals=None, context=None, attention=None, emotions=None)`:
    Обновляет когнитивное состояние агента.
- `_display_communication(self, role, content, kind, simplified=True, max_content_length=default["max_content_display_length"])`:
    Отображает текущую коммуникацию и сохраняет ее в буфере для последующего использования.
- `_push_and_display_latest_communication(self, rendering)`:
    Помещает последние сообщения в буфер агента.
- `pop_and_display_latest_communications(self)`:
    Удаляет последние сообщения и отображает их.
- `clear_communications_buffer(self)`: Очищает буфер сообщений.
- `pop_latest_actions(self) -> list`:
    Возвращает последние действия, выполненные этим агентом.
- `pop_actions_and_get_contents_for(self, action_type: str, only_last_action: bool = True) -> list`:
    Возвращает содержимое действий заданного типа, выполненных этим агентом.
- `minibio(self)`: Возвращает мини-биографию агента.
- `pp_current_interactions(self, simplified=True, skip_system=True, max_content_length=default["max_content_display_length"])`:
    Выводит текущие взаимодействия.
- `pretty_current_interactions(self, simplified=True, skip_system=True, max_content_length=default["max_content_display_length"], first_n=None, last_n=None, include_omission_info:bool=True)`:
    Возвращает строку с текущими сообщениями.
- `_pretty_stimuli(self, role, content, simplified=True, max_content_length=default["max_content_display_length"]) -> list`:
    Форматирует стимулы.
- `_pretty_action(self, role, content, simplified=True, max_content_length=default["max_content_display_length"]) -> str`:
    Форматирует действие.
- `_pretty_timestamp(self, role, timestamp) -> str`: Форматирует временную метку.
- `iso_datetime(self) -> str`:
    Возвращает текущую дату и время среды, если таковые имеются.
- `save_spec(self, path, include_mental_faculties=True, include_memory=False)`:
    Сохраняет текущую конфигурацию в JSON-файл.
- `load_spec(path, suppress_mental_faculties=False, suppress_memory=False, auto_rename_agent=False, new_agent_name=None)`:
    Загружает спецификацию агента из JSON-файла.
- `encode_complete_state(self) -> dict`:
    Кодирует полное состояние `TinyPerson`, включая текущие сообщения, доступных агентов и т.д.
- `decode_complete_state(self, state: dict) -> Self`:
    Загружает полное состояние `TinyPerson`, включая текущие сообщения, и создает новый экземпляр `TinyPerson`.
- `create_new_agent_from_current_spec(self, new_name:str) -> Self`:
    Создает нового агента из спецификации текущего агента.
- `add_agent(agent)`: Добавляет агента в глобальный список агентов.
- `has_agent(agent_name: str)`: Проверяет, зарегистрирован ли агент.
- `set_simulation_for_free_agents(simulation)`:
    Устанавливает симуляцию, если она `None`.
- `get_agent_by_name(name)`: Возвращает агента по имени.
- `clear_agents()`: Очищает глобальный список агентов.

#### `__init__`

```python
def __init__(self, name:str=None, 
                 episodic_memory=None,
                 semantic_memory=None,
                 mental_faculties:list=None):
    """
    Создает TinyPerson.

    Args:
        name (str): Имя TinyPerson. Либо это, либо spec_path должно быть указано.
        episodic_memory (EpisodicMemory, optional): Реализация памяти для использования. По умолчанию EpisodicMemory().
        semantic_memory (SemanticMemory, optional): Реализация семантической памяти для использования. По умолчанию SemanticMemory().
        mental_faculties (list, optional): Список умственных способностей, которые нужно добавить агенту. По умолчанию None.
    """
    ...
```

**Назначение**: Инициализирует объект `TinyPerson`.

**Параметры**:
- `name` (str, optional): Имя агента. Должно быть указано либо имя, либо путь к файлу спецификации агента. По умолчанию `None`.
- `episodic_memory` (EpisodicMemory, optional): Объект эпизодической памяти для агента. По умолчанию создается новый объект `EpisodicMemory`.
- `semantic_memory` (SemanticMemory, optional): Объект семантической памяти для агента. По умолчанию создается новый объект `SemanticMemory`.
- `mental_faculties` (list, optional): Список объектов умственных способностей для агента. По умолчанию `None`.

**Как работает функция**:

1. Проверяет, переданы ли объекты эпизодической и семантической памяти, и присваивает их соответствующим атрибутам агента. Если объекты не переданы, атрибуты остаются `None`.
2. Проверяет, передан ли список умственных способностей, и присваивает его атрибуту `_mental_faculties` агента. Если список не передан, атрибут остается `None`.
3. Утверждает, что имя агента не `None`.
4. Присваивает имя агента атрибуту `name`.

#### `_post_init`

```python
def _post_init(self, **kwargs):
    """
    Этот метод будет запущен после __init__, так как у класса есть декоратор @post_init.
    Удобно разделять некоторые процессы инициализации, чтобы упростить десериализацию.
    """
    ...
```

**Назначение**: Выполняет постобработку инициализации объекта `TinyPerson` после вызова метода `__init__`.

**Параметры**:
- `kwargs` (dict): Произвольные ключевые аргументы, переданные в метод.

**Внутренние функции**: Отсутствуют.

**Как работает функция**:

1. Инициализирует атрибуты `current_messages`, `environment` и `_actions_buffer` пустыми значениями (список, `None` и список соответственно).
2. Инициализирует атрибут `_accessible_agents` пустым списком.
3. Инициализирует атрибут `_displayed_communications_buffer` пустым списком.
4. Если атрибуты `episodic_memory` или `semantic_memory` не существуют, создает новые экземпляры `EpisodicMemory` и `SemanticMemory` соответственно.
5. Если атрибут `_mental_faculties` не существует, создает пустой список.
6. Создает словарь конфигурации `_configuration` со значениями по умолчанию для различных параметров агента, таких как имя, возраст, национальность, род занятий, интересы, отношения и т.д.
7. Определяет путь к шаблону prompt агента (`_prompt_template_path`) и инициализирует атрибут `_init_system_message` значением `None`.
8. Обрабатывает случаи переименования агента, если переданы параметры `new_agent_name` или `auto_rename`.
9. Регистрирует агента в глобальном списке агентов (`TinyPerson.all_agents`).
10. Сбрасывает prompt агента, вызывая метод `reset_prompt`.
11. Устанавливает идентификатор симуляции агента, если он был создан в рамках симуляции.

#### `generate_agent_prompt`

```python
def generate_agent_prompt(self):
    with open(self._prompt_template_path, "r") as f:
        agent_prompt_template = f.read()

    # let's operate on top of a copy of the configuration, because we'll need to add more variables, etc.
    template_variables = self._configuration.copy()    

    # Prepare additional action definitions and constraints
    actions_definitions_prompt = ""
    actions_constraints_prompt = ""
    for faculty in self._mental_faculties:
        actions_definitions_prompt += f"{faculty.actions_definitions_prompt()}\\n"
        actions_constraints_prompt += f"{faculty.actions_constraints_prompt()}\\n"
    
    # make the additional prompt pieces available to the template
    template_variables['actions_definitions_prompt'] = textwrap.indent(actions_definitions_prompt, "")
    template_variables['actions_constraints_prompt'] = textwrap.indent(actions_constraints_prompt, "")

    # RAI prompt components, if requested
    template_variables = utils.add_rai_template_variables_if_enabled(template_variables)

    return chevron.render(agent_prompt_template, template_variables)
```

**Назначение**: Генерирует prompt для агента на основе шаблона и текущей конфигурации.

**Внутренние функции**: Отсутствуют.

**Как работает функция**:

1. Открывает файл шаблона prompt агента, указанный в атрибуте `_prompt_template_path`, и считывает его содержимое в переменную `agent_prompt_template`.
2. Создает копию словаря конфигурации агента (`_configuration`) в переменную `template_variables`, чтобы не изменять исходную конфигурацию.
3. Подготавливает дополнительные определения и ограничения действий, перебирая когнитивные способности агента (`_mental_faculties`) и вызывая методы `actions_definitions_prompt()` и `actions_constraints_prompt()` для каждой способности.
4. Делает дополнительные фрагменты prompt доступными для шаблона, добавляя их в словарь `template_variables` с помощью отступов.
5. Добавляет компоненты prompt RAI (Responsible AI), если это запрошено, вызывая функцию `utils.add_rai_template_variables_if_enabled()`.
6. Рендерит шаблон prompt агента (`agent_prompt_template`) с использованием библиотеки `chevron` и словаря `template_variables`.
7. Возвращает сгенерированный prompt.

#### `reset_prompt`

```python
def reset_prompt(self):

    # render the template with the current configuration
    self._init_system_message = self.generate_agent_prompt()

    # TODO actually, figure out another way to update agent state without "changing history"

    # reset system message
    self.current_messages = [
        {"role": "system", "content": self._init_system_message}
    ]

    # sets up the actual interaction messages to use for prompting
    self.current_messages += self.episodic_memory.retrieve_recent()
```

**Назначение**: Сбрасывает prompt агента, генерируя новый на основе текущей конфигурации и восстанавливая историю взаимодействий.

**Внутренние функции**: Отсутствуют.

**Как работает функция**:

1. Генерирует новый prompt агента, вызывая метод `generate_agent_prompt()`, и присваивает его атрибуту `_init_system_message`.
2. Сбрасывает текущие сообщения агента (`current_messages`), создавая новый список, содержащий только системное сообщение с новым prompt.
3. Добавляет в текущие сообщения последние сообщения из эпизодической памяти агента, вызывая метод `episodic_memory.retrieve_recent()`.

#### `get`

```python
def get(self, key):
    """
    Возвращает определение ключа в конфигурации TinyPerson.
    """
    return self._configuration.get(key, None)
```

**Назначение**: Возвращает значение ключа из конфигурации TinyPerson.

**Параметры**:
- `key` (Any): Ключ, значение которого необходимо получить из конфигурации.

**Возвращает**:
- Значение ключа из конфигурации, если ключ существует, и `None` в противном случае.

**Как работает функция**:
1. Пытается получить значение ключа из словаря `_configuration` с помощью метода `get()`.
2. Если ключ найден, возвращает его значение.
3. Если ключ не найден, возвращает `None`.

#### `define`

```python
@transactional
def define(self, key, value, group=None):
    """
    Определяет значение в конфигурации TinyPerson.
    Если группа равна None, значение добавляется на верхний уровень конфигурации.
    В противном случае значение добавляется в указанную группу.
    """
    ...
```

**Назначение**: Определяет значение в конфигурации `TinyPerson`.

**Параметры**:
- `key` (Any): Ключ, для которого необходимо определить значение.
- `value` (Any): Значение, которое необходимо определить для ключа.
- `group` (Any, optional): Группа, к которой необходимо добавить значение. По умолчанию `None`.

**Как работает функция**:

1. Удаляет отступы из значения, если оно является строкой.
2. Если группа не указана, добавляет значение непосредственно в словарь `_configuration` по указанному ключу.
3. Если группа указана, добавляет значение в список, связанный с указанной группой в словаре `_configuration`.
4. Сбрасывает prompt агента после добавления значения в конфигурацию, вызывая метод `reset_prompt()`.

#### `define_several`

```python
def define_several(self, group, records):
    """
    Определяет несколько значений в конфигурации TinyPerson, все принадлежащие к одной и той же группе.
    """
    for record in records:
        self.define(key=None, value=record, group=group)
```

**Назначение**: Определяет несколько значений в конфигурации `TinyPerson`, все принадлежащие к одной и той же группе.

**Параметры**:
- `group` (Any): Группа, к которой необходимо добавить значения.
- `records` (list): Список записей, которые необходимо добавить в группу.

**Как работает функция**:

1. Перебирает список записей (`records`).
2. Для каждой записи вызывает метод `self.define(key=None, value=record, group=group)`, чтобы добавить запись в указанную группу. Ключ устанавливается в `None`, так как записи добавляются в список группы.

#### `define_relationships`

```python
@transactional
def define_relationships(self, relationships, replace=True):
    """
    Определяет или обновляет отношения TinyPerson.

    Args:
        relationships (list or dict): Отношения, которые нужно добавить или заменить. Либо список словарей, сопоставляющих имена агентов с описаниями отношений,
          либо один словарь, сопоставляющий одно имя агента с его описанием отношений.
        replace (bool, optional): Следует ли заменять текущие отношения или просто добавлять их. По умолчанию True.
    """
    ...
```

**Назначение**: Определяет или обновляет отношения `TinyPerson` с другими агентами.

**Параметры**:

- `relationships` (list or dict): Отношения для добавления или замены. Это может быть:
  - Список словарей, где каждый словарь сопоставляет имя агента с описанием отношения.
  - Один словарь, сопоставляющий имя агента с описанием отношения.
- `replace` (bool, optional): Определяет, следует ли заменять текущие отношения или добавлять к ним. По умолчанию `True`.

**Как работает функция**:

1. Проверяет, следует ли заменять текущие отношения (`replace == True`) и является ли аргумент `relationships` списком. Если да, то заменяет текущий список отношений в `self._configuration['relationships']` новым списком `relationships`.
2. Если `replace == False`, то получает текущий список отношений из `self._configuration['relationships']`.
3. Если `relationships` является списком, то добавляет каждый элемент из списка в текущий список отношений.
4. Если `relationships` является словарем и содержит 2 элемента ({"Name": ..., "Description": ...}), то добавляет словарь в текущий список отношений.
5. Если аргументы не соответствуют ожидаемым типам и структуре, вызывает исключение `Exception`.

#### `clear_relationships`

```python
@transactional
def clear_relationships(self):
    """
    Очищает отношения TinyPerson.
    """
    self._configuration['relationships'] = []

    return self
```

**Назначение**: Очищает список отношений агента.

**Как работает функция**:

1. Устанавливает значение ключа `'relationships'` в словаре `_configuration` равным пустому списку `[]`.
2. Возвращает ссылку на текущий объект `self` для обеспечения возможности chaining.

#### `related_to`

```python
@transactional
def related_to(self, other_agent, description, symmetric_description=None):
    """
    Определяет отношение между этим агентом и другим агентом.

    Args:
        other_agent (TinyPerson): Другой агент.
        description (str): Описание отношения.
        symmetric (bool): Является ли отношение симметричным или нет. То есть,
          если отношение определено для обоих агентов.
    
    Returns:
        TinyPerson: Сам агент, для облегчения связывания.
    """
    self.define_relationships([{"Name": other_agent.name, "Description": description}], replace=False)
    if symmetric_description is not None:
        other_agent.define_relationships([{"Name": self.name, "Description": symmetric_description}], replace=False)
    
    return self
```

**Назначение**: Определяет отношение между текущим агентом и другим агентом.

**Параметры**:
- `other_agent` (TinyPerson): Другой агент, с которым устанавливается отношение.
- `description` (str): Описание отношения между агентами.
- `symmetric_description` (str, optional): Описание симметричного отношения, которое будет установлено для другого агента по отношению к текущему. По умолчанию `None`.

**Как работает функция**:

1. Вызывает метод `define_relationships` для текущего агента, чтобы добавить отношение с другим агентом. Аргумент `replace` установлен в `False`, чтобы добавить отношение к существующим отношениям.
2. Если `symmetric_description` не `None`, вызывает метод `define_relationships` для другого агента, чтобы добавить симметричное отношение с текущим агентом. Аргумент `replace` также установлен в `False`.
3. Возвращает ссылку на текущий объект `self` для обеспечения возможности chaining.

#### `add_mental_faculties`

```python
def add_mental_faculties(self, mental_faculties):
    """
    Adds a list of mental faculties to the agent.
    """
    for faculty in mental_faculties:
        self.add_mental_faculty(faculty)
    
    return self
```

**Назначение**: Добавляет список когнитивных способностей агенту.

**Параметры**:
- `mental_faculties` (list): Список объектов когнитивных способностей, которые необходимо добавить агенту.

**Возвращает**:
- `self` (TinyPerson): Возвращает ссылку на текущий объект `TinyPerson` для обеспечения возможности chaining.

**Как работает функция**:

1. Перебирает список когнитивных способностей (`mental_faculties`).
2. Для каждой когнитивной способности вызывает метод `add_mental_faculty(faculty)`, чтобы добавить ее агенту.
3. После добавления всех когнитивных способностей возвращает ссылку на текущий объект `TinyPerson`.

#### `add_mental_faculty`

```python
def add_mental_faculty(self, faculty):
    """
    Adds a mental faculty to the agent.
    """
    # check if the faculty is already there or not
    if faculty not in self._mental_faculties:
        self._mental_faculties.append(faculty)
    else:
        raise Exception(f"The mental faculty {faculty} is already present in the agent.")
    
    return self
```

**Назначение**: Добавляет когнитивную способность агенту.

**Параметры**:
- `faculty` (TinyMentalFaculty): Объект когнитивной способности, который необходимо добавить агенту.

**Возвращает**:
- `self` (TinyPerson): Возвращает ссылку на текущий объект `TinyPerson` для обеспечения возможности chaining.

**Как работает функция**:

1. Проверяет, присутствует ли уже когнитивная способность в списке `_mental_faculties` агента.
2. Если когнитивная способность отсутствует, добавляет ее в список `_mental_faculties`.
3. Если когнитивная способность уже присутствует, вызывает исключение `Exception` с сообщением об ошибке.
4. Возвращает ссылку на текущий объект `TinyPerson`.

#### `act`

```python
@transactional
def act(
    self,
    until_done=True,
    n=None,
    return_actions=False,
    max_content_length=default["max_content_display_length"],
):
    """
    Действует в среде и обновляет свое внутреннее когнитивное состояние.
    Либо действует до тех пор, пока агент не будет готов и не потребуются дополнительные стимулы, либо действует фиксированное количество раз,
    но не оба варианта.

    Args:
        until_done (bool): Продолжать ли действовать до тех пор, пока агент не будет готов и не потребуются дополнительные стимулы.
        n (int): Количество действий для выполнения. По умолчанию None.
        return_actions (bool): Возвращать ли действия. По умолчанию False.
    """
    ...
```

**Назначение**: Активирует агента в среде и обновляет его внутреннее когнитивное состояние.

**Параметры**:

- `until_done` (bool, optional): Продолжать ли действовать до тех пор, пока агент не завершит выполнение и не потребуются дополнительные стимулы. По умолчанию `True`.
- `n` (int, optional): Количество действий, которые необходимо выполнить. По умолчанию `None`.
- `return_actions` (bool, optional): Возвращать ли список выполненных действий. По умолчанию `False`.
- `max_content_length` (int, optional): Максимальная длина контента для отображения. По умолчанию значение берется из конфигурации (`default["max_content_display_length"]`).

**Внутренние функции**:

- `aux_act_once()`: Выполняет одно действие агента.

**Как работает функция**:

1. Проверяет, чтобы не были одновременно установлены флаги `until_done` и `n`. Должен быть выбран только один режим работы: либо действовать до завершения, либо выполнить фиксированное количество действий.
2. Если указано количество действий `n`, проверяет, чтобы оно не превышало `TinyPerson.MAX_ACTIONS_BEFORE_DONE` (максимальное количество действий до завершения).
3. В зависимости от выбранного режима работы (`until_done` или `n`) выполняет следующие действия:
   - Если `n` указано:
     - Выполняет цикл `n` раз, вызывая функцию `aux_act_once()` для выполнения одного действия на каждой итерации.
   - Если `until_done` установлено в `True`:
     - Выполняет цикл `while`, пока не будет достигнуто условие завершения. Условием завершения является либо выполнение действия с типом "DONE", либо превышение максимального количества действий (`TinyPerson.MAX_ACTIONS_BEFORE_DONE`), либо обнаружение повторяющихся действий (зацикливание).
     - Внутри цикла вызывается функция `aux_act_once()` для выполнения одного действия.
4. Если `return_actions` установлено в `True`, возвращает список выполненных действий (`contents`).

##### `aux_act_once`

```python
def aux_act_once():
    # A quick thought before the action. This seems to help with better model responses, perhaps because
    # it interleaves user with assistant messages.
    self.think("I will now act a bit, and then issue DONE.")

  
    role, content = self._produce_message()

    self.episodic_memory.store({'role': role, 'content': content, 'simulation_timestamp': self.iso_datetime()})

    cognitive_state = content["cognitive_state"]


    action = content['action']

    self._actions_buffer.append(action)
    self._update_cognitive_state(goals=cognitive_state['goals'],
                                attention=cognitive_state['attention'],
                                emotions=cognitive_state['emotions'])
    
    contents.append(content)          
    if TinyPerson.communication_display:
        self._display_communication(role=role, content=content, kind='action', simplified=True, max_content_length=max_content_length)
    
    #
    # Some actions induce an immediate stimulus or other side-effects. We need to process them here, by means of the mental faculties.
    #
    for faculty in self._mental_faculties:
        faculty.process_action(self, action)             
```

**Назначение**: Выполняет одно действие агента.

**Как работает функция**:

1. Агент генерирует мысль перед действием, чтобы улучшить ответы модели.
2. Генерирует сообщение с помощью `_produce_message()`, которое определяет роль и содержание сообщения.
3. Сохраняет сообщение в эпизодической памяти.
4. Извлекает когнитивное состояние из содержимого сообщения.
5. Извлекает действие из содержимого сообщения.
6. Добавляет действие в буфер действий.
7. Обновляет когнитивное состояние агента на основе целей, внимания и эмоций, полученных из когнитивного состояния.
8. Добавляет содержимое в список `contents`.
9. Если включено отображение коммуникаций, отображает коммуникацию с помощью `_display_communication()`.
10. Перебирает список умственных способностей агента и вызывает метод `process_action()` для каждой способности, чтобы обработать действие и вызвать побочные эффекты.

#### `listen`

```python
@transactional
def listen(
    self,
    speech,
    source: AgentOrWorld = None,
    max_content_length=default["max_content_display_length"],
):
    """
    Слушает другого агента (искусственного или человеческого) и обновляет свое внутреннее когнитивное состояние.

    Args:
        speech (str): Речь, которую нужно прослушать.
        source (AgentOrWorld, optional): Источник речи. По умолчанию None.
    """

    return self._observe(
        stimulus={
            "type": "CONVERSATION",
            "content": speech,
            "source": name_or_empty(source),
        },
        max_content_length=max_content_length,
    )
```

**Назначение**: Моделирует процесс прослушивания агентом речи другого агента или источника. Обновляет внутреннее когнитивное состояние агента на основе полученной информации.

**Параметры**:
- `speech` (str): Речь, которую прослушивает агент.
- `source` (AgentOrWorld, optional): Источник речи. Может быть другим агентом