# Модуль hypotez/src/webdriver/header.py

## Обзор

Этот модуль содержит код для определения корневого каталога проекта, загрузки настроек из файла `settings.json` и получения документации из файла `README.MD`.  Он также определяет переменные, содержащие информацию о проекте, такие как имя, версия, автор и т.д., которые могут быть использованы другими частями кодовой базы.

## Функции

### `set_project_root`

**Описание**: Определяет корневой каталог проекта, начиная с текущей директории и двигаясь вверх по иерархии директорий.  Останавливается на первой директории, содержащей один из указанных файлов-маркеров (pyproject.toml, requirements.txt, .git).

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, используемых для определения корневого каталога проекта. По умолчанию используется кортеж `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если она найдена. В противном случае возвращает директорию, в которой находится исполняемый файл.

**Вызывает исключения**:

- Не вызывает исключений.


## Переменные

### `__root__`

**Описание**: Путь к корневому каталогу проекта, полученный с помощью функции `set_project_root`.  

### `settings`

**Описание**: Словарь настроек, загруженный из файла `settings.json`.  Возможны значения `None` если файл не найден или некорректен.

**Вызывает исключения**:

- `FileNotFoundError`: Возникает, если файл `settings.json` не найден.
- `json.JSONDecodeError`: Возникает, если файл `settings.json` содержит некорректный JSON.

### `doc_str`

**Описание**: Строка документации, полученная из файла `README.MD`.  Возможны значения `None` если файл не найден или некорректен.

**Вызывает исключения**:

- `FileNotFoundError`: Возникает, если файл `README.MD` не найден.
- `json.JSONDecodeError`: Возникает, если файл `README.MD` содержит некорректный формат.



### `__project_name__`

**Описание**: Имя проекта, полученное из настроек (`settings`). По умолчанию `hypotez`.


### `__version__`

**Описание**: Версия проекта, полученная из настроек (`settings`). По умолчанию пустая строка.


### `__doc__`

**Описание**: Строка документации (README.md), полученная из настроек (`settings`). По умолчанию пустая строка.


### `__details__`

**Описание**: Строка дополнительных деталей (пустая по умолчанию).


### `__author__`

**Описание**: Автор проекта, полученный из настроек (`settings`). По умолчанию пустая строка.


### `__copyright__`

**Описание**: Авторские права, полученные из настроек (`settings`). По умолчанию пустая строка.


### `__cofee__`

**Описание**:  Ссылка на поддержку разработчика (кофе). Получена из настроек (`settings`). По умолчанию ссылка на платформу поддержки разработчика.