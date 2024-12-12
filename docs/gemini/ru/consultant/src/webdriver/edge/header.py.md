# Анализ кода модуля `header.py`

**Качество кода**
9
-  Плюсы
    - Код содержит docstring для модуля.
    -  Функция `set_project_root` имеет docstring.
    -  Используются константы для хранения информации о проекте.
    -  Код выполняет проверку на наличие файла настроек и README.md.
    -  Используется `Path` из модуля `pathlib`.
    - Код соответствует PEP8.
-  Минусы
    -   Используется `json.load` вместо `j_loads` или `j_loads_ns`.
    -  Не все переменные имеют docstring.
    -  Избыточное использование `try-except` без логирования ошибок.
    -  Не используется `from src.logger.logger import logger`.
    -  Отсутствуют некоторые импорты.

**Рекомендации по улучшению**

1.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо `json.load`.
2.  Добавить docstring для переменных `settings`, `doc_str`, `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`.
3.  Использовать `from src.logger.logger import logger` для логирования ошибок при чтении файлов.
4.  Заменить блоки `try-except` на более компактную обработку ошибок через `logger.error`.
5.  Добавить импорт `from src.utils.jjson import j_loads`.
6.  Переписать комментарии в формате reStructuredText (RST).
7.  Улучшить форматирование кода, приведя его к единому стилю.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения и хранения глобальных настроек проекта.
=============================================================

Этот модуль определяет корневой каталог проекта, загружает настройки из файла `settings.json` и
содержит информацию о проекте, такую как имя, версия, автор и т.д.

Пример использования
--------------------

.. code-block:: python

    from src.webdriver.edge import header

    print(header.__project_name__)
    print(header.__version__)
"""

import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads # Импорт j_loads для чтения JSON
from src.logger.logger import logger # Импорт logger для логирования

MODE = 'dev'
"""str: Режим работы приложения"""

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневой каталог проекта, начиная с текущего файла,
    поиском вверх по директориям, останавливаясь на первой директории,
    содержащей любой из файлов-маркеров.

    :param marker_files: Список файлов или директорий, идентифицирующих корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
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


# Получение корневого каталога проекта
__root__ = set_project_root()
"""Path: Путь к корневому каталогу проекта"""

from src import gs

settings: dict = None
"""dict: Словарь с настройками проекта, загруженными из 'settings.json'."""
try:
    # Код загружает настройки проекта из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as ex:
    logger.error(f'Ошибка при чтении файла настроек: {ex}')
    ...

doc_str: str = None
"""str: Строка с содержимым файла README.md."""
try:
    # Код загружает содержимое файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as ex:
    logger.error(f'Ошибка при чтении файла README.MD: {ex}')
    ...


__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
"""str: Имя проекта."""
__version__: str = settings.get("version", '')  if settings  else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Содержимое файла README.md."""
__details__: str = ''
"""str: Детали проекта."""
__author__: str = settings.get("author", '')  if settings  else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
"""str: Авторское право проекта."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение о поддержке разработчика."""
```