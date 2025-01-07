# Анализ кода модуля `header.py`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и выполняет свою основную функцию определения корневой директории проекта.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Присутствует обработка исключений при загрузке настроек и документации.
    - Используются константы для определения путей поиска.
- Минусы
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения JSON файлов.
    - Отсутствуют RST docstrings для модуля, функций и переменных.
    - Используются `try-except` блоки с `...` вместо более явной обработки ошибок.
    - Есть неиспользуемая переменная `MODE`.
    - Используются `settings.get` без проверки наличия ключа в словаре `settings`.
    - Нет логирования ошибок с помощью `logger`.
    - Есть опечатка в переменной `copyrihgnt` -> `copyright`.

**Рекомендации по улучшению**
1.  Использовать `j_loads` из `src.utils.jjson` для загрузки JSON.
2.  Добавить docstrings в формате RST для модуля, функции и переменных.
3.  Использовать `logger.error` для логирования ошибок вместо `try-except ...`.
4.  Удалить неиспользуемую переменную `MODE`.
5.  Исправить опечатку в переменной `copyrihgnt` на `copyright`.
6.  Добавить обработку случая, когда `settings` не является словарем, например через проверку типа.
7.  Избавиться от избыточного использования `if settings else ...` используя `or {}`.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для определения корневой директории проекта.
====================================================

Модуль определяет корневой путь к проекту, относительно которого строятся все импорты.

:platform: Windows, Unix
:synopsis: Модуль определяющий корневой путь к проекту. Все импорты строятся относительно этого пути.

..  todo:: В дальнейшем перенести в системную переменную
"""
import sys
#  Импортируем json из jjson для корректной обработки данных
#  Импортируем logger для обработки исключений
from src.utils.jjson import j_loads
from src.logger.logger import logger
from packaging.version import Version
from pathlib import Path

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта, начиная с директории текущего файла.

    Поиск идёт вверх по дереву директорий, останавливаясь на первой директории, содержащей любой из файлов-маркеров.

    :param marker_files: Кортеж с именами файлов или директорий, которые идентифицируют корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если она найдена, иначе - директория, где расположен скрипт.
    :rtype: Path
    """
    __root__: Path
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    #  Перебираем текущую директорию и все её родительские директории
    for parent in [current_path] + list(current_path.parents):
        #  Проверяем, существует ли в текущей директории какой-либо из файлов-маркеров
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    #  Если корень проекта не в путях Python, добавляем его
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Получаем корневую директорию проекта
__root__ = set_project_root()
"""
Path: Путь к корневой директории проекта.
"""

from src import gs

settings: dict = None
try:
    #  Используем j_loads для загрузки настроек из JSON файла
    with open(gs.path.root / 'src' / 'settings.json', 'r', encoding='utf-8') as settings_file:
         settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as ex:
    #  Логируем ошибку, если файл не найден или JSON не валиден
    logger.error('Ошибка при загрузке файла настроек settings.json', exc_info=ex)


doc_str: str = None
try:
    #  Читаем содержимое файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as doc_file:
        doc_str = doc_file.read()
except (FileNotFoundError) as ex:
    # Логируем ошибку, если файл не найден
    logger.error('Ошибка при чтении файла README.MD', exc_info=ex)


# Устанавливаем значения из настроек или значения по умолчанию
__project_name__ = settings.get("project_name", 'hypotez') if isinstance(settings, dict) else 'hypotez'
__version__: str = settings.get("version", '') if isinstance(settings, dict) else ''
__doc__: str = doc_str or ''
__details__: str = ''
__author__: str = settings.get("author", '') if isinstance(settings, dict) else ''
__copyright__: str = settings.get("copyright", '')  if isinstance(settings, dict) else ''
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if isinstance(settings, dict) else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```