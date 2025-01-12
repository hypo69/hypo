# Модуль `src.logger.header`

## Обзор

Модуль `src.logger.header` определяет корневой путь к проекту и обеспечивает загрузку основных настроек проекта из файла `settings.json`. Все импорты в проекте строятся относительно этого корневого пути.

## Оглавление

1.  [Функции](#функции)
    *   [`set_project_root`](#set_project_root)
2.  [Глобальные переменные](#глобальные-переменные)
    *   [`__root__`](#__root__)
    *   [`settings`](#settings)
    *   [`doc_str`](#doc_str)
    *   [`__project_name__`](#__project_name__)
    *   [`__version__`](#__version__)
    *   [`__doc__`](#__doc__)
    *   [`__details__`](#__details__)
    *   [`__author__`](#__author__)
    *   [`__copyright__`](#__copyright__)
    *   [`__cofee__`](#__cofee__)

## Функции

### `set_project_root`

**Описание**: Находит корневой каталог проекта, начиная с каталога текущего файла, ища вверх по дереву каталогов, останавливаясь на первом каталоге, содержащем любой из маркеров.

**Параметры**:
- `marker_files` (tuple): Кортеж имен файлов или каталогов для идентификации корневого каталога проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневому каталогу, если он найден, иначе — путь к каталогу, где расположен скрипт.

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

**Описание**:  Путь к корневому каталогу проекта. Инициализируется при первом импорте модуля.

### `settings`

**Описание**: Словарь с настройками проекта, загруженный из файла `settings.json`. Загружается при первом импорте модуля. Может быть `None`, если файл не найден или содержит ошибку `JSON`.

```python
settings:dict = None
```

### `doc_str`

**Описание**: Строка документации проекта, загруженная из файла `README.MD`. Может быть `None`, если файл не найден или произошла ошибка чтения.

```python
doc_str:str = None
```

### `__project_name__`

**Описание**: Имя проекта, полученное из настроек (`settings.json`). Если настройки не загружены, по умолчанию равно `hypotez`.

```python
__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
```

### `__version__`

**Описание**: Версия проекта, полученная из настроек (`settings.json`). Если настройки не загружены, по умолчанию пустая строка.

```python
__version__: str = settings.get("version", '')  if settings  else ''
```

### `__doc__`

**Описание**: Документация проекта, загруженная из файла `README.MD`. Если не удалось загрузить, то пустая строка.

```python
__doc__: str = doc_str if doc_str else ''
```

### `__details__`

**Описание**: Детали проекта, на данный момент пустая строка.

```python
__details__: str = ''
```

### `__author__`

**Описание**: Автор проекта, полученный из настроек (`settings.json`). Если настройки не загружены, по умолчанию пустая строка.

```python
__author__: str = settings.get("author", '')  if settings  else ''
```

### `__copyright__`

**Описание**: Информация об авторских правах, полученная из настроек (`settings.json`). Если настройки не загружены, по умолчанию пустая строка.

```python
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
```

### `__cofee__`

**Описание**: Сообщение для поддержки разработчика. Получено из настроек (`settings.json`). Если настройки не загружены, предоставляется сообщение по умолчанию со ссылкой на Boosty.

```python
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```