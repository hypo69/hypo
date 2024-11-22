```
## Полученный код

```python
## \file hypotez/src/scenario/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.scenario """
MODE = 'development'

import sys
import json
from packaging.version import Version

from pathlib import Path
def get_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
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
__root__: Path = get_project_root()
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

```
## Улучшенный код

```python
## \file hypotez/src/scenario/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.scenario """
MODE = 'development'

import sys
import json
from packaging.version import Version
from pathlib import Path
from src.utils.jjson import j_loads

import logging
logger = logging.getLogger(__name__)


def get_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.

    :param marker_files: Filenames or directory names to identify the project root.
    :type marker_files: tuple
    :return: Path to the root directory if found, otherwise the directory where the script is located.
    :rtype: Path
    """
    current_path = Path(__file__).resolve().parent
    project_root = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            project_root = parent
            break
    if project_root not in sys.path:
        sys.path.insert(0, str(project_root))
    return project_root


# Get the root directory of the project
PROJECT_ROOT = get_project_root()
"""PROJECT_ROOT (Path): Path to the root directory of the project"""


settings = None
try:
    settings = j_loads((PROJECT_ROOT / 'src' / 'settings.json').open('r'))
except FileNotFoundError:
    logger.error("File 'settings.json' not found in the project root")
except json.JSONDecodeError as e:
    logger.error(f"Error decoding 'settings.json': {e}")


try:
    with open(PROJECT_ROOT / 'src' / 'README.MD', 'r', encoding="utf-8") as readme_file:
        doc_str = readme_file.read()
except FileNotFoundError:
    logger.error("File 'README.MD' not found in the project root")
except Exception as e:
    logger.error(f"Error reading 'README.MD': {e}")

__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
__version__ = settings.get("version", '') if settings else ''
__doc__ = doc_str if doc_str else ''
__details__ = ''
__author__ = settings.get("author", '') if settings else ''
__copyright__ = settings.get("copyright", '') if settings else ''
__cofee__ = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```

```
## Изменения

- Импортирован `j_loads` из `src.utils.jjson`.
- Заменены стандартные `try...except` блоки на использование `logger.error`.
- Добавлена обработка кодировки UTF-8 при чтении файла README.MD.
- Исправлено написание слова "copyrihgnt" на "copyright".
- Переменная `__root__` переименована на `PROJECT_ROOT` для лучшей читаемости.
- Добавлено описание типов для аргумента `marker_files` и возвращаемого значения функции `get_project_root` в docstring.
- Добавлены более информативные сообщения об ошибках в `logger.error`.
- Добавлен `import logging` и инициализирована переменная logger.
- Добавлены RST-комментарии к функции `get_project_root`.
- Изменен стиль импорта (`from ... import ...`).
- Убраны ненужные комментарии.


**TODO:**

- Добавить проверку на корректность формата данных в `settings.json`.
- Добавить более подробные сообщения об ошибках, включая тип ошибки.
- Добавить логирование уровня DEBUG для отладки.
- Рассмотреть возможность использования `pathlib` для более гибкой работы с путями.
```