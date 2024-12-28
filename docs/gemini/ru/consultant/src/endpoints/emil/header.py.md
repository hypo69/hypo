# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и читаем.
    - Используется функция `set_project_root` для определения корневой директории проекта, что является хорошей практикой.
    - Есть обработка ошибок при чтении файлов настроек и README.
    - Присутствуют docstring для функций и модулей, хоть и требуют доработки.
-  Минусы
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Некоторые docstring не соответствуют стандарту reStructuredText (RST).
    - Отсутствует импорт `from src.logger.logger import logger`.
    - Обработка исключений `FileNotFoundError` и `json.JSONDecodeError` выполняется через `...` (пропуск), что не является хорошей практикой.
    - Многократное использование `if settings else` можно упростить.

**Рекомендации по улучшению**

1.  Использовать `j_loads` из `src.utils.jjson` вместо стандартного `json.load`.
2.  Добавить импорт `from src.logger.logger import logger`.
3.  Заменить `...` на логирование ошибок с помощью `logger.error` при обработке исключений.
4.  Переписать docstring в соответствии со стандартом reStructuredText (RST).
5.  Упростить получение настроек, используя `settings.get(key, default)` вместо `if settings else`.
6.  Добавить комментарии, объясняющие каждый блок кода.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения настроек и путей проекта.
====================================================

Этот модуль содержит функции и переменные,
необходимые для определения корневой директории проекта,
загрузки настроек из JSON-файла и чтения документации из файла README.MD.
"""


import sys
from pathlib import Path
#  Импортируем j_loads из src.utils.jjson
from src.utils.jjson import j_loads
# импортируем logger для логирования ошибок
from src.logger.logger import logger
from packaging.version import Version

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла,
    поднимаясь вверх по иерархии каталогов. Поиск прекращается при обнаружении первого каталога,
    содержащего один из файлов-маркеров.

    :param marker_files: Кортеж с именами файлов или каталогов, которые идентифицируют корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
    :rtype: Path
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    #  цикл перебирает текущий каталог и его родительские каталоги
    for parent in [current_path] + list(current_path.parents):
        # проверяем, существует ли какой-либо из файлов-маркеров в текущем каталоге
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    # Если корневой каталог не добавлен в sys.path, добавляем его
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Получаем корневую директорию проекта
__root__ = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта"""

from src import gs

settings:dict = None
try:
    #  открываем файл settings.json, используя j_loads для загрузки JSON
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
#  обрабатываем исключение, если файл не найден или JSON некорректен
except (FileNotFoundError, json.JSONDecodeError) as e:
    #  Логируем ошибку, если файл не найден или JSON некорректен
    logger.error(f'Ошибка при чтении файла настроек {gs.path.root / "src" /  "settings.json"}', exc_info=e)
    settings = {}


doc_str:str = None
try:
    #  открываем файл README.MD
    with open(gs.path.root / 'src' /  'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
#  обрабатываем исключение, если файл не найден
except (FileNotFoundError) as e:
    #  Логируем ошибку, если файл не найден
    logger.error(f'Ошибка при чтении файла документации {gs.path.root / "src" /  "README.MD"}', exc_info=e)
    doc_str = ''



__project_name__ = settings.get("project_name", 'hypotez')
"""__project_name__ (str): Имя проекта"""
__version__: str = settings.get("version", '')
"""__version__ (str): Версия проекта"""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Строка документации"""
__details__: str = ''
"""__details__ (str): Детали проекта"""
__author__: str = settings.get("author", '')
"""__author__ (str): Автор проекта"""
__copyright__: str = settings.get("copyrihgnt", '')
"""__copyright__ (str): Копирайт проекта"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")
"""__cofee__ (str): Сообщение о поддержке разработчика"""
```