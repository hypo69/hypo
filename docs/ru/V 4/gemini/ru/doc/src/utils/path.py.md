# Модуль `src.utils.path`

## Обзор

Модуль `src.utils.path` предназначен для определения корневого пути к проекту и упрощения работы с путями в файловой системе. Он содержит функции для получения относительных путей на основе заданного сегмента. Модуль разработан для работы в операционных системах Windows и Unix.

## Подробней

Этот модуль облегчает построение импортов в проекте, делая их относительными корневой директории. Это особенно полезно при перемещении или переименовании директорий проекта. Функция `get_relative_path` позволяет получить часть пути от заданного сегмента до конца, что упрощает навигацию по файловой системе проекта.

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

     **Как работает функция**:
        Функция `get_relative_path` преобразует входные строки `full_path` и `relative_from` в объекты `Path` для удобства работы с путями. Затем она разделяет полный путь на отдельные компоненты. Если сегмент `relative_from` найден в компонентах полного пути, функция определяет его индекс и формирует новый путь, начиная с этого сегмента и до конца полного пути. Полученный относительный путь возвращается в виде строки, использующей прямой слеш (POSIX-совместимый формат). Если сегмент `relative_from` не найден в полном пути, функция возвращает `None`.

        ```mermaid
        graph LR
        A[Начало] --> B{Преобразовать в Path};
        B --> C{Разделить путь на части};
        C --> D{`relative_from` в частях?};
        D -- Да --> E{Найти индекс `relative_from`};
        D -- Нет --> F[Возврат None];
        E --> G{Сформировать относительный путь};
        G --> H[Возврат относительного пути];
        F --> I[Конец];
        H --> I;
        ```
    """
```

**Описание**: Возвращает часть пути начиная с указанного сегмента и до конца.

**Параметры**:
- `full_path` (str): Полный путь к файлу или директории.
- `relative_from` (str): Сегмент пути, с которого нужно начать извлечение относительного пути.

**Возвращает**:
- `Optional[str]`: Относительный путь начиная с `relative_from`, или `None`, если сегмент не найден.

**Примеры**:

```python
from pathlib import Path
import os

# Пример 1: Путь к файлу внутри проекта
full_path = os.path.abspath('/путь/к/проекту/src/utils/example.txt')
relative_from = 'src'
relative_path = get_relative_path(full_path, relative_from)
print(relative_path)  # Вывод: utils/example.txt

# Пример 2: Путь к директории внутри проекта
full_path = os.path.abspath('/путь/к/проекту/src/utils/')
relative_from = 'src'
relative_path = get_relative_path(full_path, relative_from)
print(relative_path)  # Вывод: utils

# Пример 3: Сегмент не найден
full_path = os.path.abspath('/путь/к/проекту/src/utils/example.txt')
relative_from = 'config'
relative_path = get_relative_path(full_path, relative_from)
print(relative_path)  # Вывод: None