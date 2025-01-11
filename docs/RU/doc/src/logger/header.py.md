# Модуль `header`

## Обзор

Модуль `header.py` предназначен для определения корневого пути проекта и загрузки основных параметров проекта из файла `settings.json`. Он обеспечивает согласованную работу с путями и параметрами проекта, импортируя необходимые модули.

## Оглавление

1.  [Обзор](#обзор)
2.  [Функции](#функции)
    *   [`set_project_root`](#set_project_root)
3.  [Переменные](#переменные)
    *   [`__root__`](#__root__)
    *   [`settings`](#settings)
    *  [`doc_str`](#doc_str)
    *   [`__project_name__`](#__project_name__)
    *   [`__version__`](#__version__)
    *   [`__doc__`](#__doc__)
    *   [`__details__`](#__details__)
    *   [`__author__`](#__author__)
    *   [`__copyright__`](#__copyright__)
    *   [`__cofee__`](#__cofee__)

## Функции

### `set_project_root`

**Описание**:
Находит корневой каталог проекта, начиная с каталога текущего файла, и поднимаясь вверх по дереву каталогов, пока не найдет один из маркерных файлов.

**Параметры**:
- `marker_files` (tuple, optional): Кортеж имен файлов или каталогов для определения корня проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневому каталогу, если он найден, иначе путь к каталогу, где расположен скрипт.

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

## Переменные

### `__root__`

**Описание**:
Путь к корневому каталогу проекта. Определяется функцией `set_project_root`.

```python
__root__ = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""
```

### `settings`

**Описание**:
Словарь с настройками проекта, загруженный из файла `settings.json`.

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
Строка содержащая документацию из файла README.MD
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
Имя проекта, извлекается из `settings.json` или установлено значение по умолчанию `hypotez`.

```python
__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
```

### `__version__`

**Описание**:
Версия проекта, извлекается из `settings.json` или установлено значение по умолчанию `''`.

```python
__version__: str = settings.get("version", '')  if settings  else ''
```

### `__doc__`

**Описание**:
Документация проекта, извлекается из `README.MD` или установлено значение по умолчанию `''`.
```python
__doc__: str = doc_str if doc_str else ''
```
### `__details__`

**Описание**:
Строка для подробностей о проекте. Изначально пустая строка.

```python
__details__: str = ''
```

### `__author__`

**Описание**:
Автор проекта, извлекается из `settings.json` или установлено значение по умолчанию `''`.

```python
__author__: str = settings.get("author", '')  if settings  else ''
```

### `__copyright__`

**Описание**:
Авторские права проекта, извлекается из `settings.json` или установлено значение по умолчанию `''`.

```python
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
```

### `__cofee__`

**Описание**:
Сообщение для поддержки разработчика, извлекается из `settings.json` или установлено значение по умолчанию `"Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"`.

```python
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```