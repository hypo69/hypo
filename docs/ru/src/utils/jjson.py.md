# Модуль для работы с JSON и SimpleNamespace (`jjson.py`)

## Обзор

Модуль `jjson.py` предоставляет набор функций для работы с данными в формате JSON и SimpleNamespace. Он включает функции для загрузки, сохранения и преобразования данных между различными форматами, такими как JSON, CSV, словари Python и объекты SimpleNamespace. Модуль также обеспечивает обработку ошибок и ведение журнала для облегчения отладки и обслуживания.

## Подробней

Этот модуль предназначен для упрощения работы с конфигурационными файлами и данными, которые могут быть представлены в различных форматах. Он предоставляет удобные функции для чтения и записи данных, а также для преобразования данных в объекты SimpleNamespace, что облегчает доступ к данным по атрибутам. Модуль также включает функции для очистки и исправления JSON-строк.

## Функции

### `_convert_to_dict`

```python
def _convert_to_dict(value: Any) -> Any:
    """Convert SimpleNamespace and lists to dict."""
    if isinstance(value, SimpleNamespace):
        return {key: _convert_to_dict(val) for key, val in vars(value).items()}
    if isinstance(value, dict):
        return {key: _convert_to_dict(val) for key, val in value.items()}
    if isinstance(value, list):
        return [_convert_to_dict(item) for item in value]
    return value
```

**Назначение**: Преобразует объекты `SimpleNamespace` и списки в словари.

**Как работает функция**:
Функция рекурсивно проходит по входным данным и преобразует объекты `SimpleNamespace` и списки в словари. Если входное значение является экземпляром `SimpleNamespace`, оно преобразуется в словарь, где ключи и значения рекурсивно обрабатываются. Если входное значение является словарем или списком, каждый элемент рекурсивно преобразуется.

**Параметры**:
- `value` (Any): Входное значение для преобразования.

**Возвращает**:
- `Any`: Преобразованное значение в виде словаря или списка.

**Примеры**:

```python
from types import SimpleNamespace
data = SimpleNamespace(a=1, b=SimpleNamespace(c=2))
result = _convert_to_dict(data)
print(result)  # Вывод: {'a': 1, 'b': {'c': 2}}
```

### `_read_existing_data`

```python
def _read_existing_data(path: Path, exc_info: bool = True) -> dict:
    """Read existing JSON data from a file."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding existing JSON in {path}: {e}", exc_info=exc_info)
        return {}
    except Exception as ex:
        logger.error(f"Error reading {path=}: {ex}", exc_info=exc_info)
        return {}
```

**Назначение**: Читает существующие JSON-данные из файла.

**Как работает функция**:
Функция пытается прочитать JSON-данные из файла, указанного в параметре `path`. В случае успеха она возвращает десериализованные данные. Если происходит ошибка при чтении или декодировании JSON, функция регистрирует ошибку с использованием модуля `logger` и возвращает пустой словарь. Параметр `exc_info` определяет, нужно ли выводить служебную информацию об исключении в лог.

**Параметры**:
- `path` (Path): Путь к файлу.
- `exc_info` (bool, optional): Если `True`, логирует исключения с трассировкой. По умолчанию `True`.

**Возвращает**:
- `dict`: JSON-данные в виде словаря или пустой словарь в случае ошибки.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден.
- `json.JSONDecodeError`: Если JSON-данные не могут быть разобраны.

**Примеры**:

```python
from pathlib import Path
file_path = Path('config.json')
data = _read_existing_data(file_path)
print(data)
```

### `_merge_data`

```python
def _merge_data(
    data: Dict, existing_data: Dict, mode: str
) -> Dict:
    """Merge new data with existing data based on mode."""
    try:
        if mode == Config.MODE_APPEND_START:
            if isinstance(data, list) and isinstance(existing_data, list):
               return data + existing_data
            if isinstance(data, dict) and isinstance(existing_data, dict):
                 existing_data.update(data)
            return existing_data
        elif mode == Config.MODE_APPEND_END:
            if isinstance(data, list) and isinstance(existing_data, list):
                return existing_data + data
            if isinstance(data, dict) and isinstance(existing_data, dict):
                 data.update(existing_data)
            return data
        return data
    except Exception as ex:
        logger.error(ex)
        return {}
```

