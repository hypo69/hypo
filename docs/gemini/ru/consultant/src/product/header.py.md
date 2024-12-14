# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    - Код выполняет поставленную задачу: определяет корневой путь проекта, загружает настройки и информацию о проекте.
    - Используется `pathlib` для работы с путями, что обеспечивает кроссплатформенность.
    - Присутствует обработка ошибок при загрузке настроек и документации.
    - Код достаточно хорошо структурирован и логически понятен.
    - Присутствует документация в виде docstring.
-  Минусы
    -  Используется `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Отсутствует обработка ошибок с использованием `logger.error` вместо стандартных `try-except`.
    - Некоторые комментарии не соответствуют стандарту reStructuredText (RST) и требуют переработки.
    -  Не все переменные и функции имеют docstring.
    - Присутствуют лишние комментарии.
    - Не все импорты соответствуют стандарту.

**Рекомендации по улучшению**

1.  **Импорт `j_loads`:** Заменить `json.load` на `j_loads` из `src.utils.jjson`.
2.  **Логирование ошибок:** Использовать `logger.error` из `src.logger.logger` для логирования ошибок вместо `try-except` с `...`.
3.  **Документация RST:**  Привести все комментарии и docstring к формату reStructuredText (RST).
4.  **Добавить недостающие docstring:** Добавить docstring ко всем функциям, переменным и константам.
5.  **Удалить лишние комментарии:** Удалить лишние комментарии, не несущие смысловой нагрузки.
6.  **Уточнить комментарии:** Добавить подробные комментарии для понимания работы кода.
7.  **Использовать `gs.path.root`:**  Использовать `gs.path.root` для формирования путей.
8. **Удалить неиспользуемые импорты**: удалить неиспользуемые импорты `MODE`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения корневого пути проекта, загрузки настроек и информации о проекте.
=========================================================================================

Модуль предоставляет функциональность для автоматического определения корневой директории проекта,
загрузки настроек из файла `settings.json` и чтения документации из файла `README.MD`.
Используется для инициализации основных параметров проекта, таких как имя, версия, автор и т.д.

Пример использования
--------------------

Пример использования функций и переменных модуля:

.. code-block:: python

    from src.product import header

    print(f"Project root: {header.__root__}")
    print(f"Project name: {header.__project_name__}")
    print(f"Project version: {header.__version__}")
"""

import sys
from pathlib import Path
from packaging.version import Version
#  Импортируем j_loads для загрузки json
from src.utils.jjson import j_loads
from src.logger.logger import logger
from src import gs


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция осуществляет поиск корневой директории проекта, начиная с директории текущего файла.
    Поиск происходит путём перебора родительских директорий до тех пор, пока не будет найдена
    директория, содержащая хотя бы один из файлов-маркеров. Если такая директория не найдена,
    возвращается директория, где расположен текущий файл. Найденный путь добавляется в `sys.path`.

    :param marker_files: Кортеж файлов-маркеров для определения корневой директории.
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

# Получаем корневой путь проекта
__root__ = set_project_root()
"""
Path: Корневой путь к директории проекта.
"""

settings: dict = None
try:
    #  Загружаем настройки из файла settings.json
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    #  Логируем ошибку, если файл не найден или не является JSON
    logger.error(f'Ошибка загрузки файла настроек: {e}')
    ...

doc_str: str = None
try:
    #  Читаем содержимое файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError,  UnicodeDecodeError) as e:
    # Логируем ошибку если файл не найден или ошибка кодировки
    logger.error(f'Ошибка загрузки файла документации: {e}')
    ...


__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""
str: Имя проекта, по умолчанию 'hypotez'.
"""
__version__: str = settings.get("version", '') if settings else ''
"""
str: Версия проекта, по умолчанию пустая строка.
"""
__doc__: str = doc_str if doc_str else ''
"""
str: Документация проекта, прочитанная из файла README.MD, по умолчанию пустая строка.
"""
__details__: str = ''
"""
str: Детальная информация о проекте, по умолчанию пустая строка.
"""
__author__: str = settings.get("author", '') if settings else ''
"""
str: Автор проекта, по умолчанию пустая строка.
"""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""
str: Авторские права проекта, по умолчанию пустая строка.
"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""
str: Строка с призывом угостить разработчика кофе, по умолчанию строка с ссылкой на boosty.
"""
```