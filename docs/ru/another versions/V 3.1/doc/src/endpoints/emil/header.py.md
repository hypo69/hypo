# Модуль `header`

## Обзор

Модуль `header` содержит функции и переменные, связанные с определением корневого каталога проекта. Это необходимо для правильной работы с путями и импортами внутри проекта `hypotez`.

## Подробней

Основная задача этого модуля - определить корневой каталог проекта, чтобы обеспечить консистентность путей и упростить импорт модулей. Функция `set_project_root` и переменная `__root__` играют ключевую роль в этой задаче. `set_project_root` ищет маркерные файлы, чтобы определить корень проекта, а `__root__` хранит путь к этому корню.

## Функции

### `set_project_root`

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
```

**Описание**: Функция `set_project_root` определяет корневой каталог проекта, начиная с текущего файла и двигаясь вверх по директориям, пока не найдет одну из маркеров.

**Параметры**:
- `marker_files` (tuple): Список файлов или директорий, используемых для идентификации корневого каталога проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневому каталогу проекта. Если корневой каталог не найден, возвращает директорию, где расположен скрипт.

**Примеры**:

```python
from pathlib import Path
# Пример вызова функции set_project_root без параметров
root_path = set_project_root()
print(f'Root path: {root_path}')

# Пример вызова функции set_project_root с указанием маркеров
root_path = set_project_root(marker_files=('marker.txt',))
print(f'Root path: {root_path}')
```

## Переменные

### `__root__`

**Описание**: Переменная `__root__` хранит путь к корневому каталогу проекта, определенному функцией `set_project_root`.

**Тип**: `Path`

**Примеры**:

```python
from pathlib import Path
from src.endpoints.emil.header import __root__

# Пример использования переменной __root__ для доступа к файлу в корневом каталоге
file_path = __root__ / 'config.ini'
print(f'File path: {file_path}')