# Анализ кода модуля `header.py`

**Качество кода**
7
- Плюсы
    - Код структурирован и относительно читаем.
    - Используется `pathlib` для работы с путями.
    - Есть обработка исключений для чтения файлов.
    - Функция `set_project_root` выделена в отдельный блок кода.
- Минусы
    - Не используется `j_loads` или `j_loads_ns` для чтения JSON, как требуется в инструкции.
    - Отсутствуют docstrings для модуля и функции `set_project_root`.
    - Не все переменные имеют аннотации типов.
    - Используется стандартный `try-except` вместо логирования через `logger.error`.
    - Некоторые переменные не имеют четкого типа, что затрудняет понимание кода.
    - Не все константы имеют префикс __
    - Отсутствует импорт logger

**Рекомендации по улучшению**
1.  Добавить docstring для модуля и функции `set_project_root` в формате reStructuredText.
2.  Использовать `j_loads` или `j_loads_ns` для чтения JSON файлов.
3.  Использовать `logger.error` для обработки исключений вместо стандартных блоков `try-except`.
4.  Добавить импорт `from src.utils.jjson import j_loads`
5.  Добавить импорт `from src.logger.logger import logger`
6.  Добавить аннотации типов для переменных, где это необходимо.
7.  Удалить неиспользуемые импорты `sys`
8.  Убрать дублирование констант, вынеся их в отдельную область
9.  Избавится от дублирования кода с try except.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для определения корневой директории проекта и загрузки основных настроек.
==============================================================================

Этот модуль определяет корневую директорию проекта, загружает настройки из файла `settings.json`,
и читает документацию из `README.MD`.

Модуль содержит:

- Функцию :func:`set_project_root` для определения корневой директории проекта.
- Глобальные переменные для хранения настроек и информации о проекте.

Пример использования
--------------------

.. code-block:: python

    from src.suppliers.ksp.header import __project_name__, __version__, __doc__

    print(f"Project Name: {__project_name__}")
    print(f"Version: {__version__}")
    print(f"Documentation: {__doc__}")

"""
import json
from pathlib import Path
from packaging.version import Version
#  Импорт модуля j_loads из src.utils.jjson
from src.utils.jjson import j_loads
#  Импорт модуля logger из src.logger.logger
from src.logger.logger import logger
# Импорт модуля gs
from src import gs


MODE: str = 'dev'
__MARKER_FILES__: tuple = ('__root__',)

def set_project_root(marker_files: tuple = __MARKER_FILES__) -> Path:
    """
    Определяет корневую директорию проекта, начиная с директории текущего файла.

    Поиск идет вверх по структуре каталогов до первого каталога,
    содержащего любой из файлов-маркеров.

    :param marker_files: Список имен файлов или каталогов, идентифицирующих корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если она найдена, иначе - директория, где находится скрипт.
    :rtype: Path
    """
    __root__: Path
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if str(__root__) not in gs.sys_path:
        gs.sys_path.insert(0, str(__root__))
    return __root__


# Get the root directory of the project
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта"""

settings: dict = {}
doc_str: str = ''

#  Функция для загрузки настроек из файла с обработкой ошибок
def _load_settings(file_path: Path) -> dict or str:
    """Загружает настройки из файла.

    :param file_path: Путь к файлу настроек.
    :type file_path: Path
    :return: Словарь с настройками или строка с данными, в случае успеха, иначе None.
    :rtype: dict or str
    """
    try:
        #  Используется j_loads для чтения файла
        with open(file_path, 'r', encoding='utf-8') as settings_file:
            if file_path.name == 'settings.json':
                return j_loads(settings_file)
            return settings_file.read()

    except FileNotFoundError:
        logger.error(f'Файл не найден: {file_path}')
        return None
    except json.JSONDecodeError as e:
        logger.error(f'Ошибка декодирования JSON в файле: {file_path}, {e}')
        return None
    except Exception as ex:
        logger.error(f'Неизвестная ошибка при чтении файла: {file_path}, {ex}')
        return None
    

# Код вызывает функцию _load_settings для чтения settings.json
settings = _load_settings(gs.path.root / 'src' / 'settings.json') if  _load_settings(gs.path.root / 'src' / 'settings.json') else {}

#  Код вызывает функцию _load_settings для чтения README.MD
doc_str = _load_settings(gs.path.root / 'src' / 'README.MD') if  _load_settings(gs.path.root / 'src' / 'README.MD') else ''



__project_name__: str = settings.get("project_name", 'hypotez')
"""__project_name__ (str): Имя проекта"""
__version__: str = settings.get("version", '')
"""__version__ (str): Версия проекта"""
__doc__: str = doc_str
"""__doc__ (str): Документация проекта"""
__details__: str = ''
"""__details__ (str): Детали проекта"""
__author__: str = settings.get("author", '')
"""__author__ (str): Автор проекта"""
__copyright__: str = settings.get("copyrihgnt", '')
"""__copyright__ (str): Авторские права"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")
"""__cofee__ (str): Сообщение для поддержки автора"""
```