# Модуль `header.py`

## Обзор

Модуль `header.py` предназначен для инициализации базовых настроек проекта, таких как определение корневой директории, загрузка настроек из `settings.json` и извлечение основной документации из `README.MD`. Также устанавливаются основные атрибуты проекта, такие как имя, версия и автор.

## Содержание

- [Функции](#функции)
    - [`set_project_root`](#set_project_root)
- [Переменные](#переменные)
  - [`MODE`](#MODE)
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
Находит корневую директорию проекта, начиная с директории текущего файла и перемещаясь вверх по дереву каталогов. Поиск останавливается на первом каталоге, содержащем любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Кортеж имен файлов или каталогов, определяющих корень проекта. По умолчанию `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если она найдена; в противном случае - путь к директории, где расположен скрипт.

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
### `MODE`
**Описание**:
Указывает режим работы приложения.
Тип: `str`
Значение по умолчанию: `'dev'`

### `__root__`
**Описание**:
Содержит путь к корневой директории проекта.
Тип: `Path`

### `settings`
**Описание**:
Словарь, содержащий настройки проекта, загруженные из файла `settings.json`.
Тип: `dict | None`

### `doc_str`
**Описание**:
Строка, содержащая документацию проекта, загруженную из файла `README.MD`.
Тип: `str | None`

### `__project_name__`
**Описание**:
Имя проекта, извлеченное из `settings.json` или установлено по умолчанию `hypotez`.
Тип: `str`

### `__version__`
**Описание**:
Версия проекта, извлеченная из `settings.json` или установлена по умолчанию `''`.
Тип: `str`

### `__doc__`
**Описание**:
Основная документация проекта, загруженная из `README.MD` или установлена по умолчанию `''`.
Тип: `str`

### `__details__`
**Описание**:
Дополнительная информация о проекте, пока не инициализирована.
Тип: `str`
Значение по умолчанию: `''`

### `__author__`
**Описание**:
Автор проекта, извлеченный из `settings.json` или установлен по умолчанию `''`.
Тип: `str`

### `__copyright__`
**Описание**:
Информация об авторских правах проекта, извлеченная из `settings.json` или установлена по умолчанию `''`.
Тип: `str`

### `__cofee__`
**Описание**:
Сообщение с предложением поддержки разработчика, извлеченное из `settings.json` или установлено по умолчанию "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69".
Тип: `str`