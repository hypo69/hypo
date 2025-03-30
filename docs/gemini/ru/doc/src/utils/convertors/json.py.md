# Модуль `json.py`

## Обзор

Модуль `json.py` предоставляет инструменты для преобразования данных JSON в различные форматы, такие как CSV, SimpleNamespace, XML и XLS. Он содержит функции для чтения JSON данных из строк, файлов или словарей и преобразования их в нужный формат.

## Подробнее

Этот модуль предназначен для облегчения работы с JSON-данными, позволяя преобразовывать их в форматы, удобные для различных целей, таких как анализ данных, экспорт в другие приложения или хранение в определенных форматах. Он использует другие модули проекта, такие как `csv`, `SimpleNamespace`, `pathlib`, `src.utils.csv`, `src.utils.jjson`, `src.utils.xls`, `src.utils.convertors.dict` и `src.logger.logger`, чтобы обеспечить необходимую функциональность.

## Функции

### `json2csv`

```python
def json2csv(json_data: str | list | dict | Path, csv_file_path: str | Path) -> bool:
    """
    Convert JSON data or JSON file to CSV format with a comma delimiter.

    Args:
        json_data (str | list | dict | Path): JSON data as a string, list of dictionaries, or file path to a JSON file.
        csv_file_path (str | Path): Path to the CSV file to write.

    Returns:
        bool: True if successful, False otherwise.

    Raises:
        ValueError: If unsupported type for json_data.
        Exception: If unable to parse JSON or write CSV.
    """
```

**Описание**: Преобразует JSON данные или JSON файл в формат CSV с использованием запятой в качестве разделителя.

**Параметры**:
- `json_data` (str | list | dict | Path): JSON данные в виде строки, списка словарей или пути к JSON файлу.
- `csv_file_path` (str | Path): Путь к CSV файлу для записи.

**Возвращает**:
- `bool`: `True`, если преобразование прошло успешно, иначе `False`.

**Вызывает исключения**:
- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если не удается распарсить JSON или записать CSV.

**Примеры**:
```python
from pathlib import Path
from src.utils.convertors.json import json2csv

# Пример 1: Преобразование JSON строки в CSV файл
json_string = '[{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]'
csv_file = "output.csv"
result = json2csv(json_string, csv_file)
print(f"Результат преобразования: {result}")  # Вывод: Результат преобразования: True

# Пример 2: Преобразование JSON файла в CSV файл
json_file_path = Path("input.json")
csv_file_path = Path("output.csv")
result = json2csv(json_file_path, csv_file_path)
print(f"Результат преобразования: {result}")  # Вывод: Результат преобразования: True
```

### `json2ns`

```python
def json2ns(json_data: str | dict | Path) -> SimpleNamespace:
    """
    Convert JSON data or JSON file to SimpleNamespace object.

    Args:
        json_data (str | dict | Path): JSON data as a string, dictionary, or file path to a JSON file.

    Returns:
        SimpleNamespace: Parsed JSON data as a SimpleNamespace object.
    
    Raises:
        ValueError: If unsupported type for json_data.
        Exception: If unable to parse JSON.
    """
```

**Описание**: Преобразует JSON данные или JSON файл в объект SimpleNamespace.

**Параметры**:
- `json_data` (str | dict | Path): JSON данные в виде строки, словаря или пути к JSON файлу.

**Возвращает**:
- `SimpleNamespace`: Распарсенные JSON данные в виде объекта SimpleNamespace.

**Вызывает исключения**:
- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если не удается распарсить JSON.

**Примеры**:
```python
from pathlib import Path
from src.utils.convertors.json import json2ns

# Пример 1: Преобразование JSON строки в SimpleNamespace
json_string = '{"name": "John", "age": 30}'
result = json2ns(json_string)
print(f"Имя: {result.name}, Возраст: {result.age}")  # Вывод: Имя: John, Возраст: 30

# Пример 2: Преобразование JSON файла в SimpleNamespace
json_file_path = Path("input.json")
result = json2ns(json_file_path)
print(f"Имя: {result.name}, Возраст: {result.age}")  # Вывод: Имя: John, Возраст: 30
```

### `json2xml`

```python
def json2xml(json_data: str | dict | Path, root_tag: str = "root") -> str:
    """
    Convert JSON data or JSON file to XML format.

    Args:
        json_data (str | dict | Path): JSON data as a string, dictionary, or file path to a JSON file.
        root_tag (str): The root element tag for the XML.

    Returns:
        str: The resulting XML string.

    Raises:
        ValueError: If unsupported type for json_data.
        Exception: If unable to parse JSON or convert to XML.
    """
```

**Описание**: Преобразует JSON данные или JSON файл в формат XML.

**Параметры**:
- `json_data` (str | dict | Path): JSON данные в виде строки, словаря или пути к JSON файлу.
- `root_tag` (str): Корневой элемент для XML.

**Возвращает**:
- `str`: Результирующая XML строка.

**Вызывает исключения**:
- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если не удается распарсить JSON или преобразовать в XML.

**Примеры**:
```python
from pathlib import Path
from src.utils.convertors.json import json2xml

# Пример 1: Преобразование JSON строки в XML
json_string = '{"name": "John", "age": 30}'
result = json2xml(json_string)
print(f"XML: {result}")  # Вывод: XML: <?xml version="1.0" encoding="utf-8"?><root><name>John</name><age>30</age></root>

# Пример 2: Преобразование JSON файла в XML
json_file_path = Path("input.json")
result = json2xml(json_file_path)
print(f"XML: {result}")  # Вывод: XML: <?xml version="1.0" encoding="utf-8"?><root><name>John</name><age>30</age></root>
```

### `json2xls`

```python
def json2xls(json_data: str | list | dict | Path, xls_file_path: str | Path) -> bool:
    """
    Convert JSON data or JSON file to XLS format.

    Args:
        json_data (str | list | dict | Path): JSON data as a string, list of dictionaries, or file path to a JSON file.
        xls_file_path (str | Path): Path to the XLS file to write.

    Returns:
        bool: True if successful, False otherwise.

    Raises:
        ValueError: If unsupported type for json_data.
        Exception: If unable to parse JSON or write XLS.
    """
```

**Описание**: Преобразует JSON данные или JSON файл в формат XLS.

**Параметры**:
- `json_data` (str | list | dict | Path): JSON данные в виде строки, списка словарей или пути к JSON файлу.
- `xls_file_path` (str | Path): Путь к XLS файлу для записи.

**Возвращает**:
- `bool`: `True`, если преобразование прошло успешно, иначе `False`.

**Вызывает исключения**:
- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если не удается распарсить JSON или записать XLS.

**Примеры**:
```python
from pathlib import Path
from src.utils.convertors.json import json2xls

# Пример 1: Преобразование JSON строки в XLS файл
json_string = '[{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]'
xls_file = "output.xls"
result = json2xls(json_string, xls_file)
print(f"Результат преобразования: {result}")  # Вывод: Результат преобразования: True

# Пример 2: Преобразование JSON файла в XLS файл
json_file_path = Path("input.json")
xls_file_path = Path("output.xls")
result = json2xls(json_file_path, xls_file_path)
print(f"Результат преобразования: {result}")  # Вывод: Результат преобразования: True