# Анализ кода модуля `path`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и выполняет поставленную задачу.
    - Использует `pathlib` для работы с путями, что является хорошей практикой.
    - Есть  документация к функции в формате reStructuredText (RST)
    - Присутствует описание модуля
- Минусы
    - Отсутствует импорт `logger`
    - Нет обработки ошибок.
    - Не стандартизированы комментарии.

**Рекомендации по улучшению**
1.  Добавить импорт `logger` из `src.logger.logger`.
2.  Добавить обработку ошибок с помощью `try-except` и логирование ошибок через `logger.error`.
3.  Стандартизировать комментарии, сделав их более подробными.
4.  Переписать код с использованием одинарных кавычек в Python коде, и двойных только в операциях вывода.
5.  Устранить лишний комментарий.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

"""
Модуль для работы с путями в проекте.
=====================================

Этот модуль предоставляет утилиты для определения относительных путей,
используя абсолютные пути и точку отсчета.

.. moduleauthor:: Timofey <timofey@mail.ru>

:platform: Windows, Unix
:synopsis: Модуль определяет корневой путь к проекту. Все импорты строятся относительно этого пути.
    :TODO: В дальнейшем перенести в системную переменную
"""

from pathlib import Path
from typing import Optional
from src.logger.logger import logger  # импортируем logger

def get_relative_path(full_path: str, relative_from: str) -> Optional[str]:
    """
    Возвращает часть пути начиная с указанного сегмента и до конца.

    :param full_path: Полный путь.
    :type full_path: str
    :param relative_from: Сегмент пути, с которого нужно начать извлечение.
    :type relative_from: str
    :return: Относительный путь начиная с `relative_from`, или None, если сегмент не найден.
    :rtype: Optional[str]
    :raises Exception: в случае ошибки при обработке пути
    
    Example:
        >>> get_relative_path('/home/user/project/src/utils', 'src')
        'src/utils'
        >>> get_relative_path('/home/user/project/src/utils', 'project')
        'project/src/utils'
        >>> get_relative_path('/home/user/project/src/utils', 'not_exist') is None
        True
    """
    try:
        # Преобразуем строки в объекты Path
        path = Path(full_path)
        parts = path.parts

        # Проверяем наличие сегмента relative_from в parts
        if relative_from in parts:
            # Находим индекс сегмента relative_from
            start_index = parts.index(relative_from)
            # Формируем путь начиная с указанного сегмента
            relative_path = Path(*parts[start_index:])
            return relative_path.as_posix()
        else:
            # Если сегмент не найден, возвращаем None
            return None
    except Exception as ex:
        # Логируем ошибку и возвращаем None
        logger.error(f'Ошибка при обработке пути: {full_path}, relative_from: {relative_from}', exc_info=ex)
        return None

```