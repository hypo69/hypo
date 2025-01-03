# Модуль `header`

## Обзор

Модуль `header.py` предназначен для определения корневой директории проекта, загрузки настроек из файла `settings.json`, а также для чтения документации из `README.MD`. Он также устанавливает глобальные переменные, содержащие информацию о проекте, такие как имя, версия, автор и т.д.

## Содержание

- [Функции](#Функции)
  - [`set_project_root`](#set_project_root)

- [Глобальные переменные](#Глобальные-переменные)
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

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла, ища вверх по дереву каталогов до первого каталога, содержащего любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Кортеж имен файлов или каталогов, которые идентифицируют корневую директорию проекта. По умолчанию `('__root__','.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если она найдена, иначе директория, где расположен скрипт.

## Глобальные переменные

### `__root__`

**Описание**: Путь к корневой директории проекта.

### `settings`
**Описание**: Словарь, содержащий настройки проекта, загруженные из файла `settings.json`.

### `doc_str`
**Описание**: Строка, содержащая содержимое файла `README.MD`.

### `__project_name__`
**Описание**: Имя проекта, взятое из `settings.json`, или по умолчанию 'hypotez'.

### `__version__`
**Описание**: Версия проекта, взятая из `settings.json`, или пустая строка.

### `__doc__`
**Описание**: Содержимое файла документации `README.MD`.

### `__details__`
**Описание**:  Строка, содержащая подробности о проекте. В текущей версии всегда пустая строка.

### `__author__`
**Описание**: Автор проекта, взятый из `settings.json`, или пустая строка.

### `__copyright__`
**Описание**: Информация о копирайте проекта, взятая из `settings.json`, или пустая строка.

### `__cofee__`
**Описание**: Сообщение с призывом поддержать разработчика чашкой кофе, взятое из `settings.json`, или строка по умолчанию.