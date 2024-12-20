# Модуль hypotez/src/webdriver/header.py

## Обзор

Этот модуль содержит функции для определения корневого каталога проекта, загрузки настроек из файла `settings.json` и получения документации из файла `README.MD`. Он также предоставляет переменные для доступа к имени проекта, версии, документации, информации об авторе и других метаданных.

## Функции

### `set_project_root`

**Описание**: Находит корневой каталог проекта, начиная с текущего каталога и идя вверх по директориям, пока не найдет каталог, содержащий указанные файлы-маркеры.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или каталогов, используемых для определения корневого каталога проекта. По умолчанию `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневому каталогу проекта, если найден, иначе путь к каталогу, где расположен текущий скрипт.

**Вызывает исключения**:

- Нет


### Загрузка настроек и документации

Этот модуль включает в себя обработку файла настроек `settings.json` и файла документации `README.MD`.

**Загрузка настроек**:

- Функция загружает настройки из файла `gs.path.root / 'src' / 'settings.json'`.
- Используется обработка исключений `FileNotFoundError` и `json.JSONDecodeError` для обработки случаев, когда файл не найден или некорректен.

**Загрузка документации**:

- Функция загружает содержимое файла `gs.path.root / 'src' / 'README.MD'`.
- Используется обработка исключений `FileNotFoundError` и `json.JSONDecodeError` для обработки случаев, когда файл не найден или некорректен.

## Переменные

### `__root__`

**Описание**: Путь к корневому каталогу проекта.  Получается с помощью вызова функции `set_project_root()`.

**Тип**: `Path`

### `settings`

**Описание**: Словарь, содержащий настройки проекта, загруженные из файла `settings.json`.

**Тип**: `dict` | `None`

### `doc_str`

**Описание**: Строка, содержащая содержимое файла `README.MD`.

**Тип**: `str` | `None`

### `__project_name__`

**Описание**: Название проекта, взятое из настроек (`settings`) или заданное по умолчанию (`'hypotez'`).

**Тип**: `str`

### `__version__`

**Описание**: Версия проекта, взятая из настроек (`settings`) или заданная по умолчанию (`''`).

**Тип**: `str`

### `__doc__`

**Описание**: Документация проекта, взятая из файла `README.MD` или заданная по умолчанию (`''`).

**Тип**: `str`

### `__details__`

**Описание**: Детали проекта (по умолчанию пустая строка).

**Тип**: `str`

### `__author__`

**Описание**: Автор проекта, взятый из настроек (`settings`) или заданный по умолчанию (`''`).

**Тип**: `str`

### `__copyright__`

**Описание**: Авторские права проекта, взятые из настроек (`settings`) или заданные по умолчанию (`''`).

**Тип**: `str`

### `__cofee__`

**Описание**: Ссылка на способ поддержать разработчика.

**Тип**: `str`