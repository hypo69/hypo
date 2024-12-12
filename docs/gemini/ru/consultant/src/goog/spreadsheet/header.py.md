# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    - Код корректно определяет корневую директорию проекта.
    - Используется `pathlib` для работы с путями, что повышает читаемость и кроссплатформенность кода.
    - Присутствует обработка исключений при загрузке `settings.json` и `README.MD`.
    - Используются константы `__project_name__`, `__version__`, `__doc__`, `__author__`, `__copyright__`, `__cofee__` для хранения данных о проекте.
-  Минусы
    -  Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения JSON файлов.
    -  Отсутствует логирование ошибок при загрузке файлов, что затрудняет отладку.
    -  Комментарии в начале файла не соответствуют стандарту RST.
    -  Использование `...` в блоках `except` неинформативно.
    -  Не все переменные имеют аннотации типов.
    -  Отсутствует  документация в формате RST для функций, переменных и модуля.

**Рекомендации по улучшению**

1.  Использовать `j_loads` или `j_loads_ns` для чтения JSON файлов.
2.  Добавить логирование ошибок с помощью `logger.error` при возникновении исключений при загрузке файлов.
3.  Переписать комментарии в начале файла в формате reStructuredText (RST).
4.  Заменить `...` на более информативное логирование или обработку ошибок.
5.  Добавить аннотации типов для всех переменных, где это возможно.
6.  Добавить docstring в формате RST для модуля, функций и переменных.
7.  Использовать `from src.logger.logger import logger` для логирования.
8.  Оптимизировать блок `try-except` для более читаемого и эффективного кода.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения корневой директории проекта и загрузки основных настроек.
==============================================================================

Этот модуль содержит функции для автоматического определения корневой директории проекта,
загрузки настроек из файла `settings.json` и чтения документации из файла `README.MD`.

Использует модуль :mod:`pathlib` для работы с путями, что обеспечивает кроссплатформенность.

Пример использования
--------------------

.. code-block:: python

    from src.goog.spreadsheet.header import __project_name__, __version__

    print(f"Имя проекта: {__project_name__}")
    print(f"Версия проекта: {__version__}")
"""

import sys
from pathlib import Path
from packaging.version import Version
# код добавляет импорт j_loads_ns из src.utils.jjson
from src.utils.jjson import j_loads_ns
# код добавляет импорт logger из src.logger.logger
from src.logger.logger import logger

MODE = 'dev'
def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с директории текущего файла.

    Поиск ведется вверх по дереву каталогов до первого каталога, содержащего один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов, идентифицирующих корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если она найдена, иначе путь к директории, где расположен скрипт.
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

# Код выполняет поиск корневой директории проекта
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта."""

from src import gs

settings: dict = None
# Код пытается открыть и прочитать файл настроек settings.json
try:
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        # Код использует j_loads_ns для загрузки JSON
        settings = j_loads_ns(settings_file)
except FileNotFoundError as e:
    # Код логирует ошибку, если файл settings.json не найден
    logger.error(f'Файл settings.json не найден: {e}')
except json.JSONDecodeError as e:
    # Код логирует ошибку, если файл settings.json не удалось декодировать
    logger.error(f'Ошибка декодирования JSON в файле settings.json: {e}')

doc_str: str = None
# Код пытается открыть и прочитать файл README.MD
try:
    with open(gs.path.root / 'src' /  'README.MD', 'r') as settings_file:
        # Код читает содержимое файла
        doc_str = settings_file.read()
except FileNotFoundError as e:
    # Код логирует ошибку, если файл README.MD не найден
    logger.error(f'Файл README.MD не найден: {e}')
except Exception as e:
    # Код логирует ошибку при возникновении других исключений
    logger.error(f'Произошла ошибка при чтении файла README.MD: {e}')

# Код извлекает данные из settings, если они доступны, иначе устанавливает значения по умолчанию
__project_name__: str = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
"""__project_name__ (str): Имя проекта."""
__version__: str = settings.get("version", '')  if settings  else ''
"""__version__ (str): Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Строка документации проекта."""
__details__: str = ''
"""__details__ (str): Детали проекта (по умолчанию пустая строка)."""
__author__: str = settings.get("author", '')  if settings  else ''
"""__author__ (str): Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
"""__copyright__ (str): Информация об авторских правах."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Сообщение с призывом угостить разработчика кофе."""
```