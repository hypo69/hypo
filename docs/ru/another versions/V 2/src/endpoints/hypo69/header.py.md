# Модуль `header.py`

## Обзор

Модуль `header.py` предназначен для настройки и инициализации проекта, включая поиск корневой директории, загрузку настроек из `settings.json` и чтение документации из `README.MD`.

## Содержание

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

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла, и добавляет её в `sys.path`.

**Параметры**:
- `marker_files` (tuple): Кортеж с именами файлов или директорий, которые используются для идентификации корневой директории проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если она найдена; в противном случае возвращает директорию, где расположен скрипт.

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

**Описание**: Путь к корневой директории проекта.
```python
__root__: Path = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""
```

### `settings`

**Описание**: Словарь, содержащий настройки проекта, загруженные из файла `settings.json`. Может быть `None`, если файл не найден или не может быть декодирован.

```python
settings: dict = None
try:
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = json.load(settings_file)
except (FileNotFoundError, json.JSONDecodeError):
    ...
```

### `doc_str`

**Описание**: Строка, содержащая документацию проекта, загруженная из файла `README.MD`. Может быть `None`, если файл не найден или не может быть прочитан.
```python
doc_str: str = None
try:
    with open(gs.path.root / 'src' /  'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError):
    ...
```

### `__project_name__`

**Описание**: Имя проекта, полученное из настроек или установлено в `'hypotez'` по умолчанию.
```python
__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
```

### `__version__`

**Описание**: Версия проекта, полученная из настроек или установлена в `''` по умолчанию.
```python
__version__: str = settings.get("version", '')  if settings  else ''
```

### `__doc__`

**Описание**: Документация проекта, полученная из файла `README.MD` или установлена в `''` по умолчанию.
```python
__doc__: str = doc_str if doc_str else ''
```

### `__details__`

**Описание**: Детали проекта (пустая строка по умолчанию).
```python
__details__: str = ''
```

### `__author__`

**Описание**: Автор проекта, полученный из настроек или установлена в `''` по умолчанию.
```python
__author__: str = settings.get("author", '')  if settings  else ''
```

### `__copyright__`

**Описание**: Авторские права проекта, полученные из настроек или установлена в `''` по умолчанию.
```python
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
```

### `__cofee__`

**Описание**: Строка, содержащая призыв к поддержке разработчика, полученная из настроек или установлена значением по умолчанию.
```python
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"