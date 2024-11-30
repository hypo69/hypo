# Анализ кода hypotez/src/logger/header.py

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
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```

## <algorithm>

**Шаг 1:** Определение функции `set_project_root`
 - Принимает кортеж `marker_files` в качестве аргумента, содержащий список файлов, по которым определяется корневой каталог проекта.
 - Начинает поиск с текущей директории, а затем поднимается вверх по дереву директорий.
 - Для каждой директории проверяет существование хотя бы одного из файлов из списка `marker_files`.
 - Если найден корневой каталог, сохраняет его в переменной `__root__` и завершает цикл.
 - Если корневой каталог не найден, возвращает текущую директорию.
 - Если корневой каталог не был добавлен в `sys.path`, добавляет его в начало.
 - Возвращает найденный корневой каталог.

**Пример:**
`marker_files = ('pyproject.toml', 'requirements.txt')`
Если текущий файл находится в директории `hypotez/src/logger`, функция будет искать `pyproject.toml` и `requirements.txt` в `hypotez/src`, `hypotez`, и т.д., пока не найдет директорию, содержащую эти файлы.

**Шаг 2:** Вызов функции `set_project_root` и сохранение результата в `__root__`

**Шаг 3:** Импорт модуля `gs` из пакета `src`.
**Шаг 4:** Попытка открыть файл `settings.json` в папке `src`, если файл найден, то загружает его содержимое в переменную `settings`. Если файл не найден или некорректен, то `settings` будет None.

**Шаг 5:** Попытка открыть файл `README.MD` в папке `src`. Если файл найден, то загружает его содержимое в переменную `doc_str`. Если файл не найден или некорректен, то `doc_str` будет None.

**Шаг 6:** Инициализация переменных `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__` с использованием данных из `settings`, если они доступны, иначе с использованием значений по умолчанию.

## <mermaid>

```mermaid
graph LR
    A[__file__/__root__] --> B(set_project_root);
    B --> C[__root__];
    C --> D{exists('settings.json')};
    D -- yes --> E[json.load];
    D -- no --> F[settings=None];
    E --> G[__project_name__, __version__, ...];
    F --> G;
    C --> H{exists('README.MD')};
    H -- yes --> I[read];
    H -- no --> J[doc_str=None];
    I --> G;
    J --> G;
    G --> K[__project_name__, __version__, ...];
    subgraph "Import"
      G -.-> src
      src -.-> gs
    end
```

## <explanation>

**Импорты:**
- `sys`: Предоставляет доступ к системным переменным, в частности `sys.path`, для добавления корневой директории проекта в путь поиска модулей.
- `json`: Используется для работы с файлами в формате JSON.
- `packaging.version`: Используется для работы с версиями пакетов, хотя в данном коде это не используется.
- `pathlib`: Предоставляет удобный класс `Path` для работы с путями файлов.
- `src.gs`: Ссылка на модуль `gs`, скорее всего, используемый для работы с различными путями в проекте. Необходимо больше контекста для полного понимания.


**Классы:**
- Нет явных классов.

**Функции:**
- `set_project_root(marker_files)`:  Ищет корневую директорию проекта, начиная с текущей и проходя вверх по дереву директорий, проверяя наличие файлов из списка `marker_files`. Возвращает найденную директорию, а также добавляет её в `sys.path`.

**Переменные:**
- `__root__`: Путь до корневой директории проекта.
- `settings`: Словарь с настройками проекта, загруженный из файла `settings.json`.
- `doc_str`: Строка с текстом README.MD
- `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`: Переменные, содержащие информацию о проекте, полученную из `settings` или с значениями по умолчанию.

**Возможные ошибки и улучшения:**
- Обработка исключений `FileNotFoundError` и `json.JSONDecodeError` в `try-except` блоках является хорошей практикой.
- Использование `Path` вместо строк для работы с путями делает код более безопасным и удобным.
- Для лучшей читаемости и поддержки, стоит использовать абсолютные пути вместо относительных.
- Документация к функциям и переменным может быть более полной.
- Необходимо уточнить назначение и структуру модуля `gs`.  Без знания `gs` трудно оценить все зависимости.

**Взаимосвязь с другими частями проекта:**
- Функция `set_project_root` жизненно необходима для правильной работы остальных импортов в проекте, особенно тех, которые находятся в подкаталогах проекта.
- Модуль `gs` очевидно играет ключевую роль в работе с путями в рамках проекта.  Необходимо больше информации, чтобы понять взаимодействие.
- Данный файл предоставляет глобальные переменные, которые могут быть использованы другими частями проекта, например,  модулями логирования, для поиска файлов.