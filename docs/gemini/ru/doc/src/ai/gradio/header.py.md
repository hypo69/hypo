# Модуль `header`

## Обзор

Модуль `header.py` предназначен для настройки и инициализации основных параметров проекта, таких как корневой путь, конфигурация из `config.json`, документация из `README.md`, а также основные сведения о проекте, такие как имя, версия, автор и авторские права.

## Содержание

- [Обзор](#обзор)
- [Функции](#функции)
  - [`set_project_root`](#set_project_root)
- [Переменные](#переменные)
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

**Описание**:
Находит корневой каталог проекта, начиная с каталога текущего файла, поднимаясь вверх и останавливаясь в первом каталоге, содержащем любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Кортеж имен файлов или каталогов для идентификации корня проекта.

**Возвращает**:
- `Path`: Путь к корневому каталогу, если он найден, в противном случае каталог, где расположен скрипт.

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
    ...
```
## Переменные

### `__root__`

**Описание**:
Путь к корневому каталогу проекта.

```python
__root__:Path
```
### `config`
**Описание**: Словарь с конфигурацией проекта, загруженный из файла `config.json`.

```python
config:dict
```

### `doc_str`
**Описание**: Строка документации проекта, загруженная из файла `README.md`.

```python
doc_str:str
```
### `__project_name__`

**Описание**: Название проекта, полученное из конфигурации или "hypotez" по умолчанию.

```python
__project_name__: str
```
### `__version__`

**Описание**: Версия проекта, полученная из конфигурации или пустая строка по умолчанию.

```python
__version__: str
```

### `__doc__`

**Описание**: Документация проекта, полученная из файла README.md или пустая строка по умолчанию.

```python
__doc__: str
```
### `__details__`

**Описание**: Детали проекта, по умолчанию пустая строка.

```python
__details__: str
```
### `__author__`

**Описание**: Автор проекта, полученный из конфигурации или пустая строка по умолчанию.

```python
__author__: str
```
### `__copyright__`

**Описание**: Информация об авторских правах, полученная из конфигурации или пустая строка по умолчанию.

```python
__copyright__: str
```
### `__cofee__`

**Описание**: Строка с призывом угостить разработчика кофе.

```python
__cofee__: str
```