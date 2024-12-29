# Модуль `extraction`

## Обзор

Модуль `extraction` предоставляет инструменты для извлечения, уменьшения и экспорта данных из элементов TinyTroupe, таких как агенты и миры. Он позволяет:

- Извлекать основные моменты из истории взаимодействий агента.
- Генерировать синтетические данные из симуляции.
- Преобразовывать данные в машиночитаемые форматы, такие как JSON или CSV.
- Уменьшать извлеченные данные до более краткой формы.
- Экспортировать артефакты из элементов TinyTroupe.

## Содержание

- [Классы](#классы)
    - [`ResultsExtractor`](#resultsextractor)
    - [`ResultsReducer`](#resultsreducer)
    - [`ArtifactExporter`](#artifactexporter)
    - [`Normalizer`](#normalizer)
- [Функции](#функции)
    - [`default_extractor`](#default_extractor)

## Классы

### `ResultsExtractor`

**Описание**: Класс для извлечения результатов из агентов и миров TinyTroupe.

**Методы**:
- `__init__`: Инициализирует объект `ResultsExtractor`.
- `extract_results_from_agent`: Извлекает результаты из экземпляра `TinyPerson`.
- `extract_results_from_world`: Извлекает результаты из экземпляра `TinyWorld`.
- `save_as_json`: Сохраняет последние результаты извлечения в формате JSON.

#### `__init__`

```python
def __init__(self):
    """
    Инициализирует объект ResultsExtractor.
    """
```

#### `extract_results_from_agent`

```python
def extract_results_from_agent(self, 
                        tinyperson:TinyPerson, 
                        extraction_objective:str="The main points present in the agent\'s interactions history.", 
                        situation:str = "", 
                        fields:list=None,
                        fields_hints:dict=None,
                        verbose:bool=False) -> dict | None:
    """
    Извлекает результаты из экземпляра TinyPerson.

    Args:
        tinyperson (TinyPerson): Экземпляр `TinyPerson`, из которого извлекаются результаты.
        extraction_objective (str): Цель извлечения.
        situation (str): Ситуация, которую необходимо учитывать.
        fields (list, optional): Список полей для извлечения. Если `None`, извлекатель определит, какие имена использовать. По умолчанию `None`.
        fields_hints (dict, optional): Словарь подсказок для полей. По умолчанию `None`.
        verbose (bool, optional): Выводить ли отладочные сообщения. По умолчанию `False`.

    Returns:
        dict | None: Извлеченные результаты в виде словаря или `None`, если извлечение не удалось.
    """
```

#### `extract_results_from_world`

```python
def extract_results_from_world(self, 
                                   tinyworld:TinyWorld, 
                                   extraction_objective:str="The main points that can be derived from the agents conversations and actions.", 
                                   situation:str="", 
                                   fields:list=None,
                                   fields_hints:dict=None,
                                   verbose:bool=False) -> dict | None:
    """
    Извлекает результаты из экземпляра TinyWorld.

    Args:
        tinyworld (TinyWorld): Экземпляр `TinyWorld`, из которого извлекаются результаты.
        extraction_objective (str): Цель извлечения.
        situation (str): Ситуация, которую необходимо учитывать.
        fields (list, optional): Список полей для извлечения. Если `None`, извлекатель определит, какие имена использовать. По умолчанию `None`.
        fields_hints (dict, optional): Словарь подсказок для полей. По умолчанию `None`.
        verbose (bool, optional): Выводить ли отладочные сообщения. По умолчанию `False`.

    Returns:
        dict | None: Извлеченные результаты в виде словаря или `None`, если извлечение не удалось.
    """
```

#### `save_as_json`

```python
def save_as_json(self, filename:str, verbose:bool=False):
    """
    Сохраняет последние результаты извлечения в формате JSON.

    Args:
        filename (str): Имя файла для сохранения JSON.
        verbose (bool, optional): Выводить ли отладочные сообщения. По умолчанию `False`.
    """
```

### `ResultsReducer`

**Описание**: Класс для уменьшения данных, полученных от агентов TinyTroupe.

**Методы**:
- `__init__`: Инициализирует объект `ResultsReducer`.
- `add_reduction_rule`: Добавляет правило уменьшения.
- `reduce_agent`: Уменьшает данные агента.
- `reduce_agent_to_dataframe`: Уменьшает данные агента и преобразует их в `pandas.DataFrame`.

#### `__init__`

```python
def __init__(self):
    """
    Инициализирует объект ResultsReducer.
    """
```

#### `add_reduction_rule`

```python
def add_reduction_rule(self, trigger: str, func: callable):
    """
    Добавляет правило уменьшения.

    Args:
        trigger (str): Тип триггера для применения правила.
        func (callable): Функция для уменьшения данных.

    Raises:
        Exception: Если правило для указанного триггера уже существует.
    """
```

#### `reduce_agent`

```python
def reduce_agent(self, agent: TinyPerson) -> list:
    """
    Уменьшает данные агента.

    Args:
        agent (TinyPerson): Агент, данные которого необходимо уменьшить.

    Returns:
        list: Список уменьшенных данных.
    """
```

#### `reduce_agent_to_dataframe`

```python
def reduce_agent_to_dataframe(self, agent: TinyPerson, column_names: list=None) -> pd.DataFrame:
    """
    Уменьшает данные агента и преобразует их в pandas.DataFrame.

    Args:
        agent (TinyPerson): Агент, данные которого необходимо уменьшить.
        column_names (list, optional): Список имен столбцов для DataFrame. По умолчанию None.

    Returns:
        pd.DataFrame: DataFrame с уменьшенными данными.
    """
```

### `ArtifactExporter`

**Описание**: Класс для экспорта артефактов из элементов TinyTroupe.

**Методы**:
- `__init__`: Инициализирует объект `ArtifactExporter`.
- `export`: Экспортирует данные артефакта в файл.
- `_export_as_txt`: Экспортирует данные в текстовый файл.
- `_export_as_json`: Экспортирует данные в JSON файл.
- `_export_as_docx`: Экспортирует данные в файл DOCX.
- `_compose_filepath`: Составляет путь к файлу артефакта.

#### `__init__`

```python
def __init__(self, base_output_folder:str) -> None:
    """
    Инициализирует объект ArtifactExporter.

    Args:
        base_output_folder (str): Базовая папка для экспорта.
    """
```

#### `export`

```python
def export(self, artifact_name:str, artifact_data:Union[dict, str], content_type:str, content_format:str=None, target_format:str="txt", verbose:bool=False):
    """
    Экспортирует указанные данные артефакта в файл.

    Args:
        artifact_name (str): Имя артефакта.
        artifact_data (Union[dict, str]): Данные для экспорта. Если передан словарь, он будет сохранен в JSON. Если строка, то будет сохранена как есть.
        content_type (str): Тип содержимого артефакта.
        content_format (str, optional): Формат содержимого артефакта (например, md, csv и т.д.). По умолчанию None.
        target_format (str, optional): Формат для экспорта артефакта (например, json, txt, docx и т.д.). По умолчанию "txt".
        verbose (bool, optional): Выводить ли отладочные сообщения. По умолчанию False.

    Raises:
        ValueError: Если `artifact_data` не является строкой или словарем.
        ValueError: Если указанный `target_format` не поддерживается.
    """
```

#### `_export_as_txt`

```python
def _export_as_txt(self, artifact_file_path:str, artifact_data:Union[dict, str], content_type:str, verbose:bool=False):
    """
    Экспортирует указанные данные артефакта в текстовый файл.

    Args:
        artifact_file_path (str): Путь к файлу для сохранения текстовых данных.
        artifact_data (Union[dict, str]): Данные для экспорта.
        content_type (str): Тип содержимого артефакта.
        verbose (bool, optional): Выводить ли отладочные сообщения. По умолчанию `False`.
    """
```

#### `_export_as_json`

```python
def _export_as_json(self, artifact_file_path:str, artifact_data:Union[dict, str], content_type:str, verbose:bool=False):
    """
    Экспортирует указанные данные артефакта в файл JSON.

    Args:
        artifact_file_path (str): Путь к файлу для сохранения JSON данных.
        artifact_data (Union[dict, str]): Данные для экспорта.
        content_type (str): Тип содержимого артефакта.
         verbose (bool, optional): Выводить ли отладочные сообщения. По умолчанию `False`.

    Raises:
        ValueError: Если `artifact_data` не является словарем.
    """
```

#### `_export_as_docx`

```python
def _export_as_docx(self, artifact_file_path:str, artifact_data:Union[dict, str], content_original_format:str, verbose:bool=False):
    """
    Экспортирует указанные данные артефакта в файл DOCX.

    Args:
        artifact_file_path (str): Путь к файлу для сохранения DOCX данных.
        artifact_data (Union[dict, str]): Данные для экспорта.
        content_original_format (str): Исходный формат содержимого (текст или Markdown).
        verbose (bool, optional): Выводить ли отладочные сообщения. По умолчанию `False`.

    Raises:
        ValueError: Если `content_original_format` не является 'text' или 'markdown'.
    """
```

#### `_compose_filepath`

```python
def _compose_filepath(self, artifact_data:Union[dict, str], artifact_name:str, content_type:str, target_format:str=None, verbose:bool=False):
    """
    Составляет путь к файлу артефакта.

    Args:
        artifact_data (Union[dict, str]): Данные для экспорта.
        artifact_name (str): Имя артефакта.
        content_type (str): Тип содержимого артефакта.
        target_format (str, optional): Формат файла (например, json, txt, docx и т.д.). По умолчанию None.
        verbose (bool, optional): Выводить ли отладочные сообщения. По умолчанию `False`.

    Returns:
        str: Полный путь к файлу артефакта.
    """
```

### `Normalizer`

**Описание**: Класс для нормализации текстовых элементов.

**Методы**:
- `__init__`: Инициализирует объект `Normalizer`.
- `normalize`: Нормализует заданный элемент или список элементов.

#### `__init__`

```python
def __init__(self, elements:List[str], n:int, verbose:bool=False):
    """
    Инициализирует объект Normalizer.

    Args:
        elements (list): Элементы для нормализации.
        n (int): Количество нормализованных элементов для вывода.
        verbose (bool, optional): Выводить ли отладочные сообщения. По умолчанию `False`.
    """
```

#### `normalize`

```python
def normalize(self, element_or_elements:Union[str, List[str]]) -> Union[str, List[str]]:
    """
    Нормализует указанный элемент или список элементов.

    Этот метод использует механизм кэширования для повышения производительности. Если элемент уже был нормализован, его нормализованная форма
    хранится в кэше (self.normalizing_map). При повторной необходимости нормализации того же элемента метод сначала проверит кэш и использует
    сохраненную нормализованную форму, если она доступна, вместо повторной нормализации.

    Порядок элементов в выводе будет таким же, как во вводе. Это обеспечивается путем обработки элементов в порядке их появления во вводе
    и добавлением нормализованных элементов к списку вывода в том же порядке.

    Args:
        element_or_elements (Union[str, List[str]]): Элемент или список элементов для нормализации.

    Returns:
        Union[str, List[str]]: Нормализованный элемент или список нормализованных элементов.

    Raises:
        ValueError: Если `element_or_elements` не является строкой или списком.
    """
```

## Функции

### `default_extractor`

```python
default_extractor = ResultsExtractor()
```
**Описание**: Экземпляр класса `ResultsExtractor` по умолчанию.