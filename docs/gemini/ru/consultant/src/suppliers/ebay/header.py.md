# Анализ кода модуля `header.py`

**Качество кода**
8
- Плюсы
    - Код выполняет свою задачу по установке корневой директории проекта и загрузке настроек.
    - Используется `pathlib` для работы с путями.
    - Присутствует обработка исключений при загрузке файла настроек.
    - Код содержит docstring для функции `set_project_root`.
- Минусы
    - Используется `json.load` вместо `j_loads` или `j_loads_ns`.
    - Отсутствуют docstring для переменных модуля.
    - Не используется `logger` для логирования ошибок.
    - `try-except` блоки можно упростить, используя `logger.error`.
    - Присутствует избыточное использование `if settings else ...` для присваивания значений переменным.
    - Не используется reStructuredText (RST) для docstring и комментариев.
    - Нет проверки на наличие ключей в словаре `settings` перед обращением к ним.

**Рекомендации по улучшению**

1. Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
2. Добавить docstring в формате RST для всех переменных модуля.
3. Использовать `from src.logger.logger import logger` для логирования ошибок и заменить `try-except` на `logger.error`.
4. Упростить присваивание значений переменным, используя оператор `or`.
5. Добавить проверки на существование ключей в словаре `settings` перед их использованием с помощью метода `get()`.
6.  Переписать все docstring и комментарии в формате reStructuredText (RST).
7.  Добавить проверки на существование `settings` и `doc_str` при присвоении значений `__project_name__`, `__version__`, `__doc__`, `__author__`, `__copyright__`, `__cofee__`

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для определения настроек проекта и путей.
=========================================================================================

Этот модуль содержит функции и переменные для:
    - определения корневой директории проекта
    - загрузки настроек из файла `settings.json`
    - загрузки документации из `README.MD`
    - установки глобальных переменных проекта

Пример использования
--------------------

.. code-block:: python

    from src.suppliers.ebay import header

    print(header.__project_name__)
    print(header.__version__)
"""


import sys
from pathlib import Path
# from src.utils.jjson import j_loads # TODO import j_loads
# from src.logger.logger import logger # TODO import logger
import json # TODO remove json import
from packaging.version import Version



def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определение корневой директории проекта.

    Ищет корневую директорию проекта, начиная с текущей директории файла.
    Поиск идет вверх по дереву каталогов до тех пор, пока не будет найдена директория,
    содержащая один из файлов-маркеров.

    :param marker_files: Кортеж с именами файлов или директорий, используемых для идентификации корневой директории.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
    :rtype: Path
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    # Код перебирает все родительские директории текущего файла
    for parent in [current_path] + list(current_path.parents):
        # Код проверяет существование одного из файлов-маркеров в текущей директории
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    # Код добавляет корневую директорию в sys.path, если ее там нет
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Код устанавливает корневую директорию проекта
__root__ = set_project_root()
"""
Path: Путь к корневой директории проекта.
"""

from src import gs

settings: dict = None
# Код загружает настройки из файла settings.json
try:
    # with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
    #     settings = json.load(settings_file)
    # TODO: use j_loads
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = json.load(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as ex:
    # logger.error(f'Ошибка загрузки файла настроек {ex=}') # TODO use logger
    ...


doc_str: str = None
# Код загружает документацию из файла README.MD
try:
    with open(gs.path.root / 'src' /  'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as ex:
    # logger.error(f'Ошибка загрузки файла документации {ex=}') # TODO use logger
    ...


__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Название проекта."""
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
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение для поддержки проекта."""
```