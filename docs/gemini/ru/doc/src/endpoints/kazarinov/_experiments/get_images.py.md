# Модуль для получения списка изображений, сгенерированных ИИ
=================================================

Модуль предназначен для получения списка изображений, сгенерированных ИИ, из указанной директории.

## Обзор

Модуль `get_images.py` предназначен для поиска файлов изображений в определенной директории и вывода списка найденных файлов. Он использует функции из других модулей проекта `hypotez` для рекурсивного поиска файлов и красивого вывода результатов.

## Подробней

Этот код используется для экспериментов с изображениями, сгенерированными ИИ. Он получает список изображений из указанной директории и выводит его. В данном случае, изображения находятся в директории `external_data/kazarinov/converted_images/pastel`.

## Функции

### `recursively_get_filepath`

```python
from src.utils.file import recursively_get_filepath
def recursively_get_filepath(root_dir: str | Path, patterns: List[str] = ['*']) -> List[str]:
    """
    Рекурсивно получает список файлов, соответствующих заданным шаблонам, в указанной директории.

    Args:
        root_dir (str | Path): Корневая директория для поиска файлов.
        patterns (List[str], optional): Список шаблонов файлов для поиска. По умолчанию ['*'].

    Returns:
        List[str]: Список путей к найденным файлам.
    """
```

**Назначение**: Рекурсивно получает список файлов, соответствующих заданным шаблонам, в указанной директории.

**Параметры**:
- `root_dir` (str | Path): Корневая директория для поиска файлов.
- `patterns` (List[str], optional): Список шаблонов файлов для поиска. По умолчанию `['*']`.

**Возвращает**:
- `List[str]`: Список путей к найденным файлам.

**Как работает функция**:

1. Функция принимает корневую директорию и список шаблонов файлов.
2. Она рекурсивно обходит директорию и ищет файлы, соответствующие заданным шаблонам.
3. Найденные пути к файлам возвращаются в виде списка.

```
        recursively_get_filepath
        │
        ├── root_dir, patterns
        │
        │
        └── List[str] (filepaths)
```

**Примеры**:

```python
from pathlib import Path
from src.utils.file import recursively_get_filepath

# Пример использования
root_dir = Path('./data')  # Укажите путь к директории
patterns = ['*.jpeg', '*.png']
image_paths = recursively_get_filepath(root_dir, patterns)
print(image_paths)
```

### `pprint`

```python
from src.utils.printer import pprint
def pprint(obj: Any, indent: int = 2, sort_dicts: bool = False, width: int = 80) -> None:
    """
    Выводит объект в консоль в удобочитаемом формате.

    Args:
        obj (Any): Объект для вывода.
        indent (int, optional): Отступ для форматирования. По умолчанию 2.
        sort_dicts (bool, optional): Сортировать ли словари по ключам. По умолчанию False.
        width (int, optional): Ширина вывода. По умолчанию 80.

    Returns:
        None
    """
```

**Назначение**: Выводит объект в консоль в удобочитаемом формате.

**Параметры**:
- `obj` (Any): Объект для вывода.
- `indent` (int, optional): Отступ для форматирования. По умолчанию 2.
- `sort_dicts` (bool, optional): Сортировать ли словари по ключам. По умолчанию `False`.
- `width` (int, optional): Ширина вывода. По умолчанию 80.

**Возвращает**:
- `None`

**Как работает функция**:

1. Функция принимает объект для вывода, отступ, флаг сортировки словарей и ширину вывода.
2. Использует модуль `pprint` для форматированного вывода объекта в консоль.

```
        pprint
        │
        ├── obj, indent, sort_dicts, width
        │
        │
        └── None (вывод в консоль)
```

**Примеры**:

```python
from src.utils.printer import pprint

# Пример использования
data = {'a': 1, 'b': 2, 'c': 3}
pprint(data, indent=4, sort_dicts=True)
```

### Переменные

- `images_path`: Список путей к изображениям, полученный с использованием функции `recursively_get_filepath`.
```python
images_path = recursively_get_filepath(gs.path.external_data / 'kazarinov' / 'converted_images' / 'pastel', ['*.jpeg','*.jpg','*.png'])
pprint(images_path)
```

**Пример**:
```python
import gs
from pathlib import Path
from typing import List

from src.utils.file import recursively_get_filepath
from src.utils.printer import pprint


# Предположим, что gs.path.external_data возвращает Path('/путь/к/external_data')
class MockGS:
    class Path:
        external_data = Path('/путь/к/external_data')

    path = Path()
gs = MockGS()

images_path = recursively_get_filepath(gs.path.external_data / 'kazarinov' / 'converted_images' / 'pastel', ['*.jpeg','*.jpg','*.png'])
pprint(images_path)
...