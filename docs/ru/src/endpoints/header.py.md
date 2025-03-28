# Модуль `header.py`

## Обзор

Модуль `header.py` содержит определения для получения корневого каталога проекта, загрузки настроек из файла `settings.json`, чтения документации из файла `README.md` и определения основных параметров проекта, таких как имя, версия, автор и т.д.

## Содержание

- [Функции](#Функции)
    - [`set_project_root`](#set_project_root)
- [Переменные](#Переменные)
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

**Описание**: Находит корневой каталог проекта, начиная с каталога текущего файла, поднимаясь вверх и останавливаясь на первом каталоге, содержащем любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Имена файлов или каталогов для идентификации корня проекта.

**Возвращает**:
- `Path`: Путь к корневому каталогу, если найден, иначе каталог, где расположен скрипт.

## Переменные

### `__root__`

**Описание**: Путь к корневому каталогу проекта.

### `settings`

**Описание**: Словарь с настройками проекта, загруженный из файла `settings.json`.

### `doc_str`

**Описание**: Строка с документацией, загруженная из файла `README.md`.

### `__project_name__`

**Описание**: Имя проекта, по умолчанию `'hypotez'`, загружается из `settings.json`.

### `__version__`

**Описание**: Версия проекта, по умолчанию `''`, загружается из `settings.json`.

### `__doc__`

**Описание**: Строка с документацией, загруженная из `README.md` или пустая строка, если файл не найден.

### `__details__`

**Описание**: Детали проекта, по умолчанию пустая строка.

### `__author__`

**Описание**: Автор проекта, по умолчанию `''`, загружается из `settings.json`.

### `__copyright__`

**Описание**: Авторские права проекта, по умолчанию `''`, загружается из `settings.json`.

### `__cofee__`

**Описание**: Строка с сообщением о поддержке разработчика, по умолчанию `"Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"`, загружается из `settings.json`.