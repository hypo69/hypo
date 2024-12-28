# Анализ кода модуля `header.py`

**Качество кода**
9
-  Плюсы
    -   Код имеет хорошую структуру и читаемость.
    -   Присутствует определение констант и переменных с использованием настроек из файла `settings.json`.
    -   Используется функция `set_project_root` для определения корневой директории проекта.
    -   Используется try-except блоки для обработки исключений при чтении файлов.
-  Минусы
    -   Используется стандартный `json.load`, нужно заменить на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -   Не используются логирование ошибок, требуется добавить.
    -   Отсутствуют docstring для функций и переменных.
    -   Использование `...` вместо обработки ошибок - не лучшее решение.
    -   Не хватает обработки ошибок при чтении файлов.
    -   Некоторые переменные не имеют аннотаций типов.
    -   Импорты не отсортированы.
    -   Отсутствует использование `logger.error`.
    -   Не все переменные и функции имеют docstring в формате reStructuredText.

**Рекомендации по улучшению**

1.  Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
2.  Добавить логирование ошибок с использованием `from src.logger.logger import logger` и `logger.error()`.
3.  Добавить docstring для всех функций, переменных, включая модуль в формате reStructuredText.
4.  Заменить `...` на более информативное логирование и обработку ошибок.
5.  Добавить аннотации типов для переменных, где это необходимо.
6.  Отсортировать импорты по алфавиту.
7.  Убрать лишние комментарии (например, `#! venv/Scripts/python.exe` и т.д.)
8.  Добавить подробные комментарии к коду.
9.  Удалить неиспользуемую переменную `MODE`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для определения основных настроек проекта.
=========================================================================================

Этот модуль определяет корневую директорию проекта, загружает настройки из `settings.json`,
устанавливает основные переменные, такие как имя проекта, версия, документация, авторские права
и другие параметры.

Пример использования
--------------------

Импорт переменных:

.. code-block:: python

    from src.webdriver.chrome.header import __project_name__, __version__, __doc__, __author__, __copyright__, __cofee__

Использование переменных:

.. code-block:: python

    print(f"Название проекта: {__project_name__}")
    print(f"Версия: {__version__}")
    print(f"Автор: {__author__}")
"""

import sys
from pathlib import Path
from typing import Tuple, Dict, Optional

from packaging.version import Version

from src import gs
from src.utils.jjson import j_loads
from src.logger.logger import logger

def set_project_root(marker_files: Tuple[str, ...] = ('__root__')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла,
    и останавливается на первом каталоге, содержащем любой из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий для идентификации корня проекта.
    :type marker_files: Tuple[str, ...]
    :return: Путь к корневой директории, если она найдена, иначе - директория, где расположен скрипт.
    :rtype: Path
    """
    current_path: Path = Path(__file__).resolve().parent
    __root__: Path = current_path

    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Получение корневой директории проекта
__root__: Path = set_project_root()
""" Path: Путь к корневой директории проекта. """

settings: Optional[Dict] = None
""" Optional[Dict]: Словарь с настройками проекта, загруженный из `settings.json`. Может быть `None`, если файл не найден или не может быть прочитан."""
try:
    #  Код открывает файл settings.json и загружает данные
    with open(gs.path.root / 'src' / 'settings.json', 'r', encoding='utf-8') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as ex:
    # Логирование ошибки если файл settings.json не найден или не может быть прочитан
    logger.error(f'Ошибка загрузки файла настроек: {ex}', exc_info=True)

doc_str: Optional[str] = None
""" Optional[str]: Строка с содержимым файла `README.MD`. Может быть `None`, если файл не найден или не может быть прочитан."""
try:
    # Код открывает файл README.MD и читает данные
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as readme_file:
        doc_str = readme_file.read()
except (FileNotFoundError,  UnicodeDecodeError) as ex:
    # Логирование ошибки если файл README.MD не найден или не может быть прочитан
    logger.error(f'Ошибка загрузки файла документации: {ex}', exc_info=True)



__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Название проекта, по умолчанию 'hypotez'."""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Содержание файла `README.MD`."""
__details__: str = ''
"""str: Детальное описание проекта."""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Авторские права проекта."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение о возможности угостить разработчика кофе."""
```