# Модуль header.py

## Обзор

Этот модуль содержит функции для определения корневого каталога проекта и загрузки настроек из файла settings.json, а также документацию из файла README.MD. Он предназначен для инициализации переменных, используемых во всем проекте.


## Функции

### `set_project_root`

**Описание**: Находит корневой каталог проекта, начиная с текущего файла. Поиск осуществляется вверх по иерархии каталогов, пока не будет найден каталог, содержащий один из указанных файлов-маркеров (pyproject.toml, requirements.txt, .git).

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или каталогов, используемых для определения корневого каталога. По умолчанию включает pyproject.toml, requirements.txt и .git.


**Возвращает**:

- `Path`: Путь к корневому каталогу проекта, если найден. В противном случае возвращает каталог, где расположен текущий скрипт.


**Вызывает исключения**:

- Нет


### `__root__`
**Описание:** Переменная, содержащая путь к корневому каталогу проекта, полученный с помощью функции `set_project_root()`.


## Загрузка настроек

**Описание**: Загружает настройки из файла settings.json, расположенного в корневом каталоге проекта. Если файл не найден или содержит некорректный JSON, переменная `settings` остаётся `None`.


## Документация

**Описание**: Загружает содержимое файла README.md. Если файл не найден или содержит некорректные данные, `doc_str` устанавливается в пустую строку.


## Переменные

### `__project_name__`

**Описание**: Название проекта, полученное из настроек (`settings.json`) или установленное по умолчанию как 'hypotez'.

### `__version__`

**Описание**: Версия проекта, полученная из настроек (`settings.json`) или установленная по умолчанию как пустая строка.

### `__doc__`

**Описание**: Документация, полученная из файла README.MD (`README.MD`) или пустая строка, если файл не найден.

### `__details__`

**Описание**: Детали проекта, по умолчанию пустая строка.

### `__author__`

**Описание**: Автор проекта, полученный из настроек (`settings.json`) или пустая строка, если не указан.

### `__copyright__`

**Описание**: Авторские права, полученные из настроек (`settings.json`) или пустая строка, если не указаны.

### `__cofee__`

**Описание**: Ссылка на поддержку разработчика через платформu boosty.to, полученная из настроек (`settings.json`) или установленное по умолчанию.