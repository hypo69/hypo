# Модуль hypotez/src/logger/header.py

## Обзор

Модуль `hypotez/src/logger/header.py` определяет корневой путь к проекту `hypotez`.  Все импорты строятся относительно этого пути.  В дальнейшем, предполагается перенести логику определения корневого пути в системную переменную.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с текущей директории файла, ищет вверх по дереву директорий, останавливаясь на первой директории, содержащей один из указанных файлов-маркеров (например, `pyproject.toml`, `requirements.txt`, `.git`).

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или каталогов, по которым определяется корневая директория проекта.  По умолчанию `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если она найдена. В противном случае возвращает директорию, в которой расположен текущий файл.

**Вызывает исключения**:

- Нет.


## Глобальные переменные

### `__root__`

**Описание**: Путь к корневой директории проекта, полученный функцией `set_project_root()`.

**Тип**: `Path`

### `settings`

**Описание**: Словарь настроек проекта, загруженный из файла `settings.json`.

**Тип**: `dict` или `None`


### `doc_str`

**Описание**: Строка документации проекта, считанная из файла `README.MD`.

**Тип**: `str` или `None`


### `__project_name__`

**Описание**: Название проекта, взятое из файла `settings.json`. По умолчанию `'hypotez'`.

**Тип**: `str`


### `__version__`

**Описание**: Версия проекта, взятая из файла `settings.json`. По умолчанию пустая строка.

**Тип**: `str`


### `__doc__`

**Описание**: Документация проекта. Считывается из `README.MD`, если файл существует.

**Тип**: `str`


### `__details__`

**Описание**: Подробная информация о проекте.

**Тип**: `str`


### `__author__`

**Описание**: Автор проекта, взятый из файла `settings.json`. По умолчанию пустая строка.

**Тип**: `str`


### `__copyright__`

**Описание**: Авторские права, взятые из файла `settings.json`. По умолчанию пустая строка.

**Тип**: `str`


### `__cofee__`

**Описание**: Ссылка для поддержки разработчика. Взята из файла `settings.json`, если он существует. По умолчанию ссылка на Boosty.

**Тип**: `str`