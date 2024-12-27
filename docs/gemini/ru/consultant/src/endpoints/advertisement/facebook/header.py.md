# Анализ кода модуля `header.py`

**Качество кода**
9
-   Плюсы
    -   Код хорошо структурирован, используются функции для определения корневой директории.
    -   Присутствует обработка исключений при чтении файлов настроек.
    -   Используются переменные для хранения информации о проекте, что упрощает доступ к ней.
    -   Код соответствует PEP8.
-   Минусы
    -   Используется `json.load` вместо `j_loads` или `j_loads_ns`.
    -   Отсутствуют docstrings для функций, переменных и модулей в формате reStructuredText.
    -   Используется `try-except` без логирования ошибок.
    -   Используются `...` как точки остановки, что не является лучшей практикой.
    -   Не все импорты необходимые для работы кода импортированы.
    -   Объявление `settings: dict = None` и `doc_str: str = None` не соответствуют стандарту PEP-8 и должны быть объявлены без указания типа.

**Рекомендации по улучшению**

1.  Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
2.  Добавить docstrings в формате reStructuredText для модуля, функций и переменных.
3.  Использовать `logger.error` для логирования ошибок вместо `try-except`.
4.  Удалить `...` как точки остановки или заменить на логирование ошибок.
5.  Добавить необходимые импорты.
6.  Переписать код в соответсвии с требованиями PEP8 и добавить docstring, с использованием reStructuredText

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения заголовка проекта.
=========================================================================================

Этот модуль определяет константы проекта, такие как имя проекта, версию, авторские права и прочее,
путем считывания данных из файла настроек проекта (settings.json).

Он также предоставляет функцию для определения корневой директории проекта.

Пример использования
--------------------

Импортируйте модуль и используйте константы:

.. code-block:: python

    from src.endpoints.advertisement.facebook import header

    print(header.__project_name__)
    print(header.__version__)
"""
MODE = 'dev'

import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads
from src.logger.logger import logger
from typing import  Tuple

def set_project_root(marker_files: Tuple[str, ...] = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с директории текущего файла.

    Поиск идет вверх по дереву каталогов и останавливается в первом каталоге, содержащем
    любой из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий для идентификации корня проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если найден, иначе - директория, где находится скрипт.
    :rtype: Path
    """
    __root__: Path
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Получение корневой директории проекта
__root__ = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта"""

from src import gs

settings = None
#  код исполняет попытку загрузки настроек из файла settings.json
try:
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError) as ex:
    #  Логирование ошибки если файл не найден
    logger.error(f'Файл настроек не найден {ex}')
    ...
except json.JSONDecodeError as ex:
    #  Логирование ошибки если файл имеет неверный формат
    logger.error(f'Ошибка декодирования JSON {ex}')
    ...


doc_str = None
#  код исполняет попытку загрузки документации из файла README.MD
try:
    with open(gs.path.root / 'src' /  'README.MD', 'r') as doc_file:
        doc_str = doc_file.read()
except (FileNotFoundError) as ex:
    #  Логирование ошибки если файл не найден
    logger.error(f'Файл документации не найден {ex}')
    ...


__project_name__: str = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
"""__project_name__ (str): Имя проекта"""
__version__: str = settings.get("version", '')  if settings  else ''
"""__version__ (str): Версия проекта"""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Документация проекта"""
__details__: str = ''
"""__details__ (str): Детали проекта"""
__author__: str = settings.get("author", '')  if settings  else ''
"""__author__ (str): Автор проекта"""
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
"""__copyright__ (str): Авторские права проекта"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Сообщение о кофе"""
```