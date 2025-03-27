# Модуль `header`

## Обзор

Модуль `header` содержит функции и переменные, необходимые для определения корневой директории проекта `hypotez`. Он предоставляет функцию `set_project_root`, которая находит корневую директорию проекта, начиная с директории текущего файла и двигаясь вверх по дереву директорий.

## Подробней

Этот модуль важен для определения абсолютных путей к файлам и ресурсам проекта, что позволяет избежать проблем с относительными путями при запуске скриптов из разных мест. Функция `set_project_root` ищет маркерные файлы, такие как `__root__` или `.git`, чтобы определить корневую директорию. Переменная `__root__` используется для хранения пути к корневой директории проекта.

## Функции

### `set_project_root`

```python
def set_project_root(marker_files: tuple[str, ...]=('__root__', '.git')) -> Path:
    """
    Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.

    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
    ...
```

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла, и ищет вверх, останавливаясь на первой директории, содержащей любой из маркерных файлов.

**Параметры**:
- `marker_files` (tuple): Имена файлов или каталогов для идентификации корневой директории проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если она найдена, в противном случае - директория, где расположен скрипт.

**Примеры**:

```python
from pathlib import Path
# Пример вызова функции set_project_root
root_path = set_project_root()
print(f'Root path: {root_path}')

# Пример вызова функции set_project_root с указанием других маркерных файлов
root_path = set_project_root(marker_files=('pyproject.toml',))
print(f'Root path: {root_path}')
```

## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта.

**Тип**: `Path`

**Примеры**:

```python
from pathlib import Path
from src.endpoints.kazarinov.scenarios.header import __root__

# Пример использования переменной __root__ для получения пути к корневой директории проекта
root_path = __root__
print(f'Root path: {root_path}')
```