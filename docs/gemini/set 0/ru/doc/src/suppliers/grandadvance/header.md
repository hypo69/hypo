# Модуль hypotez/src/suppliers/grandadvance/header.py

## Обзор

Этот модуль содержит функции для определения корневой директории проекта и загрузки настроек из файла `settings.json`. Он также обрабатывает потенциальные ошибки при чтении файла настроек и файла README.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла и ищет вверх по дереву директорий, пока не найдет директорию, содержащую один из файлов, указанных в параметре `marker_files`.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, используемых для определения корневой директории проекта. По умолчанию: `('pyproject.toml', 'requirements.txt', '.git')`.


**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена, иначе - директория, в которой находится скрипт.


**Вызывает исключения**:

- Нет


### <ins>Замечания о `set_project_root`</ins>


Эта функция находит корневую директорию проекта, проходя вверх по дереву директорий от текущего файла. Она добавляет корневую директорию в `sys.path`, что позволяет импортировать модули из проекта.


## Переменные

### `__root__`

**Описание**: Переменная, хранящая путь к корневой директории проекта. Инициализируется функцией `set_project_root`.


**Тип**: `Path`


## Переменные глобального уровня


### `settings`


**Описание**: Словарь с настройками проекта. Загружается из файла `settings.json` в корневой директории проекта. Может быть `None`, если файл не найден или содержит некорректные данные.


**Тип**: `dict` или `None`


### `doc_str`


**Описание**: Строка с содержимым файла `README.MD` в корневой директории проекта. Может быть `None`, если файл не найден или содержит некорректные данные.


**Тип**: `str` или `None`


### `__project_name__`

**Описание**: Имя проекта, полученное из настроек. По умолчанию — `hypotez`.


**Тип**: `str`


### `__version__`

**Описание**: Версия проекта, полученная из настроек. По умолчанию — пустая строка.


**Тип**: `str`


### `__doc__`

**Описание**: Документация проекта, полученная из файла `README.MD`. По умолчанию — пустая строка.


**Тип**: `str`


### `__details__`

**Описание**: Подробное описание проекта. По умолчанию — пустая строка.


**Тип**: `str`


### `__author__`

**Описание**: Автор проекта, полученный из настроек. По умолчанию — пустая строка.


**Тип**: `str`


### `__copyright__`

**Описание**: Авторские права на проект, полученные из настроек. По умолчанию — пустая строка.


**Тип**: `str`


### `__cofee__`

**Описание**: Ссылка на страницу, где можно поддержать разработчика. По умолчанию — ссылка на Boosty.


**Тип**: `str`