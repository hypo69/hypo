# Модуль `header.py`

## Обзор

Модуль `header.py` определяет корневой путь к проекту и предоставляет основные метаданные проекта, такие как имя, версия, автор и т.д. Модуль используется для настройки путей и загрузки основных настроек из `settings.json`.

## Оглавление

1. [Функции](#функции)
    - [`set_project_root`](#set_project_root)
2. [Глобальные переменные](#глобальные-переменные)

## Функции

### `set_project_root`

**Описание**:
Находит корневую директорию проекта, начиная с директории текущего файла,
поиск ведется вверх по дереву каталогов и останавливается на первой директории, содержащей любой из указанных маркерных файлов.

**Параметры**:
- `marker_files` (tuple, optional): Кортеж с именами файлов или директорий, которые идентифицируют корень проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если она найдена. В противном случае возвращает директорию, в которой находится скрипт.

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

- `__root__` (Path): Путь к корневой директории проекта.
- `settings` (dict): Словарь с настройками проекта, загруженный из `settings.json`. Если файл не найден или невалиден, значение `None`.
- `doc_str` (str): Строка, содержащая содержимое файла `README.MD`. Если файл не найден или невалиден, значение `None`.
- `__project_name__` (str): Название проекта, по умолчанию `hypotez`.
- `__version__` (str): Версия проекта, по умолчанию пустая строка.
- `__doc__` (str): Содержимое файла `README.MD`, по умолчанию пустая строка.
- `__details__` (str): Детали проекта, по умолчанию пустая строка.
- `__author__` (str): Автор проекта, по умолчанию пустая строка.
- `__copyright__` (str): Информация о копирайте, по умолчанию пустая строка.
- `__cofee__` (str): Сообщение о поддержке проекта, по умолчанию: "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"