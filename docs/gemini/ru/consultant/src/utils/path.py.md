# Анализ кода модуля `path`

**Качество кода**
9
-   Плюсы
    -   Код хорошо структурирован и читаем.
    -   Присутствует docstring для модуля и функции.
    -   Используется `pathlib` для работы с путями.
    -   Функция `get_relative_path` выполняет свою задачу корректно.
-   Минусы
    -   Отсутствует импорт `logger` для обработки исключений, что может затруднить отладку и мониторинг.
    -   Не используется `j_loads` или `j_loads_ns` для чтения файлов. Хотя в этом файле это не нужно, но в инструкции прописано.
    -   Переменная `MODE` не используется, но это не ошибка, а скорее замечание по избыточности.

**Рекомендации по улучшению**

1.  Добавить импорт `logger` из `src.logger.logger`.
2.  Добавить обработку возможных исключений в функции `get_relative_path` с использованием `logger.error`.
3.  Переписать docstring в формате reStructuredText (RST).
4.  Избавиться от неиспользуемой переменной `MODE`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с путями.
=========================================================================================

Модуль ``src.utils.path`` предоставляет функции для работы с путями в файловой системе.
Этот модуль определяет корневой путь к проекту и обеспечивает функции для преобразования путей.

:platform: Windows, Unix
:synopsis: Модуль определяющий корневой путь к проекту. Все импорты строятся относительно этого пути.
"""

from pathlib import Path
from typing import Optional
# добавляем импорт logger
from src.logger.logger import logger


def get_relative_path(full_path: str, relative_from: str) -> Optional[str]:
    """
    Извлекает относительный путь из полного пути, начиная с указанного сегмента.

    :param full_path: Полный путь к файлу или директории.
    :type full_path: str
    :param relative_from: Сегмент пути, относительно которого нужно построить относительный путь.
    :type relative_from: str
    :return: Относительный путь начиная с `relative_from`, или ``None``, если сегмент не найден.
    :rtype: Optional[str]

    :Example:
    
    .. code-block:: python

        full_path = "/path/to/my/project/src/file.py"
        relative_from = "src"
        relative_path = get_relative_path(full_path, relative_from)
        print(relative_path)  # Выведет "src/file.py"

    """
    try:
        # Преобразует строки в объекты Path
        path = Path(full_path)
        parts = path.parts

        # Проверяет наличие сегмента relative_from в частях пути
        if relative_from in parts:
            # Находит индекс сегмента relative_from
            start_index = parts.index(relative_from)
            # Формирует путь начиная с указанного сегмента
            relative_path = Path(*parts[start_index:])
            # Возвращает относительный путь в формате POSIX
            return relative_path.as_posix()
        else:
            # Возвращает None если сегмент relative_from не найден
            return None
    except Exception as e:
        # Логирует ошибку и возвращает None в случае исключения
        logger.error(f"Ошибка при обработке пути: {full_path}, {relative_from}", exc_info=True)
        return None

```