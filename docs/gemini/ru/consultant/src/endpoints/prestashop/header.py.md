# Анализ кода модуля header.py

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разбит на логические блоки.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Есть обработка исключений при чтении файлов настроек.
    -  Присутсвует  `docstring` для модуля.
- Минусы
    - Не все переменные и функции снабжены `docstring`.
    -  Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    -  Излишне использованы  `try-except` блоки, где можно обойтись логированием ошибок.
    -  Отсутствует импорт `logger` для логирования ошибок.

**Рекомендации по улучшению**

1.  Добавить `docstring` для всех функций и переменных.
2.  Использовать `j_loads` из `src.utils.jjson` для загрузки json файлов.
3.  Использовать `logger.error` для логирования ошибок вместо `try-except` в простых случаях.
4.  Добавить необходимые импорты.
5.  Улучшить обработку ошибок при отсутствии файла `settings.json` или `README.MD`

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения корневого пути проекта и загрузки основных настроек.
===========================================================================

Этот модуль определяет корневую директорию проекта, основываясь на наличии файлов-маркеров,
и загружает настройки из файла `settings.json`, а также читает содержимое `README.MD`.

Пример использования:
--------------------

.. code-block:: python

    from src.logger.header import __root__, __project_name__, __version__

    print(__root__)
    print(__project_name__)
    print(__version__)
"""
import sys
# импортируем json из src.utils.jjson
from src.utils.jjson import j_loads
# импортируем Path из pathlib
from pathlib import Path
# импортируем logger из src.logger.logger
from src.logger.logger import logger
# импортируем Version из packaging.version
from packaging.version import Version

# Устанавливаем режим работы по умолчанию
MODE = 'dev'


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневой каталог проекта.
    
    Начиная с каталога текущего файла, ищет вверх по дереву каталогов до первого каталога,
    содержащего хотя бы один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов, идентифицирующих корень проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу проекта. Если не найден, возвращает каталог, где расположен скрипт.
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


# Получаем корневой каталог проекта
__root__:Path = set_project_root()
"""
Path: Путь к корневому каталогу проекта.
"""

from src import gs

settings: dict = None
# код пытается открыть файл настроек settings.json и загрузить его содержимое
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except FileNotFoundError:
    # если файл не найден, логируем ошибку
    logger.error(f'Файл настроек settings.json не найден по пути {gs.path.root / "src" / "settings.json"}')
    ... # точка остановки
except Exception as ex:
    # если возникают другие ошибки при загрузке файла, логируем их
    logger.error(f'Ошибка загрузки файла settings.json: {ex}')
    ...# точка остановки

doc_str: str = None
# код пытается открыть файл README.MD и прочитать его содержимое
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except FileNotFoundError:
    # если файл не найден, логируем ошибку
    logger.error(f'Файл README.MD не найден по пути {gs.path.root / "src" / "README.MD"}')
    ... # точка остановки
except Exception as ex:
     # если возникают другие ошибки при загрузке файла, логируем их
    logger.error(f'Ошибка чтения файла README.MD: {ex}')
    ...# точка остановки



__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Имя проекта, по умолчанию 'hypotez'."""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта, по умолчанию ''. """
__doc__: str = doc_str if doc_str else ''
"""str: Содержимое файла README.MD, по умолчанию ''. """
__details__: str = ''
"""str: Дополнительные сведения о проекте, по умолчанию ''. """
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта, по умолчанию ''. """
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Информация об авторских правах, по умолчанию ''. """
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение для поддержки разработчика, по умолчанию 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'."""
```