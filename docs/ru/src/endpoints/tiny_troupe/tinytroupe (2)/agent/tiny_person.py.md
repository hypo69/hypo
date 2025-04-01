# Модуль `tiny_person.py`

## Обзор

Модуль `tiny_person.py` содержит класс `TinyPerson`, представляющий собой симуляцию личности в виртуальной среде TinyTroupe. Он включает в себя управление памятью, определение ментальных способностей, обработку стимулов и действий, а также механизмы взаимодействия с другими агентами и средой.

## Подробней

Данный код является основой для создания и управления виртуальными персонажами в симуляции. Он позволяет определять личностные характеристики, ментальное состояние и поведение агентов, а также обеспечивает механизмы для взаимодействия между ними и с окружающей средой. Класс `TinyPerson` управляет памятью (эпизодической и семантической), обрабатывает входящие стимулы и генерирует действия, основываясь на заданных ментальных способностях и текущем состоянии.

## Классы

### `TinyPerson`

**Описание**: Класс `TinyPerson` представляет собой симулированную личность в виртуальной среде TinyTroupe.

**Наследует**:
- `JsonSerializableRegistry`: Обеспечивает механизмы для сериализации и десериализации объектов класса в формат JSON.

**Атрибуты**:
- `MAX_ACTIONS_BEFORE_DONE` (int): Максимальное количество действий, которое агент может выполнить до того, как будет считаться завершенным. Предотвращает бесконечное выполнение действий.
- `PP_TEXT_WIDTH` (int): Ширина текста для форматированного вывода.
- `serializable_attributes` (list): Список атрибутов, которые будут сериализованы в JSON.
- `serializable_attributes_renaming` (dict): Словарь для переименования атрибутов при сериализации.
- `all_agents` (dict): Словарь, содержащий всех созданных агентов (`name -> agent`).
- `communication_style` (str): Стиль коммуникации для всех агентов ("simplified" или "full").
- `communication_display` (bool): Определяет, отображать ли коммуникацию. `True` для интерактивных приложений.
- `name` (str): Имя агента.
- `episodic_memory` (EpisodicMemory): Эпизодическая память агента.
- `semantic_memory` (SemanticMemory): Семантическая память агента.
- `_persona` (dict): Словарь, содержащий личностные характеристики агента.
- `_mental_state` (dict): Словарь, содержащий ментальное состояние агента.
- `_mental_faculties` (list): Список ментальных способностей агента.
- `current_messages` (list): Список текущих сообщений агента.
- `environment` (Any): Текущее окружение, в котором действует агент.
- `_actions_buffer` (list): Список действий, выполненных агентом, но еще не обработанных окружением.
- `_accessible_agents` (list): Список агентов, с которыми данный агент может взаимодействовать.
- `_displayed_communications_buffer` (list): Буфер отображаемых коммуникаций.
- `_extended_agent_summary` (str): Расширенное описание агента, генерируемое при необходимости.
- `_prompt_template_path` (str): Путь к шаблону системного промпта агента.
- `_init_system_message` (str): Инициализированное системное сообщение.

**Методы**:

- `__init__(self, name: str = None, episodic_memory = None, semantic_memory = None, mental_faculties: list = None)`
    ```python
    def __init__(self, name:str=None, 
                 episodic_memory=None,
                 semantic_memory=None,
                 mental_faculties:list=None):
        """
        Creates a TinyPerson.

        Args:
            name (str): The name of the TinyPerson. Either this or spec_path must be specified.
            episodic_memory (EpisodicMemory, optional): The memory implementation to use. Defaults to EpisodicMemory().
            semantic_memory (SemanticMemory, optional): The memory implementation to use. Defaults to SemanticMemory().
            mental_faculties (list, optional): A list of mental faculties to add to the agent. Defaults to None.
        """
    ```

    **Назначение**: Создает экземпляр класса `TinyPerson`.

    **Параметры**:
    - `name` (str, optional): Имя персонажа TinyPerson. Либо это, либо `spec_path` должны быть указаны.
    - `episodic_memory` (EpisodicMemory, optional): Реализация памяти для использования. По умолчанию `EpisodicMemory()`.
    - `semantic_memory` (SemanticMemory, optional): Реализация памяти для использования. По умолчанию `SemanticMemory()`.
    - `mental_faculties` (list, optional): Список ментальных способностей, добавляемых агенту. По умолчанию `None`.

    **Как работает функция**:
    1. Проверяет, переданы ли объекты эпизодической и семантической памяти, и присваивает их соответствующим атрибутам агента.
    2. Проверяет, передан ли список ментальных способностей, и присваивает его атрибуту `_mental_faculties` агента.
    3. Утверждает, что имя агента было передано.
    4. Назначает переданное имя атрибуту `name` агента.

    **Примеры**:

    ```python
    agent = TinyPerson(name="Alice", episodic_memory=EpisodicMemory(), mental_faculties=[])
    ```
    ```python
    agent = TinyPerson(name="Bob")
    ```

