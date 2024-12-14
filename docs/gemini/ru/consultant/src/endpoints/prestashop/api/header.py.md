# Анализ кода модуля `header.py`

**Качество кода**
7
 -  Плюсы
    -  Код структурирован, выделены основные блоки.
    -  Используются аннотации типов.
    -  Есть обработка исключений при чтении файлов настроек и документации.
 -  Минусы
    -  Отсутствуют docstring для модуля и функций.
    -  Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    -  Не используется `from src.logger.logger import logger` для логирования ошибок.
    -  Избыточное использование `try-except` блоков.
    -  Имена переменных  `doc_str`, `__cofee__` не соответствуют стандарту оформления.
    -  Не все переменные имеют аннотации типов.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля и функции `set_project_root`.
2.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо `json.load`.
3.  Использовать `from src.logger.logger import logger` для логирования ошибок.
4.  Избегать избыточного использования `try-except` блоков, заменив на `logger.error` .
5.  Привести имена переменных `doc_str` и `__cofee__` к виду `doc_string` и `__coffee__` соответственно.
6.  Добавить аннотации типов для переменных.
7.  Добавить RST комментарии для всех переменных.
8.  Вместо `sys.path.insert(0, str(__root__))` использовать `sys.path.append(str(__root__))`, чтобы не нарушать порядок путей.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения и установки корневой директории проекта и загрузки настроек.
=========================================================================================

Этот модуль содержит функции и переменные, необходимые для определения корневой директории проекта,
загрузки настроек из файла `settings.json`, а также чтения документации из файла `README.MD`.
Также определены глобальные переменные, содержащие информацию о проекте.

Пример использования
--------------------

.. code-block:: python

    from src.endpoints.prestashop.api.header import __root__, settings, __project_name__, __version__, __doc__, __author__, __copyright__, __coffee__

    print(f"Root directory: {__root__}")
    print(f"Project name: {__project_name__}")
"""

MODE = 'dev'

import sys
from pathlib import Path
from typing import Tuple, Dict, Optional, Any
#  импортируем j_loads
from src.utils.jjson import j_loads
#  импортируем logger
from src.logger.logger import logger
from packaging.version import Version

def set_project_root(marker_files: Tuple[str, ...] = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Ищет корневую директорию проекта, начиная с директории текущего файла,
    просматривая вверх и останавливаясь на первой директории, содержащей любой из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий, идентифицирующих корень проекта.
    :type marker_files: Tuple[str, ...]
    :return: Путь к корневой директории.
    :rtype: Path
    """
    current_path: Path = Path(__file__).resolve().parent
    __root__: Path = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        #  добавляем путь к корневой директории в sys.path
        sys.path.append(str(__root__))
    return __root__


# Получаем корневую директорию проекта
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта."""

from src import gs

settings: Optional[Dict[str, Any]] = None
try:
    # код исполняет открытие файла и загрузку настроек
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        # используем j_loads вместо json.load
        settings = j_loads(settings_file)
#  используем logger.error вместо пустого except
except (FileNotFoundError, json.JSONDecodeError) as e:
    logger.error(f'Ошибка при загрузке файла настроек: {e}')
    ...

doc_string: Optional[str] = None
try:
    # код исполняет открытие файла и чтение документации
    with open(gs.path.root / 'src' /  'README.MD', 'r') as settings_file:
        doc_string = settings_file.read()
#  используем logger.error вместо пустого except
except (FileNotFoundError, json.JSONDecodeError) as e:
    logger.error(f'Ошибка при чтении файла документации: {e}')
    ...

#  получаем имя проекта из настроек
__project_name__: str = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
"""__project_name__ (str): Имя проекта."""
# получаем версию проекта из настроек
__version__: str = settings.get("version", '')  if settings  else ''
"""__version__ (str): Версия проекта."""
#  получаем строку документации
__doc__: str = doc_string if doc_string else ''
"""__doc__ (str): Строка документации."""
__details__: str = ''
"""__details__ (str): Детали проекта."""
# получаем автора проекта из настроек
__author__: str = settings.get("author", '')  if settings  else ''
"""__author__ (str): Автор проекта."""
# получаем копирайт из настроек
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
"""__copyright__ (str): Копирайт проекта."""
# получаем строку с призывом к поддержке проекта
__coffee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__coffee__ (str): Строка с призывом к поддержке проекта."""
```