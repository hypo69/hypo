# Модуль hypotez/src/webdriver/playwright/header.py

## Обзор

Этот модуль содержит функции для определения корневой директории проекта и загрузки настроек из файла settings.json.  Он также позволяет получить и использовать информацию из файла README.MD.

## Функции

### `set_project_root`

**Описание**:  Находит корневой каталог проекта, начиная с текущей директории и продвигаясь вверх по иерархии директорий, пока не найдет директорию, содержащую указанные файлы-маркеры (например, `pyproject.toml`, `requirements.txt`, `.git`).

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или каталогов, которые указывают на корневой каталог проекта. По умолчанию содержит (`'pyproject.toml'`, `'requirements.txt'`, `.git`).

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если она найдена. В противном случае возвращает путь к директории, где находится текущий скрипт.

**Пример использования**:

```python
project_root = set_project_root()
print(project_root)
```

### <ins>Загрузка настроек</ins>

**Описание**:  Загружает настройки из файла `settings.json`, расположенного в корневой директории проекта.  Обрабатывает исключения `FileNotFoundError` и `json.JSONDecodeError` при отсутствии или повреждении файла.

**Используемые переменные**:
- `settings`: Словарь с настройками проекта.


### <ins>Загрузка информации из README.md</ins>

**Описание**:  Загружает содержимое файла `README.MD`, расположенного в корневой директории проекта.  Обрабатывает исключения `FileNotFoundError` и `json.JSONDecodeError` при отсутствии или повреждении файла.

**Используемые переменные**:
- `doc_str`: Строка с содержимым файла README.MD.


## Постоянные переменные

### `__root__`

**Описание**: Путь к корневой директории проекта, полученный с помощью функции `set_project_root()`.

**Тип**: `Path`

### `__project_name__`

**Описание**: Название проекта, взятое из настроек `settings.json`.  Если файл отсутствует или поле `project_name` не найдено, по умолчанию используется значение `'hypotez'`.

**Тип**: `str`

### `__version__`

**Описание**: Версия проекта, взятая из настроек `settings.json`. Если файл отсутствует или поле `version` не найдено, по умолчанию используется пустая строка.

**Тип**: `str`


### `__doc__`

**Описание**: Содержимое файла README.MD, или пустая строка, если файл отсутствует или поврежден.

**Тип**: `str`

### `__details__`

**Описание**: Подробная информация о проекте (по умолчанию пустая строка).

**Тип**: `str`

### `__author__`

**Описание**: Автор проекта, взятый из настроек `settings.json`. Если файл отсутствует или поле `author` не найдено, по умолчанию используется пустая строка.

**Тип**: `str`

### `__copyright__`

**Описание**: Авторские права проекта, взятые из настроек `settings.json`. Если файл отсутствует или поле `copyright` не найдено, по умолчанию используется пустая строка.

**Тип**: `str`


### `__cofee__`

**Описание**: Ссылка для поддержки разработчика, взятая из настроек `settings.json`. Если файл отсутствует или поле `cofee` не найдено, по умолчанию используется строка со ссылкой на Boosty.

**Тип**: `str`