# Модуль `hypotez/src/webdriver/crawlee_python/header.py`

## Обзор

Этот модуль содержит вспомогательные функции для работы с проектом `hypotez`. Он определяет корневую директорию проекта, загружает настройки из файла `settings.json` и содержит информацию о проекте (название, версия, описание и т.д.).

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная от текущей директории скрипта. Поиск происходит вверх по директориям до тех пор, пока не найдена директория, содержащая один из указанных файлов-маркеров.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, используемых для идентификации корневой директории проекта. По умолчанию: `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена, иначе - путь к текущей директории.


**Пример использования**:

```python
root_path = set_project_root()
print(root_path)
```

## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта, полученный с помощью функции `set_project_root()`.

**Тип**: `Path`

### `settings`

**Описание**: Словарь с настройками проекта, загруженный из файла `settings.json`.

**Тип**: `dict`

**Примечания**: Может быть `None`, если файл `settings.json` не найден или содержит некорректные данные.

### `doc_str`

**Описание**: Текст из файла `README.MD`, описывающий проект.

**Тип**: `str`


**Примечания**: Может быть `None`, если файл `README.MD` не найден или содержит некорректные данные.

### `__project_name__`

**Описание**: Название проекта, полученное из `settings` или установленное по умолчанию.

**Тип**: `str`

### `__version__`

**Описание**: Версия проекта, полученная из `settings` или пустая строка по умолчанию.

**Тип**: `str`


### `__doc__`

**Описание**: Документация проекта, полученная из `doc_str` или пустая строка по умолчанию.

**Тип**: `str`

### `__details__`

**Описание**: Подробное описание проекта (пустая строка по умолчанию).

**Тип**: `str`

### `__author__`

**Описание**: Автор проекта, полученный из `settings` или пустая строка по умолчанию.

**Тип**: `str`


### `__copyright__`

**Описание**: Авторские права проекта, полученный из `settings` или пустая строка по умолчанию.

**Тип**: `str`


### `__cofee__`

**Описание**: Ссылка для поддержки автора проекта.

**Тип**: `str`

**Примечания**: Полученный из `settings` или строка по умолчанию.