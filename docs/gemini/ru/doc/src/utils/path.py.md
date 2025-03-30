# Модуль `src.utils.path`

## Обзор

Модуль `src.utils.path` предназначен для определения относительного пути к файлам и директориям в проекте. Он содержит функцию `get_relative_path`, которая позволяет извлекать часть пути, начиная с указанного сегмента. Это полезно для построения путей относительно корня проекта или определенной директории, что упрощает переносимость и масштабируемость кода.

## Подробней

Этот модуль помогает стандартизировать работу с путями в проекте, обеспечивая единообразный подход к определению местоположения файлов и каталогов. Это особенно важно в больших проектах, где необходимо поддерживать консистентность и избегать ошибок, связанных с неправильными путями. Функция `get_relative_path` позволяет избежать жесткой привязки к абсолютным путям, что делает код более гибким и устойчивым к изменениям в структуре каталогов.

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
- `relative_from` (str): Сегмент пути, начиная с которого нужно извлечь относительный путь.

**Возвращает**:
- `Optional[str]`: Относительный путь, начиная с указанного сегмента, или `None`, если сегмент не найден.

**Примеры**:

```python
from pathlib import Path
from typing import Optional

def get_relative_path(full_path: str, relative_from: str) -> Optional[str]:
    """
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

# Пример использования:
full_path = "/home/user/project/src/utils/file.txt"
relative_from = "src"
relative_path = get_relative_path(full_path, relative_from)
print(relative_path)  # Вывод: src/utils/file.txt

full_path = "/home/user/project/src/utils/file.txt"
relative_from = "project"
relative_path = get_relative_path(full_path, relative_from)
print(relative_path)  # Вывод: project/src/utils/file.txt

full_path = "/home/user/project/src/utils/file.txt"
relative_from = "nonexistent"
relative_path = get_relative_path(full_path, relative_from)
print(relative_path)  # Вывод: None