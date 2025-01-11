# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    - Код выполняет свою задачу по определению корневой директории проекта и загрузке настроек.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Присутствуют комментарии, описывающие назначение функций.
    - Код читабельный и логически понятный.
-  Минусы
    - Отсутствует документация в формате RST для модуля и функций.
    - Используется `json.load` вместо `j_loads` или `j_loads_ns`.
    - Обработка ошибок выполняется с использованием `try-except`, а не через `logger.error`.
    - Отсутствует импорт `logger` из `src.logger.logger`.
    - Не все переменные имеют type hints.
    - Есть опечатка в слове `copyrihgnt`.
    - Проверка на `settings is None` дублируется в нескольких строках.
    - Нет пояснения, что делает `gs`.
    - Нет описания `settings.json`, `README.md` в документации.

**Рекомендации по улучшению**
1. Добавить документацию в формате RST для модуля и функции `set_project_root`.
2. Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
3. Использовать `logger.error` для обработки исключений вместо стандартного `try-except`.
4. Добавить импорт `logger` из `src.logger.logger`.
5. Добавить type hints для переменных.
6. Исправить опечатку в слове `copyrihgnt`.
7. Убрать дублирование проверки `settings is None`, заменив на `settings = settings or {}`.
8. Добавить описание модуля и переменных.
9. Добавить описание для `gs` и `settings.json`, `README.md`.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для определения корневой директории проекта и загрузки настроек.
=======================================================================

Этот модуль содержит функции для определения корневой директории проекта
и загрузки настроек из файлов `settings.json` и `README.MD`.

.. note::
    Корневая директория определяется путем поиска файлов-маркеров, таких как `__root__` или `.git`,
    вверх по структуре директорий от текущего местоположения файла.

    Настройки проекта загружаются из файла `settings.json`, а описание проекта - из `README.MD`.

    Все ошибки, возникающие в процессе, логируются с использованием `logger`.
"""

import sys
from pathlib import Path
from typing import Tuple, Dict
from src.utils.jjson import j_loads
from src.logger.logger import logger # Импорт logger

def set_project_root(marker_files: Tuple[str, ...] = ('__root__', '.git')) -> Path:
    """
    Определяет корневую директорию проекта, начиная с директории текущего файла,
    путем поиска вверх по иерархии директорий до первой директории, содержащей
    любой из файлов-маркеров.

    :param marker_files: Список имен файлов или директорий, которые используются для идентификации
                        корневой директории проекта.
    :type marker_files: Tuple[str, ...]
    :return: Путь к корневой директории, если она найдена, иначе - директория, где расположен скрипт.
    :rtype: Path

    :Example:
        >>> set_project_root()
        PosixPath('/path/to/your/project')
    """
    __root__: Path
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    # Код ищет родительские каталоги, пока не найдет маркерные файлы.
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    # Код добавляет корневую директорию в sys.path, если ее там нет.
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Вызов функции для определения корневой директории проекта
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта."""

from src import gs
"""gs: Модуль для хранения глобальных переменных и констант"""


settings: Dict = {}
# Попытка загрузить настройки из файла settings.json.
try:
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as ex:
    logger.error(f'Ошибка при загрузке settings.json: {ex}')
    ...

doc_str: str = ''
# Попытка загрузить описание проекта из файла README.MD.
try:
    with open(gs.path.root / 'src' /  'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as ex:
    logger.error(f'Ошибка при загрузке README.MD: {ex}')
    ...

settings = settings or {} # Устанавливаем settings = {}, если  settings is None
__project_name__: str = settings.get("project_name", 'hypotez')
"""__project_name__ (str): Имя проекта, по умолчанию 'hypotez'."""
__version__: str = settings.get("version", '')
"""__version__ (str): Версия проекта."""
__doc__: str = doc_str
"""__doc__ (str): Описание проекта, считанное из README.MD."""
__details__: str = ''
"""__details__ (str): Детали проекта."""
__author__: str = settings.get("author", '')
"""__author__ (str): Автор проекта."""
__copyright__: str = settings.get("copyright", '')
"""__copyright__ (str): Информация об авторских правах проекта."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")
"""__cofee__ (str): Сообщение о возможности угостить разработчика кофе."""
```