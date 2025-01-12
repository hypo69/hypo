# Модуль `header.py`

## Обзор

Модуль `header.py` предназначен для настройки и управления базовыми параметрами проекта, включая поиск корневой директории, загрузку конфигурации из `config.json`, чтение документации из `README.MD`, а также определение основных переменных проекта, таких как имя, версия, автор и т.д.

## Содержание

- [Функции](#Функции)
  - [`set_project_root`](#set_project_root)
- [Глобальные переменные](#Глобальные-переменные)
  - [`__root__`](#__root__)
  - [`config`](#config)
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

**Описание**: Находит корневой каталог проекта, начиная с каталога текущего файла, ища вверх и останавливаясь на первом каталоге, содержащем любой из маркерных файлов.

**Параметры**:
- `marker_files` (tuple, optional): Кортеж имен файлов или каталогов для идентификации корня проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневому каталогу, если найден, в противном случае - каталог, в котором находится скрипт.

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

## Глобальные переменные

### `__root__`

**Описание**: Путь к корневой директории проекта, полученный с помощью функции `set_project_root`.
```python
__root__: Path
```

### `config`

**Описание**: Словарь, содержащий конфигурационные параметры проекта, загруженные из файла `config.json`. Может быть `None`, если файл не найден или возникла ошибка при его чтении.

```python
config: dict = None
```

### `doc_str`

**Описание**: Строка, содержащая документацию проекта, загруженную из файла `README.MD`. Может быть `None`, если файл не найден или возникла ошибка при его чтении.

```python
doc_str: str = None
```
### `__project_name__`

**Описание**: Имя проекта, загруженное из конфигурации или по умолчанию `'hypotez'`.

```python
__project_name__ = config.get("project_name", 'hypotez') if config else 'hypotez'
```

### `__version__`

**Описание**: Версия проекта, загруженная из конфигурации или пустая строка `''`.

```python
__version__: str = config.get("version", '') if config else ''
```

### `__doc__`

**Описание**: Документация проекта, загруженная из `README.MD`.

```python
__doc__: str = doc_str if doc_str else ''
```
### `__details__`

**Описание**: Детали проекта, в данном случае пустая строка.

```python
__details__: str = ''
```
### `__author__`

**Описание**: Автор проекта, загруженный из конфигурации или пустая строка `''`.

```python
__author__: str = config.get("author", '') if config else ''
```
### `__copyright__`

**Описание**: Информация об авторских правах проекта, загруженная из конфигурации или пустая строка `''`.

```python
__copyright__: str = config.get("copyrihgnt", '') if config else ''
```

### `__cofee__`

**Описание**: Строка с призывом угостить разработчика чашечкой кофе, загруженная из конфигурации или строка по умолчанию.

```python
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"