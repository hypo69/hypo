# Модуль TinyTool

## Обзор

Модуль `TinyTool` определяет базовый класс для создания инструментов, используемых агентами в системе `tinytroupe`. Он предоставляет общую структуру для инструментов, включая атрибуты, такие как имя, описание, владелец, а также методы для обработки действий, проверки владения и защиты от нежелательных побочных эффектов в реальном мире. Этот модуль является частью фреймворка для разработки виртуальных ассистентов и агентов, взаимодействующих в некоторой среде.

## Подробней

Модуль `TinyTool` предоставляет абстрактный класс, который служит основой для создания различных инструментов, используемых в системе `tinytroupe`. Он включает механизмы для контроля владения инструментами, предупреждения о потенциальных побочных эффектах в реальном мире и обработки действий агентов.

## Классы

### `TinyTool`

**Описание**: Базовый класс для инструментов, используемых агентами.

**Принцип работы**:

Класс `TinyTool` предоставляет основу для создания инструментов, которые могут быть использованы агентами. Он включает механизмы для защиты от нежелательных побочных эффектов в реальном мире, проверки владения инструментом и обработки действий агентов.

**Наследует**:

- `JsonSerializableRegistry`: Класс, обеспечивающий сериализацию и десериализацию объектов в формат JSON.

**Атрибуты**:

- `name` (str): Имя инструмента.
- `description` (str): Краткое описание инструмента.
- `owner` (str): Агент, владеющий инструментом. Если `None`, инструмент может использоваться любым агентом.
- `real_world_side_effects` (bool): Указывает, имеет ли инструмент побочные эффекты в реальном мире.
- `exporter` (ArtifactExporter): Экспортер для сохранения результатов работы инструмента.
- `enricher` (Enricher): Обогатитель для добавления дополнительной информации к результатам работы инструмента.

**Методы**:

- `__init__(self, name, description, owner=None, real_world_side_effects=False, exporter=None, enricher=None)`: Инициализация нового инструмента.
- `_process_action(self, agent, action: dict) -> bool`: Абстрактный метод для обработки действий агента. Должен быть реализован в подклассах.
- `_protect_real_world(self)`: Выводит предупреждение, если инструмент имеет побочные эффекты в реальном мире.
- `_enforce_ownership(self, agent)`: Проверяет, имеет ли агент право на использование инструмента.
- `set_owner(self, owner)`: Устанавливает владельца инструмента.
- `actions_definitions_prompt(self) -> str`: Абстрактный метод, возвращающий описание действий инструмента в формате строки. Должен быть реализован в подклассах.
- `actions_constraints_prompt(self) -> str`: Абстрактный метод, возвращающий ограничения на действия инструмента в формате строки. Должен быть реализован в подклассах.
- `process_action(self, agent, action: dict) -> bool`: Обрабатывает действие агента, проверяя наличие побочных эффектов и право собственности.

## Функции

### `__init__`

```python
def __init__(self, name, description, owner=None, real_world_side_effects=False, exporter=None, enricher=None):
```

**Назначение**: Инициализация экземпляра класса `TinyTool`.

**Параметры**:

- `name` (str): Имя инструмента.
- `description` (str): Описание инструмента.
- `owner` (str, optional): Владелец инструмента. По умолчанию `None`.
- `real_world_side_effects` (bool, optional): Флаг, указывающий на наличие побочных эффектов в реальном мире. По умолчанию `False`.
- `exporter` (ArtifactExporter, optional): Экспортер результатов. По умолчанию `None`.
- `enricher` (Enricher, optional): Обогатитель результатов. По умолчанию `None`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- Отсутствуют явные исключения, но могут быть вызваны исключения из родительского класса или других вызываемых методов.

**Как работает функция**:

1. Функция инициализирует атрибуты экземпляра класса `TinyTool` значениями, переданными в качестве аргументов.
2. Устанавливает имя инструмента (`self.name`), описание (`self.description`), владельца (`self.owner`), флаг побочных эффектов (`self.real_world_side_effects`), экспортер (`self.exporter`) и обогатитель (`self.enricher`).

**Примеры**:

```python
from tinytroupe.tools.tiny_tool import TinyTool

tool = TinyTool(name='MyTool', description='A simple tool', owner='Agent1', real_world_side_effects=False)
print(tool.name)  # MyTool
print(tool.description) # A simple tool
print(tool.owner) # Agent1
print(tool.real_world_side_effects) # False
```

### `_process_action`

```python
def _process_action(self, agent, action: dict) -> bool:
```

**Назначение**: Абстрактный метод для обработки действий агента.

**Параметры**:

- `agent`: Агент, выполняющий действие.
- `action` (dict): Словарь, представляющий действие агента.

**Возвращает**:

- `bool`: Должен возвращать `True`, если действие было успешно обработано, и `False` в противном случае.

**Вызывает исключения**:

- `NotImplementedError`: Вызывается, так как метод должен быть переопределен в подклассах.

