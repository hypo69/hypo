# Модуль `ns`

## Обзор

Модуль `ns` предназначен для конвертации объектов `SimpleNamespace` в различные форматы, такие как `dict`, `JSON`, `CSV`, `XML` и `XLS`.
Он предоставляет набор функций для упрощения процесса преобразования данных между различными форматами, что может быть полезно при работе с конфигурационными файлами, обменом данными между системами и другими задачами.

## Подробней

Этот модуль облегчает преобразование данных из объектов `SimpleNamespace` в различные форматы, такие как словари, JSON, CSV, XML и XLS. 
Он содержит функции, которые рекурсивно обрабатывают объекты `SimpleNamespace` для преобразования их в нужный формат.
В проекте `hypotez` этот модуль может использоваться для работы с конфигурационными данными, сохранения результатов анализа в различных форматах и обмена данными с другими системами.

## Функции

### `ns2dict`

```python
def ns2dict(obj: Any) -> Dict[str, Any]:
    """
    Recursively convert an object with key-value pairs to a dictionary.
    Handles empty keys by substituting them with an empty string.

    Args:
        obj (Any): The object to convert. Can be SimpleNamespace, dict, or any object
                   with a similar structure.

    Returns:
        Dict[str, Any]: Converted dictionary with nested structures handled.
    """
    ...
```

**Описание**: Рекурсивно преобразует объект с парами ключ-значение в словарь. Обрабатывает пустые ключи, заменяя их пустой строкой.

**Параметры**:
- `obj` (Any): Объект для преобразования. Может быть `SimpleNamespace`, `dict` или любым объектом с аналогичной структурой.

**Возвращает**:
- `Dict[str, Any]`: Преобразованный словарь с обработанными вложенными структурами.

**Примеры**:
```python
from types import SimpleNamespace

data = SimpleNamespace(name='John', age=30, address=SimpleNamespace(city='New York', zip='10001'))
result = ns2dict(data)
print(result)  # {'name': 'John', 'age': 30, 'address': {'city': 'New York', 'zip': '10001'}}

data = {'name': 'John', 'age': 30, 'address': {'city': 'New York', 'zip': '10001'}}
result = ns2dict(data)
print(result)  # {'name': 'John', 'age': 30, 'address': {'city': 'New York', 'zip': '10001'}}
```

### `ns2csv`

```python
def ns2csv(ns_obj: SimpleNamespace, csv_file_path: str | Path) -> bool:
    """
    Convert SimpleNamespace object to CSV format.

    Args:
        ns_obj (SimpleNamespace): The SimpleNamespace object to convert.
        csv_file_path (str | Path): Path to save the CSV file.

    Returns:
        bool: True if successful, False otherwise.
    """
    ...
```

**Описание**: Преобразует объект `SimpleNamespace` в формат `CSV`.

**Параметры**:
- `ns_obj` (SimpleNamespace): Объект `SimpleNamespace` для преобразования.
- `csv_file_path` (str | Path): Путь для сохранения `CSV` файла.

**Возвращает**:
- `bool`: `True`, если преобразование выполнено успешно, `False` в противном случае.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке во время преобразования в `CSV`.

**Примеры**:
```python
from types import SimpleNamespace
from pathlib import Path

data = SimpleNamespace(name='John', age=30, city='New York')
file_path = Path('data.csv')
result = ns2csv(data, file_path)
print(result)  # True
```

### `ns2xml`

```python
def ns2xml(ns_obj: SimpleNamespace, root_tag: str = "root") -> str:
    """
    Convert SimpleNamespace object to XML format.

    Args:
        ns_obj (SimpleNamespace): The SimpleNamespace object to convert.
        root_tag (str): The root element tag for the XML.

    Returns:
        str: The resulting XML string.
    """
    ...
```

**Описание**: Преобразует объект `SimpleNamespace` в формат `XML`.

**Параметры**:
- `ns_obj` (SimpleNamespace): Объект `SimpleNamespace` для преобразования.
- `root_tag` (str): Корневой тег для `XML`. По умолчанию `"root"`.

**Возвращает**:
- `str`: Результирующая `XML` строка.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке во время преобразования в `XML`.

**Примеры**:
```python
from types import SimpleNamespace

data = SimpleNamespace(name='John', age=30, city='New York')
result = ns2xml(data, root_tag='person')
print(result)  # <person><name>John</name><age>30</age><city>New York</city></person>
```

### `ns2xls`

```python
def ns2xls(data: SimpleNamespace, xls_file_path: str | Path) -> bool:
    """
    Convert SimpleNamespace object to XLS format.

    Args:
        ns_obj (SimpleNamespace): The SimpleNamespace object to convert.
        xls_file_path (str | Path): Path to save the XLS file.

    Returns:
        bool: True if successful, False otherwise.
    """
    ...
```

**Описание**: Преобразует объект `SimpleNamespace` в формат `XLS`.

**Параметры**:
- `data` (SimpleNamespace): Объект `SimpleNamespace` для преобразования.
- `xls_file_path` (str | Path): Путь для сохранения `XLS` файла.

**Возвращает**:
- `bool`: `True`, если преобразование выполнено успешно, `False` в противном случае.

**Примеры**:
```python
from types import SimpleNamespace
from pathlib import Path

data = SimpleNamespace(name='John', age=30, city='New York')
file_path = Path('data.xls')
result = ns2xls(data, file_path)
print(result)  # True