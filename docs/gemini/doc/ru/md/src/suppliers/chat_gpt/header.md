# Модуль `hypotez/src/suppliers/chat_gpt/header.py`

## Обзор

Этот модуль содержит функции для определения корневой директории проекта, загрузки настроек из файла `settings.json` и получения документации из файла `README.MD`.  Он устанавливает переменные, хранящие информацию о проекте, такие как имя, версия, документация, автор и прочее.

## Оглавление

- [Функции](#функции)
    - [`set_project_root`](#set_project_root)


## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла. Поиск происходит вверх по иерархии директорий, пока не найдена директория, содержащая один из файлов-маркеров.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, используемых для определения корневой директории проекта. По умолчанию содержит `('pyproject.toml', 'requirements.txt', '.git')`.


**Возвращает**:

- `Path`: Путь к корневой директории проекта, если она найдена. В противном случае возвращает директорию, где находится текущий скрипт.


**Вызывает исключения**:

- Нет


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

**Описание**:  Путь к корневой директории проекта.  Инициализируется функцией `set_project_root()`.

**Тип**: `Path`


### `settings`

**Описание**: Словарь с настройками проекта, загруженный из файла `settings.json`.

**Тип**: `dict`


### `doc_str`

**Описание**: Строка с текстом документации из файла `README.MD`.

**Тип**: `str`


### `__project_name__`

**Описание**: Имя проекта, взятое из настроек (`settings.json`). По умолчанию 'hypotez'.

**Тип**: `str`


### `__version__`

**Описание**: Версия проекта, взятая из настроек (`settings.json`). По умолчанию пустая строка.

**Тип**: `str`


### `__doc__`

**Описание**: Документация проекта, взятая из `README.MD`. По умолчанию пустая строка.

**Тип**: `str`


### `__details__`

**Описание**: Дополнительные детали проекта. По умолчанию пустая строка.

**Тип**: `str`


### `__author__`

**Описание**: Автор проекта, взятый из настроек (`settings.json`). По умолчанию пустая строка.

**Тип**: `str`


### `__copyright__`

**Описание**: Авторские права, взятые из настроек (`settings.json`). По умолчанию пустая строка.

**Тип**: `str`


### `__cofee__`

**Описание**: Ссылка на возможность поддержать разработчиков.

**Тип**: `str`


```