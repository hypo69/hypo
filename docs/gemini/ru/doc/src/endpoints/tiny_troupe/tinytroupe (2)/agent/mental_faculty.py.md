# Модуль для работы с ментальными способностями агента
===================================================

Модуль содержит классы для представления и управления ментальными способностями агента, такими как память, доступ к файлам и веб-страницам, а также использование инструментов.

## Обзор

В этом модуле определены классы, представляющие ментальные способности агента. Ментальные способности позволяют агенту выполнять различные когнитивные задачи, такие как вспоминание информации, доступ к локальным файлам и веб-страницам, а также использование инструментов.

## Подробнее

Модуль предоставляет абстрактный базовый класс `TinyMentalFaculty`, от которого наследуются конкретные реализации ментальных способностей. Также модуль содержит классы `CustomMentalFaculty`, `RecallFaculty`, `FilesAndWebGroundingFaculty` и `TinyToolUse`, представляющие различные когнитивные способности агента.

## Классы

### `TinyMentalFaculty`

**Описание**:
Представляет собой ментальную способность агента. Ментальные способности - это когнитивные способности, которыми обладает агент.

**Аттрибуты**:
- `name` (str): Имя ментальной способности.
- `requires_faculties` (list): Список ментальных способностей, которые необходимы для правильной работы этой способности.

**Методы**:
- `__init__(self, name: str, requires_faculties: list=None) -> None`: Инициализирует ментальную способность.
- `__str__(self) -> str`: Возвращает строковое представление объекта `TinyMentalFaculty`.
- `__eq__(self, other)`: Сравнивает два объекта `TinyMentalFaculty` на равенство.
- `process_action(self, agent, action: dict) -> bool`: Обрабатывает действие, связанное с этой способностью.
- `actions_definitions_prompt(self) -> str`: Возвращает подсказку для определения действий, связанных с этой способностью.
- `actions_constraints_prompt(self) -> str`: Возвращает подсказку для определения ограничений на действия, связанные с этой способностью.

### `CustomMentalFaculty`

**Описание**:
Представляет собой пользовательскую ментальную способность агента. Пользовательские ментальные способности - это когнитивные способности, которые агент имеет и которые определяются пользователем просто путем указания действий, которые может выполнять способность, или ограничений, которые способность вводит. Ограничения могут быть связаны с действиями, которые может выполнять способность, или быть независимыми, более общими ограничениями, которым должен следовать агент.

**Наследует**:
`TinyMentalFaculty`

**Аттрибуты**:
- `actions_configs` (dict): Словарь с конфигурацией действий, которые может выполнять эта способность.
- `constraints` (dict): Список ограничений, введенных этой способностью.

**Методы**:
- `__init__(self, name: str, requires_faculties: list = None, actions_configs: dict = None, constraints: dict = None)`: Инициализирует пользовательскую ментальную способность.
- `add_action(self, action_name: str, description: str, function: Callable=None)`: Добавляет действие в конфигурацию действий.
- `add_actions(self, actions: dict)`: Добавляет несколько действий в конфигурацию действий.
- `add_action_constraint(self, constraint: str)`: Добавляет ограничение на действие.
- `add_actions_constraints(self, constraints: list)`: Добавляет несколько ограничений на действия.
- `process_action(self, agent, action: dict) -> bool`: Обрабатывает действие, связанное с этой способностью.
- `actions_definitions_prompt(self) -> str`: Возвращает подсказку для определения действий, связанных с этой способностью.
- `actions_constraints_prompt(self) -> str`: Возвращает подсказку для определения ограничений на действия, связанные с этой способностью.

### `RecallFaculty`

**Описание**:
Представляет собой способность агента вспоминать информацию из памяти.

**Наследует**:
`TinyMentalFaculty`

**Методы**:
- `__init__(self)`: Инициализирует способность вспоминать информацию.
- `process_action(self, agent, action: dict) -> bool`: Обрабатывает действие, связанное с этой способностью.
- `actions_definitions_prompt(self) -> str`: Возвращает подсказку для определения действий, связанных с этой способностью.
- `actions_constraints_prompt(self) -> str`: Возвращает подсказку для определения ограничений на действия, связанные с этой способностью.

### `FilesAndWebGroundingFaculty`

**Описание**:
Позволяет агенту получать доступ к локальным файлам и веб-страницам, чтобы обосновать свои знания.

