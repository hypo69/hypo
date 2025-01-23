# Модуль `header.py`

## Обзор

Модуль `header.py` предназначен для определения корневого пути проекта, загрузки настроек из файла `settings.json` и чтения документации из `README.MD`. Он также устанавливает глобальные переменные, такие как имя проекта, версия, автор и т.д.

## Содержание

1.  [Функции](#Функции)
    -   [`set_project_root`](#set_project_root)
2.  [Глобальные переменные](#Глобальные-переменные)
    -   [`__root__`](#__root__)
    -   [`settings`](#settings)
    -   [`doc_str`](#doc_str)
    -   [`__project_name__`](#__project_name__)
    -   [`__version__`](#__version__)
    -   [`__doc__`](#__doc__)
    -   [`__details__`](#__details__)
    -   [`__author__`](#__author__)
    -   [`__copyright__`](#__copyright__)
    -    [`__cofee__`](#__cofee__)

## Функции

### `set_project_root`

**Описание**: Находит корневой каталог проекта, начиная с каталога текущего файла, и останавливается на первом каталоге, содержащем любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Кортеж имен файлов или каталогов для идентификации корня проекта.

**Возвращает**:
- `Path`: Путь к корневому каталогу, если найден, иначе путь к каталогу, где расположен скрипт.

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

**Описание**: Путь к корневому каталогу проекта.
```python
__root__: Path = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""
```

### `settings`

**Описание**: Словарь, содержащий настройки проекта, загруженные из файла `settings.json`. Может быть `None`, если файл не найден или произошла ошибка декодирования JSON.
```python
settings:dict = None
```
### `doc_str`

**Описание**: Строка, содержащая содержимое файла `README.MD`. Может быть `None`, если файл не найден или произошла ошибка чтения.
```python
doc_str:str = None
```

### `__project_name__`

**Описание**: Имя проекта, полученное из файла `settings.json` или значение по умолчанию `'hypotez'`.
```python
__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
```

### `__version__`

**Описание**: Версия проекта, полученная из файла `settings.json` или пустая строка.
```python
__version__: str = settings.get("version", '')  if settings  else ''
```

### `__doc__`

**Описание**: Документация проекта, считанная из файла `README.MD`.
```python
__doc__: str = doc_str if doc_str else ''
```

### `__details__`

**Описание**: Дополнительная информация о проекте (на данный момент пустая строка).
```python
__details__: str = ''
```

### `__author__`

**Описание**: Автор проекта, полученный из файла `settings.json` или пустая строка.
```python
__author__: str = settings.get("author", '')  if settings  else ''
```

### `__copyright__`

**Описание**: Авторские права проекта, полученные из файла `settings.json` или пустая строка.
```python
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
```

### `__cofee__`

**Описание**: Сообщение с предложением угостить разработчика чашкой кофе, полученное из файла `settings.json` или значение по умолчанию.
```python
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"