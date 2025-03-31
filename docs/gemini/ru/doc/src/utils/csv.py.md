# Модуль `src.utils.csv`

## Обзор

Модуль `src.utils.csv` предоставляет утилиты для работы с файлами CSV и JSON. Он включает в себя функции для сохранения данных в формате CSV, чтения CSV-файлов, конвертации CSV в JSON и чтения CSV в различные структуры данных, такие как списки словарей и словари.

## Подробней

Этот модуль предназначен для упрощения операций чтения и записи данных в форматах CSV и JSON. Он использует стандартные библиотеки `csv` и `json`, а также библиотеку `pandas` для более удобной работы с данными. Модуль предоставляет функции для сохранения и чтения CSV-файлов, а также для преобразования CSV-файлов в формат JSON. Он также включает функции для чтения CSV-файлов в различные структуры данных, такие как списки словарей и словари. Модуль активно использует логирование через модуль `src.logger.logger` для записи информации об ошибках и исключениях.

## Функции

### `save_csv_file`

```python
def save_csv_file(
    data: List[Dict[str, str]],
    file_path: Union[str, Path],
    mode: str = 'a',
    exc_info: bool = True,
) -> bool:
    """    Saves a list of dictionaries to a CSV file.

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
Функция `save_csv_file` сохраняет список словарей в CSV-файл. Она принимает список словарей `data`, путь к файлу `file_path` и режим записи `mode`. Если режим записи `'w'` или файл не существует, функция записывает заголовок CSV-файла. Затем она записывает данные в файл. Функция обрабатывает исключения и логирует ошибки с использованием модуля `logger`.
**Параметры**:

- `data` (List[Dict[str, str]]): Список словарей для сохранения в CSV-файл. Каждый словарь представляет строку в CSV-файле, где ключи словаря становятся заголовками столбцов.
- `file_path` (Union[str, Path]): Путь к CSV-файлу, в который будут сохранены данные. Может быть строкой или объектом `Path`.
- `mode` (str, optional): Режим открытия файла. `'a'` означает добавление в конец файла, `'w'` - перезапись файла. По умолчанию `'a'`.
- `exc_info` (bool, optional): Определяет, следует ли включать информацию об исключении в логи. По умолчанию `True`.

**Возвращает**:

- `bool`: `True`, если данные успешно сохранены в файл, `False` в случае ошибки.

**Вызывает исключения**:

- `TypeError`: Если входные данные `data` не являются списком словарей.
- `ValueError`: Если входной список `data` пуст.

**Примеры**:

```python
data = [{'name': 'John', 'age': '30'}, {'name': 'Jane', 'age': '25'}]
file_path = 'output.csv'
result = save_csv_file(data, file_path, mode='w')
print(result)  # Вывод: True
```

### `read_csv_file`

```python
def read_csv_file(file_path: Union[str, Path], exc_info: bool = True) -> List[Dict[str, str]] | None:
    """    Reads CSV content as a list of dictionaries.

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
Функция `read_csv_file` читает содержимое CSV-файла и возвращает его в виде списка словарей. Она использует `csv.DictReader` для чтения файла и преобразует каждую строку в словарь. Функция обрабатывает исключения `FileNotFoundError` и `Exception` и логирует ошибки с использованием модуля `logger`.
**Параметры**:

- `file_path` (Union[str, Path]): Путь к CSV-файлу, который нужно прочитать. Может быть строкой или объектом `Path`.
- `exc_info` (bool, optional): Определяет, следует ли включать информацию об исключении в логи. По умолчанию `True`.

**Возвращает**:

- `List[Dict[str, str]] | None`: Список словарей, где каждый словарь представляет строку из CSV-файла, или `None`, если произошла ошибка при чтении файла.

**Вызывает исключения**:

- `FileNotFoundError`: Если файл, указанный в `file_path`, не найден.

**Примеры**:

```python
file_path = 'output.csv'
data = read_csv_file(file_path)
if data:
    print(data)
else:
    print("Failed to read CSV file.")
```

### `read_csv_as_json`

```python
def read_csv_as_json(csv_file_path: Union[str, Path], json_file_path: Union[str, Path], exc_info: bool = True) -> bool:
    """    Convert a CSV file to JSON format and save it.

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
Функция `read_csv_as_json` преобразует CSV-файл в формат JSON и сохраняет его в указанный файл. Она использует `read_csv_file` для чтения данных из CSV-файла, а затем записывает эти данные в JSON-файл с отступом 4 для удобочитаемости. Функция обрабатывает исключения и логирует ошибки с использованием модуля `logger`.
**Параметры**:

- `csv_file_path` (Union[str, Path]): Путь к CSV-файлу, который нужно преобразовать. Может быть строкой или объектом `Path`.
- `json_file_path` (Union[str, Path]): Путь к файлу, в который будет сохранен JSON. Может быть строкой или объектом `Path`.
- `exc_info` (bool, optional): Определяет, следует ли включать информацию об исключении в логи. По умолчанию `True`.

**Возвращает**:

- `bool`: `True`, если преобразование и сохранение прошли успешно, `False` в случае ошибки.

**Примеры**:

```python
csv_file_path = 'output.csv'
json_file_path = 'output.json'
result = read_csv_as_json(csv_file_path, json_file_path)
print(result)  # Вывод: True
```

### `read_csv_as_dict`

```python
def read_csv_as_dict(csv_file: Union[str, Path]) -> dict | None:
    """    Convert CSV content to a dictionary.

    Args:
        csv_file (Union[str, Path]): Path to the CSV file.

    Returns:
        dict | None: Dictionary representation of CSV content, or None if failed.
    """
    ...
```

**Как работает функция**:
Функция `read_csv_as_dict` читает содержимое CSV-файла и возвращает его в виде словаря, где ключ `"data"` содержит список словарей, представляющих строки CSV-файла. Она использует `csv.DictReader` для чтения файла и преобразует каждую строку в словарь. Функция обрабатывает исключения и логирует ошибки с использованием модуля `logger`.
**Параметры**:

- `csv_file` (Union[str, Path]): Путь к CSV-файлу, который нужно прочитать. Может быть строкой или объектом `Path`.

**Возвращает**:

- `dict | None`: Словарь, содержащий ключ `"data"` со списком словарей, представляющих содержимое CSV-файла, или `None`, если произошла ошибка при чтении файла.

**Примеры**:

```python
csv_file = 'output.csv'
data = read_csv_as_dict(csv_file)
if data:
    print(data)
else:
    print("Failed to read CSV file.")
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
Функция `read_csv_as_ns` загружает данные из CSV-файла в список словарей, используя библиотеку `pandas`. Она читает CSV-файл с помощью `pd.read_csv` и преобразует его в список словарей с помощью `df.to_dict(orient='records')`. Функция обрабатывает исключения `FileNotFoundError` и `Exception` и логирует ошибки с использованием модуля `logger`.
**Параметры**:

- `file_path` (Union[str, Path]): Путь к CSV-файлу, который нужно прочитать. Может быть строкой или объектом `Path`.

**Возвращает**:

- `List[dict]`: Список словарей, где каждый словарь представляет строку из CSV-файла. Возвращает пустой список, если произошла ошибка при чтении файла.

**Вызывает исключения**:

- `FileNotFoundError`: Если файл, указанный в `file_path`, не найден.

**Примеры**:

```python
file_path = 'output.csv'
data = read_csv_as_ns(file_path)
print(data)