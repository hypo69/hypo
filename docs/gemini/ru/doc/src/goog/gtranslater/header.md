# Модуль hypotez/src/goog/gtranslater/header.py

## Обзор

Этот модуль содержит вспомогательные функции для работы с настройками проекта, корневой директории и документацией. Он определяет переменные для хранения информации о проекте, такие как имя, версия, автор, описание и путь к корневому каталогу.  Также он определяет функцию для поиска корневого каталога проекта, основываясь на определённых маркерах.

## Функции

### `set_project_root`

**Описание**:  Находит корневую директорию проекта, начиная с текущей директории и поднимаясь вверх по иерархии директорий.  Останавливается на первой директории, содержащей один из указанных маркеров файлов.

**Параметры**:

- `marker_files` (tuple): Кортеж имён файлов или директорий, которые будут использоваться для определения корневой директории проекта. По умолчанию содержит `('pyproject.toml', 'requirements.txt', '.git')`.


**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена. В противном случае возвращает директорию, в которой находится текущий файл.


**Вызывает исключений**:

- Нет.


## Переменные

### `__root__`

**Описание**:  Путь к корневой директории проекта. Инициализируется функцией `set_project_root()`.


**Тип**: `Path`


### `settings`

**Описание**: Словарь с настройками проекта, загруженный из файла `settings.json`.


**Тип**: `dict` или `None`


### `doc_str`

**Описание**:  Текст из файла `README.MD`, если он найден.


**Тип**: `str` или `None`


### `__project_name__`

**Описание**:  Имя проекта, полученное из `settings.json`, по умолчанию `hypotez`.


**Тип**: `str`


### `__version__`

**Описание**: Версия проекта, полученная из `settings.json`, по умолчанию пустая строка.


**Тип**: `str`


### `__doc__`

**Описание**:  Описание проекта, полученное из `README.MD`, по умолчанию пустая строка.


**Тип**: `str`


### `__details__`

**Описание**: Дополнительные детали о проекте, по умолчанию пустая строка.


**Тип**: `str`


### `__author__`

**Описание**: Автор проекта, полученный из `settings.json`, по умолчанию пустая строка.


**Тип**: `str`


### `__copyright__`

**Описание**: Авторские права проекта, полученные из `settings.json`, по умолчанию пустая строка.


**Тип**: `str`


### `__cofee__`

**Описание**: Ссылка на возможность поддержать разработчика, по умолчанию определённая ссылка.


**Тип**: `str`