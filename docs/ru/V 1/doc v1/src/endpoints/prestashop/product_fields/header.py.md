# Модуль header

## Обзор

Модуль `header` предназначен для определения корневого каталога проекта `hypotez`. Он включает функцию `set_project_root`, которая ищет корневой каталог на основе наличия определенных файлов-маркеров.

## Подробней

Этот модуль важен для настройки путей в проекте, позволяя скриптам находить необходимые ресурсы и модули независимо от текущего рабочего каталога. Функция `set_project_root` ищет файлы-маркеры, такие как `__root__` или `.git`, чтобы определить корень проекта.

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

**Описание**: Определяет корневой каталог проекта, начиная с каталога текущего файла, и ищет вверх по дереву каталогов, останавливаясь на первом каталоге, содержащем любой из файлов-маркеров.

**Параметры**:

- `marker_files` (tuple): Имена файлов или каталогов, используемых для идентификации корня проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:

- `Path`: Путь к корневому каталогу, если он найден, в противном случае — каталог, где расположен скрипт.

**Примеры**:

```python
from pathlib import Path
# Пример использования функции set_project_root
root_path = set_project_root()
print(f'Root path: {root_path}')
```
```python
from pathlib import Path
# Пример использования функции set_project_root с другими файлами-маркерами
root_path = set_project_root(marker_files=('marker.txt',))
print(f'Root path: {root_path}')
```
```python
from pathlib import Path
# Создаем временный файл-маркер для тестирования
temp_marker = Path('./marker.txt')
temp_marker.touch()
root_path = set_project_root(marker_files=('marker.txt',))
print(f'Root path: {root_path}')
temp_marker.unlink()
```
```python
from pathlib import Path
# Если маркерный файл не найден, возвращается родительский каталог скрипта
root_path = set_project_root(marker_files=('nonexistent_marker.txt',))
print(f'Root path: {root_path}')
```

## Переменные

### `__root__`

**Описание**: Путь к корневому каталогу проекта.

**Тип**: `Path`