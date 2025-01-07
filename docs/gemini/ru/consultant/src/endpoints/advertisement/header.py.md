# Анализ кода модуля `header.py`

**Качество кода**
8
-   Плюсы
    - Код соответствует PEP 8, используются осмысленные имена переменных.
    - Присутствует документация к модулю и функции `set_project_root`.
    - Код корректно обрабатывает возможные исключения при чтении файлов.
    - Используется `packaging.version.Version`, хотя и не используется.
-   Минусы
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    - Отсутствует логирование ошибок, кроме `...`, которые являются точками остановки.
    - Комментарии не все в формате RST, некоторые строчные комментарии неинформативны.
    - Переменные  `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`  определены глобально, что затрудняет переиспользование.
    - В блоках `try` `except` используются `...` точки остановки.

**Рекомендации по улучшению**

1.  Использовать `j_loads` или `j_loads_ns` для чтения `settings.json`.
2.  Добавить логирование ошибок вместо `...` в блоках `try-except`.
3.  Переписать комментарии в формате RST для всех функций и переменных.
4.  Перенести определения глобальных переменных в класс или функцию.
5.  Импортировать `logger` из `src.logger.logger`.
6.  Удалить неиспользуемый импорт `packaging.version.Version`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для определения заголовков проекта.
=========================================================================================

Этот модуль предназначен для настройки и получения метаданных проекта, таких как версия, имя, автор и прочая информация.
Он также определяет корневой каталог проекта и загружает настройки из файла `settings.json`.

Пример использования
--------------------

.. code-block:: python

    from src.endpoints.advertisement import header

    print(header.__project_name__)
    print(header.__version__)
"""
import sys
from pathlib import Path
from src.utils.jjson import j_loads
from src.logger.logger import logger





def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневой каталог проекта, начиная с директории текущего файла.

    Функция ищет вверх по структуре директорий, пока не найдет директорию, содержащую один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий, которые используются для определения корня проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта, если она найдена; иначе - директория, где находится скрипт.
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


# Получает корневой каталог проекта
__root__ = set_project_root()
"""Path: Path to the root directory of the project"""

from src import gs


settings: dict = None
try:
    #  Код загружает настройки из файла 'settings.json', используя j_loads для обработки JSON
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except FileNotFoundError as e:
    #  Логирует ошибку, если файл 'settings.json' не найден
    logger.error(f'Файл settings.json не найден {e}')
    settings = {}
except Exception as e:
    # Логирует ошибку при любой другой проблеме с загрузкой JSON
    logger.error(f'Ошибка загрузки json {e}')
    settings = {}


doc_str: str = None
try:
     #  Код читает содержимое файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except FileNotFoundError as e:
    #  Логирует ошибку, если файл README.MD не найден
    logger.error(f'Файл README.MD не найден {e}')
    doc_str = ''
except Exception as e:
    #  Логирует ошибку при любой другой проблеме с чтением файла README.MD
    logger.error(f'Ошибка чтения файла README.MD {e}')
    doc_str = ''


__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Название проекта"""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта"""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта"""
__details__: str = ''
"""str: Детали проекта"""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта"""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Копирайт проекта"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение для поддержки проекта"""
```