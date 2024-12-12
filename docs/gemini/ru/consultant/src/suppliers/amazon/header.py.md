# Анализ кода модуля `header.py`

**Качество кода**
8
- Плюсы
    - Код выполняет свою основную функцию - определение корневой директории проекта и загрузку настроек.
    - Используется `pathlib` для работы с путями.
    - Есть обработка исключений при чтении файлов.
    - Присутствует описание модуля в docstring.
- Минусы
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    - Отсутствуют docstring для многих переменных.
    - Некоторые docstring не соответствуют RST.
    - Избыточное использование `try-except` вместо `logger.error`.
    - Отсутствует импорт `logger`
    - Некоторые комментарии `#` не информативны.

**Рекомендации по улучшению**
1.  Заменить `json.load` на `j_loads` из `src.utils.jjson`.
2.  Добавить docstring для всех переменных.
3.  Привести docstring к формату RST.
4.  Использовать `logger.error` вместо `try-except` для обработки ошибок.
5.  Добавить импорт `logger` из `src.logger.logger`.
6.  Уточнить комментарии `#` для лучшего понимания кода.
7.  Удалить `MODE = 'dev'`, так как не используется.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль инициализации проекта для Amazon
=========================================================================================

Этот модуль определяет корневую директорию проекта, загружает настройки из файла `settings.json`
и устанавливает глобальные переменные, такие как имя проекта, версию и описание.
Также обеспечивает чтение файла `README.MD` для дальнейшего использования.

Пример использования
--------------------

.. code-block:: python

    import src.suppliers.amazon.header as header

    print(header.__project_name__)
    print(header.__version__)
    print(header.__doc__)

"""

import sys
#  Импортируем j_loads из src.utils.jjson для корректной работы с JSON файлами.
from src.utils.jjson import j_loads 
#  Импортируем Version из packaging.version для работы с версиями.
from packaging.version import Version
#  Импортируем Path из pathlib для работы с путями.
from pathlib import Path
#  Импортируем logger из src.logger.logger для логирования ошибок.
from src.logger.logger import logger

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с директории текущего файла,
    поиском вверх и останавливаясь на первой директории, содержащей любой из файлов-маркеров.

    :param marker_files: Кортеж с именами файлов или директорий для определения корня проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если она найдена, иначе - путь к директории, где расположен скрипт.
    :rtype: Path
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    #  Проверяем, что __root__ нет в sys.path, и добавляем, если нужно.
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


#  Получаем корневую директорию проекта.
__root__ = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта"""

from src import gs

settings: dict = None
"""settings (dict): Словарь с настройками проекта, загруженными из `settings.json`"""
try:
    #  Пытаемся открыть и загрузить файл settings.json, используя j_loads.
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as ex:
     #  В случае ошибки логируем ее и продолжаем выполнение.
     logger.error(f'Ошибка при загрузке settings.json: {ex}')
     ...


doc_str: str = None
"""doc_str (str): Строка с содержимым файла `README.MD`"""
try:
    #  Пытаемся открыть и прочитать файл README.MD.
    with open(gs.path.root / 'src' /  'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as ex:
    #  В случае ошибки логируем ее и продолжаем выполнение.
    logger.error(f'Ошибка при чтении README.MD: {ex}')
    ...


__project_name__: str = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
"""__project_name__ (str): Имя проекта, извлекается из `settings.json` или по умолчанию `hypotez`"""
__version__: str = settings.get("version", '')  if settings  else ''
"""__version__ (str): Версия проекта, извлекается из `settings.json` или пустая строка"""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Содержимое файла `README.MD` или пустая строка"""
__details__: str = ''
"""__details__ (str): Детали проекта (в настоящее время не используется)"""
__author__: str = settings.get("author", '')  if settings  else ''
"""__author__ (str): Автор проекта, извлекается из `settings.json` или пустая строка"""
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
"""__copyright__ (str): Информация об авторских правах, извлекается из `settings.json` или пустая строка"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Сообщение о возможности поддержать разработчика, извлекается из `settings.json` или значение по умолчанию"""
```