# Анализ кода модуля `header.py`

**Качество кода**
6
- Плюсы
    - Присутствует функция `set_project_root` для определения корневой директории проекта.
    - Используется `pathlib.Path` для работы с путями, что является хорошей практикой.
    - Есть базовая обработка исключений при чтении файлов настроек и README.
    - Определены основные метаданные проекта (имя, версия, автор и т.д.)
- Минусы
    - Отсутствует описание модуля в формате docstring.
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    - Нет импорта `logger` из `src.logger`.
    - Не все переменные имеют docstring.
    - `try-except` блоки с `...` являются плохой практикой.
    -  Смешанное использование одинарных и двойных кавычек.
    - Не используются константы для ключей настроек.
    - Не везде есть rst документация.

**Рекомендации по улучшению**

1.  Добавить описание модуля в начале файла в формате docstring.
2.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо `json.load` для загрузки JSON.
3.  Импортировать `logger` из `src.logger.logger`.
4.  Добавить docstring к переменным `__root__`, `settings`, `doc_str`, `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`.
5.  Заменить `...` в `try-except` блоках на логирование ошибок с помощью `logger.error`.
6.  Привести кавычки к одному стандарту - одинарные, кроме случаев вывода (например `print()`).
7.  Создать константы для ключей `project_name`, `version`, `author`, `copyrihgnt`, `cofee`.
8.  Добавить rst документацию к функции `set_project_root`
9. Изменить импорт модуля `gs` на `from src import gs`
10. Всегда писать в конце кода return

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для определения метаданных проекта и корневой директории.
=================================================================

Этот модуль определяет корневую директорию проекта, загружает настройки из `settings.json`,
а также считывает документацию из `README.MD`. Метаданные проекта, такие как имя, версия, автор,
и прочее, сохраняются в глобальные переменные.

Пример использования
--------------------

.. code-block:: python

    from src.goog.spreadsheet.header import __project_name__, __version__, __doc__
    print(f"Project Name: {__project_name__}")
    print(f"Version: {__version__}")
    print(f"Documentation: {__doc__}")
"""

import sys
# изменено: импортируем j_loads_ns из src.utils.jjson
from src.utils.jjson import j_loads_ns
from pathlib import Path
# изменено: импортируем logger из src.logger.logger
from src.logger.logger import logger
from packaging.version import Version


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Определение корневой директории проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла
    и двигаясь вверх по дереву каталогов. Поиск останавливается на первом каталоге,
    содержащем один из файлов-маркеров.

    Args:
        marker_files (tuple): Кортеж имен файлов или каталогов для идентификации корня проекта.

    Returns:
        Path: Путь к корневой директории, если она найдена, иначе - путь к директории, где расположен скрипт.
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

# изменено: импортируем gs из src
from src import gs


settings: dict = None
SETTINGS_FILE = 'settings.json'
README_FILE = 'README.MD'
PROJECT_NAME_KEY = 'project_name'
VERSION_KEY = 'version'
AUTHOR_KEY = 'author'
COPYRIGHT_KEY = 'copyrihgnt'
COFEE_KEY = 'cofee'
try:
    # изменено: используем j_loads_ns для загрузки json
    with open(gs.path.root / 'src' / SETTINGS_FILE, 'r') as settings_file:
        settings = j_loads_ns(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as ex:
    # изменено: логируем ошибку и возвращаем None
    logger.error(f'Ошибка при чтении файла настроек {SETTINGS_FILE}', exc_info=ex)
    settings = None


doc_str: str = None
try:
    with open(gs.path.root / 'src' / README_FILE, 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as ex:
    # изменено: логируем ошибку и возвращаем None
    logger.error(f'Ошибка при чтении файла документации {README_FILE}', exc_info=ex)
    doc_str = None


__project_name__: str = settings.get(PROJECT_NAME_KEY, 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Имя проекта."""
__version__: str = settings.get(VERSION_KEY, '') if settings else ''
"""__version__ (str): Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Строка документации проекта."""
__details__: str = ''
"""__details__ (str): Детали проекта."""
__author__: str = settings.get(AUTHOR_KEY, '') if settings else ''
"""__author__ (str): Автор проекта."""
__copyright__: str = settings.get(COPYRIGHT_KEY, '') if settings else ''
"""__copyright__ (str): Информация об авторских правах."""
__cofee__: str = settings.get(COFEE_KEY, 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69') if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
"""__cofee__ (str): Сообщение о возможности поддержать разработчика."""
return True
```