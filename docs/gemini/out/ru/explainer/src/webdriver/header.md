# <input code>

```python
## \file hypotez/src/webdriver/header.py
# -*- coding: utf-8 -*-\

#! venv/bin/python/python3.12

"""
.. module: src.webdriver 
	:platform: Windows, Unix
	:synopsis:

"""


import sys
import json
from packaging.version import Version

from pathlib import Path
def set_project_root(marker_files=('__root__','.git')) -> Path:
    """ Finds the root directory of the project starting from the current file's directory,
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

# <algorithm>

**Шаг 1:**  Функция `set_project_root`.
* Вход: кортеж `marker_files` с именами файлов или директорий, используемых для определения корня проекта.
* Алгоритм: Начинает поиск корня проекта с текущей директории. Перебирает родительские директории до тех пор, пока не найдёт директорию, содержащую хотя бы один из файлов/папок из `marker_files`.
* Выход: Объект `Path` - путь к корневой директории проекта. Если корень не найден, возвращается текущая директория.


**Шаг 2:** Получение корня проекта
* Вызов `__root__ = set_project_root()`.
* Выполняется поиск корня проекта с помощью `set_project_root`


**Шаг 3:** Чтение настроек из `settings.json`
* Алгоритм:  Попытка открыть файл `settings.json` в корневой директории проекта.
* Проверка: Если файл открывается, загружает данные JSON из него в переменную `settings`.
* Обработка ошибок: Если возникает `FileNotFoundError` или `json.JSONDecodeError`, пропускает ошибку.

**Шаг 4:** Чтение документации из `README.MD`
* Алгоритм: Попытка открыть файл `README.MD` в корневой директории проекта.
* Проверка: Если файл открывается, читает содержимое файла в переменную `doc_str`.
* Обработка ошибок: Если возникает `FileNotFoundError` или `json.JSONDecodeError`, пропускает ошибку.


**Шаг 5:** Получение и присвоение метаданных из `settings`
* Используя `settings.get`, получает значения различных метаданных (например, `project_name`, `version`, `author`) из `settings` или устанавливает значения по умолчанию.


**Пример:** Если в `settings.json` есть поле `project_name` со значением "MyProject", то `__project_name__` будет равно "MyProject".


# <mermaid>

```mermaid
graph TD
    A[__root__ = set_project_root()] --> B{Найден корень?};
    B -- Да --> C[__root__ (Path)];
    B -- Нет --> D[__root__ = текущая директория];
    C --> E[Открыть settings.json];
    E -- Успех --> F[settings = json.load(settings_file)];
    E -- Ошибка --> G;
    F --> H[Получить __project_name__, __version__ ...];
    H --> I[__project_name__, __version__ ...];
    G --> J[__project_name__ = "hypotez"];
    J --> I;
    C --> K[Открыть README.MD];
    K -- Успех --> L[doc_str = settings_file.read()];
    K -- Ошибка --> M;
    L --> I;
    M --> I;
    subgraph "Зависимости"
        I --> N[gs.path.root];
        N --> O[Pathlib];
        O --> P[sys];
        N --> Q[json];
        N --> R[packaging];
    end
```

**Описание подключаемых зависимостей:**
* `Pathlib`: Для работы с путями файлов и директорий.
* `sys`: Для доступа к системным переменным, таким как `sys.path`.
* `json`: Для работы с файлами JSON.
* `packaging`: Для работы с версиями пакетов.
* `gs.path.root`: Предполагается, что это импортированный атрибут из модуля `gs`, вероятно, для получения пути к корню проекта.


# <explanation>

**Импорты:**

* `sys`: предоставляет доступ к системным переменным, включая `sys.path`, что важно для добавления пути к корню проекта в список путей поиска модулей.
* `json`: используется для работы с файлами JSON, в частности, для загрузки настроек из `settings.json`.
* `packaging.version`: необходим для работы с версиями пакетов, хотя в этом конкретном случае не используется напрямую.
* `pathlib`: используется для работы с путями к файлам и каталогам, предоставляя удобный и интуитивно понятный способ манипулирования файловыми путями.

**Классы:**

В этом коде нет определённых пользовательских классов. Используются встроенные классы `Path` из `pathlib`.

**Функции:**

* `set_project_root(marker_files)`:  Ищет корневую директорию проекта, начиная с текущей директории и поднимаясь вверх по иерархии директорий.  Возвращает `Path` к корню проекта, добавляя его в `sys.path` для упрощённого импорта модулей. Пример: `set_project_root(('pyproject.toml', 'requirements.txt'))`

**Переменные:**

* `__root__`: Хранит путь к корню проекта (`Path`).
* `settings`: Словарь (`dict`), содержащий данные из `settings.json`.
* `doc_str`: Строка (`str`), содержащая содержимое файла `README.MD`.
* `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`: Строковые переменные (`str`), содержащие метаданные о проекте, полученные из `settings.json`.

**Возможные ошибки и улучшения:**

* **Обработка ошибок:**  Использование `try...except` для обработки `FileNotFoundError` и `json.JSONDecodeError` — хороший подход, но может быть расширен для более точных сообщений об ошибках или альтернативных сценариев (например, использование файла по умолчанию).
* **Типизация:** Использование аннотаций типов (`-> Path`) для функции `set_project_root` и других переменных улучшает читабельность и позволяет статическому анализатору обнаруживать ошибки.
* **Дополнительно:** Добавление логирования для отслеживания процесса поиска корня проекта или загрузки настроек, особенно в случае ошибок.

**Взаимосвязи с другими частями проекта:**

Функция `set_project_root` и работа с настройками (`settings.json`) напрямую связаны с настройкой импорта модулей из других директорий проекта. Модуль `gs` явно используется для получения доступа к пути к корню проекта.  Без `gs.path.root` поиск `settings.json` и `README.MD` был бы некорректным, т.к. не было бы доступа к корневому каталогу проекта.