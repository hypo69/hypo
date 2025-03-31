# Модуль `csv`

## Обзор

Модуль `csv` предоставляет утилиты для конвертации данных между форматами CSV и JSON. Он включает функции для чтения CSV-файлов и преобразования их в словари или объекты SimpleNamespace, а также для сохранения данных в формате JSON.

## Подробней

Этот модуль предназначен для облегчения обмена данными между CSV-файлами и структурами данных Python, такими как словари и объекты SimpleNamespace. Он предоставляет удобные функции для чтения CSV-файлов, преобразования данных и сохранения их в формате JSON. Модуль использует внутренние функции из `src.utils.csv` для работы с CSV-файлами и `src.logger.logger` для логирования ошибок.

## Функции

### `csv2dict`

```python
def csv2dict(csv_file: str | Path, *args, **kwargs) -> dict | None:
    """
    Args:
        csv_file (str | Path): Путь к CSV-файлу для чтения.

    Returns:
        dict | None: Словарь, содержащий данные из CSV, преобразованные в формат JSON, или `None`, если преобразование не удалось.

    Raises:
        Exception: Если не удается прочитать CSV.

     **Как работает функция**:

     Функция `csv2dict` принимает путь к CSV-файлу и использует функцию `read_csv_as_dict` для чтения данных из этого файла и преобразования их в словарь. Если чтение и преобразование проходят успешно, функция возвращает полученный словарь. В случае возникновения ошибки, функция возвращает `None`.
    """
```

**Описание**: Преобразует данные из CSV-файла в словарь.

**Параметры**:
- `csv_file` (str | Path): Путь к CSV-файлу для чтения.
- `*args`: Произвольные позиционные аргументы, передаваемые в `read_csv_as_dict`.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в `read_csv_as_dict`.

**Возвращает**:
- `dict | None`: Словарь, содержащий данные из CSV, или `None`, если преобразование не удалось.

**Вызывает исключения**:
- `Exception`: Если не удается прочитать CSV-файл.

### `csv2ns`

```python
def csv2ns(csv_file: str | Path, *args, **kwargs) -> SimpleNamespace | None:
    """
    Args:
        csv_file (str | Path): Путь к CSV-файлу для чтения.

    Returns:
        SimpleNamespace | None: Объект SimpleNamespace, содержащий данные из CSV, или `None`, если преобразование не удалось.

    Raises:
        Exception: Если не удается прочитать CSV.

     **Как работает функция**:
     Функция `csv2ns` принимает путь к CSV-файлу и использует функцию `read_csv_as_ns` для чтения данных из этого файла и преобразования их в объект `SimpleNamespace`. Если чтение и преобразование проходят успешно, функция возвращает полученный объект. В случае возникновения ошибки, функция возвращает `None`.
    """
```

**Описание**: Преобразует данные из CSV-файла в объекты `SimpleNamespace`.

**Параметры**:
- `csv_file` (str | Path): Путь к CSV-файлу для чтения.
- `*args`: Произвольные позиционные аргументы, передаваемые в `read_csv_as_ns`.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в `read_csv_as_ns`.

**Возвращает**:
- `SimpleNamespace | None`: Объект `SimpleNamespace`, содержащий данные из CSV, или `None`, если преобразование не удалось.

**Вызывает исключения**:
- `Exception`: Если не удается прочитать CSV-файл.

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

**Описание**: Преобразует CSV-файл в формат JSON и сохраняет его в JSON-файл.

**Параметры**:
- `csv_file_path` (str | Path): Путь к CSV-файлу для чтения.
- `json_file_path` (str | Path): Путь к JSON-файлу для сохранения.
- `exc_info` (bool, optional): Если `True`, включает информацию трассировки в лог. По умолчанию `True`.

**Возвращает**:
- `List[Dict[str, str]] | None`: JSON-данные в виде списка словарей или `None`, если преобразование не удалось.

**Вызывает исключения**:
- `Exception`: Если не удается прочитать или преобразовать CSV-файл.

**Примеры**:
```python
>>> json_data = csv_to_json('dialogue_log.csv', 'dialogue_log.json')
>>> print(json_data)
[{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]
```
```
     **Как работает функция**:

     Функция `csv_to_json` сначала пытается прочитать CSV-файл, используя функцию `read_csv_file`. Если данные успешно прочитаны, они сохраняются в JSON-файл с использованием `json.dump` с отступом в 4 пробела для читаемости. В случае возникновения исключения, информация об ошибке логируется с помощью `logger.error`, и возвращается `None`.