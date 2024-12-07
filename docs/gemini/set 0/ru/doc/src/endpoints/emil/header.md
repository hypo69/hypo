# Модуль hypotez/src/endpoints/emil/header.py

## Обзор

Данный модуль содержит функции для определения корневой директории проекта, загрузки настроек из файла `settings.json` и получения документации из файла `README.MD`.  Он также инициализирует переменные, содержащие информацию о проекте (название, версия, описание, автор и т.д.).

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная от текущей директории и идя вверх по дереву директорий.  Использует список файлов/директорий `marker_files` для определения корня проекта.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, по которым определяется корневая директория проекта. По умолчанию содержит `('pyproject.toml', 'requirements.txt', '.git')`.


**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена, иначе — текущая директория.

**Вызывает исключения**:

- Нет.

## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта. Инициализируется функцией `set_project_root()`.


### `settings`

**Описание**: Словарь настроек, загруженный из файла `settings.json` в корневой директории проекта.

### `doc_str`

**Описание**: Текстовое содержимое файла `README.MD`, содержащее описание проекта.

### `__project_name__`

**Описание**: Имя проекта. Получается из `settings.json` или имеет значение по умолчанию "hypotez".


### `__version__`

**Описание**: Версия проекта. Получается из `settings.json` или имеет значение по умолчанию пустую строку.

### `__doc__`

**Описание**: Документация проекта. Получается из файла `README.MD`.

### `__details__`

**Описание**: Подробная информация о проекте.

### `__author__`

**Описание**: Автор проекта. Получается из `settings.json`.


### `__copyright__`

**Описание**: Авторские права. Получается из `settings.json`.

### `__cofee__`

**Описание**: Ссылка для поддержки разработчика.

## Обработка исключений

В коде используются `try...except` блоки для обработки потенциальных ошибок при чтении файла `settings.json` и `README.MD`:

- `FileNotFoundError`: Если файл не найден.
- `json.JSONDecodeError`: Если содержимое файла некорректный JSON.