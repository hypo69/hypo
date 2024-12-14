# Анализ кода модуля `header.py`

**Качество кода**
8
 -  Плюсы
    -  Код структурирован и выполняет поставленную задачу по определению корневой директории проекта и загрузке настроек.
    -  Используется `pathlib` для работы с путями, что является хорошей практикой.
    -  Присутствует обработка исключений при загрузке файлов настроек.
 -  Минусы
    -  Не все переменные и функции документированы в формате reStructuredText (RST).
    -  Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    -  Избыточное использование `try-except` без логирования ошибок.
    -  Некоторые переменные могли бы быть константами.
    -  отсутствует `from src.logger.logger import logger`.
    -  Импорт `gs` используется как есть.

**Рекомендации по улучшению**
1. Добавить недостающую документацию в формате RST для всех переменных, функций и модуля.
2. Заменить `json.load` на `j_loads` или `j_loads_ns`.
3. Улучшить обработку исключений с использованием `logger.error`.
4. Добавить импорт `from src.logger.logger import logger`
5. Использовать константы для не изменяемых переменных, например `MARKER_FILES`.
6. Привести в соответствие импорт `gs` c предыдущими файлами.
7. Добавить проверку, что `settings` не `None` перед тем как получать данные.
8. Убрать `...` и прологировать ошибки.
9. Добавить `from src.utils.jjson import j_loads`

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения корневой директории проекта и загрузки настроек.
========================================================================

Этот модуль предоставляет функциональность для определения корневой директории проекта
на основе наличия определенных файлов-маркеров и загружает настройки проекта из файла `settings.json`.
Также загружает документацию из файла `README.MD`.

Пример использования
--------------------

.. code-block:: python

    from src.webdriver.header import __root__, __project_name__, __version__, __doc__, __author__

    print(f"Project Root: {__root__}")
    print(f"Project Name: {__project_name__}")
    print(f"Project Version: {__version__}")
"""
MODE = 'dev'

import sys
from pathlib import Path
# from json import load  # Используем j_loads
from packaging.version import Version
from typing import Tuple, List
from src.logger.logger import logger
from src.utils.jjson import j_loads
from src import gs


MARKER_FILES: Tuple[str, ...] = ('pyproject.toml', 'requirements.txt', '.git')
"""
Tuple[str, ...]: Файлы-маркеры для определения корневой директории проекта.
"""


def set_project_root(marker_files: Tuple[str, ...] = MARKER_FILES) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла,
    поднимаясь вверх по дереву каталогов и останавливаясь на первой директории,
    содержащей любой из файлов-маркеров.

    :param marker_files: Список файлов-маркеров для определения корневой директории.
    :type marker_files: Tuple[str, ...]
    :return: Путь к корневой директории проекта.
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

# Получаем корневую директорию проекта.
__root__:Path = set_project_root()
"""Path: Путь к корневой директории проекта."""

settings: dict = None
"""dict: Словарь с настройками проекта."""
try:
    #  Код пытается открыть и загрузить файл настроек `settings.json`
    with open(gs.path.root / 'src' / 'settings.json', 'r', encoding='utf-8') as settings_file:
        settings = j_loads(settings_file)  # Используем j_loads вместо json.load
except FileNotFoundError as e:
    #  Код логирует ошибку, если файл не найден
    logger.error(f'Файл настроек не найден: {e}')
    ...
except Exception as e:
     #  Код логирует ошибку, если файл не найден
    logger.error(f'Ошибка загрузки файла настроек: {e}')
    ...



doc_str: str = None
"""str: Строка с содержимым файла README.MD."""
try:
    # Код пытается открыть и прочитать файл `README.MD`
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as readme_file:
        doc_str = readme_file.read()
except FileNotFoundError as e:
    #  Код логирует ошибку, если файл не найден
    logger.error(f'Файл README.MD не найден: {e}')
    ...
except Exception as e:
    #  Код логирует ошибку, если файл не найден
    logger.error(f'Ошибка загрузки файла README.MD: {e}')
    ...


#  Код устанавливает имя проекта из файла настроек или по умолчанию 'hypotez'
__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Имя проекта."""
# Код устанавливает версию проекта из файла настроек или пустую строку по умолчанию
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
# Код устанавливает строку документации из файла `README.MD` или пустую строку по умолчанию.
__doc__: str = doc_str if doc_str else ''
"""str: Строка документации проекта."""
__details__: str = ''
"""str: Детали проекта."""
#  Код устанавливает автора проекта из файла настроек или пустую строку по умолчанию
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
#  Код устанавливает копирайт проекта из файла настроек или пустую строку по умолчанию
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Копирайт проекта."""
#  Код устанавливает сообщение про кофе для разработчика из файла настроек или строку по умолчанию
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение о поддержке разработчика."""
```