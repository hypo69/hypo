# Анализ кода модуля `header.py`

**Качество кода**
9
-  Плюсы
    - Код содержит docstring для модуля и функции `set_project_root`.
    - Используется `pathlib` для работы с путями, что делает код более кроссплатформенным.
    - Наличие обработки исключений при загрузке `settings.json` и `README.MD`.
    - Установка `sys.path` для упрощения импорта модулей.
-  Минусы
    - Не используются `j_loads` и `j_loads_ns` для чтения файлов, а используется стандартный `json.load`.
    - Отсутствует обработка ошибок с помощью `logger.error` при загрузке файлов.
    - Не все переменные имеют docstring.
    - Есть использование `...` в блоках `except`.
    - Использование двойных кавычек в строках (например, `settings.get("project_name", ...)`).

**Рекомендации по улучшению**
1.  Использовать `j_loads` из `src.utils.jjson` вместо `json.load`.
2.  Добавить обработку ошибок с помощью `logger.error` при загрузке файлов.
3.  Заменить `...` в блоках `except` на логирование ошибки с помощью `logger.error` и продолжить выполнение (или вернуть `None`).
4.  Добавить docstring для переменных модуля.
5.  Использовать одинарные кавычки для строк в коде.
6.  Импортировать `logger` из `src.logger.logger`.
7.  Изменить название `settings_file` на более подходящее, например `file`.

**Оптимизированный код**
```python
"""
Модуль для определения базовых параметров проекта и настройки окружения.
=========================================================================================

Этот модуль определяет корневую директорию проекта, загружает настройки из `settings.json` и
документацию из `README.MD`, а также устанавливает основные параметры проекта.

Пример использования
--------------------

Пример использования:

.. code-block:: python

    from src.webdriver.firefox.header import __project_name__, __version__
    print(__project_name__)
    print(__version__)

"""
import sys
from pathlib import Path
from src.utils.jjson import j_loads # импортируем j_loads
from src.logger.logger import logger # импортируем logger
from packaging.version import Version


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Находит корневой каталог проекта, начиная с каталога текущего файла,
    идя вверх и останавливаясь на первом каталоге, содержащем любой из маркерных файлов.

    Args:
        marker_files (tuple): Имена файлов или каталогов, идентифицирующие корень проекта.

    Returns:
        Path: Путь к корневому каталогу, если найден, иначе каталог, где находится скрипт.
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
__root__: Path = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""

from src import gs

settings: dict = None
try:
    # используем j_loads вместо json.load и меняем имя переменной
    with open(gs.path.root / 'src' / 'settings.json', 'r') as file:
        settings = j_loads(file)
except (FileNotFoundError, json.JSONDecodeError) as ex:
    # логируем ошибку
    logger.error('Ошибка при загрузке settings.json', exc_info=ex)
    settings = {}


doc_str: str = None
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as file:
        doc_str = file.read()
except (FileNotFoundError, json.JSONDecodeError) as ex:
    # логируем ошибку
    logger.error('Ошибка при загрузке README.MD', exc_info=ex)
    doc_str = ''


__project_name__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Имя проекта"""
__version__: str = settings.get('version', '') if settings else ''
"""__version__ (str): Версия проекта"""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Документация проекта из README.MD"""
__details__: str = ''
"""__details__ (str): Детали проекта"""
__author__: str = settings.get('author', '') if settings else ''
"""__author__ (str): Автор проекта"""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""__copyright__ (str): Авторские права проекта"""
__cofee__: str = settings.get('cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69') if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
"""__cofee__ (str): Сообщение о поддержке разработчика"""
```