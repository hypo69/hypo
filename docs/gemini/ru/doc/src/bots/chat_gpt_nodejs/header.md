# Модуль `hypotez/src/bots/openai_bots/header.py`

## Обзор

Этот модуль содержит вспомогательные функции для работы с проектом `hypotez`, включая определение корневой директории проекта, загрузку настроек из файла `settings.json` и чтение документации из файла `README.MD`.  Модуль использует библиотеку `packaging` для работы с версиями.

## Функции

### `set_project_root`

**Описание**:  Находит корневую директорию проекта, начиная от текущего файла. Поиск осуществляется вверх по директориям до тех пор, пока не будет найдена директория, содержащая указанные файлы-маркеры.

**Параметры**:

- `marker_files` (tuple): Кортеж с именами файлов или каталогов, которые указывают на корневую директорию проекта. По умолчанию это `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если она найдена, иначе путь к директории, где находится текущий скрипт.

**Вызывает исключения**:
- Нет.

### <ins>Другие переменные (не функции)</ins>

**Описание**:

- `__root__`: Путь к корневой директории проекта.
- `settings`: Словарь с настройками проекта (загружается из `settings.json`).
- `doc_str`: Строка документации проекта (читается из `README.MD`).
- `__project_name__`: Имя проекта, полученное из настроек или по умолчанию `hypotez`.
- `__version__`: Версия проекта, полученная из настроек или по умолчанию пустая строка.
- `__doc__`: Документация проекта.
- `__details__`:  Детали проекта (по умолчанию пустая строка).
- `__author__`: Автор проекта, полученный из настроек или по умолчанию пустая строка.
- `__copyright__`: Авторские права, полученные из настроек или по умолчанию пустая строка.
- `__cofee__`: Ссылка на поддержку разработчика через платформа boosty.


**Обработка исключений**:

Код содержит обработку исключений `FileNotFoundError` и `json.JSONDecodeError` при чтении файлов `settings.json` и `README.MD`. При возникновении исключений соответствующие переменные не изменяются.


## Файлы, используемые модулем

- `settings.json`: Файл, содержащий настройки проекта.
- `README.MD`: Файл, содержащий документацию проекта.

##  Дополнительные замечания

- Модуль использует `Path` для работы с путями, что повышает надежность и кросс-платформенность.
- Переменные, начинающиеся с `__`, являются внутренними переменными и не предназначены для прямого доступа извне.
- Модуль использует библиотеку `packaging` для работы с версиями.