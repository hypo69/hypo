# Модуль `header.py`

## Обзор

Модуль `header.py` предназначен для определения основных настроек и переменных проекта, а также для загрузки конфигурационных данных из файлов `settings.json` и `README.MD`. Модуль также включает функцию для определения корневой директории проекта.

## Оглавление

- [Функции](#Функции)
    - [`set_project_root`](#set_project_root)
- [Переменные](#Переменные)
    - [`MODE`](#MODE)
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
Находит корневой каталог проекта, начиная с каталога текущего файла, и ищет вверх по дереву каталогов, останавливаясь на первом каталоге, содержащем любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Кортеж имен файлов или каталогов для идентификации корня проекта.

**Возвращает**:
- `Path`: Путь к корневому каталогу, если он найден. В противном случае возвращается каталог, где находится скрипт.

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
```

## Переменные

### `MODE`

**Описание**:
Режим работы приложения. По умолчанию установлен в `'dev'`.

```python
MODE = 'dev'
```

### `__root__`

**Описание**:
Путь к корневому каталогу проекта, определенный функцией `set_project_root`.

```python
__root__ = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""
```

### `settings`

**Описание**:
Словарь с настройками проекта, загруженный из файла `settings.json`. Если файл не найден или содержит ошибки JSON, переменная будет `None`.

```python
settings:dict = None
```

### `doc_str`

**Описание**:
Строка с содержимым файла `README.MD`. Если файл не найден или содержит ошибки, переменная будет `None`.

```python
doc_str:str = None
```

### `__project_name__`

**Описание**:
Название проекта, полученное из настроек или значение по умолчанию `'hypotez'`.

```python
__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
```

### `__version__`

**Описание**:
Версия проекта, полученная из настроек или пустая строка `''`.

```python
__version__: str = settings.get("version", '')  if settings  else ''
```

### `__doc__`

**Описание**:
Содержимое документации проекта, полученное из `doc_str` или пустая строка `''`.

```python
__doc__: str = doc_str if doc_str else ''
```

### `__details__`

**Описание**:
Детали проекта, по умолчанию пустая строка `''`.

```python
__details__: str = ''
```

### `__author__`

**Описание**:
Автор проекта, полученный из настроек или пустая строка `''`.

```python
__author__: str = settings.get("author", '')  if settings  else ''
```

### `__copyright__`

**Описание**:
Информация об авторских правах, полученная из настроек или пустая строка `''`.

```python
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
```

### `__cofee__`

**Описание**:
Сообщение с предложением угостить разработчика кофе, полученное из настроек или значение по умолчанию.

```python
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```