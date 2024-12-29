# `get_relative_path`

## Обзор

Этот модуль демонстрирует использование функции `get_relative_path` из `src.utils.path` для получения относительного пути.

## Содержание

- [Обзор](#обзор)
- [Функции](#функции)
    - [`get_relative_path`](#get_relative_path)

## Функции

### `get_relative_path`

**Описание**:  Функция `get_relative_path` используется для получения относительного пути от исходного пути к базовому пути.

**Параметры**:
-   `start_path` (Path): Абсолютный путь.
-   `base_path` (str): Базовый путь, относительно которого нужно получить относительный путь.

**Возвращает**:
-   `Path | None`: Относительный путь как объект `Path` или `None`, если `base_path` не является частью `start_path`.

**Пример использования**
```python
from pathlib import Path
from src.utils.path import get_relative_path

relative_path = get_relative_path(Path(__file__).resolve(), 'hypotez')
print(relative_path)
```