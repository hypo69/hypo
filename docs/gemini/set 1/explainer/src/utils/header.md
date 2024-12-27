# <input code>

```python
## \file hypotez/src/logger/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.logger 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'

"""
	:platform: Windows, Unix
	:synopsis: Модуль определяющий корневой путь к проекту. Все импорты строятся относительно этого пути.
    :TODO: В дальнейшем перенести в системную переменную"""

import sys
import json
from packaging.version import Version

from pathlib import Path
def set_project_root(marker_files=('__root__')) -> Path:
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

# <algorithm>

**Шаг 1:**  Определение корневого пути проекта (функция `set_project_root`).
* Вход: кортеж `marker_files` с именами файлов/папок, указывающих на корень проекта.
* Выход: Объект `Path` с абсолютным путем к корню проекта.
* Алгоритм:
    * Начинает поиск с текущей директории.
    * Итерирует по родительским директориям.
    * Проверяет наличие `marker_files` в каждой директории.
    * Если найден `marker_file`, устанавливает `__root__` и прерывает цикл.
    * Если `__root__` не в `sys.path`, добавляет его в начало.
* Пример: Если `__file__` в `/home/user/project/src/logger/header.py` и `pyproject.toml` есть в `/home/user/project`, то `__root__` установится в `/home/user/project`.


**Шаг 2:** Загрузка настроек из `settings.json`.
* Вход:  Путь к `settings.json` относительно корневого каталога.
* Выход: Словарь `settings` с настройками или `None`, если файл не найден или некорректен.
* Алгоритм:
    * Использует `try-except` для обработки `FileNotFoundError` и `json.JSONDecodeError`.
    * Загружает JSON файл с настройками.
* Пример: Если `settings.json` содержит `{"project_name": "MyProject"}`, то `settings` будет содержать этот словарь.


**Шаг 3:** Загрузка документации из `README.MD`.
* Вход: Путь к `README.MD` относительно корневого каталога.
* Выход: Строка с содержимым файла `README.MD` или `None`, если файл не найден.
* Алгоритм:
    * Использует `try-except` для обработки `FileNotFoundError` и `json.JSONDecodeError`.
    * Читает содержимое файла.
* Пример: Если `README.MD` содержит текст "Моя документация", то `doc_str` будет содержать эту строку.


**Шаг 4:** Инициализация переменных проекта.
* Вход: Словарь `settings`, строка `doc_str`.
* Выход: Переменные `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__` инициализируются из `settings` или имеют значения по умолчанию.
* Алгоритм:
    * Использует метод `get()` для безопасного извлечения значений из словаря `settings` и значения по умолчанию при отсутствии ключа или ошибки.


# <mermaid>

```mermaid
graph TD
    A[set_project_root] --> B{Marker file exists?};
    B -- Yes --> C[__root__ = parent];
    B -- No --> D[Continue searching];
    C --> E{__root__ in sys.path?};
    E -- Yes --> F[return __root__];
    E -- No --> G[sys.path.insert(__root__)];
    F --> H[Load settings];
    D --> B;
    G --> H;
    H --> I[Load README.MD];
    I --> J[Initialize project variables];
    J --> K[return];
    subgraph Load settings
        H -- Yes --> I;
        H -- No --> I;
    end

```

**Объяснение диаграммы:**

Функция `set_project_root` ищет корневой каталог проекта, используя указанные маркерные файлы.
`Load settings` загружает настройки из `settings.json` при успешном поиске корневого каталога.
`Load README.MD` загружает содержание из `README.MD` при успешном поиске корневого каталога.
`Initialize project variables` инициализирует переменные проекта (`__project_name__`, `__version__`, и другие) используя данные из `settings.json` или значения по умолчанию.
`return` - возвращает результат работы функции, и в конечном итоге значение `__root__`

# <explanation>

**Импорты:**

* `sys`: Предоставляет доступ к системным переменным, в частности `sys.path`, для изменения пути поиска модулей.
* `json`: Используется для загрузки настроек из файла `settings.json`.
* `packaging.version`: Вероятно, используется для работы с версиями пакетов, хотя в данном фрагменте кода эта зависимость не используется явно.
* `pathlib`: Предоставляет удобный класс `Path` для работы с путями файлов и каталогов.


**Классы:**

* Нет классов, только функции.


**Функции:**

* `set_project_root(marker_files)`:  Функция находит корневой каталог проекта. Она принимает кортеж `marker_files` с именами файлов, которые должны присутствовать в корневом каталоге. Возвращает объект `Path` с путем к корневому каталогу. Эта функция очень важна для корректной работы импорта модулей.


**Переменные:**

* `__root__`: Содержит путь к корневому каталогу проекта.
* `settings`: Словарь с настройками проекта, загруженный из `settings.json`.
* `doc_str`: Содержит текст из файла `README.MD`.
* `__project_name__`, `__version__`, `__doc__`, и т.д.: Переменные, содержащие информацию о проекте. Инициализируются из `settings` или имеют значения по умолчанию.


**Возможные ошибки и улучшения:**

* **Обработка ошибок:**  `try-except` блоки для загрузки `settings.json` и `README.MD` предотвращают аварийную остановку программы при отсутствии или некорректном формате этих файлов. Но можно добавить проверку на корректность формата данных в загружаемых файлах (например, что `settings.json` содержит `project_name`).
* **Документация:**  Добавьте документацию к переменным, таким как `__root__`, для лучшей читаемости кода.
* **Статические анализаторы:** Использование статических анализаторов кода (например, Pylint, Flake8) поможет выявить потенциальные проблемы и улучшить качество кода.
* **Зависимости:** Укажите более явно зависимости `src.gs` и другие.



**Взаимосвязь с другими частями проекта:**

Функция `set_project_root` и использование `gs.path.root` показывают, что этот код интегрирован в более крупный проект, имеющий систему управления путями и импортами.  `gs` (скорее всего) содержит вспомогательные функции для работы с путями внутри проекта.  `settings.json` определяет конфигурацию проекта, а `README.MD` содержит документацию. Этот код является частью более крупной структуры, где пути к файлам относительно корневого каталога проекта имеют важное значение.