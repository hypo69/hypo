# Модуль hypotez/src/logger/header.py

## Обзор

Модуль `hypotez/src/logger/header.py` определяет корневой путь к проекту `hypotez`. Все импорты строятся относительно этого пути.  В будущем предполагается перенести определение корневого пути в системную переменную.

## Функции

### `set_project_root`

**Описание**: Находит корневой каталог проекта, начиная с текущего каталога файла и идя вверх по дереву директорий, пока не найдет каталог, содержащий один из указанных маркеров файлов (например, `pyproject.toml`, `requirements.txt`, `.git`).

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или каталогов, которые используются в качестве маркеров корневого каталога проекта. По умолчанию используются `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневому каталогу проекта, если он найден. В противном случае возвращает путь к каталогу, где расположен скрипт.

**Обрабатывает исключения**:

-  Не обрабатывает исключения.


## Переменные

### `__root__`

**Описание**: Путь к корневому каталогу проекта, полученный с помощью функции `set_project_root()`.

**Тип**: `Path`

##  Другие переменные

### `settings`

**Описание**: Словарь со значениями из файла `settings.json` в корневом каталоге проекта.

**Тип**: `dict`

**Примечание**: Значение по умолчанию `None`.  Файл `settings.json` загружается при выполнении модуля.

### `doc_str`

**Описание**: Содержимое файла `README.MD` в корневом каталоге проекта.

**Тип**: `str`

**Примечание**: Значение по умолчанию `None`. Файл `README.MD` загружается при выполнении модуля.


### `__project_name__`

**Описание**: Имя проекта, полученное из файла `settings.json`. Значение по умолчанию `hypotez`.

**Тип**: `str`


### `__version__`

**Описание**: Версия проекта, полученная из файла `settings.json`. Значение по умолчанию пустая строка.

**Тип**: `str`

### `__doc__`

**Описание**: Документация проекта, полученная из файла `README.MD`. Значение по умолчанию пустая строка.

**Тип**: `str`


### `__details__`

**Описание**: Дополнительные детали проекта. Значение по умолчанию пустая строка.

**Тип**: `str`


### `__author__`

**Описание**: Автор проекта, полученный из файла `settings.json`. Значение по умолчанию пустая строка.

**Тип**: `str`

### `__copyright__`

**Описание**: Авторские права, полученные из файла `settings.json`. Значение по умолчанию пустая строка.

**Тип**: `str`

### `__coffee__`

**Описание**: Ссылка на поддержку разработчика. Значение по умолчанию – ссылка на Boosty.

**Тип**: `str`

**Примечание**: Это значение подтягивается из файла `settings.json` и содержит ссылку на страницу поддержки разработчика. Если файла или соответствующего ключа нет, используется значение по умолчанию.