**Назначение**: Объединяет новые данные с существующими данными в зависимости от режима.

**Как работает функция**:
Функция объединяет новые данные (`data`) с существующими данными (`existing_data`) на основе указанного режима (`mode`). Если режим `Config.MODE_APPEND_START`, то данные добавляются в начало существующих данных (для списков) или обновляются (для словарей). Если режим `Config.MODE_APPEND_END`, то данные добавляются в конец существующих данных (для списков) или существующие данные обновляют новые данные (для словарей). Если режим не соответствует ни одному из указанных, возвращаются новые данные. В случае возникновения ошибки функция логирует ее и возвращает пустой словарь.

**Параметры**:
- `data` (Dict): Новые данные для объединения.
- `existing_data` (Dict): Существующие данные.
- `mode` (str): Режим объединения (`Config.MODE_APPEND_START` или `Config.MODE_APPEND_END`).

**Возвращает**:
- `Dict`: Объединенные данные в виде словаря.

**Примеры**:

```python
data = {'a': 1, 'b': 2}
existing_data = {'c': 3, 'd': 4}
mode = Config.MODE_APPEND_END
result = _merge_data(data, existing_data, mode)
print(result)  # Вывод: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
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
    Dump JSON data to a file or return the JSON data as a dictionary.

    Args:
        data (Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]): JSON-compatible data or SimpleNamespace objects to dump.
        file_path (Optional[Path], optional): Path to the output file. If None, returns JSON as a dictionary. Defaults to None.
        ensure_ascii (bool, optional): If True, escapes non-ASCII characters in output. Defaults to True.
        mode (str, optional): File open mode ('w', 'a+', '+a'). Defaults to 'w'.
        exc_info (bool, optional): If True, logs exceptions with traceback. Defaults to True.

    Returns:
        Optional[Dict]: JSON data as a dictionary if successful, or nothing if an error occurs.

    Raises:
        ValueError: If the file mode is unsupported.
    """

    path = Path(file_path) if isinstance(file_path, (str, Path)) else None

    if isinstance(data, str):
        try:
            data = repair_json(data)
        except Exception as ex:
            logger.error(f"Error converting string: {data}", ex, exc_info)
            return None

    data = _convert_to_dict(data)

    if mode not in {Config.MODE_WRITE, Config.MODE_APPEND_START, Config.MODE_APPEND_END}:
        mode = Config.MODE_WRITE

    existing_data = {}
    if path and path.exists() and mode in {Config.MODE_APPEND_START, Config.MODE_APPEND_END}:
        existing_data = _read_existing_data(path, exc_info)
    
    data = _merge_data(data, existing_data, mode)
    
    if path:
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            json.dump(data, path.open(mode, encoding="utf-8"), ensure_ascii=ensure_ascii, indent=4)
            #path.write_text(json.dumps(data, ensure_ascii=ensure_ascii, indent=4), encoding='utf-8')
        except Exception as ex:
             logger.error(f"Failed to write to {path}: ", ex, exc_info=exc_info)
             return None
        return data
    return data
```

**Назначение**: Записывает JSON-данные в файл или возвращает JSON-данные в виде словаря.

**Как работает функция**:
Функция преобразует входные данные (`data`) в формат JSON и записывает их в файл, если указан `file_path`. Если `file_path` не указан, функция возвращает JSON-данные в виде словаря. Функция поддерживает различные режимы записи (`Config.MODE_WRITE`, `Config.MODE_APPEND_START`, `Config.MODE_APPEND_END`) и обеспечивает обработку ошибок при записи данных. Если входные данные являются строкой, функция пытается исправить JSON с помощью `repair_json`.

