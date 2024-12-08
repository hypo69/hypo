# Модуль hypotez/src/templates/version.py

## Обзор

Этот модуль предоставляет функции для получения информации о проекте, такой как имя проекта, версия, описание и другие метаданные.  Он считывает данные из файла `../settings.json` для персонализации информации о проекте.

## Переменные

### `MODE`

**Описание**: Переменная, хранящая режим работы (например, `dev`, `prod`). В данном случае установлено значение `'dev'`.

### `__project_name__`

**Описание**: Имя проекта. По умолчанию `'hypotez'`. Получает значение из `settings.json` или использует значение по умолчанию.

### `__version__`

**Описание**: Версия проекта. По умолчанию пустая строка. Получает значение из `settings.json` или использует значение по умолчанию.

### `__doc__`

**Описание**: Документация проекта. По умолчанию пустая строка.

### `__details__`

**Описание**: Подробное описание проекта. По умолчанию пустая строка.

### `__author__`

**Описание**: Автор проекта. По умолчанию пустая строка. Получает значение из `settings.json` или использует значение по умолчанию.

### `__copyright__`

**Описание**: Авторские права на проект. По умолчанию пустая строка. Получает значение из `settings.json` или использует значение по умолчанию.

### `__cofee__`

**Описание**: Ссылка на страницу, где можно поблагодарить автора за поддержку проекта. По умолчанию ссылка на Boosty. Получает значение из `settings.json` или использует значение по умолчанию.

### `settings`

**Описание**: Словарь с настройками проекта, загруженный из файла `../settings.json`.


## Функции

### `None`

Этот модуль не содержит функций в классическом понимании. Он определяет константы и переменные, используемые для представления метаданных проекта.


## Обработка исключений

### Файл `../settings.json` не найден или некорректен

**Описание**: При попытке открытия файла `../settings.json` могут возникнуть исключения `FileNotFoundError` или `json.JSONDecodeError`.  Эти исключения обрабатываются, и в случае возникновения модуль использует значения по умолчанию для метаданных проекта.


```
```
```python
import json


settings: dict = None


try:
    with open('../settings.json', 'r') as settings_file:
        settings = json.load(settings_file)
except (FileNotFoundError, json.JSONDecodeError):
    ...


__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
__version__: str = settings.get("version", '') if settings else ''
__doc__: str = ''
__details__: str = ''
__author__: str = settings.get("author", '') if settings else ''
__copyright__: str = settings.get("copyright", '') if settings else ''
__cofee__: str = settings.get("coffee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"


```