# Анализ кода модуля header

**Качество кода**
8
- Плюсы
    - Код выполняет свою основную задачу по определению корневой директории проекта и загрузке настроек.
    - Использует `pathlib.Path` для работы с путями.
    - Присутствует базовая обработка исключений при загрузке файлов настроек и документации.
- Минусы
    - Использование стандартного `json.load` вместо `j_loads` или `j_loads_ns`.
    - Не хватает документации в формате RST.
    - Не используются логирование через `logger.error` при ошибках.
    - Отсутствует описание модуля.
    - Переменные с именами `__root__` объявлены в теле функции и вне её.
    - `__root__` дважды переопределяется.
    - Некоторые имена переменных не соответствуют соглашениям (например, `doc_str`).
    - Жестко заданные пути `src/settings.json` и `src/README.MD`.

**Рекомендации по улучшению**

1.  Добавить описание модуля.
2.  Использовать `j_loads` или `j_loads_ns` для загрузки `settings.json`.
3.  Добавить документацию в формате RST для функции `set_project_root`.
4.  Использовать `logger.error` для логирования ошибок при загрузке файлов.
5.  Переименовать переменную `doc_str` в `readme_content` для большей ясности.
6.  Избегать повторного определения `__root__`.
7.  Объявить константы для путей к файлам `settings.json` и `README.MD`.
8.  Удалить лишние переменные.
9.  Использовать `get` с дефолтным значением для более безопасного доступа к словарю `settings`.
10.  Добавить исключение, если `settings` не загружен.
11.  Использовать `from src.logger.logger import logger`.
12.  Переименовать переменную `__cofee__` в `__coffee__`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для определения корневой директории проекта и загрузки настроек.
=========================================================================================

Этот модуль предоставляет функциональность для автоматического определения корневой директории
проекта на основе наличия специальных файлов-маркеров. Также он выполняет загрузку настроек
проекта из файла `settings.json` и содержимого файла `README.MD`, если они существуют.

Пример использования
--------------------

.. code-block:: python

    from pathlib import Path
    from src.utils._examples.header import set_project_root, __project_name__, __version__, __doc__, __details__, __author__, __copyright__, __coffee__

    root_path: Path = set_project_root()
    print(f"Root directory: {root_path}")
    print(f"Project name: {__project_name__}")
"""

import sys
from pathlib import Path
from packaging.version import Version

from src.utils.jjson import j_loads
from src.logger.logger import logger
from src import gs


SETTINGS_FILE = Path('src') / 'settings.json'
README_FILE = Path('src') / 'README.MD'

def set_project_root(marker_files: tuple[str,...] = ('__root__', '.git')) -> Path:
    """
    Определяет корневую директорию проекта, начиная с директории текущего файла.

    Поиск ведется вверх по иерархии каталогов до первого каталога, содержащего любой из файлов-маркеров.

    :param marker_files: Список имен файлов или директорий, по которым определяется корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
    :rtype: Path
    :raises FileNotFoundError: Если корневая директория не найдена и ни один из маркеров не обнаружен.
    :Example:
        >>> from pathlib import Path
        >>> root_path = set_project_root()
        >>> print(isinstance(root_path, Path))
        True
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
"""__root__ (Path): Путь к корневой директории проекта"""


settings: dict = None
try:
    # код загружает настройки из файла settings.json
    settings = j_loads(gs.path.root / SETTINGS_FILE)
except FileNotFoundError as ex:
    logger.error(f'Файл настроек не найден {gs.path.root / SETTINGS_FILE}', ex)
    settings = {}
except Exception as ex:
    logger.error(f'Ошибка при загрузке файла настроек {gs.path.root / SETTINGS_FILE}', ex)
    settings = {}

readme_content: str = None
try:
    # код загружает содержимое файла README.MD
    with open(gs.path.root / README_FILE, 'r', encoding='utf-8') as readme_file:
        readme_content = readme_file.read()
except FileNotFoundError as ex:
    logger.error(f'Файл README не найден {gs.path.root / README_FILE}', ex)
    readme_content = ''
except Exception as ex:
    logger.error(f'Ошибка при загрузке файла README {gs.path.root / README_FILE}', ex)
    readme_content = ''


__project_name__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Имя проекта"""
__version__: str = settings.get('version', '') if settings else ''
"""__version__ (str): Версия проекта"""
__doc__: str = readme_content if readme_content else ''
"""__doc__ (str): Содержимое файла README.MD"""
__details__: str = ''
"""__details__ (str): Детали проекта"""
__author__: str = settings.get('author', '') if settings else ''
"""__author__ (str): Автор проекта"""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""__copyright__ (str): Копирайт проекта"""
__coffee__: str = settings.get('cofee', "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__coffee__ (str): Сообщение о возможности угостить разработчика кофе"""

```