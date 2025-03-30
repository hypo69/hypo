# Модуль для работы с JSON (`jjson`)

## Обзор

Модуль `jjson` предоставляет набор функций для работы с данными в формате JSON. Он включает в себя функции для загрузки, сохранения, преобразования и обработки JSON-данных. Модуль предназначен для упрощения работы с JSON-данными в проекте `hypotez`.

## Подробнее

Модуль `jjson` содержит функции для выполнения следующих задач:

-   Загрузка JSON-данных из файлов, строк или объектов.
-   Сохранение JSON-данных в файлы.
-   Преобразование данных между различными форматами, такими как `dict`, `SimpleNamespace` и `list`.
-   Обработка ошибок, связанных с JSON-данными, таких как ошибки декодирования и отсутствующие файлы.
-   Автоматическое исправление JSON-строк с использованием библиотеки `json_repair`.
-   Поддержка чтения JSON файлов из директории

Этот модуль используется для управления конфигурационными файлами, обмена данными между компонентами системы и хранения структурированных данных.

## Классы

### `Config`

**Описание**: Класс, содержащий константы для режимов записи файлов.

**Методы**:

-   `MODE_WRITE`: Режим записи "w".
-   `MODE_APPEND_START`: Режим добавления в начало файла "a+".
-   `MODE_APPEND_END`: Режим добавления в конец файла "+a".

**Примеры**:

```python
from src.utils.jjson import Config

print(Config.MODE_WRITE)
```

## Функции

### `_convert_to_dict`

```python
def _convert_to_dict(value: Any) -> Any:
    """Convert SimpleNamespace and lists to dict."""
```

**Описание**: Преобразует объекты `SimpleNamespace` и списки в словари.

**Параметры**:

*   `value` (Any): Значение для преобразования.

**Возвращает**:

*   `Any`: Преобразованное значение в виде словаря, списка или исходного типа данных.

**Примеры**:

```python
from types import SimpleNamespace
from src.utils.jjson import _convert_to_dict

ns = SimpleNamespace(a=1, b=2)
result = _convert_to_dict(ns)
print(result)  # Вывод: {'a': 1, 'b': 2}
```

### `_read_existing_data`

```python
def _read_existing_data(path: Path, exc_info: bool = True) -> dict:
    """Read existing JSON data from a file."""
```

**Описание**: Читает существующие JSON-данные из файла.

**Параметры**:

*   `path` (Path): Путь к файлу.
*   `exc_info` (bool, optional): Определяет, следует ли логировать исключения с трассировкой. По умолчанию `True`.

**Возвращает**:

*   `dict`: Словарь с данными из файла или пустой словарь в случае ошибки.

**Вызывает исключения**:

*   `json.JSONDecodeError`: Если возникает ошибка при декодировании JSON.

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

**Описание**: Объединяет новые данные с существующими данными в зависимости от режима.

**Параметры**:

*   `data` (Dict): Новые данные для объединения.
*   `existing_data` (Dict): Существующие данные.
*   `mode` (str): Режим объединения (`Config.MODE_APPEND_START` или `Config.MODE_APPEND_END`).

**Возвращает**:

*   `Dict`: Объединенные данные в виде словаря.

**Примеры**:

```python
from src.utils.jjson import _merge_data, Config

data = {'a': 1, 'b': 2}
existing_data = {'c': 3, 'd': 4}
mode = Config.MODE_APPEND_START
merged_data = _merge_data(data, existing_data, mode)
print(merged_data)
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

**Описание**: Сохраняет JSON-данные в файл или возвращает JSON-данные в виде словаря.

**Параметры**:

*   `data` (Dict | SimpleNamespace | List\[Dict] | List\[SimpleNamespace]): JSON-совместимые данные или объекты `SimpleNamespace` для сохранения.
*   `file_path` (Optional\[Path], optional): Путь к выходному файлу. Если `None`, возвращает JSON в виде словаря. По умолчанию `None`.
*   `ensure_ascii` (bool, optional): Если `True`, экранирует не-ASCII символы в выводе. По умолчанию `False`.
*   `mode` (str, optional): Режим открытия файла (`'w'`, `'a+'`, `'+a'`). По умолчанию `'w'`.
*   `exc_info` (bool, optional): Если `True`, логирует исключения с трассировкой. По умолчанию `True`.

**Возвращает**:

*   `Optional[Dict]`: JSON-данные в виде словаря в случае успеха или `None`, если произошла ошибка.

**Вызывает исключения**:

*   `ValueError`: Если указан неподдерживаемый режим файла.

**Примеры**:

```python
from pathlib import Path
from src.utils.jjson import j_dumps

data = {'a': 1, 'b': 2}
file_path = Path('output.json')
result = j_dumps(data, file_path)
print(result)
```

### `_decode_strings`

```python
def _decode_strings(data: Any) -> Any:
    """Recursively decode strings in a data structure."""
```

**Описание**: Рекурсивно декодирует строки в структуре данных.

**Параметры**:

*   `data` (Any): Данные для декодирования.

**Возвращает**:

*   `Any`: Декодированные данные.

**Примеры**:

```python
from src.utils.jjson import _decode_strings

data = {'a': 'строка'}
decoded_data = _decode_strings(data)
print(decoded_data)
```

### `_string_to_dict`

```python
def _string_to_dict(json_string: str) -> dict:
    """Remove markdown quotes and parse JSON string."""
```

**Описание**: Удаляет markdown-кавычки и разбирает JSON-строку.

**Параметры**:

*   `json_string` (str): JSON-строка для разбора.

**Возвращает**:

*   `dict`: Словарь, полученный из JSON-строки, или пустой словарь в случае ошибки.

**Примеры**:

```python
from src.utils.jjson import _string_to_dict

json_string = '{"a": 1, "b": 2}'
data = _string_to_dict(json_string)
print(data)
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

**Описание**: Загружает JSON-данные из файла, каталога, строки или объекта.

**Параметры**:

*   `jjson` (dict | SimpleNamespace | str | Path | list): Путь к файлу/каталогу, JSON-строка или JSON-объект.
*   `ordered` (bool, optional): Использовать `OrderedDict` для сохранения порядка элементов. По умолчанию `True`.

**Возвращает**:

*   `dict | list`: Обработанные данные (словарь или список словарей).

**Вызывает исключения**:

*   `FileNotFoundError`: Если указанный файл не найден.
*   `json.JSONDecodeError`: Если JSON-данные не могут быть разобраны.

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

**Описание**: Загружает JSON/CSV-данные и преобразует их в `SimpleNamespace`.

**Параметры**:

*   `jjson` (Path | SimpleNamespace | Dict | str): Путь к файлу, объект `SimpleNamespace`, словарь или строка.
*   `ordered` (bool, optional): Использовать `OrderedDict` для сохранения порядка элементов. По умолчанию `True`.

**Возвращает**:

*   `SimpleNamespace | List[SimpleNamespace] | Dict`: Преобразованные данные в виде `SimpleNamespace` или списка `SimpleNamespace`.

**Примеры**:

```python
from pathlib import Path
from src.utils.jjson import j_loads_ns

file_path = Path('config.json')
data = j_loads_ns(file_path)
print(data)