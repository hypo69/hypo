# Модуль hypotez/src/ai/gemini/header.py

## Обзор

Данный модуль (`hypotez/src/ai/gemini/header.py`) предоставляет функции для работы с конфигурацией проекта, получения пути к корневой директории проекта и чтения файла `config.json` и `README.MD`. Он также содержит переменные, содержащие информацию о проекте (название, версия, описание, автор и т.д.).

## Функции

### `set_project_root`

**Описание**: Функция находит корневую директорию проекта, начиная от текущей директории файла и идя вверх по дереву директорий.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, по которым определяется корневая директория проекта. По умолчанию используются `'pyproject.toml'`, `'requirements.txt'`, `.git`.


**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена, иначе - путь к директории текущего файла.

**Вызывает исключения**:

- Нет


### `config`

**Описание**: переменная, содержащая данные из файла `config.json`.

**Параметры**:

- Нет


**Возвращает**:

- `dict`: Словарь с данными из `config.json` или `None` при ошибке.

**Вызывает исключения**:

- `FileNotFoundError`: Если файл `config.json` не найден.
- `json.JSONDecodeError`: Если содержимое файла `config.json` не является валидным JSON.


### `doc_str`

**Описание**: переменная, содержащая содержимое файла `README.MD`.

**Параметры**:

- Нет


**Возвращает**:

- `str`: Содержимое файла `README.MD` или `None` при ошибке.

**Вызывает исключения**:

- `FileNotFoundError`: Если файл `README.MD` не найден.
- `json.JSONDecodeError`: Если содержимое файла `README.MD` не является корректным текстом.

## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта, полученный функцией `set_project_root`.

**Тип**: `Path`

**Описание**: Путь к корневой директории проекта.


### `__project_name__`

**Описание**: Название проекта, полученное из `config.json`. По умолчанию `'hypotez'`.

**Тип**: `str`

### `__version__`

**Описание**: Версия проекта, полученная из `config.json`. По умолчанию `''`.

**Тип**: `str`


### `__doc__`

**Описание**: Документация проекта, полученная из `README.MD`. По умолчанию `''`.

**Тип**: `str`


### `__details__`

**Описание**: Дополнительные детали проекта. По умолчанию пустая строка.

**Тип**: `str`

### `__author__`

**Описание**: Автор проекта, полученный из `config.json`. По умолчанию `''`.

**Тип**: `str`

### `__copyright__`

**Описание**: Авторские права, полученные из `config.json`. По умолчанию `''`.

**Тип**: `str`

### `__cofee__`

**Описание**: Ссылка на поддержку разработчика через платёжную систему. По умолчанию - ссылка на Boosty.

**Тип**: `str`


## Использование

Этот модуль устанавливает необходимые переменные, необходимые для последующего использования в проекте.  Файл `config.json` должен содержать информацию о проекте, а файл `README.MD` — его документацию.