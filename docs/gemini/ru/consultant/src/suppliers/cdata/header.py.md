# Анализ кода модуля `header.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и читаем.
    - Используется функция `set_project_root` для определения корневой директории проекта.
    - Присутствует обработка исключений при загрузке `settings.json` и `README.MD`.
    - Код соответствует PEP 8.
- Минусы
    - Отсутствует reStructuredText (RST) документация для модуля, функций и переменных.
    - Используется стандартный `json.load` вместо `j_loads` из `src.utils.jjson`.
    - Не используется `logger` для логирования ошибок.
    - `MODE = 'dev'` не используется и не имеет документирования.
    - Отсутствует импорт `j_loads` и `logger`.

**Рекомендации по улучшению**

1.  Добавить reStructuredText (RST) документацию для модуля, функции `set_project_root` и всех переменных.
2.  Использовать `j_loads` из `src.utils.jjson` вместо `json.load`.
3.  Использовать `from src.logger.logger import logger` для логирования ошибок и заменить блоки `try-except` на `logger.error`.
4.  Добавить импорт `j_loads` и `logger`.
5.  Убрать переменную `MODE` или добавить документацию.
6.  Избавиться от `...` заменив их на `pass` или `logger`.
7.  Добавить type hints для переменных.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения и хранения основных настроек проекта.
=========================================================================================

Этот модуль выполняет следующие задачи:

-   Определение корневой директории проекта.
-   Загрузка настроек из файла `settings.json`.
-   Загрузка документации из файла `README.MD`.
-   Определение основных переменных проекта, таких как имя, версия, автор и т.д.
"""

import sys
#  Добавлен импорт j_loads
from src.utils.jjson import j_loads
from packaging.version import Version
#  Добавлен импорт logger
from src.logger.logger import logger
from pathlib import Path
from typing import Tuple, Dict, Optional


# MODE = 'dev' #TODO добавить документацию или удалить
def set_project_root(marker_files: Tuple[str, ...] = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определение корневой директории проекта.

    Начиная с директории текущего файла, функция ищет вверх по дереву каталогов,
    пока не найдет директорию, содержащую хотя бы один из файлов-маркеров.

    :param marker_files: Кортеж с именами файлов или каталогов, которые идентифицируют корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если она найдена, иначе - путь к директории, где находится скрипт.
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


#  Код исполняет поиск корневой директории проекта
__root__: Path = set_project_root()
"""
    :type: Path
    :var __root__:  Путь к корневой директории проекта
"""

from src import gs

settings: Optional[Dict] = None
#  Код исполняет попытку загрузки настроек из файла settings.json
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        #  Используется j_loads вместо json.load
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as ex:
    #  Логирование ошибки с использованием logger.error
    logger.error('Ошибка при загрузке файла settings.json', exc_info=ex)
    pass

doc_str: Optional[str] = None
#  Код исполняет попытку загрузки документации из файла README.MD
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as ex:
    #  Логирование ошибки с использованием logger.error
    logger.error('Ошибка при загрузке файла README.MD', exc_info=ex)
    pass


__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""
    :type: str
    :var __project_name__: Имя проекта
"""
__version__: str = settings.get("version", '') if settings else ''
"""
    :type: str
    :var __version__: Версия проекта
"""
__doc__: str = doc_str if doc_str else ''
"""
    :type: str
    :var __doc__: Документация проекта
"""
__details__: str = ''
"""
    :type: str
    :var __details__: Детали проекта
"""
__author__: str = settings.get("author", '') if settings else ''
"""
    :type: str
    :var __author__: Автор проекта
"""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""
    :type: str
    :var __copyright__: Авторское право проекта
"""
__cofee__: str = settings.get("cofee",
                                "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""
    :type: str
    :var __cofee__: Ссылка на поддержку автора
"""
```