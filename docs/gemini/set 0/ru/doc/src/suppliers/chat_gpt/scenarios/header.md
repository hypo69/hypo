# Модуль `hypotez/src/suppliers/chat_gpt/scenarios/header.py`

## Обзор

Этот модуль содержит вспомогательные функции для работы с настройками проекта, определяет корневой каталог проекта, загружает настройки из файла `settings.json` и документацию из `README.MD`.  Также модуль содержит переменные, хранящие информацию о проекте (имя, версия, описание, автор и др.).

## Функции

### `set_project_root`

**Описание**:  Находит корневой каталог проекта, начиная от текущей директории и идя вверх по дереву директорий, пока не найдет директорию, содержащую указанные файлы-маркеры (например, `pyproject.toml`, `requirements.txt`, `.git`).

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, которые указывают на корневой каталог проекта. По умолчанию `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневому каталогу проекта, если найден, иначе путь к текущей директории.

**Вызывает исключения**:

- Нет


### `set_project_root`


**Описание**:  Находит корневой каталог проекта, начиная от текущей директории и идя вверх по дереву директорий, пока не найдет директорию, содержащую указанные файлы-маркеры.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, которые указывают на корневой каталог проекта. По умолчанию `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневому каталогу проекта, если найден, иначе путь к текущей директории.

**Вызывает исключения**:

- Нет



## Переменные

### `__root__`

**Описание**: Путь к корневому каталогу проекта, полученный с помощью функции `set_project_root`.

**Тип**: `Path`

### `settings`

**Описание**: Словарь настроек проекта, загруженный из файла `settings.json` в корне проекта.

**Тип**: `dict`

### `doc_str`

**Описание**: Строка с содержимым файла `README.MD`, содержащего описание проекта.

**Тип**: `str`


### `__project_name__`

**Описание**: Название проекта, взятое из `settings.json` или имеющее значение 'hypotez' по умолчанию.

**Тип**: `str`


### `__version__`

**Описание**: Версия проекта, взятая из `settings.json` или пустая строка по умолчанию.

**Тип**: `str`


### `__doc__`

**Описание**: Документация проекта, взятая из `README.MD` или пустая строка по умолчанию.

**Тип**: `str`


### `__details__`

**Описание**: Дополнительные данные о проекте, по умолчанию пустая строка.

**Тип**: `str`


### `__author__`

**Описание**: Автор проекта, взятый из `settings.json` или пустая строка по умолчанию.

**Тип**: `str`


### `__copyright__`

**Описание**: Авторские права проекта, взятый из `settings.json` или пустая строка по умолчанию.

**Тип**: `str`


### `__cofee__`

**Описание**: Ссылка на возможность поддержать разработчика.

**Тип**: `str`


## Обработка исключений

В модуле используются `try...except` блоки для обработки возможных ошибок при чтении файла `settings.json` и файла `README.MD`.  В случае ошибки, соответствующие переменные остаются с пустыми значениями.


## Использование

Модуль `header.py` предназначен для инициализации и доступа к основным метаданным проекта, таким как название, версия, путь к проекту и другие важные настройки.
```