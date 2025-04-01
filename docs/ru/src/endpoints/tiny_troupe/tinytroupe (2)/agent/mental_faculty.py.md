# Модуль для работы с ментальными способностями агента
========================================================

Модуль содержит классы для представления и управления ментальными способностями агента, такие как память, доступ к файлам и использование инструментов.

## Обзор

Этот модуль предоставляет основу для определения и использования различных ментальных способностей агента. Ментальные способности позволяют агенту выполнять различные когнитивные задачи, такие как вспоминание информации, доступ к локальным файлам и веб-страницам, а также использование внешних инструментов.

## Подробнее

Модуль определяет абстрактный класс `TinyMentalFaculty`, который служит базовым классом для всех ментальных способностей. Он также включает конкретные реализации, такие как `CustomMentalFaculty`, `RecallFaculty`, `FilesAndWebGroundingFaculty` и `TinyToolUse`, которые предоставляют агенту различные когнитивные возможности.

## Классы

### `TinyMentalFaculty`

**Описание**:
Абстрактный базовый класс, представляющий ментальную способность агента.

**Атрибуты**:
- `name` (str): Название ментальной способности.
- `requires_faculties` (list): Список ментальных способностей, необходимых для функционирования данной способности.

**Методы**:
- `__init__(self, name: str, requires_faculties: list = None) -> None`:
    Инициализирует ментальную способность.
- `__str__(self) -> str`:
    Возвращает строковое представление ментальной способности.
- `__eq__(self, other)`:
    Сравнивает два объекта `TinyMentalFaculty` на равенство.
- `process_action(self, agent, action: dict) -> bool`:
    Абстрактный метод для обработки действия, связанного с этой способностью. Должен быть реализован в подклассах.
- `actions_definitions_prompt(self) -> str`:
    Абстрактный метод, возвращающий описание действий, связанных с этой способностью. Должен быть реализован в подклассах.
- `actions_constraints_prompt(self) -> str`:
    Абстрактный метод, возвращающий описание ограничений на действия, связанные с этой способностью. Должен быть реализован в подклассах.

### `CustomMentalFaculty`

**Описание**:
Класс, представляющий пользовательскую ментальную способность агента. Позволяет определять действия и ограничения для данной способности.

**Наследует**:
`TinyMentalFaculty`

**Атрибуты**:
- `actions_configs` (dict): Словарь с конфигурацией действий, которые может выполнять эта способность. Формат: `{<action_name>: {"description": <description>, "function": <function>}}`.
- `constraints` (dict): Список ограничений, введенных этой способностью. Формат: `[<constraint1>, <constraint2>, ...]`.

**Методы**:
- `__init__(self, name: str, requires_faculties: list = None, actions_configs: dict = None, constraints: dict = None)`:
    Инициализирует пользовательскую ментальную способность.
- `add_action(self, action_name: str, description: str, function: Callable = None)`:
    Добавляет действие в конфигурацию действий.
- `add_actions(self, actions: dict)`:
    Добавляет несколько действий из словаря в конфигурацию действий.
- `add_action_constraint(self, constraint: str)`:
    Добавляет ограничение для действий.
- `add_actions_constraints(self, constraints: list)`:
    Добавляет несколько ограничений из списка.
- `process_action(self, agent, action: dict) -> bool`:
    Обрабатывает действие, связанное с этой способностью.
- `actions_definitions_prompt(self) -> str`:
    Возвращает описание действий, связанных с этой способностью.
- `actions_constraints_prompt(self) -> str`:
    Возвращает описание ограничений на действия, связанные с этой способностью.

### `RecallFaculty`

**Описание**:
Класс, представляющий способность агента вспоминать информацию из памяти.

**Наследует**:
`TinyMentalFaculty`

**Методы**:
- `__init__(self)`:
    Инициализирует способность вспоминать информацию.
- `process_action(self, agent, action: dict) -> bool`:
    Обрабатывает действие `RECALL`, извлекая релевантные воспоминания из семантической памяти агента.
- `actions_definitions_prompt(self) -> str`:
    Возвращает описание действия `RECALL`.
- `actions_constraints_prompt(self) -> str`:
    Возвращает описание ограничений на действие `RECALL`.

### `FilesAndWebGroundingFaculty`

**Описание**:
Класс, предоставляющий агенту доступ к локальным файлам и веб-страницам для обоснования своих знаний.

**Наследует**:
`TinyMentalFaculty`

