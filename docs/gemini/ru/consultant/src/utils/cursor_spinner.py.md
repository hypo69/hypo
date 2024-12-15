# Анализ кода модуля `cursor_spinner.py`

**Качество кода**
8/10
-   **Плюсы**
    *   Код хорошо структурирован и понятен.
    *   Используется генератор для создания вращающегося курсора, что делает код более эффективным.
    *   Функции документированы с использованием docstring.
    *   Есть пример использования в `if __name__ == "__main__":`.

-   **Минусы**
    *   Отсутствует обработка исключений.
    *   Не используется `logger` для логирования.
    *   Комментарии в формате `reStructuredText (RST)` не везде корректны.
    *   Не указаны типы параметров и возвращаемых значений в docstring для `show_spinner`.

**Рекомендации по улучшению**

1.  Добавить импорт `from src.logger.logger import logger`.
2.  Использовать `logger.error` для логирования ошибок.
3.  Улучшить документацию в формате `reStructuredText (RST)`.
4.  Добавить типы параметров и возвращаемых значений в docstring для `show_spinner`.
5.  Исправить синтаксические ошибки в комментариях.
6.  Заменить избыточное использование `sys.stdout.write()` на более лаконичное использование форматирования строк.
7.  Добавить описание модуля в формате reStructuredText (RST).

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для отображения вращающегося курсора в консоли.
=====================================================

Этот модуль предоставляет утилиту для отображения вращающегося курсора в консоли,
чтобы имитировать процесс загрузки или ожидания.

Пример использования
--------------------

.. code-block:: python

    from src.utils.cursor_spinner import show_spinner

    show_spinner(duration=5.0, delay=0.1)
"""

import time
import sys
from src.logger.logger import logger # Импортируем logger

MODE = 'dev'

def spinning_cursor():
    """
    Генератор для вращающегося курсора.

    Этот генератор циклически проходит через символы |, /, -, \\.

    :yields: Символ из последовательности вращения курсора.
    :rtype: str
    """
    while True:
        for cursor in '|/-\\|': # исправлен символ
            yield cursor

def show_spinner(duration: float = 5.0, delay: float = 0.1) -> None:
    """
    Отображает вращающийся курсор в консоли в течение заданного времени.

    :param duration: Продолжительность отображения курсора в секундах. По умолчанию 5.0.
    :type duration: float
    :param delay: Задержка между каждым поворотом курсора в секундах. По умолчанию 0.1.
    :type delay: float
    :raises Exception: Если возникает ошибка во время работы с курсором.
    :rtype: None

    Пример:
        >>> show_spinner(duration=3.0, delay=0.2)  # Показывает спиннер в течение 3 секунд
    """
    spinner = spinning_cursor()
    end_time = time.time() + duration

    try:
        while time.time() < end_time:
            # Вывод символа курсора и его удаление
            sys.stdout.write(f'\r{next(spinner)}')
            sys.stdout.flush()
            time.sleep(delay)
    except Exception as e:
        logger.error(f'Ошибка при отображении курсора: {e}')
    finally:
        sys.stdout.write('\r')
        sys.stdout.flush()

if __name__ == "__main__":
    # Пример использования спиннера в скрипте
    print("Spinner for 5 seconds:")
    show_spinner(duration=5.0, delay=0.1)
    print("\nDone!")
```