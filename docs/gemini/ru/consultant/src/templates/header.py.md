# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    -  Код выполняет поставленную задачу по определению корневой директории проекта.
    -  Используется `pathlib` для работы с путями, что является хорошей практикой.
    -  Добавлен комментарий для переменной `__root__`
-  Минусы
    -  Отсутствует описание модуля в формате reStructuredText.
    -  Функция `set_project_root` не имеет документации в формате RST.
    -  Используется стандартный `json`, необходимо заменить на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -  Нет явной обработки исключений.
    -  Не хватает логирования.
    -  Присутствует избыточное приведение типов, которое можно убрать.
    -   Импорт `gs` не используется и его необходимо удалить.

**Рекомендации по улучшению**

1.  Добавить описание модуля в формате RST.
2.  Добавить документацию к функции `set_project_root` в формате RST.
3.  Заменить использование стандартного `json` на `j_loads` или `j_loads_ns` из `src.utils.jjson`, если требуется. В данном коде использование `json` не требуется.
4.  Добавить обработку исключений с использованием `logger.error`.
5.  Убрать неиспользуемый импорт `gs`.
6.  Убрать избыточное приведение типов.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения корневой директории проекта.
=====================================================

Этот модуль содержит функцию :func:`set_project_root`, которая используется для
определения корневой директории проекта на основе списка маркерных файлов.

Пример использования
--------------------

.. code-block:: python

    from pathlib import Path
    from src.templates.header import set_project_root

    root_path = set_project_root()
    print(root_path)
"""
import sys
# избыточное импортирование json
# import json
from packaging.version import Version
from pathlib import Path

from src.logger.logger import logger # Импортируем logger


MODE = 'dev'


def set_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с директории текущего файла.

    Поиск идёт вверх по дереву каталогов до первого каталога, содержащего любой из маркерных файлов.

    :param marker_files: Кортеж имен файлов или каталогов для идентификации корневой директории проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если она найдена, иначе - директория, где расположен скрипт.
    :rtype: Path
    """
    current_path: Path = Path(__file__).resolve().parent
    root_path: Path = current_path
    # Цикл по текущей директории и всем ее родительским директориям.
    for parent in [current_path] + list(current_path.parents):
        # Проверяет наличие любого из маркерных файлов в текущей директории.
        if any((parent / marker).exists() for marker in marker_files):
            root_path = parent
            break
    # Проверяет, что корневая директория не была добавлена в sys.path
    if root_path not in sys.path:
        # Добавляет корневую директорию в sys.path для возможности импорта модулей
        sys.path.insert(0, str(root_path))
    return root_path

# Получение корневой директории проекта
__root__ = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта."""

# Удаляем неиспользуемый импорт
# from src import gs
```