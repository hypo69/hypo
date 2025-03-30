# Название модуля

## Обзор

Модуль `header` определяет корневой путь к проекту. Все импорты строятся относительно этого пути.

## Подробней

Модуль `header` используется для определения корневой директории проекта, что позволяет упростить импорты и сделать структуру проекта более понятной. Функция `set_project_root` ищет маркерные файлы (например, `__root__` или `.git`) в директориях, начиная с текущей, и устанавливает корневую директорию проекта. Если маркерные файлы не найдены, корневой директорией считается директория, где расположен скрипт. Найденная корневая директория добавляется в `sys.path`, чтобы обеспечить правильную работу импортов.

## Классы

В данном модуле классы отсутствуют.

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
```

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла, и ищет вверх по дереву директорий, останавливаясь на первой директории, содержащей любой из маркерных файлов.

**Параметры**:
- `marker_files` (tuple): Имена файлов или директорий, используемые для идентификации корневой директории проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если она найдена, в противном случае — директория, где расположен скрипт.

**Примеры**:

```python
from pathlib import Path
# Пример использования функции set_project_root
root_path = set_project_root()
print(f"Root path: {root_path}")

# Пример с указанием альтернативных маркерных файлов
root_path_alt = set_project_root(marker_files=('marker.txt',))
print(f"Root path with alternative markers: {root_path_alt}")
```