# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    -  Код содержит docstring для модуля и функции `set_project_root`.
    -  Код использует `pathlib.Path` для работы с путями, что делает его более кроссплатформенным.
    -  Используется `packaging.version.Version` для работы с версиями, что является хорошей практикой.
    -  Код обрабатывает исключения `FileNotFoundError` и `json.JSONDecodeError` при чтении файлов настроек и README.
-  Минусы
    -  Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    -  Не все переменные и константы имеют docstring.
    -  Используется избыточное `try-except`, можно заменить на логирование.
    -  Отсутствует логирование ошибок.
    -  Не все импорты отсортированы и структурированы в начале модуля.
    -  Не соблюдено правило одинарных кавычек.
    -  Множественные определения переменных в глобальной области видимости.

**Рекомендации по улучшению**

1.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо `json.load`.
2.  Добавить docstring для всех переменных модуля, включая `MODE`, `__root__`, `settings`, `doc_str`, `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`.
3.  Заменить `try-except` на логирование с использованием `logger.error`.
4.  Использовать `from src.logger.logger import logger` для логирования.
5.  Импортировать `j_loads` из `src.utils.jjson`.
6.  Привести к одному стилю использование кавычек (одинарные).
7.  Вынести константы (например, `\'dev\'`) в отдельный блок и использовать snake_case для именования.
8. Добавить описание модуля в формате RST
9.  Добавить docstring для всех переменных модуля в формате RST
10.  Изменить все вхождения двойных кавычек на одинарные.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для настройки и инициализации проекта.
=========================================================================================

Этот модуль содержит функции и переменные, необходимые для настройки проекта,
определения корневой директории, загрузки настроек и метаданных проекта.

Пример использования
--------------------

.. code-block:: python

    from src.endpoints import header
    print(header.__project_name__)
    print(header.__version__)

"""
import sys
from pathlib import Path
from packaging.version import Version

from src.utils.jjson import j_loads  # импорт j_loads
from src.logger.logger import logger  # импорт логгера

MODE = 'dev'  # Текущий режим работы приложения.
"""str: Текущий режим работы приложения."""

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневой каталог проекта, начиная с каталога текущего файла,
    перемещаясь вверх до первого каталога, содержащего маркерные файлы.

    :param marker_files: кортеж имен файлов или каталогов, идентифицирующих корень проекта.
    :type marker_files: tuple
    :return: путь к корневой директории, если найдена, иначе - путь к каталогу, где расположен скрипт.
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


# Вызов функции для определения корневой директории проекта
__root__: Path = set_project_root()
"""Path: Путь к корневой директории проекта."""


from src import gs

settings: dict = None
"""dict: Словарь настроек проекта."""
try:
    # Чтение файла настроек settings.json с использованием j_loads
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except FileNotFoundError:
    logger.error(f'Файл настроек settings.json не найден: {gs.path.root / "src" / "settings.json"}')
    ...
except Exception as ex:
    logger.error(f'Ошибка чтения файла настроек settings.json: {ex}')
    ...

doc_str: str = None
"""str: Содержимое файла README.MD."""
try:
    # Чтение файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as readme_file:
        doc_str = readme_file.read()
except FileNotFoundError:
    logger.error(f'Файл README.MD не найден: {gs.path.root / "src" / "README.MD"}')
    ...
except Exception as ex:
    logger.error(f'Ошибка чтения файла README.MD: {ex}')
    ...

# Инициализация переменных проекта
__project_name__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""str: Имя проекта."""
__version__: str = settings.get('version', '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта (содержимое README.MD)."""
__details__: str = ''
"""str: Детали проекта."""
__author__: str = settings.get('author', '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""str: Информация о авторских правах проекта."""
__cofee__: str = settings.get('cofee', "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение о поддержке разработчика."""
```