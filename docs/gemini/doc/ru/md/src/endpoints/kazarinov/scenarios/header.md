# Модуль hypotez/src/endpoints/kazarinov/scenarios/header.py

## Обзор

Этот модуль содержит функции для определения корневой директории проекта и загрузки настроек из файла `settings.json`. Он также предоставляет доступ к документации проекта, хранящейся в файле `README.MD`.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла, перемещаясь вверх по дереву директорий до тех пор, пока не найдет директорию, содержащую указанные маркерные файлы (например, `pyproject.toml`, `requirements.txt`, `.git`).

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или директорий, используемых для определения корневой директории проекта.

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если она найдена. В противном случае возвращает директорию, где расположен скрипт.

**Вызывает исключения**:
(Не вызывают исключений)


### Загрузка настроек и документации

**Описание**: Загружает настройки из файла `settings.json` и документацию из файла `README.MD`. Если файлы не найдены или содержат невалидные данные, значения по умолчанию устанавливаются.

**Параметры**:
(Нет параметров)

**Возвращает**:
(Не возвращает значений)

**Вызывает исключения**:
- `FileNotFoundError`: Возникает, если файл `settings.json` или `README.MD` не найден.
- `json.JSONDecodeError`: Возникает, если файл `settings.json` содержит некорректный JSON.


## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта, полученный с помощью функции `set_project_root()`.

**Тип**: `Path`

### `settings`

**Описание**: Словарь, содержащий настройки из файла `settings.json`.

**Тип**: `dict` или `None`


### `doc_str`

**Описание**: Строка, содержащая текст документации из файла `README.MD`.

**Тип**: `str` или `None`


### `__project_name__`

**Описание**: Название проекта, полученное из настроек. По умолчанию 'hypotez'.

**Тип**: `str`


### `__version__`

**Описание**: Версия проекта, полученная из настроек. По умолчанию пустая строка.

**Тип**: `str`


### `__doc__`

**Описание**: Текст документации, полученный из файла `README.MD`. По умолчанию пустая строка.

**Тип**: `str`


### `__details__`

**Описание**: Подробная информация о проекте. По умолчанию пустая строка.

**Тип**: `str`


### `__author__`

**Описание**: Автор проекта, полученный из настроек. По умолчанию пустая строка.

**Тип**: `str`


### `__copyright__`

**Описание**: Авторские права, полученные из настроек. По умолчанию пустая строка.

**Тип**: `str`


### `__cofee__`

**Описание**: Ссылка на платформа для пожертвований.


**Тип**: `str`