# Модуль hypotez/src/goog/text_to_speech/header.py

## Обзор

Этот модуль содержит функции для определения корневой директории проекта, загрузки настроек из файла `settings.json` и получения документации из файла `README.MD`. Он также определяет переменные, содержащие информацию о проекте, такие как название, версия, описание и автор.

## Функции

### `set_project_root`

**Описание**: Определяет корневую директорию проекта, начиная с директории текущего файла и двигаясь вверх по дереву директорий, пока не найдёт директорию содержащую один из файлов-маркеров (pyproject.toml, requirements.txt, .git).

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или директорий, используемых для определения корневой директории проекта. По умолчанию: ('pyproject.toml', 'requirements.txt', '.git').

**Возвращает**:

- `Path`: Путь к корневой директории проекта. Если корневая директория не найдена, возвращает директорию, в которой расположен данный скрипт.

**Вызывает исключения**:

- Нет.


## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта.


### `settings`

**Описание**: Словарь, содержащий настройки проекта, загруженные из файла `settings.json`.


### `doc_str`

**Описание**: Строка, содержащая текст документации, загруженный из файла `README.MD`.


### `__project_name__`

**Описание**: Имя проекта, взятое из настроек `settings`. По умолчанию: `hypotez`.


### `__version__`

**Описание**: Версия проекта, взятая из настроек `settings`. По умолчанию: `''`.


### `__doc__`

**Описание**: Текст документации, взятый из файла `README.MD`. По умолчанию: `''`.


### `__details__`

**Описание**:  Дополнительные детали проекта. По умолчанию: `''`.


### `__author__`

**Описание**: Автор проекта, взятый из настроек `settings`. По умолчанию: `''`.


### `__copyright__`

**Описание**: Авторские права проекта, взятые из настроек `settings`. По умолчанию: `''`.


### `__cofee__`

**Описание**: Ссылка для поддержки разработчика. По умолчанию: "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"


## Обработка исключений

Этот модуль использует обработку исключений для безопасного обращения с файлами настроек и файлом README. При возникновении ошибок `FileNotFoundError` или `json.JSONDecodeError` соответствующие переменные (settings, doc_str) устанавливаются в None или пустые строки, предотвращая ошибку программы.