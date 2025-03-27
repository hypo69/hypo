# Анализ кода модуля `header`

**Качество кода**:

- **Соответствие стандартам**: 7
- **Плюсы**:
    - Код выполняет поставленную задачу по определению корневой директории проекта.
    - Присутствует обработка исключений при загрузке конфигурационных файлов.
    - Использование `pathlib` для работы с путями.
    - Документация для функции `set_project_root`.
- **Минусы**:
    - Используется `json.load` вместо `j_loads` или `j_loads_ns`.
    - Не используется `logger` для записи ошибок.
    - Смешение использования кавычек (одинарных и двойных).
    - Не используется RST-формат для документации модуля и переменных.
    - Использование `try-except` с `...` вместо конкретной обработки ошибки.
    - Отсутствие импорта `logger` из `src.logger`.
    - Не выравнен импорт модулей.
    - Не выравнено присвоение переменных.

**Рекомендации по улучшению**:

-   Использовать `j_loads` из `src.utils.jjson` вместо стандартного `json.load` для загрузки JSON-файлов.
-   Импортировать `logger` из `src.logger` и использовать его для логирования ошибок вместо `try-except` с `...`.
-   Применять только одинарные кавычки (`'`) для строк, кроме случаев, когда это необходимо для вывода (`print`, `logger.error` и т.д.).
-   Добавить RST-документацию для модуля и переменных.
-   Удалить `try-except` блоки с `...` и заменить их на логирование ошибок через `logger.error`.
-   Выровнять импорты и присваивания переменных для лучшей читаемости.
-   Добавить docstring к модулю
-   Уточнить комментарий для `__root__` что это путь именно к папке проекта.
-   Использовать `from src.logger import logger` для импорта `logger`.

**Оптимизированный код**:

```python
# -*- coding: utf-8 -*-
"""
Модуль для определения корневой директории проекта и загрузки настроек.
====================================================================

Модуль предоставляет функциональность для автоматического определения корневой директории проекта
и загрузки настроек из файла `settings.json`, а также чтения документации из `README.MD`.

Пример использования
--------------------

.. code-block:: python

    from pathlib import Path
    from src.suppliers.grandadvance.header import __root__, settings, __project_name__, __version__, __doc__, __details__, __author__, __copyright__, __cofee__

    print(__root__) # Path к папке проекта
    print(settings) # Словарь с настройками
    print(__project_name__) # Название проекта
    ...
"""
import sys
from pathlib import Path
from packaging.version import Version

from src.utils.jjson import j_loads  # используется для загрузки json
from src.logger import logger # используется для логирования
#from src import gs # данный импорт не используется и будет удален


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с директории текущего файла,
    поиском вверх и останавливаясь в первой директории, содержащей любой из маркерных файлов.

    :param marker_files: Кортеж с именами файлов или каталогов, определяющих корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если она найдена, иначе - директория, где расположен скрипт.
    :rtype: Path
    """
    current_path: Path = Path(__file__).resolve().parent
    __root__: Path = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Получаем корневую директорию проекта
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта"""


settings: dict | None = None
try:
    with open(__root__ / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file) # Используем j_loads
except (FileNotFoundError, json.JSONDecodeError) as e: # отлавливаем ошибку и логируем
    logger.error(f'Error loading settings.json: {e}')


doc_str: str | None = None
try:
    with open(__root__ / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:# отлавливаем ошибку и логируем
    logger.error(f'Error loading README.MD: {e}')


__project_name__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Название проекта."""
__version__: str = settings.get('version', '') if settings else ''
"""__version__ (str): Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Документация проекта."""
__details__: str = ''
"""__details__ (str): Детали проекта."""
__author__: str = settings.get('author', '') if settings else ''
"""__author__ (str): Автор проекта."""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""__copyright__ (str): Авторские права."""
__cofee__: str = settings.get('cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69') if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
"""__cofee__ (str): Призыв угостить разработчика кофе."""
```