# Модуль hypotez/src/endpoints/advertisement/facebook/header.py

## Обзор

Этот модуль содержит функции для определения корневого каталога проекта и загрузки настроек из файла `settings.json`. Он также предоставляет доступ к документации проекта (README.md) и различным метаданным проекта, таким как имя проекта, версия, описание, автор и информация об авторах.

## Функции

### `set_project_root`

**Описание**: Находит корневой каталог проекта, начиная с каталога текущего файла. Поиск выполняется вверх по иерархии каталогов, пока не будет найден каталог, содержащий указанные файлы-маркеры.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или каталогов, используемых для определения корневого каталога проекта. По умолчанию `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневому каталогу проекта, если найден, иначе путь к каталогу, где расположен текущий файл.

**Вызывает исключения**:

- Нет.


## Переменные

### `MODE`

**Описание**: Строковая переменная, хранящая режим работы проекта. По умолчанию `'dev'`.

### `__root__`

**Описание**: Путь к корневому каталогу проекта, полученный из функции `set_project_root`.

### `settings`

**Описание**: Словарь с настройками проекта, загруженными из файла `settings.json`.

**Значение по умолчанию**: `None`


### `doc_str`

**Описание**: Строка, содержащая содержимое файла `README.MD`, если он существует.

**Значение по умолчанию**: `None`


### `__project_name__`

**Описание**: Имя проекта.  Получается из настроек (`settings`) если они успешно загружены, иначе значение по умолчанию `'hypotez'`.

### `__version__`

**Описание**: Версия проекта. Получается из настроек (`settings`) если они успешно загружены, иначе значение по умолчанию `''`.

### `__doc__`

**Описание**: Описание проекта. Получается из файла `README.MD` (`doc_str`), если он успешно загружен, иначе значение по умолчанию `''`.


### `__details__`

**Описание**: Подробная информация о проекте. По умолчанию `''`.

### `__author__`

**Описание**: Автор проекта. Получается из настроек (`settings`) если они успешно загружены, иначе значение по умолчанию `''`.


### `__copyright__`

**Описание**: Авторские права на проект. Получается из настроек (`settings`) если они успешно загружены, иначе значение по умолчанию `''`.

### `__cofee__`

**Описание**: Ссылка для поддержки разработчика. Получается из настроек (`settings`) если они успешно загружены, иначе значение по умолчанию `"Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"`.


## Обработка исключений

Модуль использует `try...except` блоки для обработки `FileNotFoundError` и `json.JSONDecodeError` при работе с файлами `settings.json` и `README.MD`, обеспечивая устойчивость к различным ошибкам.

```