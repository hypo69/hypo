# Анализ кода модуля `path`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и выполняет свою задачу.
    - Используются `Path` из `pathlib` для работы с путями, что обеспечивает кроссплатформенность.
    - Присутствует docstring для функции, что соответствует требованиям.
    - Используются `Optional` из `typing`.
- Минусы
    - Отсутствует описание модуля в начале файла.
    - Нет подробных комментариев в коде.
    - Нет `logger` для обработки ошибок.

**Рекомендации по улучшению**

1.  Добавить описание модуля в начале файла.
2.  Добавить подробные комментарии к коду, объясняющие логику работы.
3.  Использовать `logger` для обработки ошибок и логирования важных событий.
4.  Добавить примеры использования в docstring для функции `get_relative_path`.
5.  Улучшить форматирование docstring в соответствии со стандартами RST.
6.  Переименовать переменную `path` в `full_path_obj` для ясности.
7.  Добавить проверку на пустой `full_path` и `relative_from`

**Оптимизированный код**

```python
"""
Модуль для работы с путями в проекте.
=========================================================================================

Этот модуль предоставляет функцию :func:`get_relative_path`, которая используется для
получения относительного пути от заданного сегмента.

Пример использования
--------------------

Пример использования функции `get_relative_path`:

.. code-block:: python

    from pathlib import Path
    from src.utils.path import get_relative_path

    full_path = '/path/to/my/project/src/module.py'
    relative_from = 'src'
    relative_path = get_relative_path(full_path, relative_from)
    print(relative_path)  # Выведет: src/module.py

    relative_from = 'project'
    relative_path = get_relative_path(full_path, relative_from)
    print(relative_path) # Выведет: project/src/module.py

    relative_from = 'nonexistent'
    relative_path = get_relative_path(full_path, relative_from)
    print(relative_path) # Выведет: None
"""
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

from pathlib import Path
from typing import Optional
#  Импорт logger для логирования
from src.logger.logger import logger


def get_relative_path(full_path: str, relative_from: str) -> Optional[str]:
    """
    Возвращает часть пути начиная с указанного сегмента и до конца.

    Args:
        full_path (str): Полный путь.
        relative_from (str): Сегмент пути, с которого нужно начать извлечение.

    Returns:
        Optional[str]: Относительный путь начиная с `relative_from`, или None, если сегмент не найден.

    Example:
        >>> from pathlib import Path
        >>> full_path = '/path/to/my/project/src/module.py'
        >>> relative_from = 'src'
        >>> result = get_relative_path(full_path, relative_from)
        >>> print(result)
        src/module.py
    """
    # Проверка на пустой путь
    if not full_path:
        logger.error('`full_path` не может быть пустым')
        return None

    # Проверка на пустой relative_from
    if not relative_from:
        logger.error('`relative_from` не может быть пустым')
        return None
    
    # Преобразуем строку в объект Path
    full_path_obj = Path(full_path)
    # Разбиваем путь на сегменты
    parts = full_path_obj.parts

    #  Проверка, есть ли `relative_from` в частях пути
    if relative_from in parts:
        # Находим индекс сегмента `relative_from`
        start_index = parts.index(relative_from)
        # Формируем новый путь, начиная с индекса `relative_from`
        relative_path = Path(*parts[start_index:])
        # Возвращаем относительный путь в виде строки (posix)
        return relative_path.as_posix()
    else:
        # Если сегмент `relative_from` не найден, возвращаем None
        logger.debug(f'Сегмент `{relative_from}` не найден в пути `{full_path}`')
        return None
```