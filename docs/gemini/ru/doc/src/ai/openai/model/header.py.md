# Модуль `src.logger.header`

## Обзор

Модуль `src.logger.header` предназначен для определения корневого пути проекта. Все импорты в проекте строятся относительно этого пути. Также модуль загружает основные настройки проекта из `settings.json` и документацию из `README.MD`.

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
Находит корневую директорию проекта, начиная с директории текущего файла,
двигаясь вверх и останавливаясь на первой директории, содержащей один из маркеров.

**Параметры**:
- `marker_files` (tuple): Кортеж имен файлов или директорий, используемых для идентификации корня проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если она найдена, иначе - путь к директории, где расположен скрипт.

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
`Path` к корневой директории проекта.

### `settings`

**Описание**:
Словарь, содержащий настройки проекта, загруженные из `settings.json`. Если файл не найден или не удается декодировать JSON, переменная остается `None`.

### `doc_str`

**Описание**:
Строка, содержащая содержимое файла `README.MD`. Если файл не найден или не удается прочитать, переменная остается `None`.

### `__project_name__`

**Описание**:
Строка, содержащая имя проекта, загруженное из `settings.json` или `'hypotez'` по умолчанию.

### `__version__`

**Описание**:
Строка, содержащая версию проекта, загруженную из `settings.json` или пустую строку по умолчанию.

### `__doc__`

**Описание**:
Строка, содержащая документацию проекта, загруженную из `README.MD`.

### `__details__`

**Описание**:
Строка, содержащая детали проекта, инициализирована пустой строкой.

### `__author__`

**Описание**:
Строка, содержащая автора проекта, загруженная из `settings.json` или пустую строку по умолчанию.

### `__copyright__`

**Описание**:
Строка, содержащая информацию о копирайте проекта, загруженная из `settings.json` или пустую строку по умолчанию.

### `__cofee__`

**Описание**:
Строка, содержащая сообщение с предложением угостить разработчика кофе, загруженная из `settings.json` или сообщение по умолчанию.

```python
__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
__version__: str = settings.get("version", '')  if settings  else ''
__doc__: str = doc_str if doc_str else ''
__details__: str = ''
__author__: str = settings.get("author", '')  if settings  else ''
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"