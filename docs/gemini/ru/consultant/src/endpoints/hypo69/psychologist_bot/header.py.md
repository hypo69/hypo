# Анализ кода модуля `header.py`

**Качество кода**
9
-   Плюсы
    -   Код хорошо структурирован и читаем.
    -   Используется функция `set_project_root` для определения корня проекта, что полезно для работы с путями.
    -   Присутствует обработка исключений при чтении файлов настроек и документации.
    -   Используется `packaging.version.Version` для работы с версиями.
    -   Присутствует загрузка основных параметров проекта.
-   Минусы
    -   Много пустых docstring.
    -   Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов.
    -   Не используется `from src.logger.logger import logger` для логирования ошибок.
    -   Не все переменные и функции имеют подробные docstring.
    -   Избыточное использование `try-except` вместо использования логгера.

**Рекомендации по улучшению**

1.  **Использовать RST docstring:** Заменить все docstring на reStructuredText (RST) формат.
2.  **Использовать `j_loads`:** Заменить `json.load` на `j_loads` из `src.utils.jjson` для чтения файлов.
3.  **Использовать логгер:** Добавить `from src.logger.logger import logger` и использовать его для логирования ошибок вместо `try-except`.
4.  **Улучшить docstring:** Добавить подробные описания для всех функций, переменных и констант.
5.  **Удалить лишние комментарии**: Убрать все комментарии `"""\n\t:platform: Windows, Unix\n\t:synopsis:\n\n"""` и тп.
6.  **Исправить опечатки**: Исправить `copyrihgnt` на `copyright`.
7.  **Удалить комментарий** `""" module: src.endpoints.hypo69.psychologist_bot """`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения основных настроек и параметров проекта.
==============================================================

Этот модуль предназначен для автоматического определения корневой директории проекта,
загрузки настроек из файла `settings.json` и документации из `README.MD`.
Он также устанавливает основные глобальные переменные проекта, такие как имя, версия,
авторские права и т.д.

Пример использования
--------------------

Пример инициализации:

.. code-block:: python

    from src.endpoints.hypo69.psychologist_bot import header

    print(header.__project_name__)
    print(header.__version__)
    print(header.__doc__)
"""


import sys
import json
from packaging.version import Version
from pathlib import Path
from src.utils.jjson import j_loads
from src.logger.logger import logger


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определение корневой директории проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла,
    проверяя наличие файлов-маркеров (например, `pyproject.toml`, `requirements.txt`, `.git`)
    в родительских директориях.

    :param marker_files: Кортеж с именами файлов, по наличию которых определяется корень проекта.
    :type marker_files: tuple
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


# Get the root directory of the project
__root__ = set_project_root()
"""
Path: Путь к корневой директории проекта.
"""

from src import gs

settings: dict = None
try:
    #  загрузка настроек проекта из файла settings.json с помощью j_loads
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
         settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    #  логирование ошибки, если не удалось загрузить настройки
    logger.error('Не удалось загрузить настройки из settings.json', exc_info=e)
    ...
doc_str: str = None
try:
    #  загрузка документации проекта из файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    #  логирование ошибки, если не удалось загрузить документацию
    logger.error('Не удалось загрузить документацию из README.MD', exc_info=e)
    ...

__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Имя проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта."""
__details__: str = ''
"""str: Дополнительные сведения о проекте."""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyright", '') if settings else ''
"""str: Авторские права проекта."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение для поддержки разработчика."""
```