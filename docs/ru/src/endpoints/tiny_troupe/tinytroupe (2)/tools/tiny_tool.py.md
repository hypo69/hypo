# Модуль `tiny_tool.py`

## Обзор

Модуль содержит абстрактный класс `TinyTool`, предназначенный для создания инструментов, используемых агентами в системе Tiny Troupe. Он определяет базовую структуру и методы, которые должны быть реализованы в подклассах для выполнения конкретных действий. Класс также обеспечивает механизмы для управления правами собственности на инструменты и защиты от нежелательных побочных эффектов в реальном мире.

## Подробней

Этот модуль предоставляет основу для создания специализированных инструментов, которые могут быть использованы в различных сценариях, где требуется автоматизация или выполнение определенных задач. Инструменты могут быть настроены для работы с экспортерами и обогатителями данных, что позволяет гибко настраивать процесс обработки и анализа информации.

## Классы

### `TinyTool`

**Описание**: Абстрактный класс, представляющий собой базовый инструмент в системе Tiny Troupe.

**Принцип работы**: Класс `TinyTool` предоставляет общую структуру для инструментов, используемых агентами. Он включает методы для инициализации инструмента, обработки действий, защиты от побочных эффектов и принудительного применения прав собственности. Подклассы должны реализовывать методы `_process_action`, `actions_definitions_prompt` и `actions_constraints_prompt`.

**Наследует**:
- `JsonSerializableRegistry`: Обеспечивает возможность сериализации и десериализации экземпляров класса в формат JSON.

**Аттрибуты**:
- `name` (str): Имя инструмента.
- `description` (str): Краткое описание инструмента.
- `owner` (str | None): Агент, владеющий инструментом. Если `None`, инструмент может использоваться любым агентом.
- `real_world_side_effects` (bool): Указывает, имеет ли инструмент побочные эффекты в реальном мире.
- `exporter` (ArtifactExporter | None): Экспортер для экспорта результатов действий инструмента.
- `enricher` (Enricher | None): Обогатитель для обогащения результатов действий инструмента.

**Методы**:
- `__init__(name, description, owner, real_world_side_effects, exporter, enricher)`: Инициализирует новый инструмент.
- `_process_action(agent, action)`: Абстрактный метод, который должен быть реализован в подклассах для выполнения конкретного действия.
- `_protect_real_world()`: Выводит предупреждение в лог, если инструмент имеет побочные эффекты в реальном мире.
- `_enforce_ownership(agent)`: Проверяет, имеет ли агент право собственности на инструмент.
- `set_owner(owner)`: Устанавливает владельца инструмента.
- `actions_definitions_prompt()`: Абстрактный метод, который должен быть реализован в подклассах для определения подсказок для действий.
- `actions_constraints_prompt()`: Абстрактный метод, который должен быть реализован в подклассах для определения ограничений для действий.
- `process_action(agent, action)`: Обрабатывает действие, выполняя защиту от побочных эффектов и принудительное применение прав собственности.

## Функции

### `__init__`

```python
def __init__(self, name: str, description: str, owner: str | None = None, real_world_side_effects: bool = False, exporter = None, enricher = None) -> None:
    """
    Initialize a new tool.

    Args:
        name (str): The name of the tool.
        description (str): A brief description of the tool.
        owner (str | None, optional): The agent that owns the tool. If None, the tool can be used by anyone. Defaults to None.
        real_world_side_effects (bool, optional): Whether the tool has real-world side effects. Defaults to False.
        exporter (ArtifactExporter | None, optional): An exporter that can be used to export the results of the tool's actions. Defaults to None.
        enricher (Enricher | None, optional): An enricher that can be used to enrich the results of the tool's actions. Defaults to None.

    """
```

**Назначение**: Инициализация экземпляра класса `TinyTool`.

**Параметры**:
- `name` (str): Имя инструмента.
- `description` (str): Краткое описание инструмента.
- `owner` (str | None, optional): Агент, владеющий инструментом. Если `None`, инструмент может использоваться любым агентом. По умолчанию `None`.
- `real_world_side_effects` (bool, optional): Указывает, имеет ли инструмент побочные эффекты в реальном мире. По умолчанию `False`.
- `exporter` (ArtifactExporter | None, optional): Экспортер для экспорта результатов действий инструмента. По умолчанию `None`.
- `enricher` (Enricher | None, optional): Обогатитель для обогащения результатов действий инструмента. По умолчанию `None`.

**Как работает функция**:
1. Присваивает переданные значения атрибутам экземпляра класса, таким как `name`, `description`, `owner`, `real_world_side_effects`, `exporter` и `enricher`.

