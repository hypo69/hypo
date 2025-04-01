# Модуль tiny_factory.py

## Обзор

Модуль `tiny_factory.py` определяет базовый класс `TinyFactory` для создания различных типов фабрик в проекте `hypotez`. Этот класс облегчает расширение системы, особенно в отношении кеширования транзакций. Фабрики используются для создания и управления объектами в симуляциях.

## Подробней

Модуль содержит класс `TinyFactory`, который служит базовым классом для создания различных типов фабрик. Он предоставляет функциональность для управления фабриками, включая добавление, удаление и кеширование. Фабрики играют важную роль в создании объектов в симуляциях и управлении их состоянием. Класс также содержит методы для кодирования и декодирования состояния фабрики, что необходимо для кеширования транзакций.

## Классы

### `TinyFactory`

**Описание**: Базовый класс для создания различных типов фабрик.

**Принцип работы**: Класс `TinyFactory` предоставляет базовую функциональность для управления фабриками. Он включает методы для добавления, удаления и кеширования фабрик. Класс также содержит методы для кодирования и декодирования состояния фабрики, что необходимо для кеширования транзакций.

**Аттрибуты**:
- `all_factories (dict)`: Словарь всех созданных фабрик. Ключ - имя фабрики, значение - объект фабрики.
- `name (str)`: Имя фабрики. Генерируется автоматически при создании экземпляра класса.
- `simulation_id (str, optional)`: ID симуляции, к которой принадлежит фабрика. По умолчанию `None`.

**Методы**:
- `__init__(simulation_id: str = None) -> None`: Инициализирует экземпляр класса `TinyFactory`.
- `__repr__() -> str`: Возвращает строковое представление объекта `TinyFactory`.
- `set_simulation_for_free_factories(simulation)`: Устанавливает симуляцию для свободных фабрик (с `simulation_id=None`).
- `add_factory(factory)`: Добавляет фабрику в глобальный список фабрик.
- `clear_factories()`: Очищает глобальный список всех фабрик.
- `encode_complete_state() -> dict`: Кодирует полное состояние фабрики в словарь.
- `decode_complete_state(state: dict)`: Декодирует состояние фабрики из словаря.

### `__init__`

```python
def __init__(self, simulation_id: str = None) -> None:
    """
    Initialize a TinyFactory instance.

    Args:
        simulation_id (str, optional): The ID of the simulation. Defaults to None.
    """
    ...
```

**Назначение**: Инициализирует новый экземпляр класса `TinyFactory`.

**Параметры**:
- `simulation_id (str, optional)`: ID симуляции, к которой принадлежит фабрика. По умолчанию `None`.

**Возвращает**:
- `None`

**Как работает функция**:
1. Генерирует уникальное имя для фабрики с использованием `utils.fresh_id()` и устанавливает его в атрибут `self.name`.
2. Устанавливает `simulation_id` фабрики.
3. Добавляет фабрику в глобальный список фабрик, используя `TinyFactory.add_factory(self)`.

```
Создание уникального имени фабрики --> Установка simulation_id --> Добавление фабрики в глобальный список
```

**Примеры**:

```python
factory = TinyFactory()
print(factory.name)  # Пример: Factory 123
```

### `__repr__`

```python
def __repr__(self) -> str:
    """
    """
    ...
```

**Назначение**: Возвращает строковое представление объекта `TinyFactory`.

**Параметры**:
- Нет

**Возвращает**:
- `str`: Строковое представление объекта `TinyFactory`.

**Как работает функция**:
1. Формирует строку, представляющую объект `TinyFactory` с его именем.

**Примеры**:

