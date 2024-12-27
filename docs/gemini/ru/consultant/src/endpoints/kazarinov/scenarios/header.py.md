# Анализ кода модуля `header.py`

**Качество кода**
**7**
-  Плюсы
    - Код содержит docstring для модуля и функции `set_project_root`.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Код корректно добавляет корневую директорию проекта в `sys.path`.
    - Код обрабатывает ошибки при чтении файлов `settings.json` и `README.MD`.
    - Используется `get` с значениями по умолчанию для избежания ошибок при отсутсвии ключей в `settings`.
    - Код использует константы `MODE` и `marker_files` для настройки.
-  Минусы
    - Отсутствует использование `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения JSON файлов.
    - Отсутствует логирование ошибок с помощью `from src.logger.logger import logger`.
    -  Использование `...` как заглушки не является лучшей практикой, особенно для production.
    -  Отсутствует документация в формате RST для переменных модуля.
    -  В блоках `try/except` используется `...` вместо корректной обработки исключений.
    -   Комментарии не приведены к формату RST.
    -   В комментариях отсутствуют подробные объяснения для кода.
    -   Не все переменные имеют docstring.

**Рекомендации по улучшению**

1.  Использовать `j_loads` из `src.utils.jjson` вместо стандартного `json.load` для чтения JSON файлов.
2.  Добавить импорт `from src.logger.logger import logger` и использовать его для логирования ошибок.
3.  Заменить `...` в блоках `try/except` на логирование ошибок с помощью `logger.error`.
4.  Добавить docstring в формате RST для всех переменных модуля.
5.  Преобразовать комментарии в формат RST.
6.  Добавить подробные объяснения для каждого блока кода в комментариях после `#`.
7.  Удалить неиспользуемый импорт `MODE`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для определения настроек проекта и версий.
=========================================================================================

Этот модуль определяет корневую директорию проекта, загружает настройки из JSON-файла,
читает документацию из README.MD и устанавливает глобальные переменные проекта,
такие как имя, версия, автор и прочее.

Использование
-------------

Пример:

.. code-block:: python

    from src.endpoints.kazarinov.scenarios import header

    print(header.__project_name__)
    print(header.__version__)
"""

import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads # импортируем j_loads
from src.logger.logger import logger # импортируем logger


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневой каталог проекта, начиная с каталога текущего файла,
    просматривая вверх и останавливаясь на первом каталоге, содержащем любой из маркерных файлов.

    :param marker_files: Кортеж имен файлов или каталогов для идентификации корня проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу, если он найден, иначе каталог, где находится скрипт.
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


# Получаем корневой каталог проекта
__root__: Path = set_project_root()
"""
:type: Path
:var __root__: Путь к корневому каталогу проекта.
"""

from src import gs

settings: dict = None
"""
:type: dict
:var settings: Словарь с настройками проекта.
"""
try:
    # Код исполняет чтение настроек из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file) # используем j_loads для загрузки json
except FileNotFoundError as e:
    # Логируем ошибку, если файл не найден
    logger.error(f'Файл настроек settings.json не найден: {e}')
    settings = {}
except Exception as e:
    # Логируем ошибку, если произошла ошибка при чтении json
    logger.error(f'Ошибка при чтении файла настроек settings.json: {e}')
    settings = {}


doc_str: str = None
"""
:type: str
:var doc_str: Строка с содержимым файла README.MD.
"""
try:
    # Код исполняет чтение документации из файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except FileNotFoundError as e:
    # Логируем ошибку, если файл не найден
    logger.error(f'Файл документации README.MD не найден: {e}')
    doc_str = ''
except Exception as e:
    # Логируем ошибку, если произошла ошибка при чтении файла
    logger.error(f'Ошибка при чтении файла README.MD: {e}')
    doc_str = ''


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
:var __copyright__: Информация о копирайте проекта.
"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""
:type: str
:var __cofee__: Ссылка на поддержку разработчика.
"""

```