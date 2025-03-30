# Модуль для работы с CSV и JSON файлами
## Обзор

Модуль `src.utils.csv` предоставляет набор утилит для работы с CSV и JSON файлами. Он включает в себя функции для сохранения данных в формате CSV, чтения данных из CSV файлов, конвертации CSV в JSON и представления CSV в виде словаря.

## Подробней

Этот модуль предоставляет инструменты для эффективной работы с CSV и JSON файлами. Он включает функции для сохранения данных в формате CSV, чтения данных из CSV файлов, конвертации CSV в JSON и представления CSV в виде словаря. Модуль использует библиотеку `pandas` для обработки данных в формате CSV, что обеспечивает высокую производительность и удобство использования. Расположение файла в проекте `hypotez` указывает на его использование в качестве утилиты для обработки данных в формате CSV и JSON.

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
```

**Описание**: Сохраняет список словарей в CSV файл.

**Параметры**:

- `data` (List[Dict[str, str]]): Список словарей для сохранения.
- `file_path` (Union[str, Path]): Путь к CSV файлу.
- `mode` (str, optional): Режим файла ('a' для добавления, 'w' для перезаписи). По умолчанию 'a'.
- `exc_info` (bool, optional): Включать ли информацию трассировки в логи. По умолчанию `True`.

**Возвращает**:

- `bool`: `True`, если успешно, иначе `False`.

**Вызывает исключения**:

- `TypeError`: Если входные данные не являются списком словарей.
- `ValueError`: Если входные данные пусты.

**Примеры**:

```python
data = [{'col1': 'data1', 'col2': 'data2'}, {'col1': 'data3', 'col2': 'data4'}]
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
```

**Описание**: Читает содержимое CSV файла в виде списка словарей.

**Параметры**:

- `file_path` (Union[str, Path]): Путь к CSV файлу.
- `exc_info` (bool, optional): Включать ли информацию трассировки в логи. По умолчанию `True`.

**Возвращает**:

- `List[Dict[str, str]] | None`: Список словарей или `None`, если не удалось.

**Вызывает исключения**:

- `FileNotFoundError`: Если файл не найден.

**Примеры**:

```python
file_path = 'output.csv'
data = read_csv_file(file_path)
if data:
    print(data)  # Вывод: [{'col1': 'data1', 'col2': 'data2'}, {'col1': 'data3', 'col2': 'data4'}]
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
```

**Описание**: Конвертирует CSV файл в формат JSON и сохраняет его.

**Параметры**:

- `csv_file_path` (Union[str, Path]): Путь к CSV файлу.
- `json_file_path` (Union[str, Path]): Путь для сохранения JSON файла.
- `exc_info` (bool, optional): Включать ли информацию трассировки в логи. По умолчанию `True`.

**Возвращает**:

- `bool`: `True`, если преобразование успешно, иначе `False`.

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
```

**Описание**: Конвертирует содержимое CSV файла в словарь.

**Параметры**:

- `csv_file` (Union[str, Path]): Путь к CSV файлу.

**Возвращает**:

- `dict | None`: Словарь, представляющий содержимое CSV файла, или `None`, если не удалось.

**Примеры**:

```python
csv_file_path = 'output.csv'
data = read_csv_as_dict(csv_file_path)
if data:
    print(data)  # Вывод: {'data': [{'col1': 'data1', 'col2': 'data2'}, {'col1': 'data3', 'col2': 'data4'}]}
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

**Описание**: Загружает данные из CSV файла в список словарей, используя библиотеку Pandas.

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
print(data)  # Вывод: [{'col1': 'data1', 'col2': 'data2'}, {'col1': 'data3', 'col2': 'data4'}]