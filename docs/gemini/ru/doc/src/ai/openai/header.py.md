# src.logger.header

## Обзор

Модуль определяет корневой путь к проекту. Все импорты строятся относительно этого пути.
В дальнейшем планируется перенести определение корневого пути в системную переменную.

## Оглавление

- [Функции](#функции)
    - [`set_project_root`](#set_project_root)

- [Переменные](#переменные)
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

**Описание**: Находит корневой каталог проекта, начиная с каталога текущего файла,
поиском вверх и останавливаясь на первом каталоге, содержащем любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Имена файлов или каталогов для идентификации корня проекта. По умолчанию `('__root__','.git')`.

**Возвращает**:
- `Path`: Путь к корневому каталогу, если он найден, в противном случае - каталог, в котором находится скрипт.

## Переменные
### `__root__`
**Описание**: Путь к корневому каталогу проекта.
### `settings`
**Описание**:  Словарь настроек, загруженных из файла `settings.json`, расположенного в каталоге `src` корневого каталога. Значение `None`, если произошла ошибка при чтении файла или при разборе JSON.
### `doc_str`
**Описание**: Строка с содержимым файла `README.MD`, расположенного в каталоге `src` корневого каталога. Значение `None`, если произошла ошибка при чтении файла.
### `__project_name__`
**Описание**: Название проекта, загруженное из настроек или `hypotez` по умолчанию
### `__version__`
**Описание**: Версия проекта, загруженная из настроек или пустая строка по умолчанию.
### `__doc__`
**Описание**: Строка документации проекта, загруженная из `README.MD` или пустая строка по умолчанию.
### `__details__`
**Описание**: Строка с дополнительной информацией о проекте. Значение по умолчанию — пустая строка.
### `__author__`
**Описание**: Автор проекта, загруженный из настроек или пустая строка по умолчанию.
### `__copyright__`
**Описание**: Информация о копирайте проекта, загруженная из настроек или пустая строка по умолчанию.
### `__cofee__`
**Описание**: Строка с призывом угостить разработчика чашечкой кофе, загруженная из настроек или строка по умолчанию: "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69".