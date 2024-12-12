# Анализ кода модуля `header.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и понятен.
    - Используется `pathlib` для работы с путями, что делает код более кроссплатформенным.
    - Функция `set_project_root` корректно определяет корневую директорию проекта.
    -  Логика загрузки настроек и документации из файлов реализована с использованием `try-except`.
    - Присутствует определение основных метаданных проекта (имя, версия, автор, и т.д.).
- Минусы
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    - Отсутствует обработка ошибок с использованием `logger.error`.
    - Не все переменные и функции имеют docstring в формате RST.
    - Есть избыточное использование `try-except`.

**Рекомендации по улучшению**
1. Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
2. Добавить логирование ошибок с помощью `logger.error` в блоках `try-except`.
3. Добавить docstring в формате RST для всех функций, переменных и модуля.
4. Убрать лишние `try-except`, там где это можно сделать через `if`
5. Привести в соответствие имена переменных и импортов с ранее обработанными файлами.
6. Добавить импорт для `logger` из `src.logger.logger`.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для настройки окружения и загрузки конфигурации проекта.
===============================================================

Этот модуль содержит функции и переменные для определения корневой директории проекта,
загрузки настроек из файла `settings.json`, чтения документации из файла `README.MD`,
а также определения основных метаданных проекта, таких как имя, версия и автор.

.. code-block:: python

   from src.webdriver.crawlee_python import header

   print(header.__project_name__)
   print(header.__version__)

"""
MODE = 'dev'

import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads
from src.logger.logger import logger

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла,
    продвигаясь вверх до первой директории, содержащей любой из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий для идентификации корня проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если она найдена, иначе - директория, где расположен скрипт.
    :rtype: Path
    """
    __root__: Path
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Код исполняет поиск корневой директории проекта
__root__ = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта"""

from src import gs

settings: dict = None
# Код пытается прочитать файл настроек settings.json
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except FileNotFoundError:
     logger.error(f'Файл настроек не найден: {gs.path.root / "src" / "settings.json"}')
     ...
except Exception as ex:
     logger.error(f'Ошибка при чтении файла настроек {gs.path.root / "src" / "settings.json"}', exc_info=ex)
     ...

doc_str: str = None
# Код пытается прочитать файл документации README.MD
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as doc_file:
        doc_str = doc_file.read()
except FileNotFoundError:
     logger.error(f'Файл документации не найден: {gs.path.root / "src" / "README.MD"}')
     ...
except Exception as ex:
    logger.error(f'Ошибка при чтении файла документации {gs.path.root / "src" / "README.MD"}', exc_info=ex)
    ...

# Код устанавливает значения метаданных проекта, если настройки загружены
__project_name__ = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Имя проекта"""
__version__: str = settings.get('version', '') if settings else ''
"""__version__ (str): Версия проекта"""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Документация проекта"""
__details__: str = ''
"""__details__ (str): Детали проекта"""
__author__: str = settings.get('author', '') if settings else ''
"""__author__ (str): Автор проекта"""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""__copyright__ (str): Авторские права проекта"""
__cofee__: str = settings.get('cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69')  if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
"""__cofee__ (str): Сообщение для поддержки разработчика"""
```