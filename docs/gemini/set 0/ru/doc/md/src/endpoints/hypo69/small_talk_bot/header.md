# Модуль hypotez/src/endpoints/hypo69/small_talk_bot/header.py

## Обзор

Этот модуль содержит вспомогательные функции для работы с проектом, включая нахождение корневой директории проекта, загрузку настроек из файла `settings.json` и чтение документации из файла `README.MD`.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с текущей директории и двигаясь вверх по древу директорий, до тех пор, пока не найдет директорию, содержащую файлы `pyproject.toml`, `requirements.txt` или `.git`.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, используемых для определения корневой директории проекта. По умолчанию (`pyproject.toml`, `requirements.txt`, `.git`).

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если она найдена, иначе - путь к текущей директории.

**Вызывает исключения**:

- Нет.


### `__root__`

**Описание**: Переменная, содержащая путь к корневой директории проекта, полученный с помощью функции `set_project_root`.

**Тип**: `Path`

**Значение**: Путь к корневой директории проекта.


## Переменные

### `MODE`

**Описание**: Переменная, содержащая текущий режим работы (например, 'dev').

**Тип**: `str`

**Значение**: `'dev'`


### `settings`

**Описание**: Словарь настроек проекта, загруженный из файла `settings.json`.

**Тип**: `dict`

**Значение**: Словарь настроек или `None` в случае ошибки.


### `doc_str`

**Описание**: Строка, содержащая текст документации, загруженная из файла `README.MD`.

**Тип**: `str`

**Значение**: Строка с документацией или `None` в случае ошибки.


### `__project_name__`

**Описание**: Название проекта, полученное из настроек.

**Тип**: `str`

**Значение**: Название проекта, по умолчанию `hypotez`.


### `__version__`

**Описание**: Версия проекта, полученная из настроек.

**Тип**: `str`

**Значение**: Версия проекта, по умолчанию пустая строка.


### `__doc__`

**Описание**: Текст документации, загруженная из файла `README.MD`.

**Тип**: `str`

**Значение**: Текст документации, по умолчанию пустая строка.


### `__details__`

**Описание**: Дополнительные детали проекта.

**Тип**: `str`

**Значение**: Пустая строка.


### `__author__`

**Описание**: Автор проекта, полученный из настроек.

**Тип**: `str`

**Значение**: Автор проекта, по умолчанию пустая строка.


### `__copyright__`

**Описание**: Авторские права на проект, полученный из настроек.

**Тип**: `str`

**Значение**: Авторские права, по умолчанию пустая строка.


### `__cofee__`

**Описание**: Ссылка на пожертвование автору проекта для оплаты чашки кофе.

**Тип**: `str`

**Значение**: Ссылка, по умолчанию указанная ссылка.