# Модуль `hypotez/src/logger/header.py`

## Обзор

Модуль `hypotez/src/logger/header.py` определяет корневой путь к проекту `hypotez`.  Все импорты строятся относительно этого пути.  В будущем планируется перенести определение корневого пути в системную переменную.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с текущей директории файла. Поиск происходит вверх по иерархии директорий, и останавливается на первой директории, содержащей указанные файлы-маркеры.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, используемых для определения корневой директории проекта.

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена. В противном случае возвращает директорию, в которой расположен данный скрипт.


**Пример использования**:

```python
root_path = set_project_root()
print(root_path)
```


## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта, полученный с помощью функции `set_project_root`.


### `settings`

**Описание**: Словарь настроек проекта.

**Значение по умолчанию**: `None`


### `doc_str`

**Описание**: Строка, содержащая контент из файла README.MD.


**Значение по умолчанию**: `None`

### `__project_name__`

**Описание**: Название проекта, полученное из файла настроек (`settings.json`). По умолчанию `'hypotez'`.


### `__version__`

**Описание**: Версия проекта, полученная из файла настроек (`settings.json`). По умолчанию `''`.


### `__doc__`

**Описание**: Документация проекта, полученная из файла README.MD. По умолчанию `''`.


### `__details__`

**Описание**: Дополнительные детали о проекте. По умолчанию `''`.


### `__author__`

**Описание**: Автор проекта, полученный из файла настроек (`settings.json`). По умолчанию `''`.


### `__copyright__`

**Описание**: Авторские права на проект, полученные из файла настроек (`settings.json`). По умолчанию `''`.


### `__cofee__`

**Описание**: Ссылка на спонсорскую страницу для поддержки разработчика. По умолчанию ссылка на страницу boosty.to.

**Обработка исключений**:

- `FileNotFoundError`: Если файл настроек (`settings.json`) или файл README.MD не найден.
- `json.JSONDecodeError`: Если файл настроек (`settings.json`) имеет неправильный формат JSON. В обоих случаях соответствующие переменные не изменяются.

```
```