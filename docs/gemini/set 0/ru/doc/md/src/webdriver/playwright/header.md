# Модуль hypotez/src/webdriver/playwright/header.py

## Обзор

Этот модуль содержит вспомогательные функции для работы с проектом, включая определение корневой директории проекта, загрузку настроек из файла `settings.json` и чтение документации из файла `README.MD`.

## Функции

### `set_project_root`

**Описание**: Определяет корневую директорию проекта, начиная с директории текущего файла. Поиск происходит вверх по директориям до тех пор, пока не будет найдена директория, содержащая один из файлов, указанных в аргументе `marker_files`.

**Параметры**:

- `marker_files` (tuple): Кортеж из имен файлов или каталогов, используемых для определения корневой директории проекта. По умолчанию `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена, иначе директорию, в которой расположен текущий скрипт.


###  `set_project_root`

**Описание**: Определяет корневую директорию проекта, начиная с директории текущего файла. Поиск происходит вверх по директориям до тех пор, пока не будет найдена директория, содержащая один из файлов, указанных в аргументе `marker_files`.

**Параметры**:

- `marker_files` (tuple): Кортеж из имен файлов или каталогов, используемых для определения корневой директории проекта. По умолчанию `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена, иначе директорию, в которой расположен текущий скрипт.


**Примечания**:
- Если найденная корневая директория отсутствует в пути поиска `sys.path`, она добавляется в начало этого списка.


## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта, полученный с помощью функции `set_project_root()`.


## Загрузка настроек

**Описание**: Загрузка настроек из файла `settings.json` в переменную `settings`.

**Обработка ошибок**:

- `FileNotFoundError`: Если файл `settings.json` не найден.
- `json.JSONDecodeError`: Если файл `settings.json` имеет некорректный формат JSON.


## Чтение документации

**Описание**: Чтение документации из файла `README.MD` в переменную `doc_str`.

**Обработка ошибок**:

- `FileNotFoundError`: Если файл `README.MD` не найден.
- `UnicodeDecodeError`: Если файл `README.MD` не может быть декодирован в UTF-8.


## Переменные (глобальные)

### `__project_name__`
**Описание:** Название проекта, полученное из настроек или установленное по умолчанию в `hypotez`.

### `__version__`
**Описание:** Версия проекта, полученная из настроек или установленная по умолчанию в пустую строку.

### `__doc__`
**Описание:** Текст документации из `README.MD`, если найден, иначе пустая строка.

### `__details__`
**Описание:** Дополнительные детали (по умолчанию пустая строка).

### `__author__`
**Описание:** Автор проекта, полученный из настроек или установленный по умолчанию в пустую строку.

### `__copyright__`
**Описание:** Авторские права проекта, полученный из настроек или установленный по умолчанию в пустую строку.

### `__cofee__`
**Описание:** Ссылка на поддержку разработчика (по умолчанию ссылка на Boosty).