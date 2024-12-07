# Модуль `hypotez/src/endpoints/hypo69/small_talk_bot/header.py`

## Обзор

Этот модуль содержит вспомогательные функции для определения корневого каталога проекта, загрузки настроек из файла `settings.json` и чтения файла `README.MD`.  Он также инициализирует переменные, представляющие имя проекта, версию, документацию, детали, автора, копирайт и ссылку на пожертвования.

## Функции

### `set_project_root`

**Описание**:  Находит корневую директорию проекта, начиная с директории текущего файла, ищет вверх по дереву директорий, пока не найдет директорию, содержащую один из указанных файлов-маркеров.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, по которым определяется корневая директория проекта. По умолчанию содержит `('pyproject.toml', 'requirements.txt', '.git')`.


**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена, в противном случае директория, где расположен скрипт.


**Вызывает исключения**:

- Нет


### `set_project_root`

**Описание**:  Находит корневую директорию проекта, начиная с директории текущего файла, ищет вверх по дереву директорий, пока не найдет директорию, содержащую один из указанных файлов-маркеров.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, по которым определяется корневая директория проекта. По умолчанию содержит `('pyproject.toml', 'requirements.txt', '.git')`.


**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена, в противном случае директория, где расположен скрипт.


**Вызывает исключения**:

- Нет


## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта, полученный функцией `set_project_root`. Тип: `Path`.

### `settings`

**Описание**: Словарь настроек проекта, загруженный из файла `settings.json`. Тип: `dict`. Возможные значения: `None`.

### `doc_str`

**Описание**: Строка, содержащая содержимое файла `README.MD`. Тип: `str`. Возможные значения: `None`.


### `__project_name__`

**Описание**: Имя проекта, полученное из настроек. Тип: `str`. По умолчанию: `'hypotez'`.

### `__version__`

**Описание**: Версия проекта, полученная из настроек. Тип: `str`. По умолчанию: `''`.

### `__doc__`

**Описание**: Документация проекта, полученная из файла `README.MD`. Тип: `str`. По умолчанию: `''`.

### `__details__`

**Описание**: Детали проекта. Тип: `str`. По умолчанию: `''`.

### `__author__`

**Описание**: Автор проекта, полученный из настроек. Тип: `str`. По умолчанию: `''`.

### `__copyright__`

**Описание**: Копирайт проекта, полученный из настроек. Тип: `str`. По умолчанию: `''`.

### `__cofee__`

**Описание**: Ссылка на пожертвования автору проекта. Тип: `str`. По умолчанию: `Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69`.