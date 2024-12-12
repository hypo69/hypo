# Модуль `header.py`

## Обзор

Модуль `header.py` предназначен для настройки и инициализации основных параметров проекта, включая определение корневой директории, загрузку настроек из `settings.json`, чтение документации из `README.MD`, а также определение основных переменных проекта, таких как имя проекта, версия, автор и т.д.

## Содержание

1.  [Обзор](#обзор)
2.  [Функции](#функции)
    *   [`set_project_root`](#set_project_root)
3.  [Переменные](#переменные)

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла, и добавляет её в `sys.path`. Поиск осуществляется вверх по дереву каталогов до первого каталога, содержащего один из файлов-маркеров.

**Параметры**:
-   `marker_files` (tuple, optional): Кортеж имен файлов или директорий, которые идентифицируют корень проекта. По умолчанию `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:
-   `Path`: Путь к корневой директории проекта, если она найдена. В противном случае возвращается директория, в которой расположен скрипт.

```python
def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Args:
        marker_files (tuple, optional): Filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').

    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
```

## Переменные

-   `MODE` (str): Устанавливает режим работы приложения. По умолчанию `'dev'`.
-   `__root__` (Path): Путь к корневой директории проекта, полученный с помощью функции `set_project_root`.
-   `settings` (dict): Словарь, загруженный из `settings.json` файла, содержащий настройки проекта.
-   `doc_str` (str): Строка, содержащая содержимое файла `README.MD`, используется для хранения документации проекта.
-   `__project_name__` (str): Имя проекта, полученное из файла настроек `settings.json`. По умолчанию `'hypotez'`.
-   `__version__` (str): Версия проекта, полученная из файла настроек `settings.json`. По умолчанию `''`.
-   `__doc__` (str): Строка документации проекта, полученная из файла `README.MD`. По умолчанию `''`.
-   `__details__` (str): Строка для подробностей проекта. По умолчанию `''`.
-    `__author__` (str): Автор проекта, полученный из файла `settings.json`. По умолчанию `''`.
-   `__copyright__` (str): Информация о копирайте проекта, полученная из `settings.json`. По умолчанию `''`.
-   `__cofee__` (str): Сообщение для поддержки разработчика, получено из `settings.json`. По умолчанию `"Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"`.