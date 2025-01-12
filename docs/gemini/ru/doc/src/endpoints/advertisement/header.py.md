# Модуль `header.py`

## Обзор

Модуль `header.py` отвечает за настройку и конфигурацию проекта, включая определение корневой директории, загрузку настроек из `settings.json` и документации из `README.md`, а также определение основных переменных проекта.

## Оглавление

- [Функции](#функции)
  - [`set_project_root`](#set_project_root)
- [Переменные](#переменные)
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
Находит корневой каталог проекта, начиная с каталога текущего файла, поднимаясь вверх и останавливаясь на первом каталоге, содержащем любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple, optional): Кортеж имен файлов или каталогов, определяющих корень проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневому каталогу, если он найден, иначе - каталог, где находится скрипт.

### `set_project_root`

```python
def set_project_root(marker_files: tuple = ('__root__','.git')) -> Path:
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
```

### `settings`

**Описание**:
Словарь с настройками проекта, загруженный из файла `settings.json`.

```python
settings:dict = None
try:
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = json.load(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as ex:
    ...
```

### `doc_str`

**Описание**:
Строка, содержащая документацию проекта, загруженную из файла `README.md`.

```python
doc_str:str = None
try:
    with open(gs.path.root / 'src' /  'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as ex:
    ...
```

### `__project_name__`

**Описание**:
Название проекта, взятое из `settings.json` или `'hypotez'` по умолчанию.

```python
__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
```

### `__version__`

**Описание**:
Версия проекта, взятая из `settings.json` или `''` по умолчанию.

```python
__version__: str = settings.get("version", '')  if settings  else ''
```

### `__doc__`

**Описание**:
Документация проекта, загруженная из `README.md` или `''` по умолчанию.

```python
__doc__: str = doc_str if doc_str else ''
```

### `__details__`

**Описание**:
Детальная информация о проекте, всегда инициализируется пустой строкой.

```python
__details__: str = ''
```

### `__author__`

**Описание**:
Автор проекта, взятый из `settings.json` или `''` по умолчанию.

```python
__author__: str = settings.get("author", '')  if settings  else ''
```

### `__copyright__`

**Описание**:
Информация об авторских правах проекта, взятая из `settings.json` или `''` по умолчанию.

```python
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
```

### `__cofee__`

**Описание**:
Сообщение с предложением поддержать разработчика чашечкой кофе, взятое из `settings.json` или строка по умолчанию.

```python
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```