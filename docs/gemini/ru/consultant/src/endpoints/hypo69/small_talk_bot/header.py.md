# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    - Код имеет базовую структуру и выполняет свою функцию.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Присутствует обработка ошибок при загрузке `settings.json` и `README.MD`.
    - Вынесение логики поиска корневой директории в отдельную функцию `set_project_root`.
 -  Минусы
    - Отсутствует reStructuredText (RST) документация.
    - Используется стандартный `json.load`, вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Не используется логирование ошибок.
    - Есть некоторые сокращения имен переменных.
    - Используется `try-except` блоки с многоточием `...`, без обработки ошибок.

**Рекомендации по улучшению**

1.  Добавить reStructuredText (RST) документацию для модуля, функций и переменных.
2.  Заменить стандартный `json.load` на `j_loads` из `src.utils.jjson`.
3.  Использовать `from src.logger.logger import logger` для логирования ошибок.
4.  Уточнить имена переменных для лучшей читаемости.
5.  Удалить многоточие `...` и добавить логирование ошибок.
6.  Добавить проверку наличия `settings` перед доступом к его ключам.
7.  Добавить проверку на существование `gs.path.root`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения корневой директории проекта и загрузки основных настроек.
=================================================================================

Этот модуль определяет корневую директорию проекта на основе наличия файлов маркеров, таких как `pyproject.toml`, `requirements.txt` или `.git`.
Он также загружает настройки из файла `settings.json` и документацию из `README.MD`,
а также устанавливает глобальные переменные проекта.

Пример использования
--------------------

.. code-block:: python

    from src.endpoints.hypo69.small_talk_bot import header

    # Доступ к переменным проекта
    print(header.__project_name__)
    print(header.__version__)
"""
import sys
from pathlib import Path
from packaging.version import Version

from src.utils.jjson import j_loads  #  Импортируем j_loads
from src.logger.logger import logger # импортируем logger

MODE = 'dev'

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с директории текущего файла.

    Поиск идет вверх по директориям до тех пор, пока не будет найдена директория, содержащая хотя бы один из файлов-маркеров.

    :param marker_files: Кортеж с именами файлов или директорий, которые идентифицируют корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории.
    :rtype: Path
    :raises FileNotFoundError: Если корневая директория не найдена.

    """
    current_path: Path = Path(__file__).resolve().parent #  Получаем абсолютный путь к директории, содержащей текущий файл
    __root__ = current_path  #  Устанавливаем начальное значение корневой директории
    for parent in [current_path] + list(current_path.parents):  #  Проходим по текущей директории и ее родительским директориям
        if any((parent / marker).exists() for marker in marker_files):  #  Проверяем, есть ли хотя бы один из файлов-маркеров в текущей директории
            __root__ = parent #  Обновляем корневую директорию
            break #  Выходим из цикла, так как корень найден
    if __root__ not in sys.path:  #  Проверяем, добавлен ли путь к корневой директории в sys.path
        sys.path.insert(0, str(__root__)) #  Добавляем путь к корневой директории в начало sys.path
    return __root__

# Get the root directory of the project
__root__: Path = set_project_root()  #  Находим и устанавливаем корневую директорию проекта

"""__root__ (Path): Path to the root directory of the project"""

from src import gs

settings: dict = {}  #  Инициализируем settings как пустой словарь
try:
    #  Проверяем, существует ли gs.path.root
    if not gs.path.root:
        logger.error('gs.path.root не определен') # логируем ошибку
        raise FileNotFoundError('gs.path.root не определен')# вызываем исключение
    #  Пытаемся открыть и загрузить файл settings.json с использованием j_loads
    with open(gs.path.root / 'src' / 'settings.json', 'r', encoding='utf-8') as settings_file: #  Открываем файл настроек для чтения
        settings = j_loads(settings_file) #  Загружаем настройки из файла в словарь settings
except FileNotFoundError as e:
    logger.error(f'Файл settings.json не найден: {e}') # логируем ошибку
    ... #  Оставляем многоточие так как оно не несет функционала
except Exception as e: #  Обрабатываем другие исключения
    logger.error(f'Ошибка загрузки настроек из settings.json: {e}') #  Логируем ошибку загрузки настроек
    ... #  Оставляем многоточие так как оно не несет функционала

doc_str: str = ''  #  Инициализируем doc_str как пустую строку
try:
    # Проверяем, существует ли gs.path.root
    if not gs.path.root:
        logger.error('gs.path.root не определен') # логируем ошибку
        raise FileNotFoundError('gs.path.root не определен') # вызываем исключение
    #  Пытаемся открыть и прочитать файл README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as readme_file:  #  Открываем файл README.MD для чтения
        doc_str = readme_file.read()  #  Считываем содержимое файла в строку doc_str
except FileNotFoundError as e:
    logger.error(f'Файл README.MD не найден: {e}')  #  Логируем ошибку если файл не найден
    ...  #  Оставляем многоточие так как оно не несет функционала
except Exception as e: # Обрабатываем другие исключения
    logger.error(f'Ошибка чтения файла README.MD: {e}')  #  Логируем ошибку чтения файла
    ... #  Оставляем многоточие так как оно не несет функционала

__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez' #  Получаем имя проекта из настроек или устанавливаем значение по умолчанию
"""__project_name__ (str): Имя проекта"""
__version__: str = settings.get("version", '') if settings else '' #  Получаем версию проекта из настроек или устанавливаем значение по умолчанию
"""__version__ (str): Версия проекта"""
__doc__: str = doc_str if doc_str else '' #  Устанавливаем документацию проекта
"""__doc__ (str): Документация проекта"""
__details__: str = '' #  Инициализируем __details__ как пустую строку
"""__details__ (str): Детали проекта"""
__author__: str = settings.get("author", '') if settings else '' #  Получаем автора проекта из настроек или устанавливаем значение по умолчанию
"""__author__ (str): Автор проекта"""
__copyright__: str = settings.get("copyrihgnt", '') if settings else '' #  Получаем копирайт проекта из настроек или устанавливаем значение по умолчанию
"""__copyright__ (str): Копирайт проекта"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69" #  Получаем сообщение о кофе из настроек или устанавливаем значение по умолчанию
"""__cofee__ (str): Сообщение о кофе"""
```