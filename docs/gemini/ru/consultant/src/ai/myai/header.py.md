# Анализ кода модуля `header.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и выполняет поставленные задачи.
    - Присутствует функция для определения корневой директории проекта.
    - Используются константы для хранения метаданных проекта.
    - Имеется базовая обработка ошибок при чтении файлов настроек.
    - Присутствуют docstring для функций и модуля.

- Минусы
    - Отсутствуют некоторые необходимые импорты (например `from src.utils.jjson import j_loads` и `from src.logger.logger import logger`).
    - Используется стандартный `json.load` вместо `j_loads`.
    - Излишние комментарии в виде docstring в начале файла.
    - Не все переменные имеют docstring.
    - Обработка ошибок при чтении файлов настроек не использует `logger.error`.
    - Не все переменные типа `str` имеют аннотацию типа.
    - Отсутствует полное описание модуля в начале файла.
    - Не используются одинарные кавычки.
    - Проверка `settings`  перед получением значений переменных.

**Рекомендации по улучшению**

1.  **Импорты:** Добавить необходимые импорты из `src.utils.jjson` и `src.logger.logger`.
2.  **`json.load`:** Заменить `json.load` на `j_loads` или `j_loads_ns`.
3.  **Docstring:** Улучшить docstring для модуля, добавив описание и пример использования.
4.  **Обработка ошибок:** Использовать `logger.error` для логирования ошибок при чтении файлов.
5.  **Комментарии:** Добавить подробные комментарии после `#`, объясняющие логику кода.
6. **Аннотации типов:** Добавить аннотации типа `str` к переменным.
7. **Унификация кавычек:** Использовать везде одинарные кавычки, кроме `print`, `input` и `logger`.
8. **Проверка наличия настроек:** Упростить проверку наличия `settings` при присваивании метаданных.
9. **Убрать лишние комментарии**: Убрать лишние комментарии в виде docstring

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для определения корневой директории проекта и загрузки его настроек.
=========================================================================================

Этот модуль содержит функции для определения корневой директории проекта, загрузки настроек
из файла `settings.json`, а также чтения документации из файла `README.MD`.
Модуль также определяет основные метаданные проекта, такие как имя, версия, автор и т.д.

Пример использования
--------------------

Для использования модуля необходимо импортировать его и получить доступ к переменным,
содержащим метаданные проекта.

.. code-block:: python

    from src.ai.myai.header import __project_name__, __version__, __author__, __doc__

    print(f"Project Name: {__project_name__}")
    print(f"Version: {__version__}")
    print(f"Author: {__author__}")
    print(f"Documentation: {__doc__}")
"""

#! venv/bin/python/python3.12

import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads # импорт j_loads из src.utils.jjson
from src.logger.logger import logger # импорт logger из src.logger.logger


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Определяет корневую директорию проекта, начиная с директории текущего файла,
    и двигаясь вверх до первой директории, содержащей один из маркерных файлов.

    Args:
        marker_files (tuple): Кортеж имен файлов или директорий, используемых для идентификации корня проекта.

    Returns:
        Path: Путь к корневой директории, если она найдена, иначе - директория, где находится скрипт.
    """
    __root__: Path # Объявляем переменную для хранения корневой директории
    current_path: Path = Path(__file__).resolve().parent # Получаем абсолютный путь к директории текущего файла
    __root__ = current_path # Изначально устанавливаем корневой директорией текущую
    # Проходим по всем родительским директориям, включая текущую
    for parent in [current_path] + list(current_path.parents):
        # Проверяем, существует ли маркерный файл в текущей родительской директории
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent # Если маркерный файл найден, устанавливаем эту директорию как корневую
            break # Прерываем цикл
    if __root__ not in sys.path: # Если корневая директория не в списке путей
        sys.path.insert(0, str(__root__)) # Добавляем корневую директорию в начало списка
    return __root__ # Возвращаем путь к корневой директории


# Вызов функции для определения корневой директории проекта
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта"""

from src import gs

settings: dict | None = None
try:
    #  Чтение настроек из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file) # используется j_loads для чтения json
except (FileNotFoundError, json.JSONDecodeError) as e:
    logger.error(f'Ошибка при чтении файла настроек: {e}') # Логирование ошибки при чтении файла
    ... # точка остановки

doc_str: str | None = None
try:
    # Чтение документации из файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as doc_file:
        doc_str = doc_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    logger.error(f'Ошибка при чтении файла документации: {e}') # Логирование ошибки при чтении файла
    ... # точка остановки

# Получение метаданных проекта из настроек или установка значений по умолчанию
__project_name__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Имя проекта."""
__version__: str = settings.get('version', '') if settings else ''
"""__version__ (str): Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Документация проекта."""
__details__: str = ''
"""__details__ (str): Детали проекта."""
__author__: str = settings.get('author', '') if settings else ''
"""__author__ (str): Автор проекта."""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""__copyright__ (str): Информация об авторских правах."""
__cofee__: str = settings.get('cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69') if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
"""__cofee__ (str): Сообщение о кофе для разработчика."""
```