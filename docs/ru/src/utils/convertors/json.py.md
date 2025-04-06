# Модуль для конвертации JSON данных в различные форматы
=================================================================

Модуль `src.utils.convertors.json` предоставляет функции для преобразования данных в формате JSON в различные форматы, такие как CSV, SimpleNamespace, XML и XLS.

## Обзор

Модуль содержит функции:

- `json2csv`: Преобразует JSON данные в формат CSV.
- `json2ns`: Преобразует JSON данные в объект SimpleNamespace.
- `json2xml`: Преобразует JSON данные в формат XML.
- `json2xls`: Преобразует JSON данные в формат XLS.

## Подробней

Этот модуль предоставляет удобные инструменты для работы с JSON данными и их преобразования в другие форматы, что может быть полезно для интеграции с различными системами и приложениями.

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

**Назначение**: Преобразует JSON данные (строку, список, словарь или путь к файлу) в формат CSV и сохраняет их в указанный CSV файл.

**Параметры**:

- `json_data` (str | list | dict | Path): JSON данные для преобразования. Это может быть строка с JSON, список словарей, словарь или путь к JSON файлу.
- `csv_file_path` (str | Path): Путь к CSV файлу, в который будут записаны преобразованные данные.

**Возвращает**:

- `bool`: `True`, если преобразование и запись в файл прошли успешно, иначе `False`.

**Вызывает исключения**:

- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если не удалось распарсить JSON данные или записать их в CSV файл.

**Как работает функция**:

1.  Функция `json2csv` принимает JSON данные и путь к CSV файлу.
2.  Определяет тип входных данных `json_data` (словарь, строка, список или путь к файлу).
3.  Загружает JSON данные в зависимости от их типа.
4.  Вызывает функцию `save_csv_file` из модуля `src.utils.csv` для сохранения данных в CSV файл.
5.  В случае успеха возвращает `True`, при возникновении ошибки логирует её и возвращает `False`.

```
JSON Data --> [Проверка типа данных]
    |
    -- dict --> [Преобразование в список] --> [save_csv_file] --> CSV File
    |
    -- str  --> [json.loads] --> [save_csv_file] --> CSV File
    |
    -- list --> [save_csv_file] --> CSV File
    |
    -- Path --> [Чтение файла] --> [json.load] --> [save_csv_file] --> CSV File
    |
    -- Другое --> ValueError
```

**Примеры**:

```python
from pathlib import Path

# Пример 1: Преобразование JSON строки в CSV файл
json_string = '[{"name": "Иван", "age": 30}, {"name": "Мария", "age": 25}]'
csv_file = 'data.csv'
result = json2csv(json_string, csv_file)
print(f"Результат преобразования JSON строки в CSV: {result}")  # Вывод: Результат преобразования JSON строки в CSV: True

# Пример 2: Преобразование JSON файла в CSV файл
json_file = Path('data.json')
#  Предположим, что data.json содержит: [{"name": "Иван", "age": 30}, {"name": "Мария", "age": 25}]
csv_file = 'data_from_file.csv'
result = json2csv(json_file, csv_file)
print(f"Результат преобразования JSON файла в CSV: {result}")  # Вывод: Результат преобразования JSON файла в CSV: True
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

**Назначение**: Преобразует JSON данные (строку, словарь или путь к файлу) в объект `SimpleNamespace`, что позволяет обращаться к элементам JSON как к атрибутам объекта.

**Параметры**:

- `json_data` (str | dict | Path): JSON данные для преобразования. Это может быть строка с JSON, словарь или путь к JSON файлу.

**Возвращает**:

- `SimpleNamespace`: Объект `SimpleNamespace`, представляющий JSON данные.

**Вызывает исключения**:

- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если не удалось распарсить JSON данные.

**Как работает функция**:

1.  Функция `json2ns` принимает JSON данные и путь к файлу.
2.  Определяет тип входных данных `json_data` (словарь, строка или путь к файлу).
3.  Загружает JSON данные в зависимости от их типа.
4.  Создает объект `SimpleNamespace` на основе загруженных данных и возвращает его.
5.  В случае успеха возвращает объект `SimpleNamespace`, при возникновении ошибки логирует её.

```
JSON Data --> [Проверка типа данных]
    |
    -- dict --> [Создание SimpleNamespace] --> SimpleNamespace object
    |
    -- str  --> [json.loads] --> [Создание SimpleNamespace] --> SimpleNamespace object
    |
    -- Path --> [Чтение файла] --> [json.load] --> [Создание SimpleNamespace] --> SimpleNamespace object
    |
    -- Другое --> ValueError
