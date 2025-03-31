# Модуль `csv`

## Обзор

Модуль `csv` предоставляет утилиты для конвертации данных между форматами CSV и JSON. Он содержит функции для чтения данных из CSV-файлов и преобразования их в словари или объекты SimpleNamespace, а также функцию для конвертации CSV-файла в JSON-формат и сохранения его в файл.

## Подробней

Этот модуль предназначен для упрощения работы с данными, хранящимися в формате CSV, и их преобразования в другие форматы, такие как JSON. Он предоставляет удобные функции для чтения данных из CSV-файлов, преобразования их в словари или объекты SimpleNamespace, а также для конвертации CSV-файлов в JSON-формат и сохранения их в файл. Модуль использует стандартные библиотеки `json` и `csv`, а также модуль `logger` для логирования ошибок.

## Функции

### `csv2dict`

```python
def csv2dict(csv_file: str | Path, *args, **kwargs) -> dict | None:
    """
    Convert CSV data to a dictionary.

    Args:
        csv_file (str | Path): Path to the CSV file to read.

    Returns:
        dict | None: Dictionary containing the data from CSV converted to JSON format, or `None` if conversion failed.

    Raises:
        Exception: If unable to read CSV.
    """
```

**Описание**: Преобразует данные из CSV-файла в словарь.

**Как работает функция**: Функция `csv2dict` принимает путь к CSV-файлу и передает его функции `read_csv_as_dict` из модуля `src.utils.csv`. Она возвращает словарь, содержащий данные из CSV-файла, или `None`, если преобразование не удалось.

**Параметры**:
- `csv_file` (str | Path): Путь к CSV-файлу для чтения.
- `*args`: Произвольные позиционные аргументы, передаваемые в `read_csv_as_dict`.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в `read_csv_as_dict`.

**Возвращает**:
- `dict | None`: Словарь, содержащий данные из CSV, или `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Возникает, если не удается прочитать CSV-файл.

**Примеры**:

```python
# from src.utils.convertors.csv import csv2dict
# csv_data = csv2dict('data.csv')
# if csv_data:
#     print(csv_data)
```

### `csv2ns`

```python
def csv2ns(csv_file: str | Path, *args, **kwargs) -> SimpleNamespace | None:
    """
    Convert CSV data to SimpleNamespace objects.

    Args:
        csv_file (str | Path): Path to the CSV file to read.

    Returns:
        SimpleNamespace | None: SimpleNamespace object containing the data from CSV, or `None` if conversion failed.

    Raises:
        Exception: If unable to read CSV.
    """
```

**Описание**: Преобразует данные из CSV-файла в объект SimpleNamespace.

**Как работает функция**: Функция `csv2ns` принимает путь к CSV-файлу и передает его функции `read_csv_as_ns` из модуля `src.utils.csv`. Она возвращает объект SimpleNamespace, содержащий данные из CSV-файла, или `None`, если преобразование не удалось.

**Параметры**:
- `csv_file` (str | Path): Путь к CSV-файлу для чтения.
- `*args`: Произвольные позиционные аргументы, передаваемые в `read_csv_as_ns`.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в `read_csv_as_ns`.

**Возвращает**:
- `SimpleNamespace | None`: Объект SimpleNamespace, содержащий данные из CSV, или `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Возникает, если не удается прочитать CSV-файл.

**Примеры**:

```python
# from src.utils.convertors.csv import csv2ns
# csv_data = csv2ns('data.csv')
# if csv_data:
#     print(csv_data)
```

### `csv_to_json`

```python
def csv_to_json(
    csv_file_path: str | Path,
    json_file_path: str | Path,
    exc_info: bool = True
) -> List[Dict[str, str]] | None:
    """ Convert a CSV file to JSON format and save it to a JSON file.

    Args:
        csv_file_path (str | Path): The path to the CSV file to read.
        json_file_path (str | Path): The path to the JSON file to save.
        exc_info (bool, optional): If True, includes traceback information in the log. Defaults to True.

    Returns:
        List[Dict[str, str]] | None: The JSON data as a list of dictionaries, or None if conversion failed.

    Example:
        >>> json_data = csv_to_json('dialogue_log.csv', 'dialogue_log.json')
        >>> print(json_data)
        [{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]
    """
```

**Описание**: Преобразует CSV-файл в JSON-формат и сохраняет его в JSON-файл.

**Как работает функция**: 
1. Функция `csv_to_json` принимает пути к CSV- и JSON-файлам, а также флаг `exc_info` для логирования информации об исключениях.
2. Она вызывает функцию `read_csv_file` из модуля `src.utils.csv` для чтения данных из CSV-файла.
3. Если данные успешно прочитаны, они записываются в JSON-файл с использованием отступов для удобочитаемости.
4. В случае возникновения исключений, они логируются с использованием `logger.error`, и возвращается `None`.

**Параметры**:
- `csv_file_path` (str | Path): Путь к CSV-файлу для чтения.
- `json_file_path` (str | Path): Путь к JSON-файлу для сохранения.
- `exc_info` (bool, optional): Если `True`, включает информацию об исключении в лог. По умолчанию `True`.

**Возвращает**:
- `List[Dict[str, str]] | None`: JSON-данные в виде списка словарей или `None`, если преобразование не удалось.

**Вызывает исключения**:
- Отсутствуют явные исключения, но функция логирует любые исключения, возникающие в процессе преобразования.

**Примеры**:

```python
# from src.utils.convertors.csv import csv_to_json
# json_data = csv_to_json('dialogue_log.csv', 'dialogue_log.json')
# if json_data:
#     print(json_data)
```