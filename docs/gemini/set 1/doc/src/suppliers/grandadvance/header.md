# Модуль `hypotez/src/suppliers/grandadvance/header.py`

## Обзор

Этот модуль содержит функции для определения корневой директории проекта и загрузки настроек из файла `settings.json`.  Он также загружает README файл, если он доступен.  Модуль предоставляет переменные, содержащие данные о проекте, такие как имя, версия, документация и т.д.


## Функции

### `set_project_root`

**Описание**: Определяет корневую директорию проекта, начиная от текущего файла и идя вверх по дереву директорий до первого найденного директории содержащей файлы, указанные в `marker_files`.

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или директорий, которые будут использоваться для определения корневой директории. По умолчанию используется кортеж `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена, в противном случае, директория, где расположен текущий скрипт.

**Вызывает исключения**:
- Нет

### `set_project_root`

**Описание**:  Функция, которая находит корневую директорию проекта, начиная от текущего файла.  Перебирает родительские директории до тех пор, пока не найдёт директорию, содержащую один из файлов из `marker_files`. Если такая директория найдена, её путь возвращается, а также добавляется в `sys.path`, если она ещё там не была.

**Параметры**:

- `marker_files` (tuple, optional): Список файлов/папок, по которым ищется корень проекта.


**Возвращает**:

- `Path`: Путь к корневой директории.

**Вызывает исключения**:
- Нет


## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта, полученный с помощью функции `set_project_root`.

**Тип**: `Path`


### `settings`

**Описание**: Словарь, содержащий настройки проекта, загруженные из файла `src/settings.json`.


**Тип**: `dict` | `None`


### `doc_str`

**Описание**: Содержимое файла `README.MD`, если он найден и корректен.

**Тип**: `str` | `None`


### `__project_name__`

**Описание**: Имя проекта, полученное из настроек `settings` или имеющее значение по умолчанию `hypotez`.

**Тип**: `str`


### `__version__`

**Описание**: Версия проекта, полученная из настроек `settings` или пустая строка по умолчанию.

**Тип**: `str`


### `__doc__`

**Описание**: Документация проекта, полученная из файла `README.MD` или пустая строка по умолчанию.

**Тип**: `str`


### `__details__`

**Описание**: Детали проекта, пустая строка по умолчанию.

**Тип**: `str`


### `__author__`

**Описание**: Автор проекта, полученный из настроек `settings` или пустая строка по умолчанию.

**Тип**: `str`


### `__copyright__`

**Описание**: Авторские права проекта, полученные из настроек `settings` или пустая строка по умолчанию.

**Тип**: `str`


### `__cofee__`

**Описание**: Ссылка для поддержки разработчика.

**Тип**: `str`


## Обработка исключений

Обработка `FileNotFoundError` и `json.JSONDecodeError` при чтении файлов `settings.json` и `README.MD` предотвращает сбой программы при их отсутствии или некорректном формате.

```