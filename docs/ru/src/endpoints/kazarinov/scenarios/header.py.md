# Модуль `header.py`

## Обзор

Модуль `header.py` содержит общие настройки и метаданные проекта, а также функции для определения корневой директории проекта.

## Содержание

1. [Функции](#Функции)
    - [`set_project_root`](#set_project_root)
2. [Переменные](#Переменные)
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

**Описание**:
Находит корневую директорию проекта, начиная с директории текущего файла, идя вверх по дереву каталогов до первого каталога, содержащего один из маркеров.

**Параметры**:
- `marker_files` (tuple, optional): Кортеж имен файлов или каталогов для идентификации корневой директории проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории проекта, если она найдена, иначе директория, где расположен скрипт.

## Переменные

### `__root__`
**Описание**:
`Path` к корневой директории проекта.

### `settings`
**Описание**:
Словарь с настройками проекта, загруженный из файла `settings.json`. Может быть `None`, если файл не найден или произошла ошибка при чтении.

### `doc_str`
**Описание**:
Строка с содержимым файла `README.MD`. Может быть `None`, если файл не найден или произошла ошибка при чтении.

### `__project_name__`
**Описание**:
Имя проекта, считанное из настроек (`settings.json`) или `'hypotez'` по умолчанию.

### `__version__`
**Описание**:
Версия проекта, считанная из настроек (`settings.json`) или пустая строка по умолчанию.

### `__doc__`
**Описание**:
Содержимое файла `README.MD` или пустая строка по умолчанию.

### `__details__`
**Описание**:
Строка, предназначенная для хранения дополнительных сведений о проекте. В данном файле всегда пустая строка.

### `__author__`
**Описание**:
Автор проекта, считанный из настроек (`settings.json`) или пустая строка по умолчанию.

### `__copyright__`
**Описание**:
Информация об авторских правах, считанная из настроек (`settings.json`) или пустая строка по умолчанию.

### `__cofee__`
**Описание**:
Сообщение с предложением угостить разработчика кофе, считанное из настроек (`settings.json`) или сообщение по умолчанию.