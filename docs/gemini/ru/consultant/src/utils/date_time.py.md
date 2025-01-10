# Анализ кода модуля `date_time.py`

**Качество кода: 7/10**
- **Плюсы:**
    - Код хорошо структурирован и разбит на функции, что улучшает читаемость и повторное использование.
    - Присутствует описание модуля и документация для функций.
    - Используется многопоточность для реализации тайм-аутов, что позволяет не блокировать выполнение основного потока.
    - Есть пример использования в `if __name__ == '__main__':`.
- **Минусы:**
    - Отсутствует импорт `logger` из `src.logger`.
    - Используются `print` для вывода сообщений, что не соответствует соглашению об использовании `logger`.
    - В методе `input_with_timeout` возвращается `None` при таймауте, но не указан тип возвращаемого значения в docstring.
    - Не все комментарии соответствуют стандарту reStructuredText (RST).
    - Не хватает обработки возможных ошибок.
    - Документация класса не соответствует общепринятым стандартам.
   -  Не указан тип данных для `self.result` `self.user_input`.

**Рекомендации по улучшению:**
1.  Добавить импорт `logger` из `src.logger`.
2.  Заменить все `print` на `logger.info` и `logger.error` для логирования.
3.  Добавить обработку ошибок, используя `try-except` с логированием.
4.  Уточнить тип возвращаемого значения в `input_with_timeout` ( `str | None` ) в документации.
5.  Переписать комментарии в стиле reStructuredText (RST) для корректного отображения документации.
6.  Добавить описание класса в стиле RST.
7.  Добавить typing для переменных.

**Оптимизированный код:**
```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module:: src.utils.date_time
    :platform: Windows, Unix
    :synopsis: Functions to check if the current time is within a specified interval with an optional timeout.

Модуль содержит функции для проверки, находится ли текущее время в заданном интервале, с возможностью таймаута.

Класс :class:`TimeoutCheck` предоставляет методы для определения, попадает ли текущее время в заданный
временной интервал. Это полезно для запуска задач, которые должны выполняться только в определенные периоды
(например, обслуживание в ночное время). По умолчанию интервал времени установлен с 23:00 до 06:00,
и функция может обрабатывать интервалы, которые пересекают полночь.

Дополнительно, он обеспечивает функциональность ожидания ответа с таймаутом.

Пример использования
--------------------

Пример использования класса `TimeoutCheck`:

.. code-block:: python

    timeout_check = TimeoutCheck()
    if timeout_check.interval_with_timeout(timeout=5):
        print("Current time is within the interval.")
    else:
        print("Current time is outside the interval or timeout occurred.")

"""
from datetime import datetime, time
import threading
from typing import Optional, Union
from src.logger.logger import logger # Импорт логгера

class TimeoutCheck:
    """
    Класс для проверки временных интервалов и таймаутов.

    :ivar Optional[bool] result: Результат проверки временного интервала.
    :ivar Optional[str]: Содержит ввод пользователя.

    """
    def __init__(self):
        """
        Инициализирует объект класса TimeoutCheck.

         :ivar Optional[bool] result: хранит результат проверки интервала времени
         :ivar Optional[str] user_input: хранит пользовательский ввод
        """
        self.result: Optional[bool] = None
        self.user_input: Optional[str] = None

    def interval(self, start: time = time(23, 0), end: time = time(6, 0)) -> None:
        """
        Проверяет, находится ли текущее время в заданном интервале.

        :param start: Начало интервала (по умолчанию 23:00).
        :type start: time
        :param end: Конец интервала (по умолчанию 06:00).
        :type end: time
        :return: None. Результат проверки устанавливается в атрибут `self.result`.
        :rtype: None
        """
        try:
            current_time = datetime.now().time()

            if start < end:
                # Интервал в пределах одного дня (например, с 08:00 до 17:00)
                self.result = start <= current_time <= end
            else:
                # Интервал, охватывающий полночь (например, с 23:00 до 06:00)
                self.result = current_time >= start or current_time <= end
        except Exception as ex:
            logger.error('Ошибка при проверке временного интервала', exc_info=ex)

    def interval_with_timeout(self, timeout: int = 5, start: time = time(23, 0), end: time = time(6, 0)) -> bool:
        """
        Проверяет, находится ли текущее время в заданном интервале с таймаутом.

        :param timeout: Время ожидания проверки интервала в секундах.
        :type timeout: int
        :param start: Начало интервала (по умолчанию 23:00).
        :type start: time
        :param end: Конец интервала (по умолчанию 06:00).
        :type end: time
        :return: True, если текущее время находится в интервале и получен ответ в пределах таймаута, False в противном случае или при таймауте.
        :rtype: bool
        """
        try:
            thread = threading.Thread(target=self.interval, args=(start, end))
            thread.start()
            thread.join(timeout)

            if thread.is_alive():
                logger.info(f"Таймаут {timeout} секунд. выполнение продолжается") #  логируем что произошел таймаут
                thread.join()  # Убеждаемся, что поток останавливается после таймаута
                return False  # Таймаут, возвращаем False
            return self.result
        except Exception as ex:
            logger.error('Ошибка при проверке интервала с таймаутом', exc_info=ex)
            return False

    def get_input(self) -> None:
        """
        Запрашивает ввод от пользователя.
        """
        try:
            self.user_input = input("U:> ")
        except Exception as ex:
            logger.error('Ошибка при запросе пользовательского ввода', exc_info=ex)


    def input_with_timeout(self, timeout: int = 5) -> Optional[str]:
        """
         Ожидает ввод с таймаутом.

        :param timeout: Время ожидания ввода в секундах.
        :type timeout: int
        :return: Введенные данные или None, если произошел таймаут.
        :rtype: Optional[str]
        """
        try:
            # Запускаем поток для получения ввода от пользователя
            thread = threading.Thread(target=self.get_input)
            thread.start()

            # Ожидаем завершения потока или таймаут
            thread.join(timeout)

            if thread.is_alive():
                logger.info(f"Таймаут {timeout} секунд.")# Логируем что произошел таймаут
                return None  # Возвращаем None, если произошел таймаут

            return self.user_input
        except Exception as ex:
            logger.error('Ошибка при ожидании ввода с таймаутом', exc_info=ex)
            return None

if __name__ == '__main__':
    # Пример использования
    timeout_check = TimeoutCheck()

    # Проверка интервала с таймаутом в 5 секунд
    if timeout_check.interval_with_timeout(timeout=5):
        print("Current time is within the interval.")
    else:
        print("Current time is outside the interval or timeout occurred.")
```