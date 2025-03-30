# Модуль `header`

## Обзор

Модуль `header.py` предназначен для определения основных параметров проекта `hypotez`, таких как версия, имя, автор и т. д. Он также отвечает за поиск корневой директории проекта и загрузку настроек из файла `settings.json`.

## Подробней

Данный модуль выполняет следующие задачи:

1.  Определение корневой директории проекта с помощью функции `set_project_root`.
2.  Чтение настроек проекта из файла `settings.json`.
3.  Определение основных параметров проекта, таких как имя, версия, автор и т. д.

Этот модуль важен для инициализации проекта и обеспечения доступа к основным настройкам и параметрам.

## Функции

### `set_project_root`

```python
def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
    ...
```

**Описание**: Находит корневой каталог проекта, начиная с каталога текущего файла, и останавливается на первом каталоге, содержащем любой из маркерных файлов.

**Параметры**:

*   `marker_files` (tuple): Имена файлов или каталогов для идентификации корня проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:

*   `Path`: Путь к корневому каталогу, если он найден, иначе каталог, в котором расположен скрипт.

**Примеры**:

```python
from pathlib import Path
root_path = set_project_root()
print(f'Root path: {root_path}')
```

## Переменные

### `__root__`

```python
__root__: Path = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""
```

**Описание**: Содержит путь к корневой директории проекта. Вычисляется с помощью функции `set_project_root`.

### `settings`

```python
settings: dict = None
```

**Описание**: Словарь с настройками проекта, загруженными из файла `settings.json`.

### `__project_name__`

```python
__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
```

**Описание**: Имя проекта, извлеченное из файла `settings.json`. Если значение не найдено, используется значение по умолчанию `'hypotez'`.

### `__version__`

```python
__version__: str = settings.get("version", '') if settings else ''
```

**Описание**: Версия проекта, извлеченная из файла `settings.json`. Если значение не найдено, используется значение по умолчанию `''`.

### `__doc__`

```python
__doc__: str = doc_str if doc_str else ''
```

**Описание**: Содержимое файла `README.MD`, используемое как документация проекта. Если файл не найден, используется пустая строка.

### `__author__`

```python
__author__: str = settings.get("author", '') if settings else ''
```

**Описание**: Автор проекта, извлеченный из файла `settings.json`. Если значение не найдено, используется значение по умолчанию `''`.

### `__copyright__`

```python
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
```

**Описание**: Информация об авторских правах проекта, извлеченная из файла `settings.json`. Если значение не найдено, используется значение по умолчанию `''`.

### `__cofee__`

```python
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```

**Описание**: Сообщение с предложением угостить разработчика кофе, извлеченное из файла `settings.json`. Если значение не найдено, используется значение по умолчанию `"Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"`.