- `_post_init(self, **kwargs)`
    ```python
    def _post_init(self, **kwargs):
        """
        This will run after __init__, since the class has the @post_init decorator.
        It is convenient to separate some of the initialization processes to make deserialize easier.
        """
    ```

    **Назначение**: Инициализирует дополнительные атрибуты после создания экземпляра класса `TinyPerson`.

    **Параметры**:
    - `kwargs` (dict): Дополнительные параметры, переданные при создании экземпляра.

    **Как работает функция**:
    1. Инициализирует список `current_messages` для хранения текущих сообщений агента.
    2. Устанавливает атрибут `environment` в `None`, представляющий текущее окружение агента.
    3. Создает пустой список `_actions_buffer` для хранения действий агента.
    4. Создает пустой список `_accessible_agents` для хранения агентов, доступных для взаимодействия.
    5. Создает пустой список `_displayed_communications_buffer` для хранения отображаемых коммуникаций.
    6. Если атрибуты `episodic_memory` и `semantic_memory` не существуют, создает экземпляры `EpisodicMemory` и `SemanticMemory` соответственно.
    7. Если атрибут `_mental_faculties` не существует, создает пустой список для хранения ментальных способностей агента.
    8. Создает словарь `_persona`, содержащий личностные характеристики агента, такие как имя, возраст, национальность и т.д.
    9. Если атрибут `name` не существует, инициализирует его значением из словаря `_persona`.
    10. Создает словарь `_mental_state`, содержащий ментальное состояние агента, такое как текущая дата и время, местоположение, контекст и т.д.
    11. Если атрибут `_extended_agent_summary` не существует, устанавливает его в `None`.
    12. Определяет путь к шаблону промпта агента.
    13. Инициализирует атрибут `_init_system_message` значением `None`.
    14. Переименовывает агента, если передан параметр `new_agent_name`.
    15. Автоматически переименовывает агента, если передан параметр `auto_rename`.
    16. Регистрирует агента в глобальном списке агентов.
    17. Сбрасывает промпт агента.
    18. Добавляет агента в текущую симуляцию, если она существует.

    **Примеры**:

    ```python
    agent = TinyPerson(name="Alice")
    agent._post_init()
    ```

- `_rename(self, new_name: str)`
    ```python
    def _rename(self, new_name:str):    
        self.name = new_name
        self._persona["name"] = self.name
    ```

    **Назначение**: Переименовывает агента.

    **Параметры**:
    - `new_name` (str): Новое имя агента.

    **Как работает функция**:
    1. Устанавливает атрибут `name` агента в новое имя.
    2. Обновляет имя агента в словаре `_persona`.

    **Примеры**:

    ```python
    agent = TinyPerson(name="Alice")
    agent._rename("Bob")
    print(agent.name)  # Вывод: Bob
    print(agent._persona["name"])  # Вывод: Bob
    ```

