# Модуль hypotez/src/product/product_fields/header.py

## Обзор

Этот модуль содержит функции для определения корневой директории проекта и загрузки настроек из файла `settings.json`. Он также предоставляет доступ к документирующей строке из файла `README.MD`.  Ключевые переменные содержат информацию о проекте: имя, версия, описание, автор, права и ссылку на поддержку.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная от директории текущего файла и идя вверх по дереву директорий, пока не найдёт директорию, содержащую один из файлов/папок, указанных в аргументе `marker_files`.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или каталогов, используемых для определения корневой директории проекта. По умолчанию: `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена, иначе директория, в которой расположен данный скрипт.

**Вызывает исключения**:

- Нет.


### `set_project_root`


**Описание**:  Находит корневую директорию проекта.

**Параметры**:


- Нет


**Возвращает**:

- `Path`: Путь к корневой директории.

**Вызывает исключения**:

- Нет.

## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта, полученный с помощью функции `set_project_root`.

**Тип**: `Path`

### `settings`

**Описание**: Словарь с настройками проекта, загруженный из файла `settings.json` в корневой директории.

**Тип**: `dict` или `None` (если файл не найден или содержит ошибки).

### `doc_str`

**Описание**: Строка документации, содержащая текст из файла `README.MD`.

**Тип**: `str` или `None` (если файл не найден или содержит ошибки).


### `__project_name__`

**Описание**: Имя проекта, полученное из файла настроек (`settings.json`) или по умолчанию `'hypotez'`.

**Тип**: `str`

### `__version__`

**Описание**: Версия проекта, полученная из файла настроек (`settings.json`) или по умолчанию `''`.

**Тип**: `str`

### `__doc__`

**Описание**: Текст документации проекта, загруженный из файла `README.MD` (или пустая строка, если файл не найден).

**Тип**: `str`

### `__details__`

**Описание**: Дополнительные детали о проекте (пустая строка по умолчанию).

**Тип**: `str`


### `__author__`

**Описание**: Автор проекта, полученный из файла настроек (`settings.json`) или по умолчанию `''`.

**Тип**: `str`

### `__copyright__`

**Описание**: Авторские права проекта, полученные из файла настроек (`settings.json`) или по умолчанию `''`.

**Тип**: `str`

### `__cofee__`

**Описание**: Ссылка на спонсорскую площадку для поддержки разработчика.

**Тип**: `str`