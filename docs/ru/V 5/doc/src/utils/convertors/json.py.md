# Модуль `json`

## Обзор

Модуль `json` предназначен для преобразования данных JSON в различные форматы, такие как CSV, SimpleNamespace, XML и XLS. Он предоставляет функции для обработки JSON-данных и сохранения их в соответствующих форматах файлов.

## Подробней

Этот модуль предоставляет набор функций для конвертации JSON данных в различные форматы. Он используется для обработки и преобразования данных, полученных в формате JSON, в более удобные для анализа и хранения форматы, такие как CSV, SimpleNamespace, XML и XLS. Модуль включает функции для чтения JSON данных из строк, файлов и словарей, а также для записи преобразованных данных в файлы. Расположение файла в проекте `hypotez/src/utils/convertors/json.py` указывает на то, что он является частью подсистемы конвертации данных.

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
    ...
```

**Как работает функция**:
Функция `json2csv` принимает JSON данные (в виде строки, списка словарей, словаря или пути к файлу) и преобразует их в формат CSV. Сначала она загружает JSON данные в зависимости от их типа. Затем она использует функцию `save_csv_file` для сохранения данных в CSV файл по указанному пути. В случае ошибки при загрузке JSON или записи CSV, функция регистрирует ошибку и возвращает `False`.

**Параметры**:
- `json_data` (str | list | dict | Path): JSON данные для конвертации. Это может быть строка с JSON, список словарей, словарь или путь к JSON файлу.
- `csv_file_path` (str | Path): Путь к файлу CSV, в который будут записаны преобразованные данные.

**Возвращает**:
- `bool`: Возвращает `True`, если преобразование и запись в файл прошли успешно, и `False` в противном случае.

**Вызывает исключения**:
- `ValueError`: Вызывается, если передан неподдерживаемый тип данных для `json_data`.
- `Exception`: Вызывается при возникновении ошибок в процессе разбора JSON или записи CSV файла.

**Примеры**:

```python
from pathlib import Path

# Пример 1: Преобразование JSON строки в CSV файл
json_string = '[{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]'
csv_file = 'output.csv'
result = json2csv(json_string, csv_file)
print(f'Результат преобразования JSON строки в CSV: {result}')

# Пример 2: Преобразование JSON файла в CSV файл
json_file_path = Path('input.json')  # Допустим, у нас есть файл input.json с JSON данными
csv_file_path = Path('output.csv')
result = json2csv(json_file_path, csv_file_path)
print(f'Результат преобразования JSON файла в CSV: {result}')

# Пример 3: Преобразование списка словарей в CSV файл
json_list = [{"name": "Bob", "age": 40}, {"name": "Eve", "age": 28}]
csv_file_path = Path('output.csv')
result = json2csv(json_list, csv_file_path)
print(f'Результат преобразования списка словарей в CSV: {result}')
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
    ...
```

**Как работает функция**:
Функция `json2ns` преобразует JSON данные (в виде строки, словаря или пути к файлу) в объект `SimpleNamespace`. Сначала она загружает JSON данные в зависимости от их типа. Затем она создает объект `SimpleNamespace` из загруженных данных и возвращает его. В случае ошибки при загрузке JSON, функция регистрирует ошибку.

**Параметры**:
- `json_data` (str | dict | Path): JSON данные для конвертации. Это может быть строка с JSON, словарь или путь к JSON файлу.

**Возвращает**:
- `SimpleNamespace`: Возвращает объект `SimpleNamespace`, представляющий JSON данные.

**Вызывает исключения**:
- `ValueError`: Вызывается, если передан неподдерживаемый тип данных для `json_data`.
- `Exception`: Вызывается при возникновении ошибок в процессе разбора JSON.

**Примеры**:

```python
from pathlib import Path

# Пример 1: Преобразование JSON строки в SimpleNamespace
json_string = '{"name": "John", "age": 30}'
result = json2ns(json_string)
print(f'Результат преобразования JSON строки в SimpleNamespace: {result.name}, {result.age}')

