# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    -   Код выполняет основную функцию определения корневой директории проекта и загрузки настроек.
    -   Используются `pathlib.Path` для работы с путями, что улучшает читаемость и переносимость.
    -   Используется `packaging.version.Version` для работы с версиями.
    -   Код содержит начальную документацию модуля.
    -  Код использует `try-except` для обработки ошибок при чтении файлов настроек.

-  Минусы
    -   Отсутствует явное указание кодировки при открытии файлов.
    -   Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    -   Отсутствуют `docstring` для большинства функций и переменных.
    -   Обработка ошибок в блоках `try-except` реализована через `...`, что неинформативно.
    -   Не используются логирование.
    -   Не все переменные имеют аннотации типов.
    -   Слишком много импортов (не все используются)

**Рекомендации по улучшению**

1.  Использовать `j_loads` из `src.utils.jjson` для чтения `settings.json`.
2.  Добавить `docstring` к функции `set_project_root` и ко всем переменным.
3.  Использовать явное указание кодировки UTF-8 при открытии файлов: `open(..., 'r', encoding='utf-8')`.
4.  Заменить `...` в блоках `except` на запись ошибок через `logger.error`.
5.  Добавить проверку наличия ключей в словаре `settings` перед использованием `settings.get()`.
6.  Использовать аннотации типов для переменных.
7.  Использовать `from src.logger.logger import logger` для логирования ошибок.
8.  Избавиться от неиспользуемых импортов.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения корневой директории проекта и загрузки основных настроек.
=========================================================================================

Этот модуль содержит функции и переменные для определения корневой директории проекта,
а также загрузки настроек из файла `settings.json` и документации из `README.MD`.

Пример использования
--------------------

Пример использования переменных из модуля:

.. code-block:: python

    from src.webdriver import header

    print(header.__project_name__)
    print(header.__version__)
"""
MODE: str = 'dev'

import sys
from pathlib import Path
from packaging.version import Version
from typing import Tuple
# from src.utils.jjson import j_loads # TODO убрать лишнее
from src.logger.logger import logger
from src.utils.jjson import j_loads

def set_project_root(marker_files: Tuple[str, ...] = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта, начиная с директории текущего файла.

    Поиск осуществляется вверх по дереву директорий до первой директории, содержащей
    один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий, используемых для идентификации корня проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
    :rtype: Path
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


# Определение корневой директории проекта
__root__: Path = set_project_root()
"""
:type: Path
:var __root__: Path к корневой директории проекта.
"""

from src import gs

settings: dict = {}
"""
:type: dict
:var settings: Словарь с настройками проекта.
"""
try:
    # Код исполняет чтение файла настроек settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r', encoding='utf-8') as settings_file:
        settings = j_loads(settings_file)
except FileNotFoundError:
    # Логирование ошибки, если файл не найден
    logger.error(f'Файл настроек settings.json не найден: {gs.path.root / "src" / "settings.json"}')
    ...
except Exception as ex:
    # Логирование ошибки, если не удалось декодировать JSON
    logger.error(f'Ошибка декодирования JSON в файле настроек settings.json: {ex}')
    ...


doc_str: str = ''
"""
:type: str
:var doc_str: Строка с документацией проекта из файла README.MD.
"""
try:
    # Код исполняет чтение файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as doc_file:
        doc_str = doc_file.read()
except FileNotFoundError:
    # Логирование ошибки, если файл не найден
    logger.error(f'Файл документации README.MD не найден: {gs.path.root / "src" / "README.MD"}')
    ...
except Exception as ex:
    # Логирование ошибки при чтении файла
    logger.error(f'Ошибка чтения файла README.MD: {ex}')
    ...


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
:var __doc__: Документация проекта.
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
:var __cofee__: Сообщение о поддержке разработчика.
"""
```