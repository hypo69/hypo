# Модуль header

## Обзор

Модуль `header.py` предназначен для определения корневой директории проекта, загрузки настроек из файла `settings.json` и чтения содержимого файла `README.MD`. Он также определяет основные метаданные проекта, такие как имя, версия, авторские права и т.д.

## Подробней

Модуль выполняет следующие задачи:

-   Определение корневой директории проекта на основе наличия файлов-маркеров (`__root__`, `.git`).
-   Загрузка настроек проекта из файла `settings.json`.
-   Чтение документации проекта из файла `README.MD`.
-   Определение основных метаданных проекта (имя, версия, автор и т.д.) на основе загруженных настроек.

Этот модуль важен для инициализации проекта и доступа к его основным параметрам и документации.

## Функции

### `set_project_root`

```python
def set_project_root(marker_files: tuple[str] = ('__root__', '.git')) -> Path:
    """
    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
```

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла, и поднимаясь вверх, пока не найдет директорию, содержащую один из файлов-маркеров.

**Параметры**:

-   `marker_files` (tuple[str]): Кортеж имен файлов или директорий, используемых для определения корневой директории проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:

-   `Path`: Путь к корневой директории, если она найдена, иначе директория, где расположен скрипт.

**Примеры**:

```python
from pathlib import Path
root_path = set_project_root()
print(root_path)