# Пример 2: Преобразование JSON файла в SimpleNamespace
json_file_path = Path('input.json')  # Допустим, у нас есть файл input.json с JSON данными
result = json2ns(json_file_path)
print(f'Результат преобразования JSON файла в SimpleNamespace: {result.name}, {result.age}')

# Пример 3: Преобразование словаря в SimpleNamespace
json_dict = {"name": "Bob", "age": 40}
result = json2ns(json_dict)
print(f'Результат преобразования словаря в SimpleNamespace: {result.name}, {result.age}')
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
    ...
```

**Как работает функция**:
Функция `json2xml` преобразует JSON данные (в виде строки, словаря или пути к файлу) в XML формат. Она использует функцию `dict2xml` для выполнения преобразования. Функция возвращает строку, содержащую XML данные.

**Параметры**:
- `json_data` (str | dict | Path): JSON данные для конвертации. Это может быть строка с JSON, словарь или путь к JSON файлу.
- `root_tag` (str): Корневой тег для XML. По умолчанию "root".

**Возвращает**:
- `str`: Возвращает строку, представляющую XML данные.

**Вызывает исключения**:
- `ValueError`: Вызывается, если передан неподдерживаемый тип данных для `json_data`.
- `Exception`: Вызывается при возникновении ошибок в процессе разбора JSON или преобразования в XML.

**Примеры**:

```python
from pathlib import Path

# Пример 1: Преобразование JSON строки в XML
json_string = '{"name": "John", "age": 30}'
result = json2xml(json_string, root_tag='person')
print(f'Результат преобразования JSON строки в XML: {result}')

# Пример 2: Преобразование JSON файла в XML
json_file_path = Path('input.json')  # Допустим, у нас есть файл input.json с JSON данными
result = json2xml(json_file_path, root_tag='person')
print(f'Результат преобразования JSON файла в XML: {result}')

# Пример 3: Преобразование словаря в XML
json_dict = {"name": "Bob", "age": 40}
result = json2xml(json_dict, root_tag='person')
print(f'Результат преобразования словаря в XML: {result}')
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
    ...
```

**Как работает функция**:
Функция `json2xls` принимает JSON данные (в виде строки, списка словарей, словаря или пути к файлу) и преобразует их в формат XLS. Она использует функцию `save_xls_file` для сохранения данных в XLS файл по указанному пути. Функция возвращает `True`, если преобразование и запись в файл прошли успешно, и `False` в противном случае.

**Параметры**:
- `json_data` (str | list | dict | Path): JSON данные для конвертации. Это может быть строка с JSON, список словарей, словарь или путь к JSON файлу.
- `xls_file_path` (str | Path): Путь к файлу XLS, в который будут записаны преобразованные данные.

**Возвращает**:
- `bool`: Возвращает `True`, если преобразование и запись в файл прошли успешно, и `False` в противном случае.

**Вызывает исключения**:
- `ValueError`: Вызывается, если передан неподдерживаемый тип данных для `json_data`.
- `Exception`: Вызывается при возникновении ошибок в процессе разбора JSON или записи XLS файла.

**Примеры**:

```python
from pathlib import Path

# Пример 1: Преобразование JSON строки в XLS файл
json_string = '[{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]'
xls_file = 'output.xls'
result = json2xls(json_string, xls_file)
print(f'Результат преобразования JSON строки в XLS: {result}')

# Пример 2: Преобразование JSON файла в XLS файл
json_file_path = Path('input.json')  # Допустим, у нас есть файл input.json с JSON данными
xls_file_path = Path('output.xls')
result = json2xls(json_file_path, xls_file_path)
print(f'Результат преобразования JSON файла в XLS: {result}')

# Пример 3: Преобразование списка словарей в XLS файл
json_list = [{"name": "Bob", "age": 40}, {"name": "Eve", "age": 28}]
xls_file_path = Path('output.xls')
result = json2xls(json_list, xls_file_path)
print(f'Результат преобразования списка словарей в XLS: {result}')