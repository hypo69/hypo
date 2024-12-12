# Модуль `header.py`

## Обзор

Модуль `header.py` предназначен для определения корневого пути проекта и загрузки основных настроек проекта из файла `settings.json`. Он также обеспечивает доступ к информации о проекте, такой как название, версия, автор и документация.

## Оглавление

- [Обзор](#обзор)
- [Константы](#константы)
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
## Константы

### `MODE`
  
**Описание**: Режим работы приложения (в данном случае 'dev').
```python
MODE = 'dev'
```

## Функции

### `set_project_root`

**Описание**: Находит корневой каталог проекта, начиная с каталога текущего файла, и останавливается в первом каталоге, содержащем любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Кортеж имен файлов или каталогов, которые идентифицируют корень проекта. По умолчанию `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:
- `Path`: Путь к корневому каталогу, если он найден, иначе путь к каталогу, где расположен скрипт.

```python
def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
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

**Описание**: Путь к корневому каталогу проекта. Устанавливается функцией `set_project_root`.

```python
__root__: Path
```

### `settings`

**Описание**: Словарь с настройками проекта, загруженный из `settings.json`.

```python
settings: dict
```

### `doc_str`

**Описание**: Строка с документацией проекта, загруженная из `README.MD`.
```python
doc_str: str
```

### `__project_name__`

**Описание**: Название проекта. Загружается из `settings.json`, если он существует, иначе используется значение по умолчанию `hypotez`.

```python
__project_name__: str
```

### `__version__`

**Описание**: Версия проекта. Загружается из `settings.json`, если он существует, иначе используется пустая строка.

```python
__version__: str
```

### `__doc__`

**Описание**: Строка с документацией проекта.

```python
__doc__: str
```

### `__details__`

**Описание**: Детальная информация о проекте. В данном коде остается пустой строкой.

```python
__details__: str
```

### `__author__`

**Описание**: Автор проекта. Загружается из `settings.json`, если он существует, иначе используется пустая строка.

```python
__author__: str
```

### `__copyright__`

**Описание**: Информация об авторских правах проекта. Загружается из `settings.json`, если он существует, иначе используется пустая строка.

```python
__copyright__: str
```

### `__cofee__`

**Описание**: Сообщение с предложением угостить разработчика кофе. Загружается из `settings.json`, если он существует, иначе используется значение по умолчанию.
```python
__cofee__: str