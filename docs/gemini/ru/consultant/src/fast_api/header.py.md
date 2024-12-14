# Анализ кода модуля `header.py`

**Качество кода**
8
- Плюсы
    - Код структурирован и относительно легко читается.
    - Используются docstring для описания функций.
    - Присутствует обработка исключений при загрузке конфигурационных файлов.
    - Логика определения корневой директории проекта вынесена в отдельную функцию.
- Минусы
    - Отсутствует использование `j_loads` из `src.utils.jjson`.
    - Исключения обрабатываются через `...`, без логирования.
    - Не хватает комментариев в формате RST для всех переменных модуля.
    - Некоторые docstring требуют корректировки для соответствия RST.
    - Не все переменные модуля имеют аннотацию типов.

**Рекомендации по улучшению**

1. **Использовать `j_loads`**: Замените `json.load` на `j_loads` для загрузки JSON-файлов, обеспечивая более надежную обработку.
2. **Логирование ошибок**: Добавьте логирование ошибок с использованием `logger.error` вместо `...` для более информативной отладки.
3. **Документация RST**:  Приведите все docstring к формату RST. Добавьте описание модуля в формате RST. Добавьте документацию для всех переменных модуля.
4. **Уточнение типов**: Добавьте аннотации типов для всех переменных.
5. **Избегать `...`**: Замените `...` на конкретные действия, например, `return` или `pass`.
6. **Обработка ошибок**: Упростите обработку ошибок с помощью try/except блоков и логирования.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения настроек проекта и основных переменных
============================================================

Этот модуль определяет корневую директорию проекта, загружает настройки из `settings.json`
и извлекает метаданные проекта, такие как имя, версия, автор и описание из `settings.json`
и `README.MD` файлов.

Пример использования
--------------------

.. code-block:: python

   from src.fast_api.header import __project_name__, __version__, __doc__

   print(f"Имя проекта: {__project_name__}")
   print(f"Версия: {__version__}")
   print(f"Описание: {__doc__}")
"""
import sys
from pathlib import Path
from typing import Tuple, Dict, Any
#from json import load as j_load #  Импорт  j_loads перенесён в блок try
from packaging.version import Version

from src.logger.logger import logger #  Импорт модуля логирования
from src.utils.jjson import j_loads #  Импорт j_loads

MODE = 'dev'
"""Режим работы приложения (dev/prod)."""


def set_project_root(marker_files: Tuple[str, ...] = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с директории текущего файла,
    поиском вверх до первой директории, содержащей любой из маркерных файлов.

    :param marker_files: Кортеж с именами файлов или директорий для идентификации корня проекта.
    :type marker_files: Tuple[str, ...]
    :return: Путь к корневой директории, если она найдена, иначе директория, где находится скрипт.
    :rtype: Path
    """
    __root__: Path #  Объявление типа для __root__
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Код исполняет поиск корневой директории проекта
__root__: Path = set_project_root()
"""Путь к корневой директории проекта."""


from src import gs


settings: Dict[str, Any] = None
"""Словарь с настройками проекта."""
try:
    # Код исполняет открытие и чтение файла настроек settings.json
    with open(gs.path.root / 'src' /  'settings.json', 'r', encoding='utf-8') as settings_file:
        settings = j_loads(settings_file) #  Заменено на j_loads
except FileNotFoundError as e:
    # Код логирует ошибку, если файл настроек не найден
    logger.error(f'Файл настроек не найден: {e}')
    settings = {} #  Инициализация settings пустым словарем в случае ошибки
except Exception as e: #  Заменил json.JSONDecodeError на Exception
    # Код логирует ошибку, если не удалось прочитать или декодировать файл
    logger.error(f'Ошибка при чтении файла настроек: {e}')
    settings = {} #  Инициализация settings пустым словарем в случае ошибки


doc_str: str = None
"""Строка с содержимым файла README.MD."""
try:
     # Код исполняет открытие и чтение файла README.MD
    with open(gs.path.root / 'src' /  'README.MD', 'r', encoding='utf-8') as settings_file:
        doc_str = settings_file.read()
except FileNotFoundError as e:
    # Код логирует ошибку, если файл README.MD не найден
    logger.error(f'Файл README.MD не найден: {e}')
    doc_str = ''
except Exception as e:
    # Код логирует ошибку, если не удалось прочитать файл
    logger.error(f'Ошибка при чтении файла README.MD: {e}')
    doc_str = ''



__project_name__: str = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
"""Имя проекта."""
__version__: str = settings.get("version", '')  if settings  else ''
"""Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""Описание проекта."""
__details__: str = ''
"""Детали проекта."""
__author__: str = settings.get("author", '')  if settings  else ''
"""Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
"""Авторское право проекта."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""Ссылка на поддержку разработчика."""
```