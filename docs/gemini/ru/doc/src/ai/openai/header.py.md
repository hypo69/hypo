# Модуль `src.logger.header`

## Обзор

Модуль `src.logger.header` определяет корневой путь к проекту. Все импорты строятся относительно этого пути.

## Содержание

- [Функции](#Функции)
    - [`set_project_root`](#set_project_root)
- [Переменные](#Переменные)
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

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла, ища вверх и останавливаясь на первой директории, содержащей любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Имена файлов или директорий для идентификации корневой директории проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если она найдена, иначе - директория, где расположен скрипт.

## Переменные
### `__root__`
**Описание**: Путь к корневой директории проекта.

### `settings`
**Описание**: Словарь настроек проекта, загруженный из файла `settings.json`.
Содержит различные параметры проекта, такие как имя проекта, версия и т. д.

### `doc_str`
**Описание**: Строка, содержащая содержимое файла `README.MD` проекта.

### `__project_name__`
**Описание**: Имя проекта, извлеченное из `settings.json` или `'hypotez'` по умолчанию.

### `__version__`
**Описание**: Версия проекта, извлеченная из `settings.json` или `''` по умолчанию.

### `__doc__`
**Описание**: Описание проекта, взятое из файла `README.MD` или `''` по умолчанию.

### `__details__`
**Описание**: Детальное описание проекта, в данный момент пустое `''`.

### `__author__`
**Описание**: Автор проекта, извлеченный из `settings.json` или `''` по умолчанию.

### `__copyright__`
**Описание**: Информация об авторских правах проекта, извлеченная из `settings.json` или `''` по умолчанию.

### `__cofee__`
**Описание**: Сообщение с предложением поддержать разработчика чашкой кофе, взятое из `settings.json` или сообщение по умолчанию.