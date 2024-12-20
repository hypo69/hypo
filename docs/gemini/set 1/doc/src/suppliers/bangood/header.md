# Модуль hypotez/src/suppliers/bangood/header.py

## Обзор

Данный модуль предоставляет функции для работы с настройками проекта, получения корневой директории проекта и доступа к дополнительной информации (например, README, версия проекта, автор).  Он инициализирует переменные, содержащие информацию о проекте, загружая данные из файла `settings.json` и, при необходимости, из файла `README.MD`.

## Функции

### `set_project_root`

**Описание**:  Находит корневую директорию проекта, начиная от текущего файла и идя вверх по директориям, пока не найдёт файл из переданного списка.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, используемых для определения корневой директории. По умолчанию содержит (`pyproject.toml`, `requirements.txt`, `.git`).


**Возвращает**:

- `Path`: Путь к корневой директории проекта. Если корневая директория не найдена, возвращает директорию, в которой расположен текущий файл.


**Вызывает исключения**:

-  Не вызывает никаких исключений.


###  Другие переменные

**Описание**: Данный модуль инициализирует ряд глобальных переменных, хранящих информацию о проекте: `__root__`, `settings`, `doc_str`, `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`.  Эти переменные получают свои значения из файла `settings.json` и/или `README.MD`,  или задаются по умолчанию, если файлы отсутствуют или содержат ошибки.


**Переменные**:
- `__root__`: `Path`, путь к корневой директории проекта, полученный из функции `set_project_root`.
- `settings`: `dict`, словарь с настройками проекта, загруженный из файла `settings.json`.
- `doc_str`: `str`, содержимое файла `README.MD`.
- `__project_name__`: `str`, имя проекта, полученное из `settings.json` или по умолчанию.
- `__version__`: `str`, версия проекта, полученная из `settings.json` или по умолчанию.
- `__doc__`: `str`, содержимое файла `README.MD` или пустая строка, если файл отсутствует или содержит ошибки.
- `__details__`: `str`, дополнительная информация о проекте (по умолчанию пустая строка).
- `__author__`: `str`, автор проекта, полученный из `settings.json` или по умолчанию.
- `__copyright__`: `str`, авторские права, полученные из `settings.json` или по умолчанию.
- `__cofee__`: `str`, ссылка на бонусную поддержку разработчика, полученная из `settings.json` или по умолчанию.


**Обработка исключений**:

- В блоках `try...except` обрабатываются `FileNotFoundError` и `json.JSONDecodeError` для предотвращения аварийного завершения программы при отсутствии или некорректном формате файлов `settings.json` и `README.MD`.  В случае ошибки эти переменные устанавливаются в значение по умолчанию.