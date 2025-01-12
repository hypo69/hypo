# Модуль `src.utils.path`

## Обзор

Модуль `src.utils.path` предназначен для определения корневого пути к проекту и обеспечивает возможность построения импортов относительно этого пути. Он предоставляет функцию для извлечения относительного пути из полного пути, начиная с заданного сегмента.

## Оглавление

- [Функции](#Функции)
    - [`get_relative_path`](#get_relative_path)

## Функции

### `get_relative_path`

**Описание**: Возвращает часть пути, начиная с указанного сегмента и до конца.

**Параметры**:
- `full_path` (str): Полный путь.
- `relative_from` (str): Сегмент пути, с которого нужно начать извлечение.

**Возвращает**:
- `Optional[str]`: Относительный путь, начиная с `relative_from`, или `None`, если сегмент не найден.

**Пример использования**

```python
from src.utils.path import get_relative_path

full_path = "/home/user/project/src/module/file.py"
relative_from = "src"
relative_path = get_relative_path(full_path, relative_from)
print(relative_path) # Выведет: src/module/file.py

full_path = "/home/user/project/module/file.py"
relative_from = "src"
relative_path = get_relative_path(full_path, relative_from)
print(relative_path) # Выведет: None
```