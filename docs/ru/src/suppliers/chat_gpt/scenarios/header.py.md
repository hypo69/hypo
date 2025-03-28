# Модуль `header`

## Обзор

Модуль `header` предназначен для инициализации основных параметров проекта, таких как корневая директория, настройки, версия и документация. Он также предоставляет функциональность для определения корневой директории проекта на основе наличия маркерных файлов.

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

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла, и останавливается на первой директории, содержащей любой из маркерных файлов.

**Параметры**:
- `marker_files` (tuple): Имена файлов или директорий, которые идентифицируют корень проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если она найдена. В противном случае - директория, где расположен скрипт.

## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта.

### `settings`

**Описание**: Словарь с настройками проекта, загруженный из файла `settings.json`.

### `doc_str`

**Описание**: Строка с документацией проекта, загруженная из файла `README.MD`.

### `__project_name__`

**Описание**: Имя проекта, взятое из настроек или `hypotez` по умолчанию.

### `__version__`

**Описание**: Версия проекта, взятая из настроек или пустая строка по умолчанию.

### `__doc__`

**Описание**: Строка с документацией проекта, взятая из `doc_str`.

### `__details__`

**Описание**: Строка с дополнительной информацией о проекте.

### `__author__`

**Описание**: Имя автора проекта, взятое из настроек или пустая строка по умолчанию.

### `__copyright__`

**Описание**: Информация об авторских правах, взятая из настроек или пустая строка по умолчанию.

### `__cofee__`

**Описание**: Сообщение с предложением угостить разработчика кофе, взятое из настроек или сообщение по умолчанию.