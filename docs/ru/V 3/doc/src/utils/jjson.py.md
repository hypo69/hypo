# Модуль для работы с JSON (`jjson.py`)

## Обзор

Модуль `jjson.py` предоставляет утилиты для работы с данными в формате JSON. Он включает функции для загрузки, выгрузки и обработки JSON-данных, а также для преобразования данных между различными форматами, такими как словари и объекты `SimpleNamespace`. Модуль обеспечивает удобный и надежный способ работы с JSON-данными в проекте `hypotez`.

## Подробней

Этот модуль предназначен для упрощения работы с JSON-данными в проекте `hypotez`. Он предоставляет функции для чтения и записи JSON-файлов, а также для преобразования данных между различными форматами. Это позволяет разработчикам легко интегрировать и использовать JSON-данные в своих приложениях. Модуль также включает обработку ошибок и ведение журнала, что упрощает отладку и обслуживание.

## Классы

### `Config`

**Описание**: Класс `Config` содержит константы, определяющие режимы записи файлов.

**Методы**:
- `MODE_WRITE`: Режим записи "w".
- `MODE_APPEND_START`: Режим добавления в начало файла "a+".
- `MODE_APPEND_END`: Режим добавления в конец файла "+a".

**Примеры**:
```python
from src.utils.jjson import Config

print(Config.MODE_WRITE)
print(Config.MODE_APPEND_START)
print(Config.MODE_APPEND_END)
```

## Функции

### `_convert_to_dict`

```python
def _convert_to_dict(value: Any) -> Any:
    """Convert SimpleNamespace and lists to dict."""
```

**Описание**: Преобразует объекты `SimpleNamespace` и списки в словари. Рекурсивно обрабатывает вложенные объекты и списки.

**Параметры**:
- `value` (Any): Значение для преобразования.

**Возвращает**:
- `Any`: Преобразованное значение в виде словаря или списка.

**Примеры**:
```python
from types import SimpleNamespace
from src.utils.jjson import _convert_to_dict

ns = SimpleNamespace(a=1, b=SimpleNamespace(c=2))
data = _convert_to_dict(ns)
print(data)  # {'a': 1, 'b': {'c': 2}}
```

### `_read_existing_data`

```python
def _read_existing_data(path: Path, exc_info: bool = True) -> dict:
    """Read existing JSON data from a file."""
```

**Описание**: Читает существующие JSON-данные из файла. Обрабатывает ошибки декодирования JSON и другие исключения, связанные с чтением файла.

**Параметры**:
- `path` (Path): Путь к файлу.
- `exc_info` (bool, optional): Если `True`, логирует исключения с трассировкой. По умолчанию `True`.

**Возвращает**:
- `dict`: Словарь с данными из файла или пустой словарь в случае ошибки.

**Вызывает исключения**:
- `json.JSONDecodeError`: Если возникает ошибка при декодировании JSON.
- `Exception`: Если возникает другая ошибка при чтении файла.

**Примеры**:
```python
from pathlib import Path
from src.utils.jjson import _read_existing_data

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

**Описание**: Объединяет новые данные с существующими данными в зависимости от режима (`mode`). Поддерживает режимы добавления в начало и в конец файла.

**Параметры**:
- `data` (Dict): Новые данные для добавления.
- `existing_data` (Dict): Существующие данные.
- `mode` (str): Режим объединения данных (`Config.MODE_APPEND_START` или `Config.MODE_APPEND_END`).

**Возвращает**:
- `Dict`: Объединенные данные в виде словаря.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при объединении данных.

**Примеры**:
```python
from src.utils.jjson import _merge_data, Config

