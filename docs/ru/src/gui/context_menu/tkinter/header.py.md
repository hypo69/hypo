# Модуль `header.py`

## Обзор

Модуль `header.py` предназначен для настройки окружения и импорта необходимых модулей для работы с контекстным меню в GUI на базе Tkinter.

## Содержание

- [Обзор](#обзор)
- [Импорты](#импорты)
- [Переменные](#переменные)

## Импорты

В модуле импортируются следующие библиотеки:
- `sys`: Для работы с системными переменными и путями.
- `os`: Для работы с операционной системой, например, для получения текущей директории.
- `pathlib.Path`: Для работы с путями к файлам и директориям в объектно-ориентированном стиле.

## Переменные

### `__root__`
**Описание**: Переменная `__root__` определяет корневой путь проекта `hypotez`.
**Тип**: `pathlib.Path`
```python
__root__ : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
```

### `sys.path`
**Описание**: Модифицирует `sys.path` для включения корневой директории проекта в список путей поиска модулей.
```python
sys.path.append (__root__)