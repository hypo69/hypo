# Анализ кода модуля header.py

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и легко читается.
    - Используется `pathlib` для работы с путями, что делает код более кросс-платформенным.
    - Присутствует обработка исключений при загрузке настроек и документации.
    - Функция `set_project_root` выполняет свою задачу по определению корня проекта.
    - Используются константы для хранения имен файлов и путей.
    - Документация модуля в целом присутствует.

- Минусы
    - В коде отсутствуют docstring для модуля в формате reStructuredText (RST).
    - Отсутствуют docstring для всех переменных
    - Не используется `j_loads` или `j_loads_ns` для загрузки JSON.
    - Исключения обрабатываются с помощью `...`, что усложняет отладку.
    - Некоторые переменные не имеют аннотаций типов.
    - Константы такие как `MODE` не используются в коде.
    - Отсутсвует `from src.logger.logger import logger` для логирования ошибок.
    - Есть проблема в блоке `try-except`.
     

**Рекомендации по улучшению**

1. Добавить docstring в формате RST для модуля и переменных.
2. Использовать `j_loads` или `j_loads_ns` для загрузки JSON.
3. Заменить `...` на логирование ошибок с помощью `logger.error`.
4. Добавить аннотации типов для переменных.
5. Использовать `from src.logger.logger import logger` для логирования ошибок.
6. Оптимизировать код для `try-except` блоков с помощью `logger.error`.
7. Удалить неиспользуемую переменную MODE.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения корневого каталога проекта и загрузки настроек.
===================================================================

Этот модуль определяет корневой каталог проекта, начиная с каталога текущего файла,
путем поиска вверх по дереву каталогов до первого каталога, содержащего один из
маркерных файлов (например, 'pyproject.toml', 'requirements.txt', '.git').
Также загружает настройки из файла 'settings.json' и документацию из 'README.MD',
и предоставляет доступ к основным данным проекта.

Пример использования:
--------------------

.. code-block:: python

    from src.logger.header import __root__, __project_name__, __version__

    print(f"Корневой каталог проекта: {__root__}")
    print(f"Имя проекта: {__project_name__}")
    print(f"Версия проекта: {__version__}")
"""

import sys
# from src.utils.jjson import j_loads # TODO: заменить на j_loads, если нужно будет парсить json
from json import JSONDecodeError, load
from pathlib import Path
from packaging.version import Version
from src.logger.logger import logger # импорт логера
from src import gs

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определение корневого каталога проекта.

    Функция выполняет поиск корневого каталога проекта, начиная с каталога,
    в котором находится текущий файл. Поиск идет вверх по дереву каталогов до
    первого каталога, содержащего один из файлов, указанных в `marker_files`.
    Если ни один из маркеров не найден, то возвращается каталог, где находится
    файл. Добавляет корневой путь в `sys.path`.

    :param marker_files: Кортеж с именами файлов или каталогов, которые служат маркерами корневого каталога.
    :type marker_files: tuple
    :return: Путь к корневому каталогу проекта.
    :rtype: Path
    """
    current_path: Path = Path(__file__).resolve().parent
    __root__: Path = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Получение корневого каталога проекта
__root__: Path = set_project_root()
"""Path: Путь к корневому каталогу проекта."""

settings: dict = None
"""dict: Словарь с настройками проекта."""
try:
    #  код исполняет загрузку настроек из файла settings.json
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = load(settings_file) # TODO: заменить на j_loads
except (FileNotFoundError, JSONDecodeError) as e:
     # Логирование ошибки, если файл не найден или имеет неверный формат
    logger.error(f'Не удалось загрузить настройки из файла settings.json: {e}')
    settings = {}  # TODO: добавить загрузку из os.environ


doc_str: str = None
"""str: Строка с документацией проекта."""
try:
    # Код загружает документацию из файла README.MD
    with open(gs.path.root / 'src' /  'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, JSONDecodeError) as e:
    #  Логирование ошибки, если файл не найден
    logger.error(f'Не удалось загрузить документацию из файла README.MD: {e}')
    doc_str = ''


__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Имя проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта."""
__details__: str = ''
"""str: Детали проекта."""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Копирайт проекта."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение для поддержки проекта."""
```