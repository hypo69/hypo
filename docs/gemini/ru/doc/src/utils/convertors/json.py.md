# Модуль для преобразования JSON данных в различные форматы
=============================================================

Модуль `src.utils.convertors.json` предназначен для преобразования JSON данных в различные форматы, такие как CSV, SimpleNamespace, XML и XLS.

## Обзор

Модуль предоставляет функции для преобразования JSON данных или JSON файлов в различные форматы. Это может быть полезно для экспорта данных из JSON в другие форматы для дальнейшей обработки или анализа.
Модуль содержит следующие функции:
- `json2csv`: Преобразует JSON данные в формат CSV.
- `json2ns`: Преобразует JSON данные в объект SimpleNamespace.
- `json2xml`: Преобразует JSON данные в формат XML.
- `json2xls`: Преобразует JSON данные в формат XLS.

## Подробнее

Модуль содержит функции, которые позволяют преобразовывать JSON данные в другие форматы. Каждая функция принимает JSON данные в виде строки, словаря, списка или пути к файлу, а также путь к файлу, в который будет сохранен результат преобразования.

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

**Назначение**: Преобразует JSON данные или JSON файл в формат CSV с использованием запятой в качестве разделителя.

**Параметры**:
- `json_data` (str | list | dict | Path): JSON данные в виде строки, списка словарей или пути к JSON файлу.
- `csv_file_path` (str | Path): Путь к CSV файлу, в который будут записаны данные.

**Возвращает**:
- `bool`: `True`, если преобразование прошло успешно, `False` в противном случае.

**Вызывает исключения**:
- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если не удается распарсить JSON или записать CSV.

**Как работает функция**:

1.  **Определение типа входных данных**: Функция определяет, какой тип данных был передан в качестве `json_data` (словарь, строка, список или путь к файлу).
2.  **Чтение JSON данных**: В зависимости от типа входных данных, функция загружает JSON данные. Если `json_data` это строка, она парсится с использованием `json.loads()`. Если это путь к файлу, файл открывается, и JSON данные загружаются из него.
3.  **Преобразование в CSV**: Функция вызывает `save_csv_file` для сохранения полученных данных в CSV файл.
4.  **Обработка ошибок**: Если в процессе преобразования возникают ошибки, они логируются с использованием `logger.error`, и функция возвращает `False`.

```
    json_data (str | list | dict | Path) --> [isinstance(json_data, dict)?] --> data = [json_data]
                                           |   [isinstance(json_data, str)?]  --> data = json.loads(json_data)
                                           |   [isinstance(json_data, list)?] --> data = json_data
                                           |   [isinstance(json_data, Path)?] --> open(json_data) --> data = json.load(json_file)
                                           |   [else]                        --> raise ValueError("Unsupported type for json_data")
                                           ↓
    save_csv_file(data, csv_file_path)
    ↓
    return True
```

**Примеры**:

```python
from pathlib import Path
import json
# Пример 1: Преобразование JSON строки в CSV файл
json_string = '[{"name": "Иван", "age": 30}, {"name": "Петр", "age": 25}]'
csv_file = 'output.csv'
result = json2csv(json_string, csv_file)
print(f"Результат преобразования: {result}")  # Вывод: Результат преобразования: True

# Пример 2: Преобразование JSON файла в CSV файл
json_file_path = Path('data.json')
with open(json_file_path, 'w', encoding='utf-8') as f:
    json.dump([{"name": "Иван", "age": 30}, {"name": "Петр", "age": 25}], f)
csv_file_path = 'output.csv'
result = json2csv(json_file_path, csv_file_path)
print(f"Результат преобразования: {result}")  # Вывод: Результат преобразования: True

# Пример 3: Преобразование списка словарей в CSV файл
json_list = [{"name": "Иван", "age": 30}, {"name": "Петр", "age": 25}]
csv_file_path = 'output.csv'
result = json2csv(json_list, csv_file_path)
print(f"Результат преобразования: {result}")  # Вывод: Результат преобразования: True

# Пример 4: Преобразование словаря в CSV файл
json_dict = {"name": "Иван", "age": 30}
csv_file_path = 'output.csv'
result = json2csv(json_dict, csv_file_path)
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

**Назначение**: Преобразует JSON данные или JSON файл в объект `SimpleNamespace`.

**Параметры**:
- `json_data` (str | dict | Path): JSON данные в виде строки, словаря или пути к JSON файлу.

**Возвращает**:
- `SimpleNamespace`: Объект `SimpleNamespace`, представляющий JSON данные.

**Вызывает исключения**:
- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если не удается распарсить JSON.

**Как работает функция**:

1.  **Определение типа входных данных**: Функция определяет, какой тип данных был передан в качестве `json_data` (словарь, строка или путь к файлу).
2.  **Чтение JSON данных**: В зависимости от типа входных данных, функция загружает JSON данные. Если `json_data` это строка, она парсится с использованием `json.loads()`. Если это путь к файлу, файл открывается, и JSON данные загружаются из него.
3.  **Преобразование в SimpleNamespace**: Функция преобразует JSON данные в объект `SimpleNamespace` с использованием оператора `**`.
4.  **Обработка ошибок**: Если в процессе преобразования возникают ошибки, они логируются с использованием `logger.error`.

```
    json_data (str | dict | Path) --> [isinstance(json_data, dict)?] --> data = json_data
                                           |   [isinstance(json_data, str)?]  --> data = json.loads(json_data)
                                           |   [isinstance(json_data, Path)?] --> open(json_data) --> data = json.load(json_file)
                                           |   [else]                        --> raise ValueError("Unsupported type for json_data")
                                           ↓
    return SimpleNamespace(**data)