```

**Примеры**:

```python
from pathlib import Path

# Пример 1: Преобразование JSON строки в SimpleNamespace
json_string = '{"name": "Иван", "age": 30}'
ns_object = json2ns(json_string)
print(f"Имя: {ns_object.name}, Возраст: {ns_object.age}")  # Вывод: Имя: Иван, Возраст: 30

# Пример 2: Преобразование JSON файла в SimpleNamespace
json_file = Path('data.json')
# Предположим, что data.json содержит: {"name": "Иван", "age": 30}
ns_object = json2ns(json_file)
print(f"Имя: {ns_object.name}, Возраст: {ns_object.age}")  # Вывод: Имя: Иван, Возраст: 30
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

**Назначение**: Преобразует JSON данные (строку, словарь или путь к файлу) в формат XML.

**Параметры**:

- `json_data` (str | dict | Path): JSON данные для преобразования. Это может быть строка с JSON, словарь или путь к JSON файлу.
- `root_tag` (str): Корневой тег для XML. По умолчанию "root".

**Возвращает**:

- `str`: XML строка, представляющая JSON данные.

**Вызывает исключения**:

- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если не удалось распарсить JSON данные или преобразовать их в XML.

**Как работает функция**:

1.  Функция `json2xml` принимает JSON данные, корневой тег для XML.
2.  Вызывает функцию `dict2xml` из модуля `src.utils.convertors.dict` для преобразования данных в XML.
3.  Возвращает XML строку.

```
JSON Data --> [dict2xml] --> XML String
```

**Примеры**:

```python
from pathlib import Path

# Пример 1: Преобразование JSON строки в XML
json_string = '{"name": "Иван", "age": 30}'
xml_string = json2xml(json_string, root_tag="person")
print(f"XML: {xml_string}")
# Вывод: XML: <?xml version="1.0" encoding="utf-8"?>
# <person><name>Иван</name><age>30</age></person>

# Пример 2: Преобразование JSON файла в XML
json_file = Path('data.json')
# Предположим, что data.json содержит: {"name": "Иван", "age": 30}
xml_string = json2xml(json_file, root_tag="person")
print(f"XML: {xml_string}")
# Вывод: XML: <?xml version="1.0" encoding="utf-8"?>
# <person><name>Иван</name><age>30</age></person>
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

**Назначение**: Преобразует JSON данные (строку, список, словарь или путь к файлу) в формат XLS и сохраняет их в указанный файл.

**Параметры**:

- `json_data` (str | list | dict | Path): JSON данные для преобразования. Это может быть строка с JSON, список словарей, словарь или путь к JSON файлу.
- `xls_file_path` (str | Path): Путь к XLS файлу, в который будут записаны преобразованные данные.

**Возвращает**:

- `bool`: `True`, если преобразование и запись в файл прошли успешно, иначе `False`.

**Вызывает исключения**:

- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если не удалось распарсить JSON данные или записать их в XLS файл.

**Как работает функция**:

1.  Функция `json2xls` принимает JSON данные и путь к XLS файлу.
2.  Вызывает функцию `save_xls_file` из модуля `src.utils.xls` для сохранения данных в XLS файл.
3.  Возвращает результат выполнения функции `save_xls_file`.

```
JSON Data --> [save_xls_file] --> XLS File
```

**Примеры**:

```python
from pathlib import Path

# Пример 1: Преобразование JSON строки в XLS файл
json_string = '[{"name": "Иван", "age": 30}, {"name": "Мария", "age": 25}]'
xls_file = 'data.xls'
result = json2xls(json_string, xls_file)
print(f"Результат преобразования JSON строки в XLS: {result}")  # Вывод: Результат преобразования JSON строки в XLS: True

# Пример 2: Преобразование JSON файла в XLS файл
json_file = Path('data.json')
# Предположим, что data.json содержит: [{"name": "Иван", "age": 30}, {"name": "Мария", "age": 25}]
xls_file = 'data_from_file.xls'
result = json2xls(json_file, xls_file)
print(f"Результат преобразования JSON файла в XLS: {result}")  # Вывод: Результат преобразования JSON файла в XLS: True