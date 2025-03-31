# Модуль `src.suppliers.visualdg.header`

## Обзор

Модуль `header.py` предназначен для определения корневой директории проекта, загрузки настроек из `settings.json`, чтения документации из `README.MD` и определения основных метаданных проекта.

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

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла, и останавливается на первой директории, содержащей маркерные файлы.

**Параметры**:
- `marker_files` (tuple): Кортеж имен файлов или каталогов для идентификации корня проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если она найдена, иначе директория, где находится скрипт.

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

**Описание**: Путь к корневой директории проекта. Инициализируется функцией `set_project_root`.

### `settings`

**Описание**: Словарь с настройками проекта, загруженными из файла `settings.json`. Может быть `None`, если файл не найден или произошла ошибка декодирования JSON.

### `doc_str`

**Описание**: Строка, содержащая документацию проекта, прочитанную из файла `README.MD`. Может быть `None`, если файл не найден или произошла ошибка.

### `__project_name__`

**Описание**: Название проекта. Загружается из `settings.json` или используется значение по умолчанию `'hypotez'`.

### `__version__`

**Описание**: Версия проекта. Загружается из `settings.json` или используется значение по умолчанию `''`.

### `__doc__`

**Описание**: Строка, содержащая документацию проекта, загруженную из файла `README.MD`, или пустая строка `''`, если файл не найден.

### `__details__`

**Описание**: Пустая строка. Предназначена для дополнительных сведений о проекте, но в данный момент не используется.

### `__author__`

**Описание**: Автор проекта. Загружается из `settings.json` или используется значение по умолчанию `''`.

### `__copyright__`

**Описание**: Информация об авторских правах проекта. Загружается из `settings.json` или используется значение по умолчанию `''`.

### `__cofee__`

**Описание**: Строка с предложением поддержать разработчика чашечкой кофе. Загружается из `settings.json` или используется значение по умолчанию.

```python
__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
__version__: str = settings.get("version", '')  if settings  else ''
__doc__: str = doc_str if doc_str else ''
__details__: str = ''
__author__: str = settings.get("author", '')  if settings  else ''
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"