**Наследует**:
`TinyMentalFaculty`

**Аттрибуты**:
- `local_files_grounding_connector` (LocalFilesGroundingConnector): Объект для доступа к локальным файлам.
- `web_grounding_connector` (WebPagesGroundingConnector): Объект для доступа к веб-страницам.

**Методы**:
- `__init__(self, folders_paths: list=None, web_urls: list=None)`: Инициализирует способность доступа к файлам и веб-страницам.
- `process_action(self, agent, action: dict) -> bool`: Обрабатывает действие, связанное с этой способностью.
- `actions_definitions_prompt(self) -> str`: Возвращает подсказку для определения действий, связанных с этой способностью.
- `actions_constraints_prompt(self) -> str`: Возвращает подсказку для определения ограничений на действия, связанные с этой способностью.

### `TinyToolUse`

**Описание**:
Позволяет агенту использовать инструменты для выполнения задач. Использование инструментов - один из наиболее важных когнитивных навыков, которыми обладают люди и приматы, насколько нам известно.

**Наследует**:
`TinyMentalFaculty`

**Аттрибуты**:
- `tools` (list): Список инструментов, которые может использовать агент.

**Методы**:
- `__init__(self, tools:list) -> None`: Инициализирует способность использования инструментов.
- `process_action(self, agent, action: dict) -> bool`: Обрабатывает действие, связанное с этой способностью.
- `actions_definitions_prompt(self) -> str`: Возвращает подсказку для определения действий, связанных с этой способностью.
- `actions_constraints_prompt(self) -> str`: Возвращает подсказку для определения ограничений на действия, связанные с этой способностью.

## Функции

### `TinyMentalFaculty.__init__`

```python
def __init__(self, name: str, requires_faculties: list=None) -> None:
    """
    Initializes the mental faculty.

    Args:
        name (str): The name of the mental faculty.
        requires_faculties (list): A list of mental faculties that this faculty requires to function properly.
    """
```

**Назначение**:
Инициализирует ментальную способность агента.

**Параметры**:
- `name` (str): Имя ментальной способности.
- `requires_faculties` (list, optional): Список ментальных способностей, которые необходимы для правильной работы этой способности. По умолчанию `None`.

**Возвращает**:
`None`

**Как работает функция**:

1.  Присваивает переданное имя атрибуту `self.name`.
2.  Если `requires_faculties` не указан (None), то инициализирует `self.requires_faculties` как пустой список. В противном случае присваивает переданный список атрибуту `self.requires_faculties`.

```
Инициализация
│
├───> Присвоение имени
│
└───> Проверка requires_faculties
    │
    ├───> requires_faculties is None: Инициализация пустым списком
    │
    └───> requires_faculties is not None: Присвоение списка requires_faculties
```

**Примеры**:

```python
faculty = TinyMentalFaculty("Memory", ["Reasoning"])
print(faculty.name)  # Output: Memory
print(faculty.requires_faculties)  # Output: ['Reasoning']

faculty2 = TinyMentalFaculty("Attention")
print(faculty2.requires_faculties)  # Output: []
```

### `TinyMentalFaculty.__str__`

```python
def __str__(self) -> str:
    """
    Returns the prompt for defining a actions related to this faculty.
    """
    return f"Mental Faculty: {self.name}"
```

**Назначение**:
Возвращает строковое представление объекта `TinyMentalFaculty`.

**Параметры**:
- `self` (TinyMentalFaculty): Ссылка на экземпляр класса.

**Возвращает**:
- `str`: Строковое представление ментальной способности.

**Как работает функция**:

1. Формирует строку в формате "Mental Faculty: {self.name}", где {self.name} заменяется на имя текущей ментальной способности.

```
Начало
│
└───> Формирование строки
    │
    └───> Возврат строки
```

**Примеры**:

```python
faculty = TinyMentalFaculty("Memory")
print(str(faculty))  # Output: Mental Faculty: Memory
```

### `TinyMentalFaculty.__eq__`

```python
def __eq__(self, other):
    """
    Returns the prompt for defining a actions related to this faculty.
    """
    if isinstance(other, TinyMentalFaculty):
        return self.name == other.name
    return False
```

**Назначение**:
Сравнивает текущий объект `TinyMentalFaculty` с другим объектом на равенство.

