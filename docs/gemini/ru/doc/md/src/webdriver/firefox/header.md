# Модуль hypotez/src/webdriver/firefox/header.py

## Обзор

Этот модуль содержит функции для определения корневой директории проекта, загрузки настроек из файла `settings.json` и получения информации о проекте. Он также предоставляет доступ к документации, хранящейся в файле `README.MD`.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла. Поиск происходит вверх по директориям, пока не будет найдена директория, содержащая один из указанных файлов-маркеров (например, `pyproject.toml`, `requirements.txt`, `.git`).

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, используемых для определения корневой директории проекта.


**Возвращает**:

- `Path`: Путь к корневой директории проекта, если она найдена. В противном случае возвращается директория, в которой находится текущий файл.


**Вызывает исключения**:

- Не вызывает исключений.


###  (Заметка: Другие переменные, такие как `__root__`, `settings`, `doc_str`, не являются функциями, а являются переменными, инициализированными внутри модуля.)


## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта. Инициализируется вызовом функции `set_project_root()`.

**Тип**: `Path`

### `settings`

**Описание**: Словарь, содержащий настройки проекта, загруженный из файла `settings.json`.

**Тип**: `dict` или `None`


### `doc_str`

**Описание**: Строка, содержащая содержимое файла `README.MD`.

**Тип**: `str` или `None`


### `__project_name__`

**Описание**: Название проекта, полученное из настроек или имеющее значение по умолчанию `hypotez`.

**Тип**: `str`


### `__version__`

**Описание**: Версия проекта, полученная из настроек или имеющая значение по умолчанию пустая строка.

**Тип**: `str`


### `__doc__`

**Описание**: Документация проекта, полученная из файла `README.MD` или имеющая значение по умолчанию пустая строка.

**Тип**: `str`


### `__details__`

**Описание**: Подробная информация о проекте. (Значение по умолчанию пустая строка).

**Тип**: `str`


### `__author__`

**Описание**: Автор проекта, полученный из настроек или имеющий значение по умолчанию пустая строка.

**Тип**: `str`


### `__copyright__`

**Описание**: Авторские права проекта, полученные из настроек или имеющие значение по умолчанию пустая строка.

**Тип**: `str`


### `__cofee__`

**Описание**: Ссылка на возможность поддержать разработчика через платформу boosty.

**Тип**: `str`