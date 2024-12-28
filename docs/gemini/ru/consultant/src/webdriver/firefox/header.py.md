# Анализ кода модуля `header.py`

**Качество кода**
9
-   Плюсы
    -   Код выполняет основную задачу - определение корневой директории проекта и загрузку настроек.
    -   Используется `pathlib` для работы с путями, что делает код кроссплатформенным.
    -   Присутствует обработка исключений при чтении файлов настроек и документации.
    -   Используются `settings.get` с значениями по умолчанию для параметров конфигурации.
-   Минусы
    -   Не используется `j_loads` или `j_loads_ns` для загрузки `json` файлов.
    -   Отсутствует логирование ошибок при загрузке файлов и в других местах.
    -   Используются стандартные блоки `try-except`, вместо `logger.error`
    -   Не все переменные и функции имеют документацию в формате RST.

**Рекомендации по улучшению**

1.  Использовать `j_loads` или `j_loads_ns` для загрузки `json` файлов.
2.  Добавить логирование ошибок с помощью `logger.error`.
3.  Заменить стандартные блоки `try-except` на обработку ошибок с помощью `logger.error`.
4.  Добавить reStructuredText (RST) docstring для модуля, функций и переменных.
5.  Добавить отсутствующие импорты.
6.  Переименовать `settings_file` в более конкретное имя `file` в блоке `try-except` для лучшей читаемости.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения корневой директории проекта и загрузки настроек.
======================================================================

Этот модуль определяет корневую директорию проекта, начиная с директории текущего файла,
и загружает настройки из файла `settings.json` и документацию из файла `README.MD`.
Использует :mod:`pathlib` для работы с путями.

Пример использования
--------------------

.. code-block:: python

    from src.webdriver.firefox.header import __root__, __project_name__, __version__, __doc__, __details__, __author__, __copyright__, __cofee__

    print(f"Root directory: {__root__}")
    print(f"Project name: {__project_name__}")
"""

MODE = 'dev'

import sys
from pathlib import Path
# from json import load #  Удаляем неиспользуемый импорт
from src.utils.jjson import j_loads #  Импортируем j_loads из src.utils.jjson
from src.logger.logger import logger #  Импортируем logger для логирования
from packaging.version import Version


def set_project_root(marker_files: tuple = ('__root__',)) -> Path:
    """
    Определяет корневой каталог проекта.

    Поиск производится вверх по структуре каталогов, начиная с директории текущего файла.
    Остановка поиска происходит при обнаружении каталога, содержащего любой из `marker_files`.

    :param marker_files: Кортеж имен файлов или директорий, которые идентифицируют корень проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу проекта.
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


# Получаем корневую директорию проекта
__root__ = set_project_root()
"""Path: Путь к корневой директории проекта."""

from src import gs

settings: dict = None
try:
    # Код открывает файл настроек 'settings.json' и загружает его содержимое
    with open(gs.path.root / 'src' / 'settings.json', 'r') as file:
        settings = j_loads(file) # Используем j_loads для загрузки JSON
except (FileNotFoundError, Exception) as ex:  # Обработка ошибок при открытии и чтении файла
    logger.error('Ошибка при загрузке файла настроек settings.json', exc_info=ex) #  Логируем ошибку
    ...

doc_str: str = None
try:
     # Код открывает файл документации 'README.MD' и читает его содержимое
    with open(gs.path.root / 'src' / 'README.MD', 'r') as file:
        doc_str = file.read()
except (FileNotFoundError, Exception) as ex: # Обработка ошибок при открытии и чтении файла
    logger.error('Ошибка при загрузке файла документации README.MD', exc_info=ex) #  Логируем ошибку
    ...


__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Название проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта."""
__details__: str = ''
"""str: Детали проекта."""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Авторские права проекта."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение о поддержке автора."""
```