# Модуль `hypotez/src/suppliers/aliexpress/campaign/header.py`

## Обзор

Этот модуль содержит функции для определения корневой директории проекта и загрузки настроек из файла `settings.json`. Он также предоставляет доступ к документации проекта (README.md).

## Функции

### `set_project_root`

**Описание**:  Определяет корневую директорию проекта, начиная от директории текущего файла. Поиск происходит вверх по директориям до тех пор, пока не будет найдена директория, содержащая указанные маркерные файлы (например, `pyproject.toml`, `requirements.txt`, `.git`).

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или директорий, используемые для определения корневой директории.  По умолчанию это кортеж `('pyproject.toml', 'requirements.txt', '.git')`.


**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена. В противном случае возвращается путь к директории, в которой находится скрипт.


**Пример использования**:

```python
project_root = set_project_root()
print(project_root)
```

### `set_project_root` (пример с добавкой в sys.path)

**Описание**:  Определяет корневую директорию проекта, как в предыдущей функции, но, если найдена, добавляет её в `sys.path`. Это необходимо для импорта модулей из корневой директории.

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или директорий, используемые для определения корневой директории.


**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена. В противном случае возвращается путь к директории, в которой находится скрипт.


**Пример использования**:

```python
project_root = set_project_root()
print(project_root)
```


## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта, полученный с помощью функции `set_project_root()`.


## Загрузка данных

**Описание**:  Этот раздел описывает загрузку настроек из файла `settings.json` и документации из `README.MD`.


### `settings`

**Описание**: Словарь с настройками проекта, загруженными из файла `settings.json`.


### `doc_str`

**Описание**: Строковое представление содержимого файла `README.MD`, или `None`, если файл не найден или некорректно отформатирован.


**Возможные исключения:**

- `FileNotFoundError`: Если файл `settings.json` или `README.MD` не найден.
- `json.JSONDecodeError`: Если файл `settings.json` содержит некорректные данные JSON.



## Константы и магические переменные

**Описание**:  В этом разделе описаны глобальные константы и магические переменные.

### `MODE`

**Описание**: Глобальная константа, хранящая режим работы (`'dev'`).


### `__project_name__`

**Описание**:  Название проекта, полученное из `settings.json` или установленное по умолчанию как `'hypotez'`.


### `__version__`

**Описание**: Версия проекта, полученная из `settings.json` или установленная по умолчанию как пустая строка.


### `__doc__`

**Описание**:  Документация проекта, полученная из `README.md` или пустая строка.


### `__details__`

**Описание**:  Детали проекта (пустая строка по умолчанию).


### `__author__`

**Описание**: Автор проекта, полученный из `settings.json` или пустая строка.


### `__copyright__`

**Описание**: Авторские права, полученные из `settings.json` или пустая строка.


### `__cofee__`

**Описание**: Ссылка на бусти, чтобы поблагодарить разработчика.