- `generate_agent_system_prompt(self)`
    ```python
    def generate_agent_system_prompt(self):
        with open(self._prompt_template_path, "r") as f:
            agent_prompt_template = f.read()

        # let\'s operate on top of a copy of the configuration, because we\'ll need to add more variables, etc.
        template_variables = self._persona.copy()    
        template_variables["persona"] = json.dumps(self._persona.copy(), indent=4)    

        # Prepare additional action definitions and constraints
        actions_definitions_prompt = ""
        actions_constraints_prompt = ""
        for faculty in self._mental_faculties:
            actions_definitions_prompt += f"{faculty.actions_definitions_prompt()}\\n"
            actions_constraints_prompt += f"{faculty.actions_constraints_prompt()}\\n"

        # Make the additional prompt pieces available to the template. 
        # Identation here is to align with the text structure in the template.
        template_variables[\'actions_definitions_prompt\'] = textwrap.indent(actions_definitions_prompt.strip(), "  ")
        template_variables[\'actions_constraints_prompt\'] = textwrap.indent(actions_constraints_prompt.strip(), "  ")

        # RAI prompt components, if requested
        template_variables = utils.add_rai_template_variables_if_enabled(template_variables)

        return chevron.render(agent_prompt_template, template_variables)
    ```

    **Назначение**: Генерирует системный промпт для агента на основе шаблона и конфигурации.

    **Как работает функция**:
    1. Открывает файл шаблона промпта агента.
    2. Копирует словарь `_persona` для работы с переменными шаблона.
    3. Преобразует копию `_persona` в JSON-строку и присваивает её переменной `persona` в `template_variables`.
    4. Подготавливает дополнительные определения действий и ограничения, итерируясь по `_mental_faculties`.
    5. Добавляет подготовленные фрагменты в переменные шаблона.
    6. Добавляет компоненты RAI, если они включены.
    7. Рендерит шаблон с использованием библиотеки `chevron` и возвращает результат.

    **Примеры**:

    ```python
    agent = TinyPerson(name="Alice")
    prompt = agent.generate_agent_system_prompt()
    print(prompt)
    ```

- `reset_prompt(self)`
    ```python
    def reset_prompt(self):

        # render the template with the current configuration
        self._init_system_message = self.generate_agent_system_prompt()

        # TODO actually, figure out another way to update agent state without "changing history"

        # reset system message
        self.current_messages = [
            {"role": "system", "content": self._init_system_message}
        ]

        # sets up the actual interaction messages to use for prompting
        self.current_messages += self.retrieve_recent_memories()

        # add a final user message, which is neither stimuli or action, to instigate the agent to act properly
        self.current_messages.append({"role": "user", 
                                      "content": "Now you **must** generate a sequence of actions following your interaction directives, " +\\
                                                 "and complying with **all** instructions and contraints related to the action you use." +\\
                                                 "DO NOT repeat the exact same action more than once in a row!" +\\
                                                 "DO NOT keep saying or doing very similar things, but instead try to adapt and make the interactions look natural." +\\
                                                 "These actions **MUST** be rendered following the JSON specification perfectly, including all required keys (even if their value is empty), **ALWAYS**."
                                     })
    ```

    **Назначение**: Сбрасывает и обновляет промпт агента, используя текущую конфигурацию и последние воспоминания.

    **Как работает функция**:
    1. Генерирует системное сообщение агента с использованием `generate_agent_system_prompt()`.
    2. Сбрасывает список `current_messages`, добавляя системное сообщение в качестве первого элемента.
    3. Извлекает последние воспоминания агента и добавляет их в `current_messages`.
    4. Добавляет финальное сообщение пользователя, которое стимулирует агента к действию в соответствии с директивами и ограничениями.

    **Примеры**:

    ```python
    agent = TinyPerson(name="Alice")
    agent.reset_prompt()
    print(agent.current_messages)
    ```

- `get(self, key)`
    ```python
    def get(self, key):
        """
        Returns the definition of a key in the TinyPerson\'s configuration.
        """
        return self._persona.get(key, None)
    ```

    **Назначение**: Возвращает значение ключа из конфигурации `TinyPerson`.

    **Параметры**:
    - `key` (str): Ключ для поиска в конфигурации.

    **Возвращает**:
    - Значение ключа, если он существует, иначе `None`.

    **Как работает функция**:
    1. Использует метод `get` словаря `_persona` для получения значения по ключу.
    2. Возвращает полученное значение или `None`, если ключ не найден.

    **Примеры**:

    ```python
    agent = TinyPerson(name="Alice")
    age = agent.get("age")
    print(age)  # Вывод: None (если возраст не определен)
    ```

