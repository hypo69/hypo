# Модуль `header.py`

## Обзор

Этот модуль предоставляет функциональность для определения корневой директории проекта, загрузки настроек из файла `settings.json`, чтения документации из файла `README.MD`, а также определения основных атрибутов проекта, таких как имя, версия, автор и т.д.

## Оглавление

- [Функции](#Функции)
    - [`set_project_root`](#set_project_root)
- [Переменные](#Переменные)
    - [`__root__`](#__root__)
    - [`settings`](#settings)
    - [`doc_str`](#doc_str)
    - [`__project_name__`](#__project_name__)
    - [`__version__`](#__version__)
    - [`__doc__`](#__doc__)
    - [`__details__`](#__details__)
    - [`__author__`](#__author__)
    - [`__copyright__`](#__copyright__)
    - [`__cofee__`](#__cofee__)

## Функции

### `set_project_root`

**Описание**:
Функция `set_project_root` находит корневую директорию проекта, начиная с директории текущего файла. Поиск ведется вверх по дереву каталогов и останавливается при обнаружении одного из маркерных файлов или каталогов.

**Параметры**:
- `marker_files` (tuple, optional): Набор имен файлов или каталогов, которые служат маркерами корневой директории. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории проекта. Если корневая директория не найдена, возвращается путь к директории, в которой расположен текущий файл.

```python
def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.

    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
```

## Переменные

### `__root__`

**Описание**:
`__root__` хранит путь к корневой директории проекта.

```python
__root__ = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""
```

### `settings`

**Описание**:
`settings` - словарь, содержащий настройки проекта, загруженные из файла `settings.json`. Значение `None`, если файл не найден или произошла ошибка при чтении JSON.

```python
settings:dict = None
try:
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = json.load(settings_file)
except (FileNotFoundError, json.JSONDecodeError):
    ...
```

### `doc_str`

**Описание**:
`doc_str` - строка, содержащая документацию проекта, загруженную из файла `README.MD`. Значение `None`, если файл не найден или произошла ошибка при чтении файла.

```python
doc_str:str = None
try:
    with open(gs.path.root / 'src' /  'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError):
    ...
```

### `__project_name__`

**Описание**:
`__project_name__` - имя проекта, извлекаемое из файла настроек. Если в настройках нет имени проекта, используется значение по умолчанию `'hypotez'`.

```python
__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
```

### `__version__`

**Описание**:
`__version__` - версия проекта, извлекаемая из файла настроек. Если в настройках нет версии, используется пустая строка `''`.

```python
__version__: str = settings.get("version", '')  if settings  else ''
```

### `__doc__`

**Описание**:
`__doc__` - строка, содержащая документацию проекта. Значение берется из переменной `doc_str`. Если `doc_str` пустая строка, то `__doc__` так же пустая строка.

```python
__doc__: str = doc_str if doc_str else ''
```

### `__details__`

**Описание**:
`__details__` - строка, содержащая дополнительные сведения о проекте, по умолчанию пустая строка.

```python
__details__: str = ''
```

### `__author__`

**Описание**:
`__author__` - автор проекта, извлекаемый из файла настроек. Если в настройках нет автора, используется пустая строка `''`.

```python
__author__: str = settings.get("author", '')  if settings  else ''
```

### `__copyright__`

**Описание**:
`__copyright__` - информация об авторских правах проекта, извлекаемая из файла настроек. Если в настройках нет информации об авторских правах, используется пустая строка `''`.

```python
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
```

### `__cofee__`

**Описание**:
`__cofee__` - строка, содержащая предложение угостить разработчика чашкой кофе. Значение извлекается из настроек, в противном случае используется значение по умолчанию.

```python
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```