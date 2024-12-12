# Анализ кода модуля `header.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и понятен, с использованием docstring для описания функций.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Логика поиска корневой директории проекта реализована корректно.
- Минусы
    - Не используется `j_loads` для чтения json файлов.
    -  Обработка ошибок `FileNotFoundError` и `json.JSONDecodeError`  выполнена с использованием `...` без логирования ошибок.
    - Не все переменные имеют docstring.
    -  Не используется  `from src.logger.logger import logger` для логирования ошибок.

**Рекомендации по улучшению**
1.  Используйте `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения JSON файлов.
2.  Замените `...` в блоках `try-except` на логирование ошибок с помощью `logger.error`.
3.  Добавьте docstring для всех переменных модуля.
4.  Используйте `from src.logger.logger import logger` для логирования ошибок.
5.  Измените все комментарии в стиле `#` на комментарии в формате RST.
6.  Исправьте опечатку `copyrihgnt` на `copyright`.
7.  Добавить docstring для модуля.

**Оптимизированный код**
```python
"""
Модуль для определения настроек и параметров проекта.
==================================================================

Этот модуль отвечает за определение корневой директории проекта,
загрузку настроек из файла `settings.json`, и получение информации
о проекте, такой как имя, версия, автор и прочее.

Основные функции:
    - :func:`set_project_root`: Поиск корневой директории проекта.
    - Загрузка настроек из `settings.json`.
    - Определение основных параметров проекта.

Пример использования:
---------------------

.. code-block:: python

    from src.suppliers.chat_gpt.header import __project_name__, __version__, __author__

    print(f"Project name: {__project_name__}")
    print(f"Version: {__version__}")
    print(f"Author: {__author__}")
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
MODE = 'dev'

import sys
#  Импортируем j_loads из src.utils.jjson
from src.utils.jjson import j_loads
from packaging.version import Version
from pathlib import Path
# импортируем логер
from src.logger.logger import logger
from src import gs


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Ищет корневой каталог проекта, начиная с каталога текущего файла,
    поиск идет вверх и останавливается на первом каталоге, содержащем
    любой из файлов-маркеров.

    :param marker_files: Имена файлов или каталогов для определения корня проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу, если найден, иначе каталог, где находится скрипт.
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


#  Получаем корневую директорию проекта
__root__ = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта"""

settings: dict = None
#  Используем j_loads для чтения файла settings.json
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логируем ошибку если файл не найден или невалидный json
    logger.error(f'Ошибка при чтении файла settings.json: {e}')


doc_str: str = None
#  Читаем содержимое файла README.MD
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логируем ошибку если файл не найден
    logger.error(f'Ошибка при чтении файла README.MD: {e}')

#  Определяем основные параметры проекта
__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Имя проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""__version__ (str): Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Документация проекта из README.MD."""
__details__: str = ''
"""__details__ (str): Дополнительная информация о проекте."""
__author__: str = settings.get("author", '') if settings else ''
"""__author__ (str): Автор проекта."""
__copyright__: str = settings.get("copyright", '') if settings else ''
"""__copyright__ (str): Информация об авторских правах."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Сообщение для поддержки разработчика."""
```