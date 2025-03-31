# Модуль для работы с JSON и файлами конфигурации `jjson`

## Обзор

Модуль `jjson` предоставляет инструменты для работы с JSON-данными, включая чтение, запись и преобразование данных между различными форматами, такими как словари, списки и объекты `SimpleNamespace`. Он также обеспечивает функциональность для работы с файлами конфигурации, поддерживая различные режимы записи и объединения данных.

## Подробней

Этот модуль предназначен для упрощения работы с JSON-данными и файлами конфигурации в проекте `hypotez`. Он предоставляет удобные функции для загрузки и сохранения JSON-данных, а также для преобразования данных между различными форматами. Модуль также содержит функции для обработки ошибок и ведения журнала, что упрощает отладку и сопровождение кода. Расположение модуля `hypotez/src/utils/jjson.py` указывает на то, что он является частью подсистемы `utils`, предоставляющей вспомогательные функции для других модулей проекта.

## Классы

### `Config`

**Описание**: Класс, содержащий константы для режимов записи файлов.

**Как работает класс**:
Класс `Config` определяет константы, представляющие различные режимы записи файлов, используемые в функциях модуля `jjson`. Он содержит три статических атрибута: `MODE_WRITE`, `MODE_APPEND_START` и `MODE_APPEND_END`, которые определяют режимы записи, перезаписи и добавления данных в файл соответственно.

**Методы**:
- `MODE_WRITE:str`: Режим записи "w".
- `MODE_APPEND_START:str`: Режим добавления в начало файла "a+".
- `MODE_APPEND_END:str`: Режим добавления в конец файла "+a".

## Функции

### `_convert_to_dict`

```python
def _convert_to_dict(value: Any) -> Any:
    """Convert SimpleNamespace and lists to dict."""
```

**Описание**: Преобразует объекты `SimpleNamespace` и списки в словари.

**Как работает функция**:
Функция `_convert_to_dict` рекурсивно преобразует объекты `SimpleNamespace`, словари и списки в словари. Если входное значение является экземпляром `SimpleNamespace` или словарем, функция итерируется по его элементам и рекурсивно вызывает себя для каждого значения. Если входное значение является списком, функция рекурсивно вызывает себя для каждого элемента списка. В противном случае функция возвращает входное значение без изменений.

**Параметры**:
- `value` (Any): Значение для преобразования.

**Возвращает**:
- `Any`: Преобразованное значение в виде словаря, списка или исходного значения.

**Примеры**:
```python
from types import SimpleNamespace
data = SimpleNamespace(a=1, b='test', c=[2, 3])
result = _convert_to_dict(data)
print(result)  # Вывод: {'a': 1, 'b': 'test', 'c': [2, 3]}
```

### `_read_existing_data`

```python
def _read_existing_data(path: Path, exc_info: bool = True) -> dict:
    """Read existing JSON data from a file."""
```

**Описание**: Считывает существующие JSON-данные из файла.

**Как работает функция**:
Функция `_read_existing_data` пытается прочитать JSON-данные из файла, указанного в параметре `path`. Если файл существует и содержит допустимые JSON-данные, функция возвращает словарь, представляющий эти данные. В случае возникновения ошибок при чтении или разборе JSON-данных, функция регистрирует ошибку с помощью модуля `logger` и возвращает пустой словарь. Параметр `exc_info` определяет, следует ли включать информацию об исключении в журнал ошибок.

**Параметры**:
- `path` (Path): Путь к файлу.
- `exc_info` (bool, optional): Определяет, следует ли включать информацию об исключении в журнал ошибок. По умолчанию `True`.

**Возвращает**:
- `dict`: Словарь, представляющий JSON-данные, или пустой словарь в случае ошибки.

