# Модуль `header.py`

## Обзор

Модуль `header.py` содержит определения для работы с путями, загрузки настроек и извлечения информации о проекте.

## Оглавление

- [Функции](#Функции)
    - [`set_project_root`](#set_project_root)
- [Глобальные переменные](#Глобальные-переменные)
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

**Описание**: Находит корневой каталог проекта, начиная с каталога текущего файла, и ищет вверх, останавливаясь на первом каталоге, содержащем один из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple, optional): Имена файлов или каталогов, идентифицирующих корень проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневому каталогу, если найден, иначе каталог, где находится скрипт.

## Глобальные переменные

### `__root__`
**Описание**: Путь к корневому каталогу проекта.

### `settings`
**Описание**: Словарь с настройками проекта, загруженный из файла `settings.json`. Может быть `None`, если файл не найден или не может быть декодирован.

### `doc_str`
**Описание**: Строка, содержащая содержимое файла `README.md`. Может быть `None`, если файл не найден или не может быть прочитан.

### `__project_name__`
**Описание**: Название проекта, извлекаемое из файла настроек `settings.json`. Если файла нет, то по умолчанию установлено значение `hypotez`.

### `__version__`
**Описание**: Версия проекта, извлекаемая из файла настроек `settings.json`. Если файла нет, то по умолчанию установлена пустая строка.

### `__doc__`
**Описание**: Строка, содержащая документацию из файла `README.md`. Если файл не найден, то по умолчанию установлена пустая строка.

### `__details__`
**Описание**: Строка с дополнительной информацией. По умолчанию пустая строка.

### `__author__`
**Описание**: Имя автора проекта, извлекаемое из файла настроек `settings.json`. Если файла нет, то по умолчанию установлена пустая строка.

### `__copyright__`
**Описание**: Информация об авторских правах, извлекаемая из файла настроек `settings.json`. Если файла нет, то по умолчанию установлена пустая строка.

### `__cofee__`
**Описание**: Сообщение для поощрения разработчика чашкой кофе, извлекаемое из файла настроек `settings.json`. Если файла нет, то по умолчанию установлено сообщение "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"