# Анализ кода модуля `header.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован, используются функции для выделения логических блоков.
    - Присутствует базовая обработка ошибок при загрузке конфигурации и README.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Добавлены Docstring для функции `set_project_root`.
    - Код соответствует PEP 8 по стилю.
-  Минусы
    - Не все переменные и константы имеют docstring.
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Отсутствует импорт `logger` из `src.logger.logger`.
    - Исключения обрабатываются через `...`, что не является информативным.
    - Есть неиспользуемая переменная `settings`.

**Рекомендации по улучшению**

1.  Использовать `j_loads` вместо `json.load` для загрузки конфигурации.
2.  Добавить импорт `from src.logger.logger import logger` для логирования ошибок.
3.  Заменить `...` в блоках `except` на логирование ошибок с помощью `logger.error`.
4.  Добавить docstring для всех глобальных переменных.
5.  Удалить неиспользуемую переменную `settings`.
6.  Указать тип `Path` при объявлении `__root__`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module:: src.ai.gemini
    :platform: Windows, Unix
    :synopsis: Модуль интерфейса с моделью от Coogle - generativeai

Модуль `header` содержит настройки проекта, пути и общую информацию.
======================================================================

Этот модуль устанавливает корень проекта, загружает конфигурацию,
получает информацию из README.MD и предоставляет доступ к этим данным
через глобальные переменные.

Пример использования
--------------------

.. code-block:: python

    from src.ai.gemini.header import __project_name__, __version__

    print(f"Имя проекта: {__project_name__}")
    print(f"Версия: {__version__}")
"""
import sys
from pathlib import Path
from packaging.version import Version
# from json import load #  импортируем j_loads или j_loads_ns из src.utils.jjson вместо стандартного json.load
from src.utils.jjson import j_loads
from src.logger.logger import logger # Импортируем logger
from src import gs



def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Находит корневой каталог проекта, начиная с каталога текущего файла,
    просматривая вверх и останавливаясь на первом каталоге, содержащем любой из маркеров.

    :param marker_files: Кортеж имен файлов или каталогов для идентификации корня проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу, если найден, иначе каталог, где расположен скрипт.
    :rtype: Path

    Пример:

    >>> root = set_project_root(marker_files=('.', '.git'))
    >>> print(root)
    /path/to/your/project
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


# Get the root directory of the project
__root__:Path = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""


config: dict = None
"""config (dict): Словарь с настройками из файла config.json"""
try:
    # Код загружает конфигурацию из файла config.json
    with open(gs.path.root / 'src' / 'config.json', 'r') as f:
        config = j_loads(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логируем ошибку, если файл не найден или не удается декодировать JSON
    logger.error(f"Ошибка при загрузке конфигурационного файла: {e}")

doc_str: str = None
"""doc_str (str): Содержимое файла README.MD"""
try:
    # Код читает содержимое файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логируем ошибку, если файл не найден или не удается прочитать файл
    logger.error(f"Ошибка при загрузке файла README.MD: {e}")


__project_name__: str = config.get("project_name", 'hypotez') if config else 'hypotez'
"""__project_name__ (str): Имя проекта, по умолчанию 'hypotez'."""
__version__: str = config.get("version", '') if config else ''
"""__version__ (str): Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Содержимое файла README.MD."""
__details__: str = ''
"""__details__ (str): Детали проекта."""
__author__: str = config.get("author", '') if config else ''
"""__author__ (str): Автор проекта."""
__copyright__: str = config.get("copyrihgnt", '') if config else ''
"""__copyright__ (str): Информация об авторских правах."""
__cofee__: str = "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Сообщение для поддержки разработчика."""
```