```python
factory = TinyFactory()
print(repr(factory))  # Пример: TinyFactory(name='Factory 123')
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

**Назначение**: Устанавливает симуляцию для "свободных" фабрик, у которых `simulation_id` равен `None`.

**Параметры**:
- `simulation`: Объект симуляции, к которой нужно привязать фабрики.

**Возвращает**:
- `None`

**Как работает функция**:
1. Итерируется по всем фабрикам в `TinyFactory.all_factories`.
2. Если у фабрики `simulation_id` равен `None`, добавляет фабрику в указанную симуляцию с помощью `simulation.add_factory(factory)`.

```
Итерация по фабрикам --> Проверка simulation_id --> Добавление фабрики в симуляцию
```

**Примеры**:

```python
from unittest.mock import Mock
simulation = Mock()  # Создаем мок-объект симуляции
factory1 = TinyFactory()  # simulation_id по умолчанию None
factory2 = TinyFactory(simulation_id="sim1")
TinyFactory.set_simulation_for_free_factories(simulation)
simulation.add_factory.assert_called_once_with(factory1)  # Проверяем, что add_factory был вызван только для factory1
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
- `factory`: Объект фабрики для добавления.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `ValueError`: Если фабрика с таким именем уже существует.

**Как работает функция**:
1. Проверяет, существует ли уже фабрика с таким же именем в `TinyFactory.all_factories`.
2. Если фабрика с таким именем уже существует, выбрасывает исключение `ValueError`.
3. Если фабрики с таким именем не существует, добавляет фабрику в `TinyFactory.all_factories`.

```
Проверка имени фабрики --> Выброс исключения (если имя занято) --> Добавление фабрики в глобальный список
```

**Примеры**:

```python
factory1 = TinyFactory()
TinyFactory.add_factory(factory1)

try:
    factory2 = TinyFactory()  # Создаст фабрику с тем же именем, если id генерируется не уникально
    factory2.name = factory1.name
    TinyFactory.add_factory(factory2)
except ValueError as ex:
    print(f"Ошибка: {ex}")
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

**Назначение**: Очищает глобальный список всех фабрик (`TinyFactory.all_factories`).

**Параметры**:
- Нет

**Возвращает**:
- `None`

**Как работает функция**:
1. Присваивает `TinyFactory.all_factories` пустой словарь.

**Примеры**:

```python
factory1 = TinyFactory()
TinyFactory.add_factory(factory1)
TinyFactory.clear_factories()
print(TinyFactory.all_factories)  # {}
```

### `encode_complete_state`

```python
def encode_complete_state(self) -> dict:
    """
    Encodes the complete state of the factory. If subclasses have elmements that are not serializable, they should override this method.
    """
    ...
```

**Назначение**: Кодирует полное состояние фабрики в словарь для кеширования.

**Параметры**:
- Нет

**Возвращает**:
- `dict`: Словарь, представляющий состояние фабрики.

**Как работает функция**:
1. Создает глубокую копию словаря `self.__dict__`, представляющего состояние объекта.
2. Возвращает эту копию.

```
Создание глубокой копии состояния --> Возврат словаря состояния
```

**Примеры**:

```python
factory = TinyFactory()
state = factory.encode_complete_state()
print(state)
```

### `decode_complete_state`

```python
def decode_complete_state(self, state: dict):
    """
    Decodes the complete state of the factory. If subclasses have elmements that are not serializable, they should override this method.
    """
    ...
```

**Назначение**: Декодирует состояние фабрики из словаря, восстанавливая её состояние.

**Параметры**:
- `state (dict)`: Словарь, содержащий состояние фабрики.

**Возвращает**:
- `self`: Объект `TinyFactory` с восстановленным состоянием.

**Как работает функция**:
1. Создает глубокую копию словаря `state`.
2. Обновляет словарь `self.__dict__` данными из скопированного словаря `state`.
3. Возвращает `self`.

```
Создание глубокой копии состояния --> Обновление состояния объекта --> Возврат объекта
```

**Примеры**:

```python
factory = TinyFactory()
state = {'name': 'Factory123', 'simulation_id': 'sim1'}
factory.decode_complete_state(state)
print(factory.name, factory.simulation_id)  # Factory123 sim1