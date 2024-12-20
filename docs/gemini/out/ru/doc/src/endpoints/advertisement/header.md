# Модуль hypotez/src/endpoints/advertisement/header.py

## Обзор

Данный модуль содержит функции для работы с настройками проекта, версии и документацией.  Он находит корневую директорию проекта, загружает настройки из файла `settings.json`, и, при необходимости, читает описание из файла `README.MD`.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла и проходя вверх по дереву каталогов.  Останавливается на первой директории, содержащей один из заданных файлов (например, `pyproject.toml`, `requirements.txt`, `.git`).

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или каталогов, используемых для определения корневой директории проекта. По умолчанию это `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена, иначе путь к директории, где находится текущий скрипт.


**Пример использования**:
```python
root_path = set_project_root()
print(root_path)
```

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла и проходя вверх по дереву каталогов.  Останавливается на первой директории, содержащей один из заданных файлов (например, `pyproject.toml`, `requirements.txt`, `.git`).

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или каталогов, используемых для определения корневой директории проекта. По умолчанию это `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена, иначе путь к директории, где находится текущий скрипт.

**Возможные исключения**:

* Нету: Никакие исключения не описаны.

## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта.

**Тип**: `Path`

**Примечание**:  Эта переменная инициализируется вызовом функции `set_project_root()`.

### `settings`

**Описание**: Словарь с настройками проекта, загруженными из файла `settings.json`.

**Тип**: `dict`


**Возможные исключения**:

- `FileNotFoundError`: Если файл `settings.json` не найден.
- `json.JSONDecodeError`: Если содержимое файла `settings.json` не является валидным JSON.

### `doc_str`

**Описание**: Строка с описанием проекта, загруженная из файла `README.MD`.

**Тип**: `str`

**Возможные исключения**:

- `FileNotFoundError`: Если файл `README.MD` не найден.
- `json.JSONDecodeError`: Если содержимое файла `README.MD` не является валидным текстом (вполне возможно, это вообще не ошибка, и просто файл не найден).

### `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`

**Описание**: Переменные, содержащие значения из настроек проекта (settings).

**Тип**: `str`


**Примечание**: Значения из настроек проекта (settings) взяты по умолчанию (используя `settings.get()`), если соответствующий ключ не найден.