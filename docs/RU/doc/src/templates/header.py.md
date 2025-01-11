# Модуль `header`

## Обзор

Модуль `header.py` предназначен для определения и установки корневой директории проекта, а также для добавления этой директории в `sys.path`. Это позволяет корректно импортировать модули из проекта, независимо от текущего рабочего каталога.

## Оглавление

- [Обзор](#обзор)
- [Функции](#функции)
    - [`set_project_root`](#set_project_root)
- [Переменные](#переменные)
    - [`__root__`](#__root__)

## Функции

### `set_project_root`

**Описание**:
Находит корневой каталог проекта, начиная с директории текущего файла,
поиск идет вверх по дереву каталогов до первого каталога, содержащего какой-либо из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Кортеж с именами файлов или каталогов для определения корневой директории проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если она найдена, в противном случае - путь к директории, где расположен скрипт.

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

**Описание**:
Путь к корневой директории проекта. Получается в результате работы функции `set_project_root`.
```python
__root__ = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""
```