```
Инициализация
↓
Присвоение имени инструменту
↓
Присвоение описания инструменту
↓
Присвоение владельца инструменту
↓
Присвоение флага побочных эффектов
↓
Присвоение экспортера
↓
Присвоение обогатителя
```

**Примеры**:
```python
from tinytroupe.tools.tiny_tool import TinyTool

# Пример создания экземпляра TinyTool
tool = TinyTool(name="ExampleTool", description="A simple example tool")
print(tool.name, tool.description)  # Вывод: ExampleTool A simple example tool

# Пример создания экземпляра TinyTool с владельцем
tool_with_owner = TinyTool(name="RestrictedTool", description="A tool with restricted access", owner="AgentSmith")
print(tool_with_owner.owner)  # Вывод: AgentSmith
```

### `_process_action`

```python
def _process_action(self, agent, action: dict) -> bool:
    """
    _process_action.
    """
    raise NotImplementedError("Subclasses must implement this method.")
```

**Назначение**: Абстрактный метод, предназначенный для обработки действий, выполняемых агентом с использованием инструмента.

**Параметры**:
- `agent`: Агент, выполняющий действие.
- `action` (dict): Словарь, содержащий информацию о действии.

**Возвращает**:
- `bool`: Результат выполнения действия.

**Вызывает исключения**:
- `NotImplementedError`: Вызывается, если метод не реализован в подклассе.

**Как работает функция**:
1. Вызывает исключение `NotImplementedError`, указывающее на необходимость реализации метода в подклассах.

```
Вызов метода
↓
Выброс исключения NotImplementedError
```

**Примеры**:
Поскольку это абстрактный метод, пример его использования можно увидеть только в подклассах `TinyTool`.

### `_protect_real_world`

```python
def _protect_real_world(self) -> None:
    """
    _protect_real_world.
    """
    if self.real_world_side_effects:
        logger.warning(f" !!!!!!!!!! Tool {self.name} has REAL-WORLD SIDE EFFECTS. This is NOT just a simulation. Use with caution. !!!!!!!!!!")
```

**Назначение**: Метод для защиты от нежелательных побочных эффектов в реальном мире, связанных с использованием инструмента.

**Как работает функция**:
1. Проверяет, установлен ли флаг `real_world_side_effects` в `True`.
2. Если флаг установлен, выводит предупреждение в лог с использованием модуля `logger` из `tinytroupe.tools`.

```
Проверка флага real_world_side_effects
↓
Вывод предупреждения в лог (если флаг True)
```

**Примеры**:
```python
from tinytroupe.tools.tiny_tool import TinyTool
from tinytroupe.tools import logger  # Импортируем logger

# Создаем инструмент с real_world_side_effects=True
tool = TinyTool(name="DangerousTool", description="A tool with real-world side effects", real_world_side_effects=True)

# Вызываем метод _protect_real_world
tool._protect_real_world()  # Выведет предупреждение в лог
```

### `_enforce_ownership`

```python
def _enforce_ownership(self, agent) -> None:
    """
    _enforce_ownership.
    """
    if self.owner is not None and agent.name != self.owner.name:
        raise ValueError(f"Agent {agent.name} does not own tool {self.name}, which is owned by {self.owner.name}.")
```

**Назначение**: Метод для принудительного применения прав собственности на инструмент.

**Параметры**:
- `agent`: Агент, пытающийся использовать инструмент.

**Вызывает исключения**:
- `ValueError`: Вызывается, если агент не является владельцем инструмента.

**Как работает функция**:
1. Проверяет, установлен ли владелец инструмента (`self.owner`).
2. Если владелец установлен, проверяет, совпадает ли имя агента с именем владельца.
3. Если имена не совпадают, вызывает исключение `ValueError` с сообщением о нарушении прав собственности.

```
Проверка наличия владельца
↓
Сравнение имени агента и владельца
↓
Выброс исключения ValueError (если имена не совпадают)
```

**Примеры**:
```python
from tinytroupe.tools.tiny_tool import TinyTool

class Agent:
    def __init__(self, name):
        self.name = name

# Создаем инструмент с владельцем
tool = TinyTool(name="RestrictedTool", description="A tool with restricted access", owner=Agent(name="AgentSmith"))

# Создаем агентов
agent1 = Agent(name="AgentSmith")
agent2 = Agent(name="AgentJones")

# Проверяем право собственности
tool._enforce_ownership(agent1)  # Не вызовет исключение
try:
    tool._enforce_ownership(agent2)  # Вызовет исключение ValueError
except ValueError as ex:
    print(ex)  # Agent Jones does not own tool RestrictedTool, which is owned by AgentSmith.
```

