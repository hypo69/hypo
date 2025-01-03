# Модуль `header`

## Обзор

Модуль `header` предназначен для установки корневой директории проекта и добавления ее в `sys.path`, что позволяет корректно импортировать модули внутри проекта.

## Оглавление

1. [Функции](#Функции)
    - [`set_project_root`](#set_project_root)
2. [Переменные](#Переменные)
    - [`__root__`](#__root__)

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с текущей директории файла, и поднимаясь вверх, пока не найдет один из маркерных файлов.

**Параметры**:
- `marker_files` (tuple, optional): Имена файлов или директорий для идентификации корневой директории. По умолчанию `('__root__', 'pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если найдена, иначе директория, где находится скрипт.

## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта. Инициализируется путем вызова функции `set_project_root` с маркерным файлом `__root__`.