# Модуль hypotez/src/suppliers/etzmaleh/header.py

## Обзор

Этот модуль содержит функции для определения корневой директории проекта и загрузки настроек из файла `settings.json` и документации из файла `README.MD`. Он также инициализирует переменные, хранящие информацию о проекте, такие как имя, версия, описание и др.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная от текущего файла и поднимаясь вверх по иерархии директорий, пока не найдёт директорию, содержащую один из файлов или папок, указанных в аргументе `marker_files`.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или папок, которые будут использоваться для поиска корневой директории. По умолчанию заданы `('pyproject.toml', 'requirements.txt', '.git')`.


**Возвращает**:

- `Path`: Путь к корневой директории проекта, если она найдена. В противном случае возвращает путь к директории, где расположен текущий скрипт.

**Вызывает исключения**:

Нет.


## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта.  Инициализируется функцией `set_project_root()`.

**Тип**: `Path`

### `settings`

**Описание**: Словарь с настройками проекта, загруженный из файла `src/settings.json`.

**Тип**: `dict` или `None`


### `doc_str`

**Описание**: Строка, содержащая текст документации из файла `src/README.MD`.

**Тип**: `str` или `None`


### `__project_name__`

**Описание**: Название проекта. Получает значение из `settings['project_name']`, если оно есть; иначе используется значение по умолчанию `'hypotez'`.

**Тип**: `str`

### `__version__`

**Описание**: Версия проекта. Получает значение из `settings['version']`, если оно есть; иначе используется пустая строка.

**Тип**: `str`


### `__doc__`

**Описание**: Документация проекта. Получает значение из `doc_str`, если оно есть; иначе используется пустая строка.

**Тип**: `str`


### `__details__`

**Описание**: Дополнительные детали проекта (пустая строка по умолчанию).

**Тип**: `str`


### `__author__`

**Описание**: Автор проекта. Получает значение из `settings['author']`, если оно есть; иначе используется пустая строка.

**Тип**: `str`


### `__copyright__`

**Описание**: Авторские права проекта. Получает значение из `settings['copyright']`, если оно есть; иначе используется пустая строка.

**Тип**: `str`


### `__cofee__`

**Описание**: Ссылка на страницу для поддержки разработчика (пожертвования кофе). Получает значение из `settings['cofee']`, если оно есть; иначе используется строка с ссылкой по умолчанию.

**Тип**: `str`


## Обработка исключений

Функции `set_project_root`, `settings` and `doc_str` используют обработку исключений `try...except` для обработки потенциальных ошибок, связанных с файлами (`FileNotFoundError`) и декодированием JSON (`json.JSONDecodeError`).  В случае возникновения ошибок, соответствующие переменные устанавливаются в `None` или пустые строки.