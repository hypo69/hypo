# Модуль `src.utils.path`

## Обзор

Модуль `src.utils.path` предназначен для определения корневого пути к проекту и предоставляет функцию `get_relative_path` для извлечения относительного пути из полного пути. Все импорты в проекте строятся относительно этого пути.

## Подробнее

Модуль содержит функцию `get_relative_path`, которая позволяет получить часть пути, начиная с указанного сегмента. Это полезно для работы с путями в проекте, особенно когда необходимо получить путь относительно определенной директории.

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

**Назначение**: Извлекает относительный путь из полного пути, начиная с указанного сегмента.

**Параметры**:

- `full_path` (str): Полный путь к файлу или директории.
- `relative_from` (str): Сегмент пути, начиная с которого необходимо извлечь относительный путь.

**Возвращает**:

- `Optional[str]`: Относительный путь в виде строки, начиная с сегмента `relative_from`. Возвращает `None`, если сегмент `relative_from` не найден в `full_path`.

**Как работает функция**:

1. **Преобразование в Path**: Преобразует входные строки `full_path` в объект `Path` для удобства работы с путями.
2. **Разбиение пути на сегменты**: Разбивает полный путь на список отдельных сегментов (директорий).
3. **Поиск индекса начального сегмента**: Ищет индекс сегмента `relative_from` в списке сегментов пути.
4. **Формирование относительного пути**: Если сегмент `relative_from` найден, формирует новый путь, начиная с этого сегмента и до конца исходного пути.
5. **Возврат относительного пути**: Преобразует полученный относительный путь в строку в формате POSIX и возвращает его. Если сегмент `relative_from` не найден, возвращает `None`.

```ascii
    full_path, relative_from
    |
    Преобразование в Path
    |
    Разбиение пути на сегменты
    |
    Поиск индекса начального сегмента
    |
    Если relative_from найден:
        |
        Формирование относительного пути
        |
        Возврат относительного пути в формате POSIX
    Иначе:
        |
        Возврат None
```

**Примеры**:

```python
from pathlib import Path
from typing import Optional


def get_relative_path(full_path: str, relative_from: str) -> Optional[str]:
    """
    Возвращает часть пути начиная с указанного сегмента и до конца.

    Args:
        full_path (str): Полный путь.
        relative_from (str): Сегмент пути, с которого нужно начать извлечение.

    Returns:
        Optional[str]: Относительный путь начиная с `relative_from`, или None, если сегмент не найден.
    """
    # Преобразуем строки в объекты Path
    path = Path(full_path)
    parts = path.parts

    # Находим индекс сегмента relative_from
    if relative_from in parts:
        start_index = parts.index(relative_from)
        # Формируем путь начиная с указанного сегмента
        relative_path = Path(*parts[start_index:])
        return relative_path.as_posix()
    else:
        return None
```

```python
# Пример 1: Извлечение относительного пути от 'src'
full_path = '/path/to/my/project/src/utils/path.py'
relative_from = 'src'
relative_path = get_relative_path(full_path, relative_from)
print(relative_path)  # Вывод: src/utils/path.py

# Пример 2: Извлечение относительного пути от 'utils'
full_path = '/path/to/my/project/src/utils/path.py'
relative_from = 'utils'
relative_path = get_relative_path(full_path, relative_from)
print(relative_path)  # Вывод: utils/path.py

# Пример 3: Сегмент не найден
full_path = '/path/to/my/project/src/utils/path.py'
relative_from = 'nonexistent'
relative_path = get_relative_path(full_path, relative_from)
print(relative_path)  # Вывод: None