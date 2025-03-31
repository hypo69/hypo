# Модуль `src.utils.path`

## Обзор

Модуль `src.utils.path` предназначен для определения корневого пути к проекту и получения относительных путей. Это позволяет строить все импорты относительно этого пути.

## Подробней

Модуль содержит функцию `get_relative_path`, которая извлекает часть пути, начиная с указанного сегмента. Это полезно для работы с файловой системой и определения местоположения файлов относительно корня проекта.

## Функции

### `get_relative_path`

```python
def get_relative_path(full_path: str, relative_from: str) -> Optional[str]:
    """
    Возвращает часть пути начиная с указанного сегмента и до конца.

    Args:
        full_path (str): Полный путь.
        relative_from (str): Сегмент пути, с которого нужно начать извлечение.

    Returns:
        Optional[str]: Относительный путь начиная с `relative_from`, или None, если сегмент не найден.
    """
    ...
```

**Как работает функция**:

1. Функция принимает два строковых аргумента: `full_path` (полный путь к файлу или каталогу) и `relative_from` (сегмент пути, начиная с которого нужно извлечь относительный путь).
2. Преобразует входные строки в объекты `Path` для удобства работы с путями.
3. Разбивает полный путь на отдельные компоненты (сегменты).
4. Проверяет, содержится ли сегмент `relative_from` в компонентах полного пути.
5. Если сегмент найден, определяет его индекс и формирует новый путь, начиная с этого индекса и до конца.
6. Возвращает относительный путь в виде строки, используя метод `as_posix()`, который обеспечивает переносимость между операционными системами.
7. Если сегмент `relative_from` не найден в полном пути, функция возвращает `None`.

**Параметры**:

- `full_path` (str): Полный путь к файлу или каталогу.
- `relative_from` (str): Сегмент пути, начиная с которого нужно извлечь относительный путь.

**Возвращает**:

- `Optional[str]`: Относительный путь, начиная с `relative_from`, или `None`, если сегмент не найден.

**Примеры**:

```python
from pathlib import Path
from src.utils.path import get_relative_path

full_path = "/home/user/project/src/module/file.py"
relative_from = "src"
relative_path = get_relative_path(full_path, relative_from)
print(relative_path)  # Вывод: src/module/file.py

full_path = "/home/user/project/src/module/file.py"
relative_from = "nonexistent"
relative_path = get_relative_path(full_path, relative_from)
print(relative_path)  # Вывод: None