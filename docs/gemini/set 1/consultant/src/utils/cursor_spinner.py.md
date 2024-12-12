# Анализ кода модуля `cursor_spinner`

**Качество кода**
7
-   Плюсы
    -   Код выполняет свою задачу по отображению спиннера.
    -   Используются генераторы для создания анимации, что является хорошей практикой.
    -   Присутствует базовая документация в формате docstring.
    -   Есть пример использования в `if __name__ == "__main__":`.
-   Минусы
    -   Отсутствует импорт `logger` для логирования ошибок.
    -   Не используется reStructuredText (RST) для docstring и комментариев.
    -   Нет обработки исключений.
    -   Нет явного указания кодировки utf-8 в начале файла.

**Рекомендации по улучшению**
1.  Добавить импорт `logger` из `src.logger.logger`.
2.  Переписать docstring в формате reStructuredText (RST).
3.  Добавить обработку возможных ошибок (хотя бы общего `Exception`).
4.  Обеспечить соответствие PEP8 (например, добавить пустые строки между функциями).
5.  Явно указать кодировку utf-8 в начале файла.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для отображения спиннера в консоли.
===================================================

Этот модуль предоставляет утилиту для отображения вращающегося курсора в консоли,
чтобы имитировать процесс загрузки или ожидания.

Пример использования
--------------------

.. code-block:: python

    from src.utils.cursor_spinner import show_spinner

    show_spinner(duration=3.0, delay=0.2)  # Отображает спиннер в течение 3 секунд
"""

import time
import sys
# Импорт logger для логирования ошибок
from src.logger.logger import logger


MODE = 'dev'


def spinning_cursor():
    """
    Генератор для вращающегося курсора, который циклически перебирает символы |, /, -, \\.

    :yield: Следующий символ в последовательности курсора.
    :rtype: str

    Пример:
        >>> cursor = spinning_cursor()
        >>> next(cursor)  # '|'
        >>> next(cursor)  # '/'
        >>> next(cursor)  # '-'
        >>> next(cursor)  # '\\'
    """
    while True:
        for cursor in '|/-\\':
            yield cursor


def show_spinner(duration: float = 5.0, delay: float = 0.1):
    """
    Отображает вращающийся курсор в консоли в течение указанного времени.

    :param duration: Продолжительность работы спиннера в секундах. По умолчанию 5.0.
    :type duration: float
    :param delay: Задержка между каждым вращением в секундах. По умолчанию 0.1.
    :type delay: float

    Пример:
        >>> show_spinner(duration=3.0, delay=0.2)  # Отображает спиннер в течение 3 секунд
    """
    spinner = spinning_cursor()
    end_time = time.time() + duration

    try:
        while time.time() < end_time:
            # код исполняет вывод следующего символа спиннера
            sys.stdout.write(next(spinner))
            # код исполняет принудительный вывод в консоль
            sys.stdout.flush()
            # код ожидает заданную задержку
            time.sleep(delay)
            # код исполняет возврат каретки, чтобы перезаписать символ
            sys.stdout.write('\b')
    except Exception as ex:
        # Логирование ошибки
        logger.error('Произошла ошибка при работе спиннера', exc_info=ex)


if __name__ == "__main__":
    # Пример использования спиннера в скрипте
    print("Spinner for 5 seconds:")
    show_spinner(duration=5.0, delay=0.1)
    print("\nDone!")
```