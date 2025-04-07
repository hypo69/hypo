# Модуль `tiny_factory.py`

## Обзор

Модуль содержит базовый класс `TinyFactory`, предназначенный для создания различных типов фабрик. Он обеспечивает механизм кэширования и управления фабриками, что особенно важно для расширения системы и управления транзакциями.

## Подробней

Этот модуль играет важную роль в управлении жизненным циклом фабрик, используемых для создания агентов в системе `tinytroupe`. Он предоставляет инструменты для регистрации, хранения и кэширования фабрик, а также обеспечивает возможность восстановления их состояния. Это особенно важно для обеспечения консистентности данных при работе с кэшированными агентами.

## Классы

### `TinyFactory`

**Описание**: Базовый класс для создания различных типов фабрик. Обеспечивает механизм кэширования и управления фабриками.

**Принцип работы**:
Класс `TinyFactory` предназначен для упрощения расширения системы и управления кэшированием транзакций. Он предоставляет базовую функциональность для создания, хранения и восстановления состояния фабрик.
1.  Инициализация: При создании экземпляра `TinyFactory` генерируется уникальное имя и регистрируется фабрика в глобальном списке.
2.  Управление фабриками: Класс предоставляет статические методы для добавления, очистки и установки симуляции для фабрик.
3.  Кэширование: `TinyFactory` предоставляет методы для кодирования и декодирования полного состояния фабрики, что позволяет кэшировать фабрики и восстанавливать их состояние при необходимости.

**Атрибуты**:

*   `all_factories` (dict): Статический атрибут, представляющий собой словарь всех созданных фабрик. Ключ - имя фабрики, значение - экземпляр фабрики.
*   `name` (str): Имя фабрики, генерируется автоматически при инициализации.
*   `simulation_id` (str, optional): ID симуляции, к которой принадлежит фабрика. По умолчанию `None`.

**Методы**:

*   `__init__(simulation_id: str = None) -> None`: Инициализирует экземпляр `TinyFactory`, генерирует имя и добавляет фабрику в глобальный список.
*   `__repr__() -> str`: Возвращает строковое представление объекта `TinyFactory`.
*   `set_simulation_for_free_factories(simulation)`: Устанавливает симуляцию для фабрик, у которых `simulation_id` равен `None`.
*   `add_factory(factory)`: Добавляет фабрику в глобальный список `all_factories`.
*   `clear_factories()`: Очищает глобальный список `all_factories`.
*   `encode_complete_state() -> dict`: Кодирует полное состояние фабрики в словарь.
*   `decode_complete_state(state: dict)`: Декодирует состояние фабрики из словаря.

## Функции

### `__init__`

```python
def __init__(self, simulation_id:str=None) -> None:
    """
    Initialize a TinyFactory instance.

    Args:
        simulation_id (str, optional): The ID of the simulation. Defaults to None.
    """
    ...
```

**Назначение**: Инициализирует экземпляр класса `TinyFactory`.

**Параметры**:

*   `simulation_id` (str, optional): Идентификатор симуляции, к которой принадлежит фабрика. По умолчанию `None`.

**Возвращает**:
    - `None`

**Как работает функция**:

1.  Генерирует уникальное имя для фабрики, используя функцию `fresh_id` из модуля `tinytroupe.utils`.
2.  Присваивает переданный `simulation_id` атрибуту `simulation_id` экземпляра класса.
3.  Добавляет созданный экземпляр фабрики в глобальный список фабрик, используя статический метод `add_factory`.

**Примеры**:

```python
factory1 = TinyFactory(simulation_id="sim_123")
print(factory1.name)  # Вывод: Factory <ID>
print(factory1.simulation_id)  # Вывод: sim_123

factory2 = TinyFactory()
print(factory2.simulation_id)  # Вывод: None
```

### `__repr__`

```python
def __repr__(self):
    """
    """
    ...
```

**Назначение**: Возвращает строковое представление объекта `TinyFactory`.

**Параметры**:
    - None

**Возвращает**:

*   `str`: Строковое представление объекта `TinyFactory`.

**Как работает функция**:

1.  Формирует строку, содержащую имя класса и имя фабрики.

**Примеры**:

```python
factory = TinyFactory(simulation_id="sim_123")
print(repr(factory))  # Вывод: TinyFactory(name='Factory <ID>')
```

### `set_simulation_for_free_factories`

```python
@staticmethod
def set_simulation_for_free_factories(simulation):
    """
    Sets the simulation if it is None. This allows free environments to be captured by specific simulation scopes
    if desired.
    """
    ...
```

