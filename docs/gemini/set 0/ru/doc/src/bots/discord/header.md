# Модуль `hypotez/src/bots/discord/header.py`

## Обзор

Данный модуль содержит функцию `set_project_root` для определения корневой директории проекта и переменные, содержащие информацию о проекте (имя, версия, описание и др.), загруженные из файла `settings.json` и `README.MD`.

## Функции

### `set_project_root`

**Описание**:  Функция находит корневую директорию проекта, начиная с директории текущего файла и идя вверх по иерархии директорий. Поиск завершается, когда находится директория, содержащая один из файлов/директорий, переданных в аргументе `marker_files`.

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или директорий, которые будут использоваться для поиска корневой директории. По умолчанию содержит `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневой директории, если она найдена, иначе возвращает директорию, в которой расположен текущий файл.

**Вызывает исключения**:

- Нет


## Переменные

### `MODE`

**Описание**: Строковая переменная, хранящая текущий режим работы (например, `'dev'` или `'prod'`). Значение по умолчанию - `'dev'`.

### `__root__`

**Описание**: Переменная, содержащая объект `Path`, представляющий корневую директорию проекта. Присваивается значением возвращаемым функцией `set_project_root()`.

### `settings`

**Описание**: Словарь, содержащий настройки проекта, загруженный из файла `settings.json`. Значение по умолчанию - `None`.

**Обработка исключений**:

- `FileNotFoundError`: Возникает, если файл `settings.json` не найден.
- `json.JSONDecodeError`: Возникает, если файл `settings.json` содержит невалидные данные JSON.
В этом случае переменная `settings` остаётся `None`.


### `doc_str`

**Описание**: Строковая переменная, содержащая содержимое файла `README.MD`. Значение по умолчанию - `None`.

**Обработка исключений**:

- `FileNotFoundError`: Возникает, если файл `README.MD` не найден.
- `json.JSONDecodeError`: Возникает, если файл `README.MD` содержит невалидные данные.
В этом случае переменная `doc_str` остаётся `None`.

### `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`

**Описание**: Переменные, содержащие информацию о проекте (имя, версия, описание, автор, копирайт, ссылка для пожертвований), полученные из словаря `settings` (если доступен) или имеющие значения по умолчанию.


## Модули

### `sys`, `json`, `pathlib`, `packaging.version`

**Описание**:  Импортированные модули для работы с системными переменными, JSON-данными, путями к файлам, версиями пакетов.