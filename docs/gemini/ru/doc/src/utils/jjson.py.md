# Модуль для работы с JSON и SimpleNamespace

## Обзор

Модуль `jjson` предоставляет набор функций для работы с данными в формате JSON, включая чтение, запись и преобразование данных. Он также поддерживает работу с объектами `SimpleNamespace`.

## Подробнее

Модуль содержит функции для загрузки JSON из файлов, строк и объектов, а также для сохранения JSON в файлы. Он также включает функции для преобразования данных между форматами JSON и `SimpleNamespace`. Модуль предназначен для упрощения работы с JSON-данными в проекте `hypotez`.
Основные функции:
- `j_dumps` - сохраняет JSON в файл или возвращает JSON как словарь.
- `j_loads` - загружает JSON из файла, каталога, строки или объекта.
- `j_loads_ns` - загружает JSON и преобразует его в `SimpleNamespace`.

## Классы

### `Config`

**Описание**: Класс, содержащий константы для режимов записи файлов.

**Атрибуты**:
- `MODE_WRITE` (str): Режим записи "w".
- `MODE_APPEND_START` (str): Режим добавления в начало файла "a+".
- `MODE_APPEND_END` (str): Режим добавления в конец файла "+a".

## Функции

### `_convert_to_dict`

```python
def _convert_to_dict(value: Any) -> Any:
    """ Функция преобразует SimpleNamespace и списки в словари.

    Args:
        value (Any): Значение для преобразования.

    Returns:
        Any: Преобразованное значение. Возвращает словарь, если входное значение является SimpleNamespace или списком.

    Как работает функция:
    1. Проверяет, является ли входное значение экземпляром `SimpleNamespace`. Если да, то преобразует его в словарь, рекурсивно применяя `_convert_to_dict` к каждому значению.
    2. Если входное значение является словарем, то рекурсивно применяет `_convert_to_dict` к каждому значению в словаре.
    3. Если входное значение является списком, то рекурсивно применяет `_convert_to_dict` к каждому элементу списка.
    4. Если входное значение не является ни `SimpleNamespace`, ни словарем, ни списком, то возвращает его без изменений.

    ASCII flowchart:
    Value
    |
    isinstance(Value, SimpleNamespace)? --> YES --> Convert SimpleNamespace to Dict
    |   NO
    isinstance(Value, Dict)? --> YES --> Convert Dict
    |   NO
    isinstance(Value, List)? --> YES --> Convert List
    |   NO
    Return Value

    """
```

### `_read_existing_data`

```python
def _read_existing_data(path: Path, exc_info: bool = True) -> dict:
    """ Читает существующие JSON данные из файла.

    Args:
        path (Path): Путь к файлу.
        exc_info (bool, optional): Если `True`, логирует исключения с трассировкой. По умолчанию `True`.

    Returns:
        dict: JSON данные в виде словаря. Возвращает пустой словарь в случае ошибки.

    Как работает функция:
    1. Пытается прочитать содержимое файла, используя `path.read_text(encoding="utf-8")`.
    2. Пытается преобразовать прочитанный текст в JSON, используя `json.loads()`.
    3. Если происходит ошибка `json.JSONDecodeError`, логирует ошибку с помощью `logger.error` и возвращает пустой словарь.
    4. Если происходит другая ошибка, логирует ошибку с помощью `logger.error` и возвращает пустой словарь.

    ASCII flowchart:
    Path
    |
    try: read_text
    |
    json.loads(text)
    |
    except JSONDecodeError: log error; return {}
    |
    except Exception: log error; return {}
    |
    return data

    """
```

### `_merge_data`

```python
def _merge_data(
    data: Dict, existing_data: Dict, mode: str
) -> Dict:
    """ Объединяет новые данные с существующими данными в зависимости от режима.

    Args:
        data (Dict): Новые данные для объединения.
        existing_data (Dict): Существующие данные.
        mode (str): Режим объединения (Config.MODE_APPEND_START, Config.MODE_APPEND_END).

    Returns:
        Dict: Объединенные данные. Возвращает пустой словарь в случае ошибки.

    Как работает функция:
    1. Проверяет режим объединения.
    2. Если режим `Config.MODE_APPEND_START`:
        - Если `data` и `existing_data` являются списками, объединяет `data` и `existing_data` (data + existing_data).
        - Если `data` и `existing_data` являются словарями, обновляет `existing_data` данными из `data`.
        - Возвращает `existing_data`.
    3. Если режим `Config.MODE_APPEND_END`:
        - Если `data` и `existing_data` являются списками, объединяет `existing_data` и `data` (existing_data + data).
        - Если `data` и `existing_data` являются словарями, обновляет `data` данными из `existing_data`.
        - Возвращает `data`.
    4. Если режим не соответствует ни одному из вышеперечисленных, возвращает `data`.
    5. В случае возникновения исключения логирует ошибку и возвращает пустой словарь.

    ASCII flowchart:
    Data, Existing Data, Mode
    |
    Mode == Config.MODE_APPEND_START?
    |   YES
    |   |
    |   Data и Existing Data - списки? --> YES --> data + existing_data
    |   |   NO
    |   Data и Existing Data - словари? --> YES --> existing_data.update(data)
    |   |   NO
    |   return existing_data
    |   NO
    Mode == Config.MODE_APPEND_END?
    |   YES
    |   |
    |   Data и Existing Data - списки? --> YES --> existing_data + data
    |   |   NO
    |   Data и Existing Data - словари? --> YES --> data.update(existing_data)
    |   |   NO
    |   return data
    |   NO
    return data

    """
```

