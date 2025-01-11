# Модуль `hypotez/src/suppliers/hb/header.py`

## Обзор

Этот модуль содержит функции для определения корневой директории проекта, загрузки настроек из файла `settings.json` и чтения документации из файла `README.MD`. Он инициализирует переменные, хранящие имя проекта, версию, описание, детали, автора, копирайт и ссылку на поддержку разработчика.

## Оглавление

- [Функции](#функции)
    - [`set_project_root`](#set_project_root)


## Функции

### `set_project_root`

**Описание**: Определяет корневую директорию проекта, начиная с директории текущего файла и перемещаясь вверх по иерархии директорий.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, которые используются для определения корневой директории проекта.  По умолчанию содержит ('pyproject.toml', 'requirements.txt', '.git').

**Возвращает**:

- `Path`: Путь до корневой директории проекта, если она найдена. В противном случае возвращает директорию, в которой расположен текущий файл.


**Вызывает исключения**:
- Нет


```python
def set_project_root(marker_files=(\'pyproject.toml\', \'requirements.txt\', \'.git\')) -> Path:
    """
    Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.

    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__
```

## Переменные


### `__root__`

**Описание**: Содержит путь к корневой директории проекта. Инициализируется вызовом функции `set_project_root()`.

**Тип**: `Path`

```python

# Get the root directory of the project
__root__ = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""
```


### `settings`

**Описание**: Словарь, содержащий настройки проекта. Загружается из файла `settings.json` в корне проекта.

**Тип**: `dict`


```python
settings:dict = None
try:
    with open(gs.path.root / \'src\' /  \'settings.json\', \'r\') as settings_file:
        settings = json.load(settings_file)
excep
t (FileNotFoundError, json.JSONDecodeError):
    ...
```

### `doc_str`

**Описание**: Строка, содержащая текст документации проекта (например, из файла README.MD).

**Тип**: `str`

```python
doc_str:str = None
try:
    with open(gs.path.root / \'src\' /  \'README.MD\', \'r\') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError):
    ...
```

### `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`

**Описание**: Переменные, содержащие имя проекта, версию, описание, детали, автора, копирайт и ссылку на поддержку разработчика соответственно. Значения инициализируются из словаря `settings`. Если ключ не найден или `settings` отсутствует, используется значение по умолчанию.

**Тип**: `str`


```python
__project_name__ = settings.get("project_name", \'hypotez\') if settings  else \'hypotez\'
__version__: str = settings.get("version", \'\')  if settings  else \'\'
__doc__: str = doc_str if doc_str else \'\'
__details__: str = \'\'
__author__: str = settings.get("author", \'\')  if settings  else \'\'
__copyright__: str = settings.get("copyrihgnt", \'\')  if settings  else \'\'
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```