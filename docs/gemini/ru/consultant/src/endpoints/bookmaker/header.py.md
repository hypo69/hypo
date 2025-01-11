# Анализ кода модуля `header.py`

**Качество кода**
7/10
- Плюсы:
    -  Код выполняет свою основную задачу по определению корневой директории проекта и загрузке настроек.
    -  Используется `pathlib` для работы с путями, что делает код более читаемым и кросс-платформенным.
    -  Присутствует обработка исключений для ситуаций, когда файлы настроек не найдены или повреждены.
- Минусы:
    -  Используется `json.load` вместо `j_loads` из `src.utils.jjson`.
    -  Отсутствует импорт `logger` из `src.logger.logger`.
    -  Избыточное использование `try-except` блоков с `...`.
    -  Отсутствует документация в формате RST для модуля, переменных.

**Рекомендации по улучшению**

1.  Заменить `json.load` на `j_loads_ns` из `src.utils.jjson`.
2.  Добавить импорт `logger` из `src.logger.logger`.
3.  Упростить обработку исключений, используя `logger.error` вместо `...`.
4.  Добавить документацию в формате RST для модуля, переменных и функции `set_project_root`.
5.  Использовать одинарные кавычки для строк в коде, двойные кавычки только для операций вывода.
6.  Перенести определение `__root__` в начало файла, чтобы его использование было объявлено до использования.
7.  Переименовать переменную `settings_file` на `file` в блоках `try-except`.
8.  Заменить `if settings else` на тернарный оператор.
9.  Переименовать `copyrihgnt` на `copyright`.
10. Заменить `FileNotFoundError, json.JSONDecodeError` на `OSError` и ловить все ошибки ввода вывода.

**Оптимизированный код**

```python
"""
Модуль для определения корневой директории проекта и загрузки настроек.
=========================================================================================

Этот модуль определяет корневую директорию проекта, загружает настройки из файла `settings.json` и
содержит метаданные проекта, такие как имя, версия, автор и т.д.

Пример использования
--------------------

.. code-block:: python

    from src.endpoints.bookmaker.header import __project_name__, __version__, __doc__
    print(__project_name__)
    print(__version__)
    print(__doc__)
"""
import sys
from pathlib import Path
from packaging.version import Version

from src.utils.jjson import j_loads_ns
from src.logger.logger import logger


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Определяет корневой каталог проекта, начиная с каталога текущего файла.
    
    Поиск идет вверх по дереву каталогов, останавливаясь на первом каталоге,
    содержащем любой из файлов-маркеров.
    
    :param marker_files: Кортеж имен файлов или каталогов для идентификации корня проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу, если найден, в противном случае - каталог, где расположен скрипт.
    :rtype: Path
    
    :Example:
    
    .. code-block:: python
    
        root_path = set_project_root()
        print(root_path)
    
    """
    current_path: Path = Path(__file__).resolve().parent
    root_path: Path = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            root_path = parent
            break
    if root_path not in sys.path:
        sys.path.insert(0, str(root_path))
    return root_path


# Получение корневой директории проекта
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта."""

from src import gs

settings: dict = None
try:
    # код исполняет загрузку настроек из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as file:
        settings = j_loads_ns(file)
except OSError as ex:
    # Логирование ошибки, если файл не найден или поврежден
    logger.error(f'Ошибка при загрузке файла настроек settings.json: {ex}')

doc_str: str = None
try:
    # код исполняет загрузку документации из файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as file:
        doc_str = file.read()
except OSError as ex:
    # Логирование ошибки, если файл не найден или поврежден
    logger.error(f'Ошибка при загрузке файла документации README.MD: {ex}')

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
__copyright__: str = settings.get('copyright', '') if settings else ''
"""__copyright__ (str): Авторские права проекта."""
__cofee__: str = settings.get('cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69') if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
"""__cofee__ (str): Сообщение о поддержке разработчика."""
```