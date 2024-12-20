# Модуль `header.py`

## Обзор

Модуль `header.py` содержит общие настройки и метаданные проекта, включая определение корневой директории проекта, загрузку настроек из файла `settings.json`, чтение документации из `README.MD`, а также основные метаданные проекта.

## Оглавление

- [Функции](#Функции)
    - [`set_project_root`](#set_project_root)
- [Переменные](#Переменные)
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

**Описание**: Находит корневой каталог проекта, начиная с каталога текущего файла, ища вверх по дереву каталогов до первого каталога, содержащего любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Кортеж имен файлов или каталогов для идентификации корня проекта. По умолчанию `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:
- `Path`: Путь к корневому каталогу, если он найден. В противном случае возвращает каталог, где расположен скрипт.

## Переменные

### `MODE`

**Описание**: Указывает режим работы приложения, по умолчанию установлен в `dev`.
`str`

### `__root__`

**Описание**: Путь к корневому каталогу проекта, полученный с помощью функции `set_project_root`.
`Path`

### `settings`

**Описание**: Словарь с настройками проекта, загруженными из `settings.json`. Если файл не найден или возникла ошибка JSON, переменная остаётся `None`.
`dict | None`

### `doc_str`

**Описание**: Содержимое файла `README.MD` в виде строки. Если файл не найден или возникла ошибка чтения, переменная остаётся `None`.
`str | None`

### `__project_name__`

**Описание**: Название проекта, полученное из настроек (`settings.json`). По умолчанию `hypotez`.
`str`

### `__version__`

**Описание**: Версия проекта, полученная из настроек (`settings.json`). По умолчанию пустая строка.
`str`

### `__doc__`

**Описание**: Строка, содержащая содержимое `README.MD`, используемая для документации.
`str`

### `__details__`

**Описание**: Строка для дополнительных деталей, на данный момент пустая.
`str`

### `__author__`

**Описание**: Имя автора проекта, полученное из настроек (`settings.json`). По умолчанию пустая строка.
`str`

### `__copyright__`

**Описание**: Информация о копирайте проекта, полученная из настроек (`settings.json`). По умолчанию пустая строка.
`str`

### `__cofee__`

**Описание**: Строка с предложением поддержать разработчика, полученная из настроек (`settings.json`). По умолчанию `"Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"`.
`str`