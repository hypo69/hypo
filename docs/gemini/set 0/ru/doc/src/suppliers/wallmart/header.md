# Модуль `hypotez/src/suppliers/wallmart/header.py`

## Обзор

Этот модуль содержит функции для определения корневой директории проекта и загрузки настроек из файла `settings.json`. Он также загружает описание проекта из файла `README.MD`.

## Функции

### `set_project_root`

**Описание**: Определяет корневую директорию проекта, начиная с директории текущего файла, ищет вверх по дереву директорий, пока не найдет директорию, содержащую один из файлов-маркеров (например, `pyproject.toml`, `requirements.txt`, `.git`).

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, используемых для определения корневой директории проекта. По умолчанию содержит ('pyproject.toml', 'requirements.txt', '.git').

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена, иначе — директорию текущего файла.

**Вызывает исключения**:

-  Не вызывает исключений.

## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта, полученный с помощью функции `set_project_root()`.


### `settings`

**Описание**: Словарь, содержащий настройки проекта, загруженные из файла `settings.json` в директории проекта. Если файл не найден или содержит некорректные данные, значение по умолчанию - `None`.

**Тип**: dict | None

### `doc_str`

**Описание**: Строка, содержащая описание проекта, полученная из файла `README.MD` в директории проекта. Если файл не найден или содержит некорректные данные, значение по умолчанию - `None`.

**Тип**: str | None

### `__project_name__`

**Описание**: Название проекта, полученное из настроек (словаря `settings`).  Если `settings` - None или ключ `project_name` отсутствует, используется значение по умолчанию 'hypotez'.


### `__version__`

**Описание**: Версия проекта, полученная из настроек (словаря `settings`).  Если `settings` - None или ключ `version` отсутствует, используется значение по умолчанию ''.

**Тип**: str

### `__doc__`

**Описание**:  Описание проекта, полученное из файла `README.MD`. Если `doc_str` - None, то используется значение по умолчанию ''.

**Тип**: str

### `__details__`

**Описание**: Подробности о проекте, полученные из настроек (словаря `settings`). Если `settings` - None или ключ `details` отсутствует, используется значение по умолчанию ''.

**Тип**: str

### `__author__`

**Описание**: Автор проекта, полученный из настроек (словаря `settings`). Если `settings` - None или ключ `author` отсутствует, используется значение по умолчанию ''.

**Тип**: str

### `__copyright__`

**Описание**: Авторские права на проект, полученные из настроек (словаря `settings`). Если `settings` - None или ключ `copyright` отсутствует, используется значение по умолчанию ''.

**Тип**: str

### `__cofee__`

**Описание**: Ссылка на поддержку разработчика (платформа boosty). Получено из настроек (словаря `settings`). Если `settings` - None или ключ `cofee` отсутствует, используется значение по умолчанию.

**Тип**: str