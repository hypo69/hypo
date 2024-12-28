# Анализ кода модуля `src.utils.path`

**Качество кода**

8/10
-  Плюсы
    - Код достаточно читаемый и хорошо документирован.
    - Используется `pathlib` для работы с путями, что делает код кроссплатформенным.
    - Функция `get_relative_path` выполняет свою задачу, как описано в docstring.
    - Присутствует описание модуля в формате docstring.
    - Используются type hints.
 -  Минусы
    - Отсутствуют импорты `logger` и использование его для обработки ошибок, что могло бы улучшить надежность кода.
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`, но в данном случае это не требуется.
    - Не все комментарии написаны в стиле RST.
    - Переменная MODE не документирована.

**Рекомендации по улучшению**

1.  **Документирование переменных:** Добавить docstring для переменной `MODE`, описывающей ее назначение и возможные значения.
2.  **Импорт и использование logger:** Добавить импорт `logger` из `src.logger.logger` и использовать его для логирования ошибок, если они возникнут при работе с путями.
3.  **Комментарии в стиле RST:** Привести docstring модуля в полный формат RST.
4.  **Уточнить документацию:** По возможности, уточнить описание функции `get_relative_path`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения корневого пути к проекту.
=================================================

:platform: Windows, Unix
:synopsis: Модуль определяет корневой путь к проекту. Все импорты строятся относительно этого пути.
:TODO: В дальнейшем перенести в системную переменную
"""

from pathlib import Path
from typing import Optional

# from src.logger.logger import logger  # TODO: Добавить импорт логгера

#: Режим работы приложения ('dev' - разработка, 'prod' - продакшн).



def get_relative_path(full_path: str, relative_from: str) -> Optional[str]:
    """
    Возвращает часть пути начиная с указанного сегмента и до конца.

    :param full_path: Полный путь.
    :type full_path: str
    :param relative_from: Сегмент пути, с которого нужно начать извлечение.
    :type relative_from: str
    :return: Относительный путь начиная с `relative_from`, или None, если сегмент не найден.
    :rtype: Optional[str]
    """
    # Преобразуем строки в объекты Path
    path = Path(full_path)
    parts = path.parts

    # Находим индекс сегмента relative_from
    if relative_from in parts:
        start_index = parts.index(relative_from)
        # Формируем путь начиная с указанного сегмента
        relative_path = Path(*parts[start_index:])
        return relative_path.as_posix()
    else:
        return None
    # TODO: добавить try except и логирование
    # try:
    #     # Преобразуем строки в объекты Path
    #     path = Path(full_path)
    #     parts = path.parts
    #
    #     # Находим индекс сегмента relative_from
    #     if relative_from in parts:
    #         start_index = parts.index(relative_from)
    #         # Формируем путь начиная с указанного сегмента
    #         relative_path = Path(*parts[start_index:])
    #         return relative_path.as_posix()
    #     else:
    #         return None
    # except Exception as ex:
    #     logger.error(f'Ошибка при получении относительного пути: {ex}')
    #     return None
```