# Анализ кода модуля `header.py`

**Качество кода**
6/10
- Плюсы
    -  Код выполняет свою основную задачу - находит корень проекта и загружает настройки из файлов.
    -  Используются типы `Path` из `pathlib`, что делает код более читаемым и надежным.
    -  Есть минимальная обработка ошибок при загрузке файлов настроек.
    -  Добавлены описания переменных модуля.
- Минусы
    -  Не соблюдены требования к использованию кавычек.
    -  Отсутствуют импорты `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -  Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    -  Не хватает документации к функциям и модулю в формате RST.
    -  Обработка ошибок недостаточно детализирована (используется `...` вместо логирования).
    -  Не все переменные модуля имеют docstring.
    -  Используется `sys.path.insert(0, str(__root__))`, что не рекомендуется (лучше использовать `sys.path.append`).
    -  Ошибки обрабатываются через `...` вместо логгера.

**Рекомендации по улучшению**
1.  Использовать одинарные кавычки (`'`) в коде, кроме операций вывода.
2.  Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
3.  Добавить документацию к модулю, функциям и переменным в формате RST.
4.  Заменить `...` на логирование с помощью `logger.error`.
5.  Использовать `sys.path.append(str(__root__))` вместо `sys.path.insert(0, str(__root__))`
6.  Добавить проверку на наличие файла `settings.json` и `README.MD`
7.  Убрать дублирование кода.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для определения корневой директории проекта и загрузки настроек.
======================================================================

Этот модуль предназначен для автоматического определения корневой директории проекта,
загрузки настроек из файла `settings.json` и чтения документации из `README.MD`.

Функции:
    - `set_project_root`: Находит корневую директорию проекта.

Переменные:
    - `__root__`: Путь к корневой директории проекта.
    - `settings`: Словарь с настройками проекта из `settings.json`.
    - `doc_str`: Строка с содержимым файла `README.MD`.
    - `__project_name__`: Название проекта.
    - `__version__`: Версия проекта.
    - `__doc__`: Документация проекта.
    - `__details__`: Детали проекта (пока не используется).
    - `__author__`: Автор проекта.
    - `__copyright__`: Информация об авторских правах.
    - `__cofee__`: Призыв к поддержке разработчика.

Пример использования:
--------------------

.. code-block:: python

    from src.webdriver.header import __project_name__, __version__, __doc__
    print(f"Project Name: {__project_name__}")
    print(f"Version: {__version__}")
    print(f"Documentation: {__doc__}")
"""

import sys
from pathlib import Path
from src.utils.jjson import j_loads # исправлено импорт j_loads
from src.logger.logger import logger # исправлено импорт logger
from packaging.version import Version


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с директории текущего файла.

    Поиск ведется вверх по директориям, останавливаясь на первой директории,
    содержащей любой из файлов-маркеров.

    Args:
        marker_files (tuple): Кортеж имен файлов или директорий для идентификации корня проекта.

    Returns:
        Path: Путь к корневой директории, если она найдена. Иначе - директория, где расположен скрипт.
    
    Example:
        >>> set_project_root()
        PosixPath('/path/to/project')
    """
    __root__: Path
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if str(__root__) not in sys.path:
         sys.path.append(str(__root__)) # исправлено на sys.path.append
    return __root__


# Получение корневой директории проекта
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта"""

from src import gs

settings: dict = None
try:
    settings_path = gs.path.root / 'src' / 'settings.json'
    if settings_path.exists(): # Добавлена проверка на существование файла
        with open(settings_path, 'r') as settings_file:
            settings = j_loads(settings_file) # исправлено на j_loads
    else:
         logger.error(f"Файл настроек не найден: {settings_path}")
except Exception as ex: # изменено на обработку всех ошибок
    logger.error(f'Ошибка при загрузке файла настроек: {settings_path}', exc_info=ex)
    

doc_str: str = None
try:
    doc_path = gs.path.root / 'src' / 'README.MD'
    if doc_path.exists(): # Добавлена проверка на существование файла
         with open(doc_path, 'r') as doc_file:
            doc_str = doc_file.read()
    else:
        logger.error(f"Файл документации не найден: {doc_path}")
except Exception as ex:  # изменено на обработку всех ошибок
     logger.error(f'Ошибка при загрузке файла документации: {doc_path}', exc_info=ex)

__project_name__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Название проекта."""
__version__: str = settings.get('version', '') if settings else ''
"""__version__ (str): Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Строка с содержимым файла `README.MD`."""
__details__: str = ''
"""__details__ (str): Детали проекта."""
__author__: str = settings.get('author', '') if settings else ''
"""__author__ (str): Автор проекта."""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""__copyright__ (str): Информация об авторских правах."""
__cofee__: str = settings.get('cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69') if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
"""__cofee__ (str): Сообщение с просьбой поддержать разработчика."""
```