# Модуль `hypotez/src/suppliers/aliexpress/header.py`

## Обзор

Этот модуль содержит функцию `set_project_root` для определения корневой директории проекта.  Также он загружает настройки из файла `settings.json` в переменную `settings`.

## Функции

### `set_project_root`

**Описание**: Определяет корневую директорию проекта, начиная с директории текущего файла. Поиск происходит вверх по директориям, пока не будет найдена директория, содержащая один из файлов, указанных в аргументе `marker_files`.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, используемых для определения корневой директории проекта. По умолчанию (`('pyproject.toml', 'requirements.txt', '.git')`).

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена. В противном случае возвращает директорию, в которой расположен скрипт.

**Вызывает исключения**:

-  Не вызывает никаких исключений.


### Загрузка настроек

**Описание**: Загружает настройки из файла `settings.json` в переменную `settings`.  Если файл не найден или содержит невалидный JSON, происходит обработка исключения `FileNotFoundError` или `json.JSONDecodeError`, и переменная `settings` остаётся `None`.


## Переменные

### `MODE`

**Описание**: Строковая переменная, хранящая режим работы (например, `'dev'` или `'prod'`).


### `settings`

**Описание**: Словарь, содержащий настройки проекта. Инициализируется результатом загрузки из `settings.json`.  Значение `None` указывает на то, что файл `settings.json` не был загружен или некорректно отформатирован.


## Импорты

### Модули

- `sys`
- `json`
- `packaging.version`
- `pathlib`


### Модули из проекта

- `src`
- `gs`