# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    - Код содержит docstring для модуля и функции `set_project_root`.
    - Используется `pathlib` для работы с путями, что делает код более читаемым и кроссплатформенным.
    - Наличие констант `__project_name__`, `__version__`, `__doc__`, `__author__`, `__copyright__`, `__cofee__`.
    - Попытка загрузки `settings.json` и `README.MD` с обработкой ошибок.
-  Минусы
    - Отсутствует reStructuredText (RST)  форматирование в docstring.
    - Не используются `j_loads` или `j_loads_ns` для загрузки JSON.
    - Использование `try-except` с `...` для обработки ошибок.
    - Отсутствуют комментарии к блокам кода после `#`.
    - Не хватает импорта для `logger`.
    - Код местами не соответствует PEP 8 по форматированию.

**Рекомендации по улучшению**

1.  Использовать reStructuredText (RST) для docstring.
2.  Заменить `json.load` на `j_loads` из `src.utils.jjson`.
3.  Использовать `logger.error` для логирования ошибок вместо `try-except` с `...`.
4.  Добавить импорт `logger` из `src.logger.logger`.
5.  Добавить комментарии к блокам кода после `#`.
6.  Убрать не нужные `#! venv/Scripts/python.exe` и `#! venv/bin/python/python3.12`
7.  Добавить тип для переменной `__root__` в функции `set_project_root`
8.  Форматировать код согласно PEP 8.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для определения настроек проекта и переменных окружения.
=================================================================

Этот модуль отвечает за настройку окружения проекта,
включая определение корневой директории, загрузку настроек из `settings.json`
и чтение документации из `README.MD`.

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

    Функция ищет корневой каталог проекта, начиная с директории текущего файла,
    просматривая родительские директории до тех пор, пока не будет найдена директория,
    содержащая один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов, используемых для идентификации корня проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
    :rtype: Path
    """
    __root__:Path
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Определяет корневой каталог проекта
__root__:Path = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта"""

from src import gs

settings: dict = None
try:
    # Код пытается открыть и загрузить содержимое файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, Exception) as ex:
    # Логирование ошибки если не удалось загрузить файл
    logger.error('Не удалось загрузить файл settings.json', ex)


doc_str: str = None
try:
    # Код пытается открыть и прочитать содержимое файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, Exception) as ex:
     # Логирование ошибки если не удалось прочитать файл
    logger.error('Не удалось загрузить файл README.MD', ex)



__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Имя проекта"""
__version__: str = settings.get("version", '') if settings else ''
"""__version__ (str): Версия проекта"""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Строка документации проекта"""
__details__: str = ''
"""__details__ (str): Детали проекта"""
__author__: str = settings.get("author", '') if settings else ''
"""__author__ (str): Автор проекта"""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""__copyright__ (str): Авторские права проекта"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Сообщение для пожертвования автору"""
```