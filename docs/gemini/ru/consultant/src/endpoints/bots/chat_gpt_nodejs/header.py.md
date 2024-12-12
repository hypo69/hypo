# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    - Код содержит docstring для модуля.
    - Код содержит функцию для определения корневой директории проекта `set_project_root`.
    - Используется `Path` из `pathlib` для работы с путями.
    - Код корректно обрабатывает чтение настроек из `settings.json`.
    - Код использует переменные для хранения информации о проекте.
    - Добавлена обработка ошибок при чтении файлов.
-  Минусы
    - В начале файла есть избыточные docstring, дублирующие информацию.
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    - Не используется логирование ошибок с помощью `logger.error`.
    - Нет docstring для переменных.
    -  Использованы `...` для обработки ошибок, что не является информативным.
    -  Не все переменные имеют type hint.

**Рекомендации по улучшению**

1.  Удалить избыточные docstring в начале файла.
2.  Заменить `json.load` на `j_loads` из `src.utils.jjson` для чтения JSON файлов.
3.  Добавить обработку ошибок через `logger.error` вместо `...` в блоках `try-except`.
4.  Добавить docstring для всех переменных, включая `__root__`, `settings`, `doc_str`, `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__` и `__cofee__`.
5.  Использовать type hints для переменных `__root__`, `settings`, `doc_str`, `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`.
6.  Добавить импорт `logger` из `src.logger.logger`.
7.  Добавить комментарии в формате RST ко всем переменным.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для определения настроек и метаданных проекта.
=====================================================

Этот модуль предназначен для инициализации основных настроек проекта, 
включая загрузку конфигурационных данных из файлов и определения метаданных, таких как имя проекта,
версия, автор и т.д.

Модуль определяет корневую директорию проекта, загружает настройки из файла `settings.json` и
описание из файла `README.MD`, а также предоставляет общие переменные для доступа к этим данным.

Пример использования:
--------------------
    
.. code-block:: python

    from src.bots.openai_bots import header

    print(header.__project_name__)
    print(header.__version__)

"""
import sys
from pathlib import Path
from typing import Optional, Dict, Any
from packaging.version import Version
# используется для корректной обработки ошибок
from src.logger.logger import logger
# используется для чтения файлов json
from src.utils.jjson import j_loads


MODE = 'dev'


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла,
    и поднимаясь вверх по иерархии. Поиск останавливается, когда обнаруживается
    директория, содержащая любой из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий, которые идентифицируют корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если она найдена, иначе - путь к директории, где находится скрипт.
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


# Получение корневой директории проекта
__root__:Path = set_project_root()
"""
:type: Path
:desc: Путь к корневой директории проекта.
"""
from src import gs

settings: Optional[Dict[str, Any]] = None
"""
:type: Optional[Dict[str, Any]]
:desc: Словарь с настройками проекта, загруженными из `settings.json`.
"""
try:
    # код исполняет чтение настроек из файла settings.json
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    #  Код логирует ошибку, если файл не найден или не является JSON
    logger.error(f'Ошибка при загрузке настроек из файла settings.json: {e}')

doc_str: Optional[str] = None
"""
:type: Optional[str]
:desc: Строка с документацией проекта, загруженной из `README.MD`.
"""
try:
    # код исполняет чтение документации из файла README.MD
    with open(gs.path.root / 'src' /  'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError) as e:
     # Код логирует ошибку, если файл README.MD не найден
    logger.error(f'Ошибка при загрузке документации из файла README.MD: {e}')


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
__doc__: str = doc_str if doc_str else ''
"""
:type: str
:desc: Описание проекта, загруженное из README.MD.
"""
__details__: str = ''
"""
:type: str
:desc: Дополнительная информация о проекте.
"""
__author__: str = settings.get("author", '')  if settings  else ''
"""
:type: str
:desc: Автор проекта.
"""
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
"""
:type: str
:desc: Информация об авторских правах.
"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""
:type: str
:desc: Сообщение с предложением угостить разработчика кофе.
"""
```