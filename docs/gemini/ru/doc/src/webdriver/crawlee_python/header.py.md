# Модуль `header.py`

## Обзор

Модуль `header.py` содержит основные настройки и информацию о проекте, включая версию, имя проекта, автора и т.д. Он также определяет функцию для поиска корневой директории проекта и загружает настройки из файла `settings.json`.

## Содержание
- [Обзор](#обзор)
- [Функции](#функции)
    - [`set_project_root`](#set_project_root)
- [Переменные](#переменные)
    - [`MODE`](#mode)
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
Находит корневую директорию проекта, начиная с директории текущего файла, и ищет вверх до первой директории, содержащей любой из указанных маркерных файлов.

**Параметры**:
- `marker_files` (tuple): Кортеж имен файлов или директорий, которые идентифицируют корень проекта. По умолчанию: `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если она найдена; иначе - путь к директории, где расположен скрипт.

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
Режим работы приложения. В данном случае установлено значение `'dev'`.
```python

```

### `__root__`

**Описание**:
Путь к корневой директории проекта, вычисленный с помощью функции `set_project_root`.
```python
__root__ = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""
```

### `settings`

**Описание**:
Словарь с настройками, загруженными из файла `settings.json`. Может быть `None`, если файл не найден или возникла ошибка при загрузке.
```python
settings:dict = None
```

### `doc_str`

**Описание**:
Строка с содержимым файла `README.MD`. Может быть `None`, если файл не найден или возникла ошибка при загрузке.
```python
doc_str:str = None
```

### `__project_name__`

**Описание**:
Имя проекта, полученное из настроек или по умолчанию `'hypotez'`.
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
Содержимое файла `README.MD`, сохраненное в строку или пустая строка `''`, если файл не найден.
```python
__doc__: str = doc_str if doc_str else ''
```

### `__details__`

**Описание**:
Строка с подробной информацией о проекте. В данном случае пустая строка `''`.
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
Информация об авторских правах проекта, полученная из настроек или пустая строка `''`.
```python
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
```

### `__cofee__`

**Описание**:
Сообщение для поддержки разработчика, полученное из настроек или сообщение по умолчанию.
```python
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"