**Вызывает исключения**:
- `json.JSONDecodeError`: Возникает при ошибке декодирования JSON-данных.
- `Exception`: Возникает при любой другой ошибке при чтении файла.

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
```

**Описание**: Объединяет новые данные с существующими данными в зависимости от режима.

**Как работает функция**:
Функция `_merge_data` объединяет новые данные (`data`) с существующими данными (`existing_data`) в зависимости от указанного режима (`mode`). Если режим равен `Config.MODE_APPEND_START`, новые данные добавляются в начало существующих данных. Если режим равен `Config.MODE_APPEND_END`, новые данные добавляются в конец существующих данных. Если режим не указан или не поддерживается, новые данные заменяют существующие данные. Функция обрабатывает как списки, так и словари. В случае возникновения ошибок при объединении данных, функция регистрирует ошибку с помощью модуля `logger` и возвращает пустой словарь.

**Параметры**:
- `data` (Dict): Новые данные для объединения.
- `existing_data` (Dict): Существующие данные.
- `mode` (str): Режим объединения данных (`Config.MODE_APPEND_START`, `Config.MODE_APPEND_END` или любой другой).

**Возвращает**:
- `Dict`: Объединенные данные в виде словаря.

**Вызывает исключения**:
- `Exception`: Возникает при любой ошибке при объединении данных.

**Примеры**:
```python
data = {'new_key': 'new_value'}
existing_data = {'existing_key': 'existing_value'}
mode = Config.MODE_APPEND_END
merged_data = _merge_data(data, existing_data, mode)
print(merged_data)  # Вывод: {'new_key': 'new_value', 'existing_key': 'existing_value'}
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
```

**Описание**: Записывает JSON-данные в файл или возвращает JSON-данные в виде словаря.

**Как работает функция**:
Функция `j_dumps` принимает JSON-совместимые данные (словарь, `SimpleNamespace`, список словарей или список `SimpleNamespace`) и записывает их в файл, указанный в параметре `file_path`. Если `file_path` не указан, функция возвращает JSON-данные в виде словаря. Функция поддерживает различные режимы записи (`'w'`, `'a+'`, `'+a'`), которые определяют, как данные будут записаны в файл (перезапись, добавление в начало или добавление в конец). Функция также позволяет указать, следует ли экранировать не-ASCII символы при записи в файл. В случае возникновения ошибок при записи данных в файл, функция регистрирует ошибку с помощью модуля `logger` и возвращает `None`.

**Параметры**:
- `data` (Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]): JSON-совместимые данные или объекты `SimpleNamespace` для записи.
- `file_path` (Optional[Path], optional): Путь к выходному файлу. Если `None`, возвращает JSON в виде словаря. По умолчанию `None`.
- `ensure_ascii` (bool, optional): Если `True`, экранирует не-ASCII символы в выходных данных. По умолчанию `True`.
- `mode` (str, optional): Режим открытия файла (`'w'`, `'a+'`, `'+a'`). По умолчанию `'w'`.
- `exc_info` (bool, optional): Если `True`, регистрирует исключения с трассировкой. По умолчанию `True`.

**Возвращает**:
- `Optional[Dict]`: JSON-данные в виде словаря в случае успеха или `None` в случае ошибки.

**Вызывает исключения**:
- `ValueError`: Если режим файла не поддерживается.

**Примеры**:
```python
from pathlib import Path
data = {'key': 'value'}
file_path = Path('output.json')
result = j_dumps(data, file_path=file_path, ensure_ascii=False, mode='w')
print(result)  # Вывод: {'key': 'value'}
```

### `_decode_strings`

```python
def _decode_strings(data: Any) -> Any:
    """Recursively decode strings in a data structure."""
```

**Описание**: Рекурсивно декодирует строки в структуре данных.

**Как работает функция**:
Функция `_decode_strings` рекурсивно декодирует строки в структуре данных, используя кодек `unicode_escape`. Если входное значение является строкой, функция пытается декодировать ее. Если входное значение является списком или словарем, функция рекурсивно вызывает себя для каждого элемента списка или значения словаря. В противном случае функция возвращает входное значение без изменений.

**Параметры**:
- `data` (Any): Данные для декодирования.

**Возвращает**:
- `Any`: Декодированные данные.

**Примеры**:
```python
data = {'key': 'value with unicode \\u0410'}
result = _decode_strings(data)
print(result)  # Вывод: {'key': 'value with unicode А'}
```

### `_string_to_dict`

```python
def _string_to_dict(json_string: str) -> dict:
    """Remove markdown quotes and parse JSON string."""
