# Модуль `src.utils.path`

## Обзор

Модуль `src.utils.path` предназначен для определения корневого пути к проекту. Все импорты в проекте строятся относительно этого пути. В дальнейшем планируется перенести определение корневого пути в системную переменную.

## Подробней

Модуль содержит функцию `get_relative_path`, которая позволяет получить относительный путь к файлу или каталогу, начиная с определенного сегмента пути. Это полезно для работы с путями в проекте, когда необходимо получить путь относительно корневой директории или другого известного сегмента.

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

Функция `get_relative_path` принимает полный путь (`full_path`) и сегмент пути (`relative_from`), начиная с которого нужно извлечь относительный путь. Функция преобразует входные строки в объекты `Path` для удобства работы с путями. Затем она ищет индекс сегмента `relative_from` в частях полного пути. Если сегмент найден, функция формирует новый путь, начиная с найденного сегмента и до конца пути, и возвращает его в виде строки, используя `as_posix()`. Если сегмент `relative_from` не найден в полном пути, функция возвращает `None`.

**Параметры**:

- `full_path` (str): Полный путь к файлу или каталогу.
- `relative_from` (str): Сегмент пути, с которого нужно начать извлечение относительного пути.

**Возвращает**:

- `Optional[str]`: Относительный путь, начиная с `relative_from`, или `None`, если сегмент не найден.

**Примеры**:

```python
from pathlib import Path
from src.utils.path import get_relative_path

# Пример 1: Получение относительного пути от существующего сегмента
full_path = "/home/user/project/src/utils/path.py"
relative_from = "src"
relative_path = get_relative_path(full_path, relative_from)
print(f"Относительный путь: {relative_path}")  # Вывод: Относительный путь: src/utils/path.py

# Пример 2: Сегмент не найден
full_path = "/home/user/project/src/utils/path.py"
relative_from = "config"
relative_path = get_relative_path(full_path, relative_from)
print(f"Относительный путь: {relative_path}")  # Вывод: Относительный путь: None

# Пример 3: Использование pathlib.Path object
full_path = Path("/home/user/project/src/utils/path.py")
relative_from = "project"
relative_path = get_relative_path(str(full_path), relative_from)
print(f"Относительный путь: {relative_path}")  # Вывод: Относительный путь: project/src/utils/path.py