# Модуль для работы с JSON и регистрацией классов
=================================================

Модуль предоставляет класс `JsonSerializableRegistry`, который обеспечивает JSON сериализацию, десериализацию и регистрацию подклассов. Также содержит функции для слияния словарей и удаления дубликатов из списков.

## Оглавление

- [Обзор](#обзор)
- [Классы](#классы)
    - [JsonSerializableRegistry](#jsonserializableregistry)
- [Функции](#функции)
    - [post_init](#post_init)
    - [merge_dicts](#merge_dicts)
    - [remove_duplicates](#remove_duplicates)
- [Подробнее](#подробнее)

## Обзор

Этот модуль предоставляет инструменты для работы с JSON-сериализацией и десериализацией объектов, а также для регистрации подклассов, что позволяет упростить процесс сохранения и восстановления объектов из JSON-формата. Кроме того, модуль включает функции для работы со словарями и списками, такие как слияние словарей и удаление дубликатов.

## Подробнее

Модуль `json.py` предназначен для облегчения работы с JSON-сериализацией и десериализацией объектов в проекте `hypotez`. Он предоставляет класс `JsonSerializableRegistry`, который может быть использован в качестве миксина для классов, требующих JSON-сериализации. Класс автоматически регистрирует подклассы и предоставляет методы для преобразования объектов в JSON и обратно.

Модуль также содержит вспомогательные функции для работы со словарями и списками, которые могут быть полезны при обработке данных в проекте.

## Классы

### `JsonSerializableRegistry`

**Описание**:
Миксин-класс, предоставляющий функциональность JSON-сериализации, десериализации и регистрации подклассов.

**Принцип работы**:
Класс использует атрибут `class_mapping` для хранения соответствия между именами классов и самими классами. Методы `to_json` и `from_json` обеспечивают сериализацию и десериализацию объектов соответственно. При наследовании класса, подклассы автоматически регистрируются, что позволяет создавать экземпляры классов из JSON, зная только их имена.

**Аттрибуты**:
- `class_mapping (dict)`: Словарь, содержащий соответствия между именами классов и классами.

**Методы**:
- `to_json(self, include: list = None, suppress: list = None, file_path: str = None, serialization_type_field_name: str = "json_serializable_class_name") -> dict`:
    Возвращает JSON-представление объекта.
- `from_json(cls, json_dict_or_path: dict | str, suppress: list = None, serialization_type_field_name: str = "json_serializable_class_name", post_init_params: dict = None)`:
    Загружает JSON-представление объекта и создает экземпляр класса.
- `__init_subclass__(cls, **kwargs)`:
    Регистрирует подкласс при наследовании.
- `_post_deserialization_init(self, **kwargs)`:
    Вызывает метод `_post_init` после десериализации, если он существует.
- `_programmatic_name_to_json_name(cls, name: str) -> str`:
    Конвертирует имя атрибута из программного в JSON-совместимый формат.
- `_json_name_to_programmatic_name(cls, name: str) -> str`:
    Конвертирует имя атрибута из JSON-совместимого формата в программный.

#### `to_json`

```python
def to_json(self, include: list = None, suppress: list = None, file_path: str = None,
                serialization_type_field_name = "json_serializable_class_name") -> dict:
    """
    Args:
        include (list, optional): Атрибуты, которые нужно включить в сериализацию. Переопределяет поведение по умолчанию.
        suppress (list, optional): Атрибуты, которые нужно исключить из сериализации. Переопределяет поведение по умолчанию.
        file_path (str, optional): Путь к файлу, куда будет записан JSON.
        serialization_type_field_name (str, optional): Имя поля, содержащего имя класса при сериализации. По умолчанию "json_serializable_class_name".

    Returns:
        dict: JSON-представление объекта.

    Как работает функция:
        1. Собирает все сериализуемые атрибуты из иерархии классов.
        2. Переопределяет атрибуты с параметрами метода, если они предоставлены.
        3. Создает словарь с именем класса и сериализованными атрибутами.
        4. Если указан `file_path`, записывает результат в файл.

    """
```

**Примеры**:
```python
class MyClass(JsonSerializableRegistry):
    serializable_attributes = ['attr1', 'attr2']
    def __init__(self, attr1: str, attr2: int):
        self.attr1 = attr1
        self.attr2 = attr2

instance = MyClass('value1', 123)
json_data = instance.to_json()
print(json_data)
# {'json_serializable_class_name': 'MyClass', 'attr1': 'value1', 'attr2': 123}

json_data = instance.to_json(file_path='example.json') # Объект будет записан в файл example.json
```

#### `from_json`

```python
@classmethod
def from_json(cls, json_dict_or_path, suppress: list = None, 
              serialization_type_field_name = "json_serializable_class_name", 
              post_init_params: dict = None):
    """
    Args:
        json_dict_or_path (dict or str): JSON-словарь, представляющий объект, или путь к файлу, из которого нужно загрузить JSON.
        suppress (list, optional): Атрибуты, которые нужно исключить из загрузки.
        serialization_type_field_name (str, optional): Имя поля, содержащего имя класса при сериализации. По умолчанию "json_serializable_class_name".
        post_init_params (dict, optional): Параметры для передачи в метод `_post_deserialization_init`.

    Returns:
        An instance of the class populated with the data from json_dict_or_path.

    Как работает функция:
        1. Загружает JSON из словаря или файла.
        2. Определяет класс объекта из JSON.
        3. Создает экземпляр класса без вызова `__init__`.
        4. Назначает значения атрибутам экземпляра из JSON.
        5. Вызывает метод `_post_deserialization_init`, если он существует.

    """
```

**Примеры**:

```python
class MyClass(JsonSerializableRegistry):
    serializable_attributes = ['attr1', 'attr2']
    def __init__(self, attr1: str, attr2: int):
        self.attr1 = attr1
        self.attr2 = attr2

json_data = {'json_serializable_class_name': 'MyClass', 'attr1': 'value1', 'attr2': 123}
instance = MyClass.from_json(json_data)
print(instance.attr1, instance.attr2)
# value1 123

instance = MyClass.from_json('example.json') # Объект будет создан из файла example.json
```

#### `__init_subclass__`

```python
def __init_subclass__(cls, **kwargs):
    """
    Args:
        kwargs (dict): Дополнительные аргументы, переданные при наследовании класса.

    Как работает функция:
        1. Регистрирует подкласс в `class_mapping`.
        2. Автоматически расширяет `serializable_attributes` и `custom_serialization_initializers` из родительских классов.

    """
```

#### `_post_deserialization_init`

```python
def _post_deserialization_init(self, **kwargs):
    """
    Args:
        kwargs (dict): Дополнительные аргументы, переданные при десериализации.

    Как работает функция:
        1. Вызывает метод `_post_init`, если он существует.

    """
```

#### `_programmatic_name_to_json_name`

```python
@classmethod
def _programmatic_name_to_json_name(cls, name: str) -> str:
    """
    Args:
        name (str): Имя атрибута в программном коде.

    Returns:
        str: Имя атрибута в JSON-формате.

    Как работает функция:
        1. Конвертирует имя атрибута из программного в JSON-совместимый формат (snake_case).

    """
```

#### `_json_name_to_programmatic_name`

```python
@classmethod
def _json_name_to_programmatic_name(cls, name: str) -> str:
    """
    Args:
        name (str): Имя атрибута в JSON-формате.

    Returns:
        str: Имя атрибута в программном коде.

    Как работает функция:
        1. Конвертирует имя атрибута из JSON-совместимого формата в программный.

    """
```

## Функции

### `post_init`

```python
def post_init(cls):
    """
    Args:
        cls (class): Класс, к которому применяется декоратор.

    Returns:
        class: Модифицированный класс с добавленным вызовом `_post_init` после инициализации.

    Как работает функция:
        1. Декоратор для принудительного вызова метода `_post_init` в классе после инициализации.
        2. Заменяет оригинальный метод `__init__` новым, который вызывает `_post_init` после инициализации.

    """
```

### `merge_dicts`

```python
def merge_dicts(current: dict, additions: dict, overwrite: bool = False, error_on_conflict: bool = True) -> dict:
    """
    Args:
        current (dict): Оригинальный словарь.
        additions (dict): Словарь с добавляемыми значениями.
        overwrite (bool, optional): Флаг, указывающий, нужно ли перезаписывать значения, если они имеют одинаковый тип, но не являются списками или словарями. По умолчанию `False`.
        error_on_conflict (bool, optional): Флаг, указывающий, нужно ли вызывать исключение при конфликте, если `overwrite` установлен в `False`. По умолчанию `True`.

    Returns:
        dict: Новый словарь с объединенными значениями.

    Raises:
        TypeError: Если значения имеют разные типы.
        ValueError: Если возникает конфликт и `overwrite` установлен в `False`.

    Как работает функция:
        1. Создает копию оригинального словаря.
        2. Итерируется по добавляемому словарю.
        3. Если ключ существует в обоих словарях и значения являются словарями, рекурсивно вызывает `merge_dicts`.
        4. Если ключ существует в обоих словарях и значения являются списками, объединяет списки и удаляет дубликаты.
        5. Если ключ существует в обоих словарях и значения имеют разные типы, вызывает исключение.
        6. Если ключ существует в обоих словарях и значения имеют одинаковый тип, но не являются списками или словарями, перезаписывает значение, если `overwrite` установлен в `True`.
        7. Если ключ не существует в оригинальном словаре, добавляет его из добавляемого словаря.

    """
```

**ASCII flowchart**:

```
     Начало
     │
     Создание копии `current`
     │
     Начало цикла по ключам `additions`
     │
     Ключ в `merged`?
     ├─Да─► Значение в `merged` `None`?
     │   ├─Да─► Присвоение значения из `additions`
     │   └─Нет─► Значения - словари?
     │       ├─Да─► Рекурсивный вызов `merge_dicts`
     │       └─Нет─► Значения - списки?
     │           ├─Да─► Объединение списков и удаление дубликатов
     │           └─Нет─► Типы значений разные?
     │               ├─Да─► Вызов `TypeError`
     │               └─Нет─► `overwrite` `True`?
     │                   ├─Да─► Перезапись значения
     │                   └─Нет─► Значения разные?
     │                       ├─Да─► `error_on_conflict` `True`?
     │                       │   ├─Да─► Вызов `ValueError`
     │                       │   └─Нет─► Пропуск
     │                       └─Нет─► Пропуск
     └─Нет─► Добавление ключа и значения из `additions`
     │
     Конец цикла
     │
     Возврат `merged`
     │
     Конец
```

**Примеры**:

```python
dict1 = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': [1, 2, 3]}
dict2 = {'a': 4, 'b': {'c': 5, 'f': 6}, 'e': [4, 5, 6], 'g': 7}

merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)
# {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': [1, 2, 3], 'g': 7}

merged_dict = merge_dicts(dict1, dict2, overwrite=True)
print(merged_dict)
# {'a': 4, 'b': {'c': 5, 'd': 3, 'f': 6}, 'e': [1, 2, 3, 4, 5, 6], 'g': 7}
```

### `remove_duplicates`

```python
def remove_duplicates(lst: list) -> list:
    """
    Args:
        lst (list): Список, из которого нужно удалить дубликаты.

    Returns:
        list: Новый список с удаленными дубликатами.

    Как работает функция:
        1. Удаляет дубликаты из списка, сохраняя порядок элементов.
        2. Использует список `seen` для отслеживания уже виденных элементов.
        3. Преобразует словари в `frozenset` для возможности хеширования.

    """
```

**Примеры**:

```python
list1 = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(list1)
print(unique_list)
# [1, 2, 3, 4, 5]

list2 = [{'a': 1}, {'a': 2}, {'a': 1}]
unique_list = remove_duplicates(list2)
print(unique_list)
# [{'a': 1}, {'a': 2}]
```