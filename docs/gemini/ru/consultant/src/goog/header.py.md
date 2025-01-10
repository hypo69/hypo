# Анализ кода модуля `header.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и читаем.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Есть документация для функции `set_project_root`.
    - Код обрабатывает исключения при чтении файлов настроек и README.
    -  Определение и инициализация переменных проекта из `settings.json`
 -  Минусы
    -  Отсутствует общая документация модуля.
    - Используется стандартный `json.load` вместо `j_loads` из `src.utils.jjson`.
    - Не все переменные и константы имеют документацию.
    - Исключения обрабатываются через `...`, что скрывает детали ошибок.
    -  Использование `json.JSONDecodeError` не совсем корректно, так как `FileNotFoundError` уже перехватывает ситуацию, когда файл отсутствует.
    -   `logger` не используется для логирования ошибок.
    - Отсутствуют комментарии к блокам кода.

**Рекомендации по улучшению**

1.  Добавить общую документацию модуля.
2.  Заменить `json.load` на `j_loads` из `src.utils.jjson`.
3.  Добавить документацию к глобальным переменным и константам.
4.  Заменить многоточия (`...`) на логирование ошибок с помощью `logger.error`.
5.  Убрать лишнее перехватывание исключения `json.JSONDecodeError`.
6.  Использовать `from src.logger.logger import logger` для логирования.
7.  Добавить комментарии к блокам кода.
8. Привести в соответствие имена переменных и констант с другими файлами проекта
9. Использовать одинарные кавычки для строк в коде, двойные только для вывода на экран.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для определения корневой директории проекта и загрузки настроек.
=========================================================================================

Этот модуль содержит функции и переменные для:
    - Поиска корневой директории проекта.
    - Загрузки настроек из файла 'settings.json'.
    - Загрузки документации из файла 'README.MD'.
    - Определения основных переменных проекта, таких как имя проекта, версия, автор и т.д.

Пример использования
--------------------

Пример использования переменных проекта:

.. code-block:: python

    from src.goog.header import __project_name__, __version__, __author__

    print(f'Имя проекта: {__project_name__}')
    print(f'Версия: {__version__}')
    print(f'Автор: {__author__}')
"""

import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads
from src.logger.logger import logger

def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Находит корневой каталог проекта, начиная с каталога текущего файла,
    поиска вверх и остановки в первом каталоге, содержащем любой из файлов-маркеров.

    Args:
        marker_files (tuple): Имена файлов или каталогов для идентификации корневого каталога проекта.

    Returns:
        Path: Путь к корневому каталогу, если он найден, в противном случае - каталог, где расположен скрипт.
    """
    __root__: Path
    # Определяет абсолютный путь к родительскому каталогу текущего файла
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    # Перебирает текущий каталог и все его родительские каталоги
    for parent in [current_path] + list(current_path.parents):
        # Проверяет, существует ли в текущем каталоге хотя бы один из файлов-маркеров
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    # Если корневой каталог не находится в sys.path, добавляет его
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__

# Получает корневой каталог проекта
__root__ = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта."""

from src import gs

settings: dict = None
# Пытается открыть и загрузить настройки из файла settings.json
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        # Использует j_loads для загрузки JSON данных
        settings = j_loads(settings_file)
except FileNotFoundError as ex:
    # Логирует ошибку, если файл не найден
    logger.error(f'Файл настроек не найден: {ex}')
    ...
except Exception as ex:
    # Логирует любую другую ошибку при загрузке настроек
    logger.error(f'Ошибка при загрузке настроек: {ex}')
    ...

doc_str: str = None
# Пытается открыть и прочитать содержимое файла README.MD
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except FileNotFoundError as ex:
    # Логирует ошибку, если файл не найден
    logger.error(f'Файл README.MD не найден: {ex}')
    ...
except Exception as ex:
     # Логирует любую другую ошибку при чтении README.MD
    logger.error(f'Ошибка при чтении README.MD: {ex}')
    ...

# Инициализирует переменные проекта, используя значения из settings, если они доступны
__project_name__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Имя проекта."""
__version__: str = settings.get('version', '') if settings else ''
"""__version__ (str): Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Документация проекта."""
__details__: str = ''
"""__details__ (str): Детали проекта."""
__author__: str = settings.get('author', '') if settings else ''
"""__author__ (str): Автор проекта."""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""__copyright__ (str): Авторские права проекта."""
__cofee__: str = settings.get('cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69') if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
"""__cofee__ (str): Сообщение для поддержки разработчика."""
```