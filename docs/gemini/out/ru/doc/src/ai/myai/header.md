# Модуль hypotez/src/ai/myai/header.py

## Обзор

Этот модуль содержит функции для определения корневой директории проекта, загрузки настроек из файла `settings.json` и получения документации из файла `README.MD`.  Он устанавливает `__root__` в переменную окружения `sys.path` для доступа к зависимостям.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с текущего файла и поднимаясь по иерархии директорий.

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или директорий, по которым определяется корень проекта. По умолчанию `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена; иначе - директория, в которой расположен текущий файл.

**Вызывает исключения**:

- Нет.


## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта, полученный с помощью функции `set_project_root`.

**Тип**: `Path`


### `settings`

**Описание**: Словарь, содержащий настройки проекта, загруженный из файла `src/settings.json`.

**Тип**: `dict` или `None`.


### `doc_str`

**Описание**: Строка, содержащая текст документации из файла `README.MD` в корневой директории.

**Тип**: `str` или `None`.

### `__project_name__`

**Описание**: Название проекта, взятое из файла `settings.json`. Если ключ `project_name` отсутствует, по умолчанию используется `hypotez`.


**Тип**: `str`


### `__version__`

**Описание**: Версия проекта, взятая из файла `settings.json`. Если ключ `version` отсутствует, по умолчанию используется пустая строка.


**Тип**: `str`

### `__doc__`

**Описание**: Текст документации из файла `README.MD`. Если файл не найден или пустой, используется пустая строка.


**Тип**: `str`


### `__details__`

**Описание**:  Детали проекта (строка).


**Тип**: `str`


### `__author__`

**Описание**: Автор проекта, взятый из файла `settings.json`. Если ключ `author` отсутствует, по умолчанию используется пустая строка.

**Тип**: `str`


### `__copyright__`

**Описание**: Авторские права, взятые из файла `settings.json`. Если ключ `copyrihgnt` отсутствует, по умолчанию используется пустая строка.


**Тип**: `str`


### `__cofee__`

**Описание**: Ссылка на платежную систему для поддержки разработчика (кофе).


**Тип**: `str`