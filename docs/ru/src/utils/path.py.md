# Модуль `src.utils.path`

## Обзор

Модуль `src.utils.path` определяет корневой путь к проекту. Все импорты строятся относительно этого пути. Содержит функцию для получения относительного пути из полного пути, начиная с указанного сегмента.

## Подробнее

Модуль предоставляет функцию `get_relative_path`, которая позволяет извлекать часть пути начиная с определенного сегмента. Это полезно для работы с путями в проекте, когда необходимо получить путь относительно какой-то известной точки.

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

**Назначение**: Функция `get_relative_path` извлекает относительный путь из полного пути, начиная с указанного сегмента. Если указанный сегмент не найден в полном пути, функция возвращает `None`.

**Параметры**:

- `full_path` (str): Полный путь к файлу или директории.
- `relative_from` (str): Сегмент пути, начиная с которого необходимо извлечь относительный путь.

**Возвращает**:

- `Optional[str]`: Относительный путь в виде строки, начиная с сегмента `relative_from`. Возвращает `None`, если сегмент `relative_from` не найден в `full_path`.

**Как работает функция**:

1. **Преобразование в `Path`**: Функция преобразует входные строки `full_path` и `relative_from` в объекты `Path` для удобства работы с путями.
2. **Разбиение пути на части**: Полный путь разбивается на отдельные компоненты (сегменты) с помощью `path.parts`.
3. **Поиск индекса**: Функция ищет индекс сегмента `relative_from` в списке компонентов пути.
4. **Формирование относительного пути**: Если сегмент `relative_from` найден, формируется новый путь, начиная с этого сегмента и до конца пути.
5. **Преобразование в строку**: Относительный путь преобразуется обратно в строку с помощью `as_posix()`.
6. **Обработка отсутствия сегмента**: Если сегмент `relative_from` не найден в полном пути, функция возвращает `None`.

**ASCII flowchart**:

```
full_path, relative_from
     ↓
Преобразование в Path
     ↓
Разбиение пути на части (parts)
     ↓
Поиск индекса relative_from
     ├───> Найден: Формирование относительного пути → Преобразование в строку → Возврат относительного пути
     └───> Не найден: Возврат None
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
# Пример 1: Относительный путь существует
full_path = "/home/user/project/src/utils/path.py"
relative_from = "src"
result = get_relative_path(full_path, relative_from)
print(f"Пример 1: {result}")  # Вывод: src/utils/path.py

# Пример 2: Относительный путь не существует
full_path = "/home/user/project/src/utils/path.py"
relative_from = "nonexistent"
result = get_relative_path(full_path, relative_from)
print(f"Пример 2: {result}")  # Вывод: None

# Пример 3: relative_from - последний сегмент
full_path = "/home/user/project/src/utils"
relative_from = "utils"
result = get_relative_path(full_path, relative_from)
print(f"Пример 3: {result}")  # Вывод: utils

# Пример 4: Путь без начального слеша
full_path = "home/user/project/src/utils/path.py"
relative_from = "src"
result = get_relative_path(full_path, relative_from)
print(f"Пример 4: {result}")  # Вывод: src/utils/path.py