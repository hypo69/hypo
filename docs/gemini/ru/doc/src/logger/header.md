# Модуль hypotez/src/logger/header.py

## Обзор

Этот модуль отвечает за определение корневого пути к проекту `hypotez`. Он используется для корректного импорта файлов и модулей, а также для доступа к конфигурационным файлам, например, `settings.json` и `README.MD`.

## Функции

### `set_project_root`

**Описание**: Определяет корневой каталог проекта, начиная с текущего файла и перемещаясь вверх по директориям.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или каталогов, используемых для определения корневого каталога проекта. По умолчанию включает `pyproject.toml`, `requirements.txt` и `.git`.


**Возвращает**:

- `Path`: Путь к корневому каталогу проекта, если он найден. В противном случае возвращает путь к каталогу, где расположен текущий файл.

**Вызывает исключения**:

- Нет.


## Переменные

### `__root__`

**Описание**: Путь к корневому каталогу проекта.


**Тип**: `Path`


## Конфигурация

### `settings`

**Описание**: Словарь с настройками проекта, загруженный из файла `src/settings.json`.

**Тип**: `dict` или `None`.


**Обработка ошибок**:

- Возможные исключения:
    - `FileNotFoundError`: Если файл `settings.json` не найден.
    - `json.JSONDecodeError`: Если файл `settings.json` содержит невалидные данные JSON.


### `doc_str`

**Описание**: Строка с содержимым файла `README.MD`, если он найден.

**Тип**: `str` или `None`.

**Обработка ошибок**:

- Возможные исключения:
    - `FileNotFoundError`: Если файл `README.MD` не найден.
    - `json.JSONDecodeError`: Если файл `README.MD` содержит невалидные данные.


## Другие переменные

### `__project_name__`

**Описание**: Название проекта, полученное из `settings.json`.

**Тип**: `str`

**Значение по умолчанию**: `hypotez`.


### `__version__`

**Описание**: Версия проекта, полученная из `settings.json`.

**Тип**: `str`

**Значение по умолчанию**: `''`.


### `__doc__`

**Описание**: Содержимое файла `README.MD` (если он существует).

**Тип**: `str`

**Значение по умолчанию**: `''`.


### `__details__`

**Описание**: Подробная информация о проекте.

**Тип**: `str`

**Значение по умолчанию**: `''`.


### `__author__`

**Описание**: Автор проекта, полученный из `settings.json`.

**Тип**: `str`

**Значение по умолчанию**: `''`.


### `__copyright__`

**Описание**: Авторские права, полученные из `settings.json`.

**Тип**: `str`

**Значение по умолчанию**: `''`.


### `__cofee__`

**Описание**: Ссылка для поддержки разработчика.

**Тип**: `str`

**Значение по умолчанию**: `Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69`.