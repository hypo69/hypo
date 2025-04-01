# Модуль `src.utils.convertors.ns`

## Обзор

Модуль `src.utils.convertors.ns` предназначен для преобразования объектов `SimpleNamespace` в различные форматы данных, такие как словари, JSON, CSV, XML и XLS. Он предоставляет набор функций для удобного преобразования и сохранения данных в нужном формате.

## Подробнее

Модуль содержит функции, которые позволяют преобразовывать объекты `SimpleNamespace` в различные форматы, обеспечивая гибкость при работе с данными. Каждая функция выполняет определенную задачу преобразования и использует вспомогательные функции из других модулей (`xml2dict`, `save_csv_file`, `save_xls_file`) для выполнения фактического преобразования и сохранения данных. Модуль также использует модуль `logger` для регистрации ошибок.

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
- `obj` (Any): Объект для преобразования. Может быть `SimpleNamespace`, `dict` или любым объектом со схожей структурой.

**Возвращает**:
- `Dict[str, Any]`: Преобразованный словарь с обработанными вложенными структурами.

**Как работает функция**:

1. Функция `ns2dict` принимает объект `obj` в качестве входных данных.
2. Вызывает внутреннюю функцию `convert` для рекурсивной обработки объекта.
3. Если `value` имеет атрибут `__dict__` (например, `SimpleNamespace` или пользовательские объекты), функция преобразует его в словарь, обрабатывая каждый ключ и значение рекурсивно. Пустые ключи заменяются пустой строкой.
4. Если `value` является объектом, подобным словарю (имеет метод `.items()`), функция преобразует его в словарь, обрабатывая каждый ключ и значение рекурсивно. Пустые ключи заменяются пустой строкой.
5. Если `value` является списком или другим итерируемым объектом, функция рекурсивно преобразует каждый элемент списка.
6. Если `value` не является ни одним из вышеперечисленных типов, функция возвращает его без изменений.

**Внутренние функции**:

### `convert`

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

**Как работает функция**:
1. Функция `convert` принимает значение `value` в качестве входных данных.
2. Если `value` имеет атрибут `__dict__` (например, `SimpleNamespace` или пользовательские объекты), функция преобразует его в словарь, обрабатывая каждый ключ и значение рекурсивно. Пустые ключи заменяются пустой строкой.
3. Если `value` является объектом, подобным словарю (имеет метод `.items()`), функция преобразует его в словарь, обрабатывая каждый ключ и значение рекурсивно. Пустые ключи заменяются пустой строкой.
4. Если `value` является списком или другим итерируемым объектом, функция рекурсивно преобразует каждый элемент списка.
5. Если `value` не является ни одним из вышеперечисленных типов, функция возвращает его без изменений.

```mermaid
graph TD
    A[obj: Any] --> B{hasattr(value, '__dict__')?}
    B -- Yes --> C{key or ""}
    C --> D[vars(value).items()]
    D --> E[convert(val)]
    E --> F[Dict[str, Any]]
    B -- No --> G{hasattr(value, 'items')?}
    G -- Yes --> H{key or ""}
    H --> I[value.items()]
    I --> J[convert(val)]
    J --> K[Dict[str, Any]]
    G -- No --> L{isinstance(value, list)?}
    L -- Yes --> M[convert(item) for item in value]
    M --> N[List[Any]]
    L -- No --> O[value]
    O --> P[Any]
    F --> Q[Dict[str, Any]]
    K --> R[Dict[str, Any]]
    N --> S[Dict[str, Any]]
    P --> T[Dict[str, Any]]
    Q --> return
    R --> return
    S --> return
    T --> return
```

**Примеры**:

```python
from types import SimpleNamespace

obj = SimpleNamespace(name='John', age=30, address=SimpleNamespace(city='New York', zip='10001'))
result = ns2dict(obj)
print(result)  # {'name': 'John', 'age': 30, 'address': {'city': 'New York', 'zip': '10001'}}

obj = {'name': 'John', 'age': 30, 'address': {'city': 'New York', 'zip': '10001'}}
result = ns2dict(obj)
print(result)  # {'name': 'John', 'age': 30, 'address': {'city': 'New York', 'zip': '10001'}}

obj = SimpleNamespace(name='John', age=30, address=SimpleNamespace(city='New York', zip='10001', empty_key=''))
result = ns2dict(obj)
print(result)  # {'name': 'John', 'age': 30, 'address': {'city': 'New York', 'zip': '10001', '': ''}}
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

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при преобразовании в CSV.

**Как работает функция**:

1. Функция `ns2csv` принимает объект `ns_obj` типа `SimpleNamespace` и путь к файлу `csv_file_path`.
2. Преобразует `ns_obj` в словарь с помощью функции `ns2dict`.
3. Сохраняет данные в CSV-файл с помощью функции `save_csv_file` из модуля `src.utils.csv`.
4. В случае успеха возвращает `True`, в случае ошибки логирует ошибку с помощью `logger.error` и возвращает `None`.

```mermaid
graph TD
    A[ns_obj: SimpleNamespace, csv_file_path: str | Path] --> B{try}
    B --> C[data = [ns2dict(ns_obj)]]
    C --> D[save_csv_file(data, csv_file_path)]
    D --> E[return True]
    B --> F{except Exception as ex}
    F --> G[logger.error(f"ns2csv failed", ex, True)]
    G --> H[return None]
```

**Примеры**:

```python
from types import SimpleNamespace
from pathlib import Path

ns_obj = SimpleNamespace(name='John', age=30)
csv_file_path = 'data.csv'
result = ns2csv(ns_obj, csv_file_path)
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

**Как работает функция**:

1. Функция `ns2xml` принимает объект `ns_obj` типа `SimpleNamespace` и корневой тег `root_tag`.
2. Преобразует `ns_obj` в словарь с помощью функции `ns2dict`.
3. Преобразует словарь в XML с помощью функции `xml2dict` из модуля `src.utils.convertors`.
4. В случае успеха возвращает XML-строку, в случае ошибки логирует ошибку с помощью `logger.error` и возвращает `None`.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при преобразовании в XML.

```mermaid
graph TD
    A[ns_obj: SimpleNamespace, root_tag: str] --> B{try}
    B --> C[data = ns2dict(ns_obj)]
    C --> D[xml2dict(data)]
    D --> E[return XML string]
    B --> F{except Exception as ex}
    F --> G[logger.error(f"ns2xml failed", ex, True)]
    G --> H[return None]
```

**Примеры**:

```python
from types import SimpleNamespace

ns_obj = SimpleNamespace(name='John', age=30)
xml_string = ns2xml(ns_obj)
print(xml_string)  # <root><name>John</name><age>30</age></root>
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

**Как работает функция**:

1. Функция `ns2xls` принимает объект `data` типа `SimpleNamespace` и путь к файлу `xls_file_path`.
2. Сохраняет данные в XLS-файл с помощью функции `save_xls_file` из модуля `src.utils.xls`.
3. Возвращает результат выполнения функции `save_xls_file`.

```mermaid
graph TD
    A[data: SimpleNamespace, xls_file_path: str | Path] --> B[save_xls_file(data, xls_file_path)]
    B --> C[return result]
```

**Примеры**:

```python
from types import SimpleNamespace
from pathlib import Path

data = SimpleNamespace(name='John', age=30)
xls_file_path = 'data.xls'
result = ns2xls(data, xls_file_path)
print(result)  # True