**Атрибуты**:
- `local_files_grounding_connector` (LocalFilesGroundingConnector): Коннектор для доступа к локальным файлам.
- `web_grounding_connector` (WebPagesGroundingConnector): Коннектор для доступа к веб-страницам.

**Методы**:
- `__init__(self, folders_paths: list = None, web_urls: list = None)`:
    Инициализирует способность доступа к файлам и веб-страницам.
- `process_action(self, agent, action: dict) -> bool`:
    Обрабатывает действия `CONSULT` и `LIST_DOCUMENTS`, позволяя агенту получать доступ к содержимому документов и спискам доступных документов.
- `actions_definitions_prompt(self) -> str`:
    Возвращает описание действий `CONSULT` и `LIST_DOCUMENTS`.
- `actions_constraints_prompt(self) -> str`:
    Возвращает описание ограничений на действия `CONSULT` и `LIST_DOCUMENTS`.

### `TinyToolUse`

**Описание**:
Класс, позволяющий агенту использовать инструменты для выполнения задач.

**Наследует**:
`TinyMentalFaculty`

**Атрибуты**:
- `tools` (list): Список инструментов, доступных агенту.

**Методы**:
- `__init__(self, tools: list) -> None`:
    Инициализирует способность использования инструментов.
- `process_action(self, agent, action: dict) -> bool`:
    Перебирает доступные инструменты и пытается обработать действие с помощью одного из них.
- `actions_definitions_prompt(self) -> str`:
    Возвращает объединенное описание действий для всех доступных инструментов.
- `actions_constraints_prompt(self) -> str`:
    Возвращает объединенное описание ограничений на действия для всех доступных инструментов.

## Функции

В данном модуле функции отсутствуют.

## Как работает модуль

Модуль предоставляет набор классов, которые представляют различные ментальные способности агента. Каждая ментальная способность определяет, какие действия агент может выполнять и какие ограничения должны соблюдаться при выполнении этих действий. Агент использует эти способности для взаимодействия с окружающей средой и достижения своих целей.

## Примеры

Примеры использования каждого класса можно найти в их docstring.

```python
# Пример создания и использования CustomMentalFaculty
from typing import Callable, Optional

class CustomMentalFaculty(TinyMentalFaculty):
    """
    Represents a custom mental faculty of an agent. Custom mental faculties are the cognitive abilities that an agent has
    and that are defined by the user just by specifying the actions that the faculty can perform or the constraints that
    the faculty introduces. Constraints might be related to the actions that the faculty can perform or be independent,
    more general constraints that the agent must follow.
    """

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

        super().__init__(name, requires_faculties)

        # {<action_name>: {"description": <description>, "function": <function>}}
        if actions_configs is None:
            self.actions_configs = {}
        else:
            self.actions_configs = actions_configs
        
        # [<constraint1>, <constraint2>, ...]
        if constraints is None:
            self.constraints = {}
        else:
            self.constraints = constraints
    
    def add_action(self, action_name: str, description: str, function: Callable=None):
        self.actions_configs[action_name] = {"description": description, "function": function}

    def add_actions(self, actions: dict):
        for action_name, action_config in actions.items():
            self.add_action(action_name, action_config['description'], action_config['function'])
    
    def add_action_constraint(self, constraint: str):
        self.constraints.append(constraint)
    
    def add_actions_constraints(self, constraints: list):
        for constraint in constraints:
            self.add_action_constraint(constraint)

    def process_action(self, agent, action: dict) -> bool:
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
    
    def actions_definitions_prompt(self) -> str:
        prompt = ""
        for action_name, action_config in self.actions_configs.items():
            prompt += f"  - {action_name.upper()}: {action_config['description']}\n"
        
        return prompt

    def actions_constraints_prompt(self) -> str:
        prompt = ""
        for constraint in self.constraints:
            prompt += f"  - {constraint}\n"
        
        return prompt
    

# Пример использования
class Agent:
    def __init__(self):
        self.logger = logger

    def think(self, content: str):
        print(f"Agent is thinking: {content}")

agent = Agent()

def example_action(agent: Agent, action: dict):
    print(f"Executing action: {action}")

custom_faculty = CustomMentalFaculty(
    name="ExampleFaculty",
    actions_configs={
        "EXAMPLE_ACTION": {
            "description": "Example action description",
            "function": example_action,
        }
    },
    constraints=["Constraint 1", "Constraint 2"]
)

action = {"type": "EXAMPLE_ACTION"}
custom_faculty.process_action(agent, action)