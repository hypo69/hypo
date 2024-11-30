# <input code>

```python
## \file hypotez/src/templates/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.templates 
	:platform: Windows, Unix
	:synopsis:

"""

MODE = 'dev'


import sys
import json
from packaging.version import Version

from pathlib import Path
def set_project_root(marker_files=(\'pyproject.toml\', \'requirements.txt\', \'.git\')) -> Path:
    """
    Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.

    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Get the root directory of the project
__root__ = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""

from src import gs
```

# <algorithm>

**Алгоритм работы функции `set_project_root`:**

1. **Инициализация:**
   - `current_path` получает путь к текущему файлу (`header.py`) и нормализует его.
   - `__root__` инициализируется значением `current_path`.
2. **Поиск корня проекта:**
   - Цикл `for` проходит по родительским директориям `current_path` (включая самого `current_path`).
   - Для каждой родительской директории `parent` проверяется наличие в ней файлов или папок из `marker_files`.
   - Если такой файл или папка найдены, то `__root__` обновляется до `parent`, и цикл прерывается.
3. **Добавление в `sys.path` (если необходимо):**
   - Если найденный `__root__` не присутствует в списке `sys.path`, то он добавляется в начало списка.
4. **Возврат значения:**
   - Функция возвращает значение `__root__`.

**Пример:**

Предположим, что `header.py` находится в директории `/home/user/project/hypotez/src/templates`.  `marker_files` содержит `pyproject.toml`, `requirements.txt`, `.git`.

- Алгоритм будет подниматься по дереву директорий: `/home/user/project/hypotez/src/templates`, `/home/user/project/hypotez/src`, `/home/user/project/hypotez`, `/home/user/project`.
- Если `pyproject.toml` или `requirements.txt` или `.git` присутствует в `/home/user/project`, то `__root__` будет установлен на `/home/user/project`.
- В противном случае `__root__` будет установлен на `/home/user/project/hypotez/src/templates`.
-  `/home/user/project` будет добавлен в `sys.path`.

# <mermaid>

```mermaid
graph TD
    A[header.py] --> B{set_project_root};
    B --> C[current_path = Path(__file__).resolve().parent];
    C --> D[__root__ = current_path];
    D --> E(Iterate through parents);
    E --> F{any((parent / marker).exists() for marker in marker_files)};
    F -- True --> G[__root__ = parent, break];
    F -- False --> E;
    G --> H{__root__ not in sys.path};
    H -- True --> I[sys.path.insert(0, str(__root__))];
    I --> J[__root__ is returned];
    H -- False --> J;
    J --> K[__root__ = set_project_root()];
    K --> L[from src import gs];
```

**Объяснение диаграммы:**

*   `header.py` вызывает `set_project_root`.
*   `set_project_root` определяет `current_path` и `__root__`
*   Цикл `for` ищет корневую директорию.
*   Если корневая директория найдена, она добавляется в `sys.path` и возвращается.
*   `from src import gs` импортирует модуль `gs` из пакета `src`.


# <explanation>

* **Импорты:**
    * `sys`: Модуль для доступа к системным переменным, в частности, для манипуляции с `sys.path`.
    * `json`: Модуль для работы с JSON-данными (не используется напрямую в данном коде).
    * `packaging.version`: Модуль для работы с версиями пакетов (не используется напрямую в данном коде).
    * `pathlib`: Модуль для работы с путями к файлам и каталогам. Он используется для получения пути к файлу `header.py` и работы с родительскими каталогами.
    * `src.gs`: Модуль, скорее всего, содержащий функциональность, связанную с Google Sheets. Импорт необходим для использования этой функциональности в коде.

* **Функции:**
    * `set_project_root(marker_files=...)`: Функция находит корневую директорию проекта, начиная от текущего файла.
        * Аргументы: `marker_files` — кортеж из файлов или каталогов, по наличию которых определяется корень проекта. По умолчанию используются `pyproject.toml`, `requirements.txt` и `.git`.
        * Возвращаемое значение: `Path` — путь к корневой директории проекта.
        *  Использование: Находит путь к корню проекта, чтобы импортировать модули из других папок.

* **Переменные:**
    * `MODE = 'dev'`: Строковая переменная, хранящая режим работы.
    * `__root__`: Переменная, хранящая путь к корневой директории проекта, являющаяся результатом выполнения функции `set_project_root()`. Она имеет тип `Path`.

* **Возможные ошибки и улучшения:**
    * Если ни один из файлов в `marker_files` не найден, функция вернёт путь к исходному каталогу, где был `header.py`,  что, возможно,  не является желаемым поведением. Разработчик может рассмотреть,  как функция должна себя вести в случае, если корневой каталог не может быть определён, например, возвращать ошибку или значение по умолчанию.

* **Связь с другими частями проекта:**
    Функция `set_project_root` жизненно важна для корректного импорта модулей из других частей проекта (`src.gs`). Она обеспечивает возможность работы с проектом, расположенным внутри иерархии директорий.