**Параметры**:
- `other` (Any): Объект для сравнения.

**Возвращает**:
- `bool`: True, если объекты равны (имеют одинаковое имя и являются экземплярами `TinyMentalFaculty`), иначе False.

**Как работает функция**:

1. Проверяет, является ли `other` экземпляром класса `TinyMentalFaculty`.
2. Если `other` является экземпляром `TinyMentalFaculty`, сравнивает имена текущей способности и `other`. Возвращает `True`, если имена совпадают, и `False` в противном случае.
3. Если `other` не является экземпляром `TinyMentalFaculty`, возвращает `False`.

```
Начало
│
└───> Проверка типа other
    │
    ├───> other is TinyMentalFaculty: Сравнение имен
    │   │
    │   ├───> Имена совпадают: Возврат True
    │   │
    │   └───> Имена не совпадают: Возврат False
    │
    └───> other is not TinyMentalFaculty: Возврат False
```

**Примеры**:

```python
faculty1 = TinyMentalFaculty("Memory")
faculty2 = TinyMentalFaculty("Memory")
faculty3 = TinyMentalFaculty("Reasoning")

print(faculty1 == faculty2)  # Output: True
print(faculty1 == faculty3)  # Output: False
print(faculty1 == "Memory")  # Output: False
```

### `TinyMentalFaculty.process_action`

```python
def process_action(self, agent, action: dict) -> bool:
    """
    Processes an action related to this faculty.

    Args:
        action (dict): The action to process.
    
    Returns:
        bool: True if the action was successfully processed, False otherwise.
    """
    raise NotImplementedError("Subclasses must implement this method.")
```

**Назначение**:
Обрабатывает действие, связанное с этой ментальной способностью.

**Параметры**:
- `agent` (Agent): Агент, выполняющий действие.
- `action` (dict): Действие для обработки.

**Возвращает**:
- `bool`: `True`, если действие было успешно обработано, `False` в противном случае.

**Вызывает исключения**:
- `NotImplementedError`: Всегда, так как метод должен быть переопределен в подклассах.

**Как работает функция**:

1.  Вызывает исключение `NotImplementedError`, указывающее, что подклассы должны реализовать этот метод.

```
Начало
│
└───> Вызов NotImplementedError
```

### `TinyMentalFaculty.actions_definitions_prompt`

```python
def actions_definitions_prompt(self) -> str:
    """
    Returns the prompt for defining a actions related to this faculty.
    """
    raise NotImplementedError("Subclasses must implement this method.")
```

**Назначение**:
Возвращает подсказку для определения действий, связанных с этой ментальной способностью.

**Параметры**:
- `self` (TinyMentalFaculty): Ссылка на экземпляр класса.

**Возвращает**:
- `str`: Подсказка для определения действий.

**Вызывает исключения**:
- `NotImplementedError`: Всегда, так как метод должен быть переопределен в подклассах.

**Как работает функция**:

1.  Вызывает исключение `NotImplementedError`, указывающее, что подклассы должны реализовать этот метод.

```
Начало
│
└───> Вызов NotImplementedError
```

### `TinyMentalFaculty.actions_constraints_prompt`

```python
def actions_constraints_prompt(self) -> str:
    """
    Returns the prompt for defining constraints on actions related to this faculty.
    """
    raise NotImplementedError("Subclasses must implement this method.")
```

**Назначение**:
Возвращает подсказку для определения ограничений на действия, связанные с этой ментальной способностью.

**Параметры**:
- `self` (TinyMentalFaculty): Ссылка на экземпляр класса.

**Возвращает**:
- `str`: Подсказка для определения ограничений на действия.

**Вызывает исключения**:
- `NotImplementedError`: Всегда, так как метод должен быть переопределен в подклассах.

**Как работает функция**:

1.  Вызывает исключение `NotImplementedError`, указывающее, что подклассы должны реализовать этот метод.

```
Начало
│
└───> Вызов NotImplementedError
```

### `CustomMentalFaculty.__init__`

