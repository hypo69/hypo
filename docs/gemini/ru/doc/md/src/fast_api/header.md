# Модуль hypotez/src/fast_api/header.py

## Обзор

Этот модуль содержит функции для определения корневой директории проекта и загрузки настроек из файла `settings.json`, а также для загрузки документации из файла `README.MD`. Он использует `pathlib` для работы с путями и `json` для работы с JSON-файлами. Модуль инициализирует переменные, содержащие информацию о проекте, такие как имя, версия, описание, автор, авторские права и ссылку на платформу поддержки разработчиков.


## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с текущей директории и продвигаясь вверх по дереву директорий, пока не найдёт директорию, содержащую один из указанных маркеров (файлов или директорий).

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или директорий, которые будут использоваться в качестве маркеров корневой директории. По умолчанию: `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Объект `Path` представляющий путь к корневой директории проекта, если она найдена, в противном случае - директорию, в которой находится текущий скрипт.

**Вызывает исключения**:

- Нет.


## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта, полученный с помощью функции `set_project_root()`.


### `settings`

**Описание**: Словарь, содержащий настройки проекта, загруженный из файла `src/settings.json`.


### `doc_str`

**Описание**: Строка, содержащая текст документации, загруженный из файла `src/README.MD`.


### `__project_name__`

**Описание**: Строка, содержащая имя проекта, полученная из настроек (`settings`) или установленная по умолчанию ('hypotez').


### `__version__`

**Описание**: Строка, содержащая версию проекта, полученная из настроек (`settings`) или установленная по умолчанию ('').


### `__doc__`

**Описание**: Строка, содержащая описание проекта, полученная из документации (`doc_str`) или установленная по умолчанию ('').


### `__details__`

**Описание**: Строка, содержащая дополнительные сведения о проекте. По умолчанию пустая строка.


### `__author__`

**Описание**: Строка, содержащая имя автора проекта, полученная из настроек (`settings`) или установленная по умолчанию ('').


### `__copyright__`

**Описание**: Строка, содержащая авторские права на проект, полученная из настроек (`settings`) или установленная по умолчанию ('').


### `__cofee__`

**Описание**: Строка, содержащая ссылку на платформа для поддержки разработчика. По умолчанию - ссылка на boosty.


## Обработка исключений

В коде используются блоки `try...except` для обработки потенциальных ошибок:

- `FileNotFoundError`: Обрабатывает случаи, когда файл `settings.json` или `README.MD` не найден.
- `json.JSONDecodeError`: Обрабатывает случаи, когда файл `settings.json` не является валидным JSON.


## Модули

В модуле используются следующие модули:
- `sys`
- `json`
- `pathlib`
- `packaging.version`
- `src.gs`