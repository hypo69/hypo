# Модуль hypotez/src/suppliers/ebay/header.py

## Обзор

Этот модуль содержит функции для определения корневой директории проекта и загрузки настроек из файла `settings.json`. Он также предоставляет переменные, содержащие информацию о проекте, такую как название, версия, описание и др.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с текущего файла, поднимаясь по дереву директорий. Останавливается на первой директории, содержащей один из файлов или директорий из списка `marker_files`.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, по которым определяется корневая директория проекта. По умолчанию: `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена, иначе - директория, где расположен текущий файл.

**Вызывает исключений**:

- Нет


### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с текущего файла, поднимаясь по дереву директорий. Останавливается на первой директории, содержащей один из файлов или директорий из списка `marker_files`.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, по которым определяется корневая директория проекта. По умолчанию: `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена, иначе - директория, где расположен текущий файл.

**Вызывает исключений**:

- Нет


## Переменные

### `__root__`

**Описание**:  Путь к корневой директории проекта, полученный с помощью функции `set_project_root`.

**Тип**: `Path`


### `settings`

**Описание**: Словарь с настройками проекта, загруженный из файла `settings.json`.

**Тип**: `dict` или `None`

**Обработка ошибок**:

В случае `FileNotFoundError` или `json.JSONDecodeError` при чтении файла `settings.json`, переменная `settings` будет иметь значение `None`.

### `doc_str`

**Описание**: Строка с текстом документации, прочитанная из файла `README.MD`.

**Тип**: `str` или `None`

**Обработка ошибок**:

В случае `FileNotFoundError` или `json.JSONDecodeError` при чтении файла `README.MD`, переменная `doc_str` будет иметь значение `None`.


### `__project_name__`

**Описание**: Название проекта, полученное из настроек (`settings`). По умолчанию: `hypotez`.

**Тип**: `str`

### `__version__`

**Описание**: Версия проекта, полученная из настроек (`settings`). По умолчанию: пустая строка.

**Тип**: `str`

### `__doc__`

**Описание**: Документация проекта, полученная из настроек (`settings`). По умолчанию: пустая строка.

**Тип**: `str`


### `__details__`

**Описание**: Подробная информация о проекте. По умолчанию: пустая строка.

**Тип**: `str`

### `__author__`

**Описание**: Автор проекта, полученный из настроек (`settings`). По умолчанию: пустая строка.

**Тип**: `str`

### `__copyright__`

**Описание**: Авторские права проекта, полученные из настроек (`settings`). По умолчанию: пустая строка.

**Тип**: `str`

### `__cofee__`

**Описание**: Ссылка на страницу для поддержки разработчика.

**Тип**: `str`