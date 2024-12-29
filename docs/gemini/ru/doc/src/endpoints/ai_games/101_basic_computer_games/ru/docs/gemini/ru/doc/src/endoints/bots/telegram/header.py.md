# `hypotez/src/logger/header.py`

## Обзор

Модуль `header.py` предназначен для определения корневого пути проекта и загрузки настроек из файла `settings.json`. Он также обеспечивает доступ к информации о проекте, такой как имя, версия, автор и т.д.

## Оглавление

1. [Функции](#функции)
    - [`set_project_root`](#set_project_root)
2. [Переменные](#переменные)
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
Функция `set_project_root` находит корневой каталог проекта, начиная с текущего каталога файла, и ищет вверх по дереву каталогов, останавливаясь на первом каталоге, содержащем любой из маркеров.

**Параметры**:
- `marker_files` (tuple): Кортеж с именами файлов или каталогов, используемых для идентификации корня проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневому каталогу проекта, если он найден. В противном случае возвращается каталог, где расположен скрипт.

```python
def set_project_root(marker_files=('__root__','.git')) -> Path:
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

## Переменные

### `__root__`

**Описание**:
`__root__` является переменной типа `Path` и хранит абсолютный путь к корневому каталогу проекта.

```python
__root__ = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""
```

### `settings`
**Описание**:
`settings` является переменной типа `dict` и хранит словарь с настройками проекта, загруженными из файла `settings.json`. Если файл не найден или содержит ошибку, значение переменной остается `None`.

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
`doc_str` является переменной типа `str` и хранит строку с содержимым файла `README.MD`. Если файл не найден или содержит ошибку, значение переменной остается `None`.
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
`__project_name__` является переменной типа `str` и хранит имя проекта, которое считывается из `settings.json`. Если в `settings.json` не найдено `project_name` или `settings` не был загружен, то имя проекта `hypotez`.

```python
__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
```

### `__version__`

**Описание**:
`__version__` является переменной типа `str` и хранит текущую версию проекта, считанную из `settings.json`. Если в `settings.json` не найдено `version` или `settings` не был загружен, то версия проекта пустая строка `''`.

```python
__version__: str = settings.get("version", '')  if settings  else ''
```

### `__doc__`

**Описание**:
`__doc__` является переменной типа `str` и хранит содержание файла `README.MD`. Если не удалось прочитать файл или переменная `doc_str` равна `None`, то переменная `__doc__` будет пустой строкой `''`.

```python
__doc__: str = doc_str if doc_str else ''
```

### `__details__`
**Описание**:
`__details__` является переменной типа `str` и хранит дополнительную информацию о проекте. В текущей версии переменная инициализируется пустой строкой.

```python
__details__: str = ''
```

### `__author__`
**Описание**:
`__author__` является переменной типа `str` и хранит имя автора проекта, считанное из `settings.json`. Если в `settings.json` не найдено `author` или `settings` не был загружен, то автор проекта пустая строка `''`.

```python
__author__: str = settings.get("author", '')  if settings  else ''
```

### `__copyright__`

**Описание**:
`__copyright__` является переменной типа `str` и хранит информацию об авторских правах проекта, считанную из `settings.json`. Если в `settings.json` не найдено `copyrihgnt` или `settings` не был загружен, то значение авторских прав пустая строка `''`.

```python
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
```
### `__cofee__`
**Описание**:
`__cofee__` является переменной типа `str` и хранит сообщение с ссылкой на страницу поддержки разработчика, считанную из `settings.json`. Если в `settings.json` не найдено `cofee` или `settings` не был загружен, то сообщение берется по умолчанию.

```python
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```