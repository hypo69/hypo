# Модуль hypotez/src/logger

## Обзор

Модуль `src.logger` определяет корневой путь к проекту `hypotez`. Все импорты строятся относительно этого пути. В дальнейшем путь будет передан в системную переменную.

## Функции

### `set_project_root`

**Описание**: Находит корневой каталог проекта, начиная с текущего каталога файла, поднимаясь вверх по каталогам и останавливаясь на первом каталоге, содержащем указанные файлы-маркеры.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или каталогов, используемых для определения корневого каталога проекта. По умолчанию `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневому каталогу проекта, если найден, в противном случае возвращает каталог, где находится скрипт.

**Вызывает исключения**:

- Нет.


## Переменные

### `__root__`

**Описание**: Путь к корневому каталогу проекта. Получается с помощью функции `set_project_root`.


## Обработка настроек

**Описание**: Загружает настройки из файла `settings.json` в корневой директории проекта.

**Возможные ошибки**:

- `FileNotFoundError`: Если файл `settings.json` не найден.
- `json.JSONDecodeError`: Если содержимое файла `settings.json` не является валидным JSON.


## Документация проекта

**Описание**: Загружает строку документации из файла `README.MD` в корневой директории проекта.

**Возможные ошибки**:

- `FileNotFoundError`: Если файл `README.MD` не найден.
- `json.JSONDecodeError`: Если содержимое файла `README.MD` не является валидным текстом.


## Конфигурация

**Описание**: Определяет следующие константы из файла настроек `settings.json`, или использует значения по умолчанию, если файл не найден или некорректен:
- `__project_name__`
- `__version__`
- `__doc__`
- `__details__`
- `__author__`
- `__copyright__`
- `__cofee__`


```