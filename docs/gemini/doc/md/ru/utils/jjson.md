```markdown
# Модуль jjson

## Обзор

Модуль `jjson` предоставляет функции для работы с JSON и CSV файлами, включая загрузку, выгрузку и слияние данных. Он поддерживает работу с различными типами данных, включая словари, списки словарей, `SimpleNamespace` объекты и строки, а также позволяет сохранять данные в файлы JSON и CSV, обрабатывать исключения и сохранять структуру данных.


## Функции

### `j_dumps`

**Описание**: Функция для выгрузки JSON данных в файл или возврата данных в виде словаря. Поддерживает разные режимы записи (запись поверх, добавление в конец).

**Параметры**:
- `data` (Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]): Данные для выгрузки. Должны быть JSON-совместимые или `SimpleNamespace` объекты.
- `file_path` (Optional[Path], необязательно): Путь к выходному файлу. Если `None`, функция возвращает данные в виде словаря.
- `ensure_ascii` (bool, необязательно): Если `True`, не-ASCII символы в выводе экранируются. По умолчанию `True`.
- `mode` (str, необязательно): Режим открытия файла ('w', 'a+', '+a'). По умолчанию 'w'.
- `exc_info` (bool, необязательно): Если `True`, исключения логируются с отслеживанием стека. По умолчанию `True`.

**Возвращает**:
- `Optional[Dict]`: JSON данные в виде словаря, если успешно, или `None` в случае ошибки.

**Вызывает исключения**:
- `ValueError`: Если режим файла не поддерживается.


### `j_loads`

**Описание**: Функция для загрузки JSON или CSV данных из файла, директории или строки. Поддерживает слияние данных из файлов в директории.

**Параметры**:
- `jjson` (Path | dict | str): Путь к файлу, директории, JSON данные в виде строки или JSON объект.
- `ordered` (bool, необязательно): Если `True`, возвращает `OrderedDict`, сохраняя порядок элементов. По умолчанию `False`.
- `exc_info` (bool, необязательно): Если `True`, исключения логируются с отслеживанием стека. По умолчанию `True`.


**Возвращает**:
- `Any`: Словарь или список словарей, если успешно, или `None` в случае ошибки.

**Вызывает исключения**:
- `FileNotFoundError`: Если указанный файл не найден.
- `json.JSONDecodeError`: Если JSON данные не могут быть обработаны.


### `j_loads_ns`

**Описание**: Функция для загрузки JSON или CSV данных и преобразования их в `SimpleNamespace` объекты.

**Параметры**:
- `jjson` (Path | SimpleNamespace | Dict | str): Путь к файлу, директории, JSON данные в виде строки или JSON объект.
- `ordered` (bool, необязательно): Если `True`, возвращает `OrderedDict` вместо обычного словаря, сохраняя порядок элементов. По умолчанию `False`.
- `exc_info` (bool, необязательно): Если `True`, исключения логируются с отслеживанием стека. По умолчанию `True`.

**Возвращает**:
- `Optional[SimpleNamespace | List[SimpleNamespace]]`: Возвращает `SimpleNamespace` или список `SimpleNamespace` объектов, если успешно. Возвращает `None` если `jjson` не найден или не может быть прочитан.


### `replace_key_in_json`

**Описание**: Функция для рекурсивной замены ключа в словаре или списке. Поддерживает вложенные структуры.

**Параметры**:
- `data` (dict | list): Словарь или список, в котором происходит замена ключа.
- `old_key` (str): Ключ, который нужно заменить.
- `new_key` (str): Новый ключ.

**Возвращает**:
- dict: Обновленный словарь с заменёнными ключами.

### `process_json_file`

**Описание**: Обрабатывает JSON файл, заменяя ключ `name` на `category_name`.

**Параметр**:
- `json_file` (Path): Путь к JSON файлу.

### `recursive_process_json_files`

**Описание**: Рекурсивно обходит папки и обрабатывает JSON файлы.

**Параметр**:
- `directory` (Path): Путь к директории, которую нужно обработать.


### `extract_json_from_string`

**Описание**: Извлекает JSON контент из строки Markdown между маркерами ```json и ```.

**Параметр**:
- `md_string` (str): Строка Markdown, содержащая JSON.

**Возвращает**:
- str: Извлеченная JSON строка или пустая строка, если не найдено.



```