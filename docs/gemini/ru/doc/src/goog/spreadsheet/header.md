# Модуль hypotez/src/goog/spreadsheet/header.py

## Обзор

Этот модуль содержит функции для определения корневой директории проекта, загрузки настроек из файла `settings.json` и чтения файла `README.MD`.  Он также предоставляет доступ к переменным, содержащим информацию о проекте, такие как имя, версия, описание, автор и т.д.

## Оглавление

- [Функции](#функции)
    - [`set_project_root`](#set_project_root)


## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с текущей директории и двигаясь вверх по иерархии директорий, пока не найдёт директорию, содержащую один из указанных файлов-маркеров (pyproject.toml, requirements.txt, .git).

**Параметры**:
- `marker_files` (tuple): Кортеж имён файлов или директорий, используемых для идентификации корневой директории. По умолчанию `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории проекта, если найдена, иначе - путь к директории, в которой находится скрипт.

**Вызывает исключения**:
-  Не вызывает исключений.


## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта, полученный с помощью функции `set_project_root()`.

**Тип**: `Path`

### `settings`

**Описание**: Словарь, содержащий настройки проекта, загруженный из файла `settings.json`.

**Тип**: `dict` или `None`

### `doc_str`

**Описание**: Строка, содержащая содержимое файла `README.MD`.

**Тип**: `str` или `None`

### `__project_name__`

**Описание**: Имя проекта, полученное из настроек (`settings.json`) или имеющее значение по умолчанию `hypotez`.

**Тип**: `str`

### `__version__`

**Описание**: Версия проекта, полученная из настроек (`settings.json`) или пустая строка по умолчанию.

**Тип**: `str`

### `__doc__`

**Описание**: Описание проекта, полученное из файла `README.MD` или пустая строка по умолчанию.

**Тип**: `str`

### `__details__`

**Описание**: Подробное описание проекта (пустая строка по умолчанию).

**Тип**: `str`

### `__author__`

**Описание**: Автор проекта, полученный из настроек (`settings.json`) или пустая строка по умолчанию.

**Тип**: `str`

### `__copyright__`

**Описание**: Авторские права, полученные из настроек (`settings.json`) или пустая строка по умолчанию.

**Тип**: `str`

### `__cofee__`

**Описание**: Ссылка для пожертвования на поддержку разработчика (кофе).

**Тип**: `str`