# Модуль hypotez/src/webdriver/playwright/header.py

## Обзор

Данный модуль содержит функции для определения корневой директории проекта и загрузки настроек из файла `settings.json`. Он также предоставляет доступ к информации о проекте, такой как имя, версия, документация и прочие детали.

## Функции

### `set_project_root`

**Описание**:  Определяет корневую директорию проекта, начиная с директории текущего файла и поднимаясь вверх по дереву директорий, пока не найдет директорию, содержащую один из указанных файлов (или директорий).

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, по которым определяется корневая директория проекта. По умолчанию включает `pyproject.toml`, `requirements.txt` и `.git`.

**Возвращает**:

- `Path`: Путь к корневой директории проекта. Если корневая директория не найдена, возвращается директория, где расположен текущий файл.

**Примечания**:  Добавляет корневую директорию проекта в `sys.path` для корректного импорта модулей.


###  Функции-константы

**Описание**: Данный модуль содержит глобальные константы (__project_name__, __version__, __doc__, __details__, __author__, __copyright__, __cofee__) для доступа к настройкам проекта.

**Параметры**:
- Нет

**Возвращает**:
- `str`: Значения констант.

**Примечания**: Значения инициализируются из файла `settings.json` или имеют значения по умолчанию. Если файл `settings.json` не найден или содержит невалидный JSON, значения констант остаются по умолчанию.



##  Обработка исключений

**Описание**: Модуль включает обработку возможных исключений при чтении файла `settings.json` и `README.MD`.

**Исключения**:

- `FileNotFoundError`: Исключение, возникающее, когда файл не найден.
- `json.JSONDecodeError`: Исключение, возникающее, если содержимое файла `settings.json` не является корректным JSON.

**Обработка исключений**:
В случае возникновения исключений, соответствующие переменные (settings, doc_str) устанавливаются в `None` или строку по умолчанию, сохраняя корректную работу программы.