# Анализ кода модуля `header.py`

**Качество кода**
8
- Плюсы
    - Код выполняет основную задачу: определяет корень проекта, загружает настройки и устанавливает глобальные переменные.
    - Используется `pathlib` для работы с путями, что делает код более читаемым и кроссплатформенным.
    - Присутствует обработка исключений при чтении файлов настроек и документации.
    - Есть логика определения корневой директории проекта на основе маркеров.
    - Установлены основные метаданные проекта.
- Минусы
    - Отсутствуют docstring для модуля, переменных и функций, что затрудняет понимание кода.
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Обработка ошибок `try-except` для `FileNotFoundError` и `json.JSONDecodeError` выполняется без логирования.
    - Переменная `__root__` объявлена с типом `Path` до присвоения ей значения.
    - Не используются f-строки для форматирования строк.
    - Не все переменные имеют аннотации типов.
    - Не все импорты используются или в начале модуля, не в конце.
    - Присутствует избыточное использование `if settings  else`.
    - Использование `...` в `except` блоках неинформативно.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля, функции `set_project_root` и глобальных переменных.
2.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения `settings.json`.
3.  Заменить `json.load` на `j_loads` или `j_loads_ns`.
4.  В `try-except` добавить логирование ошибок с помощью `logger.error` вместо `...`.
5.  Убрать избыточное использование `if settings else` с помощью тернарного оператора.
6.  Переместить import `gs` в начало файла.
7.  Использовать f-строки для форматирования строк.
8.  Присвоить переменным `__root__` аннотацию типа сразу при инициализации.
9.  Убрать неиспользуемые импорты `sys` и `Version`
10.  Вынести константу `COFEE_DEFAULT_MESSAGE`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для определения корневой директории проекта и загрузки основных настроек.
=========================================================================================

Этот модуль содержит функции и переменные для определения корневой директории проекта,
загрузки настроек из файла `settings.json` и установки глобальных переменных для использования в проекте.

Пример использования
--------------------

.. code-block:: python

    from src.goog.header import __root__, __project_name__, __version__

    print(__root__)
    print(__project_name__)
    print(__version__)
"""

import sys # not use
import json # TODO: remove import
from packaging.version import Version # not use
from pathlib import Path
from src.utils.jjson import j_loads
from src.logger.logger import logger
from src import gs


COFEE_DEFAULT_MESSAGE = "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Находит корневой каталог проекта, начиная с каталога текущего файла,
    поиск идет вверх и останавливается в первом каталоге, содержащем любой из файлов маркеров.

    :param marker_files: Кортеж имен файлов или каталогов для идентификации корня проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу, если он найден, иначе - каталог, где находится скрипт.
    :rtype: Path
    """
    __root__:Path = Path(__file__).resolve().parent
    # Итерируем по текущему пути и его родительским каталогам.
    for parent in [__root__] + list(__root__.parents):
        # Проверяем наличие любого из файлов маркеров в текущем каталоге.
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    # Если корневой каталог не в sys.path, добавляем его.
    if str(__root__) not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__

# Получаем корневой каталог проекта.
__root__: Path = set_project_root()
"""Path: Путь к корневому каталогу проекта."""

settings: dict = None
# Пытаемся прочитать файл настроек.
try:
    # код исполняет чтение файла настроек
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as ex:
    # Логируем ошибку, если файл не найден или невалидный JSON.
    logger.error('Ошибка при загрузке settings.json', ex)

doc_str: str = None
# Пытаемся прочитать файл README.MD.
try:
    # Код исполняет чтение файла README.MD
    with open(gs.path.root / 'src' /  'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as ex:
    # Логируем ошибку, если файл не найден или невалидный JSON.
    logger.error('Ошибка при загрузке README.MD', ex)


__project_name__: str = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
"""str: Название проекта, по умолчанию 'hypotez'."""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта, по умолчанию ''. """
__doc__: str = doc_str if doc_str else ''
"""str: Содержимое файла README.MD, по умолчанию ''. """
__details__: str = ''
"""str: Детали проекта, по умолчанию ''. """
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта, по умолчанию ''. """
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Информация об авторских правах проекта, по умолчанию ''. """
__cofee__: str = settings.get("cofee", COFEE_DEFAULT_MESSAGE) if settings else COFEE_DEFAULT_MESSAGE
"""str: Сообщение для поддержки разработчика, по умолчанию 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'."""
```