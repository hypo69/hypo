# Анализ кода модуля `header.py`

**Качество кода**
8
- Плюсы
    - Код содержит docstring для модуля и функции `set_project_root`, что соответствует требованиям по документации.
    - Используется `pathlib.Path` для работы с путями, что является хорошей практикой.
    - Определена функция `set_project_root` для поиска корневой директории проекта, что полезно для работы с относительными путями.
    - Используется `try-except` для обработки ошибок при загрузке `settings.json` и `README.MD`.
    -  Присваивание значений переменным, таким как `__project_name__`, `__version__` и др., производится с использованием метода `get()` словаря `settings`, что предотвращает ошибки при отсутствии ключей.
- Минусы
    - Используется `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Отсутствуют импорты из `src.logger.logger`.
    - Используются `...` в блоках `try-except` для пропуска обработки ошибок, что не является лучшей практикой.
    - Не все переменные имеют docstring, особенно `__root__`.
    - Отсутствует обработка ошибок при открытии `README.MD` (используется `json.JSONDecodeError`, что не подходит для текстового файла).
    - Не все переменные имеют type hinting.
    - Отсутствуют docstring для переменных `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__` и `__cofee__`.
    - `` должен быть константой и записан с верхним регистром.

**Рекомендации по улучшению**

1.  Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
2.  Добавить импорт `from src.logger.logger import logger`.
3.  Заменить `...` на логирование ошибок с помощью `logger.error`.
4.  Добавить docstring для переменных, особенно `__root__`.
5.  Исправить ошибку в `try-except` для `README.MD`, используя `FileNotFoundError` и `UnicodeDecodeError`.
6.  Добавить type hinting для всех переменных.
7.  Добавить docstring для всех переменных, особенно `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__` и `__cofee__`.
8.  Переименовать переменную `MODE` в `MODE_DEV` и перевести в верхний регистр.
9.  Добавить обработку исключений более специфично.
10. Добавить RST-комментарии к каждой переменной.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для определения корневой директории проекта и загрузки настроек.
=========================================================================================

Этот модуль определяет корневую директорию проекта, загружает настройки из `settings.json`
и документацию из `README.MD`, а также устанавливает основные переменные проекта.

Пример использования
--------------------

Импортируйте этот модуль, чтобы получить доступ к общим настройкам и переменным проекта.

.. code-block:: python

    from src.endpoints.prestashop.api import header

    print(header.__project_name__)
    print(header.__version__)
"""
import sys
#  Импортируем j_loads для загрузки json файлов
from src.utils.jjson import j_loads
#  Импортируем логгер
from src.logger.logger import logger
from packaging.version import Version
from pathlib import Path
# Константа для определения режима работы
MODE_DEV = 'dev'

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.
    
    Функция просматривает родительские директории, начиная с директории текущего файла,
    и останавливается на первой директории, содержащей любой из файлов-маркеров.
    
    :param marker_files: Кортеж имен файлов или директорий для идентификации корневой директории проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если она найдена, иначе путь к директории, где расположен скрипт.
    :rtype: Path
    
    Пример использования
    --------------------
    
    .. code-block:: python
    
        root_path = set_project_root()
    """
    __root__:Path
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
__root__: Path = set_project_root()
"""
:type: Path
:var __root__: Path к корневой директории проекта.
"""

from src import gs

settings: dict = None
try:
    #  Загрузка настроек из файла settings.json с использованием j_loads
    with open(gs.path.root / 'src' / 'settings.json', 'r', encoding='utf-8') as settings_file:
        settings = j_loads(settings_file)
except FileNotFoundError as ex:
    #  Логируем ошибку, если файл не найден
    logger.error(f'Файл settings.json не найден: {ex}')
except Exception as ex:
    #  Логируем ошибку, если файл не распарсился
    logger.error(f'Ошибка при загрузке файла settings.json: {ex}')


doc_str: str = None
try:
    #  Загружаем содержимое файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as doc_file:
        doc_str = doc_file.read()
except FileNotFoundError as ex:
    #  Логируем ошибку, если файл не найден
    logger.error(f'Файл README.MD не найден: {ex}')
except UnicodeDecodeError as ex:
    #  Логируем ошибку, если файл не декодируется
    logger.error(f'Ошибка декодирования файла README.MD: {ex}')
except Exception as ex:
     #  Логируем другие ошибки
    logger.error(f'Произошла ошибка при загрузке README.MD: {ex}')



__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""
:type: str
:var __project_name__: Имя проекта.
"""
__version__: str = settings.get("version", '') if settings else ''
"""
:type: str
:var __version__: Версия проекта.
"""
__doc__: str = doc_str if doc_str else ''
"""
:type: str
:var __doc__: Строка документации проекта.
"""
__details__: str = ''
"""
:type: str
:var __details__: Детали проекта.
"""
__author__: str = settings.get("author", '') if settings else ''
"""
:type: str
:var __author__: Автор проекта.
"""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""
:type: str
:var __copyright__: Авторские права проекта.
"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""
:type: str
:var __cofee__: Сообщение о кофе для разработчика.
"""
```