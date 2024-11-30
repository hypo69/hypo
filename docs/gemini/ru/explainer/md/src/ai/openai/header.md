# Анализ кода файла hypotez/src/logger/header.py

## <input code>

```python
## \file hypotez/src/logger/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
module: src.logger 
	:platform: Windows, Unix
	:synopsis: Модуль определяющий корневой путь к проекту. Все импорты строятся относительно этого пути.
    :TODO: В дальнейшем перенести в системную переменную"""
MODE = 'dev'

import sys
import json
from packaging.version import Version

from pathlib import Path
def set_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
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

settings:dict = None
try:
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = json.load(settings_file)
except (FileNotFoundError, json.JSONDecodeError):
    ...

doc_str:str = None
try:
    with open(gs.path.root / 'src' /  'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError):
    ...


__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
__version__: str = settings.get("version", '')  if settings  else ''
__doc__: str = doc_str if doc_str else ''
__details__: str = ''
__author__: str = settings.get("author", '')  if settings  else ''
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```

## <algorithm>

**Блок-схема:**

1. **`set_project_root(marker_files)`:**
   - Принимает кортеж `marker_files` (файлы/директории для поиска корня проекта).
   - Получает текущий путь к файлу.
   - Итерируется по родительским директориям текущего файла.
   - Для каждого родительского каталога проверяет наличие `marker_files` с помощью `any()`.
   - Если найден `marker_files`, то `__root__` обновляется до найденной родительской директории и цикл завершается.
   - Если корень не найден, то `__root__` остаётся текущим путём.
   - Если `__root__` не в `sys.path`, то добавляет его в начало списка импортируемых путей.
   - Возвращает `__root__`.
   *Пример:* Если `marker_files` - ('pyproject.toml',), то функция ищет директорию содержащую этот файл, начиная с текущей.

2. **`__root__ = set_project_root()`:**
   - Вызов функции `set_project_root()`.
   - Присваивание результата функции переменной `__root__`.

3. **`from src import gs`:**
   - Импорт модуля `gs` из пакета `src`.
   - Используется для доступа к объекту `gs.path`.

4. **`settings = ...`:**
   - Попытка открыть файл `gs.path.root / 'src' / 'settings.json'` в режиме чтения.
   - Если файл найден и успешно прочитан, данные десериализуются из JSON формата.
   - `settings` присваивается результат десериализации.
   - Если происходит ошибка (например, файл не найден или JSON некорректный), то выполняется `...` (пропускается обработка ошибки).

5. **`doc_str = ...`:**
   - Аналогичный блок, как и для настроек, но для файла `README.MD`.

6. **`__project_name__ = ...`:**
   - Используется `settings.get("project_name", 'hypotez')` для получения значения `project_name` из словаря настроек `settings`, или значение по умолчанию 'hypotez', если ключ не найден.

*Пример*: Если ключ `project_name` существует в `settings` и имеет значение "MyProject", то `__project_name__` будет равно "MyProject".
   - Аналогично для остальных переменных.


## <mermaid>

```mermaid
graph LR
    A[set_project_root] --> B(current_path);
    B --> C{any(marker_files)};
    C -- true --> D[__root__ = parent];
    C -- false --> E[loop];
    E --> F{current_path is in sys.path};
    F -- true --> G[return __root__];
    F -- false --> H[sys.path.insert(0, __root__)];
    H --> G;
    D --> G;
    A --> I[__root__ = set_project_root];
    I --> J{settings};
    J -- true --> K[load settings];
    J -- false --> L[settings = 'hypotez'];
    K --> M{doc_str};
    M -- true --> N[load doc_str];
    M -- false --> O[doc_str = ''];
    N --> P[assign project vars];
    O --> P;
    P --> Q[return];
    subgraph Imports
        I --> J1[from src import gs];
        J1 --> K1[gs.path.root];
        K1 --> Z[settings.json];
        K1 --> Y[README.MD];
    end
```


## <explanation>

**Импорты:**

- `sys`:  Модуль `sys` предоставляет доступ к системным параметрам Python, в том числе к пути поиска модулей (`sys.path`). В данном случае используется для добавления пути к корню проекта в начало пути поиска.
- `json`: Модуль для работы с JSON-данными. Используется для загрузки настроек проекта из файла `settings.json`.
- `packaging.version`: Модуль для работы с версиями пакетов.  В данном коде, возможно, используется для проверки версий в будущем.
- `pathlib`: Модуль для работы с путями к файлам. Используется для получения и работы с путями к файлам.
- `gs`:  Этот импорт подразумевает, что существует модуль `gs` в пакете `src`, скорее всего, для работы с файловой системой или ресурсами проекта. Подробности о нём не ясны без доступа к коду самого `gs`.

**Классы:**

- Нет явных определений классов.

**Функции:**

- `set_project_root(marker_files)`: Находит корневую директорию проекта. Принимает кортеж `marker_files`, в котором содержатся имена файлов или директорий, используемых для определения корневого каталога. Возвращает объект `Path` представляющий путь к корневой директории.

**Переменные:**

- `__root__`: Переменная типа `Path`, хранящая корневую директорию проекта.
- `settings`: Словарь, хранящий настройки проекта, загруженные из `settings.json`.
- `doc_str`: Строковая переменная, содержащая содержимое файла `README.MD`.
- `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`: Переменные, содержащие метаданные о проекте (имя проекта, версия, описание, автор, авторские права и т.д.)
- `MODE`: Строковая переменная, представляющая режим работы (например, 'dev' или 'prod').


**Возможные ошибки и улучшения:**

- **Обработка ошибок:** Обработка `FileNotFoundError` и `json.JSONDecodeError` при чтении `settings.json` и `README.MD` является хорошим решением. Но можно добавить логирование ошибок для лучшей диагностики проблем.
- **`gs` модуль:** Необходима более подробная информация о модуле `gs`, чтобы понять его функциональность и корректность взаимодействия с `settings.json` и `README.MD`.
- **Типизация:**  Использование аннотаций типов (`-> Path`) улучшает читабельность и позволяет статическим анализаторам лучше понимать код.

**Взаимосвязи с другими частями проекта:**

- Файл напрямую зависит от пакета `src`, который, по видимому, содержит необходимые модули для работы с файловой системой и ресурсами проекта.
- Необходимость в модуле `gs` подразумевает, что есть другие части кода, которые используют `gs` для взаимодействия с файлами и ресурсами.
- Файл `settings.json` и `README.MD` содержат данные о проекте, которые используются для инициализации различных переменных, используемых в других частях приложения.


Этот анализ показывает, что код выполняет критическую функцию определения корневого пути проекта и загрузки метаданных. Однако, без контекста кода из пакета `src` и `gs` сложно полностью понять его функциональность.