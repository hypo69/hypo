# Модуль `header`

## Обзор

Модуль `header` предназначен для определения корневой директории проекта `hypotez`. Он включает функцию `set_project_root`, которая ищет корневую директорию, начиная с текущей директории файла, и останавливается на первой директории, содержащей один из указанных файлов-маркеров.

## Подробней

Модуль `header` важен для правильной настройки путей и импорта модулей внутри проекта `hypotez`. Функция `set_project_root` позволяет динамически определять корневую директорию проекта, что упрощает запуск и отладку скриптов из разных мест в файловой системе.

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

**Описание**: Определяет корневую директорию проекта, начиная поиск от директории текущего файла и продвигаясь вверх до тех пор, пока не будет найдена директория, содержащая один из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Кортеж с именами файлов или директорий, используемых для идентификации корневой директории проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если она найдена. В противном случае возвращает директорию, в которой расположен скрипт.

**Примеры**:

```python
from pathlib import Path
# Пример вызова функции set_project_root
root_path: Path = set_project_root()
print(f"Root path: {root_path}")