**Назначение**: Устанавливает симуляцию для фабрик, у которых не задан `simulation_id`.

**Параметры**:

*   `simulation`: Объект симуляции, который необходимо установить для фабрик.

**Возвращает**:
    - None

**Как работает функция**:

1.  Проходит по всем фабрикам в глобальном списке `TinyFactory.all_factories`.
2.  Для каждой фабрики проверяет, является ли `simulation_id` равным `None`.
3.  Если `simulation_id` равен `None`, вызывает метод `add_factory` объекта `simulation`, передавая текущую фабрику в качестве аргумента.

**Примеры**:

```python
class Simulation:
    def add_factory(self, factory):
        print(f"Factory {factory.name} added to simulation")

simulation = Simulation()
factory1 = TinyFactory(simulation_id="sim_123")
factory2 = TinyFactory()

TinyFactory.set_simulation_for_free_factories(simulation) # для factory2 будет выведено "Factory Factory <ID> added to simulation"
```

### `add_factory`

```python
@staticmethod
def add_factory(factory):
    """
    Adds a factory to the list of all factories. Factory names must be unique,
    so if an factory with the same name already exists, an error is raised.
    """
    ...
```

**Назначение**: Добавляет фабрику в глобальный список `all_factories`.

**Параметры**:

*   `factory`: Объект фабрики, который необходимо добавить в список.

**Возвращает**:
    - None

**Вызывает исключения**:

*   `ValueError`: Если фабрика с таким именем уже существует.

**Как работает функция**:

1.  Проверяет, существует ли фабрика с таким же именем в глобальном списке `TinyFactory.all_factories`.
2.  Если фабрика с таким именем уже существует, выбрасывает исключение `ValueError`.
3.  В противном случае добавляет фабрику в глобальный список `TinyFactory.all_factories`, где ключом является имя фабрики, а значением - объект фабрики.

**Примеры**:

```python
factory1 = TinyFactory(simulation_id="sim_123")
# TinyFactory.add_factory(factory1)  # Фабрика уже добавлена при инициализации

try:
    factory2 = TinyFactory()
    factory2.name = factory1.name
    TinyFactory.add_factory(factory2)
except ValueError as ex:
    print(f"Error: {ex}")  # Вывод: Error: Factory names must be unique, but 'Factory <ID>' is already defined.
```

### `clear_factories`

```python
@staticmethod
def clear_factories():
    """
    Clears the global list of all factories.
    """
    ...
```

**Назначение**: Очищает глобальный список `all_factories`.

**Параметры**:
    - None

**Возвращает**:
    - None

**Как работает функция**:

1.  Присваивает глобальному списку `TinyFactory.all_factories` пустой словарь, тем самым удаляя все фабрики из списка.

**Примеры**:

```python
factory1 = TinyFactory(simulation_id="sim_123")
print(len(TinyFactory.all_factories))  # Вывод: 1

TinyFactory.clear_factories()
print(len(TinyFactory.all_factories))  # Вывод: 0
```

### `encode_complete_state`

```python
def encode_complete_state(self) -> dict:
    """
    Encodes the complete state of the factory. If subclasses have elmements that are not serializable, they should override this method.
    """
    ...
```

**Назначение**: Кодирует полное состояние фабрики в словарь.

**Параметры**:
    - None

**Возвращает**:

*   `dict`: Словарь, представляющий состояние фабрики.

**Как работает функция**:

1.  Создает глубокую копию словаря `__dict__` экземпляра класса, который содержит все атрибуты экземпляра.
2.  Возвращает созданную копию.

**Примеры**:

```python
factory = TinyFactory(simulation_id="sim_123")
state = factory.encode_complete_state()
print(state.keys())  # Вывод: dict_keys(['name', 'simulation_id'])
```

### `decode_complete_state`

```python
def decode_complete_state(self, state:dict):
    """
    Decodes the complete state of the factory. If subclasses have elmements that are not serializable, they should override this method.
    """
    ...
```

**Назначение**: Декодирует состояние фабрики из словаря.

**Параметры**:

*   `state` (dict): Словарь, содержащий состояние фабрики.

**Возвращает**:
    - self

**Как работает функция**:

1.  Создает глубокую копию переданного словаря `state`.
2.  Обновляет словарь `__dict__` экземпляра класса данными из копии словаря `state`.
3.  Возвращает экземпляр класса.

**Примеры**:

```python
factory = TinyFactory(simulation_id="sim_123")
state = {"name": "New Factory", "simulation_id": "sim_456"}
factory.decode_complete_state(state)
print(factory.name)  # Вывод: New Factory
print(factory.simulation_id)  # Вывод: sim_456
```