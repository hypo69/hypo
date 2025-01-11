# Анализ кода модуля `header.py`

**Качество кода**
9
-  Плюсы
    -   Код содержит функцию для определения корневой директории проекта.
    -   Использует `pathlib` для работы с путями.
    -   Сохраняет существующие комментарии.
    -   Использует `try-except` блоки для обработки ошибок при чтении файлов.
    -   Документированы некоторые части кода.
-  Минусы
    -   Не все функции и переменные документированы в формате RST.
    -   Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    -   Отсутствует импорт `logger` из `src.logger`.
    -   Некоторые переменные объявлены с типом `:str` после присваивания значения.
    -   Используется много  `...` в блоках `try-except`, что затрудняет отладку.
    -   Не стандартизированы отступы в  блоках документации и коде.

**Рекомендации по улучшению**
1.  Использовать `j_loads` из `src.utils.jjson` вместо `json.load`.
2.  Импортировать `logger` из `src.logger.logger`.
3.  Добавить документацию в формате RST для всех функций и переменных, включая описание модуля.
4.  Удалить `...`  в блоках `try-except`  и добавить `logger.error` для обработки исключений.
5.  Стандартизировать отступы в блоках документации.
6.  Удалить  `#! venv/bin/python/python3.12` как не нужную строку
7.  Оформить переменные, полученные из `settings`, с указанием типа через аннотацию типа, а не в виде комментария.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с заголовками проекта.
=========================================================================================

Этот модуль содержит функции и переменные для получения и хранения информации о проекте,
такой как имя, версия, описание, авторские права и т.д.
Модуль автоматически определяет корневой каталог проекта и загружает настройки из файла settings.json.

Пример использования
--------------------

Пример получения информации о проекте:

.. code-block:: python

    from src.endpoints.advertisement.header import __project_name__, __version__, __doc__, __author__

    print(f"Project Name: {__project_name__}")
    print(f"Version: {__version__}")
    print(f"Description: {__doc__}")
    print(f"Author: {__author__}")
"""

import sys
from pathlib import Path
from typing import Tuple
from src.utils.jjson import j_loads
from src.logger.logger import logger


def set_project_root(marker_files: Tuple[str, ...] = ('__root__', '.git')) -> Path:
    """
    Определение корневой директории проекта.

    Функция находит корневую директорию проекта, начиная с директории текущего файла,
    и двигаясь вверх до тех пор, пока не найдет директорию, содержащую любой из указанных
    файлов-маркеров.

    :param marker_files: Названия файлов или директорий, которые являются маркерами корневой директории проекта.
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
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта."""

from src import gs

settings: dict | None = None
try:
    # Код исполняет чтение файла настроек
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as ex:
    # Обработка ошибок при чтении файла настроек
    logger.error('Ошибка при чтении файла settings.json', ex)

doc_str: str | None = None
try:
    # Код исполняет чтение файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as ex:
    # Обработка ошибок при чтении файла README.MD
    logger.error('Ошибка при чтении файла README.MD', ex)

__project_name__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Имя проекта."""
__version__: str = settings.get('version', '') if settings else ''
"""__version__ (str): Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Описание проекта."""
__details__: str = ''
"""__details__ (str): Детали проекта."""
__author__: str = settings.get('author', '') if settings else ''
"""__author__ (str): Автор проекта."""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""__copyright__ (str): Авторские права проекта."""
__cofee__: str = settings.get(
    'cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
) if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
"""__cofee__ (str): Сообщение о возможности поддержки разработчика."""
```