# Модуль hypotez/src/gui/header.py

## Обзор

Данный модуль отвечает за определение корневого пути к проекту `hypotez`.  Он находит директорию с файлами `pyproject.toml`, `requirements.txt` или `.git` и добавляет ее в `sys.path`, что позволяет корректно импортировать модули из других частей проекта.  Модуль также загружает настройки из файла `settings.json` и документацию из `README.MD`.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с текущей директории и поднимаясь вверх по древу директорий.

**Параметры**:

- `marker_files` (tuple, optional): Кортеж имен файлов или директорий, по которым определяется корень проекта. По умолчанию `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневой директории проекта. Если корневая директория не найдена, возвращает путь к директории, где расположен данный скрипт.

**Вызывает исключения**:

- Нет.


## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта, полученный с помощью функции `set_project_root()`.


### `settings`

**Описание**: Словарь, содержащий настройки проекта, загруженные из файла `settings.json`.

**Возвращает**:

- `dict`: Словарь настроек или `None`, если файл `settings.json` не найден или содержит некорректные данные.


### `doc_str`

**Описание**: Строка, содержащая содержимое файла `README.MD`.

**Возвращает**:

- `str`: Строка с содержимым `README.MD` или `None`, если файл `README.MD` не найден или содержит некорректные данные.


### `__project_name__`

**Описание**: Название проекта, полученное из `settings` или имеющее значение `'hypotez'` по умолчанию.

**Возвращает**:

- `str`: Строка, содержащая имя проекта.


### `__version__`

**Описание**: Версия проекта, полученная из `settings` или пустая строка по умолчанию.

**Возвращает**:

- `str`: Строка, содержащая версию проекта.


### `__doc__`

**Описание**: Документация к проекту, взятая из файла `README.MD` или пустая строка по умолчанию.

**Возвращает**:

- `str`: Строка, содержащая документацию к проекту.


### `__details__`

**Описание**: Подробная информация о проекте (по умолчанию пустая строка).

**Возвращает**:

- `str`: Строка, содержащая подробную информацию о проекте.


### `__author__`

**Описание**: Автор проекта, полученный из `settings` или пустая строка по умолчанию.

**Возвращает**:

- `str`: Строка, содержащая имя автора.


### `__copyright__`

**Описание**: Авторские права, полученные из `settings` или пустая строка по умолчанию.

**Возвращает**:

- `str`: Строка, содержащая информацию об авторских правах.


### `__cofee__`

**Описание**: Ссылка на страницу сбора средств на кофе для разработчика (по умолчанию - ссылка на Boosty).

**Возвращает**:
- `str`: Строка с ссылкой на страницу для поддержки разработчика.