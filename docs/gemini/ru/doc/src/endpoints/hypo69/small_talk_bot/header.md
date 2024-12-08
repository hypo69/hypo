# Модуль hypotez/src/endpoints/hypo69/small_talk_bot/header.py

## Обзор

Этот модуль содержит функции для определения корневой директории проекта, загрузки настроек из файла `settings.json` и документации из `README.MD`. Он также предоставляет переменные, содержащие информацию о проекте, такие как название, версия, описание и автор.

## Оглавление

- [Функции](#функции)
    - [`set_project_root`](#set_project_root)

## Функции

### `set_project_root`

**Описание**: Определяет корневую директорию проекта, начиная от директории текущего файла.  Ищет вверх по дереву директорий, пока не найдет директорию содержащую один из маркеров `marker_files`.

**Параметры**:
- `marker_files` (tuple): Кортеж имен файлов или директорий, используемых для определения корневой директории проекта. По умолчанию `('pyproject.toml', 'requirements.txt', '.git')`.


**Возвращает**:
- `Path`: Путь к корневой директории проекта.  Если корневая директория не найдена, возвращается директория, в которой находится текущий файл.


**Пример использования**:

```python
root_path = set_project_root()
print(root_path)
```

**Обрабатываемые исключения**:
-  (Нет обработанных исключений)


### Загрузка настроек

**Описание**: Загружает настройки из файла `settings.json` в переменную `settings`.

**Обрабатываемые исключения**:
- `FileNotFoundError`: Возникает, если файл `settings.json` не найден.
- `json.JSONDecodeError`: Возникает, если файл `settings.json` содержит некорректный JSON.

### Загрузка документации

**Описание**: Загружает текстовую информацию из файла `README.MD` в переменную `doc_str`.

**Обрабатываемые исключения**:
- `FileNotFoundError`: Возникает, если файл `README.MD` не найден.
- `json.JSONDecodeError`: Возникает, если файл `README.MD` содержит некорректный формат текста.

## Переменные

- `__root__` (Path): Путь к корневой директории проекта.
- `settings` (dict): Словарь с настройками проекта.
- `doc_str` (str): Текст документации из файла `README.MD`.
- `__project_name__` (str): Название проекта.
- `__version__` (str): Версия проекта.
- `__doc__` (str): Документация проекта.
- `__details__` (str): Дополнительные детали о проекте.
- `__author__` (str): Автор проекта.
- `__copyright__` (str): Авторские права.
- `__cofee__` (str): Ссылка для поддержки разработчика.