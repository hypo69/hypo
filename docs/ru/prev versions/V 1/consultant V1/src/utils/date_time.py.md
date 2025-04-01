## Анализ кода модуля `date_time`

**Качество кода:**

- **Соответствие стандартам**: 6/10
- **Плюсы**:
    - Код содержит docstring для классов и методов, что облегчает понимание функциональности.
    - Использование `threading` для реализации таймаутов.
- **Минусы**:
    - Не хватает единообразия в стиле кода (использование двойных и одинарных кавычек, отсутствие пробелов вокруг операторов).
    - Отсутствуют аннотации типов для атрибутов класса.
    - Не используется модуль `logger` для логирования.
    - Смешанный стиль комментариев (русский и английский).

**Рекомендации по улучшению:**

1.  **Форматирование кода**:
    - Привести код в соответствие со стандартами PEP8 (пробелы вокруг операторов, одинарные кавычки).
2.  **Типизация**:
    - Добавить аннотации типов для атрибутов класса `TimeoutCheck`.
3.  **Логирование**:
    - Использовать модуль `logger` из `src.logger` для логирования ошибок и предупреждений.
4.  **Документация**:
    - Перевести все комментарии на русский язык для единообразия.
    - Улучшить docstring для класса `TimeoutCheck` и его методов, добавив больше деталей о работе кода и возможных исключениях.
5.  **Обработка исключений**:
    - Добавить обработку исключений в методы `interval_with_timeout` и `input_with_timeout` для более надежной работы.
6.  **Улучшение `input_with_timeout`**:
    - В текущей реализации `input_with_timeout` возвращает `None` при таймауте, что может привести к ошибкам. Лучше возвращать пустую строку `''`.
    - Добавить возможность передавать сообщение-приглашение для ввода.

**Оптимизированный код:**

```python
## \file /src/utils/date_time.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
Модуль для проверки, находится ли текущее время в заданном интервале, с возможностью таймаута.
==========================================================================================

Модуль содержит класс :class:`TimeoutCheck`, который позволяет определить, находится ли текущее время в заданном интервале,
что полезно для выполнения операций, которые должны выполняться только в определенные периоды времени
(например, ночное обслуживание).

Функция `interval` позволяет определить, попадает ли текущее время в заданный временной интервал.
Интервал по умолчанию - с 23:00 до 06:00, и функция может обрабатывать интервалы, пересекающие полночь.

Кроме того, модуль предоставляет функциональность ожидания ответа с таймаутом.

Пример использования
----------------------

>>> timeout_check = TimeoutCheck()
>>> if timeout_check.interval_with_timeout(timeout=5):
...     print('Текущее время находится в интервале.')
... else:
...     print('Текущее время находится вне интервала или произошел таймаут.')
"""

from datetime import datetime, time
import threading
from typing import Optional
from src.logger import logger  # Используем модуль logger из src.logger


class TimeoutCheck:
    """
    Класс для проверки времени с таймаутом.

    Attributes:
        result (Optional[bool]): Результат проверки интервала времени.
        user_input (Optional[str]): Ввод пользователя.
    """

    def __init__(self) -> None:
        """
        Инициализирует экземпляр класса TimeoutCheck.
        """
        self.result: Optional[bool] = None
        self.user_input: Optional[str] = None

    def interval(self, start: time = time(23, 0), end: time = time(6, 0)) -> bool:
        """
        Проверяет, находится ли текущее время в указанном интервале.

        Args:
            start (time, optional): Начало интервала (по умолчанию 23:00).
            end (time, optional): Конец интервала (по умолчанию 06:00).

        Returns:
            bool: True, если текущее время находится в интервале, иначе False.

        Example:
            >>> timeout_check = TimeoutCheck()
            >>> timeout_check.interval(start=time(8, 0), end=time(17, 0))
            False
        """
        current_time = datetime.now().time()

        if start < end:
            # Интервал в пределах одного дня (например, с 08:00 до 17:00)
            self.result = start <= current_time <= end
        else:
            # Интервал, охватывающий полночь (например, с 23:00 до 06:00)
            self.result = current_time >= start or current_time <= end
        return self.result

    def interval_with_timeout(self, timeout: int = 5, start: time = time(23, 0), end: time = time(6, 0)) -> bool:
        """
        Проверяет, находится ли текущее время в указанном интервале с таймаутом.

        Args:
            timeout (int, optional): Время ожидания проверки интервала в секундах (по умолчанию 5).
            start (time, optional): Начало интервала (по умолчанию 23:00).
            end (time, optional): Конец интервала (по умолчанию 06:00).

        Returns:
            bool: True, если текущее время находится в интервале и получен ответ в течение таймаута,
                  False, если нет или произошел таймаут.
        """
        try:
            thread = threading.Thread(target=self.interval, args=(start, end))
            thread.start()
            thread.join(timeout)

            if thread.is_alive():
                logger.warning(f'Таймаут {timeout} секунд истек, продолжаем выполнение.')  # Используем logger
                thread.join()  # Убеждаемся, что поток остановлен после таймаута
                return False  # Произошел таймаут, возвращаем False
            return self.result
        except Exception as ex:
            logger.error('Произошла ошибка при проверке интервала с таймаутом', ex, exc_info=True)
            return False

    def get_input(self) -> None:
        """
        Запрашивает ввод от пользователя.
        """
        self.user_input = input('U:> ')

    def input_with_timeout(self, timeout: int = 5, prompt: str = 'U:> ') -> str:
        """
        Ожидает ввод от пользователя с таймаутом.

        Args:
            timeout (int, optional): Время ожидания ввода в секундах (по умолчанию 5).
            prompt (str, optional): Приглашение для ввода (по умолчанию 'U:> ').

        Returns:
            str: Введенные данные или пустая строка, если произошел таймаут.
        """
        self.user_input = ''  # Сбрасываем предыдущий ввод
        thread = threading.Thread(target=self._get_input, args=(prompt,))
        thread.start()
        thread.join(timeout)

        if thread.is_alive():
            logger.warning(f'Таймаут {timeout} секунд истек при ожидании ввода.')  # Используем logger
            return ''  # Возвращаем пустую строку, если произошел таймаут

        return self.user_input

    def _get_input(self, prompt: str) -> None:
        """
        Вспомогательный метод для получения ввода от пользователя.
        """
        self.user_input = input(prompt)


if __name__ == '__main__':
    # Пример использования
    timeout_check = TimeoutCheck()

    # Проверка интервала с таймаутом в 5 секунд
    if timeout_check.interval_with_timeout(timeout=5):
        print('Текущее время находится в интервале.')
    else:
        print('Текущее время находится вне интервала или произошел таймаут.')

    # Пример использования input_with_timeout
    user_input = timeout_check.input_with_timeout(timeout=10, prompt='Пожалуйста, введите что-нибудь: ')
    if user_input:
        print(f'Вы ввели: {user_input}')
    else:
        print('Ввод не был получен вовремя.')
```