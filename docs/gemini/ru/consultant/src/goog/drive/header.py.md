# Анализ кода модуля `header.py`

**Качество кода**
8
 -  Плюсы
        - Код структурирован и разделен на логические блоки.
        - Используется `pathlib` для работы с путями, что делает код более читаемым и переносимым.
        - Функция `set_project_root` корректно определяет корневую директорию проекта.
        - Код использует `try-except` блоки для обработки ошибок при чтении файлов.
        - Присутствует информация о проекте, версии, авторе и т.д.
 -  Минусы
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для загрузки `json`
    - Отсутствует reStructuredText документация для модуля и функций.
    - Избыточное использование `try-except` блоков.
    - Не все переменные и константы аннотированы.
    - Отсутствует импорт `logger` из `src.logger.logger`.

**Рекомендации по улучшению**

1. **Документирование кода:**
   - Добавить reStructuredText (RST) документацию для модуля и функции `set_project_root`, включая параметры, возвращаемое значение и примеры использования.
2. **Использование `j_loads`:**
   - Заменить стандартный `json.load` на `j_loads` из `src.utils.jjson` для чтения `settings.json`.
3. **Логирование ошибок:**
   - Использовать `logger.error` для логирования ошибок вместо `print` и `...`.
   - Импортировать `logger` из `src.logger.logger`.
4. **Удаление лишних try-except блоков:**
   - Избавиться от `try-except` в блоках чтения файла `README.MD`. Вместо этого использовать проверку `if doc_str`
5. **Аннотирование переменных:**
   - Добавить аннотации типов для переменных `settings`, `doc_str`, `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`
6. **Форматирование кода:**
   - Привести в соответствие код с ранее обработанными файлами.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для настройки проекта.
=========================================================================================

Этот модуль определяет константы и настройки проекта, такие как имя проекта, версию,
автора и другие параметры, загружаемые из файла `settings.json`.
Также модуль устанавливает корневую директорию проекта и добавляет её в `sys.path`.

Пример использования
--------------------

Импортируйте модуль для доступа к константам и настройкам проекта:

.. code-block:: python

    from src.goog.drive.header import __project_name__, __version__, __doc__, __author__

"""
MODE = 'dev'

import sys
from pathlib import Path
from typing import Tuple, Optional, Dict
from packaging.version import Version
# TODO: from src.utils.jjson import j_loads # добавить импорт после появления файла jjson.py
from src.logger.logger import logger


def set_project_root(marker_files: Tuple[str, ...] = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла
    и поднимаясь вверх по дереву каталогов, пока не найдет один из файлов-маркеров.

    :param marker_files: Кортеж с именами файлов или каталогов, которые считаются маркерами корневой директории.
    :type marker_files: tuple[str, ...]
    :return: Путь к корневой директории.
    :rtype: Path
    
    :raises FileNotFoundError: Если ни один из файлов-маркеров не найден, возвращает директорию где находится скрипт.

    Пример:

    .. code-block:: python

        root_path = set_project_root()
        print(f"Корневая директория: {root_path}")
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


# Получение корневой директории проекта
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта"""

from src import gs

settings: Optional[Dict] = None
try:
    # код исполняет открытие файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        # код исполняет чтение файла settings.json
        settings =  json.load(settings_file) # TODO: j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    logger.error(f"Ошибка при чтении файла settings.json: {e}")
    settings = {}

doc_str: Optional[str] = None
try:
     # код исполняет открытие файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        # код исполняет чтение файла README.MD
        doc_str = settings_file.read()
except FileNotFoundError as e:
    logger.error(f"Ошибка при чтении файла README.MD: {e}")
    doc_str = ''


__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Имя проекта"""
__version__: str = settings.get("version", '') if settings else ''
"""__version__ (str): Версия проекта"""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Документация проекта"""
__details__: str = ''
"""__details__ (str): Дополнительные детали проекта"""
__author__: str = settings.get("author", '') if settings else ''
"""__author__ (str): Автор проекта"""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""__copyright__ (str): Информация об авторских правах"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Сообщение для поддержки разработчика"""
```