### `j_dumps`

```python
def j_dumps(
    data: Union[Dict, SimpleNamespace, List[Dict], List[SimpleNamespace]],
    file_path: Optional[Path] = None,
    ensure_ascii: bool = False,
    mode: str = Config.MODE_WRITE,
    exc_info: bool = True,
) -> Optional[Dict]:
    """
    Сохраняет JSON данные в файл или возвращает JSON как словарь.

    Args:
        data (Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]): JSON-совместимые данные или объекты SimpleNamespace для сохранения.
        file_path (Optional[Path], optional): Путь к выходному файлу. Если None, возвращает JSON как словарь. По умолчанию None.
        ensure_ascii (bool, optional): Если True, экранирует не-ASCII символы в выводе. По умолчанию True.
        mode (str, optional): Режим открытия файла ('w', 'a+', '+a'). По умолчанию 'w'.
        exc_info (bool, optional): Если True, логирует исключения с трассировкой. По умолчанию True.

    Returns:
        Optional[Dict]: JSON данные как словарь в случае успеха, или None в случае ошибки.

    Raises:
        ValueError: Если режим файла не поддерживается.

    Как работает функция:
    1. Преобразует `file_path` в объект `Path`, если он является строкой или `Path`.
    2. Если `data` является строкой, пытается исправить JSON с помощью `repair_json`.
    3. Преобразует `data` в словарь с помощью `_convert_to_dict`.
    4. Если `mode` не является одним из допустимых режимов, устанавливает `mode` в `Config.MODE_WRITE`.
    5. Если `path` существует и `mode` является одним из режимов добавления, читает существующие данные из файла с помощью `_read_existing_data`.
    6. Объединяет `data` с существующими данными с помощью `_merge_data`.
    7. Если `path` указан, пытается создать родительские директории и записать JSON в файл.
    8. В случае успеха возвращает `data`, иначе возвращает `None`.
    9. Если `path` не указан, возвращает `data`.

    ASCII flowchart:
    Data, File Path, Ensure ASCII, Mode
    |
    Data is str? --> YES --> repair_json(data)
    |   NO
    data = _convert_to_dict(data)
    |
    mode in valid modes? --> YES
    |   NO --> mode = Config.MODE_WRITE
    |
    path and path.exists() and mode in append modes? --> YES --> existing_data = _read_existing_data(path)
    |   NO
    data = _merge_data(data, existing_data, mode)
    |
    path? --> YES
    |   |
    |   try: write to file
    |   |
    |   except Exception: log error; return None
    |   |
    |   return data
    |   NO
    return data

    """
```

### `_decode_strings`

```python
def _decode_strings(data: Any) -> Any:
    """ Рекурсивно декодирует строки в структуре данных.

    Args:
        data (Any): Данные для декодирования.

    Returns:
        Any: Декодированные данные.

    Как работает функция:
    1. Если `data` является строкой, пытается декодировать ее, используя `codecs.decode(data, 'unicode_escape')`.
    2. Если декодирование не удалось, возвращает исходную строку.
    3. Если `data` является списком, рекурсивно применяет `_decode_strings` к каждому элементу списка.
    4. Если `data` является словарем, рекурсивно применяет `_decode_strings` к каждому ключу и значению в словаре.
    5. В противном случае возвращает `data` без изменений.

    ASCII flowchart:
    Data
    |
    isinstance(Data, str)? --> YES --> try: decode string
    |   |   |   |   |       except: return Data
    |   NO
    isinstance(Data, list)? --> YES --> Recursively decode list elements
    |   NO
    isinstance(Data, dict)? --> YES --> Recursively decode keys and values
    |   NO
    return Data

    """
```

