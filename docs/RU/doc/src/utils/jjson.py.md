# Модуль `jjson`

## Обзор

Модуль `jjson` предназначен для обработки файлов JSON и CSV, включая загрузку, выгрузку и объединение данных. Он предоставляет функции для:

- **Выгрузки данных JSON**: преобразование объектов JSON или `SimpleNamespace` в формат JSON и запись в файл, или возврат данных JSON в виде словаря.
- **Загрузки данных JSON и CSV**: чтение данных JSON или CSV из файла, директории или строки и преобразование их в словари или списки словарей.
- **Преобразования в `SimpleNamespace`**: преобразование загруженных данных JSON в объекты `SimpleNamespace` для упрощения работы с ними.
- **Объединения файлов JSON**: объединение нескольких файлов JSON из директории в один файл JSON.
- **Разбора Markdown**: преобразование строк Markdown в формат JSON для структурированного представления данных.

Функции в этом модуле обрабатывают различные аспекты работы с данными JSON и CSV, обеспечивая эффективную и надежную загрузку, сохранение и объединение данных.

## Содержание

1.  [Функции](#Функции)
    *   [`j_dumps`](#j_dumps)
    *   [`j_loads`](#j_loads)
    *   [`j_loads_ns`](#j_loads_ns)

## Функции

### `j_dumps`

**Описание**: Выгружает JSON данные в файл или возвращает JSON данные в виде словаря.

**Параметры**:

*   `data` (Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]): JSON-совместимые данные или объекты `SimpleNamespace` для выгрузки.
*   `file_path` (Optional[Path], optional): Путь к выходному файлу. Если `None`, возвращает JSON как словарь. По умолчанию `None`.
*   `ensure_ascii` (bool, optional): Если `True`, экранирует символы не ASCII в выводе. По умолчанию `True`.
*   `mode` (str, optional): Режим открытия файла (`'w'`, `'a+'`, `'+a'`). По умолчанию `'w'`.
*   `exc_info` (bool, optional): Если `True`, логирует исключения с трассировкой. По умолчанию `True`.

**Возвращает**:

*   `Optional[Dict]`: Данные JSON в виде словаря в случае успеха, или ничего в случае ошибки.

**Вызывает исключения**:

*   `ValueError`: Если режим файла не поддерживается.

### `j_loads`

**Описание**: Загружает JSON или CSV данные из файла, директории, строки, объекта JSON или `SimpleNamespace`. Перекодирует строки ключей и значений в Unicode.

**Параметры**:

*   `jjson` (dict | SimpleNamespace | str | Path | list): Путь к файлу, директории, строка JSON данных, объект JSON или `SimpleNamespace`.
*   `ordered` (bool, optional): Возвращает `OrderedDict` для сохранения порядка элементов. По умолчанию `True`.

**Возвращает**:

*   `dict | list`: Обработанные данные (словарь или список словарей).

**Вызывает исключения**:

*   `FileNotFoundError`: Если указанный файл не найден.
*   `json.JSONDecodeError`: Если данные JSON не удалось разобрать.

### `j_loads_ns`

**Описание**: Загружает данные JSON или CSV из файла, директории или строки и преобразует в `SimpleNamespace`.

**Параметры**:

*   `jjson` (Path | SimpleNamespace | Dict | str): Путь к файлу, директории или JSON данные в виде строки или объекта JSON.
*   `ordered` (bool, optional): Если `True` возвращает `OrderedDict` вместо обычного словаря для сохранения порядка элементов. По умолчанию `False`.

**Возвращает**:

*   `Optional[SimpleNamespace | List[SimpleNamespace]]`: Возвращает `SimpleNamespace` или список объектов `SimpleNamespace` в случае успеха. Возвращает `None`, если `jjson` не найден или не может быть прочитан.

**Примеры**:
```python
>>> j_loads_ns('data.json')
SimpleNamespace(key='value')

>>> j_loads_ns(Path('/path/to/directory'))
[SimpleNamespace(key1='value1'), SimpleNamespace(key2='value2')]

>>> j_loads_ns('{"key": "value"}')
SimpleNamespace(key='value')

>>> j_loads_ns(Path('/path/to/file.csv'))
[SimpleNamespace(column1='value1', column2='value2')]
```