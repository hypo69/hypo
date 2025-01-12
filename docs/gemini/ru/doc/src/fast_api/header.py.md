# Модуль `header.py`

## Обзор

Модуль `header.py` содержит функции и переменные для определения корневой директории проекта и настройки путей. Этот модуль предназначен для упрощения работы с путями в проекте и обеспечения корректной работы скриптов.

## Содержание

- [Функции](#функции)
    - [`set_project_root`](#set_project_root)
- [Переменные](#переменные)
    - [`__root__`](#__root__)

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла, поднимаясь вверх и останавливаясь на первой директории, содержащей один из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple, optional): Имена файлов или директорий, которые идентифицируют корневую директорию проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если она найдена, иначе директория, где расположен скрипт.

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

**Описание**: Путь к корневой директории проекта. Эта переменная инициализируется путем вызова функции `set_project_root`.

```python
__root__ = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""
```