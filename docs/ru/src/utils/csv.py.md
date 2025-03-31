# Модуль для работы с CSV и JSON файлами

## Обзор

Модуль `src.utils.csv` предоставляет набор утилит для работы с CSV и JSON файлами. Он включает функции для сохранения данных в формате CSV, чтения данных из CSV файлов, конвертации CSV в JSON и представления CSV в виде словаря. Модуль использует библиотеки `csv`, `json`, `pathlib` и `pandas` для обеспечения функциональности.

## Подробнее

Этот модуль предназначен для упрощения операций чтения и записи данных в форматах CSV и JSON. Он предоставляет удобные функции для работы с файлами, включая автоматическое создание директорий, обработку ошибок и логирование. Функции модуля позволяют легко конвертировать данные между различными форматами, что полезно для интеграции с другими системами и приложениями.  Анализируя код можно сказать, что модуль широко используется для обработки и хранения структурированных данных в проекте.

## Содержание

- [Функции](#Функции)
    - [save_csv_file](#save_csv_file)
    - [read_csv_file](#read_csv_file)
    - [read_csv_as_json](#read_csv_as_json)
    - [read_csv_as_dict](#read_csv_as_dict)
    - [read_csv_as_ns](#read_csv_as_ns)

## Функции

### `save_csv_file`

```python
def save_csv_file(
    data: List[Dict[str, str]],
    file_path: Union[str, Path],
    mode: str = 'a',
    exc_info: bool = True,
) -> bool:
    """ Saves a list of dictionaries to a CSV file.

    Args:
        data (List[Dict[str, str]]): List of dictionaries to save.
        file_path (Union[str, Path]): Path to the CSV file.
        mode (str): File mode ('a' to append, 'w' to overwrite). Default is 'a'.
        exc_info (bool): Include traceback information in logs.

    Returns:
        bool: True if successful, otherwise False.

    Raises:
        TypeError: If input data is not a list of dictionaries.
        ValueError: If input data is empty.
    """
    ...
```

**Как работает функция**:
Функция `save_csv_file` сохраняет список словарей в CSV файл. Она принимает данные, путь к файлу и режим записи в качестве аргументов. Сначала функция проверяет, что входные данные являются списком словарей и не пусты. Затем она создает необходимые директории, если их нет, и открывает файл в указанном режиме (добавление или перезапись). Используя `csv.DictWriter`, функция записывает заголовки столбцов (если файл создается или перезаписывается) и данные в файл. В случае возникновения исключений, функция логирует ошибку и возвращает `False`.

**Параметры**:
- `data` (List[Dict[str, str]]): Список словарей для сохранения в CSV файл. Каждый словарь представляет строку данных, где ключи словаря становятся заголовками столбцов.
- `file_path` (Union[str, Path]): Путь к CSV файлу, в который будут сохранены данные.  Путь может быть указан как строкой, так и объектом `Path`.
- `mode` (str, optional): Режим открытия файла. `'a'` - для добавления данных в конец файла, `'w'` - для перезаписи файла. По умолчанию `'a'`.
- `exc_info` (bool, optional):  Указывает, следует ли включать информацию об исключении (traceback) в логи. По умолчанию `True`.

**Возвращает**:
- `bool`: `True`, если запись в файл прошла успешно, `False` в случае ошибки.

**Вызывает исключения**:
- `TypeError`: Если входные данные (`data`) не являются списком словарей.
- `ValueError`: Если входные данные (`data`) пустые.

**Примеры**:

```python
from pathlib import Path
from src.utils.csv import save_csv_file

# Пример данных
data = [{'name': 'John', 'age': '30'}, {'name': 'Jane', 'age': '25'}]

# Пример сохранения в файл
file_path = Path('example.csv')
result = save_csv_file(data, file_path, mode='w')
print(f"CSV file saved successfully: {result}")

# Пример добавления данных в файл
new_data = [{'name': 'Mike', 'age': '40'}]
result = save_csv_file(new_data, file_path, mode='a')
print(f"CSV file appended successfully: {result}")
```

### `read_csv_file`

```python
def read_csv_file(file_path: Union[str, Path], exc_info: bool = True) -> List[Dict[str, str]] | None:
    """ Reads CSV content as a list of dictionaries.

    Args:
        file_path (Union[str, Path]): Path to the CSV file.
        exc_info (bool): Include traceback information in logs.

    Returns:
        List[Dict[str, str]] | None: List of dictionaries or None if failed.

    Raises:
        FileNotFoundError: If file not found.
    """
    ...
```

**Как работает функция**:
Функция `read_csv_file` читает содержимое CSV файла и возвращает его в виде списка словарей. Каждый словарь представляет строку данных, где ключи словаря соответствуют заголовкам столбцов. Функция открывает файл в режиме чтения, использует `csv.DictReader` для чтения данных и преобразует их в список словарей. В случае, если файл не найден или возникает другая ошибка, функция логирует ошибку и возвращает `None`.

**Параметры**:
- `file_path` (Union[str, Path]): Путь к CSV файлу, который необходимо прочитать. Путь может быть указан как строкой, так и объектом `Path`.
- `exc_info` (bool, optional): Указывает, следует ли включать информацию об исключении (traceback) в логи. По умолчанию `True`.

**Возвращает**:
- `List[Dict[str, str]] | None`: Список словарей, представляющий содержимое CSV файла. Возвращает `None`, если файл не найден или произошла ошибка при чтении.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден по указанному пути.

**Примеры**:

```python
from pathlib import Path
from src.utils.csv import read_csv_file

# Пример чтения файла
file_path = Path('example.csv')
data = read_csv_file(file_path)

if data:
    print(f"CSV file content: {data}")
else:
    print("Failed to read CSV file.")
```

### `read_csv_as_json`

```python
def read_csv_as_json(csv_file_path: Union[str, Path], json_file_path: Union[str, Path], exc_info: bool = True) -> bool:
    """ Convert a CSV file to JSON format and save it.

    Args:
        csv_file_path (Union[str, Path]): Path to the CSV file.
        json_file_path (Union[str, Path]): Path to save the JSON file.
        exc_info (bool): Include traceback information in logs.

    Returns:
        bool: True if conversion is successful, else False.
    """
    ...
```

**Как работает функция**:
Функция `read_csv_as_json` конвертирует CSV файл в JSON формат и сохраняет его в указанный файл. Она сначала читает данные из CSV файла с помощью функции `read_csv_file`, а затем записывает эти данные в JSON файл с отступами для улучшения читаемости. Если чтение CSV файла не удается, функция возвращает `False`. В случае возникновения исключений, функция логирует ошибку и возвращает `False`.

**Параметры**:
- `csv_file_path` (Union[str, Path]): Путь к CSV файлу, который необходимо конвертировать.  Путь может быть указан как строкой, так и объектом `Path`.
- `json_file_path` (Union[str, Path]): Путь к JSON файлу, в который будут сохранены конвертированные данные.  Путь может быть указан как строкой, так и объектом `Path`.
- `exc_info` (bool, optional): Указывает, следует ли включать информацию об исключении (traceback) в логи. По умолчанию `True`.

**Возвращает**:
- `bool`: `True`, если конвертация и сохранение прошли успешно, `False` в случае ошибки.

**Примеры**:

```python
from pathlib import Path
from src.utils.csv import read_csv_as_json

# Пример конвертации CSV в JSON
csv_file_path = Path('example.csv')
json_file_path = Path('example.json')
result = read_csv_as_json(csv_file_path, json_file_path)

print(f"CSV to JSON conversion successful: {result}")
```

### `read_csv_as_dict`

```python
def read_csv_as_dict(csv_file: Union[str, Path]) -> dict | None:
    """ Convert CSV content to a dictionary.

    Args:
        csv_file (Union[str, Path]): Path to the CSV file.

    Returns:
        dict | None: Dictionary representation of CSV content, or None if failed.
    """
    ...
```

**Как работает функция**:
Функция `read_csv_as_dict` читает содержимое CSV файла и возвращает его в виде словаря, где ключ `"data"` содержит список словарей, представляющих строки CSV файла. Функция открывает файл в режиме чтения, использует `csv.DictReader` для чтения данных и формирует словарь. В случае возникновения исключений, функция логирует ошибку и возвращает `None`.

**Параметры**:
- `csv_file` (Union[str, Path]): Путь к CSV файлу, который необходимо прочитать. Путь может быть указан как строкой, так и объектом `Path`.

**Возвращает**:
- `dict | None`: Словарь, содержащий CSV данные, или `None`, если произошла ошибка.  Словарь имеет структуру `{"data": [список словарей]}`.

**Примеры**:

```python
from pathlib import Path
from src.utils.csv import read_csv_as_dict

# Пример чтения CSV в словарь
csv_file_path = Path('example.csv')
data = read_csv_as_dict(csv_file_path)

if data:
    print(f"CSV file content as dictionary: {data}")
else:
    print("Failed to read CSV file as dictionary.")
```

### `read_csv_as_ns`

```python
def read_csv_as_ns(file_path: Union[str, Path]) -> List[dict]:
    """!
    Load CSV data into a list of dictionaries using Pandas.

    Args:
        file_path (Union[str, Path]): Path to the CSV file.

    Returns:
        List[dict]: List of dictionaries representing the CSV content.

    Raises:
        FileNotFoundError: If file not found.
    """
    ...
```

**Как работает функция**:
Функция `read_csv_as_ns` читает содержимое CSV файла, используя библиотеку `pandas`, и возвращает его в виде списка словарей. Она использует `pd.read_csv` для чтения CSV файла в DataFrame, а затем преобразует DataFrame в список словарей с помощью `df.to_dict(orient='records')`. В случае, если файл не найден, функция логирует ошибку и возвращает пустой список. В случае возникновения других исключений, функция также логирует ошибку и возвращает пустой список.

**Параметры**:
- `file_path` (Union[str, Path]): Путь к CSV файлу, который необходимо прочитать. Путь может быть указан как строкой, так и объектом `Path`.

**Возвращает**:
- `List[dict]`: Список словарей, представляющий содержимое CSV файла. Возвращает пустой список, если файл не найден или произошла ошибка при чтении.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден по указанному пути.

**Примеры**:

```python
from pathlib import Path
from src.utils.csv import read_csv_as_ns

# Пример чтения CSV в список словарей с использованием pandas
csv_file_path = Path('example.csv')
data = read_csv_as_ns(csv_file_path)

print(f"CSV file content as list of dictionaries: {data}")