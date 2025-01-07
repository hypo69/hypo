# Анализ кода модуля `header.py`

**Качество кода**

8
- Плюсы
    - Код хорошо структурирован и легко читается.
    - Используется функция `set_project_root` для определения корневой директории проекта, что является хорошей практикой.
    - Применяются `try-except` блоки для обработки ошибок при чтении файлов, хотя можно улучшить логирование.
    - Присутствует начальная документация в формате docstring.
- Минусы
    -  Используется стандартный `json.load`, что противоречит инструкции.
    -  Не все переменные и функции имеют docstring в формате RST.
    -  Отсутствует импорт `logger` для логирования ошибок.
    -   Отсутсвует обработки исключений в блоке чтения `README.MD`.
    -  Используются `...` как заглушки, что требует доработки.
    -  Имя переменной `copyrihgnt` с опечаткой.
    -  Используется `FileNotFoundError` при открытии `README.MD`, хотя это не JSON файл

**Рекомендации по улучшению**

1.  **Импорты**: Добавить `from src.utils.jjson import j_loads` и `from src.logger.logger import logger`.
2.  **Использование `j_loads`**: Заменить `json.load` на `j_loads` для загрузки `settings.json`.
3.  **Документация**: Добавить docstring в формате RST для модуля, функции `set_project_root` и всех глобальных переменных.
4.  **Обработка ошибок**: Заменить `try-except` блоки на использование `logger.error` для логирования ошибок.
5.  **Обработка `README.MD`**: Использовать более подходящий обработчик ошибок, например `FileNotFoundError` или `IOError`.
6.  **Убрать заглушки**: Заменить `...` на соответствующую логику обработки ошибок.
7.  **Исправить опечатку**: Исправить `copyrihgnt` на `copyright`.
8.  **Улучшить читаемость**:  Добавить перенос строки для длинной строки `__cofee__`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для загрузки настроек и метаданных проекта.
=================================================

Этот модуль предназначен для загрузки настроек проекта из файла `settings.json`,
а также чтения документации из `README.MD`.

Модуль также содержит функцию для определения корневой директории проекта.

Пример использования
--------------------

.. code-block:: python

    from src.endpoints.kazarinov.pricelist_generator import header

    print(header.__project_name__)
    print(header.__version__)
"""


import sys
from pathlib import Path
from packaging.version import Version

from src.utils.jjson import j_loads
from src.logger.logger import logger


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определение корневой директории проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла
    и поднимаясь вверх по дереву каталогов. Поиск останавливается на первой
    директории, содержащей один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий, которые идентифицируют корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
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
__root__ = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта."""


from src import gs

settings: dict = None
try:
    #  Код загружает настройки из файла 'settings.json'
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except FileNotFoundError:
    #  Код логирует ошибку, если файл 'settings.json' не найден
    logger.error(f'Файл настроек не найден {gs.path.root / "src" / "settings.json"}')
except Exception as ex:
    #  Код логирует ошибку, если не удалось декодировать JSON в файле 'settings.json'
    logger.error(f'Ошибка декодирования файла настроек {gs.path.root / "src" / "settings.json"}', exc_info=ex)


doc_str: str = None
try:
    #  Код считывает содержимое файла 'README.MD'
    with open(gs.path.root / 'src' / 'README.MD', 'r') as doc_file:
        doc_str = doc_file.read()
except FileNotFoundError:
    #  Код логирует ошибку, если файл 'README.MD' не найден
    logger.error(f'Файл документации не найден {gs.path.root / "src" / "README.MD"}')
except Exception as ex:
    #  Код логирует ошибку, если не удалось прочитать файл 'README.MD'
    logger.error(f'Ошибка чтения файла документации {gs.path.root / "src" / "README.MD"}', exc_info=ex)


__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Имя проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""__version__ (str): Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Документация проекта."""
__details__: str = ''
"""__details__ (str): Детали проекта."""
__author__: str = settings.get("author", '') if settings else ''
"""__author__ (str): Автор проекта."""
__copyright__: str = settings.get("copyright", '') if settings else ''
"""__copyright__ (str): Авторские права проекта."""
__cofee__: str = settings.get("cofee",
                             "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
                             ) if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Сообщение о поддержке разработчика."""
```