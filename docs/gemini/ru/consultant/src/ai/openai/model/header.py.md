# Анализ кода модуля header.py

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован, использует функции для логической организации.
    - Определена функция `set_project_root` для определения корневой директории проекта.
    - Используются константы для задания имен файлов и директорий.
    - Присутствует обработка исключений при чтении файлов настроек.
    - Используется `pathlib` для работы с путями, что делает код более читаемым.
    - Присутствует базовая документация, хоть и не в полном объеме.
    - Код инициализирует основные переменные проекта, такие как имя, версия, автор и описание.
    - Используется `packaging.version` для версионирования
- Минусы
    - Не используется `j_loads` для чтения JSON файлов.
    - Некоторые комментарии не в формате reStructuredText (RST).
    - Отсутствует логирование ошибок при возникновении исключений.
    - Отсутствуют docstring для переменных модуля.
    - Не все переменные в модуле имеют тип аннотации.
    - Дублирование кода в блоках try-except.
    - Не хватает подробных комментариев для некоторых блоков кода.

**Рекомендации по улучшению**
1.  Использовать `j_loads` для загрузки `settings.json`.
2.  Добавить reStructuredText (RST) документацию для модуля, всех функций и переменных.
3.  Использовать `from src.logger.logger import logger` для логирования ошибок.
4.  Обрабатывать ошибки через `logger.error` вместо стандартных блоков `try-except`, избегая дублирования.
5.  Добавить аннотацию типа для переменных модуля.
6.  Добавить подробные комментарии в формате RST для блоков кода.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения корневого пути проекта и загрузки настроек.
=================================================================

Модуль определяет корневой путь к проекту, а также загружает
основные настройки проекта из файла `settings.json`.
Все импорты строятся относительно этого пути.

:var MODE: Режим работы приложения ('dev' или 'prod').
:vartype MODE: str
:var __root__: Корневой путь проекта.
:vartype __root__: pathlib.Path
:var settings: Настройки проекта из файла settings.json
:vartype settings: dict | None
:var doc_str: Содержимое файла README.MD.
:vartype doc_str: str | None
:var __project_name__: Имя проекта.
:vartype __project_name__: str
:var __version__: Версия проекта.
:vartype __version__: str
:var __doc__: Описание проекта.
:vartype __doc__: str
:var __details__: Дополнительные сведения о проекте.
:vartype __details__: str
:var __author__: Автор проекта.
:vartype __author__: str
:var __copyright__: Информация об авторских правах.
:vartype __copyright__: str
:var __cofee__: Сообщение о поддержке разработчика.
:vartype __cofee__: str

:Example:

    Пример использования переменных:

    .. code-block:: python

        from src.logger.header import __project_name__, __version__

        print(f"Название проекта: {__project_name__}")
        print(f"Версия: {__version__}")
"""

MODE: str = 'dev'

import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads_ns as j_loads
from src.logger.logger import logger

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Поиск ведется вверх от директории текущего файла до первой
    директории, содержащей один из файлов-маркеров.

    :param marker_files: Имена файлов или директорий, идентифицирующих корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
    :rtype: pathlib.Path
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


# Устанавливаем корневую директорию проекта
__root__: Path = set_project_root()
"""Path: Путь к корневой директории проекта"""


from src import gs

settings: dict | None = None
try:
    # Чтение настроек из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file) # Используем j_loads для загрузки JSON
except (FileNotFoundError, Exception) as ex:
    # Логирование ошибки, если файл не найден или при декодировании JSON
    logger.error(f"Ошибка при чтении файла настроек: {ex}")
    settings = None

doc_str: str | None = None
try:
    # Чтение документации из файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, Exception) as ex:
    # Логирование ошибки, если файл не найден или при чтении
    logger.error(f"Ошибка при чтении файла документации: {ex}")
    doc_str = None


__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Имя проекта"""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта"""
__doc__: str = doc_str if doc_str else ''
"""str: Описание проекта"""
__details__: str = ''
"""str: Дополнительные сведения о проекте"""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта"""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Информация об авторских правах"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение о поддержке разработчика"""
```