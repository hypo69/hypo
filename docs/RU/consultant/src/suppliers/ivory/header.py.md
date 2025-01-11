# Анализ кода модуля `header`

**Качество кода**
1.  Соответствие требованиям по оформлению кода: 7/10
    *   **Плюсы**:
        *   Используются docstring для описания модуля и функции `set_project_root`.
        *   Код структурирован и читаем.
        *   Импорты расположены в начале файла.
    *   **Минусы**:
        *   Не везде используется `j_loads` или `j_loads_ns` для чтения JSON файлов.
        *   Не все переменные и функции имеют docstring.
        *   Обработка исключений `FileNotFoundError` и `json.JSONDecodeError` используется без логирования ошибок.
        *   Используются двойные кавычки в строках, где должны быть одинарные.

**Рекомендации по улучшению**

1.  Заменить `json.load` на `j_loads` из `src.utils.jjson`.
2.  Добавить docstring для всех переменных, включая `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`.
3.  Использовать одинарные кавычки в коде, кроме операций вывода.
4.  Добавить логирование ошибок при обработке исключений.
5.  Добавить более подробное описание модуля.
6.  Использовать `from src.logger.logger import logger` для логирования.
7.  Удалить неиспользуемые импорты, если таковые есть.
8.  Добавить проверку на `settings` прежде чем брать данные из словаря.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

"""
Модуль для инициализации проекта и загрузки настроек.
=====================================================

Этот модуль выполняет следующие задачи:

- Определение корневой директории проекта.
- Загрузка настроек из файла `settings.json`.
- Чтение документации из файла `README.MD`.
- Определение основных параметров проекта, таких как имя, версия, автор и т.д.

Пример использования:
---------------------

.. code-block:: python

    from src.suppliers.ivory.header import __project_name__, __version__

    print(f'Имя проекта: {__project_name__}')
    print(f'Версия проекта: {__version__}')
"""

import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads # Импортируем j_loads
from src.logger.logger import logger # Импортируем logger

def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Определяет корневую директорию проекта, начиная с директории текущего файла.

    Поиск идет вверх по дереву каталогов до первого каталога, содержащего один из файлов-маркеров.

    Args:
        marker_files (tuple): Имена файлов или каталогов, идентифицирующих корень проекта.

    Returns:
        Path: Путь к корневой директории, если она найдена, или директория, где расположен скрипт.
    
    Example:
        >>> set_project_root()
        PosixPath('/Users/user/my_project')
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

# Код исполняет поиск и установку корневой директории проекта
__root__ = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта"""

from src import gs

settings: dict | None = None
# Код выполняет попытку чтения файла настроек
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file) # Используем j_loads
except (FileNotFoundError, json.JSONDecodeError) as e:
    logger.error(f'Ошибка при чтении файла настроек: {e}') # Логируем ошибку
    settings = {}
    
doc_str: str | None = None
# Код выполняет попытку чтения файла документации
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    logger.error(f'Ошибка при чтении файла документации: {e}') # Логируем ошибку
    doc_str = ''

# Проверяем settings перед использованием
__project_name__ = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Имя проекта"""
__version__: str = settings.get('version', '') if settings else ''
"""__version__ (str): Версия проекта"""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Документация проекта"""
__details__: str = ''
"""__details__ (str): Детали проекта"""
__author__: str = settings.get('author', '') if settings else ''
"""__author__ (str): Автор проекта"""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""__copyright__ (str): Авторские права проекта"""
__cofee__: str = settings.get('cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69') if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
"""__cofee__ (str): Сообщение с предложением угостить разработчика кофе"""
```