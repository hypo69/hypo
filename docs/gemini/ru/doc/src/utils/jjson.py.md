# Модуль `jjson`

## Обзор

Модуль `jjson` предназначен для работы с файлами JSON и CSV, включая загрузку, выгрузку и слияние данных. Он предоставляет функции для:

- **Выгрузки JSON данных**: Преобразование объектов JSON или SimpleNamespace в формат JSON и запись в файл или возврат данных JSON в виде словаря.
- **Загрузки JSON и CSV данных**: Чтение данных JSON или CSV из файла, каталога или строки и преобразование их в словари или списки словарей.
- **Преобразования в SimpleNamespace**: Преобразование загруженных данных JSON в объекты SimpleNamespace для более удобного манипулирования.
- **Слияния JSON файлов**: Объединение нескольких JSON файлов из каталога в один файл JSON.
- **Парсинга Markdown**: Преобразование строк Markdown в формат JSON для представления структурированных данных.

Функции в этом модуле обрабатывают различные аспекты работы с данными JSON и CSV, обеспечивая эффективную загрузку, сохранение и слияние данных.

## Оглавление

- [Функции](#Функции)
  - [`j_dumps`](#j_dumps)
  - [`j_loads`](#j_loads)
  - [`j_loads_ns`](#j_loads_ns)

## Функции

### `j_dumps`

**Описание**: Выгружает JSON данные в файл или возвращает JSON данные в виде словаря.

**Параметры**:

- `data` (Any): JSON-совместимые данные или объекты SimpleNamespace для выгрузки.
- `file_path` (Optional[Path], optional): Путь к выходному файлу. Если None, возвращает JSON как словарь. По умолчанию `None`.
- `ensure_ascii` (bool, optional): Если True, экранирует не-ASCII символы в выводе. По умолчанию `True`.
- `mode` (str, optional): Режим открытия файла ('w', 'a+', '+a'). По умолчанию 'w'.
- `exc_info` (bool, optional): Если True, записывает исключения с трассировкой. По умолчанию `True`.

**Возвращает**:

- `Optional[Dict]`: JSON данные в виде словаря в случае успеха или ничего, если произошла ошибка.

**Вызывает исключения**:

- `ValueError`: Если режим файла не поддерживается.

### `j_loads`

**Описание**: Загружает данные JSON или CSV из файла, каталога, строки, объекта JSON или SimpleNamespace. Перекодирует строки ключей и значений в Unicode.

**Параметры**:

- `jjson` (dict | SimpleNamespace | str | Path | list): Путь к файлу, каталогу, строка JSON данных, объект JSON или SimpleNamespace.
- `ordered` (bool, optional): Возвращает OrderedDict для сохранения порядка элементов. По умолчанию `True`.

**Возвращает**:

- `dict | list`: Обработанные данные (словарь или список словарей).

**Вызывает исключения**:

- `FileNotFoundError`: Если указанный файл не найден.
- `json.JSONDecodeError`: Если данные JSON не удалось разобрать.

### `j_loads_ns`

**Описание**: Загружает данные JSON или CSV из файла, каталога или строки и преобразует их в SimpleNamespace.

**Параметры**:

- `jjson` (Path | SimpleNamespace | Dict | str): Путь к файлу, каталогу или JSON данные в виде строки или объекта JSON.
- `ordered` (bool, optional): Если True возвращает OrderedDict вместо обычного dict для сохранения порядка элементов. По умолчанию `True`.
- `exc_info` (bool, optional): Если True, то логирует исключения с трассировкой. По умолчанию `True`.

**Возвращает**:

- `SimpleNamespace | List[SimpleNamespace]`: Возвращает SimpleNamespace или список объектов SimpleNamespace в случае успеха. Возвращает None, если `jjson` не найден или не может быть прочитан.

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