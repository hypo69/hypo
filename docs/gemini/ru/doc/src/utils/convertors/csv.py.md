# Модуль для конвертации CSV в JSON

## Обзор

Модуль `csv.py` предоставляет утилиты для конвертации данных из формата CSV в JSON и наоборот. Он включает функции для чтения данных из CSV файлов и преобразования их в словари (`dict`) или объекты `SimpleNamespace`, а также для сохранения данных в формате JSON.

## Подробней

Этот модуль предназначен для обеспечения удобного способа преобразования между форматами CSV и JSON, что может быть полезно при обработке и анализе данных, хранящихся в различных форматах. Модуль использует стандартные библиотеки `json` и `csv`, а также библиотеку `pathlib` для работы с путями к файлам.

## Функции

### `csv2dict`

```python
def csv2dict(csv_file: str | Path, *args, **kwargs) -> dict | None:
    """
    Конвертирует CSV данные в словарь.

    Args:
        csv_file (str | Path): Путь к CSV файлу для чтения.

    Returns:
        dict | None: Словарь, содержащий данные из CSV, конвертированные в формат JSON, или `None`, если конвертация не удалась.

    Raises:
        Exception: Если не удается прочитать CSV файл.
    """
```

**Назначение**: Функция `csv2dict` преобразует содержимое CSV-файла в словарь Python.

**Параметры**:
- `csv_file` (str | Path): Путь к CSV-файлу, который необходимо преобразовать.
- `*args`: Произвольные позиционные аргументы, передаваемые в функцию `read_csv_as_dict`.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в функцию `read_csv_as_dict`.

**Возвращает**:
- `dict | None`: Функция возвращает словарь, содержащий данные из CSV-файла, или `None`, если преобразование не удалось.

**Вызывает исключения**:
- `Exception`: Возникает, если не удается прочитать CSV-файл.

**Как работает функция**:

1. Функция вызывает функцию `read_csv_as_dict` из модуля `src.utils.csv`, передавая ей путь к CSV-файлу и все дополнительные аргументы.
2. Функция `read_csv_as_dict` читает содержимое CSV-файла и преобразует его в словарь Python.
3. Функция `csv2dict` возвращает полученный словарь.

```
Чтение CSV файла --> Преобразование в словарь --> Возврат словаря
```

**Примеры**:

```python
from pathlib import Path
# Пример 1: Преобразование CSV файла в словарь
csv_file_path = Path('data.csv')
data_dict = csv2dict(csv_file_path)
if data_dict:
    print(data_dict)

# Пример 2: Преобразование CSV файла с дополнительными параметрами
csv_file_path = Path('data.csv')
data_dict = csv2dict(csv_file_path, delimiter=';')
if data_dict:
    print(data_dict)
```

### `csv2ns`

```python
def csv2ns(csv_file: str | Path, *args, **kwargs) -> SimpleNamespace | None:
    """
    Конвертирует CSV данные в объекты SimpleNamespace.

    Args:
        csv_file (str | Path): Путь к CSV файлу для чтения.

    Returns:
        SimpleNamespace | None: Объект SimpleNamespace, содержащий данные из CSV, или `None`, если конвертация не удалась.

    Raises:
        Exception: Если не удается прочитать CSV файл.
    """
```

**Назначение**: Функция `csv2ns` преобразует содержимое CSV-файла в объект `SimpleNamespace`.

**Параметры**:
- `csv_file` (str | Path): Путь к CSV-файлу, который необходимо преобразовать.
- `*args`: Произвольные позиционные аргументы, передаваемые в функцию `read_csv_as_ns`.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в функцию `read_csv_as_ns`.

**Возвращает**:
- `SimpleNamespace | None`: Функция возвращает объект `SimpleNamespace`, содержащий данные из CSV-файла, или `None`, если преобразование не удалось.

**Вызывает исключения**:
- `Exception`: Возникает, если не удается прочитать CSV-файл.

**Как работает функция**:

1. Функция вызывает функцию `read_csv_as_ns` из модуля `src.utils.csv`, передавая ей путь к CSV-файлу и все дополнительные аргументы.
2. Функция `read_csv_as_ns` читает содержимое CSV-файла и преобразует его в объект `SimpleNamespace`.
3. Функция `csv2ns` возвращает полученный объект `SimpleNamespace`.

```
Чтение CSV файла --> Преобразование в SimpleNamespace --> Возврат SimpleNamespace
```

**Примеры**:

```python
from pathlib import Path
# Пример 1: Преобразование CSV файла в SimpleNamespace
csv_file_path = Path('data.csv')
data_ns = csv2ns(csv_file_path)
if data_ns:
    print(data_ns)

# Пример 2: Преобразование CSV файла с дополнительными параметрами
csv_file_path = Path('data.csv')
data_ns = csv2ns(csv_file_path, delimiter=';')
if data_ns:
    print(data_ns)
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

**Назначение**: Функция `csv_to_json` преобразует содержимое CSV-файла в формат JSON и сохраняет его в JSON-файл.

**Параметры**:
- `csv_file_path` (str | Path): Путь к CSV-файлу, который необходимо преобразовать.
- `json_file_path` (str | Path): Путь к JSON-файлу, в который будет сохранено преобразованное содержимое.
- `exc_info` (bool, optional): Если `True`, включает информацию об исключении в лог. По умолчанию `True`.

**Возвращает**:
- `List[Dict[str, str]] | None`: Функция возвращает JSON-данные в виде списка словарей или `None`, если преобразование не удалось.

**Как работает функция**:

1. Функция вызывает функцию `read_csv_file` из модуля `src.utils.csv`, передавая ей путь к CSV-файлу и флаг `exc_info`.
2. Если данные успешно прочитаны из CSV-файла, функция открывает JSON-файл для записи в кодировке UTF-8.
3. Функция записывает JSON-данные в файл с отступом 4 для удобочитаемости.
4. Функция возвращает JSON-данные.
5. Если во время процесса возникает исключение, функция логирует ошибку с использованием `logger.error` и возвращает `None`.

```
Чтение CSV файла --> Преобразование в JSON --> Запись в JSON файл --> Возврат JSON данных
```

**Примеры**:

```python
from pathlib import Path
# Пример 1: Преобразование CSV файла в JSON
csv_file_path = Path('data.csv')
json_file_path = Path('data.json')
json_data = csv_to_json(csv_file_path, json_file_path)
if json_data:
    print(json_data)

# Пример 2: Преобразование CSV файла в JSON с отключением информации об исключении
csv_file_path = Path('data.csv')
json_file_path = Path('data.json')
json_data = csv_to_json(csv_file_path, json_file_path, exc_info=False)
if json_data:
    print(json_data)