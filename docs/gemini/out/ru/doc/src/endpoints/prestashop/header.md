# Модуль `hypotez/src/logger/header.py`

## Обзор

Данный модуль определяет корневой путь к проекту `hypotez`. Все импорты в проекте строятся относительно этого пути.  В дальнейшем предполагается перенести определение корневого пути в системные переменные.  Модуль обрабатывает файлы `settings.json` и `README.MD` для получения настроек проекта и документации.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с текущей директории файла и идя вверх по дереву каталогов, пока не найдет директорию содержащую один из файлов-маркеров (pyproject.toml, requirements.txt, .git).

**Параметры**:
- `marker_files` (tuple): Кортеж имён файлов или директорий, используемых для идентификации корневой директории проекта.

**Возвращает**:
- `Path`: Путь к корневой директории, если найдена, иначе путь к директории, где находится текущий скрипт.

**Вызывает исключения**:
- Нет


## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта. Получается вызовом функции `set_project_root()`.

**Тип**: `Path`


## Обработка настроек

### Загрузка настроек из `settings.json`

**Описание**: Загружает настройки проекта из файла `settings.json` расположенного в корне проекта.

**Возможные ошибки**:
- `FileNotFoundError`: Если файл `settings.json` не найден.
- `json.JSONDecodeError`: Если файл `settings.json` содержит некорректный JSON.

**Обработка ошибок**: Исключение (FileNotFoundError, json.JSONDecodeError) обрабатывается с помощью `...`.

**Результат**: Загрузка настроек проекта в переменную `settings`.


### Загрузка документации из `README.MD`

**Описание**: Загружает документацию проекта из файла `README.MD` расположенного в корне проекта.

**Возможные ошибки**:
- `FileNotFoundError`: Если файл `README.MD` не найден.
- `json.JSONDecodeError`: Если файл `README.MD` содержит некорректный JSON.

**Обработка ошибок**: Исключение (FileNotFoundError, json.JSONDecodeError) обрабатывается с помощью `...`.

**Результат**: Загрузка документации в переменную `doc_str`.

## Переменные проекта

### `__project_name__`

**Описание**: Название проекта, полученное из настроек или установленное по умолчанию ('hypotez').

**Тип**: `str`

### `__version__`

**Описание**: Версия проекта, полученная из настроек или установленная по умолчанию ('').

**Тип**: `str`

### `__doc__`

**Описание**: Документация проекта, полученная из файла `README.MD` или установленная по умолчанию ('').

**Тип**: `str`

### `__details__`

**Описание**: Детали проекта (пустая строка по умолчанию).

**Тип**: `str`

### `__author__`

**Описание**: Автор проекта, полученный из настроек или установленный по умолчанию ('').

**Тип**: `str`

### `__copyright__`

**Описание**: Авторские права проекта, полученные из настроек или установленные по умолчанию ('').

**Тип**: `str`

### `__cofee__`

**Описание**: Ссылка на платежную систему для поддержки разработчика.

**Тип**: `str`