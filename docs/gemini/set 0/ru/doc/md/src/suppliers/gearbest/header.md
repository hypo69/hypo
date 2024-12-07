# Модуль `hypotez/src/suppliers/gearbest/header.py`

## Обзор

Данный модуль содержит функции для определения корневой директории проекта и загрузки настроек из файла `settings.json`.  Он также предоставляет доступ к информации о проекте, такой как имя, версия, описание и автор.

## Функции

### `set_project_root`

**Описание**: Функция находит корневую директорию проекта, начиная с текущей директории, ищет вверх по директориям, пока не найдет директорию, содержащую файлы, указанные в аргументе `marker_files`.

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или каталогов, которые используются для определения корневой директории проекта. По умолчанию используются ('pyproject.toml', 'requirements.txt', '.git').

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена, иначе путь к директории, где расположен скрипт.

**Вызывает исключения**:

- Нет

### Загрузка настроек из `settings.json`


**Описание**: Данный код загружает настройки из файла `settings.json` в переменную `settings` и обрабатывает возможные исключения.

**Возвращает**:

- `settings` (dict): Словарь с настройками из файла `settings.json`. Если файл не найден или не удалось загрузить данные, возвращает `None`.


## Использование

```python
from hypotez.src.suppliers.gearbest.header import set_project_root

# Находим корневую директорию проекта
root_dir = set_project_root()
print(f"Root directory: {root_dir}")
```


## Переменные

### `__root__`

**Описание**: Переменная, содержащая путь к корневой директории проекта. Она инициализируется функцией `set_project_root`.

**Тип**: `Path`

### `settings`

**Описание**: Переменная, содержащая словарь с настройками проекта. Загружается из файла `settings.json`.


**Тип**: `dict`


### `doc_str`

**Описание**: Переменная, содержащая строку с описанием проекта из файла `README.MD`.

**Тип**: `str`

### `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`

**Описание**: Переменные, содержащие информацию о проекте (название, версия, описание, автор, права, ссылка на поддержку). Значения берутся из `settings` или устанавливаются по умолчанию.

**Тип**: `str`


## Обработка исключений

Код содержит обработку исключений `FileNotFoundError` и `json.JSONDecodeError` при чтении файлов `settings.json` и `README.MD`.  Если файл не найден или не удалось обработать его содержимое, соответствующие переменные (`settings`, `doc_str`) остаются с первоначальными значениями (`None`, `''`).

```

```
```