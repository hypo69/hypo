# Модуль `hypotez/src/suppliers/morlevi/header.py`

## Обзор

Этот модуль содержит функции для определения корневой директории проекта и загрузки настроек из файла `settings.json`. Он также предоставляет доступ к документации, содержащейся в файле `README.MD`, и к дополнительным метаданным о проекте.

## Функции

### `set_project_root`

**Описание**: Определяет корневую директорию проекта, начиная с директории текущего файла и идя вверх по дереву директорий, пока не найдет директорию, содержащую один из указанных файлов или папок (например, `pyproject.toml`, `requirements.txt`, `.git`).

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, которые используются для определения корневой директории проекта. По умолчанию содержит ('pyproject.toml', 'requirements.txt', '.git').

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если она найдена. В противном случае возвращает директорию, в которой находится текущий файл.

**Вызывает исключения**:

- Не вызывает исключений.


## Переменные

### `__root__`

**Описание**: Переменная, содержащая путь к корневой директории проекта. Присваивается значением, возвращаемым функцией `set_project_root()`.


## Инициализация переменных

**Описание**: Загружает настройки проекта из файла `settings.json` и документацию из `README.MD`, если они существуют. В случае ошибок, такие как отсутствие файла или некорректный формат JSON, переменные устанавливаются в `None` или пустую строку соответственно.


### `settings`

**Описание**: Словарь с настройками проекта, загруженный из файла `settings.json`.

**Возможные значения**:
- Словарь: если файл `settings.json` существует и содержит корректный JSON.
- `None`: если файл `settings.json` не найден или содержит некорректный JSON.

### `doc_str`

**Описание**: Строка с документацией проекта, загруженная из файла `README.MD`.

**Возможные значения**:
- Строка: если файл `README.MD` существует и содержит корректный текст.
- `None`: если файл `README.MD` не найден или содержит некорректный текст.

## Константы

### `__project_name__`

**Описание**: Название проекта. Значение берется из настроек, если доступны, иначе используется значение `'hypotez'`.

**Возможные значения**:
- Строка: наименование проекта.


### `__version__`

**Описание**: Версия проекта. Значение берется из настроек, если доступны, иначе используется пустая строка.

**Возможные значения**:
- Строка: версия проекта.


### `__doc__`

**Описание**: Документация проекта. Значение берется из переменной `doc_str` или пустая строка.

**Возможные значения**:
- Строка: документация проекта.


### `__details__`

**Описание**: Дополнительные детали о проекте. По умолчанию пустая строка.


### `__author__`

**Описание**: Автор проекта. Значение берется из настроек, если доступны, иначе пустая строка.


### `__copyright__`

**Описание**: Авторские права на проект. Значение берется из настроек, если доступны, иначе пустая строка.


### `__cofee__`

**Описание**: Ссылка для поддержки разработчика. Значение берется из настроек, если доступны, иначе используется значение по умолчанию.