data = {'new': 1}
existing_data = {'old': 2}
mode = Config.MODE_APPEND_END
merged_data = _merge_data(data, existing_data, mode)
print(merged_data)  # {'new': 1, 'old': 2}
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
    """
```

**Описание**: Записывает JSON-данные в файл или возвращает JSON-данные в виде словаря. Поддерживает различные режимы записи и обработку ошибок.

**Параметры**:
- `data` (Union[Dict, SimpleNamespace, List[Dict], List[SimpleNamespace]]): JSON-совместимые данные или объекты `SimpleNamespace` для записи.
- `file_path` (Optional[Path], optional): Путь к выходному файлу. Если `None`, возвращает JSON в виде словаря. По умолчанию `None`.
- `ensure_ascii` (bool, optional): Если `True`, экранирует не-ASCII символы в выводе. По умолчанию `False`.
- `mode` (str, optional): Режим открытия файла (`'w'`, `'a+'`, `'+a'`). По умолчанию `'w'`.
- `exc_info` (bool, optional): Если `True`, логирует исключения с трассировкой. По умолчанию `True`.

**Возвращает**:
- `Optional[Dict]`: JSON-данные в виде словаря при успехе или `None` в случае ошибки.

**Вызывает исключения**:
- `ValueError`: Если режим файла не поддерживается.

**Примеры**:
```python
from pathlib import Path
from src.utils.jjson import j_dumps

data = {'key': 'value'}
file_path = Path('output.json')
result = j_dumps(data, file_path=file_path)
print(result)  # {'key': 'value'}
```

### `_decode_strings`

```python
def _decode_strings(data: Any) -> Any:
    """Recursively decode strings in a data structure."""
```

**Описание**: Рекурсивно декодирует строки в структуре данных. Использует `codecs.decode` для обработки escape-последовательностей Unicode.

**Параметры**:
- `data` (Any): Данные для декодирования.

**Возвращает**:
- `Any`: Декодированные данные.

**Примеры**:
```python
from src.utils.jjson import _decode_strings

data = {'key': 'value\\u0020'}
decoded_data = _decode_strings(data)
print(decoded_data)  # {'key': 'value '}
```

### `_string_to_dict`

```python
def _string_to_dict(json_string: str) -> dict:
    """Remove markdown quotes and parse JSON string."""
```

**Описание**: Удаляет маркеры Markdown из JSON-строки и преобразует её в словарь.

**Параметры**:
- `json_string` (str): JSON-строка для преобразования.

**Возвращает**:
- `dict`: Словарь, полученный из JSON-строки.

**Вызывает исключения**:
- `json.JSONDecodeError`: Если возникает ошибка при парсинге JSON.

**Примеры**:
```python
from src.utils.jjson import _string_to_dict

json_string = "```json\n{\"key\": \"value\"}\n```"
data = _string_to_dict(json_string)
print(data)  # {'key': 'value'}
```

### `j_loads`

```python
def j_loads(
    jjson: Union[dict, SimpleNamespace, str, Path, list], ordered: bool = True
) -> Union[dict, list]:
    """
    Load JSON or CSV data from a file, directory, string, or object.
    """
```

**Описание**: Загружает JSON-данные из файла, директории, строки или объекта. Поддерживает чтение JSON и CSV файлов, а также обработку данных из различных источников.

**Параметры**:
- `jjson` (Union[dict, SimpleNamespace, str, Path, list]): Путь к файлу/директории, JSON-строка или JSON-объект.
- `ordered` (bool, optional): Использовать `OrderedDict` для сохранения порядка элементов. По умолчанию `True`.

**Возвращает**:
- `Union[dict, list]`: Обработанные данные (словарь или список словарей).

**Вызывает исключения**:
- `FileNotFoundError`: Если указанный файл не найден.
- `json.JSONDecodeError`: Если JSON-данные не могут быть распарсены.

**Примеры**:
```python
from pathlib import Path
from src.utils.jjson import j_loads

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

**Описание**: Загружает JSON/CSV-данные и преобразует их в объекты `SimpleNamespace`.

**Параметры**:
- `jjson` (Union[Path, SimpleNamespace, Dict, str]): Путь к файлу, объект `SimpleNamespace`, словарь или строка с JSON-данными.
- `ordered` (bool, optional): Использовать `OrderedDict` для сохранения порядка элементов. По умолчанию `True`.

**Возвращает**:
- `Union[SimpleNamespace, List[SimpleNamespace], Dict]`: Преобразованные данные в виде объекта `SimpleNamespace`, списка объектов `SimpleNamespace` или словаря.

**Примеры**:
```python
from pathlib import Path
from src.utils.jjson import j_loads_ns

file_path = Path('config.json')
data = j_loads_ns(file_path)
print(data)