```

**Описание**: Удаляет кавычки Markdown и разбирает JSON-строку.

**Как работает функция**:
Функция `_string_to_dict` принимает строку, содержащую JSON-данные, и пытается преобразовать ее в словарь. Если строка начинается и заканчивается кавычками Markdown (``` или ```json), функция удаляет эти кавычки и пробелы. Затем функция использует `json.loads` для разбора JSON-строки и возвращает полученный словарь. В случае возникновения ошибок при разборе JSON-данных, функция регистрирует ошибку с помощью модуля `logger` и возвращает пустой словарь.

**Параметры**:
- `json_string` (str): Строка, содержащая JSON-данные.

**Возвращает**:
- `dict`: Словарь, представляющий JSON-данные, или пустой словарь в случае ошибки.

**Вызывает исключения**:
- `json.JSONDecodeError`: Возникает при ошибке разбора JSON-данных.

**Примеры**:
```python
json_string = "```json\n{\"key\": \"value\"}\n```"
result = _string_to_dict(json_string)
print(result)  # Вывод: {'key': 'value'}
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
```

**Описание**: Загружает JSON-данные из файла, каталога, строки или объекта.

**Как работает функция**:
Функция `j_loads` загружает JSON-данные из различных источников, таких как файл, каталог, строка или объект. Функция определяет тип входных данных и выполняет соответствующие действия для загрузки и разбора JSON-данных. Если входные данные являются путем к файлу, функция проверяет, является ли путь каталогом или файлом. Если это каталог, функция загружает все JSON-файлы в каталоге. Если это файл, функция загружает JSON-данные из файла. Если входные данные являются строкой, функция разбирает JSON-строку. Если входные данные являются списком или словарем, функция рекурсивно декодирует строки в структуре данных. В случае возникновения ошибок при загрузке или разборе JSON-данных, функция регистрирует ошибку с помощью модуля `logger` и возвращает пустой словарь.

**Параметры**:
- `jjson` (dict | SimpleNamespace | str | Path | list): Путь к файлу/каталогу, JSON-строка или JSON-объект.
- `ordered` (bool, optional): Использовать `OrderedDict` для сохранения порядка элементов. По умолчанию `True`.

**Возвращает**:
- `dict | list`: Обработанные данные (словарь или список словарей).

**Вызывает исключения**:
- `FileNotFoundError`: Если указанный файл не найден.
- `json.JSONDecodeError`: Если не удается разобрать JSON-данные.

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
```

**Описание**: Загружает JSON/CSV-данные и преобразует их в `SimpleNamespace`.

**Как работает функция**:
Функция `j_loads_ns` загружает JSON-данные с использованием функции `j_loads` и преобразует их в объекты `SimpleNamespace`. Если загруженные данные являются списком, функция преобразует каждый элемент списка в объект `SimpleNamespace`. Если загруженные данные являются словарем, функция преобразует словарь в объект `SimpleNamespace`. В случае возникновения ошибок при загрузке данных, функция возвращает пустой словарь.

**Параметры**:
- `jjson` (Path | SimpleNamespace | Dict | str): Путь к файлу, объект `SimpleNamespace`, словарь или строка, содержащая JSON-данные.
- `ordered` (bool, optional): Использовать `OrderedDict` для сохранения порядка элементов. По умолчанию `True`.

**Возвращает**:
- `SimpleNamespace | List[SimpleNamespace] | Dict`: Объект `SimpleNamespace`, список объектов `SimpleNamespace` или словарь.

**Примеры**:
```python
from pathlib import Path
file_path = Path('config.json')
data = j_loads_ns(file_path)
print(data)