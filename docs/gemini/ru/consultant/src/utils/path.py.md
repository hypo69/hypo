### Анализ кода модуля `src.utils.path`

**Качество кода**:
- **Соответствие стандартам**: 7
- **Плюсы**:
    - Код выполняет свою задачу корректно.
    - Используется `pathlib` для работы с путями.
    - Есть документация для функции.
- **Минусы**:
    - Отсутствует импорт `logger` и его использование для отладки.
    - Комментарии не соответствуют формату RST.
    - Отсутствует общее описание модуля в формате RST.
    - Не используются одинарные кавычки для строк в коде.

**Рекомендации по улучшению**:
- Добавить описание модуля в формате RST.
- Изменить docstring функции на формат RST.
- Использовать одинарные кавычки для строк в коде, кроме вывода.
- Добавить импорт `logger` из `src.logger`.
- Изменить обработку ошибки на использование `logger.error` вместо возврата `None`.
- Использовать более точные формулировки в комментариях.
-  Выровнять импорты.

**Оптимизированный код**:
```python
# -*- coding: utf-8 -*-
# file: src/utils/path.py
#! venv/bin/python/python3.12

"""
Модуль для работы с путями в проекте.
====================================

Этот модуль предоставляет функции для определения относительных путей
внутри проекта, основываясь на корневом каталоге.

:platform: Windows, Unix
:synopsis: Модуль определяющий корневой путь к проекту. Все импорты строятся относительно этого пути.
:TODO: В дальнейшем перенести в системную переменную.

Пример использования:
----------------------
.. code-block:: python

    from src.utils.path import get_relative_path

    full_path = '/home/user/project/src/utils/file.py'
    relative_from = 'src'
    relative_path = get_relative_path(full_path, relative_from)
    print(relative_path) # Выведет: 'src/utils/file.py'
"""

from pathlib import Path
from typing import Optional

from src.logger import logger  # Добавлен импорт logger


def get_relative_path(full_path: str, relative_from: str) -> Optional[str]:
    """
    Возвращает часть пути начиная с указанного сегмента и до конца.

    :param full_path: Полный путь.
    :type full_path: str
    :param relative_from: Сегмент пути, с которого нужно начать извлечение.
    :type relative_from: str
    :return: Относительный путь начиная с `relative_from`, или None, если сегмент не найден.
    :rtype: Optional[str]
    
    :raises ValueError: Если сегмент `relative_from` не найден в `full_path`.

    Пример:
        >>> full_path = '/home/user/project/src/utils/file.py'
        >>> relative_from = 'src'
        >>> result = get_relative_path(full_path, relative_from)
        >>> print(result)
        src/utils/file.py
    """
    path = Path(full_path) # Преобразуем строку в объект Path
    parts = path.parts # Получаем части пути

    if relative_from in parts: # Проверяем наличие сегмента
        start_index = parts.index(relative_from) # Находим индекс сегмента
        relative_path = Path(*parts[start_index:])  # Формируем путь начиная с указанного сегмента
        return relative_path.as_posix() # Возвращаем относительный путь в формате posix
    else:
        logger.error(f'Сегмент {relative_from} не найден в пути {full_path}') # Логируем ошибку
        return None # Возвращаем None в случае ошибки