# Модуль hypotez/src/suppliers/ksp/header.py

## Обзор

Данный модуль содержит функции для определения корневого каталога проекта и загрузки настроек из файла `settings.json`.  Он также обеспечивает доступ к документации проекта (README.md), если она существует.

## Функции

### `set_project_root`

**Описание**: Определяет корневой каталог проекта, начиная с текущего каталога и идя вверх по дереву директорий.  Ищет файлы или каталоги, перечисленные в параметре `marker_files`.

**Параметры**:

- `marker_files` (tuple): Кортеж, содержащий имена файлов или каталогов, по которым определяется корневой каталог проекта. По умолчанию содержит ('pyproject.toml', 'requirements.txt', '.git').

**Возвращает**:

- `Path`: Путь к корневому каталогу проекта. Если корневой каталог не найден, возвращает текущий каталог.


**Пример использования**:

```python
root_path = set_project_root()
print(root_path)
```


### Загрузка настроек (`settings.json`)

**Описание**: Загружает настройки из файла `settings.json` в переменную `settings`.


**Возвращает**:

- `dict`: Словарь с настройками проекта.


**Обработка исключений**:

- `FileNotFoundError`: Если файл `settings.json` не найден.
- `json.JSONDecodeError`: Если файл `settings.json` имеет неверный формат JSON.

**Пример использования**:

```python
# ... (код для загрузки настроек)
if settings:
    print(settings['project_name'])
```

### Загрузка документации (README.MD)

**Описание**: Загружает текст из файла `README.MD` в переменную `doc_str`, если он существует.

**Возвращает**:

- `str`: Текст файла README.MD.

**Обработка исключений**:

- `FileNotFoundError`: Если файл `README.MD` не найден.
- `json.JSONDecodeError`: Если файл `README.MD` имеет неверный формат.

**Пример использования**:

```python
# ... (код для загрузки документации)
if doc_str:
   print(doc_str)
```


## Переменные

### `__root__`

**Описание**: Путь к корневому каталогу проекта.


### `__project_name__`

**Описание**: Название проекта. Значение взято из `settings.json` или установлено по умолчанию как 'hypotez'.

### `__version__`

**Описание**: Версия проекта. Значение взято из `settings.json` или установлено по умолчанию как пустая строка.

### `__doc__`

**Описание**: Текст из файла `README.MD` или пустая строка.

### `__details__`

**Описание**: Подробная информация о проекте (по умолчанию пустая строка).

### `__author__`

**Описание**: Автор проекта. Значение взято из `settings.json` или установлено по умолчанию как пустая строка.

### `__copyright__`

**Описание**: Авторские права на проект. Значение взято из `settings.json` или установлено по умолчанию как пустая строка.

### `__cofee__`

**Описание**: Ссылка на возможность поддержать разработчиков. Значение взято из `settings.json` или установлено по умолчанию как ссылка.