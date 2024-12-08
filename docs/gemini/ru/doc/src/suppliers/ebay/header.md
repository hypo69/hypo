# Модуль `hypotez/src/suppliers/ebay/header.py`

## Обзор

Этот модуль содержит функции для определения корневой директории проекта, загрузки настроек из файла `settings.json` и получения документации из файла `README.MD`. Он также предоставляет глобальные переменные, хранящие информацию о проекте, такие как имя, версия, описание, автор и т.д.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с текущей директории. Поиск происходит вверх по директориям, пока не будет найдена директория, содержащая один из указанных файлов или директорий.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, которые используются для определения корневой директории проекта. По умолчанию это `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневой директории проекта. Если корневая директория не найдена, возвращается директория, в которой расположен данный скрипт.

**Вызывает исключения**:

- Нет


## Глобальные переменные

### `__root__`

**Описание**: Путь к корневой директории проекта, полученный с помощью функции `set_project_root()`.

**Тип**: `Path`

### `settings`

**Описание**: Словарь настроек, загруженный из файла `src/settings.json`.

**Тип**: `dict`

### `doc_str`

**Описание**: Строка документации, полученная из файла `src/README.MD`.

**Тип**: `str`

### `__project_name__`

**Описание**: Имя проекта, полученное из настроек. По умолчанию `'hypotez'`.

**Тип**: `str`

### `__version__`

**Описание**: Версия проекта, полученная из настроек. По умолчанию `''`.

**Тип**: `str`

### `__doc__`

**Описание**: Документация проекта, полученная из `README.MD`. По умолчанию `''`.

**Тип**: `str`

### `__details__`

**Описание**: Подробная информация о проекте. По умолчанию `''`.

**Тип**: `str`

### `__author__`

**Описание**: Автор проекта, полученный из настроек. По умолчанию `''`.

**Тип**: `str`

### `__copyright__`

**Описание**: Авторские права проекта, полученный из настроек. По умолчанию `''`.

**Тип**: `str`

### `__cofee__`

**Описание**: Ссылка на страницу сбора пожертвований на кофе для разработчика. По умолчанию ссылка.

**Тип**: `str`


## Обработка исключений

При попытке загрузить настройки или документацию, этот модуль обрабатывает исключения `FileNotFoundError` и `json.JSONDecodeError`. В случае ошибки, соответствующие переменные (settings, doc_str) устанавливаются в `None` или пустую строку.