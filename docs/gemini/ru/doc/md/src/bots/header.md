# Модуль hypotez/src/bots/header.py

## Обзор

Этот модуль отвечает за определение корневого пути проекта `hypotez`. Он находит директорию с определенными файлами (например, `pyproject.toml`, `requirements.txt`, `.git`) и добавляет ее в `sys.path`. Также модуль загружает настройки из `settings.json` и описание из `README.MD`, если они существуют.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная от текущей директории скрипта, ищет вверх по дереву директорий до тех пор, пока не найдет директорию, содержащую указанные маркерные файлы.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, которые указывают на корневую директорию проекта. По умолчанию: `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если она найдена, в противном случае — директорию, где расположен скрипт.

**Вызывает исключения**:

- Нет

## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта. Присваивается значением, возвращаемым функцией `set_project_root`.

**Тип**: `Path`

### `settings`

**Описание**: Словарь с настройками проекта, загруженный из файла `settings.json` в корневой директории проекта.

**Тип**: `dict` или `None`

### `doc_str`

**Описание**: Строка с описанием проекта, загруженная из файла `README.MD` в корневой директории проекта.

**Тип**: `str` или `None`


### `__project_name__`

**Описание**: Название проекта. Получается из настроек `settings`. По умолчанию: `'hypotez'`.

**Тип**: `str`

### `__version__`

**Описание**: Версия проекта. Получается из настроек `settings`. По умолчанию: пустая строка.

**Тип**: `str`

### `__doc__`

**Описание**: Описание проекта. Получается из `doc_str` если он загружен, иначе пустая строка.

**Тип**: `str`

### `__details__`

**Описание**: Дополнительные детали проекта. По умолчанию: пустая строка.

**Тип**: `str`

### `__author__`

**Описание**: Автор проекта. Получается из настроек `settings`. По умолчанию: пустая строка.

**Тип**: `str`

### `__copyright__`

**Описание**: Авторские права на проект. Получается из настроек `settings`. По умолчанию: пустая строка.

**Тип**: `str`

### `__cofee__`

**Описание**: Ссылка на поддержку разработчика. Получается из настроек `settings`. По умолчанию: ссылка на boosty.

**Тип**: `str`


## Обработка исключений

Этот модуль использует `try...except` блоки для обработки `FileNotFoundError` и `json.JSONDecodeError` при чтении файлов `settings.json` и `README.MD`. Если эти файлы не найдены или содержат некорректные данные, соответствующие переменные остаются `None`.