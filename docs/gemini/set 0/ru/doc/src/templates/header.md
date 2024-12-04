# Модуль `hypotez/src/templates/header.py`

## Обзор

Модуль `header.py` содержит функцию `set_project_root`, которая определяет корневую директорию проекта, начиная с текущей директории и двигаясь вверх по дереву директорий.  Функция ищет в родительских директориях файлы и папки, указанные в качестве маркеров (например, `pyproject.toml`, `requirements.txt`, `.git`). Если корневая директория найдена, она добавляется в `sys.path`.

## Функции

### `set_project_root`

**Описание**: Определяет корневую директорию проекта.

**Параметры**:

- `marker_files` (tuple): Кортеж из строк, представляющих имена файлов или папок, которые будут использоваться для поиска корневой директории. По умолчанию: `('pyproject.toml', 'requirements.txt', '.git')`.


**Возвращает**:

- `Path`: Объект `Path` представляющий корневую директорию проекта.  Возвращает директорию текущего файла, если корневая директория не найдена.

**Использует**:

- `Path`: Для работы с путями к файлам и папкам.
- `sys.path`: Для добавления пути к корневой директории проекта в переменную `sys.path`.


```python
def set_project_root(marker_files=(\'pyproject.toml\', \'requirements.txt\', \'.git\')) -> Path:\n    """\n    Finds the root directory of the project starting from the current file\'s directory,\n    searching upwards and stopping at the first directory containing any of the marker files.\n\n    Args:\n        marker_files (tuple): Filenames or directory names to identify the project root.\n    \n    Returns:\n        Path: Path to the root directory if found, otherwise the directory where the script is located.\n    """\n    __root__:Path\n    current_path:Path = Path(__file__).resolve().parent\n    __root__ = current_path\n    for parent in [current_path] + list(current_path.parents):\n        if any((parent / marker).exists() for marker in marker_files):\n            __root__ = parent\n            break\n    if __root__ not in sys.path:\n        sys.path.insert(0, str(__root__))\n    return __root__
```


## Переменные

### `__root__`

**Описание**: Переменная, содержащая корневую директорию проекта.


```python
__root__ = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""
```