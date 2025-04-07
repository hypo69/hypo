# Модуль для преобразования SimpleNamespace в различные форматы
=================================================================

Модуль `src.utils.convertors.ns` предназначен для преобразования объектов `SimpleNamespace` в различные форматы данных, такие как словари, JSON, CSV, XML и XLS. Это упрощает экспорт и интеграцию данных из объектов `SimpleNamespace` в различные системы и приложения.

## Обзор

Модуль содержит функции для преобразования объектов `SimpleNamespace` в различные форматы.

## Подробней

Этот модуль предоставляет набор функций, которые позволяют преобразовывать объекты `SimpleNamespace` в другие форматы данных. Объекты `SimpleNamespace` удобны для хранения данных, но часто требуется их экспорт в другие форматы для интеграции с различными системами и приложениями. Модуль `ns` предоставляет простые и удобные функции для выполнения таких преобразований.

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
- `obj` (Any): Объект для преобразования. Может быть `SimpleNamespace`, `dict` или любым другим объектом со схожей структурой.

**Возвращает**:
- `Dict[str, Any]`: Преобразованный словарь с обработанными вложенными структурами.

**Как работает функция**:

1. Функция принимает объект `obj` в качестве входных данных.
2. Если `obj` имеет атрибут `__dict__` (например, `SimpleNamespace` или пользовательские объекты), то функция преобразует его в словарь, обрабатывая каждый ключ и значение рекурсивно. Пустые ключи заменяются пустой строкой.
3. Если `obj` является объектом, подобным словарю (имеет метод `items()`), функция также преобразует его в словарь, обрабатывая каждый ключ и значение рекурсивно. Пустые ключи заменяются пустой строкой.
4. Если `obj` является списком или другой итерируемой структурой, функция рекурсивно обрабатывает каждый элемент списка.
5. Если `obj` не является ни одним из вышеперечисленных типов, функция возвращает его без изменений.

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

1. Если значение имеет атрибут `__dict__` (например, `SimpleNamespace` или пользовательские объекты), функция преобразует его в словарь, обрабатывая каждый ключ и значение рекурсивно. Пустые ключи заменяются пустой строкой.
2. Если значение является объектом, подобным словарю (имеет метод `items()`), функция также преобразует его в словарь, обрабатывая каждый ключ и значение рекурсивно. Пустые ключи заменяются пустой строкой.
3. Если значение является списком или другой итерируемой структурой, функция рекурсивно обрабатывает каждый элемент списка.
4. Если значение не является ни одним из вышеперечисленных типов, функция возвращает его без изменений.

**ASCII Flowchart**:

```
    Начало
     ↓
  hasattr(value, '__dict__')? -- Да → Преобразование в словарь (vars(value).items())
     |                                  ↓
     |                                  Рекурсивная обработка каждого элемента
     |
     Нет
     ↓
  hasattr(value, 'items')?    -- Да → Преобразование в словарь (value.items())
     |                                  ↓
     |                                  Рекурсивная обработка каждого элемента
     |
     Нет
     ↓
  isinstance(value, list)?       -- Да → Рекурсивная обработка каждого элемента списка
     |
     Нет
     ↓
  Возврат значения без изменений
     ↓
    Конец
```

**Примеры**:

```python
from types import SimpleNamespace

# Пример 1: Преобразование SimpleNamespace в словарь
ns_obj = SimpleNamespace(name='John', age=30, address=SimpleNamespace(city='New York', zip='10001'))
result = ns2dict(ns_obj)
print(result)
# Вывод: {'name': 'John', 'age': 30, 'address': {'city': 'New York', 'zip': '10001'}}

# Пример 2: Преобразование словаря в словарь (с обработкой пустых ключей)
dict_obj = {'name': 'Alice', '': 'empty', 'details': {'age': 25, '': 'none'}}
result = ns2dict(dict_obj)
print(result)
# Вывод: {'name': 'Alice', '': 'empty', 'details': {'age': 25, '': 'none'}}
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
- `bool`: `True`, если преобразование успешно, `False` в противном случае.

**Как работает функция**:

1. Функция принимает объект `SimpleNamespace` и путь к файлу CSV в качестве входных данных.
2. Преобразует `SimpleNamespace` в словарь, используя функцию `ns2dict`.
3. Сохраняет данные в CSV-файл, используя функцию `save_csv_file` из модуля `src.utils.csv`.
4. В случае успеха возвращает `True`, в случае ошибки логирует ошибку и возвращает `False`.

**ASCII Flowchart**:

```
    Начало
     ↓
  Преобразование SimpleNamespace в словарь (ns2dict)
     ↓
  Сохранение данных в CSV-файл (save_csv_file)
     ↓
  Успех? -- Да → Возврат True
     |
     Нет
     ↓
  Логирование ошибки
     ↓
  Возврат False
     ↓
    Конец
```

**Примеры**:

```python
from types import SimpleNamespace
from pathlib import Path

# Пример: Преобразование SimpleNamespace в CSV
ns_obj = SimpleNamespace(name='John', age=30, city='New York')
csv_file_path = Path('output.csv')
result = ns2csv(ns_obj, csv_file_path)
print(result)
# Вывод: True (если успешно)
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

1. Функция принимает объект `SimpleNamespace` и корневой тег XML в качестве входных данных.
2. Преобразует `SimpleNamespace` в словарь, используя функцию `ns2dict`.
3. Преобразует словарь в XML, используя функцию `xml2dict` из модуля `src.utils.convertors`.
4. В случае успеха возвращает XML-строку, в случае ошибки логирует ошибку и возвращает `None`.

**ASCII Flowchart**:

```
    Начало
     ↓
  Преобразование SimpleNamespace в словарь (ns2dict)
     ↓
  Преобразование словаря в XML (xml2dict)
     ↓
  Успех? -- Да → Возврат XML-строки
     |
     Нет
     ↓
  Логирование ошибки
     ↓
  Возврат None
     ↓
    Конец
```

**Примеры**:

```python
from types import SimpleNamespace

# Пример: Преобразование SimpleNamespace в XML
ns_obj = SimpleNamespace(name='John', age=30, city='New York')
xml_string = ns2xml(ns_obj, root_tag='person')
print(xml_string)
# Вывод: XML-строка (например, '<person><name>John</name><age>30</age><city>New York</city></person>')
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
- `bool`: `True`, если преобразование успешно, `False` в противном случае.

**Как работает функция**:

1. Функция принимает объект `SimpleNamespace` и путь к файлу XLS в качестве входных данных.
2. Сохраняет данные в XLS-файл, используя функцию `save_xls_file` из модуля `src.utils.xls`.
3. Возвращает результат сохранения XLS файла

**ASCII Flowchart**:

```
    Начало
     ↓
  Сохранение данных в XLS-файл (save_xls_file)
     ↓
  Успех? -- Да → Возврат True
     |
     Нет
     ↓
  Возврат False
     ↓
    Конец
```

**Примеры**:

```python
from types import SimpleNamespace
from pathlib import Path

# Пример: Преобразование SimpleNamespace в XLS
ns_obj = SimpleNamespace(name='John', age=30, city='New York')
xls_file_path = Path('output.xls')
result = ns2xls(ns_obj, xls_file_path)
print(result)
# Вывод: True (если успешно)