```python
def __init__(self, name: str, requires_faculties: list = None,
                 actions_configs: dict = None, constraints: dict = None):
    """
    Initializes the custom mental faculty.

    Args:
        name (str): The name of the mental faculty.
        requires_faculties (list): A list of mental faculties that this faculty requires to function properly. 
          Format is ["faculty1", "faculty2", ...]
        actions_configs (dict): A dictionary with the configuration of actions that this faculty can perform.
          Format is {<action_name>: {"description": <description>, "function": <function>}}
        constraints (dict): A list with the constraints introduced by this faculty.
          Format is [<constraint1>, <constraint2>, ...]
    """
```

**Назначение**:
Инициализирует пользовательскую ментальную способность.

**Параметры**:
- `name` (str): Имя ментальной способности.
- `requires_faculties` (list, optional): Список ментальных способностей, которые необходимы для правильной работы этой способности. Формат: `["faculty1", "faculty2", ...]`. По умолчанию `None`.
- `actions_configs` (dict, optional): Словарь с конфигурацией действий, которые может выполнять эта способность. Формат: `{<action_name>: {"description": <description>, "function": <function>}}`. По умолчанию `None`.
- `constraints` (dict, optional): Список ограничений, введенных этой способностью. Формат: `[<constraint1>, <constraint2>, ...]`. По умолчанию `None`.

**Возвращает**:
- `None`

**Как работает функция**:

1.  Вызывает конструктор базового класса `TinyMentalFaculty` с переданными именем и списком необходимых способностей.
2.  Если `actions_configs` не указан (None), то инициализирует `self.actions_configs` как пустой словарь. В противном случае присваивает переданный словарь атрибуту `self.actions_configs`.
3.  Если `constraints` не указан (None), то инициализирует `self.constraints` как пустой словарь. В противном случае присваивает переданный список атрибуту `self.constraints`.

```
Инициализация
│
├───> Вызов конструктора TinyMentalFaculty
│
├───> Проверка actions_configs
│   │
│   ├───> actions_configs is None: Инициализация пустым словарем
│   │
│   └───> actions_configs is not None: Присвоение словаря actions_configs
│
└───> Проверка constraints
    │
    ├───> constraints is None: Инициализация пустым словарем
    │
    └───> constraints is not None: Присвоение списка constraints
```

**Примеры**:

```python
faculty = CustomMentalFaculty("Custom", ["Memory"], {"action1": {"description": "Do something", "function": None}}, ["constraint1"])
print(faculty.name)  # Output: Custom
print(faculty.requires_faculties)  # Output: ['Memory']
print(faculty.actions_configs)  # Output: {'action1': {'description': 'Do something', 'function': None}}
print(faculty.constraints)  # Output: ['constraint1']

faculty2 = CustomMentalFaculty("Another")
print(faculty2.actions_configs)  # Output: {}
print(faculty2.constraints)  # Output: {}
```

### `CustomMentalFaculty.add_action`

```python
def add_action(self, action_name: str, description: str, function: Callable=None):
    """
    Returns the prompt for defining a actions related to this faculty.
    """
    self.actions_configs[action_name] = {"description": description, "function": function}
```

**Назначение**:
Добавляет новое действие в конфигурацию действий данной ментальной способности.

**Параметры**:
- `action_name` (str): Имя добавляемого действия.
- `description` (str): Описание добавляемого действия.
- `function` (Callable, optional): Функция, связанная с данным действием. По умолчанию `None`.

**Возвращает**:
`None`

**Как работает функция**:

1. Добавляет в словарь `self.actions_configs` новую запись, где ключом является `action_name`, а значением — словарь с ключами `"description"` и `"function"`, соответствующими переданным аргументам `description` и `function`.

```
Добавление действия
│
└───> Обновление self.actions_configs с новым действием
```

**Примеры**:

```python
faculty = CustomMentalFaculty("Custom")
faculty.add_action("ACTION1", "Description of action 1", lambda agent, action: None)
print(faculty.actions_configs)
# Output: {'ACTION1': {'description': 'Description of action 1', 'function': <function <lambda> at 0x...>}}
```

### `CustomMentalFaculty.add_actions`

```python
def add_actions(self, actions: dict):
    """
    Returns the prompt for defining a actions related to this faculty.
    """
    for action_name, action_config in actions.items():
        self.add_action(action_name, action_config['description'], action_config['function'])
```

**Назначение**:
Добавляет несколько действий в конфигурацию действий данной ментальной способности.

**Параметры**:
- `actions` (dict): Словарь, где ключи — имена действий, а значения — словари с ключами `"description"` и `"function"`.

