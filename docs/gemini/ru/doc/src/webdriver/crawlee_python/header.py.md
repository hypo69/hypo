# Модуль `header`

## Обзор

Модуль `header.py` предназначен для определения корневого каталога проекта. Он содержит функцию `set_project_root`, которая ищет маркерные файлы (например, `__root__` или `.git`) в родительских каталогах, чтобы определить корень проекта. Это позволяет правильно устанавливать пути к файлам и модулям внутри проекта, независимо от текущего рабочего каталога.

## Подробней

Модуль `header` важен для обеспечения правильной работы скриптов и модулей внутри проекта `hypotez`. Он гарантирует, что все пути к файлам и модулям будут корректно разрешены, даже если скрипт запускается из другого каталога. Функция `set_project_root` ищет специальные файлы-маркеры, чтобы определить корень проекта, и добавляет его в `sys.path`, что позволяет импортировать модули из этого каталога.

## Функции

### `set_project_root`

```python
def set_project_root(marker_files: tuple[str, ...] = ('__root__', '.git')) -> Path:
    """
    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
    # Finds the root directory of the project starting from the current file's directory,
    # searching upwards and stopping at the first directory containing any of the marker files.
    ...
```

**Описание**: Функция для определения корневого каталога проекта.

**Параметры**:
- `marker_files` (tuple): Кортеж с именами файлов или каталогов, которые используются для идентификации корня проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневому каталогу, если он найден. В противном случае возвращает путь к каталогу, где находится скрипт.

**Примеры**:
```python
from pathlib import Path
# Предположим, что в корне проекта есть файл '__root__'
root_path = set_project_root(marker_files=('__root__',))
print(root_path)
```

## Переменные

### `__root__`

```python
"""__root__ (Path): Path to the root directory of the project"""
```

**Описание**: Путь к корневому каталогу проекта. Определяется с помощью функции `set_project_root`.