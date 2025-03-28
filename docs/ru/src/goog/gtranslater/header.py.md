# Модуль `header.py`

## Обзор

Модуль `header.py` предназначен для определения и настройки корневой директории проекта, загрузки настроек и документации, а также определения основных метаданных проекта, таких как имя, версия, автор и т.д.

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

**Описание**: 
Находит корневой каталог проекта, начиная с каталога текущего файла,
просматривая вверх и останавливаясь в первом каталоге, содержащем любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple, optional): Имена файлов или каталогов для идентификации корневого каталога проекта. По умолчанию `('__root__','.git')`.

**Возвращает**:
- `Path`: Путь к корневому каталогу, если он найден, иначе каталог, где расположен скрипт.

## Переменные

### `__root__`

**Описание**: 
Путь к корневому каталогу проекта.

### `settings`

**Описание**: 
Словарь, содержащий настройки проекта, загруженные из файла `settings.json`.

### `doc_str`

**Описание**: 
Строка, содержащая документацию проекта, загруженную из файла `README.MD`.

### `__project_name__`

**Описание**: 
Имя проекта, полученное из настроек или по умолчанию 'hypotez'.

### `__version__`

**Описание**: 
Версия проекта, полученная из настроек или по умолчанию ''.

### `__doc__`

**Описание**: 
Документация проекта, загруженная из файла или по умолчанию ''.

### `__details__`

**Описание**: 
Детали проекта, в данный момент пустая строка ''.

### `__author__`

**Описание**: 
Автор проекта, полученный из настроек или по умолчанию ''.

### `__copyright__`

**Описание**: 
Авторские права проекта, полученные из настроек или по умолчанию ''.

### `__cofee__`

**Описание**: 
Строка для поддержки разработчика, полученная из настроек или по умолчанию "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69".