# Модуль hypotez/src/endpoints/kazarinov/header.py

## Обзор

Этот модуль содержит функции для определения корневой директории проекта, загрузки настроек из файла `settings.json` и документации из файла `README.MD`, а также инициализирует переменные, содержащие информацию о проекте (название, версия, описание и др.).

## Функции

### `set_project_root`

**Описание**:  Ищет корневую директорию проекта, начиная с директории текущего файла и поднимаясь вверх по дереву каталогов.  Останавливается на первой директории, содержащей один из файлов маркеров (например, `pyproject.toml`, `requirements.txt`, `.git`).

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или каталогов, которые используются в качестве маркеров для определения корневой директории. По умолчанию это (`'pyproject.toml'`, `'requirements.txt'`, `.git`).

**Возвращает**:

- `Path`: Путь до корневой директории проекта, если она найдена. В противном случае возвращает директорию, где находится текущий файл.

**Вызывает исключения**:

- Никаких исключений не вызывает.


## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта, полученный с помощью функции `set_project_root`.


### `settings`

**Описание**: Словарь, содержащий настройки проекта, загруженный из файла `src/settings.json`. По умолчанию `None`.

### `doc_str`

**Описание**: Строка с текстом документации, загруженная из файла `src/README.MD`. По умолчанию `None`.


### `__project_name__`

**Описание**:  Имя проекта, полученное из настроек (`settings`). По умолчанию 'hypotez'.


### `__version__`

**Описание**: Версия проекта, полученная из настроек (`settings`). По умолчанию пустая строка.

### `__doc__`

**Описание**: Строка с текстом документации, полученная из файла `src/README.MD`. По умолчанию пустая строка.


### `__details__`

**Описание**: Детали проекта (строка). По умолчанию пустая строка.


### `__author__`

**Описание**: Автор проекта, полученный из настроек (`settings`). По умолчанию пустая строка.


### `__copyright__`

**Описание**: Авторские права на проект, полученный из настроек (`settings`). По умолчанию пустая строка.


### `__cofee__`

**Описание**: Ссылка на возможность поддержать разработчика. По умолчанию ссылка на Boosty.


## Обработка исключений

В коде используются `try...except` блоки для обработки возможных исключений:

- `FileNotFoundError`: Если файл `settings.json` или `README.MD` не найден.
- `json.JSONDecodeError`: Если файл `settings.json` некорректно отформатирован.

В случае возникновения ошибки, соответствующие переменные (settings и doc_str) останутся со значениями по умолчанию.