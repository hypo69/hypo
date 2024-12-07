# Модуль `hypotez/src/logger/header.py`

## Обзор

Модуль `hypotez/src/logger/header.py` определяет корневой путь к проекту. Все импорты строятся относительно этого пути.  В дальнейшем планируется перенести эту функциональность в системные переменные.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с текущей директории и идя вверх по дереву директорий, пока не найдет директорию, содержащую один из указанных маркеров (файлов или директорий).

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или директорий, которые используются в качестве маркеров для определения корневой директории проекта. По умолчанию содержит ('pyproject.toml', 'requirements.txt', '.git').

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если она найдена, иначе - путь к директории, в которой находится текущий файл.

**Вызывает исключения**:

- Нет.


## Переменные

### `__root__`

**Описание**:  Путь к корневой директории проекта, полученный с помощью функции `set_project_root`.

**Тип**: `Path`

### `settings`

**Описание**: Словарь настроек проекта, загруженный из файла `settings.json`.

**Тип**: `dict`

### `doc_str`

**Описание**:  Строковое содержимое файла `README.MD` проекта.

**Тип**: `str`

### `__project_name__`

**Описание**: Название проекта, полученное из настроек (`settings.json`). По умолчанию `hypotez`.

**Тип**: `str`

### `__version__`

**Описание**: Версия проекта, полученная из настроек (`settings.json`). По умолчанию пустая строка.

**Тип**: `str`

### `__doc__`

**Описание**:  Документация проекта, полученная из файла `README.MD`. По умолчанию пустая строка.

**Тип**: `str`

### `__details__`

**Описание**: Подробное описание проекта (пустая строка по умолчанию).

**Тип**: `str`

### `__author__`

**Описание**: Автор проекта, полученный из настроек (`settings.json`). По умолчанию пустая строка.

**Тип**: `str`

### `__copyright__`

**Описание**: Авторские права проекта, полученные из настроек (`settings.json`). По умолчанию пустая строка.

**Тип**: `str`

### `__cofee__`

**Описание**: Ссылка для поддержки разработчика (например, на Boosty). По умолчанию ссылка на Boosty.

**Тип**: `str`

## Обработка исключений

В модуле используются блоки `try...except` для обработки возможных исключений при чтении файлов: `FileNotFoundError` и `json.JSONDecodeError`.  Обработка исключений происходит с использованием `...` для обозначения пропуска возможного исключения.