**Параметры**:
- `data` (Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]): Данные, совместимые с JSON, или объекты SimpleNamespace для записи.
- `file_path` (Optional[Path], optional): Путь к выходному файлу. Если `None`, возвращает JSON как словарь. По умолчанию `None`.
- `ensure_ascii` (bool, optional): Если `True`, экранирует символы, не входящие в ASCII, в выводе. По умолчанию `False`.
- `mode` (str, optional): Режим открытия файла (`'w'`, `'a+'`, `'+a'`). По умолчанию `'w'`.
- `exc_info` (bool, optional): Если `True`, логирует исключения с трассировкой. По умолчанию `True`.

**Возвращает**:
- `Optional[Dict]`: JSON-данные в виде словаря в случае успеха или `None`, если произошла ошибка.

**Вызывает исключения**:
- `ValueError`: Если режим файла не поддерживается.

**Примеры**:

```python
from pathlib import Path
data = {'a': 1, 'b': 2}
file_path = Path('output.json')
result = j_dumps(data, file_path)
print(result)  # Вывод: {'a': 1, 'b': 2}
```

### `_decode_strings`

```python
def _decode_strings(data: Any) -> Any:
    """Recursively decode strings in a data structure."""
    if isinstance(data, str):
        try:
           return codecs.decode(data, 'unicode_escape')
        except Exception:
            return data
    if isinstance(data, list):\
        return [_decode_strings(item) for item in data]
    if isinstance(data, dict):
        return {\
            _decode_strings(key): _decode_strings(value) for key, value in data.items()\
        }
    return data
```

**Назначение**: Рекурсивно декодирует строки в структуре данных.

**Как работает функция**:
Функция рекурсивно проходит по структуре данных и пытается декодировать строки с использованием кодека `unicode_escape`. Если декодирование успешно, возвращается декодированная строка. Если происходит ошибка при декодировании, возвращается исходная строка.

**Параметры**:
- `data` (Any): Входные данные для декодирования.

**Возвращает**:
- `Any`: Декодированные данные.

**Примеры**:

```python
data = {'a': 'test\\u0020string', 'b': ['another\\u0020string']}
result = _decode_strings(data)
print(result)  # Вывод: {'a': 'test string', 'b': ['another string']}
```

### `_string_to_dict`

```python
def _string_to_dict(json_string: str) -> dict:
    """Remove markdown quotes and parse JSON string."""
    if json_string.startswith(("```", "```json")) and json_string.endswith(
        ("```", "```\\n")
    ):
        json_string = json_string.strip("`").replace("json", "", 1).strip()
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as ex:
        logger.error(f"JSON parsing error:\\n {json_string}", ex, False)
        return {}
```

**Назначение**: Удаляет маркеры Markdown и разбирает JSON-строку.

**Как работает функция**:
Функция принимает строку (`json_string`) в качестве входных данных и пытается удалить маркеры Markdown, такие как ```json, а затем разбирает строку как JSON. Если разбор JSON успешен, функция возвращает полученный словарь. В случае ошибки разбора JSON, функция записывает сообщение об ошибке в журнал и возвращает пустой словарь.

**Параметры**:
- `json_string` (str): JSON-строка для разбора.

**Возвращает**:
- `dict`: Словарь, полученный из JSON-строки, или пустой словарь в случае ошибки.

**Вызывает исключения**:
- `json.JSONDecodeError`: Если JSON-данные не могут быть разобраны.

**Примеры**:

