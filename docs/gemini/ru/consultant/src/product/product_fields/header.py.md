# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    - Код выполняет задачу определения корневой директории проекта и загрузки настроек.
    - Используется `pathlib` для работы с путями.
    - Присутствует обработка исключений `FileNotFoundError` и `json.JSONDecodeError` при загрузке настроек.
-  Минусы
    -  Не все комментарии и docstring соответствуют reStructuredText.
    -  Используется `json.load` вместо `j_loads` или `j_loads_ns`.
    -  Не используется логирование ошибок.
    -  Присутствуют избыточные пустые docstring.
    -  Не все переменные имеют аннотации типов.
    -  Некоторые названия переменных не соответствуют code style.

**Рекомендации по улучшению**
1. Заменить стандартный `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
2. Добавить логирование ошибок с помощью `logger.error` вместо `...` в блоках `except`.
3. Переписать все docstring в формате reStructuredText.
4.  Добавить аннотации типов для переменных `settings`, `doc_str`.
5.  Удалить лишние пустые docstring.
6.  Привести названия переменных в соответствие code style.
7.  Использовать `from src.logger.logger import logger` для логирования.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#!\venv\Scripts\python.exe
#!\venv\bin\python\python3.12
"""
Модуль для определения корневой директории проекта и загрузки настроек.
=========================================================================================

Этот модуль содержит функции и переменные для определения корневой директории проекта,
загрузки настроек из файла `settings.json` и документации из файла `README.MD`.

Пример использования
--------------------

.. code-block:: python

    from src.product.product_fields.header import __root__, __project_name__, __version__, __doc__

    print(__root__)
    print(__project_name__)
    print(__version__)
    print(__doc__)
"""

import sys
# from json import load # Заменено на j_loads или j_loads_ns
from packaging.version import Version
from pathlib import Path
from typing import Optional, Dict
from src.utils.jjson import j_loads
from src.logger.logger import logger

MODE = 'dev'

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневой каталог проекта, начиная с каталога текущего файла,
    поиском вверх и остановкой на первом каталоге, содержащем любой из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов для определения корня проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу, если найден, иначе каталог, где находится скрипт.
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

# Получение корневой директории проекта
__root__: Path = set_project_root()
"""
    :type: Path
    :description: Путь к корневой директории проекта
"""

from src import gs

settings: Optional[Dict] = None
# Блок try-except для обработки ошибок загрузки файла настроек
try:
    # Чтение настроек из файла settings.json с использованием j_loads
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
         settings = j_loads(settings_file)
except FileNotFoundError as ex:
    # Логирование ошибки, если файл не найден
    logger.error('Файл settings.json не найден', ex)
    ...
except Exception as ex:
    # Логирование ошибки, если не удалось декодировать JSON
    logger.error('Ошибка декодирования JSON в файле settings.json', ex)
    ...

doc_str: Optional[str] = None
# Блок try-except для обработки ошибок чтения файла README.MD
try:
    # Чтение содержимого файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except FileNotFoundError as ex:
    # Логирование ошибки, если файл не найден
     logger.error('Файл README.MD не найден', ex)
    ...
except Exception as ex:
    # Логирование ошибки, если не удалось прочитать файл
    logger.error('Ошибка чтения файла README.MD', ex)
    ...


__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""
    :type: str
    :description: Название проекта
"""
__version__: str = settings.get("version", '') if settings else ''
"""
    :type: str
    :description: Версия проекта
"""
__doc__: str = doc_str if doc_str else ''
"""
    :type: str
    :description: Документация проекта
"""
__details__: str = ''
"""
    :type: str
    :description: Детали проекта
"""
__author__: str = settings.get("author", '') if settings else ''
"""
    :type: str
    :description: Автор проекта
"""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""
    :type: str
    :description: Авторские права проекта
"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""
    :type: str
    :description: Сообщение для поддержки разработчика
"""
```