### `set_owner`

```python
def set_owner(self, owner) -> None:
    """
    set_owner.
    """
    self.owner = owner
```

**Назначение**: Метод для установки владельца инструмента.

**Параметры**:
- `owner`: Новый владелец инструмента.

**Как работает функция**:
1. Присваивает переданное значение атрибуту `owner` экземпляра класса.

```
Присвоение владельца инструменту
```

**Примеры**:
```python
from tinytroupe.tools.tiny_tool import TinyTool

class Agent:
    def __init__(self, name):
        self.name = name

# Создаем инструмент без владельца
tool = TinyTool(name="ExampleTool", description="A simple example tool")
print(tool.owner)  # Вывод: None

# Устанавливаем владельца
agent = Agent(name="AgentSmith")
tool.set_owner(agent)
print(tool.owner.name)  # Вывод: AgentSmith
```

### `actions_definitions_prompt`

```python
def actions_definitions_prompt(self) -> str:
    """
    actions_definitions_prompt.
    """
    raise NotImplementedError("Subclasses must implement this method.")
```

**Назначение**: Абстрактный метод, предназначенный для определения подсказок для действий, которые могут быть выполнены с использованием инструмента.

**Возвращает**:
- `str`: Строка, содержащая подсказки для действий.

**Вызывает исключения**:
- `NotImplementedError`: Вызывается, если метод не реализован в подклассе.

**Как работает функция**:
1. Вызывает исключение `NotImplementedError`, указывающее на необходимость реализации метода в подклассах.

```
Вызов метода
↓
Выброс исключения NotImplementedError
```

**Примеры**:
Поскольку это абстрактный метод, пример его использования можно увидеть только в подклассах `TinyTool`.

### `actions_constraints_prompt`

```python
def actions_constraints_prompt(self) -> str:
    """
    actions_constraints_prompt.
    """
    raise NotImplementedError("Subclasses must implement this method.")
```

**Назначение**: Абстрактный метод, предназначенный для определения ограничений для действий, которые могут быть выполнены с использованием инструмента.

**Возвращает**:
- `str`: Строка, содержащая ограничения для действий.

**Вызывает исключения**:
- `NotImplementedError`: Вызывается, если метод не реализован в подклассе.

**Как работает функция**:
1. Вызывает исключение `NotImplementedError`, указывающее на необходимость реализации метода в подклассах.

```
Вызов метода
↓
Выброс исключения NotImplementedError
```

**Примеры**:
Поскольку это абстрактный метод, пример его использования можно увидеть только в подклассах `TinyTool`.

### `process_action`

```python
def process_action(self, agent, action: dict) -> bool:
    """
    process_action.
    """
    self._protect_real_world()
    self._enforce_ownership(agent)
    self._process_action(agent, action)
```

**Назначение**: Метод для обработки действия, выполняемого агентом с использованием инструмента.

**Параметры**:
- `agent`: Агент, выполняющий действие.
- `action` (dict): Словарь, содержащий информацию о действии.

**Как работает функция**:
1. Вызывает метод `_protect_real_world` для защиты от побочных эффектов в реальном мире.
2. Вызывает метод `_enforce_ownership` для принудительного применения прав собственности на инструмент.
3. Вызывает метод `_process_action` для выполнения конкретного действия.

```
Вызов метода _protect_real_world
↓
Вызов метода _enforce_ownership
↓
Вызов метода _process_action
```

**Примеры**:
```python
from tinytroupe.tools.tiny_tool import TinyTool

class Agent:
    def __init__(self, name):
        self.name = name

class ExampleTool(TinyTool):
    def __init__(self, name, description, owner=None, real_world_side_effects=False, exporter=None, enricher=None):
        super().__init__(name, description, owner, real_world_side_effects, exporter, enricher)

    def _process_action(self, agent, action: dict) -> bool:
        print(f"Agent {agent.name} is performing action: {action}")
        return True

    def actions_definitions_prompt(self) -> str:
        return "Example action definitions"

    def actions_constraints_prompt(self) -> str:
        return "Example action constraints"

# Создаем инструмент и агента
tool = ExampleTool(name="ExampleTool", description="A simple example tool")
agent = Agent(name="AgentSmith")

# Выполняем действие
action = {"name": "example_action", "parameters": {"param1": "value1"}}
tool.process_action(agent, action)  # Agent AgentSmith is performing action: {'name': 'example_action', 'parameters': {'param1': 'value1'}}