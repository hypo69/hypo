# Модуль hypotez/src/gui/header.py

## Обзор

Данный модуль отвечает за определение корневого пути к проекту `hypotez`. Он используется для корректного импорта файлов и ресурсов,  используя системную переменную `sys.path`. Модуль также загружает настройки из файла `settings.json` и документацию из `README.MD`.

## Функции

### `set_project_root`

**Описание**: Находит корневой каталог проекта, начиная от текущего файла и идя вверх по директориям. Останавливается на первой директории, содержащей указанные файлы-маркеры (например, `pyproject.toml`, `requirements.txt`, `.git`).

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или каталогов, используемых для определения корневого каталога.

**Возвращает**:

- `Path`: Путь к корневому каталогу проекта, если найден, в противном случае - путь к директории, в которой находится текущий скрипт.  Возвращает объект `Path`.

**Вызывает исключения**:

- Нет.


## Переменные

### `__root__`

**Описание**: Путь к корневому каталогу проекта.  Инициализируется вызовом функции `set_project_root`.

**Тип**: `Path`

### `settings`

**Описание**: Словарь, содержащий настройки проекта, загруженные из файла `settings.json`.

**Тип**: `dict` или `None`

### `doc_str`

**Описание**: Текст документации из файла `README.MD`.

**Тип**: `str` или `None`

### `__project_name__`

**Описание**: Имя проекта. Извлекается из `settings`, если доступно, иначе используется значение по умолчанию `hypotez`.

**Тип**: `str`

### `__version__`

**Описание**: Версия проекта. Извлекается из `settings`, если доступно, иначе значение по умолчанию - пустая строка.

**Тип**: `str`


### `__doc__`

**Описание**: Документация проекта. Извлекается из `doc_str`, если доступно, иначе пустая строка.

**Тип**: `str`


### `__details__`

**Описание**: Подробная информация о проекте.

**Тип**: `str` (значение по умолчанию пустая строка)


### `__author__`

**Описание**: Автор проекта. Извлекается из `settings`, если доступно, иначе пустая строка.

**Тип**: `str`

### `__copyright__`

**Описание**: Авторские права. Извлекается из `settings`, если доступно, иначе пустая строка.

**Тип**: `str`

### `__cofee__`

**Описание**: Ссылка на платформа для поддержки разработчика. Извлекается из `settings`, если доступно, иначе значение по умолчанию.

**Тип**: `str`


## Обработка исключений

Обработка потенциальных ошибок (FileNotFoundError и json.JSONDecodeError) при чтении файлов `settings.json` и `README.MD` предотвращает аварийный выход программы.