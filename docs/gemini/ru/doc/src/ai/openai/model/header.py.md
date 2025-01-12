# Модуль `header.py`

## Обзор

Модуль `header.py` предназначен для определения корневого пути к проекту и загрузки основных настроек из `settings.json`. Все импорты строятся относительно этого корневого пути. Также модуль предоставляет информацию о проекте, такую как имя, версию, авторство, копирайт и прочее, загружая их из файла `settings.json` и `README.md`.

## Содержание

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
Находит корневой каталог проекта, начиная с каталога текущего файла, перемещаясь вверх и останавливаясь на первом каталоге, содержащем любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple, optional): Имена файлов или каталогов для идентификации корня проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневому каталогу, если он найден, в противном случае — каталог, где находится скрипт.

### `set_project_root`

```python
def set_project_root(marker_files:tuple =('__root__','.git')) -> Path:
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
`Path` к корневому каталогу проекта. Инициализируется результатом функции `set_project_root`.

### `settings`

**Описание**:
`dict`, содержащий настройки проекта, загруженные из файла `settings.json`.

### `doc_str`

**Описание**:
`str`, содержащий текст документации проекта, загруженный из файла `README.MD`.

### `__project_name__`

**Описание**:
`str`, имя проекта. По умолчанию `hypotez`, если значение не найдено в `settings.json`.

### `__version__`

**Описание**:
`str`, версия проекта. По умолчанию пустая строка, если значение не найдено в `settings.json`.

### `__doc__`

**Описание**:
`str`, текст документации из `README.md` . Если файл не найден, то `''`

### `__details__`

**Описание**:
`str`, дополнительные детали проекта. По умолчанию пустая строка.

### `__author__`

**Описание**:
`str`, автор проекта. По умолчанию пустая строка, если значение не найдено в `settings.json`.

### `__copyright__`

**Описание**:
`str`, информация о копирайте проекта. По умолчанию пустая строка, если значение не найдено в `settings.json`.

### `__cofee__`

**Описание**:
`str`, строка с предложением угостить разработчика кофе. Значение берётся из `settings.json`, если есть, иначе используется значение по умолчанию.