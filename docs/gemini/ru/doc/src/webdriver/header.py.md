# Модуль `header`

## Обзор

Модуль `header.py` предназначен для определения корневой директории проекта, загрузки настроек из файла `settings.json`, чтения документации из файла `README.MD` и хранения общих переменных проекта.

## Содержание

- [Обзор](#обзор)
- [Функции](#функции)
  - [`set_project_root`](#set_project_root)
- [Переменные](#переменные)
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

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла, и останавливается на первой директории, содержащей любой из маркерных файлов.

**Параметры**:
- `marker_files` (tuple, optional): Кортеж имен файлов или директорий, идентифицирующих корень проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если она найдена. В противном случае возвращается директория, где расположен скрипт.

```python
def set_project_root(marker_files=('__root__','.git')) -> Path:
    """ Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.

    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
```

## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта.

```python
__root__:Path
```

### `settings`

**Описание**: Словарь с настройками проекта, загруженными из файла `settings.json`. Может быть `None`, если файл не найден или не удалось его прочитать.

```python
settings:dict = None
```

### `doc_str`

**Описание**: Строка с содержимым файла `README.MD`. Может быть `None`, если файл не найден или не удалось его прочитать.

```python
doc_str:str = None
```

### `__project_name__`

**Описание**: Название проекта, взятое из `settings.json` или `hypotez` по умолчанию.

```python
__project_name__: str
```

### `__version__`

**Описание**: Версия проекта, взятая из `settings.json` или пустая строка по умолчанию.

```python
__version__: str
```

### `__doc__`

**Описание**: Документация проекта, взятая из `doc_str` или пустая строка по умолчанию.

```python
__doc__: str
```

### `__details__`

**Описание**: Дополнительная информация о проекте, пока пустая строка.

```python
__details__: str = ''
```

### `__author__`

**Описание**: Автор проекта, взятый из `settings.json` или пустая строка по умолчанию.

```python
__author__: str
```

### `__copyright__`

**Описание**: Информация об авторских правах, взятая из `settings.json` или пустая строка по умолчанию.

```python
__copyright__: str
```

### `__cofee__`

**Описание**: Сообщение о возможности поддержать разработчика, взятое из `settings.json` или дефолтная строка со ссылкой на boosty.

```python
__cofee__: str