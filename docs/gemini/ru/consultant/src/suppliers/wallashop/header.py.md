# Анализ кода модуля `header.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и читаем.
    - Используется функция `set_project_root` для определения корневой директории проекта, что является хорошей практикой.
    - Есть обработка исключений при чтении файлов `settings.json` и `README.MD`.
    - Используются переменные `__project_name__`, `__version__`, `__doc__`, `__author__` и другие для хранения метаданных проекта.
    - Добавлены константы `MODE`,  `__cofee__`.
- Минусы
    - Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения `settings.json`.
    - Отсутствует  логирование ошибок при загрузке файлов конфигурации.
    - Нет docstring для модуля и некоторых переменных, что уменьшает понятность кода.
    - Отсутствуют проверки на корректность полученных данных.
    - Не все импорты используются.
    - В коде есть `...`, которые должны быть заменены на `pass` или другую логику обработки.

**Рекомендации по улучшению**
1.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для загрузки `settings.json`.
2.  Добавить docstring для модуля.
3.  Добавить комментарии reStructuredText (RST) для функций и переменных.
4.  Использовать `logger.error` из `src.logger.logger` для логирования ошибок.
5.  Избавиться от `...` и заменить их на `pass` или логику обработки.
6.  Удалить неиспользуемый импорт `sys`.
7.  Добавить проверки на корректность данных, полученных из `settings.json` и `README.MD`.
8.  Добавить комментарии `#` с пояснением для каждого блока кода.
9.  Указать `encoding='utf-8'` при открытии файла `README.MD`.
10. Добавить обработку ошибки, если `settings` is `None` при получении переменных проекта.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для определения основных настроек и метаданных проекта.
=================================================================

Этот модуль выполняет следующие задачи:
    - Находит корневую директорию проекта.
    - Загружает настройки проекта из файла `settings.json`.
    - Читает документацию проекта из файла `README.MD`.
    - Определяет основные метаданные проекта, такие как имя, версия, автор и т.д.

Пример использования
--------------------
Для использования достаточно импортировать модуль.
Переменные будут автоматически инициализированы:

.. code-block:: python

    from src.suppliers.wallashop import header

    print(header.__project_name__)
    print(header.__version__)
"""


# import sys #  Импорт не используется

import json
from packaging.version import Version
from pathlib import Path

from src.utils.jjson import j_loads #  Используем j_loads для загрузки json
from src.logger.logger import logger # Используем logger для логирования ошибок
from src import gs

def set_project_root(marker_files: tuple = ('__root__',)) -> Path:
    """
    Находит корневую директорию проекта, начиная с директории текущего файла.
    Поиск идет вверх по дереву каталогов и останавливается на первом каталоге,
    содержащем любой из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов, которые идентифицируют корень проекта.
    :type marker_files: tuple, optional
    :return: Путь к корневой директории, если она найдена, иначе директория, где находится скрипт.
    :rtype: Path
    """
    __root__: Path
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    #  проходим по родительским директориям, начиная с текущей
    for parent in [current_path] + list(current_path.parents):
        # проверяем, существует ли какой-либо маркерный файл в текущей родительской директории
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent #  если маркер найден, устанавливаем корень проекта
            break #  прерываем цикл
    if str(__root__) not in sys.path: #  проверяем, добавлен ли корень проекта в sys.path
        sys.path.insert(0, str(__root__)) #  добавляем корень проекта в начало sys.path, если его там нет
    return __root__

#  получаем корневую директорию проекта
__root__ = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта"""

settings: dict = None
#  блок try для загрузки настроек из settings.json
try:
    #  открываем файл настроек в режиме чтения
    with open(gs.path.root / 'src' / 'settings.json', 'r', encoding='utf-8') as settings_file:
        #  загружаем настройки из файла с использованием j_loads
        settings = j_loads(settings_file)
except FileNotFoundError as ex:
    #  Логируем ошибку, если файл не найден
    logger.error(f'Файл settings.json не найден: {ex}', exc_info=True)
    settings = {} #  Устанавливаем пустой словарь, чтобы избежать ошибок при дальнейшей работе.
except json.JSONDecodeError as ex:
    #  Логируем ошибку, если файл не может быть декодирован
    logger.error(f'Ошибка декодирования settings.json: {ex}', exc_info=True)
    settings = {} #  Устанавливаем пустой словарь, чтобы избежать ошибок при дальнейшей работе.


doc_str: str = None
#  блок try для загрузки документации из README.MD
try:
    #  открываем файл документации в режиме чтения
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as settings_file:
        #  читаем содержимое файла
        doc_str = settings_file.read()
except FileNotFoundError as ex:
    #  Логируем ошибку, если файл не найден
    logger.error(f'Файл README.MD не найден: {ex}', exc_info=True)
    doc_str = '' #  Устанавливаем пустую строку, чтобы избежать ошибок при дальнейшей работе.
except Exception as ex:
    #  Логируем ошибку, если произошла другая ошибка при чтении файла
    logger.error(f'Ошибка чтения README.MD: {ex}', exc_info=True)
    doc_str = ''  #  Устанавливаем пустую строку, чтобы избежать ошибок при дальнейшей работе.

#  получаем имя проекта из настроек или устанавливаем значение по умолчанию
__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Имя проекта."""
#  получаем версию проекта из настроек или устанавливаем пустую строку по умолчанию
__version__: str = settings.get("version", '') if settings else ''
"""__version__ (str): Версия проекта."""
#  получаем документацию проекта или устанавливаем пустую строку по умолчанию
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Документация проекта."""
#  переменная для дополнительных деталей, пока не используется
__details__: str = ''
"""__details__ (str): Дополнительные детали проекта."""
#  получаем автора проекта из настроек или устанавливаем пустую строку по умолчанию
__author__: str = settings.get("author", '') if settings else ''
"""__author__ (str): Автор проекта."""
#  получаем информацию об авторских правах из настроек или устанавливаем пустую строку по умолчанию
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""__copyright__ (str): Информация об авторских правах проекта."""
#  получаем сообщение о кофе для разработчика из настроек или устанавливаем значение по умолчанию
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Сообщение о кофе для разработчика."""
```