# Анализ кода модуля `header.py`

**Качество кода**
6
- Плюсы
    - Код выполняет поиск корневой директории проекта.
    - Есть обработка ошибок при загрузке настроек и документации.
    - Используются константы для определения имени проекта, версии и т.д.
- Минусы
    -  Присутствуют лишние комментарии в начале файла.
    -  Не используется `j_loads` или `j_loads_ns` для чтения файлов.
    - Отсутствуют docstring для модуля и функций.
    - Исключения обрабатываются через `try-except`, а не через `logger.error`.
    - Не все переменные и константы описаны в docstring.
    -  Отсутствует импорт `logger` для обработки ошибок.

**Рекомендации по улучшению**

1.  Удалить лишние комментарии в начале файла.
2.  Использовать `j_loads` для чтения `settings.json` вместо `json.load`.
3.  Добавить docstring для модуля, функции `set_project_root`, и переменных.
4.  Использовать `logger.error` для логирования ошибок вместо стандартного `try-except` (сделать импорт `from src.logger.logger import logger`).
5.  Добавить проверку наличия ключей в `settings`, чтобы избежать `KeyError`.
6.  Форматировать все комментарии в стиле reStructuredText (RST).

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения заголовков и метаданных проекта.
======================================================

Этот модуль определяет корневую директорию проекта, загружает настройки из `settings.json`
и устанавливает глобальные переменные, такие как имя проекта, версия, автор и т. д.

Пример использования
--------------------

.. code-block:: python

    from src.translators.header import __project_name__, __version__, __author__

    print(f"Имя проекта: {__project_name__}")
    print(f"Версия: {__version__}")
    print(f"Автор: {__author__}")
"""

"""str: Режим работы (dev, prod и т.д.)."""

import sys
from pathlib import Path
#  импортируем j_loads  для загрузки json
from src.utils.jjson import j_loads
# импортируем logger для логирования
from src.logger.logger import logger
from packaging.version import Version


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла,
    поднимаясь вверх по дереву директорий, пока не найдет один из файлов-маркеров.

    :param marker_files: Список имен файлов или директорий, которые обозначают корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
    :rtype: Path
    """
    __root__: Path
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        # проверяем есть ли маркер в текущей директории
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    #  проверяем есть ли путь к корню проекта в sys.path и добавляем если нет
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Get the root directory of the project
__root__ = set_project_root()
"""Path: Путь к корневой директории проекта."""

from src import gs

settings: dict = None
try:
    #  загружаем настройки из файла settings.json, используем j_loads вместо json.load
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as ex:
    #  логируем ошибку если не удается загрузить настройки
    logger.error(f"Не удалось загрузить файл настроек {gs.path.root / 'src' / 'settings.json'}", exc_info=ex)
    ...

doc_str: str = None
try:
    # загружаем README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as ex:
    #  логируем ошибку если не удается загрузить README.MD
    logger.error(f"Не удалось загрузить файл документации {gs.path.root / 'src' / 'README.MD'}", exc_info=ex)
    ...


__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Название проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта из файла README.MD."""
__details__: str = ''
"""str: Дополнительные детали проекта."""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Информация об авторских правах."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение о поддержке разработчика."""
```