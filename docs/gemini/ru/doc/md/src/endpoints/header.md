# Модуль hypotez/src/endpoints/header.py

## Обзор

Этот модуль содержит функции для определения корневой директории проекта и загрузки настроек из файла `settings.json`.  Он также обрабатывает чтение файла документации `README.MD` и инициализирует переменные, содержащие информацию о проекте (название, версия, автор, и т.д.).

## Оглавление

- [Функции](#функции)
    - [`set_project_root`](#set_project_root)

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла, ищет вверх по директориям, пока не найдет директорию, содержащую указанные файлы-маркеры (например, `pyproject.toml`, `requirements.txt`, `.git`).

**Параметры**:
- `marker_files` (tuple): Кортеж имен файлов или директорий, используемых для идентификации корневой директории проекта. По умолчанию `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории проекта, если найдена, иначе путь к директории, где расположен скрипт.

**Вызывает исключения**:
- Нет


## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта, полученный с помощью функции `set_project_root`.


### `settings`

**Описание**: Словарь настроек проекта, загруженный из файла `settings.json`.  Если файл не найден или некорректен, `settings` устанавливается в `None`.

### `doc_str`

**Описание**: Строка, содержащая содержимое файла `README.MD`. Если файл не найден или некорректен, `doc_str` устанавливается в `None`.

### `__project_name__`

**Описание**: Название проекта, полученное из настроек (`settings`). По умолчанию `hypotez`.

### `__version__`

**Описание**: Версия проекта, полученная из настроек (`settings`). По умолчанию пустая строка.

### `__doc__`

**Описание**: Документация проекта, полученная из файла `README.MD`. По умолчанию пустая строка.

### `__details__`

**Описание**: Подробная информация о проекте. По умолчанию пустая строка.

### `__author__`

**Описание**: Автор проекта, полученный из настроек (`settings`). По умолчанию пустая строка.

### `__copyright__`

**Описание**: Авторские права проекта, полученные из настроек (`settings`). По умолчанию пустая строка.

### `__cofee__`

**Описание**: Ссылка для поддержки разработчика. По умолчанию ссылка для пожертвования.