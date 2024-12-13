# hypotez/src/webdriver/playwright/header.py

## Обзор

Данный модуль `header.py` предназначен для настройки и инициализации основных параметров проекта, включая определение корневой директории проекта, загрузку настроек из `settings.json`, чтение документации из `README.md`, а также установку основных переменных проекта, таких как имя, версия, автор и т.д.

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

**Описание**:
Находит корневой каталог проекта, начиная с текущего каталога файла, двигаясь вверх и останавливаясь в первом каталоге, содержащем любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Кортеж с именами файлов или каталогов, которые идентифицируют корень проекта. По умолчанию `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:
- `Path`: Путь к корневому каталогу, если он найден, или к каталогу, где расположен скрипт.

```python
def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.

    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
    ...
```

## Глобальные переменные

### `__root__`

**Описание**:
Путь к корневому каталогу проекта. Устанавливается с помощью функции `set_project_root`.

```python
__root__ = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""
```

### `settings`

**Описание**:
Словарь с настройками проекта, загруженными из файла `settings.json`.

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
Строка с документацией проекта, загруженная из файла `README.MD`.

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
Имя проекта, извлекается из `settings.json` или устанавливается как `hypotez` по умолчанию.

```python
__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
```

### `__version__`

**Описание**:
Версия проекта, извлекается из `settings.json` или устанавливается пустой строкой по умолчанию.

```python
__version__: str = settings.get("version", '')  if settings  else ''
```

### `__doc__`

**Описание**:
Документация проекта, загруженная из `README.MD` или устанавливается пустой строкой по умолчанию.

```python
__doc__: str = doc_str if doc_str else ''
```

### `__details__`

**Описание**:
Детали проекта, пока пустая строка.

```python
__details__: str = ''
```

### `__author__`

**Описание**:
Автор проекта, извлекается из `settings.json` или устанавливается пустой строкой по умолчанию.

```python
__author__: str = settings.get("author", '')  if settings  else ''
```

### `__copyright__`

**Описание**:
Информация об авторских правах, извлекается из `settings.json` или устанавливается пустой строкой по умолчанию.

```python
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
```

### `__cofee__`

**Описание**:
Сообщение о поддержке проекта (ссылка на boosty), извлекается из `settings.json` или устанавливается строкой по умолчанию.

```python
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"