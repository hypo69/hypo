# Модуль `hypotez/src/utils/jjson.py`

## Обзор

Модуль `jjson` предназначен для работы с JSON и CSV файлами. Он предоставляет функции для загрузки, выгрузки, объединения данных в JSON формате, а также конвертации данных в `SimpleNamespace` для удобной работы.  Модуль также включает обработку Markdown строк в JSON и поддержку различных режимов работы с файлами.


## Функции

### `j_dumps`

**Описание**: Функция `j_dumps` выгружает данные в JSON-формат в файл или возвращает данные в виде словаря. Поддерживает различные типы данных: словари, `SimpleNamespace`, списки словарей и списки `SimpleNamespace`.

**Параметры**:

- `data` (Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]): Данные для выгрузки в JSON-формат.
- `file_path` (Optional[Path], optional): Путь к файлу для выгрузки. Если `None`, возвращает JSON данные в виде словаря. По умолчанию `None`.
- `ensure_ascii` (bool, optional): Если `True`, эскейпит не-ASCII символы в выводе. По умолчанию `True`.
- `mode` (str, optional): Режим открытия файла (`'w'`, `'a+'`, `'+a'`). По умолчанию `'w'`.
- `exc_info` (bool, optional): Если `True`, логгирует исключения с отслеживанием стека. По умолчанию `True`.

**Возвращает**:

- `Optional[Dict]`:  JSON данные в виде словаря, если успешно, или `None` в случае ошибки.

**Возможные исключения**:

- `ValueError`: Если режим файла не поддерживается.


### `j_loads`

**Описание**: Функция `j_loads` загружает данные из JSON или CSV файла, директории, строки, объекта `dict` или `SimpleNamespace`.  Перекодирует строки ключей и значений в Unicode для правильной обработки.

**Параметры**:

- `jjson` (dict | SimpleNamespace | str | Path | list): Путь к файлу, директории, строка JSON данных, объект JSON или `SimpleNamespace`.
- `ordered` (bool, optional): Возвращает `OrderedDict` для сохранения порядка элементов. По умолчанию `True`.


**Возвращает**:

- `dict | list`: Обработанные данные (словарь или список словарей).

**Возможные исключения**:

- `FileNotFoundError`: Если указанный файл не найден.
- `json.JSONDecodeError`: Если данные JSON не удалось разобрать.
- Другие исключения: В случае ошибок при чтении или обработке данных.


### `j_loads_ns`

**Описание**: Функция `j_loads_ns` загружает JSON или CSV данные из файла, директории, или строки и конвертирует их в объекты `SimpleNamespace`.

**Параметры**:

- `jjson` (Path | SimpleNamespace | Dict | str): Путь к файлу, директории, или JSON данные в виде строки, или объект JSON.
- `ordered` (bool, optional):  Возвращает `OrderedDict` для сохранения порядка элементов. По умолчанию `False`.

**Возвращает**:

- `Optional[SimpleNamespace | List[SimpleNamespace]]`: Возвращает `SimpleNamespace` или список `SimpleNamespace` объектов, если успешно. Возвращает `None` в случае, если `jjson` не найден или не может быть прочитан.

**Примеры**:

```
>>> j_loads_ns('data.json')
SimpleNamespace(key='value')

>>> j_loads_ns(Path('/path/to/directory'))
[SimpleNamespace(key1='value1'), SimpleNamespace(key2='value2')]

>>> j_loads_ns('{"key": "value"}')
SimpleNamespace(key='value')

>>> j_loads_ns(Path('/path/to/file.csv'))
[SimpleNamespace(column1='value1', column2='value2')]
```

**Примечание**: Функция `j_loads_ns` использует `j_loads` для загрузки данных, а затем конвертирует их в `SimpleNamespace`.


## Поддержка

Данный модуль обеспечивает  функциональность для работы с JSON/CSV данными, обработкой ошибок и поддержкой различных режимов работы с файлами.