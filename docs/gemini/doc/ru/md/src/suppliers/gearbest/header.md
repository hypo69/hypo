# Модуль hypotez/src/suppliers/gearbest/header.py

## Обзор

Этот модуль содержит функции для определения корневой директории проекта и загрузки настроек из файла `settings.json`.  Он также пытается загрузить текстовую информацию из файла `README.MD`.  Модуль инициализирует переменные, хранящие информацию о проекте, например, имя проекта, версию, описание, автора и т.д., с использованием данных из `settings.json` или предопределёнными значениями в случае отсутствия или ошибок при чтении файла.


## Функции

### `set_project_root`

**Описание**: Функция находит корневую директорию проекта, начиная с текущего файла и идя вверх по директориям, пока не найдет директорию содержащую один из указанных файлов (или директорий).

**Параметры**:

- `marker_files` (tuple): Кортеж строк или путей к файлам/директориям, по которым будет определяться корневая директория проекта.


**Возвращает**:

- `Path`: Путь к корневой директории проекта.  Если корневая директория не найдена, возвращает директорию, где расположен текущий файл.

**Вызывает исключения**:

- Не вызывает никаких исключений.


### `__init__`

**Описание**: Инициализирует модуль.

**Параметры**:

- Не принимает никаких параметров.

**Возвращает**:

- Не возвращает значения.

**Вызывает исключения**:

- `FileNotFoundError`: Возникает, если файл `settings.json` не найден.
- `json.JSONDecodeError`: Возникает, если содержимое `settings.json` не является корректным JSON-объектом.
- Исключения, которые могут генерировать функции из модуля `src`.


## Переменные

### `MODE`

**Описание**: Переменная, хранящая режим работы модуля (в данном случае 'dev').


### `__root__`

**Описание**: Переменная, хранящая путь к корневой директории проекта. Инициализируется функцией `set_project_root`.

**Тип**: `Path`


### `settings`

**Описание**: Переменная, хранящая данные из файла `settings.json`.


**Тип**: `dict` или `None`


### `doc_str`

**Описание**: Переменная, хранящая текст из файла `README.MD`.

**Тип**: `str` или `None`


### `__project_name__`

**Описание**: Переменная, содержащая имя проекта. Получает значение из `settings` или задаёт значение по умолчанию.

**Тип**: `str`


### `__version__`

**Описание**: Переменная, содержащая версию проекта. Получает значение из `settings` или задаёт значение по умолчанию.

**Тип**: `str`


### `__doc__`

**Описание**: Переменная, содержащая описание проекта. Получает значение из `doc_str` или задаёт значение по умолчанию.

**Тип**: `str`


### `__details__`

**Описание**: Переменная, содержащая дополнительные детали о проекте.

**Тип**: `str`


### `__author__`

**Описание**: Переменная, содержащая имя автора проекта. Получает значение из `settings` или задаёт значение по умолчанию.

**Тип**: `str`


### `__copyright__`

**Описание**: Переменная, содержащая копирайт проекта. Получает значение из `settings` или задаёт значение по умолчанию.

**Тип**: `str`


### `__cofee__`

**Описание**: Переменная, содержащая ссылку для поддержки разработчика. Получает значение из `settings` или задаёт значение по умолчанию.

**Тип**: `str`