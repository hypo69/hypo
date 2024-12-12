# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    - Код выполняет свою основную задачу - определяет корень проекта и загружает настройки.
    - Используется `pathlib` для работы с путями, что делает код более читаемым и кроссплатформенным.
    - Есть обработка исключений при чтении файлов, что предотвращает сбои программы.
    - Документация в формате docstring для функции `set_project_root`.

-  Минусы
    - Не используется `j_loads` или `j_loads_ns` для загрузки JSON, как указано в инструкции.
    - Присутствуют множественные try-except блоки, которые можно упростить.
    - Отсутствует логирование ошибок.
    - Много переменных  определены  на уровне модуля, что может усложнить поддержку.
    - Не все переменные имеют docstring.
    -  `__file__`  используется не безопасно при packag-е.
    -  Отсутствует описание модуля.
    -  Присутсвуют не безопасные try except.
    - Использования `...` как заглушки.

**Рекомендации по улучшению**

1.  Использовать `j_loads` или `j_loads_ns` для загрузки `settings.json`.
2.  Добавить логирование ошибок с помощью `src.logger.logger.error`.
3.  Улучшить обработку исключений, избегая `try-except` без конкретной обработки.
4.  Добавить docstring для всех переменных, включая `__root__`, `settings`, `doc_str`, `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`.
5.  Добавить описание модуля в формате reStructuredText (RST).
6.  Убрать  `...` и добавить обработку исключения
7.  Использовать `__package__` для определения корня проекта.
8.  Проверить  `copyrihgnt`  на опечатку
9.  Убрать `#! venv/Scripts/python.exe` , `#! venv/bin/python/python3.12` тк она не несет никакой нагрузки
10. Присвоить `__root__` значение по умолчанию `Path('./')`

**Оптимизированный код**

```python
"""
Модуль для определения настроек проекта.
=========================================================================================

Этот модуль отвечает за определение корня проекта, загрузку основных настроек и
предоставление доступа к метаданным проекта.

Основные функции:
    - :func:`set_project_root`: определяет корень проекта.

Переменные модуля:
    - __root__ (Path): Корневой каталог проекта.
    - settings (dict): Словарь с настройками проекта из файла `settings.json`.
    - doc_str (str): Строка с содержимым файла `README.md`.
    - __project_name__ (str): Название проекта.
    - __version__ (str): Версия проекта.
    - __doc__ (str): Описание проекта.
    - __details__ (str): Дополнительные детали проекта.
    - __author__ (str): Автор проекта.
    - __copyright__ (str): Информация об авторских правах.
    - __cofee__ (str): Сообщение с приглашением поддержать разработчика.

Пример использования
--------------------

Импортируйте модуль и используйте переменные для получения информации о проекте.

.. code-block:: python

    from src.suppliers.morlevi import header

    print(f"Название проекта: {header.__project_name__}")
    print(f"Версия проекта: {header.__version__}")
"""
# -*- coding: utf-8 -*-
import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads
from src.logger.logger import logger
from typing import Optional

MODE = 'dev'

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневой каталог проекта, начиная с директории текущего файла,
    поиском вверх по структуре директорий до первой директории, содержащей
    один из указанных файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий, которые используются для идентификации корня проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если найден, иначе директория, где расположен скрипт.
    :rtype: Path
    """
    __root__:Path = Path('./')
    current_path: Path = Path(__file__).resolve().parent if __package__ is None else Path(__package__).resolve().parent
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if str(__root__) not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__

# Получение корневой директории проекта
__root__: Path = set_project_root()
"""Path: Путь к корневой директории проекта."""

from src import gs

settings: Optional[dict] = None
"""dict: Словарь с настройками проекта из файла `settings.json`."""
try:
    # Код загружает настройки из файла settings.json, используя j_loads
    with open(gs.path.root / 'src' / 'settings.json', 'r', encoding='utf-8') as settings_file:
        settings = j_loads(settings_file)
except FileNotFoundError as e:
    # Логирование ошибки, если файл не найден
    logger.error(f'Файл настроек не найден: {e}')
except Exception as e:
    # Логирование ошибки, если произошла ошибка при загрузке JSON
    logger.error(f'Ошибка при загрузке настроек из JSON: {e}')

doc_str: Optional[str] = None
"""str: Строка с содержимым файла `README.md`."""
try:
    # Код читает содержимое файла README.md
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as readme_file:
        doc_str = readme_file.read()
except FileNotFoundError as e:
    # Логирование ошибки, если файл не найден
    logger.error(f'Файл README.md не найден: {e}')
except Exception as e:
    # Логирование ошибки, если произошла ошибка при чтении файла
    logger.error(f'Ошибка при чтении файла README.md: {e}')


__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Название проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Описание проекта."""
__details__: str = ''
"""str: Дополнительные детали проекта."""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyright", '') if settings else '' # fix typo copyrihgnt -> copyright
"""str: Информация об авторских правах."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение с приглашением поддержать разработчика."""
```