**Возвращает**:
`None`

**Как работает функция**:

1. Перебирает все элементы словаря `actions`.
2. Для каждого элемента вызывает метод `self.add_action` с именем действия, описанием и функцией из словаря `actions`.

```
Добавление нескольких действий
│
└───> Перебор элементов словаря actions
    │
    └───> Вызов self.add_action для каждого действия
```

**Примеры**:

```python
faculty = CustomMentalFaculty("Custom")
actions = {
    "ACTION1": {"description": "Description of action 1", "function": lambda agent, action: None},
    "ACTION2": {"description": "Description of action 2", "function": lambda agent, action: None}
}
faculty.add_actions(actions)
print(faculty.actions_configs)
# Output: {'ACTION1': {'description': 'Description of action 1', 'function': <function <lambda> at 0x...>}, 'ACTION2': {'description': 'Description of action 2', 'function': <function <lambda> at 0x...>}}
```

### `CustomMentalFaculty.add_action_constraint`

```python
def add_action_constraint(self, constraint: str):
    """
    Returns the prompt for defining a actions related to this faculty.
    """
    self.constraints.append(constraint)
```

**Назначение**:
Добавляет новое ограничение на действия данной ментальной способности.

**Параметры**:
- `constraint` (str): Текст ограничения.

**Возвращает**:
`None`

**Как работает функция**:

1. Добавляет переданный текст ограничения в список `self.constraints`.

```
Добавление ограничения
│
└───> Добавление ограничения в self.constraints
```

**Примеры**:

```python
faculty = CustomMentalFaculty("Custom")
faculty.add_action_constraint("Constraint 1")
print(faculty.constraints)
# Output: ['Constraint 1']
```

### `CustomMentalFaculty.add_actions_constraints`

```python
def add_actions_constraints(self, constraints: list):
    """
    Returns the prompt for defining a actions related to this faculty.
    """
    for constraint in constraints:
        self.add_action_constraint(constraint)
```

**Назначение**:
Добавляет несколько ограничений на действия данной ментальной способности.

**Параметры**:
- `constraints` (list): Список ограничений.

**Возвращает**:
`None`

**Как работает функция**:

1. Перебирает все элементы списка `constraints`.
2. Для каждого элемента вызывает метод `self.add_action_constraint` с текстом ограничения.

```
Добавление нескольких ограничений
│
└───> Перебор элементов списка constraints
    │
    └───> Вызов self.add_action_constraint для каждого ограничения
```

**Примеры**:

```python
faculty = CustomMentalFaculty("Custom")
constraints = ["Constraint 1", "Constraint 2"]
faculty.add_actions_constraints(constraints)
print(faculty.constraints)
# Output: ['Constraint 1', 'Constraint 2']
```

### `CustomMentalFaculty.process_action`

```python
def process_action(self, agent, action: dict) -> bool:
    """
    Returns the prompt for defining a actions related to this faculty.
    """
    agent.logger.debug(f"Processing action: {action}")

    action_type = action['type']
    if action_type in self.actions_configs:
        action_config = self.actions_configs[action_type]
        action_function = action_config.get("function", None)

        if action_function is not None:
            action_function(agent, action)
        
        # one way or another, the action was processed
        return True 
    
    else:
        return False
```

**Назначение**:
Обрабатывает действие, связанное с этой ментальной способностью.

**Параметры**:
- `agent` (Agent): Агент, выполняющий действие.
- `action` (dict): Действие для обработки (словарь, содержащий информацию о действии).

**Возвращает**:
- `bool`: True, если действие было успешно обработано, False в противном случае.

**Как работает функция**:

1.  Логирует информацию об обрабатываемом действии с использованием `agent.logger.debug`.
2.  Извлекает тип действия из словаря `action` по ключу `"type"`.
3.  Проверяет, содержится ли тип действия в ключах словаря `self.actions_configs`.
4.  Если тип действия содержится в `self.actions_configs`:
    - Извлекает конфигурацию действия из `self.actions_configs` по типу действия.
    - Извлекает функцию действия из конфигурации действия по ключу `"function"` (если функция не указана, то `action_function` будет `None`).
    - Если `action_function` не `None`, то вызывает эту функцию, передавая ей `agent` и `action` в качестве аргументов.
    - Возвращает `True`, так как действие было обработано (даже если функция не была вызвана).
