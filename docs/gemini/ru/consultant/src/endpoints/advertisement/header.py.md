# Анализ кода модуля `header.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован, с четким разделением на логические блоки.
    - Используется функция `set_project_root` для определения корневой директории проекта, что полезно для переносимости.
    - Есть обработка исключений при загрузке файлов настроек и документации.
    - Присваивание значений переменных, таких как `__project_name__`, `__version__`, `__doc__`, `__author__`, `__copyright__`, `__cofee__` корректно.
    - Использование `pathlib.Path` для работы с путями повышает читаемость и переносимость кода.
- Минусы
    - Отсутствуют docstring для модуля и некоторых переменных.
    - Используется `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Использование `...` для обработки исключений, что может затруднить отладку.
    - Отсутствует логирование ошибок при загрузке файлов настроек и документации.
    - Некоторые комментарии не соответствуют стилю reStructuredText (RST).
    - Не все импорты используються явно

**Рекомендации по улучшению**
- Добавить docstring для модуля и всех функций в формате RST.
- Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для загрузки JSON файлов.
- Заменить `...` в блоках `except` на логирование ошибок с использованием `logger.error`.
- Использовать более информативные комментарии, переписанные в стиле reStructuredText (RST).
- Добавить проверку на существование `settings` перед обращением к его ключам.
- Явное указание используемых import.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для настройки окружения и загрузки основных параметров проекта.
======================================================================

Этот модуль отвечает за определение корневой директории проекта,
загрузку настроек из файла `settings.json`, а также документации из `README.MD`.
Он устанавливает основные переменные проекта, такие как имя проекта, версию,
автора и т.д.

Пример использования
--------------------

.. code-block:: python

    from src.endpoints.advertisement import header

    print(header.__project_name__)
    print(header.__version__)
"""
import sys
from pathlib import Path
from packaging.version import Version

from src.utils.jjson import j_loads  # Используем j_loads для загрузки JSON
from src.logger.logger import logger #Используем logger для логирования

MODE = 'dev'
"""str: Режим работы приложения, по умолчанию `dev`"""


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневой каталог проекта, начиная с каталога текущего файла.

    Поиск ведется вверх по иерархии каталогов до первого каталога, содержащего
    один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов, идентифицирующих корень проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу, если он найден, иначе - каталог, где находится скрипт.
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


# Get the root directory of the project
__root__ = set_project_root()
"""Path: Путь к корневому каталогу проекта."""


from src import gs

settings: dict = None
"""dict: Словарь с настройками проекта, загруженный из `settings.json`."""
try:
    # код исполняет загрузку настроек из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except FileNotFoundError as e:
    # Логирование ошибки, если файл настроек не найден
    logger.error(f'Файл настроек не найден {e}', exc_info=True)
except json.JSONDecodeError as e:
    # Логирование ошибки, если файл настроек имеет неверный формат JSON
    logger.error(f'Ошибка декодирования JSON в файле настроек {e}', exc_info=True)


doc_str: str = None
"""str: Строка с документацией проекта, загруженная из `README.MD`."""
try:
    # код исполняет чтение документации из файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as doc_file:
        doc_str = doc_file.read()
except FileNotFoundError as e:
    # Логирование ошибки, если файл документации не найден
    logger.error(f'Файл документации не найден {e}', exc_info=True)
except Exception as e:
    # Логирование ошибки, если при чтении файла произошла ошибка
    logger.error(f'Ошибка чтения файла документации {e}', exc_info=True)

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
"""str: Авторские права проекта."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение для поддержки разработчика."""
```