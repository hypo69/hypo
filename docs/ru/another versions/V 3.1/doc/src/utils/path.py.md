# Модуль `src.utils.path`

## Обзор

Модуль `src.utils.path` предназначен для определения корневого пути к проекту и предоставляет функцию `get_relative_path` для получения относительного пути от заданного сегмента. Этот модуль обеспечивает согласованность импортов в проекте, строящихся относительно корневого пути.

## Подробней

Этот модуль полезен для определения относительных путей внутри проекта, что упрощает перенос и реорганизацию структуры каталогов. Функция `get_relative_path` позволяет извлекать часть пути, начиная с указанного сегмента, что может быть полезно для динамического определения путей к файлам и ресурсам.

## Функции

### `get_relative_path`

```python
def get_relative_path(full_path: str, relative_from: str) -> Optional[str]:
    """
    Args:
        full_path (str): Полный путь.
        relative_from (str): Сегмент пути, с которого нужно начать извлечение.

    Returns:
        Optional[str]: Относительный путь начиная с `relative_from`, или None, если сегмент не найден.
    """
```

**Описание**: Возвращает часть пути начиная с указанного сегмента и до конца.

**Параметры**:
- `full_path` (str): Полный путь к файлу или директории.
- `relative_from` (str): Сегмент пути, с которого начинается относительный путь.

**Возвращает**:
- `Optional[str]`: Относительный путь начиная с `relative_from`, или `None`, если сегмент не найден.

**Примеры**:

Пример 1: Извлечение относительного пути из полного пути.

```python
from src.utils.path import get_relative_path

full_path = "/home/user/project/src/module/file.py"
relative_from = "src"
relative_path = get_relative_path(full_path, relative_from)
print(relative_path)  # Вывод: src/module/file.py
```

Пример 2: Сегмент `relative_from` не найден в `full_path`.

```python
from src.utils.path import get_relative_path

full_path = "/home/user/project/module/file.py"
relative_from = "src"
relative_path = get_relative_path(full_path, relative_from)
print(relative_path)  # Вывод: None
```