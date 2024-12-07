# Модуль hypotez/src/webdriver/bs/header.py

## Обзор

Этот модуль содержит функции для получения корневой директории проекта и загрузки настроек из файла settings.json. Он также загружает строку документации из файла README.MD.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с текущей директории и поднимаясь вверх по дереву директорий. Останавливается на первой директории, содержащей один из файлов-маркеров (pyproject.toml, requirements.txt, .git).

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или каталогов, которые используются для определения корневой директории проекта. По умолчанию содержит ('pyproject.toml', 'requirements.txt', '.git').

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если она найдена. В противном случае возвращает путь к директории, где находится скрипт.

**Вызывает исключения**:

- Не вызывает исключений.


### <details><summary>Дополнительные пояснения к функции set_project_root</summary>
  <p>
Функция `set_project_root` использует итерацию по родительским директориям для нахождения корневой директории проекта, а не только для проверки непосредственной директории. Она также добавляет найденную директорию в `sys.path`, что позволяет импортировать модули из корневой директории проекта.
</p>
</details>

## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта. Получается вызовом функции `set_project_root`.

**Тип**: `Path`


### `settings`

**Описание**: Словарь с настройками проекта. Загружается из файла `src/settings.json` в корневой директории проекта.

**Тип**: `dict` или `None`


### `doc_str`

**Описание**: Строка документации проекта. Загружается из файла `src/README.MD` в корневой директории проекта.

**Тип**: `str` или `None`


### `__project_name__`

**Описание**: Имя проекта. Получается из настроек `settings`, по умолчанию равно 'hypotez'.

**Тип**: `str`


### `__version__`

**Описание**: Версия проекта. Получается из настроек `settings`, по умолчанию равно пустой строке.

**Тип**: `str`


### `__doc__`

**Описание**: Документация проекта. Получается из `doc_str`, по умолчанию пустая строка.

**Тип**: `str`


### `__details__`

**Описание**: Дополнительные детали проекта. По умолчанию пустая строка.

**Тип**: `str`


### `__author__`

**Описание**: Автор проекта. Получается из настроек `settings`, по умолчанию пустая строка.

**Тип**: `str`


### `__copyright__`

**Описание**: Авторские права на проект. Получается из настроек `settings`, по умолчанию пустая строка.

**Тип**: `str`


### `__cofee__`

**Описание**: Ссылка на спонсорство разработчика. Получается из настроек `settings`, по умолчанию содержит ссылку.

**Тип**: `str`


## Обработка исключений

### Обработка `FileNotFoundError` и `json.JSONDecodeError`


При чтении файлов `settings.json` и `README.MD`, если файлы не найдены или содержат невалидный JSON, соответствующие переменные инициализируются как `None` или пустые строки, а обработка продолжается.
```