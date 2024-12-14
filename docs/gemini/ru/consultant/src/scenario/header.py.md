# Анализ кода модуля `header.py`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован, функции имеют понятные имена.
    - Используется `pathlib` для работы с путями, что делает код более читаемым.
    - Присутствует обработка исключений при чтении файлов настроек.
    - Определены основные константы проекта.
    - Использование `reStructuredText` в docstring для функции `set_project_root`
- Минусы
    - Используется стандартный `json.load` для чтения файла, а не `j_loads`.
    - Отсутствует логирование ошибок.
    - Не все переменные документированы в формате `RST`.
    - Блок `try-except` используется в виде `...` вместо обработки ошибок.
    - Комментарии после `#` не соответствуют стандарту RST

**Рекомендации по улучшению**

1.  Использовать `j_loads` вместо `json.load` для загрузки JSON файлов.
2.  Добавить логирование ошибок с помощью `src.logger.logger`.
3.  Заменить `...` в блоках `try-except` на логирование ошибок и, возможно, дальнейшую обработку.
4.  Документировать все переменные и константы с использованием RST.
5.  Убрать лишние `#!` комментарии.
6.  Преобразовать все комментарии в формат RST.
7.  Добавить docstring для модуля.
8.  Исправить опечатку `copyrihgnt` на `copyright`
9.  Добавить импорт `logger` из `src.logger.logger`
10. Использовать `Path.cwd()` для старта поиска корневой директории
11. Добавить RST docstring для переменных.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для определения основных параметров проекта.
====================================================

Этот модуль определяет корневую директорию проекта, загружает настройки из файла `settings.json`,
а также устанавливает основные константы проекта, такие как имя, версию, документацию и информацию об авторе.

Пример использования
--------------------
.. code-block:: python

    from src.scenario import header

    print(header.__project_name__)
    print(header.__version__)
    print(header.__doc__)
"""

import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads
from src.logger.logger import logger


MODE = 'dev'
"""Режим работы приложения."""


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Поиск производится от текущей директории файла вверх до первого каталога, содержащего один из маркеров.

    :param marker_files: Кортеж имен файлов или каталогов, используемых для идентификации корня проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта, если найдена, иначе путь к директории, где расположен скрипт.
    :rtype: Path
    """
    __root__: Path
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [Path.cwd()] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Вызов функции для определения корневой директории проекта
__root__ = set_project_root()
"""Путь к корневой директории проекта."""

from src import gs

settings: dict = None
"""Словарь с настройками проекта."""
try:
    #  код выполняет загрузку настроек из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, Exception) as ex:
    #  в случае ошибки код логирует ошибку
    logger.error(f'Ошибка чтения файла settings.json: {ex}')


doc_str: str = None
"""Строка документации из файла README.MD"""
try:
    #  код выполняет чтение документации из файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, Exception) as ex:
    # в случае ошибки код логирует ошибку
    logger.error(f'Ошибка чтения файла README.MD: {ex}')

__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""Имя проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""Документация проекта."""
__details__: str = ''
"""Детали проекта."""
__author__: str = settings.get("author", '') if settings else ''
"""Автор проекта."""
__copyright__: str = settings.get("copyright", '') if settings else ''
"""Информация об авторских правах."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""Сообщение о поддержке разработчика."""
```