# Модуль `src.utils.csv`

## Обзор

Модуль `src.utils.csv` предоставляет набор утилит для работы с CSV и JSON файлами. Он включает функции для сохранения данных в CSV файлы, чтения данных из CSV файлов в различных форматах (список словарей, JSON, словарь) и преобразования CSV файлов в JSON формат.

## Подробней

Этот модуль предназначен для облегчения операций чтения и записи данных в формате CSV, а также для преобразования этих данных в формат JSON. Он использует стандартные библиотеки `csv` и `json`, а также библиотеку `pandas` для более удобной работы с данными. Функции модуля обеспечивают гибкость при работе с файлами, позволяя сохранять данные в различных режимах (добавление или перезапись) и читать данные в различных форматах в зависимости от потребностей.
Модуль содержит функции для обработки исключений и логирования ошибок с использованием модуля `src.logger`.

## Функции

### `save_csv_file`

```python
def save_csv_file(
    data: List[Dict[str, str]],
    file_path: Union[str, Path],
    mode: str = 'a',
    exc_info: bool = True,
) -> bool:
    """
    Saves a list of dictionaries to a CSV file.

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
```

**Описание**: Сохраняет список словарей в CSV файл.

**Параметры**:
- `data` (List[Dict[str, str]]): Список словарей для сохранения.
- `file_path` (Union[str, Path]): Путь к CSV файлу.
- `mode` (str, optional): Режим файла ('a' для добавления, 'w' для перезаписи). По умолчанию 'a'.
- `exc_info` (bool, optional): Включать ли информацию трассировки в логи. По умолчанию `True`.

**Возвращает**:
- `bool`: `True`, если сохранение прошло успешно, иначе `False`.

**Вызывает исключения**:
- `TypeError`: Если входные данные не являются списком словарей.
- `ValueError`: Если входные данные пусты.

**Примеры**:

```python
data = [{'name': 'John', 'age': '30'}, {'name': 'Jane', 'age': '25'}]
file_path = 'output.csv'
result = save_csv_file(data, file_path, mode='w')
print(f'CSV file saved successfully: {result}')
```

### `read_csv_file`

```python
def read_csv_file(file_path: Union[str, Path], exc_info: bool = True) -> List[Dict[str, str]] | None:
    """
    Reads CSV content as a list of dictionaries.

    Args:
        file_path (Union[str, Path]): Path to the CSV file.
        exc_info (bool): Include traceback information in logs.

    Returns:
        List[Dict[str, str]] | None: List of dictionaries or None if failed.

    Raises:
        FileNotFoundError: If file not found.
    """
```

**Описание**: Читает содержимое CSV файла и возвращает его в виде списка словарей.

**Параметры**:
- `file_path` (Union[str, Path]): Путь к CSV файлу.
- `exc_info` (bool, optional): Включать ли информацию трассировки в логи. По умолчанию `True`.

**Возвращает**:
- `List[Dict[str, str]] | None`: Список словарей, представляющих содержимое CSV файла, или `None` в случае ошибки.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден.

**Примеры**:

```python
file_path = 'output.csv'
data = read_csv_file(file_path)
if data:
    print(f'CSV file content: {data}')
else:
    print('Failed to read CSV file.')
```

### `read_csv_as_json`

```python
def read_csv_as_json(csv_file_path: Union[str, Path], json_file_path: Union[str, Path], exc_info: bool = True) -> bool:
    """
    Convert a CSV file to JSON format and save it.

    Args:
        csv_file_path (Union[str, Path]): Path to the CSV file.
        json_file_path (Union[str, Path]): Path to save the JSON file.
        exc_info (bool): Include traceback information in logs.

    Returns:
        bool: True if conversion is successful, else False.
    """
```

**Описание**: Преобразует CSV файл в JSON формат и сохраняет его в указанный файл.

**Параметры**:
- `csv_file_path` (Union[str, Path]): Путь к CSV файлу.
- `json_file_path` (Union[str, Path]): Путь для сохранения JSON файла.
- `exc_info` (bool, optional): Включать ли информацию трассировки в логи. По умолчанию `True`.

**Возвращает**:
- `bool`: `True`, если преобразование и сохранение прошли успешно, иначе `False`.

**Примеры**:

```python
csv_file_path = 'output.csv'
json_file_path = 'output.json'
result = read_csv_as_json(csv_file_path, json_file_path)
print(f'CSV file converted to JSON: {result}')
```

### `read_csv_as_dict`

```python
def read_csv_as_dict(csv_file: Union[str, Path]) -> dict | None:
    """
    Convert CSV content to a dictionary.

    Args:
        csv_file (Union[str, Path]): Path to the CSV file.

    Returns:
        dict | None: Dictionary representation of CSV content, or None if failed.
    """
```

**Описание**: Читает содержимое CSV файла и возвращает его в виде словаря, где ключ `"data"` содержит список словарей, представляющих строки CSV файла.

**Параметры**:
- `csv_file` (Union[str, Path]): Путь к CSV файлу.

**Возвращает**:
- `dict | None`: Словарь, представляющий содержимое CSV файла, или `None` в случае ошибки.

**Примеры**:

```python
csv_file_path = 'output.csv'
data = read_csv_as_dict(csv_file_path)
if data:
    print(f'CSV file content as dict: {data}')
else:
    print('Failed to read CSV file as dict.')
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
```

**Описание**: Загружает данные из CSV файла в список словарей, используя библиотеку `pandas`.

**Параметры**:
- `file_path` (Union[str, Path]): Путь к CSV файлу.

**Возвращает**:
- `List[dict]`: Список словарей, представляющих содержимое CSV файла.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден.

**Примеры**:

```python
file_path = 'output.csv'
data = read_csv_as_ns(file_path)
print(f'CSV file content as list of dicts (using Pandas): {data}')