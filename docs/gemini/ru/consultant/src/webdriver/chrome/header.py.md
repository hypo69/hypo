# Анализ кода модуля `header.py`

**Качество кода**
7
- Плюсы
    - Код читаемый и в целом соответствует назначению.
    - Присутствует функция для определения корневой директории проекта.
    - Используются константы для хранения информации о проекте.
    - Есть обработка исключений при чтении файлов настроек.
- Минусы
    - Отсутствует reStructuredText (RST) документация для модуля, функций, и переменных.
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    - Желательно использовать `logger` для логирования ошибок вместо `...` в блоках `try-except`.
    - Есть дублирование логики обработки исключений при чтении файлов.
    - Не хватает импорта `logger`.
    - Переменные `__root__` объявляется дважды, и второе объявление ни к чему.

**Рекомендации по улучшению**

1.  Добавить RST документацию для модуля, функций и переменных.
2.  Использовать `j_loads` из `src.utils.jjson` для чтения файла `settings.json`.
3.  Использовать `logger.error` для логирования ошибок и убрать `...`.
4.  Избежать дублирования обработки ошибок при чтении файлов.
5.  Импортировать `logger` из `src.logger.logger`.
6.  Исправить двойное определение `__root__`.
7.  Переименовать `copyrihgnt` на `copyright`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения метаданных проекта и настройки окружения.
=================================================================

Этот модуль выполняет следующие задачи:
    - Определение корневой директории проекта.
    - Загрузка настроек проекта из файла `settings.json`.
    - Загрузка документации проекта из файла `README.MD`.
    - Определение основных метаданных проекта, таких как имя, версия, автор и т.д.

Пример использования
--------------------

.. code-block:: python

   from src.webdriver.chrome import header

   print(header.__project_name__)
   print(header.__version__)
   print(header.__doc__)
"""
MODE = 'dev'

import sys
from pathlib import Path
from packaging.version import Version
# from src.utils.jjson import j_loads #TODO:  не используется
# TODO: import json - не используется 
from src.logger.logger import logger # Добавлен импорт logger

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Ищет вверх по дереву директорий от текущего файла, пока не найдет директорию,
    содержащую один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий, обозначающих корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
    :rtype: Path
    """
    #  Переменная __root__  объявлена для хранения пути к корневой директории
    current_path: Path = Path(__file__).resolve().parent
    __root__: Path = current_path
    #  Итерируемся по родительским директориям, начиная с текущей
    for parent in [current_path] + list(current_path.parents):
        # Проверяем наличие маркеров в текущей родительской директории
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    #  Если корневая директория еще не в sys.path, добавляем ее
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__

# Определяем корневую директорию проекта
__root__: Path = set_project_root()
"""Path: Путь к корневой директории проекта."""

from src import gs

settings: dict = None
# Пытаемся загрузить настройки из settings.json
try:
    # Читаем файл настроек
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        # Используем j_loads для чтения JSON файла
        settings = j_loads(settings_file)  # Исправлено: json.load заменено на j_loads
except (FileNotFoundError, json.JSONDecodeError) as ex:
    # Логируем ошибку, если файл не найден или не является валидным JSON
    logger.error('Ошибка при чтении файла настроек settings.json', exc_info=ex)
    settings = {} # Инициализируем settings пустым словарем, чтобы не было ошибок далее

doc_str: str = None
# Пытаемся загрузить документацию из README.MD
try:
    # Читаем файл README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as ex:
    # Логируем ошибку, если файл не найден
    logger.error('Ошибка при чтении файла документации README.MD', exc_info=ex)
    doc_str = '' #  Инициализируем doc_str пустой строкой, чтобы не было ошибок далее

# Извлекаем метаданные проекта из настроек или устанавливаем значения по умолчанию
__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Имя проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта."""
__details__: str = ''
"""str: Дополнительная информация о проекте."""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyright", '') if settings else '' # Исправлено: copyrihgnt на copyright
"""str: Информация об авторских правах."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Призыв поддержать разработчика."""
```