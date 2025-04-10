# Модуль для работы с JSON и SimpleNamespace объектами
====================================================

Модуль содержит функции для загрузки и выгрузки данных в формате JSON, а также для преобразования данных в объекты SimpleNamespace.
Он предоставляет удобные инструменты для работы с конфигурационными файлами и другими данными, представленными в формате JSON.

## Оглавление

- [Обзор](#обзор)
- [Подробнее](#подробнее)
- [Классы](#классы)
    - [Config](#config)
- [Функции](#функции)
    - [_convert_to_dict](#_convert_to_dict)
    - [_read_existing_data](#_read_existing_data)
    - [_merge_data](#_merge_data)
    - [j_dumps](#j_dumps)
    - [_decode_strings](#_decode_strings)
    - [_string_to_dict](#_string_to_dict)
    - [j_loads](#j_loads)
    - [j_loads_ns](#j_loads_ns)

## Обзор

Модуль `jjson` предоставляет функции для работы с данными в формате JSON. Он включает в себя функции для загрузки данных из файлов, строк и объектов, а также для выгрузки данных в файлы. Кроме того, модуль содержит функции для преобразования данных в объекты `SimpleNamespace`, что упрощает доступ к данным по атрибутам.

## Подробнее

Модуль предназначен для упрощения работы с JSON-данными в проекте `hypotez`. Он предоставляет функции для чтения, записи и преобразования данных, а также обеспечивает обработку ошибок и логирование. Использование данного модуля позволяет унифицировать работу с JSON-данными и упростить код.

## Классы

### `Config`

**Описание**: Класс, содержащий константы для режимов записи файлов.

**Аттрибуты**:
- `MODE_WRITE` (str): Режим записи "w".
- `MODE_APPEND_START` (str): Режим записи "a+".
- `MODE_APPEND_END` (str): Режим записи "+a".

## Функции

### `_convert_to_dict`

```python
def _convert_to_dict(value: Any) -> Any:
    """ Функция преобразует SimpleNamespace объекты и списки в словари.
    Args:
        value (Any): Значение, которое нужно преобразовать.

    Returns:
        Any: Преобразованное значение в виде словаря или списка.
    """
```

**Назначение**: Преобразует объекты `SimpleNamespace` и списки в словари рекурсивно.

**Параметры**:
- `value` (Any): Значение, которое нужно преобразовать. Может быть объектом `SimpleNamespace`, словарем, списком или другим типом данных.

**Возвращает**:
- `Any`: Преобразованное значение в виде словаря, списка или исходного значения, если оно не требует преобразования.

**Как работает функция**:

1. **Проверка типа**: Функция проверяет тип входного значения `value`.
2. **Преобразование SimpleNamespace**: Если `value` является экземпляром `SimpleNamespace`, функция преобразует его в словарь, рекурсивно применяя `_convert_to_dict` к каждому значению атрибута.
3. **Преобразование словаря**: Если `value` является словарем, функция создает новый словарь, рекурсивно применяя `_convert_to_dict` к каждому значению.
4. **Преобразование списка**: Если `value` является списком, функция создает новый список, рекурсивно применяя `_convert_to_dict` к каждому элементу.
5. **Возврат значения**: Если `value` не является ни `SimpleNamespace`, ни словарем, ни списком, функция возвращает его без изменений.

```
A: Проверка типа value
|
├── SimpleNamespace? --> B: Преобразование SimpleNamespace в словарь
|   |
|   └── Рекурсивный вызов _convert_to_dict для каждого значения
|
├── dict? --> C: Преобразование словаря
|   |
|   └── Рекурсивный вызов _convert_to_dict для каждого значения
|
├── list? --> D: Преобразование списка
|   |
|   └── Рекурсивный вызов _convert_to_dict для каждого элемента
|
└── E: Возврат value без изменений
```

**Примеры**:

```python
from types import SimpleNamespace

# Пример 1: Преобразование SimpleNamespace в словарь
ns = SimpleNamespace(name='John', age=30)
result = _convert_to_dict(ns)
print(result)  # Вывод: {'name': 'John', 'age': 30}

# Пример 2: Преобразование списка, содержащего SimpleNamespace объекты
data = [SimpleNamespace(name='John', age=30), SimpleNamespace(name='Jane', age=25)]
result = _convert_to_dict(data)
print(result)  # Вывод: [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}]

# Пример 3: Преобразование вложенных структур
data = {'person': SimpleNamespace(name='John', age=30, address={'city': 'New York'})}
result = _convert_to_dict(data)
print(result)  # Вывод: {'person': {'name': 'John', 'age': 30, 'address': {'city': 'New York'}}}
```

### `_read_existing_data`

```python
def _read_existing_data(path: Path, exc_info: bool = True) -> dict:
    """Чтение существующих данных JSON из файла.
    Args:
        path (Path): Путь к файлу.
        exc_info (bool, optional): Если True, регистрирует исключения с трассировкой. По умолчанию True.

    Returns:
        dict: Данные JSON в виде словаря или пустой словарь в случае ошибки.
    """
```

**Назначение**: Читает существующие JSON данные из файла.

**Параметры**:
- `path` (Path): Путь к файлу.
- `exc_info` (bool, optional): Если `True`, то в случае возникновения исключения будет выводиться полная информация об ошибке, включая трассировку стека. По умолчанию `True`.

**Возвращает**:
- `dict`: Данные JSON в виде словаря. В случае возникновения ошибки возвращает пустой словарь `{}`.

**Вызывает исключения**:
- `json.JSONDecodeError`: Если не удается декодировать JSON из файла.
- `Exception`: При возникновении любой другой ошибки при чтении файла.

**Как работает функция**:

1. **Чтение данных из файла**: Функция пытается прочитать содержимое файла, указанного в параметре `path`, используя кодировку UTF-8.
2. **Декодирование JSON**: Функция пытается декодировать прочитанные данные из формата JSON в словарь.
3. **Обработка ошибок**:
   - Если происходит ошибка `json.JSONDecodeError` при декодировании JSON, функция логирует ошибку с использованием `logger.error` и возвращает пустой словарь.
   - Если происходит любая другая ошибка при чтении файла, функция логирует ошибку и возвращает пустой словарь.

```
A: Попытка чтения данных из файла
|
├── Успешно --> B: Попытка декодирования JSON
|   |
|   ├── Успешно --> C: Возврат данных в виде словаря
|   |
|   └── Ошибка JSONDecodeError --> D: Логирование ошибки и возврат пустого словаря
|
└── Ошибка чтения файла --> E: Логирование ошибки и возврат пустого словаря
```

**Примеры**:

```python
from pathlib import Path

# Пример 1: Чтение существующего JSON файла
file_path = Path('config.json')
# Создаем файл config.json с содержимым {"name": "John", "age": 30}
file_path.write_text('{"name": "John", "age": 30}', encoding='utf-8')
data = _read_existing_data(file_path)
print(data)  # Вывод: {'name': 'John', 'age': 30}

# Пример 2: Обработка несуществующего файла
file_path = Path('nonexistent.json')
data = _read_existing_data(file_path)
print(data)  # Вывод: {}

# Пример 3: Обработка файла с некорректным JSON
file_path = Path('invalid.json')
file_path.write_text('{"name": "John", "age": 30', encoding='utf-8')  # Некорректный JSON
data = _read_existing_data(file_path)
print(data)  # Вывод: {}
```

### `_merge_data`

```python
def _merge_data(data: Dict, existing_data: Dict, mode: str) -> Dict:
    """Объединяет новые данные с существующими в зависимости от режима.
    Args:
        data (Dict): Новые данные для объединения.
        existing_data (Dict): Существующие данные.
        mode (str): Режим объединения ('w', 'a+', '+a').

    Returns:
        Dict: Объединенные данные.
    """
```

**Назначение**: Объединяет новые данные с существующими данными в зависимости от указанного режима.

**Параметры**:
- `data` (Dict): Новые данные для объединения.
- `existing_data` (Dict): Существующие данные, с которыми нужно объединить новые данные.
- `mode` (str): Режим объединения. Возможные значения:
  - `Config.MODE_WRITE` ("w"): Записывает новые данные, перезаписывая существующие.
  - `Config.MODE_APPEND_START` ("a+"): Добавляет новые данные в начало существующих.
  - `Config.MODE_APPEND_END` ("+a"): Добавляет новые данные в конец существующих.

**Возвращает**:
- `Dict`: Объединенные данные в виде словаря. В случае возникновения ошибки возвращает пустой словарь `{}`.

**Как работает функция**:

1. **Проверка режима**: Функция проверяет значение параметра `mode` и выполняет соответствующие действия в зависимости от режима.
2. **Режим `Config.MODE_APPEND_START`**:
   - Если `data` и `existing_data` являются списками, функция объединяет их, добавляя `data` в начало `existing_data`.
   - Если `data` и `existing_data` являются словарями, функция обновляет `existing_data` данными из `data`.
   - Возвращает `existing_data`.
3. **Режим `Config.MODE_APPEND_END`**:
   - Если `data` и `existing_data` являются списками, функция объединяет их, добавляя `data` в конец `existing_data`.
   - Если `data` и `existing_data` являются словарями, функция обновляет `data` данными из `existing_data`.
   - Возвращает `data`.
4. **Режим по умолчанию**: Если `mode` не соответствует ни одному из известных режимов, функция возвращает `data` без изменений.
5. **Обработка ошибок**: Если в процессе объединения данных возникает исключение, функция логирует ошибку и возвращает пустой словарь.

```
A: Проверка режима mode
|
├── MODE_APPEND_START? --> B: Обработка режима MODE_APPEND_START
|   |
|   ├── data и existing_data - списки? --> C: Объединение списков (data + existing_data)
|   |   |
|   |   └── Возврат объединенного списка
|   |
|   ├── data и existing_data - словари? --> D: Обновление existing_data данными из data
|   |   |
|   |   └── Возврат existing_data
|   |
|   └── Возврат existing_data
|
├── MODE_APPEND_END? --> E: Обработка режима MODE_APPEND_END
|   |
|   ├── data и existing_data - списки? --> F: Объединение списков (existing_data + data)
|   |   |
|   |   └── Возврат объединенного списка
|   |
|   ├── data и existing_data - словари? --> G: Обновление data данными из existing_data
|   |   |
|   |   └── Возврат data
|   |
|   └── Возврат data
|
└── H: Возврат data без изменений (режим по умолчанию)
```

**Примеры**:

```python
# Пример 1: Объединение словарей в режиме MODE_APPEND_START
data = {'name': 'John', 'age': 30}
existing_data = {'city': 'New York'}
mode = Config.MODE_APPEND_START
result = _merge_data(data, existing_data, mode)
print(result)  # Вывод: {'city': 'New York', 'name': 'John', 'age': 30}

# Пример 2: Объединение списков в режиме MODE_APPEND_END
data = [1, 2, 3]
existing_data = [4, 5, 6]
mode = Config.MODE_APPEND_END
result = _merge_data(data, existing_data, mode)
print(result)  # Вывод: [4, 5, 6, 1, 2, 3]

# Пример 3: Объединение данных в режиме по умолчанию (MODE_WRITE)
data = {'name': 'John', 'age': 30}
existing_data = {'city': 'New York'}
mode = Config.MODE_WRITE
result = _merge_data(data, existing_data, mode)
print(result)  # Вывод: {'name': 'John', 'age': 30}
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
    Записывает JSON данные в файл или возвращает JSON данные в виде словаря.

    Args:
        data (Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]): JSON-совместимые данные или объекты SimpleNamespace для записи.
        file_path (Optional[Path], optional): Путь к выходному файлу. Если None, возвращает JSON как словарь. По умолчанию None.
        ensure_ascii (bool, optional): Если True, экранирует не-ASCII символы в выводе. По умолчанию True.
        mode (str, optional): Режим открытия файла ('w', 'a+', '+a'). По умолчанию 'w'.
        exc_info (bool, optional): Если True, логирует исключения с трассировкой. По умолчанию True.

    Returns:
        Optional[Dict]: JSON данные в виде словаря, если успешно, или None, если произошла ошибка.

    Raises:
        ValueError: Если режим файла не поддерживается.
    """
```

**Назначение**: Записывает JSON данные в файл или возвращает JSON данные в виде словаря.

**Параметры**:
- `data` (Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]): JSON-совместимые данные или объекты `SimpleNamespace` для записи.
- `file_path` (Optional[Path], optional): Путь к выходному файлу. Если `None`, функция возвращает JSON данные в виде словаря. По умолчанию `None`.
- `ensure_ascii` (bool, optional): Если `True`, функция экранирует не-ASCII символы в выводе. По умолчанию `True`.
- `mode` (str, optional): Режим открытия файла (`'w'`, `'a+'`, `'+a'`). По умолчанию `'w'`.
- `exc_info` (bool, optional): Если `True`, функция логирует исключения с трассировкой стека. По умолчанию `True`.

**Возвращает**:
- `Optional[Dict]`: JSON данные в виде словаря, если запись прошла успешно. Если произошла ошибка, функция возвращает `None`. Если `file_path` равен `None`, функция возвращает JSON данные в виде словаря.

**Вызывает исключения**:
- `ValueError`: Если режим файла не поддерживается.

**Как работает функция**:

1. **Преобразование данных**: Функция преобразует входные данные `data` в словарь с помощью функции `_convert_to_dict`. Если `data` является строкой, функция пытается исправить JSON с помощью `repair_json`.
2. **Выбор режима**: Функция проверяет, что режим `mode` является одним из допустимых (`'w'`, `'a+'`, `'+a'`). Если режим не поддерживается, устанавливается режим по умолчанию `'w'`.
3. **Чтение существующих данных**: Если указан путь к файлу и режим является `'a+'` или `'+a'`, функция читает существующие данные из файла с помощью функции `_read_existing_data`.
4. **Объединение данных**: Функция объединяет новые данные с существующими данными с помощью функции `_merge_data`.
5. **Запись в файл**: Если указан путь к файлу, функция записывает объединенные данные в файл в формате JSON с отступами и кодировкой UTF-8. Если `ensure_ascii` равен `True`, функция экранирует не-ASCII символы.
6. **Обработка ошибок**: Если в процессе записи в файл возникает исключение, функция логирует ошибку и возвращает `None`.
7. **Возврат данных**: Если запись в файл прошла успешно или `file_path` равен `None`, функция возвращает JSON данные в виде словаря.

```
A: Преобразование данных в словарь
|
├── Данные - строка? --> B: Попытка исправить JSON
|   |
|   └── Успешно/Ошибка --> C: Продолжение
|
└── C: Проверка режима mode
|
├── Режим поддерживается? --> D: Чтение существующих данных (если необходимо)
|   |
|   └── E: Объединение данных
|
└── F: Запись данных в файл (если указан file_path)
|
└── G: Возврат данных в виде словаря
```

**Примеры**:

```python
from pathlib import Path
from types import SimpleNamespace

# Пример 1: Запись данных в файл
data = {'name': 'John', 'age': 30}
file_path = Path('data.json')
result = j_dumps(data, file_path=file_path)
print(result)  # Вывод: {'name': 'John', 'age': 30}

# Пример 2: Запись данных в файл с экранированием не-ASCII символов
data = {'name': 'Иван', 'age': 30}
file_path = Path('data_ascii.json')
result = j_dumps(data, file_path=file_path, ensure_ascii=True)
print(result)  # Вывод: {'name': '\\u0418\\u0432\\u0430\\u043d', 'age': 30}

# Пример 3: Возврат данных в виде словаря
data = {'name': 'John', 'age': 30}
result = j_dumps(data)
print(result)  # Вывод: {'name': 'John', 'age': 30}

# Пример 4: Запись SimpleNamespace объекта в файл
data = SimpleNamespace(name='John', age=30)
file_path = Path('data_ns.json')
result = j_dumps(data, file_path=file_path)
print(result)  # Вывод: {'name': 'John', 'age': 30}
```

### `_decode_strings`

```python
def _decode_strings(data: Any) -> Any:
    """Рекурсивно декодирует строки в структуре данных."""
```

**Назначение**: Рекурсивно декодирует строки в структуре данных, используя кодировку `unicode_escape`.

**Параметры**:
- `data` (Any): Структура данных, в которой необходимо декодировать строки. Может быть строкой, списком, словарем или другим типом данных.

**Возвращает**:
- `Any`: Структура данных с декодированными строками. Если входные данные не являются строкой, списком или словарем, функция возвращает их без изменений.

**Как работает функция**:

1. **Проверка типа данных**: Функция проверяет тип входных данных `data`.
2. **Декодирование строки**: Если `data` является строкой, функция пытается декодировать ее с использованием кодировки `unicode_escape`. Если декодирование не удается, функция возвращает исходную строку без изменений.
3. **Декодирование списка**: Если `data` является списком, функция рекурсивно вызывает `_decode_strings` для каждого элемента списка и возвращает новый список с декодированными элементами.
4. **Декодирование словаря**: Если `data` является словарем, функция рекурсивно вызывает `_decode_strings` для каждого ключа и значения словаря и возвращает новый словарь с декодированными ключами и значениями.
5. **Возврат данных без изменений**: Если `data` не является строкой, списком или словарем, функция возвращает `data` без изменений.

```
A: Проверка типа данных data
|
├── Строка? --> B: Попытка декодирования строки
|   |
|   └── Успешно/Ошибка --> C: Возврат декодированной/исходной строки
|
├── Список? --> D: Рекурсивная обработка списка
|   |
|   └── Возврат списка с декодированными элементами
|
├── Словарь? --> E: Рекурсивная обработка словаря
|   |
|   └── Возврат словаря с декодированными ключами и значениями
|
└── Возврат данных без изменений
```

**Примеры**:

```python
# Пример 1: Декодирование строки
data = 'Пример строки с \\u044d\\u043a\\u0440\\u0430\\u043d\\u0438\\u0440\\u043e\\u0432\\u0430\\u043d\\u043d\\u044b\\u043c\\u0438 символами'
result = _decode_strings(data)
print(result)  # Вывод: Пример строки с экранированными символами

# Пример 2: Декодирование списка строк
data = ['\\u041f\\u0440\\u0438\\u043c\\u0435\\u0440 1', '\\u041f\\u0440\\u0438\\u043c\\u0435\\u0440 2']
result = _decode_strings(data)
print(result)  # Вывод: ['Пример 1', 'Пример 2']

# Пример 3: Декодирование словаря
data = {'ключ': '\\u0417\\u043d\\u0430\\u0447\\u0435\\u043d\\u0438\\u0435'}
result = _decode_strings(data)
print(result)  # Вывод: {'ключ': 'Значение'}
```

### `_string_to_dict`

```python
def _string_to_dict(json_string: str) -> dict:
    """Удаляет markdown кавычки и преобразует JSON строку в словарь."""
```

**Назначение**: Удаляет markdown кавычки (```json) и преобразует JSON строку в словарь.

**Параметры**:
- `json_string` (str): JSON строка, которую необходимо преобразовать.

**Возвращает**:
- `dict`: Словарь, полученный из JSON строки. В случае ошибки парсинга возвращает пустой словарь `{}`.

**Как работает функция**:

1. **Удаление markdown кавычек**: Функция проверяет, начинается ли строка с "```" или "```json" и заканчивается ли на "```" или "```\n". Если это так, функция удаляет эти кавычки и префикс "json" (если он есть) из строки.
2. **Парсинг JSON**: Функция пытается преобразовать очищенную строку в словарь с помощью `json.loads`.
3. **Обработка ошибок**: Если происходит ошибка `json.JSONDecodeError` при парсинге JSON, функция логирует ошибку с использованием `logger.error` и возвращает пустой словарь.

```
A: Проверка наличия markdown кавычек
|
├── Кавычки есть --> B: Удаление кавычек и префикса "json"
|   |
|   └── C: Попытка парсинга JSON
|
└── Кавычек нет --> C: Попытка парсинга JSON
|
├── Успешно --> D: Возврат словаря
|
└── Ошибка JSONDecodeError --> E: Логирование ошибки и возврат пустого словаря
```

**Примеры**:

```python
# Пример 1: Преобразование JSON строки с markdown кавычками
json_string = "```json\n{\"name\": \"John\", \"age\": 30}\n```"
result = _string_to_dict(json_string)
print(result)  # Вывод: {'name': 'John', 'age': 30}

# Пример 2: Преобразование JSON строки без markdown кавычек
json_string = "{\"name\": \"John\", \"age\": 30}"
result = _string_to_dict(json_string)
print(result)  # Вывод: {'name': 'John', 'age': 30}

# Пример 3: Обработка некорректной JSON строки
json_string = "{\"name\": \"John\", \"age\": 30"  # Некорректный JSON
result = _string_to_dict(json_string)
print(result)  # Вывод: {}
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
    """
```

**Назначение**: Загружает JSON данные из различных источников, таких как файлы, директории, строки или объекты, и преобразует их в словарь или список.

**Параметры**:
- `jjson` (Union[dict, SimpleNamespace, str, Path, list]): Источник JSON данных. Может быть:
  - `dict`: Словарь с данными.
  - `SimpleNamespace`: Объект SimpleNamespace с данными.
  - `str`: Строка, содержащая JSON данные.
  - `Path`: Путь к файлу или директории с JSON данными.
  - `list`: Список с данными.
- `ordered` (bool, optional): Определяет, нужно ли использовать `OrderedDict` для сохранения порядка элементов в словаре. По умолчанию `True`.

**Возвращает**:
- `Union[dict, list]`: Обработанные данные в виде словаря или списка словарей. Если происходит ошибка, функция возвращает пустой словарь `{}`.

**Вызывает исключения**:
- `FileNotFoundError`: Если указанный файл не найден.
- `json.JSONDecodeError`: Если JSON данные не могут быть распарсены.

**Как работает функция**:

1. **Преобразование SimpleNamespace**: Если `jjson` является объектом `SimpleNamespace`, он преобразуется в словарь с помощью `vars(jjson)`.
2. **Обработка типа Path**: Если `jjson` является объектом `Path`:
   - Если это директория, функция рекурсивно вызывает `j_loads` для каждого файла `.json` в этой директории и возвращает список результатов.
   - Если это файл, функция читает его содержимое и преобразует в JSON.
3. **Обработка строки**: Если `jjson` является строкой, функция преобразует ее в словарь с помощью `_string_to_dict`.
4. **Обработка списка**: Если `jjson` является списком, функция декодирует строки в списке с помощью `_decode_strings`.
5. **Обработка словаря**: Если `jjson` является словарем, функция декодирует строки в словаре с помощью `_decode_strings`.
6. **Обработка ошибок**:
   - Если файл не найден (`FileNotFoundError`), функция логирует ошибку и возвращает пустой словарь.
   - Если JSON данные не могут быть распарсены (`json.JSONDecodeError`), функция логирует ошибку и возвращает пустой словарь.
   - Если возникает любая другая ошибка, функция логирует ошибку и возвращает пустой словарь.

```
A: Проверка типа jjson
|
├── SimpleNamespace? --> B: Преобразование в словарь (vars(jjson))
|
├── Path? --> C: Обработка Path
|   |
|   ├── Директория? --> D: Рекурсивный вызов j_loads для каждого файла .json
|   |
|   └── Файл? --> E: Чтение и парсинг JSON из файла
|
├── Строка? --> F: Преобразование строки в словарь (_string_to_dict)
|
├── Список? --> G: Декодирование строк в списке (_decode_strings)
|
├── Словарь? --> H: Декодирование строк в словаре (_decode_strings)
|
└── Обработка ошибок и возврат {}
```

**Примеры**:

```python
from pathlib import Path
from types import SimpleNamespace

# Пример 1: Загрузка JSON из строки
json_string = '{"name": "John", "age": 30}'
data = j_loads(json_string)
print(data)  # Вывод: {'name': 'John', 'age': 30}

# Пример 2: Загрузка JSON из файла
file_path = Path('config.json')
file_path.write_text('{"name": "John", "age": 30}', encoding='utf-8')
data = j_loads(file_path)
print(data)  # Вывод: {'name': 'John', 'age': 30}

# Пример 3: Загрузка JSON из SimpleNamespace
ns = SimpleNamespace(name='John', age=30)
data = j_loads(ns)
print(data)  # Вывод: {'name': 'John', 'age': 30}

# Пример 4: Загрузка JSON из списка
json_list = ['{"name": "John", "age": 30}', '{"name": "Jane", "age": 25}']
data = j_loads(json_list)
print(data)
```

### `j_loads_ns`

```python
def j_loads_ns(
    jjson: Union[Path, SimpleNamespace, Dict, str], ordered: bool = True
) -> Union[SimpleNamespace, List[SimpleNamespace], Dict]:
    """Загружает JSON/CSV данные и преобразует в SimpleNamespace."""
```

**Назначение**: Загружает JSON данные из различных источников (файла, объекта `SimpleNamespace`, словаря или строки) и преобразует их в объект `SimpleNamespace` или список объектов `SimpleNamespace`.

**Параметры**:
- `jjson` (Union[Path, SimpleNamespace, Dict, str]): Источник JSON данных. Может быть:
  - `Path`: Путь к файлу с JSON данными.
  - `SimpleNamespace`: Объект `SimpleNamespace` с данными.
  - `Dict`: Словарь с данными.
  - `str`: Строка, содержащая JSON данные.
- `ordered` (bool, optional): Определяет, нужно ли использовать `OrderedDict` для сохранения порядка элементов в словаре. По умолчанию `True`.

**Возвращает**:
- `Union[SimpleNamespace, List[SimpleNamespace], Dict]`: Обработанные данные в виде объекта `SimpleNamespace`, списка объектов `SimpleNamespace` или словаря. Если происходит ошибка или данные отсутствуют, функция возвращает пустой словарь `{}`.

**Как работает функция**:

1. **Загрузка данных**: Функция вызывает функцию `j_loads` для загрузки JSON данных из указанного источника.
2. **Преобразование в SimpleNamespace**:
   - Если загруженные данные являются списком, функция преобразует каждый элемент списка в объект `SimpleNamespace` с помощью функции `dict2ns`.
   - Если загруженные данные являются словарем, функция преобразует их в объект `SimpleNamespace` с помощью функции `dict2ns`.
3. **Возврат данных**: Функция возвращает преобразованные данные в виде объекта `SimpleNamespace`, списка объектов `SimpleNamespace` или пустой словарь, если произошла ошибка или данные отсутствуют.

```
A: Загрузка данных с помощью j_loads
|
├── Данные загружены? --> B: Проверка типа данных
|   |
|   ├── Список? --> C: Преобразование каждого элемента списка в SimpleNamespace (dict2ns)
|   |
|   └── Словарь? --> D: Преобразование словаря в SimpleNamespace (dict2ns)
|
└── Возврат {} (в случае ошибки или отсутствия данных)
```

**Примеры**:

```python
from pathlib import Path
from types import SimpleNamespace

# Пример 1: Загрузка и преобразование JSON из строки
json_string = '{"name": "John", "age": 30}'
data = j_loads_ns(json_string)
print(data)  # Вывод: namespace(name='John', age=30)
print(data.name)  # Вывод: John

# Пример 2: Загрузка и преобразование JSON из файла
file_path = Path('config.json')
file_path.write_text('{"name": "John", "age": 30}', encoding='utf-8')
data = j_loads_ns(file_path)
print(data)  # Вывод: namespace(name='John', age=30)

# Пример 3: Загрузка и преобразование JSON из словаря
json_dict = {"name": "John", "age": 30}
data = j_loads_ns(json_dict)
print(data)  # Вывод: namespace(name='John', age=30)

# Пример 4: Загрузка и преобразование JSON из списка
json_list = [{"name": "John", "age": 30}, {"name": "Jane", "age": 2