# Модуль hypotez/src/suppliers/wallmart/header.py

## Обзор

Этот модуль содержит функции для определения корневой директории проекта и загрузки настроек из файла `settings.json`. Он также загружает описание проекта из `README.MD`.

## Функции

### `set_project_root`

**Описание**: Функция находит корневую директорию проекта, начиная с текущей директории и идя вверх по дереву директорий. Поиск останавливается на первой директории, содержащей указанные файлы-маркеры (например, `pyproject.toml`, `requirements.txt`, `.git`).

**Параметры**:

- `marker_files` (tuple): Кортеж имён файлов или директорий, используемых для определения корневой директории проекта. По умолчанию содержит ('pyproject.toml', 'requirements.txt', '.git').

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если она найдена. В противном случае возвращает директорию, где находится текущий файл.

**Вызывает исключения**:

- Нет.


### `set_project_root`

**Описание**: Функция находит корневую директорию проекта, начиная с текущей директории и идя вверх по дереву директорий. Поиск останавливается на первой директории, содержащей указанные файлы-маркеры (например, `pyproject.toml`, `requirements.txt`, `.git`).

**Параметры**:

- `marker_files` (tuple): Кортеж имён файлов или директорий, используемых для определения корневой директории проекта. По умолчанию содержит ('pyproject.toml', 'requirements.txt', '.git').

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если она найдена. В противном случае возвращает директорию, где находится текущий файл.

**Вызывает исключения**:

- Нет.


## Переменные

### `__root__`

**Описание**: Переменная, хранящая путь к корневой директории проекта. Инициализируется функцией `set_project_root`.

**Тип**: `Path`


### `settings`

**Описание**: Словарь, содержащий настройки проекта, загруженные из файла `settings.json`.

**Тип**: `dict`


### `doc_str`

**Описание**: Строка, содержащая описание проекта, загруженная из файла `README.MD`.

**Тип**: `str`


### `__project_name__`

**Описание**: Имя проекта, взятое из настроек или установленное по умолчанию.

**Тип**: `str`


### `__version__`

**Описание**: Версия проекта, взятая из настроек или установленная по умолчанию.

**Тип**: `str`


### `__doc__`

**Описание**: Описание проекта, взятое из файла `README.MD` или установленное по умолчанию.

**Тип**: `str`


### `__details__`

**Описание**: Дополнительные детали проекта (по умолчанию пустая строка).

**Тип**: `str`


### `__author__`

**Описание**: Автор проекта, взятый из настроек или установленный по умолчанию.

**Тип**: `str`


### `__copyright__`

**Описание**: Авторские права проекта, взятые из настроек или установленные по умолчанию.

**Тип**: `str`


### `__cofee__`

**Описание**: Ссылка на страницу для пожертвований на кофе разработчику.

**Тип**: `str`