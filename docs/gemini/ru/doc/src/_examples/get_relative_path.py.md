# Модуль `get_relative_path`

## Обзор

Модуль `get_relative_path` демонстрирует использование функции `get_relative_path` для получения относительного пути.

## Содержание

- [Обзор](#обзор)
- [Функции](#функции)

## Функции

### `get_relative_path`

**Описание**: Функция `get_relative_path` вычисляет относительный путь от текущего файла до указанной директории.

**Параметры**:
- `current_file_path` (Path): Абсолютный путь к текущему файлу.
- `root_directory` (str): Название корневой директории.

**Возвращает**:
- `str`: Относительный путь от текущего файла до корневой директории.

**Пример использования**
```python
from pathlib import Path
from src.utils.path import get_relative_path

relative_path = get_relative_path(Path(__file__).resolve(), 'hypotez')
print(relative_path)
```
```