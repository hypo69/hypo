# Модуль hypotez/src/logger/header.py

## Обзор

Модуль `hypotez/src/logger/header.py` определяет корневой путь к проекту `hypotez`. Все импорты в других модулях строятся относительно этого пути.  Он также загружает настройки из файла `settings.json` и описание проекта из `README.MD`.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с текущего файла, проходя вверх по дереву каталогов и останавливаясь на первой директории, содержащей один из указанных маркеров файлов (например, `pyproject.toml`, `requirements.txt`, `.git`). Если корневой каталог не найден, возвращает директорию, где расположен текущий файл.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, используемых для поиска корневого каталога. По умолчанию `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневому каталогу проекта, если он найден. В противном случае возвращает путь к директории текущего файла.

**Вызывает исключения**:

- Нет


## Переменные

### `__root__`

**Описание**: Переменная, содержащая корневой путь к проекту.  Инициализируется функцией `set_project_root()`.

**Тип**: `Path`

**Значение**: Путь к корневому каталогу проекта


### `settings`

**Описание**: Словарь со настройками проекта, загруженный из файла `settings.json`.

**Тип**: `dict` или `None`.

**Значение**: Словарь с настройками или `None`, если файл `settings.json` не найден или содержит некорректные данные.


### `doc_str`

**Описание**: Строка с описанием проекта, загруженная из файла `README.MD`.

**Тип**: `str` или `None`

**Значение**:  Строка с описанием проекта или `None`, если файл `README.MD` не найден или содержит некорректные данные.


### `__project_name__`

**Описание**: Название проекта, полученное из настроек `settings`. По умолчанию `hypotez`.

**Тип**: `str`

**Значение**:  Название проекта


### `__version__`

**Описание**: Версия проекта, полученная из настроек `settings`. По умолчанию пустая строка.

**Тип**: `str`

**Значение**:  Версия проекта


### `__doc__`

**Описание**:  Описание проекта, загруженное из `README.MD`. По умолчанию пустая строка.

**Тип**: `str`

**Значение**: Описание проекта


### `__details__`

**Описание**: Дополнительные детали проекта (пустая строка по умолчанию).

**Тип**: `str`

**Значение**: Дополнительные детали проекта


### `__author__`

**Описание**: Автор проекта, полученный из настроек `settings`. По умолчанию пустая строка.

**Тип**: `str`

**Значение**: Автор проекта


### `__copyright__`

**Описание**: Авторские права проекта, полученные из настроек `settings`. По умолчанию пустая строка.

**Тип**: `str`

**Значение**: Авторские права проекта


### `__cofee__`

**Описание**: Ссылка на бонусную поддержку автора проекта (кофе). По умолчанию ссылка на Boosty.

**Тип**: `str`

**Значение**: Ссылка на бонусную поддержку проекта.