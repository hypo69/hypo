# Анализ кода модуля `header.py`

**Качество кода**
8
- Плюсы
    - Код содержит docstring для модуля и функции `set_project_root`, что соответствует стандартам.
    - Используется `pathlib.Path` для работы с путями, что улучшает читаемость и переносимость кода.
    - Есть обработка исключений при чтении файлов настроек и документации, что предотвращает сбои в случае отсутствия этих файлов.
    - Код структурирован и относительно понятен.
- Минусы
    - Отсутствует импорт `logger`.
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Комментарии после `#` не всегда объясняют следующую строку кода.
    - Не все переменные имеют docstring.
    - `try-except` блоки с `...` в обработке ошибок могут быть улучшены с помощью `logger.error`.

**Рекомендации по улучшению**

1.  Добавить импорт `logger` из `src.logger.logger`.
2.  Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
3.  Добавить docstring к переменным модуля.
4.  Улучшить обработку ошибок, используя `logger.error` вместо `try-except` с `...`.
5.  Расширить комментарии, чтобы они объясняли логику кода.
6.  Унифицировать использование кавычек: использовать одинарные кавычки для строк в коде и двойные для вывода.
7.  Добавить документацию RST для всех функций и переменных.
8.  Убрать `#! venv/bin/python/python3.12`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для установки корневого каталога проекта и загрузки настроек.
====================================================================

Этот модуль определяет корневой каталог проекта, загружает настройки из файла `settings.json`
и документацию из `README.MD`, а также устанавливает основные переменные проекта,
такие как имя, версия, автор и т.д.

Пример использования
--------------------
    
    .. code-block:: python

        from src.suppliers.chat_gpt.header import __project_name__, __version__, __doc__
        print(__project_name__, __version__, __doc__)
"""

import sys
from pathlib import Path
from src.utils.jjson import j_loads
from src.logger.logger import logger  # Импортируем logger
from packaging.version import Version
from typing import Tuple


def set_project_root(marker_files: Tuple[str, ...] = ('__root__', '.git')) -> Path:
    """
    Находит корневой каталог проекта, начиная с каталога текущего файла,
    поиска вверх и остановки в первом каталоге, содержащем любой из маркерных файлов.

    :param marker_files: Кортеж имен файлов или каталогов для определения корня проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу, если найден, в противном случае - каталог, где находится скрипт.
    :rtype: pathlib.Path

    :Example:
        >>> set_project_root(marker_files=('__root__', '.git'))
        PosixPath('/home/user/project')
    """
    __root__: Path
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    # Итерируемся по текущему каталогу и его родительским каталогам
    for parent in [current_path] + list(current_path.parents):
        # Проверяем, существует ли какой-либо из маркерных файлов/директорий в текущем родительском каталоге
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    # Если корневой каталог не в системном пути, добавляем его
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Получаем корневой каталог проекта
__root__: Path = set_project_root()
"""Path: Путь к корневому каталогу проекта."""

from src import gs

settings: dict = None
# Читаем настройки из файла settings.json
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)  # используем j_loads
except (FileNotFoundError, json.JSONDecodeError) as ex:
    logger.error(f'Ошибка при чтении файла настроек: {ex}')  # Логируем ошибку

doc_str: str = None
# Читаем документацию из файла README.MD
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as ex:
     logger.error(f'Ошибка при чтении файла документации: {ex}') # Логируем ошибку

__project_name__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""str: Имя проекта."""
__version__: str = settings.get('version', '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта."""
__details__: str = ''
"""str: Детали проекта."""
__author__: str = settings.get('author', '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""str: Авторские права проекта."""
__cofee__: str = settings.get('cofee', "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение с призывом угостить разработчика кофе."""

```