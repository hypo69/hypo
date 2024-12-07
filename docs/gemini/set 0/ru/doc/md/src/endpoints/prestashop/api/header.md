# Модуль hypotez/src/endpoints/prestashop/api/header.py

## Обзор

Этот модуль содержит функции для определения корневой директории проекта и загрузки настроек из файла `settings.json`. Он также загружает описание проекта из файла `README.MD`.

## Функции

### `set_project_root`

**Описание**:  Определяет корневую директорию проекта, начиная с директории текущего файла и идя вверх по дереву директорий, пока не найдет директорию, содержащую один из файлов или директорий, переданных в качестве аргумента `marker_files`.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, которые используются для определения корневой директории проекта. По умолчанию содержит ('pyproject.toml', 'requirements.txt', '.git').


**Возвращает**:

- `Path`: Путь к корневой директории проекта, если она найдена, иначе - путь к директории, где расположен текущий скрипт.


**Вызывает исключения**:

- Нет


### `set_project_root`

**Описание**: Функция устанавливает переменную `__root__`, содержащую путь к корневой директории проекта.

**Параметры**:

- Нет


**Возвращает**:

- Нет


**Вызывает исключения**:

- Нет


## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта.

**Тип**: `Path`


## Загрузка настроек

**Описание**: Загрузка настроек из файла `settings.json` в переменную `settings`.

**Вызывает исключения**:

- `FileNotFoundError`: Если файл `settings.json` не найден.
- `json.JSONDecodeError`: Если файл `settings.json` содержит невалидный JSON.


## Загрузка документации

**Описание**: Загрузка описания проекта из файла `README.MD` в переменную `doc_str`.

**Вызывает исключения**:

- `FileNotFoundError`: Если файл `README.MD` не найден.
- `json.JSONDecodeError`: Если файл `README.MD` содержит невалидный JSON.

## Переменные

### `__project_name__`

**Описание**: Имя проекта, полученное из настроек или, по умолчанию, 'hypotez'.

**Тип**: `str`


### `__version__`

**Описание**: Версия проекта, полученная из настроек или, по умолчанию, пустая строка.

**Тип**: `str`


### `__doc__`

**Описание**: Документация проекта, полученная из файла `README.MD` или, по умолчанию, пустая строка.

**Тип**: `str`


### `__details__`

**Описание**: Подробная информация о проекте, по умолчанию пустая строка.

**Тип**: `str`


### `__author__`

**Описание**: Автор проекта, полученный из настроек или, по умолчанию, пустая строка.

**Тип**: `str`


### `__copyright__`

**Описание**: Авторские права проекта, полученные из настроек или, по умолчанию, пустая строка.

**Тип**: `str`


### `__cofee__`

**Описание**: Ссылка для поддержки разработчика через кофе, полученная из настроек или, по умолчанию, указанная ссылка.

**Тип**: `str`