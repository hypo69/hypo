# Модуль hypotez/src/product/header.py

## Обзор

Модуль `header.py` определяет корневой путь к проекту `hypotez`. Все импорты в других модулях строятся относительно этого пути. В будущем этот путь может быть перенесен в системную переменную.  Он также загружает настройки из файла `settings.json` и описание из файла `README.MD` (если они существуют).


## Функции

### `set_project_root`

**Описание**: Находит корневой каталог проекта, начиная с текущего каталога файла, ищет вверх по дереву каталогов, пока не найдет каталог, содержащий один из указанных файлов-маркеров.

**Параметры**:

- `marker_files` (tuple): Список имен файлов или каталогов, которые используются для идентификации корневого каталога проекта. По умолчанию: `('pyproject.toml', 'requirements.txt', '.git')`.


**Возвращает**:

- `Path`: Путь к корневому каталогу проекта, если найден, иначе путь к каталогу, в котором находится текущий скрипт.


**Вызывает исключения**:

- Нет



## Переменные

### `__root__`

**Описание**: Путь к корневому каталогу проекта, полученный с помощью функции `set_project_root()`.

**Тип**: `Path`


### `settings`

**Описание**: Словарь настроек, загруженный из файла `settings.json` в каталоге `src`.

**Тип**: `dict` или `None`


### `doc_str`

**Описание**: Строка документации, загруженная из файла `README.MD` в каталоге `src`.

**Тип**: `str` или `None`


### `__project_name__`

**Описание**: Название проекта, полученное из настроек или имеющее значение по умолчанию `hypotez`.

**Тип**: `str`


### `__version__`

**Описание**: Версия проекта, полученная из настроек или имеющая значение по умолчанию пустая строка.

**Тип**: `str`


### `__doc__`

**Описание**: Документация проекта, полученная из `README.MD` или имеющая значение по умолчанию пустая строка.

**Тип**: `str`


### `__details__`

**Описание**: Подробности о проекте, по умолчанию пустая строка.

**Тип**: `str`


### `__author__`

**Описание**: Автор проекта, полученный из настроек или имеющий значение по умолчанию пустая строка.

**Тип**: `str`


### `__copyright__`

**Описание**: Авторские права, полученные из настроек или имеющие значение по умолчанию пустая строка.

**Тип**: `str`


### `__cofee__`

**Описание**: Ссылка на поддержку разработчика, по умолчанию имеет значение  `Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69`.

**Тип**: `str`


## Обработка исключений


При чтении файлов `settings.json` и `README.MD` обрабатываются исключения `FileNotFoundError` и `json.JSONDecodeError`. В случае ошибки соответствующие переменные ( `settings`, `doc_str`) устанавливаются в `None` или пустые значения, чтобы избежать ошибок в дальнейшем коде.

```