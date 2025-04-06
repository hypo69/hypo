# Модуль для конвертации CSV в JSON и наоборот
=================================================

Модуль содержит функции для конвертации данных из формата CSV в JSON и из JSON в CSV.
Он предоставляет удобные инструменты для преобразования данных между этими двумя распространенными форматами.

## Оглавление

- [Обзор](#обзор)
- [Подробнее](#подробнее)
- [Функции](#функции)
    - [csv2dict](#csv2dict)
    - [csv2ns](#csv2ns)
    - [csv_to_json](#csv_to_json)

## Обзор

Модуль `src.utils.convertors.csv` предоставляет функции для конвертации данных между форматами CSV и JSON. Он включает функции для чтения CSV файлов, преобразования их в словари или объекты SimpleNamespace, а также для сохранения данных в формате JSON.

## Подробнее

Этот модуль предназначен для облегчения работы с данными в формате CSV и JSON. Он предоставляет простой и удобный интерфейс для преобразования данных между этими форматами, что может быть полезно во многих сценариях, таких как обработка данных, импорт/экспорт данных и т.д.
Анализируя предоставленный код можно сказать, что этот модуль используется для конвертации файлов с данными, например логов диалогов.

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

**Назначение**: Преобразует данные из CSV файла в словарь.

**Параметры**:
- `csv_file` (str | Path): Путь к CSV файлу, который нужно прочитать.
- `*args`: Произвольные позиционные аргументы, передаваемые в функцию `read_csv_as_dict`.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в функцию `read_csv_as_dict`.

**Возвращает**:
- `dict | None`: Словарь, содержащий данные из CSV файла, преобразованные в формат JSON, или `None`, если преобразование не удалось.

**Вызывает исключения**:
- `Exception`: Возникает, если не удается прочитать CSV файл.

**Как работает функция**:

1. Функция `csv2dict` принимает путь к CSV файлу (`csv_file`).
2. Она вызывает функцию `read_csv_as_dict` с переданным путем и дополнительными аргументами (`*args`, `**kwargs`).
3. Функция `read_csv_as_dict` читает данные из CSV файла и преобразует их в словарь.
4. Если чтение и преобразование прошли успешно, функция возвращает полученный словарь.
5. Если произошла ошибка, функция возвращает `None`.

```
CSV файл --> Прочитать CSV как словарь --> Возвращает словарь
```

**Примеры**:

```python
# Пример 1: Преобразование CSV файла в словарь
csv_file_path = 'data.csv'
data = csv2dict(csv_file_path)
if data:
    print(data)
else:
    print('Не удалось преобразовать CSV файл в словарь.')

# Пример 2: Преобразование CSV файла с дополнительными аргументами
csv_file_path = 'data.csv'
data = csv2dict(csv_file_path, delimiter=';')  # Указание разделителя
if data:
    print(data)
else:
    print('Не удалось преобразовать CSV файл в словарь.')
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

**Назначение**: Преобразует данные из CSV файла в объекты `SimpleNamespace`.

**Параметры**:
- `csv_file` (str | Path): Путь к CSV файлу, который нужно прочитать.
- `*args`: Произвольные позиционные аргументы, передаваемые в функцию `read_csv_as_ns`.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в функцию `read_csv_as_ns`.

**Возвращает**:
- `SimpleNamespace | None`: Объект `SimpleNamespace`, содержащий данные из CSV файла, или `None`, если преобразование не удалось.

**Вызывает исключения**:
- `Exception`: Возникает, если не удается прочитать CSV файл.

**Как работает функция**:

1. Функция `csv2ns` принимает путь к CSV файлу (`csv_file`).
2. Она вызывает функцию `read_csv_as_ns` с переданным путем и дополнительными аргументами (`*args`, `**kwargs`).
3. Функция `read_csv_as_ns` читает данные из CSV файла и преобразует их в объекты `SimpleNamespace`.
4. Если чтение и преобразование прошли успешно, функция возвращает полученный объект `SimpleNamespace`.
5. Если произошла ошибка, функция возвращает `None`.

```
CSV файл --> Прочитать CSV как SimpleNamespace --> Возвращает SimpleNamespace
```

**Примеры**:

```python
# Пример 1: Преобразование CSV файла в SimpleNamespace
csv_file_path = 'data.csv'
data = csv2ns(csv_file_path)
if data:
    print(data)
else:
    print('Не удалось преобразовать CSV файл в SimpleNamespace.')

# Пример 2: Преобразование CSV файла с дополнительными аргументами
csv_file_path = 'data.csv'
data = csv2ns(csv_file_path, delimiter=';')  # Указание разделителя
if data:
    print(data)
else:
    print('Не удалось преобразовать CSV файл в SimpleNamespace.')
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

**Назначение**: Преобразует CSV файл в формат JSON и сохраняет его в JSON файл.

**Параметры**:
- `csv_file_path` (str | Path): Путь к CSV файлу, который нужно прочитать.
- `json_file_path` (str | Path): Путь к JSON файлу, в который нужно сохранить данные.
- `exc_info` (bool, optional): Если `True`, включает информацию об отслеживании в журнал. По умолчанию `True`.

**Возвращает**:
- `List[Dict[str, str]] | None`: Данные JSON в виде списка словарей, или `None`, если преобразование не удалось.

**Вызывает исключения**:
- `Exception`: Возникает, если не удается преобразовать CSV в JSON.

**Как работает функция**:

1. Функция `csv_to_json` принимает путь к CSV файлу (`csv_file_path`) и путь к JSON файлу (`json_file_path`).
2. Она вызывает функцию `read_csv_file` для чтения данных из CSV файла. Параметр `exc_info` определяет, будет ли включена информация об исключениях в логи.
3. Если данные успешно прочитаны, функция открывает JSON файл для записи (`json_file_path`) в кодировке UTF-8.
4. Данные записываются в JSON файл с отступом в 4 пробела для удобочитаемости.
5. Функция возвращает данные JSON в виде списка словарей.
6. Если в процессе преобразования возникает исключение, оно логируется с помощью `logger.error`, и функция возвращает `None`.

```
CSV файл --> Прочитать CSV файл --> Записать в JSON файл --> Возвращает JSON данные
                                      ^
                                      |
                                      Если ошибка
```

**Примеры**:

```python
# Пример 1: Преобразование CSV файла в JSON
csv_file_path = 'data.csv'
json_file_path = 'data.json'
json_data = csv_to_json(csv_file_path, json_file_path)
if json_data:
    print(json_data)
else:
    print('Не удалось преобразовать CSV файл в JSON.')

# Пример 2: Преобразование CSV файла в JSON с отключением информации об исключениях в логах
csv_file_path = 'data.csv'
json_file_path = 'data.json'
json_data = csv_to_json(csv_file_path, json_file_path, exc_info=False)
if json_data:
    print(json_data)
else:
    print('Не удалось преобразовать CSV файл в JSON.')