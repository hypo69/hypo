# Модуль hypotez/src/suppliers/kualastyle/header.py

## Обзор

Этот модуль содержит функции для определения корневой директории проекта и загрузки настроек из файла `settings.json`. Он также предоставляет доступ к документации, хранящейся в файле `README.MD`.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная от директории текущего файла и идя вверх по иерархии директорий. Останавливается на первой директории, содержащей один из заданных файлов или директорий (например, `pyproject.toml`, `requirements.txt`, `.git`).

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или директорий, используемых для определения корневой директории проекта. По умолчанию включает `'pyproject.toml'`, `'requirements.txt'`, `.git`.

**Возвращает**:

- `Path`: Путь к корневой директории проекта. Если корневая директория не найдена, возвращает директорию текущего файла.

**Вызывает исключения**:

- Нет


### Загрузка настроек

**Описание**: Загружает настройки из файла `settings.json` в переменную `settings`. Если файл не найден или содержит некорректные данные, переменная `settings` получает значение `None`. Документировано с использованием обработки исключений.

**Вызывает исключения**:

- `FileNotFoundError`: Если файл `settings.json` не найден.
- `json.JSONDecodeError`: Если файл `settings.json` содержит некорректные данные JSON.


### Загрузка документации

**Описание**: Загружает содержимое файла `README.MD` в переменную `doc_str`. Если файл не найден или содержимое некорректно, переменная `doc_str` получает значение `None`. Документировано с использованием обработки исключений.

**Вызывает исключения**:

- `FileNotFoundError`: Если файл `README.MD` не найден.
- `UnicodeDecodeError`: Если файл `README.MD` содержит некорректные данные.

## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта, полученный с помощью функции `set_project_root()`.

**Тип**: `Path`

### `__project_name__`

**Описание**: Имя проекта. Получается из настроек (`settings.json`) или имеет значение по умолчанию `'hypotez'`.

**Тип**: `str`

### `__version__`

**Описание**: Версия проекта. Получается из настроек (`settings.json`) или имеет значение по умолчанию `''`.

**Тип**: `str`

### `__doc__`

**Описание**: Содержимое файла `README.MD`. Если файл не найден или содержит некорректные данные, имеет значение `''`.

**Тип**: `str`

### `__details__`

**Описание**:  Дополнительная информация о проекте. По умолчанию пустая строка.

**Тип**: `str`

### `__author__`

**Описание**: Автор проекта. Получается из настроек (`settings.json`) или имеет значение по умолчанию `''`.

**Тип**: `str`

### `__copyright__`

**Описание**: Авторские права. Получается из настроек (`settings.json`) или имеет значение по умолчанию `''`.

**Тип**: `str`

### `__cofee__`

**Описание**: Ссылка для поддержки разработчика. Получается из настроек (`settings.json`) или имеет значение по умолчанию.

**Тип**: `str`