# Модуль `jjson`

## Обзор

Модуль `jjson` предназначен для обработки JSON и CSV файлов, включая загрузку, выгрузку и слияние данных.

Этот модуль предоставляет функции для:
- **Выгрузки JSON данных**: Преобразует JSON или объекты `SimpleNamespace` в JSON-формат и записывает в файл, или возвращает JSON данные в виде словаря.
- **Загрузки JSON и CSV данных**: Читает JSON или CSV данные из файла, директории или строки и преобразует их в словари или списки словарей.
- **Конвертации в SimpleNamespace**: Преобразует загруженные JSON данные в объекты `SimpleNamespace` для упрощения работы с ними.
- **Слияния JSON файлов**: Объединяет несколько JSON файлов из директории в один JSON файл.
- **Парсинга Markdown**: Преобразует строки Markdown в формат JSON для структурированного представления данных.

Функции в этом модуле обрабатывают различные аспекты работы с JSON и CSV данными, обеспечивая эффективную и надежную загрузку, сохранение и слияние данных.

## Оглавление

1. [Функции](#Функции)
   - [`j_dumps`](#j_dumps)
   - [`j_loads`](#j_loads)
   - [`j_loads_ns`](#j_loads_ns)

## Функции

### `j_dumps`

**Описание**: Выгрузка JSON данных в файл или возврат JSON данных в виде словаря.

**Параметры**:
- `data` (Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]): JSON-совместимые данные или объекты `SimpleNamespace` для выгрузки.
- `file_path` (Optional[Path], optional): Путь к выходному файлу. Если `None`, возвращает JSON в виде словаря. По умолчанию `None`.
- `ensure_ascii` (bool, optional): Если `True`, экранирует не-ASCII символы в выводе. По умолчанию `True`.
- `mode` (str, optional): Режим открытия файла (`'w'`, `'a+'`, `'+a'`). По умолчанию `'w'`.
- `exc_info` (bool, optional): Если `True`, логирует исключения с трассировкой. По умолчанию `True`.

**Возвращает**:
- `Optional[Dict]`: JSON данные в виде словаря в случае успеха или ничего в случае ошибки.

**Вызывает исключения**:
- `ValueError`: Если режим открытия файла не поддерживается.

### `j_loads`

**Описание**: Загрузка JSON или CSV данных из файла, директории, строки, объекта JSON или `SimpleNamespace`. Перекодирует строки ключей и значений в Unicode.

**Параметры**:
- `jjson` (dict | SimpleNamespace | str | Path | list): Путь к файлу, директории, строка JSON данных, объект JSON или `SimpleNamespace`.
- `ordered` (bool, optional): Возвращает `OrderedDict` для сохранения порядка элементов. По умолчанию `True`.

**Возвращает**:
- `dict | list`: Обработанные данные (словарь или список словарей).

**Вызывает исключения**:
- `FileNotFoundError`: Если указанный файл не найден.
- `json.JSONDecodeError`: Если данные JSON не удалось разобрать.

### `j_loads_ns`

**Описание**: Загрузка JSON или CSV данных из файла, директории или строки и преобразование в `SimpleNamespace`.

**Параметры**:
- `jjson` (Path | SimpleNamespace | Dict | str): Путь к файлу, директории, строка JSON данных или объект JSON.
- `ordered` (bool, optional): Если `True`, возвращает `OrderedDict` вместо обычного словаря для сохранения порядка элементов. По умолчанию `True`.

**Возвращает**:
- `Optional[SimpleNamespace | List[SimpleNamespace]]`: Возвращает `SimpleNamespace` или список объектов `SimpleNamespace` в случае успеха. Возвращает `None`, если `jjson` не найден или не может быть прочитан.

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