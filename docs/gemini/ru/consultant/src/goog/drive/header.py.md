# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    - Код выполняет свою функцию по определению корневой директории проекта и загрузке настроек.
    - Используется `pathlib` для работы с путями, что делает код более читаемым и кроссплатформенным.
    - Присутствует обработка исключений для случаев, когда файлы настроек не найдены или повреждены.
    - Используются константы для хранения версии проекта и имени, что делает код более удобным для поддержки.
-  Минусы
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Отсутствует логирование ошибок при загрузке настроек и файла `README.MD`.
    - Комментарии в коде не соответствуют стандарту reStructuredText (RST).
    - Нет документации в формате RST для модуля.
    - Используется `...` в блоках `except`, что не является хорошей практикой (следует использовать `pass` или логирование ошибок).
    - Отсутствуют проверки на корректность полученных данных из `settings.json`.
    - Не все магические переменные документированы.
    - Код использует глобальные переменные.

**Рекомендации по улучшению**

1. **Импорты:**
   - Добавить `from src.utils.jjson import j_loads` и `from src.logger.logger import logger`.

2. **Использование `j_loads`:**
   - Заменить `json.load` на `j_loads` для загрузки `settings.json`.

3. **Логирование ошибок:**
   - Добавить логирование ошибок с помощью `logger.error` в блоках `except` для обработки исключений `FileNotFoundError` и `json.JSONDecodeError`.

4. **Формат документации:**
   - Переписать все комментарии и docstring в формате RST. Добавить docstring для модуля.

5. **Обработка исключений:**
   - Исключить использование `...` в блоках `except`, заменив их на `logger.error` и `pass`.

6. **Проверки данных:**
    - Проверять загруженные данные `settings` на наличие необходимых полей, чтобы избежать ошибок.

7. **Именование переменных:**
    - Имена переменных, используемых для хранения данных из json `settings`, следует вынести в константы или сделать именованными кортежами.

8. **Глобальные переменные:**
    - Рассмотреть возможность инкапсулировать глобальные переменные, например в класс.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для определения корневой директории проекта и загрузки основных настроек.
=============================================================================

Этот модуль предназначен для автоматического определения корневой директории проекта на основе наличия
маркерных файлов, таких как ``pyproject.toml``, ``requirements.txt``, или ``.git``. Также
модуль загружает настройки проекта из файла ``settings.json`` и устанавливает глобальные переменные
с информацией о проекте, такие как имя, версия и автор.

Пример использования
--------------------

.. code-block:: python

   from src.goog.drive.header import __project_name__, __version__, __doc__, __author__

   print(f"Project name: {__project_name__}")
   print(f"Version: {__version__}")
   print(f"Author: {__author__}")
"""
MODE = 'dev'

import sys
from pathlib import Path
from packaging.version import Version
# import json #  Используется j_loads
from src.utils.jjson import j_loads #  Импортируем j_loads для загрузки JSON
from src.logger.logger import logger #  Импортируем logger для логирования ошибок


def set_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневой каталог проекта.

    Функция осуществляет поиск корневого каталога проекта, начиная с директории текущего файла,
    и двигаясь вверх по структуре каталогов. Поиск останавливается, когда будет найден первый каталог,
    содержащий хотя бы один из маркерных файлов.

    :param marker_files: Кортеж имен файлов или директорий, которые используются для идентификации корневого каталога.
    :type marker_files: tuple
    :return: Путь к корневому каталогу, если найден. В противном случае, возвращается директория, где находится скрипт.
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


# Получаем корневой каталог проекта
__root__ = set_project_root()
"""__root__ (Path): Путь к корневому каталогу проекта."""

from src import gs

settings: dict = None
try:
    # Код загружает настройки из файла 'settings.json' с использованием j_loads
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except FileNotFoundError as e:
    # Логируем ошибку, если файл 'settings.json' не найден
    logger.error(f'Файл settings.json не найден: {e}')
    settings = {} # Устанавливаем пустой словарь, что бы избежать падения
except Exception as e:
    # Логируем ошибку, если возникли проблемы с декодированием JSON
    logger.error(f'Ошибка декодирования JSON в файле settings.json: {e}')
    settings = {}  # Устанавливаем пустой словарь, что бы избежать падения

doc_str: str = None
try:
    # Код загружает содержимое файла 'README.MD'
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except FileNotFoundError as e:
    # Логируем ошибку, если файл 'README.MD' не найден
    logger.error(f'Файл README.MD не найден: {e}')
    doc_str = '' # Устанавливаем пустую строку что бы избежать падения
except Exception as e:
     # Логируем ошибку, если возникли проблемы с чтением файла 'README.MD'
    logger.error(f'Ошибка чтения файла README.MD: {e}')
    doc_str = '' # Устанавливаем пустую строку что бы избежать падения

# Получаем данные из настроек
__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Имя проекта, полученное из settings.json или 'hypotez' по умолчанию."""
__version__: str = settings.get("version", '') if settings else ''
"""__version__ (str): Версия проекта, полученная из settings.json или '' по умолчанию."""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Содержимое файла README.MD или '' по умолчанию."""
__details__: str = ''
"""__details__ (str): Дополнительная информация о проекте."""
__author__: str = settings.get("author", '') if settings else ''
"""__author__ (str): Автор проекта, полученный из settings.json или '' по умолчанию."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""__copyright__ (str): Информация об авторских правах, полученная из settings.json или '' по умолчанию."""
__cofee__: str = settings.get("cofee",
                             "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Призыв поддержать разработчика, полученный из settings.json или строка по умолчанию."""
```