# Анализ кода модуля header.py

**Качество кода**
6
- Плюсы
    - Код выполняет задачу по определению корневой директории проекта и загрузке настроек.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Есть обработка исключений при загрузке файлов.
- Минусы
    - Отсутствует документация модуля.
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Нет импорта `logger` из `src.logger.logger`.
    - Использование `...` в блоках `except` не является информативным.
    - Не все переменные имеют docstring.
    - Использование двойных кавычек в строках там где нужно одинарные.

**Рекомендации по улучшению**

1.  Добавить документацию модуля.
2.  Использовать `j_loads` из `src.utils.jjson` для загрузки `settings.json`.
3.  Импортировать `logger` из `src.logger.logger`.
4.  Заменить `...` в `except` на логирование ошибки с помощью `logger.error`.
5.  Добавить docstring для всех переменных модуля.
6.  Использовать одинарные кавычки для строк в коде, кроме операций вывода.
7.  Привести имена переменных к общему виду.
8.  Улучшить читаемость кода путем добавления пустых строк и комментариев.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для определения корневой директории проекта и загрузки общих настроек.
==============================================================================

Этот модуль выполняет поиск корневой директории проекта, загружает настройки из
файла `settings.json` и читает документацию из `README.MD`.

Пример использования
--------------------

.. code-block:: python

    from src.endpoints.header import __project_name__, __version__, __doc__

    print(__project_name__)
    print(__version__)
    print(__doc__)
"""

import sys
from pathlib import Path
#  Импортируем j_loads_ns  для чтения json
from src.utils.jjson import j_loads_ns
#  Импортируем logger
from src.logger.logger import logger
#  Импортируем Version
from packaging.version import Version


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с директории текущего файла,
    поиск ведется вверх до первой директории, содержащей один из файлов-маркеров.

    Args:
        marker_files (tuple): Имена файлов или директорий для идентификации корня проекта.

    Returns:
        Path: Путь к корневой директории, если она найдена, иначе путь к директории, где находится скрипт.
    """
    current_path: Path = Path(__file__).resolve().parent
    project_root: Path = current_path
    #  Код выполняет поиск родительских директорий
    for parent in [current_path] + list(current_path.parents):
        #  Проверяем наличие маркеров в родительской директории
        if any((parent / marker).exists() for marker in marker_files):
            project_root = parent
            break
    #  Добавляем путь к корневой директории в sys.path
    if project_root not in sys.path:
        sys.path.insert(0, str(project_root))
    return project_root


#  Получаем корневую директорию проекта
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта."""

from src import gs

settings: dict = None
#  Попытка загрузить настройки из файла settings.json
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads_ns(settings_file)
except (FileNotFoundError, Exception) as ex:
    # Логируем ошибку при неудачной загрузке файла
    logger.error(f'Ошибка загрузки файла настроек: {ex}')

doc_str: str = None
#  Попытка загрузить документацию из файла README.MD
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, Exception) as ex:
    # Логируем ошибку при неудачной загрузке файла
    logger.error(f'Ошибка загрузки файла документации: {ex}')


__project_name__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Название проекта."""
__version__: str = settings.get('version', '') if settings else ''
"""__version__ (str): Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Документация проекта."""
__details__: str = ''
"""__details__ (str): Дополнительные детали проекта."""
__author__: str = settings.get('author', '') if settings else ''
"""__author__ (str): Автор проекта."""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""__copyright__ (str): Информация об авторских правах проекта."""
__cofee__: str = settings.get('cofee', "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Сообщение с предложением поддержать разработчика."""
```