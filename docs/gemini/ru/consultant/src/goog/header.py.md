# Анализ кода модуля `header.py`

**Качество кода**
7
- Плюсы
    - Код выполняет функцию определения корневой директории проекта и загрузки настроек.
    - Используется `pathlib.Path` для работы с путями, что является хорошей практикой.
    - Присутствует обработка исключений `FileNotFoundError` и `json.JSONDecodeError`.
- Минусы
    - Отсутствуют docstring для модуля и переменных, что затрудняет понимание кода.
    - Не используются `j_loads` или `j_loads_ns` для загрузки JSON.
    - Использование `try-except` с `...` в блоке `except` не является информативным.
    - Некоторые переменные, такие как `__root__` и `settings`, объявляются без аннотации типа.
    - Код не стандартизирован под требования reStructuredText.
    - Не используется `logger` для логирования ошибок.

**Рекомендации по улучшению**

1. Добавить docstring для модуля, переменных и функций в формате reStructuredText (RST).
2. Использовать `j_loads` из `src.utils.jjson` для загрузки JSON-файла.
3. Заменить `...` в `except` блоках на использование `logger.error`.
4. Добавить аннотации типов для переменных.
5. Изменить комментарии на reStructuredText (RST).
6. Использовать `from src.logger.logger import logger` для логирования.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения корневой директории проекта и загрузки настроек.
=========================================================================================

Этот модуль содержит функции и переменные для автоматического определения
корневой директории проекта на основе наличия определенных файлов-маркеров,
а также загружает настройки проекта из файла `settings.json` и документацию из `README.MD`.

:var MODE: Режим работы приложения. По умолчанию 'dev'.
:vartype MODE: str
"""
MODE = 'dev'

import sys
from pathlib import Path
# from typing import Dict, Optional, Any
from packaging.version import Version

# from src.utils.jjson import j_loads
from src.logger.logger import logger # Добавлен импорт logger

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с директории текущего файла,
    поиска вверх и останавливаясь на первой директории, содержащей любой из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий для идентификации корня проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если она найдена, иначе директория, где расположен скрипт.
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

# Получение корневой директории проекта
__root__: Path = set_project_root()
"""
:var __root__: Путь к корневой директории проекта.
:vartype __root__: Path
"""

from src import gs
from src.utils.jjson import j_loads # импорт j_loads

settings: dict = None
try:
    # Загрузка настроек из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r', encoding='utf-8') as settings_file:
        settings = j_loads(settings_file) # Используем j_loads
except FileNotFoundError as e:
    # Логирование ошибки при отсутствии файла настроек
    logger.error(f'Файл настроек не найден: {e}')
except Exception as e:
    # Логирование ошибки при чтении JSON
    logger.error(f'Ошибка при чтении файла настроек: {e}')

doc_str: str = None
try:
    # Чтение документации из файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as settings_file:
        doc_str = settings_file.read()
except FileNotFoundError as e:
    # Логирование ошибки при отсутствии файла документации
    logger.error(f'Файл документации не найден: {e}')
except Exception as e:
    # Логирование ошибки при чтении файла документации
    logger.error(f'Ошибка при чтении файла документации: {e}')


__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""
:var __project_name__: Название проекта.
:vartype __project_name__: str
"""
__version__: str = settings.get("version", '') if settings else ''
"""
:var __version__: Версия проекта.
:vartype __version__: str
"""
__doc__: str = doc_str if doc_str else ''
"""
:var __doc__: Документация проекта.
:vartype __doc__: str
"""
__details__: str = ''
"""
:var __details__: Детали проекта.
:vartype __details__: str
"""
__author__: str = settings.get("author", '') if settings else ''
"""
:var __author__: Автор проекта.
:vartype __author__: str
"""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""
:var __copyright__: Информация об авторских правах проекта.
:vartype __copyright__: str
"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""
:var __cofee__: Сообщение с предложением угостить разработчика кофе.
:vartype __cofee__: str
"""
```