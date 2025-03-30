# Модуль `ns`

## Обзор

Модуль `ns` предназначен для преобразования объектов `SimpleNamespace` в различные форматы данных, такие как `dict`, `JSON`, `CSV`, `XML` и `XLS`. Это облегчает экспорт и сериализацию данных, хранящихся в объектах `SimpleNamespace`.

## Подробней

Модуль предоставляет набор функций для конвертации объектов `SimpleNamespace` в различные форматы. Каждая функция выполняет определенную задачу преобразования, обеспечивая гибкость при работе с данными в разных представлениях. Функции используют другие модули, такие как `xml2dict`, `save_csv_file` и `save_xls_file` из проекта `hypotez`.

## Функции

### `ns2dict`

```python
def ns2dict(obj: Any) -> Dict[str, Any]:
    """
    Args:
        obj (Any): Объект для конвертации. Может быть SimpleNamespace, dict или любой объект
                   с похожей структурой.

    Returns:
        Dict[str, Any]: Преобразованный словарь с обработанными вложенными структурами.

    **Как работает функция**:
    Функция рекурсивно преобразует объект с парами ключ-значение в словарь. Обрабатывает пустые ключи, заменяя их пустой строкой.

    ```
    +-------+
    |  Начало |
    +-------+
        |
        V
    +-----------------------------------------------------+
    | Проверка: Есть ли у объекта атрибут '__dict__'?     |
    +-----------------------------------------------------+
        |   Да                                          |   Нет
        V                                               V
    +-----------------------------------------------------+   +-----------------------------------------------------+
    | Преобразование: Рекурсивное преобразование в словарь |   | Проверка: Является ли объект словарем?            |
    +-----------------------------------------------------+   +-----------------------------------------------------+
        |                                               |       |   Да                                          |   Нет
        |                                               |       V                                               V
        +-----------------------------------------------------+   +-----------------------------------------------------+   +-------+
        | Преобразование: Рекурсивное преобразование в словарь |   | Проверка: Является ли объект списком?             |   | Возврат |
        +-----------------------------------------------------+   +-----------------------------------------------------+   +-------+
        |                                               |       |   Да                                          |
        |                                               |       V
        |                                               |       +-----------------------------------------------------+
        |                                               |       | Преобразование: Рекурсивное преобразование элементов |
        |                                               |       +-----------------------------------------------------+
        |                                               |       |   Нет
        |                                               |       V
        |                                               |       +-------+
        |                                               |       | Возврат |
        |                                               |       +-------+
        V
    +-------+
    |  Возврат |
    +-------+
    ```
    """
    ...
```

**Описание**: Рекурсивно преобразует объект с парами ключ-значение в словарь. Обрабатывает пустые ключи, заменяя их пустой строкой.

**Параметры**:
- `obj` (Any): Объект для конвертации. Может быть `SimpleNamespace`, `dict` или любой объект с похожей структурой.

**Возвращает**:
- `Dict[str, Any]`: Преобразованный словарь с обработанными вложенными структурами.

**Примеры**:

```python
from types import SimpleNamespace

data = SimpleNamespace(name='John', age=30, address=SimpleNamespace(city='New York', zip='10001'))
result = ns2dict(data)
print(result)
# Expected output: {'name': 'John', 'age': 30, 'address': {'city': 'New York', 'zip': '10001'}}

data = {'name': 'John', 'age': 30, 'address': {'city': 'New York', 'zip': '10001'}}
result = ns2dict(data)
print(result)
# Expected output: {'name': 'John', 'age': 30, 'address': {'city': 'New York', 'zip': '10001'}}
```

### `ns2csv`

```python
def ns2csv(ns_obj: SimpleNamespace, csv_file_path: str | Path) -> bool:
    """
    Args:
        ns_obj (SimpleNamespace): Объект SimpleNamespace для конвертации.
        csv_file_path (str | Path): Путь для сохранения CSV файла.

    Returns:
        bool: True в случае успеха, False в противном случае.
    
    Raises:
        Exception: Возникает, если происходит ошибка при преобразовании SimpleNamespace в CSV.

    **Как работает функция**:
    Преобразует объект SimpleNamespace в CSV формат и сохраняет его в указанный файл.
    """
    ...
```

**Описание**: Преобразует объект `SimpleNamespace` в формат `CSV`.

**Параметры**:
- `ns_obj` (SimpleNamespace): Объект `SimpleNamespace` для конвертации.
- `csv_file_path` (str | Path): Путь для сохранения `CSV` файла.

**Возвращает**:
- `bool`: `True` в случае успеха, `False` в противном случае.

**Примеры**:

```python
from types import SimpleNamespace
from pathlib import Path

data = SimpleNamespace(name='John', age=30, city='New York')
file_path = Path('output.csv')
result = ns2csv(data, file_path)
print(result)
# Expected output: True
```

### `ns2xml`

```python
def ns2xml(ns_obj: SimpleNamespace, root_tag: str = "root") -> str:
    """
    Args:
        ns_obj (SimpleNamespace): Объект SimpleNamespace для конвертации.
        root_tag (str): Корневой тег для XML.

    Returns:
        str: Результирующая XML строка.

    Raises:
        Exception: Возникает, если происходит ошибка при преобразовании SimpleNamespace в XML.

    **Как работает функция**:
    Преобразует объект SimpleNamespace в XML формат.
    """
    ...
```

**Описание**: Преобразует объект `SimpleNamespace` в формат `XML`.

**Параметры**:
- `ns_obj` (SimpleNamespace): Объект `SimpleNamespace` для конвертации.
- `root_tag` (str): Корневой тег для `XML`.

**Возвращает**:
- `str`: Результирующая `XML` строка.

**Примеры**:

```python
from types import SimpleNamespace

data = SimpleNamespace(name='John', age=30, city='New York')
result = ns2xml(data, root_tag='person')
print(result)
# Example output: <person><name>John</name><age>30</age><city>New York</city></person>
```

### `ns2xls`

```python
def ns2xls(data: SimpleNamespace, xls_file_path: str | Path) -> bool:
    """
    Args:
        ns_obj (SimpleNamespace): Объект SimpleNamespace для конвертации.
        xls_file_path (str | Path): Путь для сохранения XLS файла.

    Returns:
        bool: True в случае успеха, False в противном случае.
    """
    ...
```

**Описание**: Преобразует объект `SimpleNamespace` в формат `XLS`.

**Параметры**:
- `data` (SimpleNamespace): Объект `SimpleNamespace` для конвертации.
- `xls_file_path` (str | Path): Путь для сохранения `XLS` файла.

**Возвращает**:
- `bool`: `True` в случае успеха, `False` в противном случае.

**Примеры**:

```python
from types import SimpleNamespace
from pathlib import Path

data = SimpleNamespace(name='John', age=30, city='New York')
file_path = Path('output.xls')
result = ns2xls(data, file_path)
print(result)
# Expected output: True