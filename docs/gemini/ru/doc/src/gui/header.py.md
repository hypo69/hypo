# Модуль `header.py`

## Обзор

Модуль `header.py` предназначен для определения корневого пути проекта и загрузки основных настроек. Он обеспечивает корректную работу импортов и предоставляет доступ к метаданным проекта, таким как имя, версия и автор.

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
Находит корневой каталог проекта, начиная с текущего каталога файла, выполняя поиск вверх и останавливаясь в первом каталоге, содержащем любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Кортеж имен файлов или каталогов для идентификации корня проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневому каталогу, если он найден, иначе каталог, где расположен скрипт.

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
Путь к корневому каталогу проекта.

```python
__root__ = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""
```

### `settings`

**Описание**:
Словарь с настройками проекта, загруженными из файла `settings.json`.

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
Строка с содержимым файла `README.MD`.

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
Имя проекта, полученное из настроек или по умолчанию `hypotez`.

```python
__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
```

### `__version__`

**Описание**:
Версия проекта, полученная из настроек или пустая строка.

```python
__version__: str = settings.get("version", '')  if settings  else ''
```
### `__doc__`

**Описание**:
Строка документации проекта, считанная из `README.MD` файла.

```python
__doc__: str = doc_str if doc_str else ''
```
### `__details__`

**Описание**:
Строка деталей проекта. В данный момент пустая.

```python
__details__: str = ''
```
### `__author__`

**Описание**:
Автор проекта, полученный из настроек или пустая строка.

```python
__author__: str = settings.get("author", '')  if settings  else ''
```
### `__copyright__`

**Описание**:
Информация об авторских правах, полученная из настроек или пустая строка.

```python
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
```

### `__cofee__`

**Описание**:
Строка с предложением поддержать разработчика, полученная из настроек или стандартная ссылка.

```python
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"