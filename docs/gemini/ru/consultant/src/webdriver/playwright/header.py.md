# Анализ кода модуля `header.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и читаем.
    - Используется `Path` для работы с путями, что является хорошей практикой.
    - Функция `set_project_root` четко определена и выполняет свою задачу.
    - Присутствует обработка ошибок при загрузке файлов настроек.
    - Используются переменные для хранения информации о проекте.
-  Минусы
    - Отсутствует документация в формате reStructuredText.
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Избыточное использование `try-except` с `...` вместо использования логирования.
    - Некоторые переменные имеют неинформативные названия (например, `doc_str`).
    - Не все константы имеют описания

**Рекомендации по улучшению**

1.  **Документация**: Добавить документацию в формате reStructuredText для модуля, функций и переменных.
2.  **Использование `j_loads`**: Заменить `json.load` на `j_loads` или `j_loads_ns` для чтения `settings.json`.
3.  **Логирование ошибок**: Использовать `logger.error` вместо `try-except` с `...` для обработки ошибок.
4.  **Информативные имена**: Переименовать переменные, такие как `doc_str`, в более информативные.
5.  **Унификация**: Использовать константы `settings_file_path`, `readme_file_path` для упрощения доступа к файлам.
6.  **Описание констант**: Добавить описание для констант `MODE`, `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`.
7. **Убрать дублирование**: Убрать дублирование конструкции `if settings  else 'значение по умолчанию'`
8. **Комментарии**: Добавить комментарии к коду

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения основных параметров проекта.
=========================================================================================

Этот модуль содержит функции для определения корневой директории проекта, загрузки настроек из JSON файла
и инициализации глобальных переменных, таких как имя проекта, версия, автор и т.д.

Пример использования
--------------------

.. code-block:: python

    from src.webdriver.playwright import header

    print(header.__project_name__)
    print(header.__version__)

"""
import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads
from src.logger.logger import logger

"""
Режим работы проекта: 'dev' для разработки, 'prod' для продакшена
"""

def set_project_root(marker_files=('__root__','.git')) -> Path:
    """
    Определяет корневую директорию проекта.
    Ищет директорию, содержащую файлы-маркеры, начиная с текущей директории файла.

    :param marker_files: Кортеж имен файлов-маркеров для поиска корневой директории.
    :type marker_files: tuple
    :return: Путь к корневой директории.
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


# Определение корневой директории проекта
__root__ = set_project_root()
"""
__root__ (Path): Путь к корневой директории проекта.
"""

from src import gs
settings_file_path = gs.path.root / 'src' / 'settings.json'
"""
settings_file_path (Path): Путь к файлу настроек `settings.json`.
"""
readme_file_path = gs.path.root / 'src' / 'README.MD'
"""
readme_file_path (Path): Путь к файлу `README.MD`.
"""
settings: dict = None

# Попытка загрузить настройки из файла settings.json
try:
    settings = j_loads(settings_file_path)
except FileNotFoundError:
    logger.error(f'Файл настроек не найден: {settings_file_path}')
except Exception as e:
    logger.error(f'Ошибка при загрузке файла настроек: {settings_file_path}', exc_info=True)
    ...

project_doc_string: str = None

# Попытка загрузить строку документации из файла README.MD
try:
    with open(readme_file_path, 'r', encoding='utf-8') as doc_file:
        project_doc_string = doc_file.read()
except FileNotFoundError:
    logger.error(f'Файл README.MD не найден: {readme_file_path}')
    ...
except Exception as e:
    logger.error(f'Ошибка при загрузке файла README.MD: {readme_file_path}', exc_info=True)
    ...


__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""
__project_name__ (str): Название проекта, по умолчанию 'hypotez'.
"""
__version__: str = settings.get("version", '')  if settings else ''
"""
__version__ (str): Версия проекта.
"""
__doc__: str = project_doc_string if project_doc_string else ''
"""
__doc__ (str): Строка документации проекта.
"""
__details__: str = ''
"""
__details__ (str): Детали проекта.
"""
__author__: str = settings.get("author", '')  if settings else ''
"""
__author__ (str): Автор проекта.
"""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""
__copyright__ (str): Информация об авторских правах.
"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""
__cofee__ (str): Сообщение для поддержки разработчика.
"""
```