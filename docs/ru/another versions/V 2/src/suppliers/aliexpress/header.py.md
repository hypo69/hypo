# Модуль `header.py`

## Обзор

Модуль `header.py` предназначен для инициализации и настройки окружения проекта. Он определяет корневую директорию проекта, добавляет её в `sys.path` и загружает настройки из файла `settings.json`.

## Содержание

- [Функции](#Функции)
    - [`set_project_root`](#set_project_root)

- [Переменные](#Переменные)
    - [`__root__`](#__root__)
    - [`settings`](#settings)


## Функции

### `set_project_root`

**Описание**:
Функция `set_project_root` определяет корневую директорию проекта, начиная с директории текущего файла, и добавляет её в `sys.path`. Поиск ведётся вверх по дереву каталогов до тех пор, пока не будет найден каталог, содержащий хотя бы один из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Кортеж с именами файлов или каталогов, которые используются для идентификации корневой директории проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Объект `Path` к корневой директории проекта, если она найдена. В противном случае возвращается директория, где находится скрипт.

```python
def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
```

## Переменные

### `__root__`

**Описание**:
Глобальная переменная `__root__` хранит объект `Path` к корневой директории проекта. Значение переменной устанавливается при вызове функции `set_project_root`.

### `settings`

**Описание**:
Глобальная переменная `settings` хранит словарь с настройками, загруженными из файла `settings.json`. Если файл не найден или имеет неверный формат, переменная будет `None`.

```python
settings:dict = None
try:
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = json.load(settings_file)
except (FileNotFoundError, json.JSONDecodeError):
    ...
```