5.  Если тип действия не содержится в `self.actions_configs`, возвращает `False`.

```
Обработка действия
│
├───> Логирование информации о действии
│
├───> Извлечение типа действия
│
├───> Проверка типа действия в self.actions_configs
│   │
│   ├───> Тип действия найден:
│   │   │
│   │   ├───> Извлечение конфигурации действия
│   │   │
│   │   ├───> Извлечение функции действия
│   │   │
│   │   ├───> Проверка action_function
│   │   │   │
│   │   │   ├───> action_function is not None: Вызов action_function
│   │   │   │
│   │   │   └───> action_function is None: Пропуск вызова
│   │   │
│   │   └───> Возврат True
│   │
│   └───> Тип действия не найден: Возврат False
```

**Примеры**:

```python
def my_action_function(agent, action):
    agent.name = "Action processed"

faculty = CustomMentalFaculty("Custom")
faculty.add_action("MY_ACTION", "Description", my_action_function)
agent = Agent()
agent.name = "Original name"
action = {"type": "MY_ACTION"}
result = faculty.process_action(agent, action)
print(result)  # Output: True
print(agent.name)  # Output: Action processed

action = {"type": "UNKNOWN_ACTION"}
result = faculty.process_action(agent, action)
print(result)  # Output: False
```

### `CustomMentalFaculty.actions_definitions_prompt`

```python
def actions_definitions_prompt(self) -> str:
    """
    Returns the prompt for defining a actions related to this faculty.
    """
    prompt = ""
    for action_name, action_config in self.actions_configs.items():
        prompt += f"  - {action_name.upper()}: {action_config['description']}\\n"
    
    return prompt
```

**Назначение**:
Формирует строку подсказки для определения действий, связанных с данной ментальной способностью.

**Параметры**:
- `self` (CustomMentalFaculty): Ссылка на экземпляр класса.

**Возвращает**:
- `str`: Строка подсказки, содержащая определения действий.

**Как работает функция**:

1. Инициализирует пустую строку `prompt`.
2. Перебирает все элементы словаря `self.actions_configs`.
3. Для каждого элемента формирует строку в формате `" - {action_name.upper()}: {action_config['description']}\\n"`, где `action_name` преобразуется в верхний регистр, а `action_config['description']` — описание действия.
4. Добавляет сформированную строку к `prompt`.
5. Возвращает строку `prompt`.

```
Формирование строки подсказки
│
├───> Инициализация пустой строки prompt
│
├───> Перебор элементов словаря self.actions_configs
│   │
│   └───> Формирование строки с определением действия
│   │
│   └───> Добавление строки к prompt
│
└───> Возврат строки prompt
```

**Примеры**:

```python
faculty = CustomMentalFaculty("Custom")
faculty.add_action("action1", "Description of action 1")
faculty.add_action("action2", "Description of action 2")
prompt = faculty.actions_definitions_prompt()
print(prompt)
# Output:
#   - ACTION1: Description of action 1\n  - ACTION2: Description of action 2\n
```

### `CustomMentalFaculty.actions_constraints_prompt`

```python
def actions_constraints_prompt(self) -> str:
    """
    Returns the prompt for defining constraints on actions related to this faculty.
    """
    prompt = ""
    for constraint in self.constraints:
        prompt += f"  - {constraint}\\n"
    
    return prompt
```

**Назначение**:
Формирует строку подсказки для определения ограничений на действия, связанные с данной ментальной способностью.

**Параметры**:
- `self` (CustomMentalFaculty): Ссылка на экземпляр класса.

**Возвращает**:
- `str`: Строка подсказки, содержащая ограничения на действия.

**Как работает функция**:

1. Инициализирует пустую строку `prompt`.
2. Перебирает все элементы списка `self.constraints`.
3. Для каждого элемента формирует строку в формате `" - {constraint}\\n"`.
4. Добавляет сформированную строку к `prompt`.
5. Возвращает строку `prompt`.

```
Формирование строки подсказки об ограничениях
│
├───> Инициализация пустой строки prompt
│
├───> Перебор элементов списка self.constraints
│   │
│   └───> Формирование строки с ограничением
│   │
│   └───> Добавление строки к prompt
│
└───> Возврат строки prompt
```

**Примеры**:

