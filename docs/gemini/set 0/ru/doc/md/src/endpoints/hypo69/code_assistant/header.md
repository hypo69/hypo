# Модуль hypotez/src/logger/header.py

## Обзор

Модуль `src.logger` определяет корневой путь к проекту `hypotez`. Все импорты строятся относительно этого пути. В дальнейшем этот путь будет передан в системную переменную.

## Функции

### `set_project_root`

**Описание**: Находит корневой каталог проекта, начиная с текущего файла, ищет вверх по каталогам и останавливается на первом каталоге, содержащем один из указанных маркеров файлов.

**Параметры**:

- `marker_files` (tuple): Список имен файлов или каталогов, используемых для определения корневого каталога проекта. По умолчанию - `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневому каталогу проекта, если найден, иначе - путь к каталогу, где находится скрипт.


**Вызывает исключения**:

- Нет

## Переменные

### `__root__`

**Описание**: Путь к корневому каталогу проекта, полученный с помощью функции `set_project_root()`.

**Тип**: `Path`

## Блок кода

**Описание**: Блок кода для загрузки настроек из файла `settings.json` и документации из файла `README.MD`


**Обработка исключений**:

- `FileNotFoundError`: Возникает, если файлы `settings.json` или `README.MD` не найдены.
- `json.JSONDecodeError`: Возникает, если содержимое `settings.json` не является корректным JSON.

## Переменные (константы)

### `MODE`

**Описание**: Строковая переменная, хранящая текущий режим работы (`'dev'`).

### `__project_name__`

**Описание**: Название проекта. Получается из `settings.json` (ключ `"project_name"`), если доступен, иначе - `'hypotez'`.

### `__version__`

**Описание**: Версия проекта. Получается из `settings.json` (ключ `"version"`), если доступен, иначе - пустая строка.

### `__doc__`

**Описание**: Документация проекта. Получается из `README.MD`, если доступен, иначе - пустая строка.

### `__details__`

**Описание**: Дополнительные подробности. По умолчанию пустая строка.

### `__author__`

**Описание**: Автор проекта. Получается из `settings.json` (ключ `"author"`), если доступен, иначе - пустая строка.

### `__copyright__`

**Описание**: Авторские права. Получается из `settings.json` (ключ `"copyright"`), если доступен, иначе - пустая строка.

### `__cofee__`

**Описание**: Ссылка на Boosty для поддержки разработчика. Получается из `settings.json` (ключ `"cofee"`), если доступен, иначе - строка с ссылкой по умолчанию.


## Импорты

- `sys`
- `json`
- `packaging.version`
- `pathlib`
- `src.gs`