**Как работает функция**:

1. Метод `_process_action` предназначен для обработки действий, выполняемых агентами с использованием данного инструмента.
2. Поскольку это абстрактный метод, он не имеет реализации в базовом классе `TinyTool` и должен быть переопределен в подклассах для предоставления конкретной логики обработки действий.

**Примеры**:

```python
from tinytroupe.tools.tiny_tool import TinyTool

class MyTool(TinyTool):
    def __init__(self, name, description, owner=None, real_world_side_effects=False, exporter=None, enricher=None):
        super().__init__(name, description, owner, real_world_side_effects, exporter, enricher)

    def _process_action(self, agent, action: dict) -> bool:
        print(f"Agent {agent.name} выполнил действие: {action}")
        return True

# Создание инстанса класса MyTool
tool = MyTool(name='MyTool', description='A simple tool')

# Пример вызова функции _process_action
# agent = ...  # Необходима инициализация агента
# action = {'type': 'example_action', 'param': 'example_value'}
# result = tool._process_action(agent, action)
# print(result)
```

### `_protect_real_world`

```python
def _protect_real_world(self):
```

**Назначение**: Выводит предупреждение в лог, если инструмент имеет побочные эффекты в реальном мире.

**Параметры**:

- `self`: Экземпляр класса `TinyTool`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- Отсутствуют.

**Как работает функция**:

1. Функция проверяет, установлен ли флаг `real_world_side_effects` в `True`.
2. Если флаг установлен, функция выводит предупреждение в лог с использованием модуля `logger`, указывающее на то, что инструмент имеет побочные эффекты в реальном мире и должен использоваться с осторожностью.

**Примеры**:

```python
from tinytroupe.tools.tiny_tool import TinyTool
from tinytroupe.tools import logger
# Пример с real_world_side_effects = True
tool_with_side_effects = TinyTool(name='DangerousTool', description='Tool with real-world side effects', real_world_side_effects=True)
tool_with_side_effects._protect_real_world()  # Выведет предупреждение в лог

# Пример с real_world_side_effects = False
tool_without_side_effects = TinyTool(name='SafeTool', description='Tool without real-world side effects', real_world_side_effects=False)
tool_without_side_effects._protect_real_world()  # Ничего не выведет
```

### `_enforce_ownership`

```python
def _enforce_ownership(self, agent):
```

**Назначение**: Проверяет, имеет ли агент право на использование инструмента.

**Параметры**:

- `self`: Экземпляр класса `TinyTool`.
- `agent`: Агент, пытающийся использовать инструмент.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `ValueError`: Если агент не является владельцем инструмента.

**Как работает функция**:

1. Функция проверяет, установлен ли владелец инструмента (`self.owner`).
2. Если владелец установлен, функция сравнивает имя агента (`agent.name`) с именем владельца (`self.owner.name`).
3. Если агент не является владельцем, функция вызывает исключение `ValueError` с сообщением об ошибке.

**Примеры**:

```python
from tinytroupe.tools.tiny_tool import TinyTool

# Пример с владельцем
class Agent:
    def __init__(self, name):
        self.name = name

agent1 = Agent('Agent1')
agent2 = Agent('Agent2')
tool_owned = TinyTool(name='OwnedTool', description='Tool owned by Agent1', owner=agent1)

tool_owned._enforce_ownership(agent1)  # Не вызовет исключение

try:
    tool_owned._enforce_ownership(agent2)  # Вызовет ValueError
except ValueError as ex:
    print(ex)  # Agent Agent2 does not own tool OwnedTool, which is owned by Agent1.

# Пример без владельца
tool_unowned = TinyTool(name='UnownedTool', description='Tool without owner')
tool_unowned._enforce_ownership(agent2)  # Не вызовет исключение
```

### `set_owner`

```python
def set_owner(self, owner):
```

**Назначение**: Устанавливает владельца инструмента.

**Параметры**:

- `self`: Экземпляр класса `TinyTool`.
- `owner`: Агент, который будет установлен в качестве владельца инструмента.

**Возвращает**:

- `None`

**Вызывает исключения**:

- Отсутствуют.

**Как работает функция**:

1. Функция устанавливает атрибут `self.owner` равным значению, переданному в параметре `owner`.

**Примеры**:

```python
from tinytroupe.tools.tiny_tool import TinyTool

class Agent:
    def __init__(self, name):
        self.name = name

agent1 = Agent('Agent1')
agent2 = Agent('Agent2')
tool = TinyTool(name='MyTool', description='A simple tool')

tool.set_owner(agent1)
print(tool.owner.name)  # Agent1

tool.set_owner(agent2)
print(tool.owner.name)  # Agent2
```

### `actions_definitions_prompt`

```python
def actions_definitions_prompt(self) -> str:
```

**Назначение**: Абстрактный метод, возвращающий описание действий инструмента в формате строки.

**Параметры**:

- `self`: Экземпляр класса `TinyTool`.

