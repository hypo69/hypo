# Модуль `header.py`

## Обзор

Модуль `header.py` предназначен для определения корневой директории проекта, загрузки настроек из `settings.json` и чтения документации из `README.md`. Также он предоставляет глобальные переменные с информацией о проекте.

## Оглавление
- [Функции](#Функции)
    - [`set_project_root`](#set_project_root)
- [Глобальные переменные](#Глобальные-переменные)
    - [`__root__`](#__root__)
    - [`settings`](#settings)
    - [`doc_str`](#doc_str)
    - [`__project_name__`](#__project_name__)
    - [`__version__`](#__version__)
    - [`__doc__`](#__doc__)
    - [`__details__`](#__details__)
    - [`__author__`](#__author__)
    - [`__copyright__`](#__copyright__)
    - [`__cofee__`](#__cofee__)


## Функции

### `set_project_root`

**Описание**:
Находит корневой каталог проекта, начиная с каталога текущего файла, путем поиска вверх до первого каталога, содержащего любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple, optional): Имена файлов или каталогов, которые идентифицируют корень проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневому каталогу, если он найден, или каталог, где находится скрипт.

```python
def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.

    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
```
## Глобальные переменные
 
### `__root__`

**Описание**:
`Path` к корневой директории проекта. Инициализируется функцией `set_project_root`.

```python
__root__: Path = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""
```

### `settings`
**Описание**:
Словарь с настройками проекта, загруженный из файла `settings.json`. Если файл не найден или произошла ошибка JSONDecodeError, значение будет `None`.

```python
settings:dict = None
try:
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = json.load(settings_file)
except (FileNotFoundError, json.JSONDecodeError):
    ...
```

### `doc_str`

**Описание**:
Строка с содержимым документации, загруженная из файла `README.md`. Если файл не найден или произошла ошибка JSONDecodeError, значение будет `None`.

```python
doc_str:str = None
try:
    with open(gs.path.root / 'src' /  'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError):
    ...
```

### `__project_name__`

**Описание**:
Строка с именем проекта. Получается из `settings.json` или `hypotez` по умолчанию.

```python
__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
```

### `__version__`

**Описание**:
Строка с версией проекта. Получается из `settings.json` или пустая строка по умолчанию.

```python
__version__: str = settings.get("version", '')  if settings  else ''
```

### `__doc__`

**Описание**:
Строка с документацией проекта.  Содержимое файла `README.md` или пустая строка по умолчанию.

```python
__doc__: str = doc_str if doc_str else ''
```

### `__details__`

**Описание**:
Строка с дополнительной информацией о проекте. В данном файле всегда пустая строка.

```python
__details__: str = ''
```

### `__author__`

**Описание**:
Строка с именем автора проекта. Получается из `settings.json` или пустая строка по умолчанию.

```python
__author__: str = settings.get("author", '')  if settings  else ''
```

### `__copyright__`

**Описание**:
Строка с информацией об авторском праве. Получается из `settings.json` или пустая строка по умолчанию.

```python
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
```

### `__cofee__`

**Описание**:
Строка с предложением угостить разработчика кофе. Получается из `settings.json` или строка с ссылкой на Boosty по умолчанию.

```python
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"