- `import_fragment(self, path)`
    ```python
    @transactional
    def import_fragment(self, path):
        """
        Imports a fragment of a persona configuration from a JSON file.
        """
        with open(path, "r") as f:
            fragment = json.load(f)

        # check the type is "Fragment" and that there\'s also a "persona" key
        if fragment.get("type", None) == "Fragment" and fragment.get("persona", None) is not None:
            self.include_persona_definitions(fragment["persona"])\n        else:\n            raise ValueError("The imported JSON file must be a valid fragment of a persona configuration.")
        \n        # must reset prompt after adding to configuration
        self.reset_prompt()
    ```

    **Назначение**: Импортирует фрагмент конфигурации персонажа из JSON-файла.

    **Параметры**:
    - `path` (str): Путь к JSON-файлу с фрагментом конфигурации.

    **Как работает функция**:
    1. Открывает JSON-файл по указанному пути и загружает его содержимое.
    2. Проверяет, является ли фрагмент валидным, проверяя наличие ключей "type" и "persona".
    3. Если фрагмент валиден, вызывает метод `include_persona_definitions` для включения определения персонажа.
    4. Сбрасывает промпт агента после добавления конфигурации.

    **Примеры**:

    ```python
    agent = TinyPerson(name="Alice")
    agent.import_fragment("path/to/fragment.json")
    ```

- `include_persona_definitions(self, additional_definitions: dict)`
    ```python
    @transactional
    def include_persona_definitions(self, additional_definitions: dict):
        """
        Imports a set of definitions into the TinyPerson. They will be merged with the current configuration.
        It is also a convenient way to include multiple bundled definitions into the agent.

        Args:
            additional_definitions (dict): The additional definitions to import.
        """

        self._persona = utils.merge_dicts(self._persona, additional_definitions)

        # must reset prompt after adding to configuration
        self.reset_prompt()
    ```

    **Назначение**: Импортирует набор определений в `TinyPerson`.

    **Параметры**:
    - `additional_definitions` (dict): Дополнительные определения для импорта.

    **Как работает функция**:
    1. Объединяет переданные определения с текущей конфигурацией персонажа.
    2. Сбрасывает промпт агента после добавления конфигурации.

    **Примеры**:

    ```python
    agent = TinyPerson(name="Alice")
    additional_definitions = {"age": 30, "occupation": "Software Engineer"}
    agent.include_persona_definitions(additional_definitions)
    ```

- `define(self, key, value, merge=True, overwrite_scalars=True)`
    ```python
    @transactional
    def define(self, key, value, merge=True, overwrite_scalars=True):
        """
        Define a value to the TinyPerson\'s persona configuration. Value can either be a scalar or a dictionary.\n        If the value is a dictionary or list, you can choose to merge it with the existing value or replace it. 
        If the value is a scalar, you can choose to overwrite the existing value or not.

        Args:
            key (str): The key to define.
            value (Any): The value to define.
            merge (bool, optional): Whether to merge the dict/list values with the existing values or replace them. Defaults to True.
            overwrite_scalars (bool, optional): Whether to overwrite scalar values or not. Defaults to True.
        """

        # dedent value if it is a string
        if isinstance(value, str):\n            value = textwrap.dedent(value)

        # if the value is a dictionary, we can choose to merge it with the existing value or replace it
        if isinstance(value, dict) or isinstance(value, list):\n            if merge:\n                self._persona = utils.merge_dicts(self._persona, {key: value})\n            else:\n                self._persona[key] = value

        # if the value is a scalar, we can choose to overwrite it or not
        elif overwrite_scalars or (key not in self._persona):\n            self._persona[key] = value
        \n        else:\n            raise ValueError(f"The key \'{key}\' already exists in the persona configuration and overwrite_scalars is set to False.")
        \n        # must reset prompt after adding to configuration
        self.reset_prompt()
    ```

    **Назначение**: Определяет значение для ключа в конфигурации персонажа `TinyPerson`.

    **Параметры**:
    - `key` (str): Ключ для определения.
    - `value` (Any): Значение для определения.
    - `merge` (bool, optional): Определяет, следует ли объединять значения словаря/списка с существующими значениями или заменить их. По умолчанию `True`.
    - `overwrite_scalars` (bool, optional): Определяет, следует ли перезаписывать скалярные значения или нет. По умолчанию `True`.

    **Как работает функция**:
    1. Удаляет отступы в начале и конце строки, если значение является строкой.
    2. Если значение является словарем или списком, объединяет его с существующим значением или заменяет его в зависимости от параметра `merge`.
    3. Если значение является скалярным, перезаписывает его или нет в зависимости от параметра `overwrite_scalars`.
    4. Сбрасывает промпт агента после добавления конфигурации.

    **Примеры**:

    ```python
    agent = TinyPerson(name="Alice")
    agent.define("age", 30)
    agent.define("occupation", "Software Engineer", overwrite_scalars=False)
    agent.define("interests", ["reading", "coding"], merge=False)
    ```

