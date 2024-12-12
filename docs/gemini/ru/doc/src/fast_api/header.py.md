# Модуль `header.py`

## Обзор

Модуль `header.py` предназначен для инициализации основных настроек проекта, включая определение корневой директории, загрузку конфигураций из `settings.json`, и получение документации из `README.MD`. Он также предоставляет основные сведения о проекте, такие как имя, версия, автор и копирайт.

## Содержание

1. [Функции](#Функции)
    - [`set_project_root`](#set_project_root)
2. [Глобальные переменные](#Глобальные-переменные)
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

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла и двигаясь вверх до первой директории, содержащей один из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Кортеж имен файлов или директорий для определения корневой директории проекта. По умолчанию: `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если она найдена, иначе путь к директории, где расположен скрипт.

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

## Глобальные переменные

### `__root__`

**Описание**: Путь к корневой директории проекта. Устанавливается функцией `set_project_root`.

### `settings`

**Описание**: Словарь настроек проекта, загруженный из файла `settings.json`. Если файл не найден или не удается декодировать JSON, значение будет `None`.

### `doc_str`

**Описание**: Содержимое файла `README.MD` в виде строки. Если файл не найден, значение будет `None`.

### `__project_name__`

**Описание**: Имя проекта, загруженное из `settings.json` или `'hypotez'`, если `settings` не определен.

### `__version__`

**Описание**: Версия проекта, загруженная из `settings.json` или `''`, если `settings` не определен.

### `__doc__`

**Описание**: Документация проекта, загруженная из `doc_str`. Если `doc_str` не определен, то `''`.

### `__details__`

**Описание**: Детали проекта, на данный момент всегда пустая строка `''`.

### `__author__`

**Описание**: Автор проекта, загруженный из `settings.json` или `''`, если `settings` не определен.

### `__copyright__`

**Описание**: Копирайт проекта, загруженный из `settings.json` или `''`, если `settings` не определен.

### `__cofee__`

**Описание**: Текст, предлагающий угостить разработчика кофе, загруженный из `settings.json` или значение по умолчанию, если `settings` не определен.