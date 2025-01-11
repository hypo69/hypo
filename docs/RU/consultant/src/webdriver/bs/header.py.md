# Анализ кода модуля `header.py`

**Качество кода**
7
- Плюсы
    -  Код выполняет свою основную задачу: определение корневой директории проекта, загрузка настроек из `settings.json` и документации из `README.MD`, а также определение основных переменных проекта.
    -  Используется `pathlib` для работы с путями, что является хорошей практикой.
    -  Присутствуют базовые комментарии, описывающие функциональность.
- Минусы
    - Отсутствует docstring в начале модуля.
    -  Не используются `j_loads` или `j_loads_ns` для чтения файлов.
    -  Не хватает подробных комментариев к некоторым блокам кода.
    -  Используется `try-except` с `...` что не дает информации об ошибках
    -  Не все переменные и функции имеют docstring
    -  Не соблюдено требование по использованию одинарных кавычек в коде.
    -  Использование глобальных переменных `settings`, `doc_str` без явной необходимости.

**Рекомендации по улучшению**

1.  Добавить docstring в начало модуля с описанием назначения, структуры и примером использования.
2.  Использовать `j_loads` из `src.utils.jjson` вместо стандартного `json.load` для загрузки `settings.json`.
3.  Добавить подробные docstring для всех функций и переменных модуля, используя RST формат.
4.  Заменить `try-except` блоки с `...` на логирование ошибок с помощью `logger.error` для отслеживания проблем.
5.  Избегать использования `global settings` и `global doc_str` без крайней необходимости. Лучше использовать их как локальные переменные в функциях.
6.  Привести в порядок использование кавычек: использовать одинарные кавычки в коде и двойные только в операциях вывода.
7.  Добавить проверку наличия ключей в словаре `settings` перед их использованием.
8.  Перенести определение переменных в начало файла, после описания модуля.
9.  Улучшить читаемость, разбив код на небольшие блоки и добавив комментарии.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для определения корневой директории проекта и загрузки настроек.
======================================================================

Этот модуль содержит функции и переменные для определения корневой директории проекта,
загрузки настроек из файла `settings.json`, чтения документации из файла `README.MD`,
а также определения основных параметров проекта, таких как имя, версия, автор и т.д.

Пример использования
--------------------

.. code-block:: python

    from src.webdriver.bs.header import __project_name__, __version__, __doc__

    print(f"Project name: {__project_name__}")
    print(f"Version: {__version__}")
    print(f"Documentation: {__doc__}")
"""
import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads
from src.logger.logger import logger # импортируем logger


__project_name__: str = 'hypotez'
"""str: Имя проекта."""
__version__: str = ''
"""str: Версия проекта."""
__doc__: str = ''
"""str: Строка документации проекта."""
__details__: str = ''
"""str: Детали проекта."""
__author__: str = ''
"""str: Автор проекта."""
__copyright__: str = ''
"""str: Авторское право."""
__cofee__: str = "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Строка для пожертвования на кофе."""



def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Определяет корневой каталог проекта, начиная с директории текущего файла.

    Поиск ведется вверх по дереву каталогов до первого каталога, содержащего
    один из файлов-маркеров.

    Args:
        marker_files (tuple, optional): Кортеж имен файлов или каталогов, которые
            идентифицируют корень проекта. По умолчанию ('__root__', '.git').

    Returns:
        Path: Путь к корневому каталогу, если найден, иначе директория, где
            расположен скрипт.

    Example:
        >>> set_project_root()
        ... # doctest: +SKIP
        PosixPath('/path/to/your/project')
    """
    current_path: Path = Path(__file__).resolve().parent
    __root__: Path = current_path # Объявление типа переменной
    # Итерируемся по текущей директории и ее родительским директориям
    for parent in [current_path] + list(current_path.parents):
        # Проверяем, существует ли какой-либо из маркерных файлов в текущей директории
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    # Проверка наличия корневой директории в путях поиска
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__

# Определение корневой директории проекта
__root__: Path = set_project_root()
"""Path: Путь к корневому каталогу проекта."""

from src import gs

# Инициализация переменных для настроек и документации
settings: dict | None = None
doc_str: str | None = None

# Попытка загрузить настройки из файла settings.json
try:
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, Exception) as ex:
    logger.error('Не удалось загрузить файл settings.json', exc_info=ex)
# Попытка прочитать документацию из файла README.MD
try:
    with open(gs.path.root / 'src' /  'README.MD', 'r') as doc_file:
        doc_str = doc_file.read()
except (FileNotFoundError, Exception) as ex:
    logger.error('Не удалось прочитать файл README.MD', exc_info=ex)
# Обновление глобальных переменных проекта, если настройки были загружены успешно
if settings:
    __project_name__ = settings.get('project_name', 'hypotez')
    __version__ = settings.get('version', '')
    __author__ = settings.get('author', '')
    __copyright__ = settings.get('copyrihgnt', '')
    __cofee__ = settings.get('cofee', "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")

if doc_str:
   __doc__ = doc_str
```