- `define_relationships(self, relationships, replace=True)`
    ```python
    @transactional
    def define_relationships(self, relationships, replace=True):
        """
        Defines or updates the TinyPerson\'s relationships.

        Args:
            relationships (list or dict): The relationships to add or replace. Either a list of dicts mapping agent names to relationship descriptions,
              or a single dict mapping one agent name to its relationship description.
            replace (bool, optional): Whether to replace the current relationships or just add to them. Defaults to True.
        """

        if (replace == True) and (isinstance(relationships, list)):\n            self._persona[\'relationships\'] = relationships

        elif replace == False:\n            current_relationships = self._persona[\'relationships\']\n            if isinstance(relationships, list):\n                for r in relationships:\n                    current_relationships.append(r)
                \n            elif isinstance(relationships, dict) and len(relationships) == 2: #{"Name": ..., "Description": ...}\n                current_relationships.append(relationships)

            else:\n                raise Exception("Only one key-value pair is allowed in the relationships dict.")

        else:\n            raise Exception("Invalid arguments for define_relationships.")
    ```

    **Назначение**: Определяет или обновляет отношения `TinyPerson`.

    **Параметры**:
    - `relationships` (list или dict): Отношения для добавления или замены. Может быть списком словарей, сопоставляющих имена агентов с описаниями отношений, или одним словарем, сопоставляющим имя агента с описанием его отношений.
    - `replace` (bool, optional): Определяет, следует ли заменять текущие отношения или просто добавлять к ним. По умолчанию `True`.

    **Как работает функция**:
    1. Если `replace` равно `True` и `relationships` является списком, заменяет текущие отношения новыми отношениями.
    2. Если `replace` равно `False`, добавляет новые отношения к текущим отношениям.
    3. Если `relationships` является списком, добавляет каждое отношение из списка.
    4. Если `relationships` является словарем, добавляет его, если в словаре только два элемента.

    **Примеры**:

    ```python
    agent = TinyPerson(name="Alice")
    relationships = [{"Name": "Bob", "Description": "Friend"}]
    agent.define_relationships(relationships)
    ```

- `clear_relationships(self)`
    ```python
    @transactional
    def clear_relationships(self):
        """
        Clears the TinyPerson\'s relationships.
        """
        self._persona[\'relationships\'] = []  
        return self
    ```

    **Назначение**: Очищает отношения `TinyPerson`.

    **Как работает функция**:
    1. Устанавливает список отношений в пустой список.
    2. Возвращает самого агента для облегчения цепочки методов.

    **Примеры**:

    ```python
    agent = TinyPerson(name="Alice")
    agent.clear_relationships()
    ```

- `related_to(self, other_agent, description, symmetric_description=None)`
    ```python
    @transactional
    def related_to(self, other_agent, description, symmetric_description=None):
        """
        Defines a relationship between this agent and another agent.

        Args:
            other_agent (TinyPerson): The other agent.
            description (str): The description of the relationship.
            symmetric (bool): Whether the relationship is symmetric or not. That is, 
              if the relationship is defined for both agents.
        
        Returns:
            TinyPerson: The agent itself, to facilitate chaining.
        """
        self.define_relationships([{"Name": other_agent.name, "Description": description}], replace=False)
        if symmetric_description is not None:
            other_agent.define_relationships([{"Name": self.name, "Description": symmetric_description}], replace=False)
        
        return self
    ```

    **Назначение**: Определяет отношение между этим агентом и другим агентом.

    **Параметры**:
    - `other_agent` (TinyPerson): Другой агент.
    - `description` (str): Описание отношения.
    - `symmetric_description` (str, optional): Симметричное описание отношения.

    **Как работает функция**:
    1. Определяет отношение между этим агентом и другим агентом.
    2. Если предоставлено симметричное описание, определяет отношение и для другого агента.
    3. Возвращает самого агента для облегчения цепочки методов.

    **Примеры**:

    ```python
    agent1 = TinyPerson(name="Alice")
    agent2 = TinyPerson(name="Bob")
    agent1.related_to(agent2, "Friend", "Friend")
    ```

