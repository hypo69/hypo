# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    - Код выполняет поиск корневой директории проекта и добавляет её в `sys.path`.
    - Присутствует обработка ошибок при загрузке `settings.json` и `README.MD`.
    - Используется `pathlib.Path` для работы с путями, что является хорошей практикой.
    - Есть переменные с метаданными проекта (`__project_name__`, `__version__` и т.д.).
-  Минусы
    - Отсутствуют импорты `json` и `sys`, необходимых для работы кода.
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Присутствует избыточное использование `try-except` блоков с `...` вместо логирования.
    - Отсутствуют docstring для модуля и функций в формате reStructuredText.
    - Некоторые переменные не имеют аннотаций типов.
    - Имена некоторых переменных и констант не соответствуют стандарту (например, `__root__`, `doc_str`).

**Рекомендации по улучшению**

1.  Добавить импорты `json` и `sys`.
2.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для загрузки `settings.json`.
3.  Заменить использование `try-except` с `...` на логирование ошибок с помощью `logger.error`.
4.  Добавить docstring в формате reStructuredText для модуля и функции `set_project_root`.
5.  Добавить аннотации типов для переменных `__root__` , `doc_str`,  `settings`.
6.  Привести имена переменных в соответствие стандартам (например, `project_root` вместо `__root__`).
7.  Использовать константы для строк (например, `settings.json`, `README.MD`, `hypotez`).
8. Добавить логирование при неудачной загрузке настроек.
9.  Привести код в соответствие со стандартом PEP8.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения корневой директории проекта и загрузки настроек.
========================================================================

Этот модуль определяет корневую директорию проекта, загружает настройки из файла `settings.json`
и документацию из `README.MD`, а также устанавливает глобальные переменные проекта.

Пример использования
--------------------

.. code-block:: python

    from src.suppliers.aliexpress.campaign import header

    # Получение имени проекта
    project_name = header.__project_name__

    # Получение версии проекта
    version = header.__version__
"""
import sys
from pathlib import Path
import json
from src.logger.logger import logger
from src.utils.jjson import j_loads
from src import gs

# Константы
SETTINGS_FILE = 'settings.json'
README_FILE = 'README.MD'
DEFAULT_PROJECT_NAME = 'hypotez'
DEFAULT_COFFEE_MESSAGE = "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"

def set_project_root(marker_files: tuple = ('__root__',)) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция выполняет поиск вверх по директориям, начиная с директории текущего файла,
    до первой директории, содержащей любой из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий для определения корневой директории.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
    :rtype: Path
    """
    current_path: Path = Path(__file__).resolve().parent
    project_root: Path = current_path

    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            project_root = parent
            break
    
    if project_root not in sys.path:
        sys.path.insert(0, str(project_root))
    return project_root

# Получение корневой директории проекта
project_root: Path = set_project_root()
"""Path: Путь к корневой директории проекта."""

settings: dict = {}
"""dict: Словарь с настройками проекта."""
try:
    # код исполняет загрузку настроек из файла settings.json
    with open(project_root / 'src' / SETTINGS_FILE, 'r') as settings_file:
         settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логирование ошибки, если файл не найден или не является JSON
    logger.error(f'Не удалось загрузить настройки из файла {SETTINGS_FILE}: {e}')


doc_str: str = ''
"""str: Строка с содержимым файла README.MD."""
try:
    # код исполняет загрузку документации из файла README.MD
    with open(project_root / 'src' / README_FILE, 'r') as readme_file:
        doc_str = readme_file.read()
except (FileNotFoundError,  UnicodeDecodeError) as e:
    # Логирование ошибки, если файл не найден или не может быть прочитан
    logger.error(f'Не удалось загрузить документацию из файла {README_FILE}: {e}')

__project_name__: str = settings.get("project_name", DEFAULT_PROJECT_NAME) if settings else DEFAULT_PROJECT_NAME
"""str: Имя проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта."""
__details__: str = ''
"""str: Детали проекта."""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Авторские права проекта."""
__cofee__: str = settings.get("cofee", DEFAULT_COFFEE_MESSAGE) if settings else DEFAULT_COFFEE_MESSAGE
"""str: Сообщение для поддержки разработчика."""
```