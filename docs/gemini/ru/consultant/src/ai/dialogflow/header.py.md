# Анализ кода модуля `header.py`

**Качество кода**
8
- Плюсы
    - Код выполняет основную задачу - настройку окружения и загрузку конфигурации.
    - Используется `pathlib` для работы с путями, что улучшает читаемость.
    - Код пытается загрузить настройки из файла, обрабатывая исключения.
    - Присутствует определение версии и других метаданных проекта.
- Минусы
    - Не используется `src.utils.jjson` для загрузки JSON, как требуется в инструкции.
    - Отсутствует логирование ошибок.
    - В docstring модуля не указано его назначение.
    - Не все переменные имеют docstring.
    - `try-except` блоки не логируют ошибку.
    - Жестко задано чтение README.MD.
    - Не все переменные имеют docstring.
    - Присутствует избыточное использование `if settings else ...`.

**Рекомендации по улучшению**
1. Заменить `json.load` на `j_loads` из `src.utils.jjson`.
2. Добавить логирование ошибок с использованием `logger.error`.
3. Добавить описание модуля, функций и переменных в формате RST.
4. Упростить код, избавившись от дублирования проверок `if settings`.
5. Добавить обработку исключения для `FileNotFoundError` и `json.JSONDecodeError`.
6. Использовать более явное имя переменной `settings_file` в блоке чтения `README.MD`.
7. Добавить проверку наличия настроек.
8. Установить кодировку при чтении файлов.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для определения корневой директории проекта и загрузки настроек.
======================================================================

Модуль выполняет поиск корневой директории проекта, а также загружает настройки
из файла `settings.json` и README из файла `README.MD` в корень проекта.

.. code-block:: python

    from src.ai.dialogflow.header import __root__, settings, __project_name__, __version__, __doc__

"""
import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads
from src.logger.logger import logger

MODE = 'dev'
"""str: Режим работы приложения (dev, prod)."""


def set_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла и поднимаясь вверх
    до тех пор, пока не найдет директорию, содержащую один из файлов-маркеров.

    :param marker_files: Список имен файлов или директорий, которые обозначают корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта, либо директория, где расположен скрипт, если маркер не найден.
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


# Получение корневой директории проекта
__root__ = set_project_root()
"""Path: Путь к корневой директории проекта."""

from src import gs


settings: dict = None
"""dict: Словарь с настройками проекта."""
try:
    # код исполняет чтение настроек из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r', encoding='utf-8') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    # логирование ошибки, если файл не найден или не является валидным JSON
    logger.error(f'Ошибка при чтении файла настроек: {e}', exc_info=True)
    ...

doc_str: str = None
"""str: Строка с содержимым README проекта."""
try:
    # код исполняет чтение README из файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as readme_file:
        doc_str = readme_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    # логирование ошибки, если файл не найден или не может быть прочитан
    logger.error(f'Ошибка при чтении файла README: {e}', exc_info=True)
    ...

# Получение имени проекта из настроек или установка значения по умолчанию
__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
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

__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение о поддержке разработчика."""
```