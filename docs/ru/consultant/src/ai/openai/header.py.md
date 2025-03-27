# Анализ кода модуля `header`

## Качество кода:

- **Соответствие стандартам**: 7
- **Плюсы**:
    - Код выполняет свою основную задачу - определение корневого каталога проекта.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Есть обработка исключений при чтении файлов настроек и документации.
    - Добавлены аннотации типов, что улучшает читаемость и понятность кода.
    -  Присутствует базовая документация модуля.
- **Минусы**:
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    - Не все комментарии соответствуют стандарту RST.
    - Обработка ошибок происходит без использования `logger.error`.
    - Есть избыточное присваивание `__root__ = current_path` и затем переопределение в цикле.
    - Использование `...` в блоках `try-except` без логирования.
    - Нарушение форматирования в некоторых местах (например, отсутствие пробелов после `:` в аннотациях типов).

## Рекомендации по улучшению:

- Заменить стандартный `json.load` на `j_loads` из `src.utils.jjson`.
- Использовать `logger.error` для логирования ошибок вместо `...` в блоках `try-except`.
- Добавить RST-комментарии для модуля, функций и переменных.
- Избавиться от избыточного присваивания `__root__ = current_path` и сразу присваивать в цикле.
- Привести код в соответствие со стандартами PEP8.
-  Использовать `from src.logger.logger import logger`.
- Добавить обработку исключений при импорте `gs`.
- Изменить способ установки переменных по умолчанию, например, через оператор `or`.

## Оптимизированный код:

```python
"""
Модуль для определения корневого каталога проекта и загрузки настроек.
=======================================================================

Модуль определяет корневой каталог проекта на основе наличия маркерных файлов
и загружает настройки проекта из файла `settings.json`. Также извлекает
основную документацию проекта из `README.MD`.

Пример использования
----------------------
.. code-block:: python

    from src.logger.header import __project_name__, __version__, __doc__, __author__

    print(f"Имя проекта: {__project_name__}")
    print(f"Версия: {__version__}")
    print(f"Автор: {__author__}")
    print(f"Описание: {__doc__}")
"""

import sys
from pathlib import Path
from packaging.version import Version

from src.utils.jjson import j_loads  # Используем j_loads для загрузки json
from src.logger.logger import logger  # Импортируем logger из src.logger.logger

def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Находит корневой каталог проекта, начиная с каталога текущего файла,
    идя вверх по дереву каталогов и останавливаясь на первом каталоге,
    содержащем любой из маркерных файлов.

    :param marker_files: Кортеж имен файлов или каталогов для идентификации корня проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу, если он найден, иначе путь к каталогу, где находится скрипт.
    :rtype: Path

    Пример
    -------
    .. code-block:: python
        
        from pathlib import Path
        root_path = set_project_root(marker_files=('_root_', '.git'))
        print(root_path)
        # Output will vary based on the location of the project root
    """
    current_path: Path = Path(__file__).resolve().parent
    __root__: Path = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if str(__root__) not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__

# Get the root directory of the project
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневому каталогу проекта"""

try:
    from src import gs  # Импортируем gs
except ImportError as e:
    logger.error(f"Ошибка импорта модуля gs: {e}")  # Логируем ошибку импорта
    gs = None  # Присваиваем None, чтобы избежать ошибки в дальнейшем

settings: dict = None
try:
    if gs:
        with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
           settings = j_loads(settings_file) # Используем j_loads для загрузки json
except FileNotFoundError:
    logger.error("Файл settings.json не найден.")  # Логируем ошибку отсутствия файла
except Exception as e:
    logger.error(f"Ошибка при чтении settings.json: {e}")  # Логируем другие ошибки при чтении

doc_str: str = None
try:
    if gs:
        with open(gs.path.root / 'src' / 'README.MD', 'r') as doc_file:
            doc_str = doc_file.read()
except FileNotFoundError:
    logger.error("Файл README.MD не найден.")  # Логируем ошибку отсутствия файла
except Exception as e:
     logger.error(f"Ошибка при чтении README.MD: {e}")  # Логируем другие ошибки при чтении

__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez' # Установка значения по умолчанию через оператор or
"""__project_name__ (str): Имя проекта"""
__version__: str = settings.get("version", '') if settings else ''
"""__version__ (str): Версия проекта"""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Документация проекта"""
__details__: str = ''
"""__details__ (str): Детали проекта (в текущей реализации не используется)"""
__author__: str = settings.get("author", '') if settings else ''
"""__author__ (str): Автор проекта"""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""__copyright__ (str): Информация об авторских правах"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Информация о поддержке разработчика"""
```