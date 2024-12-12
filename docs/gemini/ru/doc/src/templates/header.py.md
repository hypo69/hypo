# Модуль `header.py`

## Обзор

Модуль `header.py` предназначен для определения корневой директории проекта и настройки пути для импорта модулей, а также для определения режима работы приложения (`dev`).

## Оглавление

1. [Обзор](#обзор)
2. [Переменные](#переменные)
3. [Функции](#функции)
    - [`set_project_root`](#set_project_root)

## Переменные

### `MODE`

**Описание**: Определяет режим работы приложения. По умолчанию установлено значение `'dev'`.
- `MODE` (str): `'dev'`

### `__root__`

**Описание**: Путь к корневой директории проекта. Определяется функцией `set_project_root` и используется для добавления корневой директории в `sys.path`.
- `__root__` (Path): Путь к корневой директории проекта.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла, и поднимаясь вверх по дереву директорий. Поиск останавливается на первой директории, содержащей хотя бы один из указанных файлов-маркеров.

**Параметры**:
- `marker_files` (tuple, optional): Кортеж с именами файлов или директорий, которые используются для идентификации корневой директории. По умолчанию: `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если она найдена. В противном случае возвращается директория, где расположен скрипт.

**Пример**:

```python
from pathlib import Path
def set_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
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