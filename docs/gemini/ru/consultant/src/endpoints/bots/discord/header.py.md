# Анализ кода модуля `header.py`

**Качество кода**
9
-  Плюсы
    - Код содержит docstring для модуля и функции `set_project_root`.
    - Используется `pathlib.Path` для работы с путями.
    - Присутствует обработка ошибок при чтении файлов конфигурации.
    - Код определяет корневую директорию проекта.
    - Используются переменные окружения.
-  Минусы
    -  Используется `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -  Не все строки задокументированы в формате reStructuredText (RST).
    -  Присутствуют множественные пустые docstring.
    -  Обработка ошибок при чтении файлов не использует логирование.
    -  Не используются f-строки для форматирования строк.
    -  Избыточное использование `try-except` без логирования.
    - Не используются `logger`.
    - Присутствует дублирование кода.

**Рекомендации по улучшению**

1.  Использовать `j_loads` или `j_loads_ns` для загрузки JSON файлов.
2.  Переписать docstring в формате RST для всех сущностей.
3.  Использовать `from src.logger.logger import logger` для логирования ошибок.
4.  Избегать использования `...` в коде, заменяя их на `pass` или логирование.
5.  Убрать дублирование кода и лишние комментарии.
6.  Добавить f-строки для форматирования.
7.  Переписать комментарии после `#` для подробного объяснения кода.
8. Добавить проверку на `settings` перед использованием `settings.get`.
9. Избегать дублирования кода.
10. Заменить `json.JSONDecodeError` на `json.decoder.JSONDecodeError` для большей конкретики

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для определения заголовков и метаданных проекта.
========================================================

Этот модуль определяет основные метаданные проекта, такие как имя, версия, автор и т.д.
Также определяет корневую директорию проекта.

.. code-block:: python

    from src.bots.discord.header import __version__, __project_name__
    print(__version__)
    print(__project_name__)
"""
import sys
from pathlib import Path
import json
from packaging.version import Version
from src.utils.jjson import j_loads
from src.logger.logger import logger


"""
    Режим работы приложения (dev/prod).
    :type: str
"""


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла,
    поднимаясь вверх по иерархии каталогов до первого каталога, содержащего любой из
    маркерных файлов.

    :param marker_files: Кортеж имен файлов или директорий, которые идентифицируют корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
    :rtype: Path
    """
    current_path: Path = Path(__file__).resolve().parent
    __root__: Path = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if str(__root__) not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Получаем корневую директорию проекта
__root__ = set_project_root()
"""
    Корневая директория проекта.
    :type: Path
"""

from src import gs

settings: dict = None
# Пытаемся загрузить настройки из файла settings.json
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r', encoding='utf-8') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
    logger.error(f'Ошибка при чтении файла настроек {e}', exc_info=True)
    settings = {}


doc_str: str = None
# Пытаемся загрузить документацию из файла README.MD
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as doc_file:
        doc_str = doc_file.read()
except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
    logger.error(f'Ошибка при чтении файла документации {e}', exc_info=True)
    doc_str = ''


__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""
    Имя проекта.
    :type: str
"""
__version__: str = settings.get("version", '') if settings else ''
"""
    Версия проекта.
    :type: str
"""
__doc__: str = doc_str if doc_str else ''
"""
    Описание проекта.
    :type: str
"""
__details__: str = ''
"""
    Детальная информация о проекте.
    :type: str
"""
__author__: str = settings.get("author", '') if settings else ''
"""
    Автор проекта.
    :type: str
"""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""
    Авторские права проекта.
    :type: str
"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""
    Сообщение для поддержки разработчика.
    :type: str
"""
```