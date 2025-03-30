# Модуль `extraction.py`

## Обзор

Модуль `extraction.py` предоставляет утилиты для извлечения данных из элементов TinyTroupe, таких как агенты и миры. Он также предоставляет механизм для сокращения извлеченных данных до более краткой формы и экспорта артефактов из элементов TinyTroupe.

## Содержание

- [Классы](#Классы)
  - [`ResultsExtractor`](#ResultsExtractor)
    - [`__init__`](#__init__)
    - [`extract_results_from_agent`](#extract_results_from_agent)
    - [`extract_results_from_world`](#extract_results_from_world)
    - [`save_as_json`](#save_as_json)
  - [`ResultsReducer`](#ResultsReducer)
    - [`__init__`](#__init__-1)
    - [`add_reduction_rule`](#add_reduction_rule)
    - [`reduce_agent`](#reduce_agent)
    - [`reduce_agent_to_dataframe`](#reduce_agent_to_dataframe)
  - [`ArtifactExporter`](#ArtifactExporter)
    - [`__init__`](#__init__-2)
    - [`export`](#export)
    - [`_export_as_txt`](#_export_as_txt)
    - [`_export_as_json`](#_export_as_json)
    - [`_export_as_docx`](#_export_as_docx)
    - [`_compose_filepath`](#_compose_filepath)
  - [`Normalizer`](#Normalizer)
    - [`__init__`](#__init__-3)
    - [`normalize`](#normalize)
- [Переменные](#Переменные)
  - [`default_extractor`](#default_extractor)

## Классы

### `ResultsExtractor`

**Описание**:
Класс для извлечения результатов из агентов и миров TinyTroupe.

#### `__init__`

**Описание**:
Инициализирует экземпляр класса `ResultsExtractor`.

**Параметры**:
- Нет

**Возвращает**:
- Нет

#### `extract_results_from_agent`

**Описание**:
Извлекает результаты из экземпляра `TinyPerson`.

**Параметры**:
- `tinyperson` (`TinyPerson`): Экземпляр `TinyPerson`, из которого нужно извлечь результаты.
- `extraction_objective` (`str`): Цель извлечения.
- `situation` (`str`): Ситуация, которую нужно учитывать.
- `fields` (`list`, optional): Поля для извлечения. Если `None`, извлекатель сам определит, какие имена использовать. По умолчанию `None`.
- `fields_hints` (`dict`, optional): Подсказки для извлекаемых полей. По умолчанию `None`.
- `verbose` (`bool`, optional): Выводить ли отладочные сообщения. По умолчанию `False`.

**Возвращает**:
- `dict | None`: Извлеченные результаты в виде словаря или `None`, если извлечение не удалось.

#### `extract_results_from_world`

**Описание**:
Извлекает результаты из экземпляра `TinyWorld`.

**Параметры**:
- `tinyworld` (`TinyWorld`): Экземпляр `TinyWorld`, из которого нужно извлечь результаты.
- `extraction_objective` (`str`): Цель извлечения.
- `situation` (`str`): Ситуация, которую нужно учитывать.
- `fields` (`list`, optional): Поля для извлечения. Если `None`, извлекатель сам определит, какие имена использовать. По умолчанию `None`.
- `fields_hints` (`dict`, optional): Подсказки для извлекаемых полей. По умолчанию `None`.
- `verbose` (`bool`, optional): Выводить ли отладочные сообщения. По умолчанию `False`.

**Возвращает**:
- `dict | None`: Извлеченные результаты в виде словаря или `None`, если извлечение не удалось.

#### `save_as_json`

**Описание**:
Сохраняет последние результаты извлечения в формате JSON.

**Параметры**:
- `filename` (`str`): Имя файла для сохранения JSON.
- `verbose` (`bool`, optional): Выводить ли отладочные сообщения. По умолчанию `False`.

**Возвращает**:
- Нет

### `ResultsReducer`

**Описание**:
Класс для сокращения извлеченных результатов.

#### `__init__`

**Описание**:
Инициализирует экземпляр класса `ResultsReducer`.

**Параметры**:
- Нет

**Возвращает**:
- Нет

#### `add_reduction_rule`

**Описание**:
Добавляет правило сокращения.

**Параметры**:
- `trigger` (`str`): Триггер для правила сокращения.
- `func` (`callable`): Функция для сокращения.

**Возвращает**:
- Нет

**Вызывает исключения**:
- `Exception`: Если правило для данного триггера уже существует.

#### `reduce_agent`

**Описание**:
Сокращает данные агента на основе заданных правил.

**Параметры**:
- `agent` (`TinyPerson`): Агент, данные которого нужно сократить.

**Возвращает**:
- `list`: Список сокращенных данных.

#### `reduce_agent_to_dataframe`

**Описание**:
Сокращает данные агента и возвращает их в виде DataFrame.

**Параметры**:
- `agent` (`TinyPerson`): Агент, данные которого нужно сократить.
- `column_names` (`list`, optional): Список имен столбцов для DataFrame. По умолчанию `None`.

**Возвращает**:
- `pd.DataFrame`: DataFrame с сокращенными данными.

### `ArtifactExporter`

**Описание**:
Класс для экспорта артефактов из элементов TinyTroupe.

#### `__init__`

**Описание**:
Инициализирует экземпляр класса `ArtifactExporter`.

**Параметры**:
- `base_output_folder` (`str`): Базовая папка для сохранения экспортированных артефактов.

**Возвращает**:
- Нет

#### `export`

**Описание**:
Экспортирует артефакт в файл.

**Параметры**:
- `artifact_name` (`str`): Имя артефакта.
- `artifact_data` (`Union[dict, str]`): Данные для экспорта. Если словарь, будет сохранен как JSON, если строка - как текст.
- `content_type` (`str`): Тип контента в артефакте.
- `content_format` (`str`, optional): Формат контента в артефакте (например, md, csv и т.д.). По умолчанию `None`.
- `target_format` (`str`, optional): Формат для экспорта артефакта (например, json, txt, docx и т.д.). По умолчанию `txt`.
- `verbose` (`bool`, optional): Выводить ли отладочные сообщения. По умолчанию `False`.

**Возвращает**:
- Нет

**Вызывает исключения**:
- `ValueError`: Если `artifact_data` не является строкой или словарем, или если `target_format` не поддерживается.

#### `_export_as_txt`

**Описание**:
Экспортирует данные артефакта в текстовый файл.

**Параметры**:
- `artifact_file_path` (`str`): Путь к файлу для экспорта.
- `artifact_data` (`Union[dict, str]`): Данные для экспорта.
- `content_type` (`str`): Тип контента в артефакте.
- `verbose` (`bool`, optional): Выводить ли отладочные сообщения. По умолчанию `False`.

**Возвращает**:
- Нет

#### `_export_as_json`

**Описание**:
Экспортирует данные артефакта в JSON-файл.

**Параметры**:
- `artifact_file_path` (`str`): Путь к файлу для экспорта.
- `artifact_data` (`Union[dict, str]`): Данные для экспорта.
- `content_type` (`str`): Тип контента в артефакте.
- `verbose` (`bool`, optional): Выводить ли отладочные сообщения. По умолчанию `False`.

**Возвращает**:
- Нет

**Вызывает исключения**:
- `ValueError`: Если `artifact_data` не является словарем.

#### `_export_as_docx`

**Описание**:
Экспортирует данные артефакта в DOCX-файл.

**Параметры**:
- `artifact_file_path` (`str`): Путь к файлу для экспорта.
- `artifact_data` (`Union[dict, str]`): Данные для экспорта.
- `content_original_format` (`str`): Исходный формат контента (например, 'text', 'markdown').
- `verbose` (`bool`, optional): Выводить ли отладочные сообщения. По умолчанию `False`.

**Возвращает**:
- Нет

**Вызывает исключения**:
- `ValueError`: Если `content_original_format` не поддерживается.

#### `_compose_filepath`

**Описание**:
Составляет путь к файлу для экспорта артефакта.

**Параметры**:
- `artifact_data` (`Union[dict, str]`): Данные для экспорта.
- `artifact_name` (`str`): Имя артефакта.
- `content_type` (`str`): Тип контента в артефакте.
- `target_format` (`str`, optional): Формат для экспорта артефакта. По умолчанию `None`.
- `verbose` (`bool`, optional): Выводить ли отладочные сообщения. По умолчанию `False`.

**Возвращает**:
- `str`: Сформированный путь к файлу.

### `Normalizer`

**Описание**:
Класс для нормализации текстовых элементов.

#### `__init__`

**Описание**:
Инициализирует экземпляр класса `Normalizer`.

**Параметры**:
- `elements` (`list`): Список элементов для нормализации.
- `n` (`int`): Количество нормализованных элементов для вывода.
- `verbose` (`bool`, optional): Выводить ли отладочные сообщения. По умолчанию `False`.

**Возвращает**:
- Нет

#### `normalize`

**Описание**:
Нормализует указанный элемент или список элементов.

**Параметры**:
- `element_or_elements` (`Union[str, List[str]]`): Элемент или список элементов для нормализации.

**Возвращает**:
- `str` | `List[str]`: Нормализованный элемент или список нормализованных элементов в зависимости от типа входных данных.

**Вызывает исключения**:
- `ValueError`: Если `element_or_elements` не является строкой или списком.

## Переменные

### `default_extractor`

**Описание**:
Экземпляр `ResultsExtractor` по умолчанию.

**Тип**:
- `ResultsExtractor`