**Возвращает**:

- `str`: Описание действий инструмента.

**Вызывает исключения**:

- `NotImplementedError`: Вызывается, так как метод должен быть переопределен в подклассах.

**Как работает функция**:

1. Функция `actions_definitions_prompt` предназначена для предоставления описания действий, которые может выполнять данный инструмент.
2. Поскольку это абстрактный метод, он не имеет реализации в базовом классе `TinyTool` и должен быть переопределен в подклассах для предоставления конкретного описания действий.

**Примеры**:

```python
from tinytroupe.tools.tiny_tool import TinyTool

class MyTool(TinyTool):
    def __init__(self, name, description, owner=None, real_world_side_effects=False, exporter=None, enricher=None):
        super().__init__(name, description, owner, real_world_side_effects, exporter, enricher)

    def actions_definitions_prompt(self) -> str:
        return "Действия: выполнить задачу, проверить статус"

# Создание инстанса класса MyTool
tool = MyTool(name='MyTool', description='A simple tool')

# Пример вызова функции actions_definitions_prompt
result = tool.actions_definitions_prompt()
print(result)  # Действия: выполнить задачу, проверить статус
```

### `actions_constraints_prompt`

```python
def actions_constraints_prompt(self) -> str:
```

**Назначение**: Абстрактный метод, возвращающий ограничения на действия инструмента в формате строки.

**Параметры**:

- `self`: Экземпляр класса `TinyTool`.

**Возвращает**:

- `str`: Ограничения на действия инструмента.

**Вызывает исключения**:

- `NotImplementedError`: Вызывается, так как метод должен быть переопределен в подклассах.

**Как работает функция**:

1. Функция `actions_constraints_prompt` предназначена для предоставления описания ограничений на действия, которые может выполнять данный инструмент.
2. Поскольку это абстрактный метод, он не имеет реализации в базовом классе `TinyTool` и должен быть переопределен в подклассах для предоставления конкретного описания ограничений.

**Примеры**:

```python
from tinytroupe.tools.tiny_tool import TinyTool

class MyTool(TinyTool):
    def __init__(self, name, description, owner=None, real_world_side_effects=False, exporter=None, enricher=None):
        super().__init__(name, description, owner, real_world_side_effects, exporter, enricher)

    def actions_constraints_prompt(self) -> str:
        return "Ограничения: нельзя выполнять более одной задачи одновременно"

# Создание инстанса класса MyTool
tool = MyTool(name='MyTool', description='A simple tool')

# Пример вызова функции actions_constraints_prompt
result = tool.actions_constraints_prompt()
print(result)  # Ограничения: нельзя выполнять более одной задачи одновременно
```

### `process_action`

```python
def process_action(self, agent, action: dict) -> bool:
```

**Назначение**: Обрабатывает действие агента, проверяя наличие побочных эффектов и право собственности.

**Параметры**:

- `self`: Экземпляр класса `TinyTool`.
- `agent`: Агент, выполняющий действие.
- `action` (dict): Словарь, представляющий действие агента.

**Возвращает**:

- `bool`: Результат выполнения действия.

**Вызывает исключения**:

- `ValueError`: Если агент не является владельцем инструмента.

**Как работает функция**:

1.  **Защита от побочных эффектов в реальном мире**:

    -   Вызывается метод `self._protect_real_world()`, который логирует предупреждение, если инструмент имеет `real_world_side_effects`.
2.  **Проверка права собственности**:

    -   Вызывается метод `self._enforce_ownership(agent)`, который проверяет, имеет ли агент право на использование инструмента. Если агент не является владельцем, вызывается исключение `ValueError`.
3.  **Обработка действия**:

    -   Вызывается метод `self._process_action(agent, action)` для фактической обработки действия. Результат этого метода возвращается как результат функции `process_action`.

**Примеры**:

```python
from tinytroupe.tools.tiny_tool import TinyTool

class Agent:
    def __init__(self, name):
        self.name = name

class MyTool(TinyTool):
    def __init__(self, name, description, owner=None, real_world_side_effects=False, exporter=None, enricher=None):
        super().__init__(name, description, owner, real_world_side_effects, exporter, enricher)

    def _process_action(self, agent, action: dict) -> bool:
        print(f"Agent {agent.name} выполнил действие: {action}")
        return True

# Создание инстанса класса MyTool
agent1 = Agent('Agent1')
agent2 = Agent('Agent2')
tool = MyTool(name='MyTool', description='A simple tool', owner=agent1)

# Пример вызова функции process_action
action = {'type': 'example_action', 'param': 'example_value'}
result = tool.process_action(agent1, action)  # Agent Agent1 выполнил действие: {'type': 'example_action', 'param': 'example_value'}
print(result)  # True

try:
    result = tool.process_action(agent2, action)  # Вызовет ValueError, так как agent2 не владеет инструментом
except ValueError as ex:
    print(ex)  # Agent Agent2 does not own tool MyTool, which is owned by Agent1.