# Модуль extraction

## Обзор

Этот модуль предоставляет инструменты для извлечения структурированных данных из элементов TinyTroupe, таких как агенты и миры. Он включает в себя механизмы для сжатия данных и экспорта артефактов. Модуль демонстрирует различие между агентами-симуляциями и помощниками ИИ, поскольку последние не предназначены для интроспекции таким образом.


## Классы

### `ResultsExtractor`

**Описание**: Класс `ResultsExtractor` предназначен для извлечения результатов из агентов и миров. Он кеширует результаты извлечения для последующего использования.

**Методы**

#### `extract_results_from_agent`

**Описание**: Извлекает результаты из объекта `TinyPerson`.

**Параметры**:
- `tinyperson` (TinyPerson): Экземпляр объекта `TinyPerson`.
- `extraction_objective` (str): Цель извлечения.
- `situation` (str): Ситуация, для которой нужно извлечь данные.
- `fields` (list, optional): Список полей для извлечения. Если `None`, извлечение будет по умолчанию.
- `fields_hints` (dict, optional): Словарь с подсказками для полей.
- `verbose` (bool, optional): Выводить ли отладочные сообщения.

**Возвращает**:
- `dict | None`: Результаты извлечения в виде словаря или `None`, если возникла ошибка.

**Вызывает исключения**
- Не указано


#### `extract_results_from_world`

**Описание**: Извлекает результаты из объекта `TinyWorld`.

**Параметры**:
- `tinyworld` (TinyWorld): Экземпляр объекта `TinyWorld`.
- `extraction_objective` (str): Цель извлечения.
- `situation` (str): Ситуация, для которой нужно извлечь данные.
- `fields` (list, optional): Список полей для извлечения. Если `None`, извлечение будет по умолчанию.
- `fields_hints` (dict, optional): Словарь с подсказками для полей.
- `verbose` (bool, optional): Выводить ли отладочные сообщения.

**Возвращает**:
- `dict | None`: Результаты извлечения в виде словаря или `None`, если возникла ошибка.

**Вызывает исключения**
- Не указано

#### `save_as_json`

**Описание**: Сохраняет результаты извлечения в формате JSON.

**Параметры**:
- `filename` (str): Имя файла для сохранения.
- `verbose` (bool, optional): Выводить ли отладочные сообщения.

**Возвращает**:
- Не указано

**Вызывает исключения**
- Не указано


### `ResultsReducer`

**Описание**: Класс `ResultsReducer` предназначен для сжатия данных, полученных с помощью `ResultsExtractor`.


**Методы**

#### `add_reduction_rule`

**Описание**: Добавляет правило сокращения.

**Параметры**:
- `trigger` (str): Триггер для срабатывания правила.
- `func` (callable): Функция, которая выполняет сокращение.


**Возвращает**:
- Не указано

**Вызывает исключения**:
- `Exception`: Если правило для данного триггера уже существует.

#### `reduce_agent`

**Описание**: Применяет правила сокращения к агенту.

**Параметры**:
- `agent` (TinyPerson): Объект агента.

**Возвращает**:
- `list`: Список результатов сокращения.


**Вызывает исключения**
- Не указано


#### `reduce_agent_to_dataframe`

**Описание**: Преобразует результаты сокращения в DataFrame.

**Параметры**:
- `agent` (TinyPerson): Объект агента.
- `column_names` (list, optional): Имена столбцов для DataFrame.

**Возвращает**:
- `pd.DataFrame`: DataFrame с результатами сокращения.


**Вызывает исключения**
- Не указано



### `ArtifactExporter`

**Описание**: Класс `ArtifactExporter` отвечает за экспорт артефактов из элементов TinyTroupe.

**Методы**

#### `export`

**Описание**: Экспортирует данные артефакта в файл.

**Параметры**:
- `artifact_name` (str): Имя артефакта.
- `artifact_data` (Union[dict, str]): Данные артефакта (словарь или строка).
- `content_type` (str): Тип содержимого артефакта.
- `content_format` (str, optional): Формат содержимого артефакта.
- `target_format` (str): Целевой формат экспорта.
- `verbose` (bool, optional): Выводить ли отладочные сообщения.


**Возвращает**:
- Не указано

**Вызывает исключения**:
- `ValueError`: Если тип данных артефакта не поддерживается.
- Не указано


#### `_export_as_txt`

**Описание**: Экспортирует артефакт в текстовый файл.

#### `_export_as_json`

**Описание**: Экспортирует артефакт в JSON-файл.

#### `_export_as_docx`

**Описание**: Экспортирует артефакт в DOCX-файл.

#### `_compose_filepath`

**Описание**: Составляет путь к файлу для экспорта.

### `Normalizer`

**Описание**: Класс `Normalizer` предназначен для нормализации текстовых элементов.

**Методы**

#### `__init__`

**Описание**: Инициализирует нормализатор.

**Параметры**:
- `elements` (list): Элементы для нормализации.
- `n` (int): Количество элементов для нормализации.
- `verbose` (bool, optional): Выводить ли отладочные сообщения.

**Возвращает**:
- Не указано

**Вызывает исключения**
- Не указано


#### `normalize`

**Описание**: Нормализует элемент или список элементов.

**Параметры**:
- `element_or_elements` (Union[str, List[str]]): Элемент или список элементов для нормализации.

**Возвращает**:
- str/list: Нормализованный элемент/список.


**Вызывает исключения**
- `ValueError`: Если входной параметр не является строкой или списком.



## Функции

- Не указано