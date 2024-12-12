# Анализ кода модуля `date_time`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и выполняет поставленные задачи.
    - Присутствует базовая документация к функциям и классам.
    - Используется многопоточность для реализации таймаутов.
-  Минусы
    - Не хватает обработки ошибок и логирования.
    - Не используются константы для значений по умолчанию.
    - Не все комментарии соответствуют стандарту reStructuredText.
    - Есть избыточное использование `print` для сообщений, лучше использовать `logger`
    - Не хватает docstring для модуля

**Рекомендации по улучшению**

1.  **Документация:**
    -   Добавить описание модуля в формате reStructuredText.
    -   Переписать все docstring в формате reStructuredText, соблюдая стандарты оформления.
2.  **Логирование:**
    -   Использовать `logger.error` для логирования ошибок вместо `print`.
    -   Добавить логирование для разных событий (например, успешная проверка интервала, таймаут).
3.  **Обработка ошибок:**
    -   Добавить обработку исключений в функции `interval` и `get_input` с использованием `try-except` и `logger.error`.
4.  **Константы:**
    -   Использовать константы для значений по умолчанию (например, время начала и конца интервала, таймаут).
5.  **Улучшение функции `interval_with_timeout`:**
    -   Убрать дублирующийся `thread.join()` после таймаута.
    -   Сделать более явным возвращаемое значение при таймауте.
6.  **Улучшение функции `input_with_timeout`:**
    -   Возвращать None явно при таймауте.
    -   Добавить `try-except` для обработки возможных ошибок.

**Оптимизиробанный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с датой и временем
=========================================================================================

Этот модуль предоставляет класс :class:`TimeoutCheck`, который используется для проверки,
находится ли текущее время в заданном интервале, и ожидания ввода от пользователя с тайм-аутом.

Класс содержит следующие методы:

    - ``interval``: Проверяет, находится ли текущее время в заданном интервале.
    - ``interval_with_timeout``: Проверяет, находится ли текущее время в заданном интервале с таймаутом.
    - ``get_input``: Запрашивает ввод от пользователя.
    - ``input_with_timeout``: Ожидает ввод от пользователя с таймаутом.

Пример использования
--------------------

Пример использования класса ``TimeoutCheck``:

.. code-block:: python

    timeout_check = TimeoutCheck()
    if timeout_check.interval_with_timeout(timeout=5):
        print("Current time is within the interval.")
    else:
        print("Current time is outside the interval or timeout occurred.")
"""
from datetime import datetime, time
import threading
from src.logger.logger import logger  #  Импортирован logger

MODE = 'dev'

DEFAULT_START_TIME = time(23, 0)
DEFAULT_END_TIME = time(6, 0)
DEFAULT_TIMEOUT = 5


class TimeoutCheck:
    """
    Класс для проверки временных интервалов и ожидания ввода с таймаутом.
    """
    def __init__(self):
        """
        Инициализирует объект класса TimeoutCheck.
        """
        self.result = None
        self.user_input = None # Инициализация user_input

    def interval(self, start: time = DEFAULT_START_TIME, end: time = DEFAULT_END_TIME) -> bool:
        """
        Проверяет, находится ли текущее время в заданном интервале.

        :param start: Начало интервала (по умолчанию 23:00).
        :type start: time
        :param end: Конец интервала (по умолчанию 06:00).
        :type end: time
        :return: True, если текущее время находится в интервале, иначе False.
        :rtype: bool
        """
        try:
            current_time = datetime.now().time()
            if start < end:
                # Проверка интервала в пределах одного дня
                self.result = start <= current_time <= end
            else:
                # Проверка интервала, пересекающего полночь
                self.result = current_time >= start or current_time <= end
            return self.result
        except Exception as ex:
            logger.error('Ошибка при проверке интервала', ex)
            return False  # В случае ошибки возвращаем False

    def interval_with_timeout(self, timeout: int = DEFAULT_TIMEOUT, start: time = DEFAULT_START_TIME,
                              end: time = DEFAULT_END_TIME) -> bool:
        """
        Проверяет, находится ли текущее время в заданном интервале с таймаутом.

        :param timeout: Время ожидания проверки в секундах (по умолчанию 5).
        :type timeout: int
        :param start: Начало интервала (по умолчанию 23:00).
        :type start: time
        :param end: Конец интервала (по умолчанию 06:00).
        :type end: time
        :return: True, если текущее время находится в интервале и проверка выполнена в пределах таймаута, иначе False.
        :rtype: bool
        """
        thread = threading.Thread(target=self.interval, args=(start, end))
        thread.start()
        thread.join(timeout)

        if thread.is_alive():
            logger.error(f"Таймаут {timeout} секунд, проверка интервала не выполнена") # Используем логгер
            thread.join()  # Ожидание завершения потока
            return False # Возвращаем False, если таймаут

        return self.result

    def get_input(self):
        """
        Запрашивает ввод от пользователя.
        """
        try:
            self.user_input = input("U:> ")
        except Exception as ex:
            logger.error('Ошибка при получении ввода от пользователя', ex)
            self.user_input = None # присваиваем значение None при ошибке


    def input_with_timeout(self, timeout: int = DEFAULT_TIMEOUT) -> str | None:
        """
        Ожидает ввод от пользователя с таймаутом.

        :param timeout: Время ожидания ввода в секундах (по умолчанию 5).
        :type timeout: int
        :return: Введенные данные или None, если был тайм-аут.
        :rtype: str | None
        """
        thread = threading.Thread(target=self.get_input)
        thread.start()
        thread.join(timeout)

        if thread.is_alive():
            logger.error(f"Таймаут {timeout} секунд, ввод не получен.")  #  Используем логгер
            return None # Возвращаем None, если таймаут

        return self.user_input

if __name__ == '__main__':
    # Example usage
    timeout_check = TimeoutCheck()

    # Check interval with a timeout of 5 seconds
    if timeout_check.interval_with_timeout(timeout=5):
        print("Current time is within the interval.")
    else:
        print("Current time is outside the interval or timeout occurred.")
```