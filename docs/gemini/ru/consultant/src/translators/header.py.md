# Анализ кода модуля header.py

**Качество кода**
7
-  Плюсы
    - Код выполняет задачу определения корневой директории проекта и загрузки настроек.
    - Используется `pathlib` для работы с путями.
    - Присутствует обработка исключений при чтении файлов настроек.
-  Минусы
    - Не используются импорты `j_loads` и `j_loads_ns` из `src.utils.jjson`.
    - Отсутствует использование `logger`.
    - Комментарии в начале файла не соответствуют стандарту оформления.
    - Отсутствует документация в формате RST для функций и переменных.
    - Избыточное использование try-except.
    - В начале файла есть много пустых docstring.
    - `FileNotFoundError, json.JSONDecodeError` перехвачены, но не залогированы
    - Не используются константы для путей `settings.json` и `README.MD`

**Рекомендации по улучшению**

1.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов JSON.
2.  Добавить импорт и использовать `logger` из `src.logger.logger` для логирования ошибок.
3.  Добавить описание модуля в начале файла в формате RST.
4.  Документировать каждую функцию и переменную, используя docstrings в формате RST.
5.  Избегать избыточного использования `try-except`, использовать `logger.error` для обработки ошибок.
6.  Удалить лишние docstring в начале файла.
7.  Убрать неиспользуемые импорты.
8.  Добавить константы для путей `settings.json` и `README.MD`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для определения корневой директории проекта и загрузки настроек.
======================================================================

Этот модуль предоставляет функциональность для автоматического определения
корневой директории проекта на основе наличия специальных файлов-маркеров.
Также он загружает настройки проекта из файла `settings.json` и считывает
содержимое файла `README.MD` для использования в переменных проекта.

Пример использования
--------------------

.. code-block:: python

    from src.translators.header import __project_name__, __version__, __doc__

    print(f"Имя проекта: {__project_name__}")
    print(f"Версия проекта: {__version__}")
    print(f"Документация проекта: {__doc__}")
"""
import sys
from pathlib import Path
from src.utils.jjson import j_loads #  Используем j_loads для загрузки JSON
from src.logger.logger import logger #  Импортируем logger
SETTINGS_FILE = 'settings.json' # Константа для пути к файлу настроек
README_FILE = 'README.MD'      # Константа для пути к файлу README

def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Находит корневой каталог проекта, начиная с каталога текущего файла,
    просматривая вверх и останавливаясь на первом каталоге, содержащем
    любой из файлов-маркеров.

    :param marker_files: Имена файлов или каталогов для идентификации корня проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу, если найден, иначе каталог, где расположен скрипт.
    :rtype: Path

    :Example:
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
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__

#  Получаем корневую директорию проекта
__root__ = set_project_root()
"""__root__ (Path): Путь к корневому каталогу проекта"""

from src import gs

settings: dict = None
try:
    #  Используем j_loads для загрузки настроек из файла
    with open(gs.path.root / 'src' / SETTINGS_FILE, 'r') as settings_file: # Используем константу SETTINGS_FILE
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    #  Логируем ошибку, если файл не найден или JSON не может быть декодирован
    logger.error(f'Не удалось загрузить файл настроек {SETTINGS_FILE}: {e}')
    settings = {}

doc_str: str = None
try:
    #  Считываем содержимое README.MD
    with open(gs.path.root / 'src' / README_FILE, 'r') as readme_file: # Используем константу README_FILE
        doc_str = readme_file.read()
except (FileNotFoundError, UnicodeDecodeError) as e:
    #  Логируем ошибку, если файл не найден или не может быть прочитан
    logger.error(f'Не удалось загрузить файл документации {README_FILE}: {e}')
    doc_str = ''
    
__project_name__ = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Имя проекта, извлекается из settings.json или по умолчанию 'hypotez'"""
__version__: str = settings.get('version', '') if settings else ''
"""__version__ (str): Версия проекта, извлекается из settings.json или по умолчанию ''"""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Документация проекта, извлекается из README.MD или по умолчанию ''"""
__details__: str = ''
"""__details__ (str): Детали проекта, пока не используется"""
__author__: str = settings.get('author', '') if settings else ''
"""__author__ (str): Автор проекта, извлекается из settings.json или по умолчанию ''"""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""__copyright__ (str): Информация об авторских правах, извлекается из settings.json или по умолчанию ''"""
__cofee__: str = settings.get('cofee', "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Сообщение о кофе, извлекается из settings.json или значение по умолчанию"""
```