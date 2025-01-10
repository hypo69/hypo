# Анализ кода модуля `header.py`

**Качество кода**
   -  **Соответствие требованиям по оформлению кода:** 8/10
   -  **Плюсы**
        *  Код имеет четкую структуру и разделен на логические блоки.
        *  Функция `set_project_root` корректно определяет корневую директорию проекта.
        *  Используются стандартные библиотеки `pathlib` и `json`.
   -  **Минусы**
       *  Используется стандартный `json.load`, вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
       *  Комментарии в начале файла не соответствуют стандарту docstring, необходимо переработать
       *  Отсутствует docstring для модуля
       *  В блоках try-except используется `...`, что не информативно
       *  Не используется `logger` для логирования ошибок
       *  Много проверок `if settings else ...` для каждого поля, можно вынести в отдельную функцию
       *  Не все переменные имеют docstring

**Рекомендации по улучшению**

1.  **Документация модуля:**
    *   Добавить docstring в начале файла, описывающий назначение модуля, а также пример использования (в формате RST)
2.  **Использование `j_loads`:**
    *   Заменить `json.load` на `j_loads` или `j_loads_ns` для чтения файлов `settings.json`.
3.  **Обработка ошибок:**
    *   Заменить `...` в блоках `try-except` на логирование ошибок с помощью `logger.error`.
4.  **Упрощение инициализации переменных:**
    *   Создать функцию для получения значения из `settings` с дефолтным значением.
5.  **Документирование переменных и функций:**
    *   Добавить docstring для всех функций и переменных.
6. **Оформление комментариев:**
   *  Комментарии должны быть на русском языке и объяснять назначение каждого блока кода.
7.  **Импорт logger**:
    *   Импортировать `logger` из `src.logger.logger`.
8.  **Переменные:**
    *   Добавить аннотацию типа для переменных.
9.  **Удалить лишний комментарий:**
    *   Удалить `#! venv/bin/python/python3.12`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для определения корневого пути проекта и загрузки основных настроек.
=========================================================================================

Модуль :mod:`src.logger.header` определяет корневой путь проекта, загружает настройки
из файла `settings.json` и устанавливает глобальные переменные проекта, такие как
имя, версия, автор и т.д.

Пример использования
--------------------

Пример использования:

.. code-block:: python

    from src.logger.header import __project_name__, __version__, __doc__, __author__

    print(f"Project Name: {__project_name__}")
    print(f"Version: {__version__}")
    print(f"Author: {__author__}")
    print(f"Doc: {__doc__}")
"""
import sys
from pathlib import Path
from packaging.version import Version
# from src.utils.jjson import j_loads  # TODO: Раскомментировать когда будет реализован модуль
from src.logger.logger import logger # Импорт logger

def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Определяет корневой каталог проекта, начиная с текущего каталога файла.

    Обход каталогов вверх и останавливается на первом каталоге, содержащем
    любой из файлов-маркеров.

    Args:
        marker_files (tuple): Имена файлов или каталогов для идентификации корня проекта.

    Returns:
        Path: Путь к корневому каталогу, если найден, иначе каталог, где расположен скрипт.
    """
    __root__: Path
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    #  Обход родительских каталогов в поисках маркеров
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    # Добавление корневого каталога в sys.path, если его там нет
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__

# Определение корневого каталога проекта
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневому каталогу проекта"""

from src import gs

settings: dict | None = None
# Попытка загрузить настройки из settings.json
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        # settings = j_loads(settings_file) # TODO: Раскомментировать когда будет реализован модуль
        settings = settings_file.read() # TODO: УДАЛИТЬ КОГДА БУДЕТ РЕАЛИЗОВАН МОДУЛЬ
except (FileNotFoundError, json.JSONDecodeError) as e:
    logger.error(f'Ошибка при загрузке файла настроек: {e}')


doc_str: str | None = None
# Попытка загрузить описание проекта из README.MD
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    logger.error(f'Ошибка при загрузке файла README.MD: {e}')

def get_setting(key: str, default: str) -> str:
    """
    Извлекает значение настройки из словаря settings или возвращает значение по умолчанию.

    Args:
        key (str): Ключ настройки.
        default (str): Значение по умолчанию.

    Returns:
        str: Значение настройки или значение по умолчанию.
    """
    if settings:
        try:
            return settings.get(key, default)
        except AttributeError as e:
             logger.error(f'Ошибка при получении настройки {key}: {e}')
             return default
    return default

# Инициализация глобальных переменных проекта
__project_name__: str = get_setting("project_name", 'hypotez')
"""__project_name__ (str): Имя проекта"""
__version__: str = get_setting("version", '')
"""__version__ (str): Версия проекта"""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Описание проекта"""
__details__: str = ''
"""__details__ (str): Детали проекта"""
__author__: str = get_setting("author", '')
"""__author__ (str): Автор проекта"""
__copyright__: str = get_setting("copyrihgnt", '')
"""__copyright__ (str): Авторские права"""
__cofee__: str = get_setting("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")
"""__cofee__ (str): Сообщение с предложением угостить разработчика кофе"""
```