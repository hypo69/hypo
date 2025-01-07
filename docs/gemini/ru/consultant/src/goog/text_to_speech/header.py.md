# Анализ кода модуля `header.py`

**Качество кода**
5
- Плюсы
    - Код структурирован,  используются константы и переменные для хранения основных настроек проекта.
    - Присутствует функция `set_project_root`, предназначенная для определения корневой директории проекта.
    - Используется `try-except` для обработки ошибок при загрузке `settings.json` и `README.MD`.
- Минусы
    -  Отсутствует документация в формате reStructuredText (RST).
    -  Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -  Использование `...` вместо обработки ошибок может затруднить отладку.
    -  Не используется логгер для регистрации ошибок.
    -  Не все импорты используются.
    -  Переменные, такие как `doc_str`  не документированы.
    -  Наличие магических строк в коде.

**Рекомендации по улучшению**

1.  **Документация**:
    - Добавить docstring в формате reStructuredText (RST) для модуля, функций и переменных.
2.  **Импорты**:
    -  Добавить `from src.utils.jjson import j_loads` для загрузки JSON файлов.
    -  Добавить `from src.logger.logger import logger` для логирования.
3.  **Загрузка JSON**:
    - Использовать `j_loads` из `src.utils.jjson` вместо стандартного `json.load`.
4.  **Обработка ошибок**:
    - Заменить `...` на `logger.error` для регистрации ошибок и корректной их обработки.
5.  **Переменные**:
    - Добавить аннотацию типов для всех переменных.
6.  **Магические строки**:
    - Вынести магические строки в константы.
7.  **Логирование**:
    - Добавить логирование успешной загрузки файла.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для инициализации проекта и загрузки настроек.
====================================================

Этот модуль определяет константы и переменные, необходимые для работы всего проекта.
Он также устанавливает корневую директорию проекта и загружает настройки из `settings.json` и `README.MD`.

.. code-block:: python

    from src.goog.text_to_speech import header
    print(header.__project_name__)
"""

import sys
from pathlib import Path
from packaging.version import Version
from typing import Dict, Any

from src.utils.jjson import j_loads
from src.logger.logger import logger
from src import gs # импорт используется

MODE: str = 'dev'
"""Режим работы проекта."""

MARKER_FILES: tuple[str, ...] = ('pyproject.toml', 'requirements.txt', '.git')
"""Файлы-маркеры для определения корневой директории проекта."""

COFEE_MESSAGE: str = "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""Сообщение с призывом поддержать разработчика."""


def set_project_root(marker_files: tuple[str, ...] = MARKER_FILES) -> Path:
    """
    Находит корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла,
    и поднимаясь вверх по дереву директорий. Поиск останавливается на первой директории,
    содержащей любой из файлов-маркеров.

    :param marker_files: Список файлов или директорий, которые идентифицируют корень проекта.
    :type marker_files: tuple[str, ...]
    :return: Путь к корневой директории проекта. Если корень не найден, возвращает директорию, где расположен скрипт.
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

# Get the root directory of the project
__root__: Path = set_project_root()
"""Путь к корневой директории проекта."""


settings: Dict[str, Any] = None
"""Словарь с настройками проекта, загруженный из `settings.json`."""
try:
    # код исполняет попытку открытия и загрузки файла настроек settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file) # используем j_loads из src.utils.jjson
        logger.info(f'Файл settings.json успешно загружен')
except (FileNotFoundError, json.JSONDecodeError) as e:
    # код исполняет логирование ошибки, если файл не найден или не является JSON
    logger.error(f'Ошибка загрузки файла settings.json: {e}')


doc_str: str = None
"""Строка с содержимым файла README.MD."""
try:
     # код исполняет попытку открытия и чтения файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
        logger.info(f'Файл README.MD успешно загружен')
except (FileNotFoundError, json.JSONDecodeError) as e:
     # код исполняет логирование ошибки, если файл не найден
    logger.error(f'Ошибка загрузки файла README.MD: {e}')



__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""Название проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""Документация проекта из файла README.MD."""
__details__: str = ''
"""Детали проекта."""
__author__: str = settings.get("author", '') if settings else ''
"""Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""Авторские права проекта."""
__cofee__: str = settings.get("cofee", COFEE_MESSAGE) if settings else COFEE_MESSAGE
"""Сообщение с предложением поддержать разработчика."""
```