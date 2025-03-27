# Модуль `header`

## Обзор

Модуль `header.py` предназначен для определения корневой директории проекта `hypotez`. Он содержит функцию `set_project_root`, которая ищет корневую директорию, начиная с директории текущего файла и поднимаясь вверх по дереву каталогов. Поиск прекращается при обнаружении каталога, содержащего один из маркеров (файлы или директории).

## Подробней

Этот модуль важен для правильной настройки путей в проекте, особенно когда необходимо импортировать модули из других частей проекта. Функция `set_project_root` гарантирует, что корневая директория проекта добавлена в `sys.path`, что позволяет импортировать модули, используя абсолютные пути относительно корня проекта. Это особенно полезно при работе с большими проектами, где относительные пути могут стать сложными и запутанными.

## Функции

### `set_project_root`

```python
def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """ Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.

    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
    ...
```

**Описание**: Функция `set_project_root` определяет корневую директорию проекта, начиная поиск с текущей директории файла и двигаясь вверх по дереву каталогов. Поиск останавливается, когда обнаруживается каталог, содержащий один из указанных маркеров (файлы или директории).

**Параметры**:
- `marker_files` (tuple): Кортеж имен файлов или директорий, которые используются для идентификации корневой директории проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Объект `Path`, представляющий путь к корневой директории проекта. Если корневая директория не найдена, возвращается директория, в которой расположен скрипт.

**Примеры**:

```python
from pathlib import Path

# Пример вызова функции set_project_root
root_path = set_project_root()
print(f"Корневая директория проекта: {root_path}")

# Пример вызова функции set_project_root с пользовательскими маркерами
root_path = set_project_root(marker_files=('my_marker_file',))
print(f"Корневая директория проекта: {root_path}")