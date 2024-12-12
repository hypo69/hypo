# Анализ кода модуля `header`

**Качество кода**
9
-  Плюсы
    - Код имеет хорошую структуру и логику.
    - Используется `pathlib` для работы с путями, что делает код более читаемым и кроссплатформенным.
    - Присутствуют комментарии, объясняющие назначение функций.
    - Код обрабатывает исключения, возникающие при открытии файлов.
 -  Минусы
    - Отсутствуют docstring у модуля.
    - Не используется `j_loads` или `j_loads_ns` для загрузки JSON.
    - Некоторые переменные не имеют docstring.
    - Отсутствуют импорты модулей `sys` и `json` в начале файла.
    - Не используется логирование ошибок с помощью `src.logger.logger`.
    - Не все переменные, используемые в глобальной области, документированы.
    - Присутствует избыточное использование `try-except` без логирования ошибки.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля с подробным описанием его назначения.
2.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для загрузки JSON файлов.
3.  Добавить docstring для всех функций и переменных.
4.  Импортировать модули `sys` и `json`.
5.  Заменить избыточное использование `try-except` на логирование ошибок с помощью `logger.error`.
6.  Добавить подробные комментарии с использованием reStructuredText (RST) для всех функций и методов.
7.  Заменить стандартный `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
8.  Добавить тип `Path` для переменной `__root__` в `set_project_root`.
9.  Добавить логирование ошибок с помощью `logger.error` и `logger.debug` для лучшей отладки.
10. Добавить обработку ситуации, когда `settings` и `doc_str` остаются `None`.

**Оптимизиробанный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль `header` - инициализация проекта и загрузка настроек.
=========================================================================================

Этот модуль выполняет поиск корневой директории проекта, загружает настройки из `settings.json` и `README.md`,
а также определяет основные глобальные переменные проекта, такие как имя, версия и автор.
Используется для централизованного управления и инициализации основных параметров проекта.

.. code-block:: python

    from src.suppliers.aliexpress.campaign.header import __project_name__, __version__, __doc__, __author__, __copyright__, __cofee__

Пример использования
--------------------

Импортируйте этот модуль для доступа к глобальным переменным проекта.

.. code-block:: python

    import src.suppliers.aliexpress.campaign.header as header

    print(header.__project_name__)
"""
import sys
import json
from pathlib import Path
from typing import Tuple, Any
from src.utils.jjson import j_loads
from src.logger.logger import logger
from src import gs



MODE = 'dev'
"""Режим работы модуля (например, 'dev', 'prod')."""



def set_project_root(marker_files: Tuple[str, ...] =('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории, в которой находится текущий файл.
    Поиск осуществляется вверх по дереву каталогов до тех пор, пока не будет найдена директория,
    содержащая один из файлов-маркеров.

    :param marker_files: Кортеж с именами файлов или директорий, которые служат маркерами корневой директории проекта.
    :type marker_files: Tuple[str, ...]
    :return: Путь к корневой директории проекта. Если корневая директория не найдена, возвращается директория, где расположен скрипт.
    :rtype: Path
    """
    __root__: Path #  Объявление переменной для корневой директории
    current_path: Path = Path(__file__).resolve().parent #  Получение абсолютного пути к директории текущего файла
    __root__ = current_path #  Начальное значение корневой директории - текущая директория
    for parent in [current_path] + list(current_path.parents): # Итерация по текущей и родительским директориям
        if any((parent / marker).exists() for marker in marker_files):# Проверка наличия одного из маркерных файлов в текущей директории
            __root__ = parent # Если маркерный файл найден, то текущая родительская директория становится корневой
            break
    if __root__ not in sys.path:# Проверка, добавлена ли корневая директория в sys.path
        sys.path.insert(0, str(__root__))# Добавление корневой директории в sys.path для корректного импорта модулей
    return __root__


# Получение корневой директории проекта
__root__: Path = set_project_root()
"""
:meta hide-value:
Путь к корневой директории проекта.
"""


settings: dict = None
"""
:meta hide-value:
Словарь с настройками проекта, загруженными из `settings.json`.
"""
try:
    #  Код загружает настройки из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r', encoding='utf-8') as settings_file:
        settings = j_loads(settings_file) #  Использование j_loads для загрузки JSON
except FileNotFoundError:
     #  Логирование ошибки, если файл settings.json не найден
    logger.error(f'Файл settings.json не найден по пути {gs.path.root / "src" / "settings.json"}')
except json.JSONDecodeError as e:
     #  Логирование ошибки, если файл settings.json имеет неверный формат
    logger.error(f'Ошибка декодирования JSON в файле settings.json: {e}')
except Exception as ex:
     #  Логирование других возможных ошибок
    logger.error(f'Непредвиденная ошибка при загрузке settings.json: {ex}')


doc_str: str = None
"""
:meta hide-value:
Строка с содержимым файла `README.MD`.
"""
try:
    #  Код читает содержимое файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as settings_file:
        doc_str = settings_file.read()
except FileNotFoundError:
    #  Логирование ошибки, если файл README.MD не найден
    logger.error(f'Файл README.MD не найден по пути {gs.path.root / "src" / "README.MD"}')
except Exception as ex:
    #  Логирование других возможных ошибок
    logger.error(f'Непредвиденная ошибка при чтении README.MD: {ex}')

__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""Имя проекта. Значение по умолчанию 'hypotez'."""
__version__: str = settings.get("version", '') if settings else ''
"""Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""Описание проекта, взятое из файла `README.md`."""
__details__: str = ''
"""Дополнительные детали проекта."""
__author__: str = settings.get("author", '') if settings else ''
"""Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""Информация об авторских правах проекта."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""Сообщение для поддержки разработчика."""
```