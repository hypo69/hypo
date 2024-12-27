# Модуль `header.py`

## Обзор

Модуль `header.py` предназначен для определения основных настроек и метаданных проекта, таких как путь к корневой директории, версия проекта, имя проекта, а также загружает настройки из файла `settings.json` и `README.MD`.

## Оглавление
1. [Функции](#Функции)
    - [`set_project_root`](#set_project_root)
2. [Переменные](#Переменные)
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
Находит корневую директорию проекта, начиная с директории текущего файла, ища вверх и останавливаясь на первой директории, содержащей любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple, optional): Кортеж с именами файлов или директорий, которые используются для определения корневой директории проекта. По умолчанию `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если она найдена. В противном случае возвращает директорию, где расположен скрипт.

```python
def set_project_root(marker_files=('__root__')) -> Path:
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
Путь к корневой директории проекта, определенный функцией `set_project_root`.

### `settings`

**Описание**:
Словарь с настройками проекта, загруженный из файла `settings.json`. Если файл не найден или неверного формата, переменная остается `None`.

### `doc_str`

**Описание**:
Строка с содержимым файла `README.MD`. Если файл не найден или неверного формата, переменная остается `None`.

### `__project_name__`

**Описание**:
Имя проекта, взятое из `settings.json` или по умолчанию `'hypotez'`.

### `__version__`

**Описание**:
Версия проекта, взятая из `settings.json` или по умолчанию `''`.

### `__doc__`

**Описание**:
Содержимое файла README.MD.

### `__details__`

**Описание**:
Подробная информация о проекте. В текущей версии всегда `''`.

### `__author__`

**Описание**:
Имя автора проекта, взятое из `settings.json` или по умолчанию `''`.

### `__copyright__`

**Описание**:
Информация об авторских правах, взятая из `settings.json` или по умолчанию `''`.

### `__cofee__`

**Описание**:
Строка со ссылкой на возможность угостить разработчика кофе, взятая из `settings.json` или строка по умолчанию: "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"