# Модуль `header.py`

## Обзор

Модуль `header.py` содержит общие настройки и константы для проекта, включая путь к корневой директории, настройки из `settings.json`, версию проекта и документацию из `README.md`. Также предоставляет функцию для определения корневой директории проекта.

## Оглавление

1.  [Функции](#функции)
    -   [`set_project_root`](#set_project_root)
2.  [Глобальные переменные](#глобальные-переменные)
    -   [`__root__`](#__root__)
    -   [`settings`](#settings)
    -   [`doc_str`](#doc_str)
    -   [`__project_name__`](#__project_name__)
    -   [`__version__`](#__version__)
    -   [`__doc__`](#__doc__)
    -   [`__details__`](#__details__)
    -   [`__author__`](#__author__)
    -   [`__copyright__`](#__copyright__)
    -   [`__cofee__`](#__cofee__)

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла, поднимаясь вверх и останавливаясь на первой директории, содержащей любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple, optional): Имена файлов или директорий для идентификации корневой директории проекта. По умолчанию `('__root__','.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если найдена, иначе директория, где находится скрипт.

```python
def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Args:
        marker_files (tuple, optional): Filenames or directory names to identify the project root. Defaults to ('__root__', '.git').
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
```
## Глобальные переменные
### `__root__`
**Описание**: Путь к корневой директории проекта. Определяется функцией `set_project_root`.
```python
__root__: Path
```

### `settings`
**Описание**: Словарь с настройками проекта, загруженный из файла `settings.json`. Может быть `None`, если файл не найден или произошла ошибка при парсинге.

```python
settings: dict = None
```
### `doc_str`
**Описание**: Строка с содержимым документации проекта, загруженной из файла `README.md`. Может быть `None`, если файл не найден или произошла ошибка при чтении.
```python
doc_str: str = None
```

### `__project_name__`
**Описание**: Название проекта. Загружается из `settings.json`, если доступно, иначе устанавливается значение `'hypotez'`.
```python
__project_name__: str
```

### `__version__`
**Описание**: Версия проекта. Загружается из `settings.json`, если доступна, иначе устанавливается значение `''`.
```python
__version__: str
```

### `__doc__`
**Описание**: Документация проекта, загруженная из файла `README.md`.
```python
__doc__: str
```

### `__details__`
**Описание**:  Дополнительная информация о проекте, пока не определена.
```python
__details__: str
```
### `__author__`
**Описание**: Автор проекта. Загружается из `settings.json`, если доступно, иначе устанавливается значение `''`.
```python
__author__: str
```

### `__copyright__`
**Описание**: Копирайт проекта. Загружается из `settings.json`, если доступно, иначе устанавливается значение `''`.
```python
__copyright__: str
```
### `__cofee__`
**Описание**: Сообщение с предложением угостить разработчика кофе. Загружается из `settings.json`, если доступно, иначе устанавливается значение "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69".
```python
__cofee__: str