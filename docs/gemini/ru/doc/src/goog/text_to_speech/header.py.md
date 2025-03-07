# Модуль `header.py`

## Обзор

Модуль `header.py` предназначен для определения корневой директории проекта, загрузки настроек из файла `settings.json`, чтения документации из `README.MD` и определения основных метаданных проекта, таких как название, версия, автор и т.д.

## Оглавление

- [Функции](#функции)
    - [`set_project_root`](#set_project_root)
- [Глобальные переменные](#глобальные-переменные)
    - [`__root__`](#__root__)
    - [`settings`](#settings)
    - [`doc_str`](#doc_str)
    - [`__project_name__`](#__project_name__)
    - [`__version__`](#__version__)
    - [`__doc__`](#__doc__)
    - [`__details__`](#__details__)
    - [`__author__`](#__author__)
    - [`__copyright__`](#__copyright__)
    - [`__cofee__`](#__cofee__)
## Функции

### `set_project_root`

**Описание**: Находит корневой каталог проекта, начиная с каталога текущего файла, и поднимаясь вверх, пока не найдет каталог, содержащий любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Имена файлов или каталогов для идентификации корневого каталога проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневому каталогу, если он найден, иначе каталог, в котором находится скрипт.

### Глобальные переменные
#### `__root__`
**Описание**: Путь к корневой директории проекта.

#### `settings`
**Описание**: Словарь с настройками, загруженными из файла `settings.json`.

#### `doc_str`
**Описание**: Строка с документацией, прочитанной из файла `README.MD`.

#### `__project_name__`
**Описание**: Название проекта. По умолчанию 'hypotez'.

#### `__version__`
**Описание**: Версия проекта.

#### `__doc__`
**Описание**: Строка с документацией проекта.

#### `__details__`
**Описание**: Детали проекта.

#### `__author__`
**Описание**: Автор проекта.

#### `__copyright__`
**Описание**: Авторские права проекта.

#### `__cofee__`
**Описание**: Строка с предложением угостить разработчика кофе.