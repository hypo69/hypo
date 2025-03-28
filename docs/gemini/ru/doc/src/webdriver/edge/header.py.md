# Модуль `header.py`

## Обзор

Модуль `header.py` предназначен для определения корневой директории проекта. Это необходимо для правильной работы с путями к файлам и модулям внутри проекта, особенно при его запуске из разных мест. Модуль использует файлы-маркеры (`__root__`, `.git`) для определения корневой директории.

## Подорбней

Модуль содержит функцию `set_project_root`, которая ищет корневую директорию проекта, начиная с директории текущего файла и двигаясь вверх по дереву директорий. Поиск прекращается, когда найдена директория, содержащая один из файлов-маркеров. Если корневая директория не найдена, то используется директория, в которой расположен скрипт. После определения корневой директории, она добавляется в `sys.path`, чтобы обеспечить возможность импорта модулей из этой директории.

## Функции

### `set_project_root`

```python
def set_project_root(marker_files: tuple[str, ...]=('__root__', '.git')) -> Path:
    """
    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
```

**Описание**:
Функция `set_project_root` ищет корневую директорию проекта, начиная с директории текущего файла и двигаясь вверх по дереву директорий. Поиск прекращается, когда найдена директория, содержащая один из файлов-маркеров. Если корневая директория не найдена, то используется директория, в которой расположен скрипт. После определения корневой директории, она добавляется в `sys.path`, чтобы обеспечить возможность импорта модулей из этой директории.

**Параметры**:

- `marker_files` (tuple[str, ...], optional): Кортеж имен файлов или директорий, используемых для определения корневой директории проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:

- `Path`: Объект `Path`, представляющий путь к корневой директории проекта. Если корневая директория не найдена, возвращается путь к директории, в которой расположен скрипт.

**Примеры**:

```python
from pathlib import Path
# Пример вызова функции set_project_root
root_path = set_project_root()
print(f'Root path: {root_path}')
```

## Переменные

### `__root__`

```python
"""__root__ (Path): Path to the root directory of the project"""
```

**Описание**:
`__root__` - это переменная, хранящая путь к корневой директории проекта. Она инициализируется путем вызова функции `set_project_root`.

```python
from pathlib import Path
# Get the root directory of the project
__root__: Path = set_project_root()
print(f'Root path: {__root__}')