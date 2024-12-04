# Модуль hypotez/src/templates/version.py

## Обзор

Этот модуль содержит переменные, определяющие версию проекта и другие метаданные. Он загружает настройки из файла `../settings.json` и, в случае его отсутствия или ошибки при чтении, использует значения по умолчанию.

## Переменные

### `MODE`

**Описание**: Строковая переменная, хранящая режим работы (например, `dev`, `prod`).  Значение по умолчанию `'dev'`.

### `__project_name__`

**Описание**: Строковая переменная, хранящая имя проекта.  Значение берется из настроек `settings.json` с ключом `project_name`. По умолчанию `'hypotez'`.

### `__version__`

**Описание**: Строковая переменная, хранящая версию проекта. Значение берется из настроек `settings.json` с ключом `version`. По умолчанию пустая строка.

### `__doc__`

**Описание**: Строковая переменная, хранящая документацию проекта.  По умолчанию пустая строка.

### `__details__`

**Описание**: Строковая переменная, хранящая дополнительные детали о проекте. По умолчанию пустая строка.

### `__author__`

**Описание**: Строковая переменная, хранящая имя автора проекта.  Значение берется из настроек `settings.json` с ключом `author`. По умолчанию пустая строка.

### `__copyright__`

**Описание**: Строковая переменная, хранящая авторские права проекта.  Значение берется из настроек `settings.json` с ключом `copyright`. По умолчанию пустая строка.

### `__cofee__`

**Описание**: Строковая переменная, содержащая ссылку для поддержки разработчика.  Значение берется из настроек `settings.json` с ключом `cofee`. По умолчанию ссылка на Boosty.


## Функции

### `None`

**Описание**: Модуль не содержит функций.


## Обработка исключений

### Чтение файла настроек

**Описание**: При попытке чтения файла `../settings.json` могут возникнуть следующие исключения:

- `FileNotFoundError`: Если файл `../settings.json` не найден.
- `json.JSONDecodeError`: Если содержимое файла `../settings.json` не является корректным JSON-объектом.

В случае возникновения этих исключений, значения переменных будут установлены по умолчанию.


```
```
```python
import json

settings: dict = None

try:
    with open('../settings.json', 'r') as settings_file:
        settings = json.load(settings_file)
except (FileNotFoundError, json.JSONDecodeError):
    pass  # Обработка исключений


__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
__version__: str = settings.get("version", '') if settings else ''
__doc__: str = ''
__details__: str = ''
__author__: str = settings.get("author", '') if settings else ''
__copyright__: str = settings.get("copyright", '') if settings else ''
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"