### `_string_to_dict`

```python
def _string_to_dict(json_string: str) -> dict:
    """ Удаляет markdown кавычки и преобразует JSON строку в словарь.

    Args:
        json_string (str): JSON строка.

    Returns:
        dict: Словарь, полученный из JSON строки. Возвращает пустой словарь в случае ошибки.

    Как работает функция:
    1. Проверяет, начинается ли строка с markdown кавычек ("```" или "```json") и заканчивается ли markdown кавычками ("```" или "```\\n").
    2. Если да, удаляет кавычки и префикс "json" (если он есть).
    3. Пытается преобразовать строку в словарь, используя `json.loads()`.
    4. Если происходит ошибка `json.JSONDecodeError`, логирует ошибку и возвращает пустой словарь.

    ASCII flowchart:
    JSON String
    |
    Starts and ends with markdown quotes? --> YES --> Remove quotes and 'json' prefix
    |   NO
    try: json.loads(string)
    |
    except JSONDecodeError: log error; return {}
    |
    return dict

    """
```

### `j_loads`

```python
def j_loads(
    jjson: Union[dict, SimpleNamespace, str, Path, list], ordered: bool = True
) -> Union[dict, list]:
    """
    Загружает JSON или CSV данные из файла, директории, строки или объекта.

    Args:
        jjson (dict | SimpleNamespace | str | Path | list): Путь к файлу/директории, JSON строка или JSON объект.
        ordered (bool, optional): Использовать OrderedDict для сохранения порядка элементов. По умолчанию True.

    Returns:
        dict | list: Обработанные данные (словарь или список словарей).

    Raises:
        FileNotFoundError: Если указанный файл не найден.
        json.JSONDecodeError: Если JSON данные не могут быть распарсены.

    Как работает функция:
    1. Если `jjson` является `SimpleNamespace`, преобразует его в словарь.
    2. Если `jjson` является `Path`:
        - Если это директория, рекурсивно загружает все JSON файлы из этой директории.
        - Если это файл, читает и парсит JSON данные из файла.
    3. Если `jjson` является строкой, преобразует строку в словарь с помощью `_string_to_dict`.
    4. Если `jjson` является списком, декодирует строки в списке с помощью `_decode_strings`.
    5. Если `jjson` является словарем, декодирует строки в словаре с помощью `_decode_strings`.
    6. Обрабатывает исключения `FileNotFoundError`, `json.JSONDecodeError` и `Exception`, логируя ошибки и возвращая пустой словарь.

    ASCII flowchart:
    jjson, ordered
    |
    jjson instanceof SimpleNamespace? --> YES --> jjson = vars(jjson)
    |   NO
    jjson instanceof Path? --> YES --> is directory? --> YES --> recursively load json files
    |   |                       |   NO --> read and parse json
    |   NO
    jjson instanceof str? --> YES --> _string_to_dict(jjson)
    |   NO
    jjson instanceof list? --> YES --> _decode_strings(jjson)
    |   NO
    jjson instanceof dict? --> YES --> _decode_strings(jjson)
    |   NO
    handle FileNotFoundError, JSONDecodeError, Exception: log and return {}
    return {}
    """
```

### `j_loads_ns`

```python
def j_loads_ns(
    jjson: Union[Path, SimpleNamespace, Dict, str], ordered: bool = True
) -> Union[SimpleNamespace, List[SimpleNamespace], Dict]:
    """ Загружает JSON/CSV данные и преобразует в SimpleNamespace.

    Args:
        jjson (Path | SimpleNamespace | Dict | str): Путь к файлу, SimpleNamespace, словарь или строка.
        ordered (bool, optional): Использовать OrderedDict для сохранения порядка элементов. По умолчанию True.

    Returns:
        Union[SimpleNamespace, List[SimpleNamespace], Dict]: SimpleNamespace или список SimpleNamespace объектов.

    Как работает функция:
    1. Загружает JSON данные с помощью функции `j_loads`.
    2. Если данные успешно загружены:
        - Если данные являются списком, преобразует каждый элемент списка в `SimpleNamespace` с помощью `dict2ns`.
        - Если данные не являются списком, преобразует данные в `SimpleNamespace` с помощью `dict2ns`.
    3. Возвращает полученные данные в формате `SimpleNamespace`.
    4. В случае ошибки возвращает пустой словарь.

    ASCII flowchart:
    jjson, ordered
    |
    data = j_loads(jjson, ordered)
    |
    data? --> YES --> data instanceof list? --> YES --> convert each item to SimpleNamespace
    |   |   |   |   |   NO --> convert data to SimpleNamespace
    |   NO
    return {}

    """