```

**Примеры**:

```python
from pathlib import Path
import json
# Пример 1: Преобразование JSON строки в SimpleNamespace
json_string = '{"name": "Иван", "age": 30}'
result = json2ns(json_string)
print(f"Имя: {result.name}, Возраст: {result.age}")  # Вывод: Имя: Иван, Возраст: 30

# Пример 2: Преобразование JSON файла в SimpleNamespace
json_file_path = Path('data.json')
with open(json_file_path, 'w', encoding='utf-8') as f:
    json.dump({"name": "Иван", "age": 30}, f)
result = json2ns(json_file_path)
print(f"Имя: {result.name}, Возраст: {result.age}")  # Вывод: Имя: Иван, Возраст: 30

# Пример 3: Преобразование словаря в SimpleNamespace
json_dict = {"name": "Иван", "age": 30}
result = json2ns(json_dict)
print(f"Имя: {result.name}, Возраст: {result.age}")  # Вывод: Имя: Иван, Возраст: 30
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

**Назначение**: Преобразует JSON данные или JSON файл в формат XML.

**Параметры**:
- `json_data` (str | dict | Path): JSON данные в виде строки, словаря или пути к JSON файлу.
- `root_tag` (str): Корневой элемент для XML. По умолчанию "root".

**Возвращает**:
- `str`: Строка, представляющая XML.

**Вызывает исключения**:
- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если не удается распарсить JSON или преобразовать в XML.

**Как работает функция**:

Функция вызывает `dict2xml` для преобразования JSON данных в XML.

```
    json_data (str | dict | Path), root_tag (str) --> dict2xml(json_data, root_tag)
    ↓
    return xml_string
```

**Примеры**:

```python
from pathlib import Path
import json

# Пример 1: Преобразование JSON строки в XML
json_string = '{"name": "Иван", "age": 30}'
result = json2xml(json_string)
print(f"XML: {result}")

# Пример 2: Преобразование JSON файла в XML
json_file_path = Path('data.json')
with open(json_file_path, 'w', encoding='utf-8') as f:
    json.dump({"name": "Иван", "age": 30}, f)
result = json2xml(json_file_path)
print(f"XML: {result}")

# Пример 3: Преобразование словаря в XML
json_dict = {"name": "Иван", "age": 30}
result = json2xml(json_dict)
print(f"XML: {result}")
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

**Назначение**: Преобразует JSON данные или JSON файл в формат XLS.

**Параметры**:
- `json_data` (str | list | dict | Path): JSON данные в виде строки, списка словарей или пути к JSON файлу.
- `xls_file_path` (str | Path): Путь к XLS файлу, в который будут записаны данные.

**Возвращает**:
- `bool`: `True`, если преобразование прошло успешно, `False` в противном случае.

**Вызывает исключения**:
- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если не удается распарсить JSON или записать XLS.

**Как работает функция**:

Функция вызывает `save_xls_file` для сохранения JSON данных в XLS файл.

```
    json_data (str | list | dict | Path), xls_file_path (str | Path) --> save_xls_file(json_data, xls_file_path)
    ↓
    return True/False
```

**Примеры**:

```python
from pathlib import Path
import json
# Пример 1: Преобразование JSON строки в XLS файл
json_string = '[{"name": "Иван", "age": 30}, {"name": "Петр", "age": 25}]'
xls_file = 'output.xls'
result = json2xls(json_string, xls_file)
print(f"Результат преобразования: {result}")

# Пример 2: Преобразование JSON файла в XLS файл
json_file_path = Path('data.json')
with open(json_file_path, 'w', encoding='utf-8') as f:
    json.dump([{"name": "Иван", "age": 30}, {"name": "Петр", "age": 25}], f)
xls_file_path = 'output.xls'
result = json2xls(json_file_path, xls_file_path)
print(f"Результат преобразования: {result}")

# Пример 3: Преобразование списка словарей в XLS файл
json_list = [{"name": "Иван", "age": 30}, {"name": "Петр", "age": 25}]
xls_file_path = 'output.xls'
result = json2xls(json_list, xls_file_path)
print(f"Результат преобразования: {result}")

# Пример 4: Преобразование словаря в XLS файл
json_dict = {"name": "Иван", "age": 30}
xls_file_path = 'output.xls'
result = json2xls(json_dict, xls_file_path)
print(f"Результат преобразования: {result}")