- `add_mental_faculties(self, mental_faculties)`
    ```python
    def add_mental_faculties(self, mental_faculties):
        """
        Adds a list of mental faculties to the agent.
        """
        for faculty in mental_faculties:
            self.add_mental_faculty(faculty)
        \n        return self
    ```

    **Назначение**: Добавляет список ментальных способностей агенту.

    **Параметры**:
    - `mental_faculties` (list): Список ментальных способностей для добавления.

    **Как работает функция**:
    1. Перебирает список ментальных способностей.
    2. Для каждой способности вызывает метод `add_mental_faculty`.
    3. Возвращает самого агента для облегчения цепочки методов.

    **Примеры**:

    ```python
    agent = TinyPerson(name="Alice")
    mental_faculties = [CognitiveActionModel()]
    agent.add_mental_faculties(mental_faculties)
    ```

- `add_mental_faculty(self, faculty)`
    ```python
    def add_mental_faculty(self, faculty):
        """
        Adds a mental faculty to the agent.
        """
        # check if the faculty is already there or not
        if faculty not in self._mental_faculties:\n            self._mental_faculties.append(faculty)
        else:\n            raise Exception(f"The mental faculty {faculty} is already present in the agent.")
        \n        return self
    ```

    **Назначение**: Добавляет ментальную способность агенту.

    **Параметры**:
    - `faculty` (Any): Ментальная способность для добавления.

    **Как работает функция**:
    1. Проверяет, присутствует ли уже ментальная способность.
    2. Если нет, добавляет ее в список `_mental_faculties`.
    3. Если да, вызывает исключение.
    4. Возвращает самого агента для облегчения цепочки методов.

    **Примеры**:

    ```python
    agent = TinyPerson(name="Alice")
    faculty = CognitiveActionModel()
    agent.add_mental_faculty(faculty)
    ```

