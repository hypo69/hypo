# Анализ кода модуля `header.py`

**Качество кода**
7
-  Плюсы
    - Код имеет docstring для модуля и функции `set_project_root`.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Код выполняет поиск корневой директории проекта.
    - Используются константы для настроек, что улучшает читаемость и сопровождаемость.
-  Минусы
    - Не все функции и переменные имеют docstring.
    - Используется `json.load` вместо `j_loads` или `j_loads_ns`.
    - Отсутствует импорт `logger` из `src.logger.logger`.
    - Избыточное использование `try-except` блоков с `...` для обработки ошибок.
    - Код для чтения `README.MD` обрабатывается так же как и JSON файл, что является некорректным.
    - Отсутствует проверка на наличие ключей в словаре `settings` перед доступом.

**Рекомендации по улучшению**
1. Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
2. Добавить импорт `from src.logger.logger import logger`.
3. Добавить docstring для всех переменных и констант, которые используются в модуле.
4. Убрать избыточное использование try-except, заменив их на логирование с `logger.error`.
5. Разделить обработку ошибок при чтении `settings.json` и `README.MD`.
6. Проверять наличие ключей в словаре `settings` с помощью метода `get` с дефолтным значением.
7. Ко всем функциям и методам добавить документацию в формате RST.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для инициализации проекта и загрузки настроек.
=====================================================

Этот модуль определяет корневую директорию проекта, загружает настройки из `settings.json`
и читает документацию из `README.MD`.

Пример использования
--------------------

.. code-block:: python

    from src.suppliers.grandadvance.header import __root__, __project_name__, __version__, __doc__
    print(__project_name__)

"""
import sys
from pathlib import Path
from packaging.version import Version

from src.utils.jjson import j_loads # Импорт j_loads для обработки JSON
from src.logger.logger import logger # Импорт logger для логирования

def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Определяет корневую директорию проекта, начиная с директории текущего файла.

    Поиск идет вверх по директориям, пока не будет найдена директория, содержащая
    один из файлов-маркеров.

    :param marker_files: Кортеж с именами файлов или директорий, которые идентифицируют корень проекта.
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


# Определение корневой директории проекта
__root__: Path = set_project_root()
"""Path: Путь к корневой директории проекта."""

from src import gs

settings: dict | None = None
"""dict | None: Словарь с настройками проекта, загруженными из 'settings.json'."""

try:
    # код выполняет чтение настроек из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file.read()) # Используем j_loads для загрузки JSON
except FileNotFoundError as e:
    logger.error(f'Файл settings.json не найден: {e}')
except Exception as e:
    logger.error(f'Ошибка при чтении или парсинге файла settings.json: {e}')
    

doc_str: str | None = None
"""str | None: Строка с содержимым файла 'README.MD'."""
try:
    # код выполняет чтение содержимого файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as doc_file:
        doc_str = doc_file.read()
except FileNotFoundError as e:
    logger.error(f'Файл README.MD не найден: {e}')
except Exception as e:
     logger.error(f'Ошибка при чтении файла README.MD: {e}')

__project_name__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""str: Название проекта."""

__version__: str = settings.get('version', '') if settings else ''
"""str: Версия проекта."""

__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта, полученная из README.MD."""

__details__: str = ''
"""str: Детали проекта."""

__author__: str = settings.get('author', '') if settings else ''
"""str: Автор проекта."""

__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""str: Копирайт проекта."""

__cofee__: str = settings.get('cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69') if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
"""str: Сообщение о поддержке разработчика."""
```