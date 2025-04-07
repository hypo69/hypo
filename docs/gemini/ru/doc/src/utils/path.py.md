# Модуль `src.utils.path`

## Обзор

Модуль `src.utils.path` предназначен для определения корневого пути к проекту и предоставляет функцию для получения относительного пути из полного пути, начиная с указанного сегмента. Это позволяет строить импорты относительно этого пути.

## Подробней

Этот модуль содержит функцию `get_relative_path`, которая принимает полный путь и сегмент пути, начиная с которого нужно извлечь относительный путь. Если указанный сегмент найден в полном пути, функция возвращает относительный путь начиная с этого сегмента. В противном случае функция возвращает `None`.

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
```

**Назначение**: Возвращает относительный путь из полного пути, начиная с указанного сегмента.

**Параметры**:
- `full_path` (str): Полный путь.
- `relative_from` (str): Сегмент пути, с которого нужно начать извлечение.

**Возвращает**:
- `Optional[str]`: Относительный путь, начиная с `relative_from`, или `None`, если сегмент не найден.

**Как работает функция**:

1. Преобразует входные строки `full_path` и `relative_from` в объекты `Path` для удобства работы с путями.
2. Разделяет полный путь на отдельные компоненты (сегменты).
3. Проверяет, содержится ли сегмент `relative_from` в компонентах полного пути.
4. Если сегмент найден, определяет индекс этого сегмента и формирует новый путь, начиная с этого индекса и до конца.
5. Преобразует полученный относительный путь в строку в формате POSIX и возвращает его.
6. Если сегмент не найден, возвращает `None`.

```
A: Преобразование строк в объекты Path
|
B: Разделение полного пути на компоненты
|
C: Проверка наличия сегмента relative_from в компонентах
|
D: Определение индекса сегмента
|
E: Формирование относительного пути
|
F: Преобразование в строку и возврат
```

**Примеры**:

```python
from pathlib import Path
from src.utils.path import get_relative_path

# Пример 1: Сегмент найден
full_path = "/home/user/project/src/utils/path.py"
relative_from = "src"
relative_path = get_relative_path(full_path, relative_from)
print(relative_path)  # Вывод: src/utils/path.py

# Пример 2: Сегмент не найден
full_path = "/home/user/project/src/utils/path.py"
relative_from = "config"
relative_path = get_relative_path(full_path, relative_from)
print(relative_path)  # Вывод: None

# Пример 3: Использование pathlib.Path
full_path = Path("/home/user/project/src/utils/path.py")
relative_from = "src"
relative_path = get_relative_path(str(full_path), relative_from)
print(relative_path)

# Пример 4: Путь с относительными указателями
full_path = "./src/utils/path.py"
relative_from = "src"
relative_path = get_relative_path(full_path, relative_from)
print(relative_path)

# Пример 5: Windows path
full_path = "C:\\Users\\user\\project\\src\\utils\\path.py"
relative_from = "src"
relative_path = get_relative_path(full_path, relative_from)
print(relative_path)