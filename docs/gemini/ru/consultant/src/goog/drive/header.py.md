# Анализ кода модуля `header.py`

**Качество кода**
7
 - Плюсы
        - Код выполняет основную задачу по определению корневой директории проекта и загрузке настроек.
        - Используется `pathlib` для работы с путями, что делает код более читаемым и кроссплатформенным.
        - Есть базовая обработка ошибок при загрузке настроек и документации.
 - Минусы
    - Используется `json.load` вместо `j_loads` или `j_loads_ns`.
    - Отсутствует логирование ошибок, что усложняет отладку.
    - Некоторые переменные и константы не документированы в формате RST.
    - `try-except` блоки с `...` выглядят неинформативно.
    - Нет проверки на тип данных в настройках, что потенциально может вызвать ошибки.
    - Не все переменные имеют аннотации типов.

**Рекомендации по улучшению**
1.  Используйте `j_loads` из `src.utils.jjson` вместо `json.load` для чтения файла настроек.
2.  Добавьте логирование ошибок с помощью `logger.error`, особенно в блоках `try-except`.
3.  Добавьте документацию в формате RST для модуля, функций и переменных.
4.  Уберите многоточия `...` и замените их на логирование ошибок или другие конкретные действия.
5.  Добавьте аннотации типов для всех переменных и констант.
6.  Переименуйте `cofee` на `coffee` в соответствии с общепринятым написанием.
7.  Добавьте проверку наличия ключей в словаре `settings` перед доступом к ним, чтобы избежать ошибок, если какие-то ключи отсутствуют.
8.  Оберните константы в конвенцию `UPPER_CASE_WITH_UNDERSCORES`.

**Оптимизированный код**
```python
"""
Модуль для определения корневой директории проекта и загрузки настроек.
=========================================================================================

Этот модуль предоставляет функции для определения корневой директории проекта,
загрузки настроек из файла `settings.json` и чтения документации из файла `README.MD`.

Пример использования
--------------------

.. code-block:: python

    from src.goog.drive.header import ROOT_DIR, PROJECT_NAME, VERSION, DOC, AUTHOR, COPYRIGHT, COFFEE

    print(f"Project root: {ROOT_DIR}")
    print(f"Project name: {PROJECT_NAME}")
    print(f"Version: {VERSION}")
    print(f"Author: {AUTHOR}")
"""
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

import sys
from pathlib import Path
from typing import Tuple, Dict, Optional
from packaging.version import Version

from src.utils.jjson import j_loads
from src.logger.logger import logger # Импортируем logger


MODE: str = 'dev'


def set_project_root(marker_files: Tuple[str, ...] = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла,
    поднимаясь вверх по дереву директорий и останавливаясь на первой директории,
    содержащей любой из файлов-маркеров.

    :param marker_files:  Кортеж с именами файлов или директорий, которые идентифицируют корневую директорию проекта.
    :return:  Путь к корневой директории проекта, если она найдена, или директория, где находится скрипт.
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
ROOT_DIR: Path = set_project_root()
"""ROOT_DIR (Path): Путь к корневой директории проекта."""

from src import gs

settings: Optional[Dict] = None
try:
    # Код пытается загрузить настройки из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
         settings = j_loads(settings_file)  # Используем j_loads для загрузки настроек из JSON
except FileNotFoundError as e:
    # Логируем ошибку, если файл не найден
    logger.error(f'Файл settings.json не найден {e}', exc_info=True)
except Exception as e:
    # Логируем ошибку, если произошла ошибка JSONDecodeError
    logger.error(f'Ошибка при чтении файла settings.json {e}', exc_info=True)



doc_str: Optional[str] = None
try:
    # Код пытается прочитать документацию из файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as doc_file:
        doc_str = doc_file.read()
except FileNotFoundError as e:
    # Логируем ошибку, если файл не найден
    logger.error(f'Файл README.MD не найден {e}', exc_info=True)
except Exception as e:
    # Логируем ошибку, если произошла ошибка JSONDecodeError
    logger.error(f'Ошибка при чтении файла README.MD {e}', exc_info=True)


PROJECT_NAME: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""PROJECT_NAME (str): Имя проекта, по умолчанию 'hypotez'."""
VERSION: str = settings.get("version", '') if settings else ''
"""VERSION (str): Версия проекта."""
DOC: str = doc_str if doc_str else ''
"""DOC (str): Документация проекта."""
DETAILS: str = ''
"""DETAILS (str): Дополнительные детали проекта."""
AUTHOR: str = settings.get("author", '') if settings else ''
"""AUTHOR (str): Автор проекта."""
COPYRIGHT: str = settings.get("copyrihgnt", '') if settings else ''
"""COPYRIGHT (str): Авторское право проекта."""
COFFEE: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""COFFEE (str): Сообщение с предложением поддержать разработчика."""
```