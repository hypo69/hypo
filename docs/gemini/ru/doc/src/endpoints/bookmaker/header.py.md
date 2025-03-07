# Модуль `header.py`

## Обзор

Модуль `header.py` содержит настройки и метаданные проекта, включая определение корневой директории проекта, загрузку настроек из `settings.json` и документации из `README.MD`, а также основные переменные, описывающие проект.

## Оглавление
1. [Функции](#Функции)
    - [`set_project_root`](#set_project_root)
2. [Глобальные переменные](#Глобальные-переменные)
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
Находит корневую директорию проекта, начиная с директории текущего файла, поднимаясь вверх и останавливаясь в первой директории, содержащей любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Кортеж имен файлов или директорий для идентификации корневой директории проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если она найдена, иначе - путь к директории, где расположен скрипт.

## Глобальные переменные

### `__root__`

**Описание**:
Путь к корневой директории проекта, полученный с помощью функции `set_project_root`.

### `settings`

**Описание**:
Словарь с настройками проекта, загруженный из файла `settings.json`. В случае ошибки (файла нет или он некорректен) значение будет `None`.

### `doc_str`

**Описание**:
Строка, содержащая документацию из файла `README.MD`. В случае ошибки (файла нет) значение будет `None`.

### `__project_name__`

**Описание**:
Название проекта. По умолчанию - 'hypotez'. Загружается из настроек (`settings.json`), если они доступны.

### `__version__`

**Описание**:
Версия проекта. Загружается из настроек (`settings.json`), если они доступны.

### `__doc__`

**Описание**:
Документация проекта, загруженная из `README.MD`.

### `__details__`

**Описание**:
Дополнительная информация о проекте (сейчас всегда пустая строка).

### `__author__`

**Описание**:
Автор проекта. Загружается из настроек (`settings.json`), если они доступны.

### `__copyright__`

**Описание**:
Информация об авторских правах. Загружается из настроек (`settings.json`), если они доступны.

### `__cofee__`

**Описание**:
Сообщение о возможности поддержать разработчика чашкой кофе. Загружается из настроек (`settings.json`), если они доступны, иначе - используется сообщение по умолчанию.