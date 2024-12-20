# Модуль `src.endpoints.hypo69.code_assistant.make_summary`

## Обзор

Модуль `src.endpoints.hypo69.code_assistant.make_summary` предназначен для создания файла `SUMMARY.md`, необходимого для компиляции документации с помощью `mdbook`. Он рекурсивно обходит указанную директорию, и на основе найденных `.md` файлов, формирует файл `SUMMARY.md` со структурой глав.

## Содержание

1. [Функции](#Функции)
   - [`make_summary`](#make_summary)
   - [`_make_summary`](#_make_summary)
   - [`prepare_summary_path`](#prepare_summary_path)

## Функции

### `make_summary`

**Описание**: Создает файл `SUMMARY.md`, рекурсивно обходя папку.

**Параметры**:
- `docs_dir` (Path): Путь к исходной директории `docs`.

**Возвращает**:
- `None`: Функция ничего не возвращает.

### `_make_summary`

**Описание**: Рекурсивно обходит папку и создает файл `SUMMARY.md` с главами на основе `.md` файлов.

**Параметры**:
- `src_dir` (Path): Путь к папке с исходниками `.md`.
- `summary_file` (Path): Путь для сохранения файла `SUMMARY.md`.

**Возвращает**:
- `bool`: `True` в случае успешного создания файла, в противном случае ничего не возвращает.

**Вызывает исключения**:
- `Exception`: Выводит сообщение об ошибке при создании файла `summary.md`.

### `prepare_summary_path`

**Описание**: Формирует путь к файлу, заменяя часть пути `src` на `docs` и добавляя имя файла.

**Параметры**:
- `src_dir` (Path): Исходный путь с `src`.
- `file_name` (str, optional): Имя файла, который нужно создать. По умолчанию `SUMMARY.md`.

**Возвращает**:
- `Path`: Новый путь к файлу.