```python
faculty = CustomMentalFaculty("Custom")
faculty.add_action_constraint("Constraint 1")
faculty.add_action_constraint("Constraint 2")
prompt = faculty.actions_constraints_prompt()
print(prompt)
# Output:
#   - Constraint 1\n  - Constraint 2\n
```

### `RecallFaculty.__init__`

```python
def __init__(self):
    """
    Returns the prompt for defining constraints on actions related to this faculty.
    """
    super().__init__("Memory Recall")
```

**Назначение**:
Инициализирует объект класса `RecallFaculty`.

**Параметры**:
- `self` (RecallFaculty): Ссылка на экземпляр класса.

**Возвращает**:
`None`

**Как работает функция**:

1. Вызывает конструктор базового класса `TinyMentalFaculty` с именем "Memory Recall".

```
Инициализация
│
└───> Вызов конструктора TinyMentalFaculty с именем "Memory Recall"
```

**Примеры**:

```python
faculty = RecallFaculty()
print(faculty.name)  # Output: Memory Recall
```

### `RecallFaculty.process_action`

```python
def process_action(self, agent, action: dict) -> bool:
    """
    Returns the prompt for defining constraints on actions related to this faculty.
    """
    agent.logger.debug(f"Processing action: {action}")

    if action['type'] == "RECALL" and action['content'] is not None:
        content = action['content']

        semantic_memories = agent.retrieve_relevant_memories(relevance_target=content)

        agent.logger.info(f"Recalling information related to '{content}'. Found {len(semantic_memories)} relevant memories.")

        if len(semantic_memories) > 0:
            # a string with each element in the list in a new line starting with a bullet point
            agent.think("I have remembered the following information from my semantic memory and will use it to guide me in my subsequent actions: \n" + \
                    "\n".join([f"  - {item}" for item in semantic_memories]))
        else:
            agent.think(f"I can't remember anything about '{content}'.")
        
        return True
    
    else:
        return False
```

**Назначение**:
Обрабатывает действие, связанное с вспоминанием информации из памяти.

**Параметры**:
- `agent` (Agent): Агент, выполняющий действие.
- `action` (dict): Действие для обработки (словарь, содержащий информацию о действии).

**Возвращает**:
- `bool`: True, если действие было успешно обработано, False в противном случае.

**Как работает функция**:

1. Логирует информацию об обрабатываемом действии с использованием `agent.logger.debug`.
2. Проверяет, что тип действия равен "RECALL" и что в действии указано содержимое (`action['content'] is not None`).
3. Если условия выполнены:
    - Извлекает содержимое из действия (`content = action['content']`).
    - Вызывает метод `agent.retrieve_relevant_memories` для получения релевантных воспоминаний на основе содержимого.
    - Логирует информацию о количестве найденных воспоминаний с использованием `agent.logger.info`.
    - Если найдены воспоминания (их количество больше 0):
        - Формирует строку с перечислением воспоминаний и вызывает метод `agent.think` для добавления этой информации в мысли агента.
    - Если воспоминания не найдены:
        - Вызывает метод `agent.think` для добавления сообщения о невозможности вспомнить что-либо.
    - Возвращает `True`, так как действие было обработано.
4. Если условия не выполнены, возвращает `False`.

```
Обработка действия Recall
│
├───> Логирование информации о действии
│
├───> Проверка типа действия и наличия содержимого
│   │
│   ├───> Условия выполнены:
│   │   │
│   │   ├───> Извлечение содержимого
│   │   │
│   │   ├───> Получение релевантных воспоминаний
│   │   │
│   │   ├───> Логирование информации о найденных воспоминаниях
│   │   │
│   │   ├───> Проверка количества воспоминаний
│   │   │   │
│   │   │   ├───> Воспоминания найдены: Формирование строки и вызов agent.think
│   │   │   │
│   │   │   └───> Воспоминания не найдены: Вызов agent.think с сообщением о невозможности вспомнить
│   │   │
│   │   └───> Возврат True
│   │
│   └───> Условия не выполнены: Возврат False
```

**Примеры**:

```python
class MockAgent:
    def __init__(self):
        self.memories = ["Memory 1", "Memory 2"]
        self.thought = None
    
    def retrieve_relevant_memories(self, relevance_target):
        return self.memories
    
    def think(self, thought):
        self.thought = thought