# Модуль `misc`

## Обзор

Модуль содержит различные утилиты, такие как функции для получения имени агента или мира, вычисления хеша, генерации уникальных ID и сброса счетчика ID.

## Подробней

Модуль `misc` предоставляет набор вспомогательных функций, используемых в проекте `hypotez` для различных целей, включая обработку имен агентов, вычисление хешей объектов и генерацию уникальных идентификаторов. Эти функции обеспечивают удобные инструменты для работы с данными и управления состоянием в проекте.

## Функции

### `name_or_empty`

```python
def name_or_empty(named_entity: AgentOrWorld) -> str:
    """
    Returns the name of the specified agent or environment, or an empty string if the agent is None.
    """
    ...
```

**Назначение**: Возвращает имя указанного агента или окружения, или пустую строку, если агент `None`.

**Параметры**:
- `named_entity` (AgentOrWorld): Агент или окружение, имя которого нужно получить.

**Возвращает**:
- `str`: Имя агента или окружения, или пустая строка, если `named_entity` равен `None`.

**Как работает функция**:

1. Проверяет, является ли `named_entity` равным `None`.
2. Если `named_entity` равен `None`, возвращает пустую строку.
3. В противном случае возвращает атрибут `name` объекта `named_entity`.

```
Проверка на None --> Возврат пустой строки
       |
       Нет
       |
Возврат имени объекта
```

**Примеры**:

```python
class MockAgent:
    def __init__(self, name: str):
        self.name = name

agent = MockAgent("TestAgent")
empty_agent = None

print(name_or_empty(agent))
print(name_or_empty(empty_agent))
```

### `custom_hash`

```python
def custom_hash(obj) -> str:
    """
    Returns a hash for the specified object. The object is first converted
    to a string, to make it hashable. This method is deterministic,
    contrary to the built-in hash() function.
    """
    ...
```

**Назначение**: Возвращает хеш для указанного объекта. Объект сначала преобразуется в строку, чтобы сделать его хешируемым. Этот метод является детерминированным, в отличие от встроенной функции `hash()`.

**Параметры**:
- `obj` (any): Объект, для которого нужно вычислить хеш.

**Возвращает**:
- `str`: Хеш объекта в виде шестнадцатеричной строки.

**Как работает функция**:

1. Преобразует объект `obj` в строку с помощью `str(obj)`.
2. Кодирует строку в байты с использованием кодировки UTF-8.
3. Вычисляет SHA-256 хеш байтовой строки с помощью `hashlib.sha256()`.
4. Возвращает шестнадцатеричное представление хеша с помощью `hexdigest()`.

```
Преобразование объекта в строку --> Кодирование строки в байты --> Вычисление SHA-256 хеша --> Возврат шестнадцатеричного представления хеша
```

**Примеры**:

```python
print(custom_hash("test"))
print(custom_hash(123))
print(custom_hash({"a": 1, "b": 2}))
```

### `fresh_id`

```python
def fresh_id() -> int:
    """
    Returns a fresh ID for a new object. This is useful for generating unique IDs for objects.
    """
    ...
```

**Назначение**: Возвращает новый уникальный ID для нового объекта. Это полезно для генерации уникальных ID для объектов.

**Возвращает**:
- `int`: Новый уникальный ID.

**Как работает функция**:

1. Объявляет глобальную переменную `_fresh_id_counter`.
2. Увеличивает значение `_fresh_id_counter` на 1.
3. Возвращает новое значение `_fresh_id_counter`.

```
Увеличение счетчика --> Возврат нового ID
```

**Примеры**:

```python
print(fresh_id())
print(fresh_id())
print(fresh_id())
```

### `reset_fresh_id`

```python
def reset_fresh_id() -> None:
    """
    Resets the fresh ID counter. This is useful for testing purposes.
    """
    ...
```

**Назначение**: Сбрасывает счетчик новых ID. Это полезно для целей тестирования.

**Как работает функция**:

1. Объявляет глобальную переменную `_fresh_id_counter`.
2. Устанавливает значение `_fresh_id_counter` в 0.

```
Установка счетчика в 0
```

**Примеры**:

```python
print(fresh_id())
reset_fresh_id()
print(fresh_id())