- `act(self, until_done=True, n=None, return_actions=False, max_content_length=default["max_content_display_length"])`
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
        Acts in the environment and updates its internal cognitive state.\n        Either acts until the agent is done and needs additional stimuli, or acts a fixed number of times,
        but not both.

        Args:
            until_done (bool): Whether to keep acting until the agent is done and needs additional stimuli.
            n (int): The number of actions to perform. Defaults to None.
            return_actions (bool): Whether to return the actions or not. Defaults to False.
        """

        # either act until done or act a fixed number of times, but not both
        assert not (until_done and n is not None)
        if n is not None:\n            assert n < TinyPerson.MAX_ACTIONS_BEFORE_DONE

        contents = []

        # A separate function to run before each action, which is not meant to be repeated in case of errors.
        def aux_pre_act():
            # TODO maybe we don\'t need this at all anymore?
            #\n            # A quick thought before the action. This seems to help with better model responses, perhaps because
            # it interleaves user with assistant messages.
            pass # self.think("I will now think, reflect and act a bit, and then issue DONE.")        

        # Aux function to perform exactly one action.
        # Occasionally, the model will return JSON missing important keys, so we just ask it to try again
        # Sometimes `content` contains EpisodicMemory\'s MEMORY_BLOCK_OMISSION_INFO message, which raises a TypeError on line 443
        @repeat_on_error(retries=5, exceptions=[KeyError, TypeError])
        def aux_act_once():
            role, content = self._produce_message()

            cognitive_state = content["cognitive_state"]


            action = content[\'action\']
            logger.debug(f"{self.name}\'s action: {action}")

            goals = cognitive_state[\'goals\']
            attention = cognitive_state[\'attention\']
            emotions = cognitive_state[\'emotions\']

            self.store_in_memory({\'role\': role, \'content\': content, 
                                  \'type\': \'action\', 
                                  \'simulation_timestamp\': self.iso_datetime()})

            self._actions_buffer.append(action)
            self._update_cognitive_state(goals=cognitive_state[\'goals\'],\n                                        attention=cognitive_state[\'attention\'],\n                                        emotions=cognitive_state[\'emotions\'])\n            \n            contents.append(content)          \n            if TinyPerson.communication_display:\n                self._display_communication(role=role, content=content, kind=\'action\', simplified=True, max_content_length=max_content_length)
            \n            #\n            # Some actions induce an immediate stimulus or other side-effects. We need to process them here, by means of the mental faculties.\n            #\n            for faculty in self._mental_faculties:\n                faculty.process_action(self, action)             
            

        #\n        # How to proceed with a sequence of actions.\n        #\n        ##### Option 1: run N actions ######
        if n is not None:\n            for i in range(n):\n                aux_pre_act()\n                aux_act_once()

        ##### Option 2: run until DONE ######
        elif until_done:\n            while (len(contents) == 0) or (\n                not contents[-1]["action"]["type"] == "DONE"\n            ):\n                # check if the agent is acting without ever stopping
                if len(contents) > TinyPerson.MAX_ACTIONS_BEFORE_DONE:\n                    logger.warning(f"[{self.name}] Agent {self.name} is acting without ever stopping. This may be a bug. Let\'s stop it here anyway.")
                    break
                if len(contents) > 4: # just some minimum number of actions to check for repetition, could be anything >= 3\n                    # if the last three actions were the same, then we are probably in a loop
                    if contents[-1][\'action\'] == contents[-2][\'action\'] == contents[-3][\'action\']:\n                        logger.warning(f"[{self.name}] Agent {self.name} is acting in a loop. This may be a bug. Let\'s stop it here anyway.")
                        break
                aux_pre_act()\n                aux_act_once()

        if return_actions:\n            return contents
    ```

    **Назначение**: Действует в окружающей среде и обновляет свое внутреннее когнитивное состояние.

    **Параметры**:
    - `until_done` (bool): Следует ли продолжать действовать до тех пор, пока агент не будет завершен и не потребуются дополнительные стимулы.
    - `n` (int, optional): Количество выполняемых действий. По умолчанию `None`.
    - `return_actions` (bool): Следует ли возвращать действия или нет. По умолчанию `False`.

    **Как работает функция**:
    1.  Функция `act` позволяет агенту действовать в окружающей среде. Агент может действовать либо до тех пор, пока не будет достигнуто состояние "DONE", либо фиксированное количество раз.
    2.  Функция содержит две вспомогательные функции: `aux_pre_act` и `aux_act_once`. Функция `aux_pre_act` выполняет предварительные действия перед каждым действием агента. Функция `aux_act_once` выполняет одно действие агента.
    3.  В функции `aux_act_once` агент генерирует сообщение, извлекает из него когнитивное состояние и действие, сохраняет сообщение в памяти, добавляет действие в буфер действий, обновляет когнитивное состояние и отображает коммуникацию.
    4.  Функция `act` содержит два варианта выполнения действий: выполнение `N` действий и выполнение до состояния "DONE". В первом варианте функция выполняет цикл `N` раз, вызывая функции `aux_pre_act` и `aux_act_once` на каждой итерации. Во втором варианте функция выполняет цикл до тех пор, пока не будет достигнуто состояние "DONE".
    5.  Внутри цикла проверяется, не действует ли агент бесконечно, и если это происходит, цикл прерывается. Также проверяется, не повторяет ли агент одни и те же действия несколько раз подряд, и если это происходит, цикл также прерывается.

    **Внутренние функции**:
      - `aux_pre_act()`:
          ```python
           def aux_pre_act():
                """
                A quick thought before the action. This seems to help with better model responses, perhaps because
                it interleaves user with assistant messages.
                """
                pass # self.think("I will now think, reflect and act a bit, and then issue DONE.")
          ```
           **Назначение**: Выполняет предварительные действия перед каждым действием агента. В текущей реализации ничего не делает.

      - `