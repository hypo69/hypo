# Модуль hypotez/src/gui/header.py

## Обзор

Этот модуль определяет корневой путь к проекту Hypotez.  Он находит директорию проекта, начиная с текущего файла и идя вверх по дереву директорий, пока не найдет директорию, содержащую файлы-маркеры (pyproject.toml, requirements.txt, .git).  Модуль также устанавливает найденный корневой путь в системный путь `sys.path`, чтобы импорты работали корректно.  В дальнейшем планируется перенести корневой путь в системные переменные.

## Функции

### `set_project_root`

**Описание**: Функция находит корневую директорию проекта, начиная от текущего файла.

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или директорий, которые используются для определения корневой директории проекта. По умолчанию: `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если она найдена, иначе — путь к директории, в которой находится скрипт.

**Вызывает исключения**:

- Нет


## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта.

**Тип**: `Path`

**Инициализация**: Вызывается функция `set_project_root()` для определения пути.

## Загрузка настроек

### Загрузка настроек из settings.json

**Описание**: Загружает настройки из файла `settings.json` в переменную `settings`.

**Детали**:
Этот блок пытается открыть файл `src/settings.json` и загрузить его содержимое в формате JSON.
Обрабатываются возможные исключения `FileNotFoundError` и `json.JSONDecodeError`, если файл не найден или имеет неправильный формат. В случае ошибки переменная `settings` остаётся `None`.

### Загрузка документации из README.MD

**Описание**: Загружает содержание файла README.MD в переменную `doc_str`.

**Детали**:
Этот блок пытается открыть файл `src/README.MD` и прочитать его содержимое.
Обрабатываются возможные исключения `FileNotFoundError` и `json.JSONDecodeError`, если файл не найден или имеет неправильный формат. В случае ошибки переменная `doc_str` остаётся `None`.


## Переменные проекта (Global Variables)

### `__project_name__`

**Описание**: Имя проекта. Значение по умолчанию — `hypotez`.

**Тип**: `str`

**Инициализация**: Получается из `settings.json` или устанавливается как `hypotez`, если `settings` не задан или `project_name` не найден.

### `__version__`

**Описание**: Версия проекта. Значение по умолчанию — пустая строка.

**Тип**: `str`

**Инициализация**: Получается из `settings.json` или устанавливается как пустая строка, если `settings` не задан или `version` не найден.

### `__doc__`

**Описание**: Документация проекта (содержание из README.md). Значение по умолчанию — пустая строка.

**Тип**: `str`

**Инициализация**: Получается из `doc_str` или устанавливается как пустая строка, если `doc_str` не задан.


### `__details__`

**Описание**: Подробная информация о проекте.  Значение по умолчанию - пустая строка.

**Тип**: `str`


### `__author__`

**Описание**: Автор проекта. Значение по умолчанию — пустая строка.

**Тип**: `str`

**Инициализация**: Получается из `settings.json` или устанавливается как пустая строка, если `settings` не задан или `author` не найден.

### `__copyright__`

**Описание**: Авторские права проекта. Значение по умолчанию — пустая строка.

**Тип**: `str`

**Инициализация**: Получается из `settings.json` или устанавливается как пустая строка, если `settings` не задан или `copyright` не найден.

### `__cofee__`

**Описание**: Ссылка на способ поддержания разработчика. Значение по умолчанию — ссылка на Boosty.

**Тип**: `str`

**Инициализация**: Получается из `settings.json` или устанавливается как ссылка на Boosty, если `settings` не задан или `cofee` не найден.