# Модуль `header.py`

## Обзор

Модуль `header.py` предназначен для настройки окружения проекта, включая определение корневой директории, загрузку настроек из файла `settings.json` и чтение документации из файла `README.MD`. Также модуль определяет общие переменные проекта, такие как имя, версия, автор и т.д.

## Оглавление

1. [Обзор](#обзор)
2. [Константы](#константы)
3. [Функции](#функции)
    - [`set_project_root`](#set_project_root)
4. [Переменные](#переменные)
    - [`__root__`](#__root__)
    - [`settings`](#settings)
    - [`doc_str`](#doc_str)
    - [`__project_name__`](#__project_name__)
    - [`__version__`](#__version__)
    - [`__doc__`](#__doc__)
    - [`__details__`](#__details__)
    - [`__author__`](#__author__)
    - [`__copyright__`](#__copyright__)
    - [`__cofee__`](#__cofee__)

## Константы

### `MODE`
```python
MODE = 'dev'
```

**Описание**: Режим работы приложения. В данном случае установлен в 'dev'.

## Функции

### `set_project_root`

```python
def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
```

**Описание**:
Функция `set_project_root` находит корневую директорию проекта, начиная с текущего файла, двигаясь вверх по дереву директорий и останавливаясь на первой директории, содержащей любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple, optional): Кортеж с именами файлов или директорий, которые используются для идентификации корневой директории проекта. По умолчанию `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если она найдена, или директории, где расположен скрипт.

## Переменные

### `__root__`

```python
__root__: Path
```

**Описание**: Путь к корневой директории проекта.

### `settings`

```python
settings: dict | None
```
**Описание**: Словарь с настройками проекта, загруженный из файла `settings.json`. Может быть `None`, если файл не найден или не удается прочитать.

### `doc_str`

```python
doc_str: str | None
```

**Описание**: Строка с документацией проекта, загруженная из файла `README.MD`. Может быть `None`, если файл не найден или не удается прочитать.

### `__project_name__`

```python
__project_name__: str
```

**Описание**: Имя проекта. По умолчанию 'hypotez' или значение из `settings.json`, если доступно.

### `__version__`

```python
__version__: str
```
**Описание**: Версия проекта. Пустая строка или значение из `settings.json`, если доступно.

### `__doc__`

```python
__doc__: str
```

**Описание**: Документация проекта. Содержимое файла `README.MD` или пустая строка, если файл не найден.

### `__details__`

```python
__details__: str
```

**Описание**: Детальная информация о проекте. В данный момент - пустая строка.

### `__author__`

```python
__author__: str
```

**Описание**: Автор проекта. Пустая строка или значение из `settings.json`, если доступно.

### `__copyright__`

```python
__copyright__: str
```

**Описание**: Информация об авторских правах. Пустая строка или значение из `settings.json`, если доступно.

### `__cofee__`

```python
__cofee__: str
```

**Описание**: Строка с предложением поддержать разработчика чашкой кофе. По умолчанию или значение из `settings.json`, если доступно.