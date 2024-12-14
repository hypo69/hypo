# Анализ кода модуля `src.utils.path`

**Качество кода**
9
 -  Плюсы
        - Код хорошо структурирован и легко читается.
        - Используется `pathlib` для работы с путями, что делает код более кроссплатформенным.
        - Функция `get_relative_path` имеет docstring, описывающий ее назначение, параметры и возвращаемое значение.
 -  Минусы
    - Отсутствуют импорты из `src.logger.logger`, необходимо добавить для логирования.
    - Нет обработки ошибок при работе с путями.

**Рекомендации по улучшению**

1.  Добавить логирование ошибок с использованием `src.logger.logger`.
2.  Улучшить комментарии в формате reStructuredText (RST), включая более подробное описание модуля и функции.
3.  Добавить обработку возможных ошибок при работе с путями.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с путями в проекте.
=====================================

Этот модуль предоставляет функции для работы с путями файлов и каталогов.
Основной функциональностью является определение корневого пути проекта
и получение относительных путей от заданного сегмента.

.. moduleauthor::  Hypotez
"""

MODE = 'dev'

from pathlib import Path
from typing import Optional
from src.logger.logger import logger # Добавлен импорт для логирования


def get_relative_path(full_path: str, relative_from: str) -> Optional[str]:
    """
    Возвращает относительный путь начиная с указанного сегмента.

    :param full_path: Полный путь.
    :type full_path: str
    :param relative_from: Сегмент пути, с которого нужно начать извлечение.
    :type relative_from: str
    :return: Относительный путь начиная с `relative_from`, или None, если сегмент не найден.
    :rtype: Optional[str]
    
    :raises TypeError: Если `full_path` или `relative_from` не являются строками.
    :raises Exception: Если возникает ошибка при работе с путями.

    Пример использования:
    
    .. code-block:: python

       path = get_relative_path("/home/user/project/src/utils", "src")
       print(path)
    """
    try:
        # Преобразуем строки в объекты Path
        if not isinstance(full_path, str) or not isinstance(relative_from, str): # Проверка типа входных параметров
            logger.error(f'Неверный тип данных. full_path: {type(full_path)=} relative_from: {type(relative_from)=}') # Логирование ошибки типа
            raise TypeError('Аргументы `full_path` и `relative_from` должны быть строками')# Вывод ошибки типа
        path = Path(full_path) # Создаем объект Path
        parts = path.parts # Получаем части пути
        # Находим индекс сегмента relative_from
        if relative_from in parts: # Проверка наличия сегмента в пути
            start_index = parts.index(relative_from) # Код получает индекс сегмента
            # Формируем путь начиная с указанного сегмента
            relative_path = Path(*parts[start_index:]) # Создаем новый объект Path с относительным путем
            return relative_path.as_posix() # Код преобразует путь в строку posix
        else:
            logger.debug(f'Сегмент "{relative_from}" не найден в пути "{full_path}"') # Логирование, если сегмент не найден
            return None
    except Exception as ex:
        logger.error(f'Ошибка при работе с путями: {ex}') # Логирование любых других ошибок
        return None
```