# Анализ кода модуля `header.py`

**Качество кода**
8
-   Плюсы
    -   Код соответствует PEP 8.
    -   Присутствует базовая документация.
    -   Используется `pathlib` для работы с путями.
    -   Присутствует обработка ошибок при загрузке JSON и README.
-   Минусы
    -   Не используется reStructuredText (RST) для комментариев и docstring.
    -   Используется `json.load` вместо `j_loads` или `j_loads_ns`.
    -   Отсутствует импорт `logger` для логирования ошибок.
    -   Используется `try-except` с `...` вместо логирования ошибок.
    -   Комментарии `#` не соответствуют инструкциям по оформлению.
    -   Не все переменные аннотированы типами.
    -   Не все переменные и функции имеют документацию.
    -   Не производится проверка на наличие ключей в словаре `settings` перед обращением к ним через `.get()`.

**Рекомендации по улучшению**

1.  **Импорты**:
    -   Добавить импорт `from src.utils.jjson import j_loads` и `from src.logger.logger import logger`.
2.  **Использование** `j_loads`:
    -   Заменить `json.load` на `j_loads` для загрузки `settings.json`.
3.  **Логирование ошибок**:
    -   Заменить `...` в блоках `try-except` на `logger.error`.
4.  **Документация**:
    -   Переписать комментарии и docstring в формате RST.
    -   Добавить аннотации типов для всех переменных.
5.  **Проверка ключей**:
    -   Добавить проверку наличия ключей в словаре `settings` перед вызовом `.get()`.
6. **Обновление комментариев**:
    -   Все комментарии `#` должны быть переписаны с подробными пояснениями.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для определения и установки корневой директории проекта,
а также загрузки настроек и документации.
=========================================================================================

Этот модуль предоставляет функции и переменные, необходимые для инициализации проекта.
Он устанавливает корневую директорию, загружает настройки из JSON файла и
содержит информацию о проекте, такую как имя, версия, автор и т.д.

Использование
------------

Для использования модуля, импортируйте его и получите доступ к переменным
проекта:

.. code-block:: python

    from src.suppliers.hb import header
    print(header.__project_name__)
    print(header.__version__)
"""

MODE: str = 'dev'

import sys
from pathlib import Path
from packaging.version import Version
# импортируем j_loads из src.utils.jjson
from src.utils.jjson import j_loads
# импортируем logger из src.logger.logger
from src.logger.logger import logger


def set_project_root(marker_files: tuple = ('__root__',)) -> Path:
    """
    Определяет корневую директорию проекта, начиная с директории текущего файла.

    Поиск идет вверх по структуре каталогов до тех пор, пока не будет найден
    каталог, содержащий один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий, которые идентифицируют корневой каталог проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если она найдена, иначе путь к директории, где расположен скрипт.
    :rtype: Path
    """
    __root__: Path
    # получаем абсолютный путь к текущему файлу и его родительской директории
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    # проходим по всем родительским директориям, включая текущую
    for parent in [current_path] + list(current_path.parents):
        # если в текущей директории найден хотя бы один из файлов-маркеров
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    # если корневая директория не в списке путей, добавляем ее
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# устанавливаем корневую директорию проекта
__root__: Path = set_project_root()
"""Path: Путь к корневой директории проекта."""

from src import gs

settings: dict = None
try:
    # загружаем настройки из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        # используем j_loads для загрузки данных из JSON файла
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    # логируем ошибку, если файл не найден или не может быть декодирован
    logger.error(f"Ошибка загрузки файла настроек: {e}")


doc_str: str = None
try:
    # читаем содержимое файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
     # логируем ошибку, если файл не найден или не может быть прочитан
    logger.error(f"Ошибка загрузки файла документации: {e}")



# определяем имя проекта из настроек, если они есть
__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
# определяем версию проекта из настроек, если они есть
__version__: str = settings.get("version", '') if settings else ''
# определяем документацию проекта из файла, если он прочитан
__doc__: str = doc_str if doc_str else ''
__details__: str = ''
# определяем автора проекта из настроек, если они есть
__author__: str = settings.get("author", '') if settings else ''
# определяем копирайт проекта из настроек, если они есть
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
# определяем сообщение о кофе из настроек, если они есть, иначе используем сообщение по умолчанию
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```