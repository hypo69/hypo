# Анализ кода модуля `header.py`

**Качество кода**
8
- Плюсы
    - Код структурирован и имеет docstring для функции `set_project_root`.
    - Используется `pathlib.Path` для работы с путями.
    - Добавлены проверки на наличие файлов и ошибок при чтении JSON.
    - Выделены переменные `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__` для хранения данных из файла настроек.
- Минусы
    - Отсутствует reStructuredText (RST) документация для модуля.
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Избыточное использование `try-except` блоков с `...` вместо обработки ошибок через `logger.error`.
    - Отсутствует импорт `logger` из `src.logger.logger`.
    - Отсутствует документация для переменных.
    - Код содержит `#! venv/Scripts/python.exe` и `#! venv/bin/python/python3.12` которые не нужны и могут вызвать ошибку в других окружениях
    - Код содержит лишние переменные `MODE = 'dev'` которые не используются

**Рекомендации по улучшению**

1.  Добавить reStructuredText (RST) документацию для модуля.
2.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо `json.load`.
3.  Использовать `logger.error` для обработки ошибок вместо `try-except` с `...`.
4.  Добавить импорт `logger` из `src.logger.logger`.
5.  Добавить документацию для переменных.
6.  Удалить лишние переменные `MODE = 'dev'` и `#! venv/Scripts/python.exe` `#! venv/bin/python/python3.12`.
7.  Соблюдать единый стиль кавычек в коде (`'`).

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для определения и хранения основных настроек проекта.
=================================================================

Этот модуль предназначен для загрузки настроек проекта из файла `settings.json`
и документации из `README.MD`, а также для определения корневой директории проекта.

Модуль устанавливает значения глобальных переменных, таких как:
    - `__project_name__`: имя проекта.
    - `__version__`: версия проекта.
    - `__doc__`: документация проекта из `README.MD`.
    - `__author__`: автор проекта.
    - `__copyright__`: информация об авторских правах.
    - `__cofee__`: сообщение для поддержки разработчика.

Пример использования
--------------------

.. code-block:: python

    from src.webdriver.edge.header import __project_name__, __version__

    print(f"Project name: {__project_name__}")
    print(f"Version: {__version__}")
"""
import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads
from src.logger.logger import logger


def set_project_root(marker_files: tuple = ('__root__')) -> Path:
    """
    Определение корневой директории проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла
    и продвигаясь вверх по иерархии. Поиск останавливается при обнаружении
    первой директории, содержащей один из файлов-маркеров.

    :param marker_files: кортеж имен файлов или директорий, обозначающих корень проекта.
    :type marker_files: tuple
    :return: путь к корневой директории проекта.
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
"""Path: Путь к корневой директории проекта."""

from src import gs

settings: dict = None
try:
    # Код исполняет загрузку настроек из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r', encoding='utf-8') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, Exception) as ex:
    # Логирование ошибки, если файл не найден или произошла ошибка при чтении JSON
    logger.error(f'Ошибка загрузки файла настроек {ex}')
    ...


doc_str: str = None
try:
    # Код исполняет загрузку документации из файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, Exception) as ex:
    # Логирование ошибки, если файл не найден или произошла ошибка при чтении файла
    logger.error(f'Ошибка загрузки файла документации {ex}')
    ...

# Глобальные переменные для хранения данных проекта
__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Имя проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта."""
__details__: str = ''
"""str: Дополнительная информация о проекте."""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Информация об авторских правах."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение для поддержки разработчика."""
```