```python
json_string = "```json\n{\"a\": 1, \"b\": 2}\n```"
result = _string_to_dict(json_string)
print(result)  # Вывод: {'a': 1, 'b': 2}
```

### `j_loads`

```python
def j_loads(
    jjson: Union[dict, SimpleNamespace, str, Path, list], ordered: bool = True
) -> Union[dict, list]:
    """
    Load JSON or CSV data from a file, directory, string, or object.

    Args:
        jjson (dict | SimpleNamespace | str | Path | list): Path to file/directory, JSON string, or JSON object.
        ordered (bool, optional): Use OrderedDict to preserve element order. Defaults to True.

    Returns:
        dict | list: Processed data (dictionary or list of dictionaries).

    Raises:
        FileNotFoundError: If the specified file is not found.
        json.JSONDecodeError: If the JSON data cannot be parsed.
    """
    try:
        if isinstance(jjson, SimpleNamespace):
            jjson = vars(jjson)

        if isinstance(jjson, Path):
            if jjson.is_dir():
                files = list(jjson.glob("*.json"))
                return [j_loads(file, ordered=ordered) for file in files]
            # if jjson.suffix.lower() == ".csv":
            #     return pd.read_csv(jjson).to_dict(orient="records")
             
            return json.loads(jjson.read_text(encoding="utf-8"))
        if isinstance(jjson, str):
            return _string_to_dict(jjson)
        if isinstance(jjson, list):
             return _decode_strings(jjson)
        if isinstance(jjson, dict):
            return _decode_strings(jjson)
    except FileNotFoundError:
        logger.error(f"File not found: {jjson}",None,False)
        return {}
    except json.JSONDecodeError as ex:
        logger.error(f"JSON parsing error:\\n{jjson}\\n", ex, False)
        return {}
    except Exception as ex:
        logger.error(f"Error loading data: ", ex, False)
        return {}
    return {}
```

**Назначение**: Загружает JSON или CSV данные из файла, каталога, строки или объекта.

**Как работает функция**:
Функция `j_loads` загружает данные из различных источников, таких как файлы, каталоги, JSON-строки или объекты Python. Она автоматически определяет тип входных данных и выполняет соответствующие действия для загрузки и разбора данных. Если указан путь к каталогу, функция загружает все JSON-файлы из этого каталога. Функция также поддерживает загрузку данных из объектов SimpleNamespace и JSON-строк. В случае возникновения ошибок функция записывает сообщение об ошибке в журнал и возвращает пустой словарь.

**Параметры**:
- `jjson` (dict | SimpleNamespace | str | Path | list): Путь к файлу/каталогу, JSON-строка или JSON-объект.
- `ordered` (bool, optional): Использовать `OrderedDict` для сохранения порядка элементов. По умолчанию `True`.

**Возвращает**:
- `dict | list`: Обработанные данные (словарь или список словарей).

**Вызывает исключения**:
- `FileNotFoundError`: Если указанный файл не найден.
- `json.JSONDecodeError`: Если JSON-данные не могут быть разобраны.

**Примеры**:

```python
from pathlib import Path
file_path = Path('config.json')
data = j_loads(file_path)
print(data)
```

### `j_loads_ns`

```python
def j_loads_ns(
    jjson: Union[Path, SimpleNamespace, Dict, str], ordered: bool = True
) -> Union[SimpleNamespace, List[SimpleNamespace], Dict]:
    """Load JSON/CSV data and convert to SimpleNamespace."""
    data = j_loads(jjson, ordered=ordered)
    if data:
        if isinstance(data, list):
            return [dict2ns(item) for item in data]
        return dict2ns(data)
    return {}
```

**Назначение**: Загружает JSON/CSV данные и преобразует их в SimpleNamespace.

**Как работает функция**:
Функция `j_loads_ns` загружает данные с использованием функции `j_loads` и преобразует их в объекты `SimpleNamespace`. Если загруженные данные являются списком, функция преобразует каждый элемент списка в объект `SimpleNamespace`. Если загруженные данные являются словарем, функция преобразует словарь в объект `SimpleNamespace`. В случае ошибки функция возвращает пустой словарь.

**Параметры**:
- `jjson` (Path | SimpleNamespace | Dict | str): Путь к файлу/каталогу, JSON-строка или JSON-объект.
- `ordered` (bool, optional): Использовать `OrderedDict` для сохранения порядка элементов. По умолчанию `True`.

**Возвращает**:
- `Union[SimpleNamespace, List[SimpleNamespace], Dict]`: Обработанные данные в виде объекта `SimpleNamespace`, списка объектов `SimpleNamespace` или словаря.

**Примеры**:

```python
from pathlib import Path
file_path = Path('config.json')
data = j_loads_ns(file_path)
print(data)
```