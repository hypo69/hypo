# Анализ кода модуля `header`

**Качество кода:**

- **Соответствие стандартам**: 6/10
- **Плюсы**:
    - Код выполняет поставленную задачу по определению корневой директории проекта.
    - Используется `pathlib` для работы с путями, что улучшает читаемость кода.
    - Присутствует базовая обработка ошибок при чтении файлов `settings.json` и `README.MD`.
- **Минусы**:
    - Используются стандартные `json.load` и `open` вместо `j_loads` и `j_loads_ns` из `src.utils.jjson`.
    - Отсутствует явное логирование ошибок.
    - Не хватает `RST` документации для модуля и функций.
    - Не все переменные и импорты выровнены.
    - Используются двойные кавычки для строк, кроме `print`.
    - Используется устаревший способ добавления пути проекта `sys.path.insert`.
    - Есть опечатка в имени переменной `copyrihgnt`.

**Рекомендации по улучшению:**

1.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.load`.
2.  Добавить логирование ошибок с использованием `logger.error` из `src.logger`.
3.  Добавить `RST` документацию для модуля и функции `set_project_root`.
4.  Выровнять названия функций, переменных и импортов.
5.  Использовать одинарные кавычки для строк, за исключением операций вывода.
6.  Переработать способ добавления пути в `sys.path` на более корректный.
7.  Исправить опечатку в переменной `copyrihgnt`.
8.  Удалить магические переменные, а использовать константы в верхнем регистре.

**Оптимизированный код:**

```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

"""
Модуль для определения корневой директории проекта и загрузки настроек.
======================================================================

Этот модуль содержит функции для автоматического определения корневой директории проекта
и загрузки настроек из файлов `settings.json` и `README.MD`.

Пример использования
----------------------
.. code-block:: python

    from pathlib import Path
    from src.suppliers.chat_gpt.header import PROJECT_ROOT, SETTINGS, PROJECT_NAME, VERSION, DOC, DETAILS, AUTHOR, COPYRIGHT, COFEE

    print(f"Project root: {PROJECT_ROOT}")
    print(f"Project name: {PROJECT_NAME}")
    print(f"Project version: {VERSION}")
"""
import sys
from pathlib import Path

from packaging.version import Version

from src.utils.jjson import j_loads #  Импорт j_loads из src.utils.jjson
from src.logger import logger # Импорт logger из src.logger

MARKER_FILES = ('__root__', '.git') # Замена кортежа на константу

def set_project_root(marker_files: tuple = MARKER_FILES) -> Path:
    """
    Находит корневой каталог проекта, начиная с каталога текущего файла,
    поиском вверх и остановкой в первом каталоге, содержащем любой из маркерных файлов.

    :param marker_files: Имена файлов или каталогов для определения корня проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу, если найден, иначе - каталог, где расположен скрипт.
    :rtype: Path

    Пример:
        >>> from pathlib import Path
        >>> root_path = set_project_root()
        >>> print(root_path)
        /path/to/your/project
    """
    current_path: Path = Path(__file__).resolve().parent
    root_path: Path = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            root_path = parent
            break
    return root_path

# Получение корневого каталога проекта
PROJECT_ROOT: Path = set_project_root()

# Добавление корневого каталога в sys.path
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT)) #  Используем insert для добавления в начало списка

SETTINGS: dict = None
try:
    with open(PROJECT_ROOT / 'src' / 'settings.json', 'r') as settings_file:
        SETTINGS = j_loads(settings_file) # Используем j_loads
except (FileNotFoundError, json.JSONDecodeError) as e:
    logger.error(f'Error loading settings.json: {e}') #  Логирование ошибки

DOC: str = None
try:
    with open(PROJECT_ROOT / 'src' / 'README.MD', 'r') as doc_file:
        DOC = doc_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    logger.error(f'Error loading README.MD: {e}') # Логирование ошибки

PROJECT_NAME: str = SETTINGS.get('project_name', 'hypotez') if SETTINGS else 'hypotez' #  Замена двойных кавычек на одинарные
VERSION: str = SETTINGS.get('version', '') if SETTINGS else '' # Замена двойных кавычек на одинарные
DOC: str = DOC if DOC else ''
DETAILS: str = ''
AUTHOR: str = SETTINGS.get('author', '') if SETTINGS else '' # Замена двойных кавычек на одинарные
COPYRIGHT: str = SETTINGS.get('copyright', '') if SETTINGS else '' # Исправлена опечатка, замена двойных кавычек на одинарные
COFEE: str = SETTINGS.get('cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69')  if SETTINGS  else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69' # Замена двойных кавычек на одинарные
```