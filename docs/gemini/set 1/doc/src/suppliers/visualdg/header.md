# Модуль `hypotez/src/suppliers/visualdg/header.py`

## Обзор

Данный модуль содержит функции для определения корневой директории проекта и загрузки настроек из файла `settings.json`. Он также предоставляет доступ к информации о проекте, такой как название, версия, описание, автор и прочие детали.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла. Поиск ведется вверх по директориям, пока не будет найдена директория, содержащая один из указанных файлов или папок.  Если корневая директория не найдена, возвращает директорию, где расположен текущий скрипт.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, которые используются для определения корневой директории. По умолчанию: `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневой директории проекта.

**Вызывает исключения**:

- Нет

### `set_project_root`

**Описание**: Загрузка настроек проекта из файла `settings.json`.

**Параметры**:

- Нет

**Возвращает**:

- `dict`: Словарь с настройками проекта. Возвращает `None`, если файл не найден или не удалось его обработать.


## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта, полученный с помощью функции `set_project_root()`.

**Тип**: `Path`


## Переменные (константы)


### `MODE`

**Описание**: Переменная, хранящая значение режима работы (`'dev'`).


### `__project_name__`

**Описание**: Имя проекта. Получается из настроек `settings`, по умолчанию `'hypotez'`.

**Тип**: `str`


### `__version__`

**Описание**: Версия проекта. Получается из настроек `settings`, по умолчанию пустая строка.

**Тип**: `str`

### `__doc__`

**Описание**: Документация к проекту. Получается из файла `README.MD`, по умолчанию пустая строка.

**Тип**: `str`

### `__details__`

**Описание**: Подробная информация о проекте. По умолчанию пустая строка.

**Тип**: `str`

### `__author__`

**Описание**: Автор проекта. Получается из настроек `settings`, по умолчанию пустая строка.

**Тип**: `str`


### `__copyright__`

**Описание**: Авторские права. Получается из настроек `settings`, по умолчанию пустая строка.

**Тип**: `str`


### `__cofee__`

**Описание**: Ссылка на возможность поддержать разработчика. Получается из настроек `settings`, по умолчанию значение по умолчанию.

**Тип**: `str`


## Обработка исключений

В модуле используется конструкция `try...except` для обработки потенциальных ошибок `FileNotFoundError` и `json.JSONDecodeError` при чтении файлов `settings.json` и `README.MD`. В случае ошибки переменные `settings` и `doc_str` соответственно устанавливаются в `None` или пустую строку.