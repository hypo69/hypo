# Модуль hypotez/src/utils/ai/header.py

## Обзор

Этот модуль предоставляет функции для работы с заголовками.


## Функции

### `set_project_root`

**Описание**: Находит корневой каталог проекта, начиная с текущего каталога и двигаясь вверх по иерархии каталогов. Останавливается на первом каталоге, содержащем файлы-маркеры (например, `pyproject.toml`, `requirements.txt`, `.git`). Если корневой каталог не найден, возвращает каталог, где расположен данный скрипт. Добавляет корневой каталог в `sys.path`.

**Параметры**:

- `marker_files` (tuple, опционально): Кортеж имен файлов или каталогов, которые используются для определения корневого каталога проекта. По умолчанию: (`'pyproject.toml'`, `'requirements.txt'`, `.git`).

**Возвращает**:

- `Path`: Путь к корневому каталогу проекта, если он найден, в противном случае путь к каталогу, где расположен скрипт.

**Вызывает исключения**:

- Не вызывает исключений.


```
```python
def set_project_root(marker_files=(\'pyproject.toml\', \'requirements.txt\', \'.git\')) -> Path:
    """
    Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.

    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__
```
```
```
```markdown
## Переменные

### `__root__`

**Описание**: Путь к корневому каталогу проекта. Присваивается значение после вызова функции `set_project_root()`.

**Тип**: `Path`

```
```python
# Get the root directory of the project
__root__ = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""
```
```

```markdown
**Примечание:**  Документация для остальных частей кода (например, импорты, обработка исключений) должна быть дополнена аналогичным образом.  В данном примере приведены только основные части, требующие документации,  в соответствии с предоставленной инструкцией.