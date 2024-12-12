# Модуль hypotez/src/templates/header.py

## Обзор

Этот модуль содержит функцию `set_project_root`, которая определяет корневой каталог проекта, начиная с текущей директории и поднимаясь вверх по иерархии директорий.  Функция ищет файлы или директории, указанные в качестве маркеров проекта, и возвращает путь к найденному корневому каталогу.  В случае отсутствия маркеров или если корневой каталог не найден, возвращается директория, в которой расположен текущий файл.  Модуль также устанавливает корневой каталог в `sys.path`, что позволяет импортировать модули из этого каталога.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с текущей директории.

**Параметры**:
- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или директорий, используемых для определения корневого каталога проекта. По умолчанию содержит ('pyproject.toml', 'requirements.txt', '.git').


**Возвращает**:
- `Path`: Путь к корневому каталогу проекта, если он найден.  В противном случае возвращает путь к директории текущего файла.

**Вызывает исключения**:
- Нет.

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

## Переменные

### `__root__`

**Описание**: Путь к корневому каталогу проекта, установленный функцией `set_project_root()`.

**Тип**: `Path`


## Импорты

- `sys`
- `json`
- `packaging.version`
- `pathlib`

```
```