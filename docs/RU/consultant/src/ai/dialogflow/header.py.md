# Анализ кода модуля `header.py`

**Качество кода**
7
- Плюсы
    - Код выполняет свою задачу по определению корневой директории проекта и загрузке настроек.
    - Имеется базовая документация для функций.
    - Используется `pathlib` для работы с путями, что улучшает читаемость и кроссплатформенность.
    - Используются константы для путей, что облегчает поддержку кода.
- Минусы
    - Отсутствует обработка ошибок с использованием `logger.error` вместо `try-except` с `...`.
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Отсутствуют проверки на существование `settings` перед использованием в присвоениях переменных.
    - Не хватает подробной документации в формате RST для модуля, функций и переменных.
    - Желательно использовать `str(Path)` для преобразования путей к строкам, чтобы избежать неявного преобразования.
    - Не хватает подробных комментариев.

**Рекомендации по улучшению**
1.  Использовать `j_loads` из `src.utils.jjson` для загрузки JSON файлов.
2.  Заменить `try-except` с `...` на обработку ошибок с помощью `logger.error`.
3.  Добавить docstring в формате RST для модуля.
4.  Добавить docstring в формате RST для функции `set_project_root`
5.  Добавить аннотации типов для переменных.
6.  Добавить проверки на существование `settings` перед использованием в присвоениях переменных
7.  Использовать `str(Path)` для преобразования путей к строкам
8.  Добавить подробные комментарии.
9.  Использовать `from src.logger.logger import logger` для логирования.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для определения корневой директории проекта и загрузки общих настроек.
===========================================================================

Этот модуль предоставляет функциональность для автоматического определения корневой директории проекта,
а также загрузки общих настроек проекта из файлов `settings.json` и `README.MD`.
Он также устанавливает различные глобальные переменные на основе загруженных настроек.

Пример использования
--------------------

.. code-block:: python

    from pathlib import Path
    from src.ai.dialogflow.header import __project_name__, __version__, __doc__, __author__

    print(f"Имя проекта: {__project_name__}")
    print(f"Версия: {__version__}")
    print(f"Автор: {__author__}")
    print(f"Документация: {__doc__}")


"""
#! venv/bin/python/python3.12
import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads
from src.logger.logger import logger  # Import logger
from typing import Tuple
def set_project_root(marker_files: Tuple[str, ...] = ('__root__', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла и
    поднимаясь вверх по дереву каталогов. Поиск прекращается при обнаружении первого каталога,
    содержащего любой из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов, используемых для идентификации корневого каталога проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта. Если корневая директория не найдена, возвращает директорию, где расположен скрипт.
    :rtype: Path
    
    :Example:
        >>> from pathlib import Path
        >>> root_dir = set_project_root(marker_files=('__root__', '.git'))
        >>> print(f"Корневая директория: {root_dir}")
        Корневая директория: /путь/к/корневой/директории
    """
    __root__: Path
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    # Проход по текущей директории и ее родительским директориям
    for parent in [current_path] + list(current_path.parents):
        # Проверка наличия любого из файлов-маркеров в текущей родительской директории
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    # Добавление корневой директории в sys.path, если ее там нет
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Get the root directory of the project
__root__: Path = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""

from src import gs
# Инициализация переменной settings
settings: dict = None
# Попытка загрузить настройки из файла settings.json
try:
    with open(str(gs.path.root / 'src' /  'settings.json'), 'r',encoding='utf-8') as settings_file: # Открываем файл настроек
        settings = j_loads(settings_file) # Загрузка данных из JSON файла
except FileNotFoundError:
     logger.error(f"Файл настроек settings.json не найден по пути {str(gs.path.root / 'src' /  'settings.json')}") # Логируем ошибку если файл не найден
except Exception as e:
    logger.error(f"Ошибка при загрузке settings.json: {e}")  # Логируем ошибку декодирования JSON файла
# Инициализация переменной doc_str
doc_str: str = None
# Попытка загрузить документацию из файла README.MD
try:
    with open(str(gs.path.root / 'src' /  'README.MD'), 'r',encoding='utf-8') as doc_file: # Открываем файл документации
        doc_str = doc_file.read() # Читаем данные из файла
except FileNotFoundError:
    logger.error(f"Файл документации README.MD не найден по пути {str(gs.path.root / 'src' /  'README.MD')}") # Логируем ошибку если файл не найден
except Exception as e:
    logger.error(f"Ошибка при чтении README.MD: {e}") # Логируем ошибку чтения файла
# Получение значений из settings или установка значений по умолчанию
__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Название проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""__version__ (str): Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Документация проекта."""
__details__: str = ''
"""__details__ (str): Детали проекта (не определены)."""
__author__: str = settings.get("author", '') if settings else ''
"""__author__ (str): Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""__copyright__ (str): Авторские права проекта."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Сообщение для поддержки разработчика."""
```