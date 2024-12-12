# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    - Код структурирован и разделен на логические блоки.
    - Используется функция `set_project_root` для определения корня проекта, что улучшает переносимость кода.
    - Параметры проекта вынесены в `settings.json`, что позволяет легко их менять.
-  Минусы
    - Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Отсутствуют docstring для переменных.
    - Используются `try-except` блоки с `...` вместо логирования.
    - Не хватает комментариев в формате RST.
    - Не хватает импортов из `src.logger.logger`.

**Рекомендации по улучшению**

1.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо `json.load` для загрузки `settings.json`.
2.  Добавить docstring для всех переменных, включая `__root__`, `settings`, `doc_str`, `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`.
3.  Заменить блоки `try-except` с `...` на логирование ошибок через `logger.error`.
4.  Добавить комментарии в формате RST для функций, переменных и модуля.
5.  Импортировать `logger` из `src.logger.logger`.
6.  Избегать дублирования кода в блоках `try` по чтению `settings.json` и `README.MD`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для настройки и инициализации проекта.
=========================================================================================

Этот модуль выполняет начальную настройку проекта, включая определение корневой директории,
загрузку настроек из `settings.json` и чтение документации из `README.MD`.

Пример использования
--------------------

.. code-block:: python

    from src.scenario import header

    # Доступ к переменным проекта:
    print(header.__project_name__)
    print(header.__version__)
"""

MODE = 'dev'

import sys
from pathlib import Path
#  импортируем j_loads_ns из src.utils.jjson
from src.utils.jjson import j_loads_ns
# импортируем logger
from src.logger.logger import logger
from packaging.version import Version


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневой каталог проекта.

    Начиная с каталога текущего файла, поиск вверх по иерархии каталогов
    до первого каталога, содержащего любой из файлов-маркеров.

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


#  Определение корневой директории проекта
__root__: Path = set_project_root()
"""
Path:  Путь к корневому каталогу проекта.
"""


from src import gs

settings: dict = None
"""dict:  Словарь настроек проекта, загруженных из `settings.json`."""
try:
    #  Загрузка настроек из settings.json с использованием j_loads_ns
    settings = j_loads_ns(gs.path.root / 'src' / 'settings.json')
except (FileNotFoundError, Exception) as ex:
    #  Логирование ошибки, если файл не найден или произошла ошибка декодирования
    logger.error(f'Не удалось загрузить настройки из файла {gs.path.root / "src" / "settings.json"}', exc_info=ex)
    ...

doc_str: str = None
"""str: Строка документации, загруженная из `README.MD`."""
try:
    #  Чтение файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as doc_file:
        doc_str = doc_file.read()
except (FileNotFoundError, Exception) as ex:
    # Логирование ошибки, если файл не найден или произошла ошибка чтения
    logger.error(f'Не удалось загрузить документацию из файла {gs.path.root / "src" / "README.MD"}', exc_info=ex)
    ...
 

__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Имя проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта."""
__details__: str = ''
"""str: Детали проекта (пока не определены)."""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Информация об авторских правах."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение о поддержке разработчика."""
```