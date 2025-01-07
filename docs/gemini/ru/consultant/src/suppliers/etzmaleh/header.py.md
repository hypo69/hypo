# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    -  Код выполняет задачу определения корневой директории проекта.
    -  Используется `pathlib.Path` для работы с путями.
    -  Используются константы для хранения настроек проекта.
    -  Есть обработка исключений при чтении файлов.
-  Минусы
    -  Не используются docstring для модуля.
    -  Не используются `j_loads` или `j_loads_ns`.
    -  Используется `try-except` для обработки ошибок, что не соответствует требованиям инструкции.
    -  Отсутствует логирование ошибок.
    -  Смешивание объявлений и присваиваний констант.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля в формате RST.
2.  Заменить `json.load` на `j_loads` для загрузки файла `settings.json`.
3.  Добавить логирование ошибок с использованием `logger.error` вместо `...` в блоках `try-except`.
4.  Удалить неиспользуемую переменную `MODE`.
5.  Перенести определение констант проекта после загрузки настроек `settings`.
6.  Добавить описание типов для констант.
7.  Удалить лишнюю переменную `__root__` и объеденить объявление и присваивание в `set_project_root`
8.  Использовать f-строки для форматирования логов.
9.  Использовать `or` в выражении при чтении `settings.json` и `README.MD`.
10. Добавить более конкретные сообщения в `logger.error`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для определения корневой директории проекта и загрузки основных настроек.
=========================================================================================

Этот модуль определяет корневую директорию проекта и загружает настройки из файла `settings.json`.
Также он предоставляет константы с информацией о проекте, такие как имя, версия, автор и т.д.

Пример использования
--------------------

Пример использования функций и переменных модуля::

    from src.suppliers.etzmaleh import header

    print(header.__project_name__)
    print(header.__version__)
    print(header.__doc__)
"""

import sys
#from json import load as j_loads # TODO: разобраться почему так
from pathlib import Path
from src.utils.jjson import j_loads
from src.logger.logger import logger
from packaging.version import Version

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.
    
    Поиск ведется вверх по директориям, начиная с директории текущего файла, до тех пор,
    пока не будет найдена директория, содержащая один из файлов-маркеров.

    :param marker_files: Список имен файлов-маркеров, определяющих корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
    :rtype: Path
    """
    current_path:Path = Path(__file__).resolve().parent
    root:Path = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            root = parent
            break
    if root not in sys.path:
        sys.path.insert(0, str(root))
    return root

# Код исполняет поиск и определение корневой директории проекта
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта"""

from src import gs

settings: dict = {}
# Код исполняет загрузку настроек из файла settings.json
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, Exception) as e:
     logger.error(f'Ошибка при загрузке файла settings.json: {e}')


doc_str: str = ''
# Код исполняет чтение содержимого файла README.MD
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as readme_file:
        doc_str = readme_file.read()
except (FileNotFoundError, Exception) as e:
    logger.error(f'Ошибка при чтении файла README.MD: {e}')

# Код исполняет определение констант проекта
__project_name__: str = settings.get("project_name", 'hypotez')  if settings else 'hypotez'
"""__project_name__ (str): Имя проекта"""
__version__: str = settings.get("version", '')  if settings else ''
"""__version__ (str): Версия проекта"""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Содержание документации проекта"""
__details__: str = ''
"""__details__ (str): Детали проекта"""
__author__: str = settings.get("author", '')  if settings else ''
"""__author__ (str): Автор проекта"""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""__copyright__ (str): Авторские права проекта"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Сообщение о поддержке проекта"""
```