# Модуль hypotez/src/suppliers/wallashop/header.py

## Обзор

Этот модуль содержит функции для определения корневой директории проекта и загрузки настроек из файла `settings.json` и документации из `README.MD`. Он также предоставляет переменные, содержащие информацию о проекте, такие как имя, версия, описание и автор.


## Функции

### `set_project_root`

**Описание**: Определяет корневую директорию проекта, начиная с текущей директории и ищет вверх по дереву директорий, пока не найдет директорию, содержащую файлы-маркеры (например, `pyproject.toml`, `requirements.txt`, `.git`).

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или директорий, используемых для определения корневой директории проекта. По умолчанию: (`'pyproject.toml'`, `'requirements.txt'`, `'.git'`).


**Возвращает**:

- `Path`: Путь к корневой директории проекта, если она найдена. В противном случае возвращает директорию, где расположен текущий скрипт.


**Вызывает исключения**:

- Нет


### `__init__`

**Описание**: Эта функция выполняется при импорте и инициализирует переменные проекта.


**Параметры**:


**Возвращает**:


**Вызывает исключения**:


## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта. Инициализируется при вызове `set_project_root()`.

**Тип**: `Path`


### `settings`

**Описание**: Словарь с настройками проекта, загруженный из файла `settings.json`.

**Тип**: `dict` или `None`


### `doc_str`

**Описание**: Строковое содержимое файла `README.MD`.

**Тип**: `str` или `None`



### `__project_name__`

**Описание**: Имя проекта, полученное из настроек или значение по умолчанию `'hypotez'`.

**Тип**: `str`


### `__version__`

**Описание**: Версия проекта, полученная из настроек или значение по умолчанию `''`.

**Тип**: `str`


### `__doc__`

**Описание**: Документация проекта, полученная из `README.MD` или значение по умолчанию `''`.

**Тип**: `str`


### `__details__`

**Описание**: Подробная информация о проекте (значение по умолчанию пустая строка).

**Тип**: `str`


### `__author__`

**Описание**: Автор проекта, полученный из настроек или значение по умолчанию `''`.

**Тип**: `str`


### `__copyright__`

**Описание**: Авторские права, полученные из настроек или значение по умолчанию `''`.

**Тип**: `str`


### `__cofee__`

**Описание**: Ссылка для поддержки разработчика.

**Тип**: `str`