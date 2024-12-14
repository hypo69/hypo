# Анализ кода модуля `header`

**Качество кода**
8
- Плюсы
    - Код выполняет задачу определения корневой директории проекта и загрузки настроек.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Присутствует обработка исключений при загрузке файлов настроек.
    - Код разбит на логические блоки.
    - Определены метаданные проекта.
    - Использованы `docstring` для документирования модуля и функций
- Минусы
    - Не используется `j_loads` из `src.utils.jjson` для чтения файлов.
    - Избыточное использование стандартных блоков `try-except`.
    - Отсутствуют необходимые импорты из `src.logger.logger`.
    - Местами отсутствуют docstring для переменных
    - Имена некоторых переменных не соответствуют общепринятым соглашениям (например, `doc_str`).
    - Есть опечатки в метаданных (например, `copyrihgnt`).

**Рекомендации по улучшению**

1.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для загрузки `settings.json`.
2.  Заменить множественные блоки `try-except` на единый блок с использованием `logger.error` для логирования ошибок.
3.  Добавить необходимые импорты из `src.logger.logger`.
4.  Переименовать переменные для соответствия соглашениям (например, `doc_str` на `readme_content`).
5.  Исправить опечатку в `copyright`.
6. Добавить документацию для переменных.
7. Добавить более подробные описания в docstring.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения корневой директории проекта и загрузки основных настроек.
=================================================================================

Этот модуль предоставляет функциональность для автоматического определения корневой
директории проекта на основе наличия маркерных файлов, таких как 'pyproject.toml',
'requirements.txt' или '.git'. Также модуль загружает настройки проекта из файла
'settings.json' и считывает содержимое 'README.MD', предоставляя доступ к этим
данным через глобальные переменные.

Пример использования
--------------------

.. code-block:: python

    from src.suppliers.header import __project_name__, __version__, __doc__, __author__

    print(f"Project Name: {__project_name__}")
    print(f"Version: {__version__}")
    print(f"Author: {__author__}")
"""
MODE = 'dev'

import sys
from pathlib import Path
# импортируем j_loads
from src.utils.jjson import j_loads
from src.logger.logger import logger
from packaging.version import Version

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла и поднимаясь вверх
    по дереву каталогов. Поиск останавливается при обнаружении первого каталога, содержащего
    один из маркерных файлов.

    :param marker_files: Кортеж имен файлов или каталогов для идентификации корня проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта, если она найдена, иначе - путь к директории, где находится скрипт.
    :rtype: Path
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Определяем корневую директорию проекта
__root__ = set_project_root()
"""
:type: Path
:desc:  Путь к корневой директории проекта.
"""

from src import gs

settings: dict = None
"""
:type: dict
:desc: Словарь с настройками проекта, загруженными из файла 'settings.json'.
"""
try:
    # код исполняет загрузку настроек из файла 'settings.json'
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логируем ошибку, если файл не найден или не удается декодировать JSON
    logger.error(f'Ошибка при загрузке настроек из файла {gs.path.root / "src" / "settings.json"}', exc_info=e)
    ...

readme_content: str = None
"""
:type: str
:desc: Содержимое файла 'README.MD'.
"""
try:
    # Код исполняет чтение содержимого файла 'README.MD'
    with open(gs.path.root / 'src' /  'README.MD', 'r') as readme_file:
        readme_content = readme_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логируем ошибку, если файл не найден или не удается прочитать файл
    logger.error(f'Ошибка при чтении файла {gs.path.root / "src" / "README.MD"}', exc_info=e)
    ...

# Получение метаданных проекта из настроек или установка значений по умолчанию.
__project_name__: str = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
"""
:type: str
:desc: Имя проекта.
"""
__version__: str = settings.get("version", '')  if settings  else ''
"""
:type: str
:desc: Версия проекта.
"""
__doc__: str = readme_content if readme_content else ''
"""
:type: str
:desc: Содержимое файла README.MD.
"""
__details__: str = ''
"""
:type: str
:desc: Детали проекта (в текущей реализации не используется).
"""
__author__: str = settings.get("author", '')  if settings  else ''
"""
:type: str
:desc: Автор проекта.
"""
__copyright__: str = settings.get("copyright", '')  if settings  else ''
"""
:type: str
:desc: Информация об авторских правах.
"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""
:type: str
:desc: Сообщение для поддержки разработчика.
"""
```