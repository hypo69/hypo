# Модуль header

## Обзор

Модуль `header.py` предназначен для определения корневой директории проекта `hypotez`. Он содержит функцию `set_project_root`, которая ищет корневую директорию, начиная с директории текущего файла и поднимаясь вверх по дереву директорий. Поиск останавливается, когда обнаруживается директория, содержащая один из заданных файлов-маркеров.

## Подорбней

Этот модуль важен для правильной работы путей к файлам и ресурсам внутри проекта. Он гарантирует, что независимо от того, где запускается скрипт, корневая директория проекта будет определена корректно. Это особенно полезно для импорта модулей и доступа к конфигурационным файлам. Функция `set_project_root` добавляет корневую директорию в `sys.path`, что позволяет импортировать модули из любой части проекта.

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

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла, и ищет вверх, останавливаясь на первой директории, содержащей любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Имена файлов или директорий, используемые для идентификации корневой директории проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если она найдена, иначе директория, где расположен скрипт.

**Примеры**:

```python
from pathlib import Path
# Пример использования функции set_project_root
root_path = set_project_root()
print(f"Root directory: {root_path}")