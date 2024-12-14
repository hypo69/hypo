# Анализ кода модуля `header.py`

**Качество кода**
9
-   Плюсы
    - Код достаточно хорошо структурирован и читаем.
    - Используется функция `set_project_root` для определения корневой директории проекта.
    - Есть базовая обработка ошибок при загрузке файлов `settings.json` и `README.MD`.
    - Использование переменных для хранения информации о проекте.
-   Минусы
    -  Не хватает документации в формате reStructuredText (RST) для модуля, функций и переменных.
    -  Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -  Отсутствует использование `logger` для логирования ошибок.
    -  Избыточное использование `try-except` с `...` вместо обработки ошибок через `logger.error`.
    -  Необходимо добавить импорты, если они нужны, в частности,  `from src.utils.jjson import j_loads`

**Рекомендации по улучшению**

1.  **Документация**: Добавить docstring в формате RST для модуля, функции `set_project_root` и всех глобальных переменных.
2.  **Обработка JSON**: Использовать `j_loads` из `src.utils.jjson` вместо `json.load`.
3.  **Логирование**: Заменить `try-except` на использование `logger.error` для обработки ошибок.
4.  **Импорты**: Добавить `from src.utils.jjson import j_loads` в импорты.
5.  **Убрать лишнее**: убрать `MODE = 'dev'`.
6.  **Использовать f-строки**: Применить f-строки для более читаемого форматирования строк.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения основных настроек и информации о проекте.
=========================================================================================

Этот модуль определяет корневую директорию проекта, загружает настройки из `settings.json`
и документацию из `README.MD`, а также предоставляет доступ к основным параметрам проекта.

Пример использования
--------------------

Пример использования:

.. code-block:: python

    from src.scenario.header import __project_name__, __version__, __doc__

    print(f"Project Name: {__project_name__}")
    print(f"Version: {__version__}")
    print(f"Documentation: {__doc__}")

"""

import sys
from pathlib import Path
from packaging.version import Version

from src.logger.logger import logger #  Добавлен импорт для логирования
from src.utils.jjson import j_loads #  Добавлен импорт для j_loads

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с текущей директории файла,
    поднимаясь вверх по дереву каталогов до тех пор, пока не найдет один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий, используемых для идентификации корня проекта.
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
"""Path: Путь к корневой директории проекта."""

from src import gs

settings: dict = None
try:
    #  используется j_loads вместо json.load
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError,  Exception) as ex: #  обрабатываем ошибку через логер, убираем json.JSONDecodeError
    logger.error(f'Ошибка при загрузке файла настроек: {ex}') #  логер
    ... # сохраняем точку остановки

doc_str: str = None
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError,  Exception) as ex: # обрабатываем ошибку через логер, убираем json.JSONDecodeError
    logger.error(f'Ошибка при чтении файла README.MD: {ex}') # логер
    ... # сохраняем точку остановки


__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Имя проекта, по умолчанию 'hypotez'."""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Строка документации проекта, взятая из README.MD."""
__details__: str = ''
"""str: Дополнительная информация о проекте."""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Информация об авторских правах."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение о поддержке разработчика."""
```