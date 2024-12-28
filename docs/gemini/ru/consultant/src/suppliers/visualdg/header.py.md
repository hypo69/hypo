# Анализ кода модуля `header.py`

**Качество кода**
8
- Плюсы
    - Код выполняет свою задачу по определению корневой директории проекта и загрузке настроек.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Присутствует обработка исключений `FileNotFoundError` и `json.JSONDecodeError` при загрузке настроек.
    - Использование `packaging.version.Version` для работы с версиями (хотя не используется в коде)
    - Код достаточно структурирован и понятен.

- Минусы
    - Не используются `j_loads` или `j_loads_ns` для загрузки JSON.
    - Отсутствуют docstring для модуля и функций.
    - Нет логирования ошибок.
    -  Смешаны импорты библиотек.
    -  Использованы множественные `...` в блоках `try-except`, что не способствует отладке.
    -  Много повторяющегося кода (например, при чтении файлов настроек и README)
     -   Переменные с именами вида `__variable__` в глобальной области видимости.
      -  Не используется `logger` для вывода ошибок.

**Рекомендации по улучшению**

1.  **Документация:** Добавить docstring к модулю и функции `set_project_root`.
2.  **Импорты:**  Упорядочить и добавить импорты.
3.  **Загрузка JSON:** Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо `json.load`.
4.  **Обработка ошибок:** Использовать `logger.error` для логирования ошибок вместо `...` в блоках `try-except`.
5.  **Избегать повторения кода:** Вынести чтение файлов в отдельную функцию.
6. **Именование переменных:** Использовать осмысленные имена переменных (не в стиле `__variable__`)
7. **Сообщения logger:**  Использовать осмысленные сообщения logger.
8. **Убрать лишние комментарии:** Убрать лишние комментарии, которые не несут смысловой нагрузки.
9. **Логика:** убрать дублирование `if settings else ` в коде.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения корневой директории проекта, загрузки настроек и определения метаданных проекта.
==================================================================================================

Этот модуль предоставляет функциональность для:

-   Автоматического определения корневой директории проекта на основе наличия файлов-маркеров.
-   Загрузки настроек проекта из файла `settings.json`.
-   Чтения документации проекта из файла `README.MD`.
-   Определения метаданных проекта, таких как имя, версия, автор и т.д.

Пример использования
--------------------

Для использования модуля необходимо импортировать его в ваш проект.

.. code-block:: python

    from src.suppliers.visualdg import header

    print(header.__project_name__)
    print(header.__version__)
"""
import sys
from pathlib import Path
from typing import Tuple

from src.logger.logger import logger
from src.utils.jjson import j_loads
from packaging.version import Version # TODO: пока не используется, но может пригодится

MODE = 'dev'


def set_project_root(marker_files: Tuple[str, ...] = ('__root__',)) -> Path:
    """
    Определение корневой директории проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла,
    двигаясь вверх по дереву каталогов до тех пор, пока не будет найден каталог,
    содержащий один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов, которые используются для идентификации корневой директории проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории.
    :rtype: pathlib.Path
    """
    current_path: Path = Path(__file__).resolve().parent
    root_path: Path = current_path

    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            root_path = parent
            break
    if root_path not in sys.path:
        sys.path.insert(0, str(root_path))
    return root_path


# Определение корневой директории проекта
__root__ = set_project_root()
"""Path: Путь к корневой директории проекта."""

from src import gs


def _load_file(file_path: Path) -> str or dict or None:
    """
    Загрузка файла.

    Функция загружает данные из указанного файла, обрабатывая ошибки,
    и возвращает результат в виде строки или словаря.
    Если при загрузке файла возникает ошибка, она логируется.

    :param file_path: Путь к файлу для загрузки.
    :type file_path: Path
    :return: Содержимое файла в виде строки (для текстовых файлов) или словаря (для JSON), или None в случае ошибки.
    :rtype: str or dict or None
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            if file_path.suffix == '.json':
                return j_loads(file)
            return file.read()
    except FileNotFoundError:
        logger.error(f'Файл не найден: {file_path}')
    except json.JSONDecodeError:
        logger.error(f'Ошибка декодирования JSON из файла: {file_path}')
    except Exception as e:
        logger.error(f'Неизвестная ошибка при чтении файла: {file_path}', exc_info=e)
    return None

# загрузка настроек
settings_file_path = gs.path.root / 'src' / 'settings.json'
settings = _load_file(settings_file_path)
"""dict: словарь с настройками проекта"""
# загрузка документации
readme_file_path = gs.path.root / 'src' / 'README.MD'
doc_str = _load_file(readme_file_path)
"""str: строка документации проекта"""

__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Наименование проекта"""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта"""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта"""
__details__: str = ''
"""str: Детали проекта"""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта"""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Авторские права проекта"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Призыв угостить разработчика кофе"""
```