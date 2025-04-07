# Модуль для конвертации CSV и JSON файлов
## Обзор

Модуль `src.utils.convertors.csv` предоставляет утилиты для конвертации данных между форматами CSV и JSON. Он включает функции для чтения CSV-файлов и преобразования их в словари (`csv2dict`) или объекты `SimpleNamespace` (`csv2ns`), а также функцию для преобразования CSV в JSON с сохранением в файл (`csv_to_json`).

## Подробней

Этот модуль предназначен для упрощения работы с данными, хранящимися в формате CSV, и преобразования их в более удобные структуры данных Python, такие как словари и объекты `SimpleNamespace`. Это позволяет легко манипулировать данными и использовать их в различных приложениях. Также реализована возможность сохранения данных из CSV файла в файл JSON.

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

**Назначение**: Преобразует данные из CSV-файла в словарь.

**Параметры**:
- `csv_file` (str | Path): Путь к CSV-файлу, который нужно прочитать.
- `*args`: Произвольные позиционные аргументы, передаваемые в функцию `read_csv_as_dict`.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в функцию `read_csv_as_dict`.

**Возвращает**:
- `dict | None`: Словарь, содержащий данные из CSV-файла, преобразованные в формат JSON, или `None`, если преобразование не удалось.

**Вызывает исключения**:
- `Exception`: Если не удается прочитать CSV-файл.

**Как работает функция**:
Функция вызывает `read_csv_as_dict` с переданными аргументами для выполнения преобразования.

```ascii
Начало
  ↓
Вызов read_csv_as_dict(csv_file, *args, **kwargs)
  ↓
Возврат результата (словарь или None)
  ↓
Конец
```

**Примеры**:

```python
from pathlib import Path
# Пример 1: Преобразование CSV-файла в словарь
csv_file_path = Path('data.csv')
data_dict = csv2dict(csv_file_path)
if data_dict:
    print(data_dict)
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

**Назначение**: Преобразует данные из CSV-файла в объекты `SimpleNamespace`.

**Параметры**:
- `csv_file` (str | Path): Путь к CSV-файлу, который нужно прочитать.
- `*args`: Произвольные позиционные аргументы, передаваемые в функцию `read_csv_as_ns`.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в функцию `read_csv_as_ns`.

**Возвращает**:
- `SimpleNamespace | None`: Объект `SimpleNamespace`, содержащий данные из CSV-файла, или `None`, если преобразование не удалось.

**Вызывает исключения**:
- `Exception`: Если не удается прочитать CSV-файл.

**Как работает функция**:
Функция вызывает `read_csv_as_ns` с переданными аргументами для выполнения преобразования.

```ascii
Начало
  ↓
Вызов read_csv_as_ns(csv_file, *args, **kwargs)
  ↓
Возврат результата (SimpleNamespace или None)
  ↓
Конец
```

**Примеры**:

```python
from pathlib import Path
# Пример 1: Преобразование CSV-файла в SimpleNamespace
csv_file_path = Path('data.csv')
data_ns = csv2ns(csv_file_path)
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
    try:
        data = read_csv_file(csv_file_path, exc_info=exc_info)
        if data is not None:
            with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, indent=4)
            return data
        return
    except Exception as ex:
        logger.error("Failed to convert CSV to JSON", ex, exc_info=exc_info)
        return
```

**Назначение**: Преобразует CSV-файл в формат JSON и сохраняет его в JSON-файл.

**Параметры**:
- `csv_file_path` (str | Path): Путь к CSV-файлу, который нужно прочитать.
- `json_file_path` (str | Path): Путь к JSON-файлу, в который нужно сохранить данные.
- `exc_info` (bool, optional): Если `True`, включает информацию об отслеживании в журнал. По умолчанию `True`.

**Возвращает**:
- `List[Dict[str, str]] | None`: Данные JSON в виде списка словарей или `None`, если преобразование не удалось.

**Вызывает исключения**:
- `Exception`: Если не удается преобразовать CSV в JSON.

**Как работает функция**:

1.  **Чтение CSV-файла**: Функция `read_csv_file` используется для чтения данных из CSV-файла.
2.  **Проверка данных**: Проверяется, что данные были успешно прочитаны из CSV-файла.
3.  **Запись в JSON-файл**: Если данные были успешно прочитаны, они записываются в JSON-файл с использованием `json.dump` и отступом в 4 пробела для удобочитаемости.
4.  **Обработка ошибок**: Если во время процесса возникает исключение, оно перехватывается, логируется с использованием `logger.error`, и функция возвращает `None`.

```ascii
Начало
  ↓
Чтение данных из CSV-файла с использованием read_csv_file(csv_file_path, exc_info=exc_info)
  ↓
Проверка: Данные прочитаны успешно?
  ├── Да: Запись данных в JSON-файл с использованием json.dump(data, jsonfile, indent=4)
  │    ↓
  │    Возврат данных
  └── Нет: Возврат None
  ↓
Конец (успех или ошибка)
```

**Примеры**:

```python
from pathlib import Path

# Пример 1: Преобразование CSV-файла в JSON и сохранение в файл
csv_file_path = Path('data.csv')
json_file_path = Path('data.json')
json_data = csv_to_json(csv_file_path, json_file_path)
if json_data:
    print(f"Данные успешно преобразованы и сохранены в {json_file_path}")
    print(json_data)