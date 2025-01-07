# Анализ кода файла hypotez/src/webdriver/edge/header.py

## <input code>

```python
## \file hypotez/src/webdriver/edge/header.py
# -*- coding: utf-8 -*-\

#! venv/bin/python/python3.12

"""
.. module:: src.webdriver.edge 
	:platform: Windows, Unix
	:synopsis:

"""



import sys
import json
from packaging.version import Version

from pathlib import Path
def set_project_root(marker_files=('__root__','.git')) -> Path:
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
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = json.load(settings_file)
except (FileNotFoundError, json.JSONDecodeError):
    ...

doc_str:str = None
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
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

```mermaid
graph TD
    A[Получить текущий путь] --> B{Проверить наличие файлов в родительских каталогах};
    B -- Да -> C[Установить __root__];
    B -- Нет -> D[Установить __root__ текущий путь];
    C --> E[Добавить __root__ в sys.path];
    D --> E;
    E --> F[Загрузить settings.json];
    F -- Успешно -> G[Загрузить README.MD];
    F -- Ошибка -> G[Установить значения по умолчанию];
    G -- Успешно -> H[Сформировать __project_name__, __version__, __doc__, ...];
    G -- Ошибка -> H[Установить значения по умолчанию];
    H --> I[Возвратить __root__];
```

**Описание блоков:**

* **A:** Получает путь к текущему файлу (`__file__`) и определяет родительские каталоги.
* **B:** Проверяет, содержит ли родительский каталог один из файлов, указанных в `marker_files`.
* **C:** Обновляет значение `__root__` на найденный родительский каталог, где присутствуют маркеры проекта.
* **D:** Если маркеры не найдены, `__root__` сохраняет значение текущего каталога.
* **E:** Добавляет `__root__` в `sys.path`, что позволяет импортировать модули из корня проекта.
* **F:** Попытка загрузить `settings.json` из каталога `__root__`.
* **G:** Попытка загрузить `README.MD` из каталога `__root__`.
* **H:** Формирование переменных проекта (`__project_name__`, `__version__`, `__doc__`, ...) на основе `settings.json` и `README.MD`.
* **I:** Возвращает вычисленное значение `__root__`.

**Пример:**

Если файл `header.py` находится в каталоге `hypotez/src/webdriver/edge`, то алгоритм будет искать `pyproject.toml`, `requirements.txt` или `.git` в родительских каталогах: `hypotez/src/webdriver`, `hypotez/src`, `hypotez`. При нахождении первого из указанных файлов, `__root__` устанавливается в соответствующую директорию.

## <mermaid>

```mermaid
graph LR
    A[header.py] --> B(set_project_root);
    B --> C{__root__ in sys.path?};
    C -- Да --> D[return __root__];
    C -- Нет --> E[sys.path.insert(0, str(__root__))];
    E --> D;
    B --> F[Открыть settings.json];
    F -- Успешно --> G[Прочитать settings.json];
    F -- Ошибка --> H[settings = None];
    G --> I[Открыть README.MD];
    I -- Успешно --> J[Прочитать README.MD];
    I -- Ошибка --> K[doc_str = None];
    J --> L[Формирование __project_name__, ...];
    H --> L;
    K --> L;
    L --> M[return __root__];
    subgraph Получение корня проекта
        B -.-> A;
    end
```

## <explanation>

**Импорты:**

* `sys`: Модуль для доступа к системным переменным, в том числе `sys.path`. Используется для добавления пути к корню проекта в `sys.path`.
* `json`: Модуль для работы с JSON-файлами. Используется для загрузки настроек проекта из `settings.json`.
* `packaging.version`: Модуль для работы с версиями пакетов. Неясно, зачем используется в данном контексте.
* `pathlib`: Модуль для работы с путями. Используется для работы с файлами проекта.
* `src.gs`: Импортируется модуль `gs` из пакета `src`.  Без контекста неясно, что он делает, но он используется для получения пути к корню проекта.

**Классы:**

Нет явных классов.

**Функции:**

* `set_project_root(marker_files)`: Находит корневой каталог проекта, начиная с текущего файла и ища вверх по иерархии директорий. Возвращает `Path` объект корневого каталога, и добавляет его в `sys.path` если его там нет.
    * `marker_files`: Кортеж имен файлов или директорий, по наличию которых определяется корень проекта.
    * Возвращаемое значение: `Path` объект, представляющий путь к корневому каталогу проекта.

**Переменные:**

* `MODE`: Строковая переменная, хранящая режим работы (`'dev'`).
* `__root__`: `Path` объект, представляющий корневой каталог проекта.
* `settings`: Словарь, содержащий настройки проекта, загружаемый из `settings.json`.
* `doc_str`: Строка, содержащая содержимое файла `README.MD`.
* `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`: Строковые переменные, содержащие соответствующие данные из настроек проекта.

**Возможные ошибки и улучшения:**

* **Обработка исключений:** Обработка `FileNotFoundError` и `json.JSONDecodeError` в блоках `try...except` важна для устойчивости кода. Однако, обработка может быть улучшена. Например, в случае ошибки вывода более подробной информации, а не просто пропуска блока кода.
* **Типизация:** Использование аннотаций типов (`-> Path`) улучшает читабельность и проверяемость кода.
* **Использование `__root__`:** Если `__root__` не будет существовать в корне проекта, код может не работать корректно.
* **Модуль `gs`:** Необходим контекст, что делает модуль `gs`. Если `gs` отвечает за получение пути, лучше сделать это через функцию, а не через глобальную переменную.
* **Проверка валидности JSON:** Проверка валидности данных, загружаемых из `settings.json`.


**Взаимосвязи с другими частями проекта:**

Функция `set_project_root` является критически важной для корректной работы импорта других модулей проекта. Файлы `settings.json` и `README.MD` содержат важные метаданные о проекте, необходимые для его работы. Модуль `gs` играет важную роль в получении пути к корневому каталогу проекта, без него `header.py` не сможет получить доступ к данным.