# Модуль hypotez/src/suppliers/bangood/header.py

## Обзор

Этот модуль содержит функции для определения корневого каталога проекта, загрузки настроек из файла `settings.json` и чтения документации из файла `README.MD`.  Он также предоставляет переменные, содержащие информацию о проекте (название, версия, автор и т.д.).

## Функции

### `set_project_root`

**Описание**:  Находит корневой каталог проекта, начиная с текущей директории и двигаясь вверх по иерархии директорий.  Ищет файлы или директории, указанные в аргументе `marker_files`.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, которые используются для определения корневого каталога проекта.  По умолчанию содержит `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Объект `Path` представляющий путь к корневому каталогу проекта. Если корневой каталог не найден, возвращает директорию, где находится текущий файл.

**Вызывает исключения**:

Нет.


## Переменные

### `__root__`

**Описание**:  Содержит объект `Path` представляющий корневой каталог проекта, полученный вызовом функции `set_project_root()`.


### `settings`

**Описание**: Словарь, содержащий настройки проекта, загруженные из файла `settings.json` в корневом каталоге проекта.  Значение по умолчанию `None`.


### `doc_str`

**Описание**: Строка, содержащая содержимое файла `README.MD` в корневом каталоге проекта. Значение по умолчанию `None`.


### `__project_name__`

**Описание**: Название проекта, полученное из настроек (`settings`). Значение по умолчанию `hypotez`.


### `__version__`

**Описание**: Версия проекта, полученное из настроек (`settings`). Значение по умолчанию пустая строка.


### `__doc__`

**Описание**: Документация проекта, полученная из файла `README.MD`. Значение по умолчанию пустая строка.


### `__details__`

**Описание**:  Дополнительные детали о проекте. Значение по умолчанию пустая строка.


### `__author__`

**Описание**: Автор проекта, полученное из настроек (`settings`). Значение по умолчанию пустая строка.


### `__copyright__`

**Описание**: Авторские права на проект, полученное из настроек (`settings`). Значение по умолчанию пустая строка.


### `__cofee__`

**Описание**: Ссылка на поддержку разработчика через платёжную систему boosty. Значение по умолчанию – строка с ссылкой.


## Обработка исключений

В модуле используется конструкция `try...except` для обработки `FileNotFoundError` и `json.JSONDecodeError` при чтении файла `settings.json` и `README.MD`.  В случае ошибки, соответствующие переменные не заполняются и сохраняют значение `None` или пустую строку.