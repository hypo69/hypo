# Модуль hypotez/src/ai/myai/header.py

## Обзор

Этот модуль содержит функции для определения корневого каталога проекта и загрузки настроек проекта из файла `settings.json`.  Он также содержит переменные, хранящие информацию о проекте, например, имя, версию, документацию, автора и ссылку на поддержку разработчика.

## Функции

### `set_project_root`

**Описание**:  Находит корневой каталог проекта, начиная с текущего каталога и поднимаясь по иерархии каталогов до тех пор, пока не найдет каталоги, содержащие файлы, указанные в аргументе `marker_files`.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или каталогов, которые указывают на корневой каталог проекта. По умолчанию включает `pyproject.toml`, `requirements.txt` и `.git`.

**Возвращает**:

- `Path`: Путь к корневому каталогу проекта, если он найден. В противном случае возвращает каталог, в котором находится текущий скрипт.

**Вызывает исключения**:

- Нет


## Переменные

### `__root__`

**Описание**: Путь к корневому каталогу проекта, полученный с помощью функции `set_project_root`.

**Тип**: `Path`

**Значение**: Путь к корневому каталогу проекта.


### `settings`

**Описание**: Словарь настроек проекта, загруженный из файла `settings.json`.

**Тип**: `dict`

**Значение**: Словарь с настройками проекта или `None`, если файл `settings.json` не найден или содержит невалидный JSON.


### `doc_str`

**Описание**: Строка документации проекта, загруженная из файла `README.MD`.

**Тип**: `str`

**Значение**: Содержимое файла `README.MD` или `None`, если файл не найден или при возникновении ошибки.

### `__project_name__`

**Описание**: Имя проекта, взятое из файла `settings.json`. По умолчанию `hypotez`.

**Тип**: `str`

**Значение**: Имя проекта.

### `__version__`

**Описание**: Версия проекта, взятая из файла `settings.json`. По умолчанию пустая строка.

**Тип**: `str`

**Значение**: Версия проекта.


### `__doc__`

**Описание**: Документация проекта, взятая из файла `README.MD`. По умолчанию пустая строка.

**Тип**: `str`

**Значение**: Документация проекта.


### `__details__`

**Описание**: Дополнительная информация о проекте (по умолчанию пустая строка).

**Тип**: `str`

**Значение**: Дополнительная информация.


### `__author__`

**Описание**: Автор проекта, взятый из файла `settings.json`. По умолчанию пустая строка.

**Тип**: `str`

**Значение**: Автор проекта.


### `__copyright__`

**Описание**: Авторские права проекта, взятые из файла `settings.json`. По умолчанию пустая строка.

**Тип**: `str`

**Значение**: Авторские права проекта.

### `__cofee__`

**Описание**: Ссылка на спонсорскую платформу для поддержки разработчика (по умолчанию ссылка на Boosty).

**Тип**: `str`

**Значение**: Ссылка на спонсорскую платформу.