# Анализ кода модуля `header.py`

**Качество кода**
9
 -  Плюсы
    - Код содержит docstring для модуля.
    - Функция `set_project_root` имеет docstring и корректно определяет корневую директорию проекта.
    - Используются константы для имени проекта, версии и т.д.
    - Код обрабатывает ошибки при чтении файлов настроек и документации.
    - Используются `Path` для работы с путями.

 -  Минусы
    -  Используется `json.load` вместо `j_loads` или `j_loads_ns`.
    -  В блоках `try-except` используются `...`, лучше заменить на `logger.error`
    -  Не все переменные имеют docstring.
    -  Не используется `from src.logger.logger import logger`.
    -  Отсутствует проверка типа данных для переменных `settings`, `doc_str`.
    -  Отсутствуют docstring для констант `MODE`
    -  Дублирование кода обработки исключений.
    -  Docstring не в формате reStructuredText (RST)

**Рекомендации по улучшению**

1.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо `json.load` для чтения файлов.
2.  Заменить использование `...` в блоках `try-except` на логирование ошибок с помощью `logger.error`.
3.  Добавить docstring в формате RST для всех переменных и констант.
4.  Импортировать и использовать `from src.logger.logger import logger` для логирования.
5.  Удалить дублирование кода обработки исключений, вынести в отдельную функцию.
6.  Добавить проверку типа данных для переменных `settings`, `doc_str`.
7.  Уточнить комментарии к коду.
8.  Удалить неиспользуемые импорты.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для инициализации основных переменных проекта.
========================================================

Этот модуль определяет константы и глобальные переменные, используемые во всем проекте.
Он также включает функцию для определения корневой директории проекта.

.. note::
    Использует ``src.utils.jjson.j_loads`` для чтения JSON файлов.

Пример использования
--------------------

.. code-block:: python

    from src.endpoints.kazarinov.pricelist_generator import header

    print(header.__project_name__)
    print(header.__version__)
"""
#    импортируем logger для обработки ошибок
from src.logger.logger import logger
import sys
#   импортируем j_loads для загрузки json файлов
from src.utils.jjson import j_loads
#   импортируем Version для работы с версиями
from packaging.version import Version
from pathlib import Path
#   константа MODE
MODE = 'dev'
"""str: Режим работы приложения (dev/prod)."""

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла,
    поднимаясь вверх до первой директории, содержащей один из файлов-маркеров.

    :param marker_files: Кортеж с именами файлов или директорий, которые идентифицируют корень проекта.
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
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__

# Получение корневой директории проекта
__root__ = set_project_root()
"""Path: Путь к корневой директории проекта."""


from src import gs


def _load_data_from_file(file_path: Path, loader) -> str | dict | None:
    """
    Читает данные из файла, обрабатывая исключения.

    :param file_path: Путь к файлу.
    :type file_path: Path
    :param loader: Функция загрузки данных (например, j_loads).
    :type loader: callable
    :return: Данные из файла или None, если произошла ошибка.
    :rtype: str | dict | None
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return loader(file)
    except FileNotFoundError:
        logger.error(f'Файл не найден: {file_path}')
    except Exception as ex:
        logger.error(f'Ошибка при чтении файла: {file_path}', exc_info=ex)
    return None

#   читаем файл настроек
settings: dict = _load_data_from_file(gs.path.root / 'src' / 'settings.json', j_loads)
#   читаем файл документации
doc_str: str = _load_data_from_file(gs.path.root / 'src' / 'README.MD', lambda f: f.read())

__project_name__: str = settings.get("project_name", 'hypotez') if settings and isinstance(settings, dict) else 'hypotez'
"""str: Имя проекта."""
__version__: str = settings.get("version", '') if settings and isinstance(settings, dict) else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str and isinstance(doc_str, str) else ''
"""str: Документация проекта."""
__details__: str = ''
"""str: Детали проекта."""
__author__: str = settings.get("author", '') if settings and isinstance(settings, dict) else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings and isinstance(settings, dict) else ''
"""str: Авторские права."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings and isinstance(settings, dict) else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение о поддержке разработчика."""
```