# Модуль `header.py`

## Обзор

Модуль `header.py` предназначен для определения корневой директории проекта и добавления её в `sys.path`. Это позволяет корректно импортировать модули из различных частей проекта.

## Оглавление

1. [Функции](#функции)
    - [`set_project_root`](#set_project_root)

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла и поднимаясь вверх, останавливаясь на первой директории, содержащей любой из указанных файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Кортеж с именами файлов или директорий для идентификации корневой директории проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если она найдена. Если корневая директория не найдена, возвращает директорию, в которой расположен скрипт.

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