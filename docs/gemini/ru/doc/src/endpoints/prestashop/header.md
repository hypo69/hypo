# Модуль `hypotez/src/logger/header.py`

## Обзор

Данный модуль определяет корневой путь к проекту `hypotez`. Все импорты строятся относительно этого пути.  В будущем этот путь будет переноситься в системную переменную.

## Функции

### `set_project_root`

**Описание**:  Находит корневой каталог проекта, начиная с текущей директории и поднимаясь вверх по иерархии директорий до первой директории, содержащей указанные файлы-маркеры.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, которые используются для определения корневого каталога проекта. По умолчанию: `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневому каталогу проекта, если найден, иначе - путь к текущей директории.


**Вызывает исключения**:

-  Никаких исключений не генерирует.


## Переменные

### `__root__`

**Описание**: Путь к корневому каталогу проекта, полученный с помощью функции `set_project_root()`.

**Тип**: `Path`

**Значение**:  Результат вызова `set_project_root()`.

### `settings`

**Описание**: Словарь со значениями настроек проекта, загруженный из файла `settings.json`.

**Тип**: `dict`

**Значение**:  Загруженный из файла `settings.json` или `None`, если файл не найден или содержит некорректные данные.

### `doc_str`

**Описание**: Строка с содержимым файла `README.MD`.

**Тип**: `str`

**Значение**: Содержимое файла `README.MD` или `None`, если файл не найден или содержит некорректные данные.


### `__project_name__`

**Описание**: Название проекта.

**Тип**: `str`

**Значение**: Значение ключа `"project_name"` в `settings`, если он существует, иначе `'hypotez'`.

### `__version__`

**Описание**: Версия проекта.

**Тип**: `str`

**Значение**: Значение ключа `"version"` в `settings`, если он существует, иначе `''`.

### `__doc__`

**Описание**: Документация проекта.

**Тип**: `str`

**Значение**: Содержимое файла `README.MD` если он доступен, иначе `''`.


### `__details__`

**Описание**:  Дополнительные детали.

**Тип**: `str`

**Значение**: Пустая строка (`''`).

### `__author__`

**Описание**: Автор проекта.

**Тип**: `str`

**Значение**: Значение ключа `"author"` в `settings`, если он существует, иначе `''`.

### `__copyright__`

**Описание**: Авторские права.

**Тип**: `str`

**Значение**: Значение ключа `"copyright"` в `settings`, если он существует, иначе `''`.

### `__cofee__`

**Описание**: Ссылка для поддержки разработчика.

**Тип**: `str`

**Значение**: Значение ключа `"cofee"` в `settings`, если он существует, иначе строка с ссылкой.