# Модуль hypotez/src/templates/header.py

## Обзор

Данный модуль содержит функцию `set_project_root`, которая находит корневую директорию проекта, начиная с директории текущего файла. Он также добавляет корневую директорию в `sys.path`, что позволяет импортировать модули из этой директории.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с текущей директории.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, используемых для определения корневой директории проекта. По умолчанию - `('pyproject.toml', 'requirements.txt', '.git')`.


**Возвращает**:

- `Path`: Путь к корневой директории проекта, если она найдена, иначе - путь к директории текущего файла.


**Вызывает исключения**:
- Нет


## Переменные

### `MODE`

**Описание**: Переменная, содержащая режим работы. В данном случае, `'dev'`.


### `__root__`

**Описание**:  Путь к корневой директории проекта, полученный вызовом функции `set_project_root()`.


```
```python
def set_project_root(marker_files=(\'pyproject.toml\', \'requirements.txt\', \'.git\')) -> Path:\n    """\n    Finds the root directory of the project starting from the current file\'s directory,\n    searching upwards and stopping at the first directory containing any of the marker files.\n\n    Args:\n        marker_files (tuple): Filenames or directory names to identify the project root.\n    \n    Returns:\n        Path: Path to the root directory if found, otherwise the directory where the script is located.\n    """\n    __root__:Path\n    current_path:Path = Path(__file__).resolve().parent\n    __root__ = current_path\n    for parent in [current_path] + list(current_path.parents):\n        if any((parent / marker).exists() for marker in marker_files):\n            __root__ = parent\n            break\n    if __root__ not in sys.path:\n        sys.path.insert(0, str(__root__))\n    return __root__\n
```
```