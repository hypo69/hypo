# Модуль `extraction.py`

## Обзор

Модуль `extraction.py` предоставляет инструменты для извлечения структурированных данных из элементов TinyTroupe, таких как агенты и миры. Он включает в себя механизмы для сокращения извлеченных данных, экспорта артефактов и нормализации текстовых элементов.

## Содержание

1.  [Классы](#классы)
    *   [`ResultsExtractor`](#class-resultsextractor)
    *   [`ResultsReducer`](#class-resultsreducer)
    *   [`ArtifactExporter`](#class-artifactexporter)
    *   [`Normalizer`](#class-normalizer)
2.  [Функции](#функции)
    *   [`default_extractor`](#function-default_extractor)

## Классы

### `ResultsExtractor`

**Описание**: Класс `ResultsExtractor` предназначен для извлечения результатов из экземпляров `TinyPerson` и `TinyWorld`.

**Методы**:

*   `__init__`:
    **Описание**: Инициализирует экземпляр класса `ResultsExtractor`.
*    `extract_results_from_agent`:
    
    **Описание**: Извлекает результаты из экземпляра `TinyPerson`.

    **Параметры**:
    - `tinyperson` (`TinyPerson`): Экземпляр `TinyPerson`, из которого извлекаются результаты.
    - `extraction_objective` (`str`, optional): Цель извлечения. По умолчанию "The main points present in the agent's interactions history.".
    - `situation` (`str`, optional): Ситуация, которую необходимо учитывать. По умолчанию "".
    - `fields` (`list`, optional): Поля для извлечения. Если `None`, извлекатель определит имена полей самостоятельно. По умолчанию `None`.
    - `fields_hints` (`dict`, optional): Подсказки для полей. По умолчанию `None`.
    - `verbose` (`bool`, optional): Флаг для вывода отладочных сообщений. По умолчанию `False`.

    **Возвращает**:
    - `dict | None`: Извлеченные результаты в виде словаря или `None`, если результаты не были получены.

*   `extract_results_from_world`:
    
    **Описание**: Извлекает результаты из экземпляра `TinyWorld`.

    **Параметры**:
    - `tinyworld` (`TinyWorld`): Экземпляр `TinyWorld`, из которого извлекаются результаты.
    - `extraction_objective` (`str`, optional): Цель извлечения. По умолчанию "The main points that can be derived from the agents conversations and actions.".
    - `situation` (`str`, optional): Ситуация, которую необходимо учитывать. По умолчанию "".
    - `fields` (`list`, optional): Поля для извлечения. Если `None`, извлекатель определит имена полей самостоятельно. По умолчанию `None`.
    - `fields_hints` (`dict`, optional): Подсказки для полей. По умолчанию `None`.
    - `verbose` (`bool`, optional): Флаг для вывода отладочных сообщений. По умолчанию `False`.

    **Возвращает**:
    - `dict | None`: Извлеченные результаты в виде словаря или `None`, если результаты не были получены.
*   `save_as_json`:
    
    **Описание**: Сохраняет последние извлеченные результаты в формате JSON.

    **Параметры**:
    - `filename` (`str`): Имя файла для сохранения JSON.
    - `verbose` (`bool`, optional): Флаг для вывода отладочных сообщений. По умолчанию `False`.

### `ResultsReducer`

**Описание**: Класс `ResultsReducer` предназначен для сокращения результатов извлечения на основе заданных правил.

**Методы**:

*   `__init__`:
    **Описание**: Инициализирует экземпляр класса `ResultsReducer`.
*   `add_reduction_rule`:
    
    **Описание**: Добавляет правило сокращения для определенного триггера.

    **Параметры**:
    - `trigger` (`str`): Триггер, для которого добавляется правило.
    - `func` (`callable`): Функция, выполняющая сокращение.
    
    **Вызывает исключения**:
    - `Exception`: Если правило для данного триггера уже существует.
*   `reduce_agent`:
    
    **Описание**: Сокращает данные агента на основе заданных правил.

    **Параметры**:
    - `agent` (`TinyPerson`): Экземпляр `TinyPerson`, данные которого нужно сократить.

    **Возвращает**:
    - `list`: Список сокращенных данных.
*   `reduce_agent_to_dataframe`:
    
    **Описание**: Сокращает данные агента и преобразует их в `pandas.DataFrame`.

    **Параметры**:
    - `agent` (`TinyPerson`): Экземпляр `TinyPerson`, данные которого нужно сократить.
    - `column_names` (`list`, optional): Список имен столбцов для `DataFrame`. По умолчанию `None`.

    **Возвращает**:
    - `pd.DataFrame`: `DataFrame` с сокращенными данными.

### `ArtifactExporter`

**Описание**: Класс `ArtifactExporter` предназначен для экспорта артефактов из элементов TinyTroupe.

**Методы**:

*   `__init__`:
    
    **Описание**: Инициализирует экземпляр класса `ArtifactExporter`.

    **Параметры**:
    - `base_output_folder` (`str`): Базовая папка для вывода.
*   `export`:
    
    **Описание**: Экспортирует артефакт в файл.

    **Параметры**:
    - `artifact_name` (`str`): Имя артефакта.
    - `artifact_data` (`Union[dict, str]`): Данные для экспорта. Если это словарь, он будет сохранен в JSON. Если строка - сохраняется как есть.
    - `content_type` (`str`): Тип содержимого артефакта.
    - `content_format` (`str`, optional): Формат содержимого артефакта (например, 'md', 'csv'). По умолчанию `None`.
    - `target_format` (`str`, optional): Целевой формат экспорта (например, 'json', 'txt', 'docx'). По умолчанию "txt".
    - `verbose` (`bool`, optional): Флаг для вывода отладочных сообщений. По умолчанию `False`.
    
    **Вызывает исключения**:
    - `ValueError`: Если `artifact_data` не является строкой или словарем, или если `target_format` не поддерживается.
*    `_export_as_txt`:
    
    **Описание**: Экспортирует артефакт в текстовый файл.

    **Параметры**:
    - `artifact_file_path` (`str`): Путь к файлу для экспорта.
    - `artifact_data` (`Union[dict, str]`): Данные для экспорта.
    - `content_type` (`str`): Тип содержимого артефакта.
    - `verbose` (`bool`, optional): Флаг для вывода отладочных сообщений. По умолчанию `False`.
*    `_export_as_json`:
    
    **Описание**: Экспортирует артефакт в JSON-файл.

    **Параметры**:
    - `artifact_file_path` (`str`): Путь к файлу для экспорта.
    - `artifact_data` (`Union[dict, str]`): Данные для экспорта.
    - `content_type` (`str`): Тип содержимого артефакта.
    - `verbose` (`bool`, optional): Флаг для вывода отладочных сообщений. По умолчанию `False`.
        
    **Вызывает исключения**:
    - `ValueError`: Если `artifact_data` не является словарем.
*    `_export_as_docx`:
    
    **Описание**: Экспортирует артефакт в DOCX-файл.

    **Параметры**:
    - `artifact_file_path` (`str`): Путь к файлу для экспорта.
    - `artifact_data` (`Union[dict, str]`): Данные для экспорта.
    - `content_original_format` (`str`): Исходный формат содержимого (например, `text`, `markdown`).
    - `verbose` (`bool`, optional): Флаг для вывода отладочных сообщений. По умолчанию `False`.
        
    **Вызывает исключения**:
    - `ValueError`: Если `content_original_format` не является `text`, `txt`, `markdown` или `md`.
*   `_compose_filepath`:
    
    **Описание**: Составляет путь к файлу для экспорта артефакта.

    **Параметры**:
    - `artifact_data` (`Union[dict, str]`): Данные для экспорта.
    - `artifact_name` (`str`): Имя артефакта.
    - `content_type` (`str`): Тип содержимого артефакта.
    - `target_format` (`str`, optional): Целевой формат экспорта (например, 'json', 'txt', 'docx'). По умолчанию `None`.
    - `verbose` (`bool`, optional): Флаг для вывода отладочных сообщений. По умолчанию `False`.

    **Возвращает**:
    - `str`: Составленный путь к файлу.

### `Normalizer`

**Описание**: Класс `Normalizer` предназначен для нормализации текстовых элементов.

**Методы**:

*   `__init__`:
    
    **Описание**: Инициализирует экземпляр класса `Normalizer`.

    **Параметры**:
    - `elements` (`List[str]`): Список элементов для нормализации.
    - `n` (`int`): Количество нормализованных элементов для вывода.
    - `verbose` (`bool`, optional): Флаг для вывода отладочных сообщений. По умолчанию `False`.
*   `normalize`:
    
    **Описание**: Нормализует один или несколько элементов.

    **Параметры**:
    - `element_or_elements` (`Union[str, List[str]]`): Элемент или элементы для нормализации.

    **Возвращает**:
    - `Union[str, List[str]]`: Нормализованный элемент или список нормализованных элементов.
    
    **Вызывает исключения**:
    - `ValueError`: Если `element_or_elements` не является строкой или списком.

## Функции

### `default_extractor`

**Описание**: Экземпляр класса `ResultsExtractor` по умолчанию.