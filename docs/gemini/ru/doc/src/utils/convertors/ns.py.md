# Модуль для преобразования SimpleNamespace в различные форматы
=================================================================

Модуль `src.utils.convertors.ns` предназначен для преобразования объектов `SimpleNamespace` в различные форматы данных, такие как словари, JSON, CSV, XML и XLS.

## Обзор

Модуль предоставляет набор функций для конвертации объектов `SimpleNamespace` в различные форматы. Это может быть полезно при работе с данными, которые необходимо экспортировать или сохранить в определенном формате.

## Подробней

Модуль содержит функции для преобразования `SimpleNamespace` в `dict`, `JSON`, `CSV`, `XML` и `XLS`. Каждая функция выполняет преобразование и обработку данных, чтобы обеспечить совместимость с требуемым форматом. Например, функция `ns2dict` рекурсивно преобразует объект `SimpleNamespace` в словарь, обрабатывая вложенные структуры.

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
```

**Назначение**: Рекурсивно преобразует объект с парами "ключ-значение" в словарь. Обрабатывает пустые ключи, заменяя их пустой строкой.

**Параметры**:
- `obj` (Any): Объект для преобразования. Может быть `SimpleNamespace`, `dict` или любым объектом с аналогичной структурой.

**Возвращает**:
- `Dict[str, Any]`: Преобразованный словарь с обработанными вложенными структурами.

**Внутренние функции**:

#### `convert`

```python
def convert(value: Any) -> Any:
    """
    Recursively process values to handle nested structures and empty keys.

    Args:
        value (Any): Value to process.

    Returns:
        Any: Converted value.
    """
```

**Назначение**: Рекурсивно обрабатывает значения для обработки вложенных структур и пустых ключей.

**Параметры**:
- `value` (Any): Значение для обработки.

**Возвращает**:
- `Any`: Преобразованное значение.

**Как работает функция `ns2dict`**:

1. Функция `ns2dict` принимает объект `obj` в качестве входных данных.
2. Внутри функции определяется внутренняя функция `convert`, которая рекурсивно обрабатывает значения.
3. Если значение имеет атрибут `__dict__` (например, `SimpleNamespace` или пользовательские объекты), функция преобразует его в словарь, обрабатывая каждый элемент.
4. Если значение является объектом, подобным словарю (имеет метод `.items()`), функция также преобразует его в словарь.
5. Если значение является списком или другим итерируемым объектом, функция рекурсивно обрабатывает каждый элемент списка.
6. В конечном итоге функция возвращает преобразованный словарь.

**Пример**:
```python
from types import SimpleNamespace

data = SimpleNamespace(name='John', age=30, address=SimpleNamespace(city='New York', zip='10001'))
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
```

**Назначение**: Преобразует объект `SimpleNamespace` в формат CSV.

**Параметры**:
- `ns_obj` (SimpleNamespace): Объект `SimpleNamespace` для преобразования.
- `csv_file_path` (str | Path): Путь для сохранения CSV-файла.

**Возвращает**:
- `bool`: `True`, если преобразование выполнено успешно, `False` в противном случае.

**Как работает функция `ns2csv`**:

1. Функция принимает объект `ns_obj` типа `SimpleNamespace` и путь к CSV-файлу `csv_file_path`.
2. Преобразует `ns_obj` в словарь с помощью функции `ns2dict`.
3. Сохраняет данные в CSV-файл с помощью функции `save_csv_file` из модуля `src.utils.csv`.
4. В случае успеха возвращает `True`, иначе логирует ошибку и возвращает `None`.

**Пример**:

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
```

**Назначение**: Преобразует объект `SimpleNamespace` в формат XML.

**Параметры**:
- `ns_obj` (SimpleNamespace): Объект `SimpleNamespace` для преобразования.
- `root_tag` (str): Корневой тег для XML. По умолчанию "root".

**Возвращает**:
- `str`: Результирующая XML-строка.

**Как работает функция `ns2xml`**:

1. Функция принимает объект `ns_obj` типа `SimpleNamespace` и корневой тег `root_tag`.
2. Преобразует `ns_obj` в словарь с помощью функции `ns2dict`.
3. Преобразует словарь в XML с помощью функции `xml2dict` из модуля `src.utils.convertors`.
4. В случае успеха возвращает XML-строку, иначе логирует ошибку.

**Пример**:

```python
from types import SimpleNamespace

data = SimpleNamespace(name='John', age=30, city='New York')
xml_string = ns2xml(data, root_tag='person')
print(xml_string)  # <person><name>John</name><age>30</age><city>New York</city></person>
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
```

**Назначение**: Преобразует объект `SimpleNamespace` в формат XLS.

**Параметры**:
- `data` (SimpleNamespace): Объект `SimpleNamespace` для преобразования.
- `xls_file_path` (str | Path): Путь для сохранения XLS-файла.

**Возвращает**:
- `bool`: `True`, если преобразование выполнено успешно, `False` в противном случае.

**Как работает функция `ns2xls`**:

1. Функция принимает объект `data` типа `SimpleNamespace` и путь к XLS-файлу `xls_file_path`.
2. Сохраняет данные в XLS-файл с помощью функции `save_xls_file` из модуля `src.utils.xls`.
3. В случае успеха возвращает `True`, иначе логирует ошибку.

**Пример**:

```python
from types import SimpleNamespace
from pathlib import Path

data = SimpleNamespace(name='John', age=30, city='New York')
file_path = Path('data.xls')
result = ns2xls(data, file_path)
print(result)  # True