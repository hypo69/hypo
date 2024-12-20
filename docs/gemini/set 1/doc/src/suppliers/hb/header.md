# Модуль hypotez/src/suppliers/hb/header.py

## Обзор

Этот модуль содержит функции для определения корневого каталога проекта и загрузки настроек из файла `settings.json`. Он также загружает содержимое файла `README.MD` для использования в других частях проекта.

## Функции

### `set_project_root`

**Описание**: Находит корневой каталог проекта, начиная с текущего файла, ищет вверх по дереву каталогов, пока не найдет каталог, содержащий один из указанных файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Кортеж имен файлов или каталогов, которые используются для определения корневого каталога проекта. По умолчанию: `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:
- `Path`: Путь к корневому каталогу проекта, если он найден, иначе – путь к каталогу, в котором находится текущий скрипт.

**Обрабатывает исключения**:
- Нет.

### Загрузка настроек из файла `settings.json`

**Описание**: Загружает настройки из файла `settings.json`, расположенного в корневом каталоге проекта.

**Обрабатывает исключения**:
- `FileNotFoundError`: Если файл `settings.json` не найден.
- `json.JSONDecodeError`: Если файл `settings.json` имеет неправильный формат JSON.

### Загрузка документации из файла `README.MD`

**Описание**: Загружает содержимое файла `README.MD` из корневого каталога проекта.

**Обрабатывает исключения**:
- `FileNotFoundError`: Если файл `README.MD` не найден.
- `UnicodeDecodeError`: Если файл `README.MD` имеет неправильное кодирование.


## Переменные

### `__root__`

**Описание**: Путь к корневому каталогу проекта.


### `settings`

**Описание**: Словарь настроек, загруженных из файла `settings.json`.


### `doc_str`

**Описание**: Содержимое файла `README.MD`, загруженное из корневого каталога проекта.


### `__project_name__`

**Описание**: Название проекта, полученное из файла `settings.json`. По умолчанию `'hypotez'`.


### `__version__`

**Описание**: Версия проекта, полученная из файла `settings.json`. По умолчанию пустая строка.


### `__doc__`

**Описание**: Документация проекта, полученная из файла `README.MD`. По умолчанию пустая строка.


### `__details__`

**Описание**: Дополнительные детали проекта. По умолчанию пустая строка.


### `__author__`

**Описание**: Автор проекта, полученный из файла `settings.json`. По умолчанию пустая строка.


### `__copyright__`

**Описание**: Авторские права проекта, полученные из файла `settings.json`. По умолчанию пустая строка.


### `__cofee__`

**Описание**: Ссылка на возможность поддержать разработчика. По умолчанию ссылка на Boosty.