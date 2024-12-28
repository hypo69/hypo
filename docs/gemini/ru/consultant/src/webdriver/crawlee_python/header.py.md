# Анализ кода модуля `header.py`

**Качество кода**
8
- Плюсы
    - Код структурирован и читаем.
    - Присутствует определение константы `MODE`.
    - Используется функция `set_project_root` для определения корневой директории проекта, что является хорошей практикой для переносимости.
    - Есть обработка исключений при чтении файлов настроек и README.
    - Используется `packaging.version.Version` для работы с версиями.
- Минусы
    -  Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    -  Не все блоки кода документированы в формате reStructuredText (RST).
    - Отсутствует логирование ошибок с помощью `logger.error`.
    - Обработка исключений  через `try-except`  и `...` не информативна.
    - Присутствует дублирование кода в блоках `try-except` для `settings.json` и `README.MD`
    - Некоторые переменные не имеют docstring, например `__root__`.

**Рекомендации по улучшению**
1.  Использовать `j_loads` или `j_loads_ns` для чтения JSON файлов.
2.  Добавить документацию в формате RST для всех функций, переменных и модуля.
3.  Заменить  `try-except` и  `...` на `logger.error` для логирования ошибок.
4.  Добавить импорт `from src.logger.logger import logger`.
5.  Устранить дублирование кода для чтения `settings.json` и `README.MD` с использованием функции.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения основных настроек и констант проекта.
============================================================

Этот модуль отвечает за:
    - Определение корневой директории проекта.
    - Загрузку настроек из `settings.json`.
    - Чтение документации из `README.MD`.
    - Определение основных переменных проекта, таких как имя, версия, автор и т.д.

Пример использования
--------------------

.. code-block:: python

    from src.webdriver.crawlee_python import header

    print(header.__project_name__)
    print(header.__version__)
"""



import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads
from src.logger.logger import logger


def set_project_root(marker_files: tuple = ('__root__',)) -> Path:
    """
    Определяет корневой каталог проекта.

    Функция ищет корневой каталог проекта, начиная с директории текущего файла,
    поднимаясь вверх по дереву каталогов до тех пор, пока не будет найден
    каталог, содержащий один из указанных файлов-маркеров.

    :param marker_files: Список файлов или директорий для идентификации корня проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу, если найден, иначе путь к директории, где находится скрипт.
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
"""Path: Путь к корневой директории проекта."""

from src import gs

settings: dict = None
doc_str: str = None

def load_file(file_path: Path, is_json: bool = False) -> any:
    """
    Загружает данные из файла.

    Функция пытается загрузить данные из указанного файла.
    В случае ошибки логирует ее и возвращает None.

    :param file_path: Путь к файлу.
    :type file_path: Path
    :param is_json: Флаг, указывающий, что файл содержит JSON. По умолчанию False.
    :type is_json: bool
    :return: Содержимое файла, если загрузка прошла успешно, иначе None.
    :rtype: any
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            if is_json:
                return j_loads(file)
            else:
                return file.read()
    except (FileNotFoundError, json.JSONDecodeError) as ex:
        logger.error(f'Ошибка загрузки файла {file_path}: {ex}')
        return None


settings = load_file(gs.path.root / 'src' / 'settings.json', is_json=True)
doc_str = load_file(gs.path.root / 'src' / 'README.MD')


__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Имя проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Строка документации проекта."""
__details__: str = ''
"""str: Детали проекта."""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Копирайт проекта."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение о поддержке разработчика."""

```