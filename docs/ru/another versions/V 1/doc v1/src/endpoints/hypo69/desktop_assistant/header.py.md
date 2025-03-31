# Модуль header

## Обзор

Модуль `header.py` предназначен для определения корневой директории проекта `hypotez`. Он содержит функцию `set_project_root`, которая осуществляет поиск корневой директории на основе заданных файлов-маркеров.

## Подорбней

Основная задача модуля заключается в автоматическом определении корневой директории проекта, что позволяет упростить импорт модулей и работу с путями файлов относительно корня проекта. Функция `set_project_root` ищет директорию, содержащую определенные файлы-маркеры (например, `__root__` или `.git`), начиная с текущей директории файла и двигаясь вверх по дереву директорий. Это обеспечивает гибкость и независимость от текущего рабочего каталога при запуске скриптов.

## Функции

### `set_project_root`

```python
def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
```

**Описание**: Функция `set_project_root` определяет корневую директорию проекта путем поиска файлов-маркеров в родительских директориях.

**Параметры**:
- `marker_files` (tuple): Кортеж имен файлов или директорий, которые используются для определения корневой директории проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории проекта, если она найдена. В противном случае возвращает директорию, где расположен скрипт.

**Примеры**:

```python
from pathlib import Path
import sys

# Пример использования функции set_project_root
root_path = set_project_root()
print(f"Root path: {root_path}")

# Добавление корневой директории в sys.path, если ее там нет
if root_path not in sys.path:
    sys.path.insert(0, str(root_path))
    print(f"Added {root_path} to sys.path")
else:
    print(f"{root_path} already in sys.path")
```
```python
# Get the root directory of the project
__root__: Path = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""