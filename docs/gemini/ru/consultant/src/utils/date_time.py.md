# Анализ кода модуля `date_time`

**Качество кода:**

- **Соответствие стандартам**: 7
- **Плюсы**:
    - Код выполняет поставленные задачи по проверке интервалов времени и ожидания ввода с таймаутом.
    - Используется многопоточность для неблокирующего ожидания ввода и проверки интервала с таймаутом.
    - Документация к функциям присутствует, но требует доработки.
- **Минусы**:
    - Не используются одинарные кавычки для строк в коде, кроме комментариев.
    - Отсутствует импорт `logger`.
    - Используются избыточные `print` для вывода сообщений о таймауте, лучше использовать логирование.
    - Не полная документация в формате RST
    - Отсутствует проверка типов для входных аргументов.

**Рекомендации по улучшению:**

1. **Форматирование**:
   - Используйте одинарные кавычки для строк в коде, например `a = 'A1'`, `b = ['a', 'b']`, `c = {'key': 'value'}`.
   - Двойные кавычки используйте только для `print`, `input` и `logger`.

2. **Импорт `logger`**:
   - Добавьте импорт `from src.logger import logger` для логирования ошибок и сообщений.

3. **Логирование**:
   - Замените `print` на `logger.info`, `logger.error` для вывода сообщений, особенно в случаях таймаута и ошибок.

4. **Документация**:
   - Добавьте **RST** документацию для модуля и класса `TimeoutCheck`.
   - Опишите подробнее параметры и возвращаемые значения для всех методов.
   - Укажите возможные исключения в документации.
  
5.  **Управление потоками**:
    - Убедитесь, что потоки завершаются корректно после таймаута.

6.  **Использование `None`**:
    - Явное возвращение `None` в `input_with_timeout` может быть более явным, чем отсутствие `return`.

7. **Проверка типов**:
   - Добавьте проверки типов для входных аргументов.
   -  Используйте аннотации типов для параметров функций.

**Оптимизированный код:**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для работы с проверками времени и таймаутами.
===================================================

Модуль содержит класс :class:`TimeoutCheck`, который используется для проверки,
находится ли текущее время в заданном интервале, и ожидания ввода с таймаутом.

Пример использования:
---------------------
.. code-block:: python

    timeout_check = TimeoutCheck()
    if timeout_check.interval_with_timeout(timeout=5):
        print("Current time is within the interval.")
    else:
        print("Current time is outside the interval or timeout occurred.")
"""
from datetime import datetime, time
import threading
from src.logger import logger # Добавлен импорт logger # Изменен импорт

class TimeoutCheck:
    """
    Класс для проверки интервала времени и ожидания ввода с таймаутом.
    """
    def __init__(self) -> None:
        """
        Инициализация объекта TimeoutCheck.
        """
        self.result = None
        self.user_input = None

    def interval(self, start: time = time(23, 0), end: time = time(6, 0)) -> bool:
        """
        Проверяет, находится ли текущее время в заданном интервале.

        :param start: Начало интервала (по умолчанию 23:00).
        :type start: time, optional
        :param end: Конец интервала (по умолчанию 06:00).
        :type end: time, optional
        :return: True, если текущее время находится в интервале, иначе False.
        :rtype: bool
        
        Пример:
        
            >>> from datetime import time
            >>> tc = TimeoutCheck()
            >>> tc.interval(start=time(22, 0), end=time(23, 0))
        """
        current_time = datetime.now().time()

        if start < end:
            # Interval within the same day (e.g., 08:00 to 17:00) # Interval within the same day
            self.result = start <= current_time <= end # Используем одинарные кавычки
        else:
            # Interval spanning midnight (e.g., 23:00 to 06:00) # Interval spanning midnight
            self.result = current_time >= start or current_time <= end # Используем одинарные кавычки

        return self.result

    def interval_with_timeout(self, timeout: int = 5, start: time = time(23, 0), end: time = time(6, 0)) -> bool:
        """
        Проверяет, находится ли текущее время в заданном интервале с таймаутом.

        :param timeout: Время в секундах для ожидания проверки интервала.
        :type timeout: int, optional
        :param start: Начало интервала (по умолчанию 23:00).
        :type start: time, optional
        :param end: Конец интервала (по умолчанию 06:00).
        :type end: time, optional
        :return: True, если текущее время находится в интервале и проверка уложилась в таймаут, иначе False.
        :rtype: bool

        :raises TypeError: Если timeout не является целым числом, start и end не являются объектами time.
        
        Пример:
        
            >>> from datetime import time
            >>> tc = TimeoutCheck()
            >>> tc.interval_with_timeout(timeout=3, start=time(22, 0), end=time(23, 0))
        """
        if not isinstance(timeout, int):
             raise TypeError('timeout must be an int') # Проверка типа timeout
        if not isinstance(start, time):
             raise TypeError('start must be a time object') # Проверка типа start
        if not isinstance(end, time):
            raise TypeError('end must be a time object') # Проверка типа end

        thread = threading.Thread(target=self.interval, args=(start, end)) # Запускаем поток для проверки интервала
        thread.start()
        thread.join(timeout) # Ожидаем завершения потока с таймаутом

        if thread.is_alive():
            logger.error(f'Timeout occurred after {timeout} seconds, continuing execution.') # Логируем таймаут
            thread.join()  # Ensures thread stops after timeout # Ensures thread stops after timeout
            return False  # Timeout occurred, so returning False # Возвращаем False, если произошел таймаут

        return self.result # Возвращаем результат

    def get_input(self) -> None:
        """
        Запрашивает ввод от пользователя.
        """
        self.user_input = input('U:> ') # Используем одинарные кавычки

    def input_with_timeout(self, timeout: int = 5) -> str | None:
        """
        Ожидает ввод от пользователя с таймаутом.

        :param timeout: Время в секундах для ожидания ввода.
        :type timeout: int, optional
        :return: Введенные данные или None, если произошел таймаут.
        :rtype: str | None

        :raises TypeError: Если timeout не является целым числом.
        
        Пример:
        
            >>> tc = TimeoutCheck()
            >>> tc.input_with_timeout(timeout=3)
        """
        if not isinstance(timeout, int):
             raise TypeError('timeout must be an int') # Проверка типа timeout
        # Запускаем поток для получения ввода от пользователя
        thread = threading.Thread(target=self.get_input) # Запускаем поток для получения ввода
        thread.start()
        # Ожидаем завершения потока или тайм-аут
        thread.join(timeout) # Ожидаем завершения потока с таймаутом

        if thread.is_alive():
            logger.error(f'Timeout occurred after {timeout} seconds.') # Логируем таймаут
            return None # Возвращаем None, если таймаут произошел

        return self.user_input # Возвращаем введенные данные


if __name__ == '__main__':
    # Example usage # Пример использования
    timeout_check = TimeoutCheck()

    # Check interval with a timeout of 5 seconds # Проверяем интервал с таймаутом 5 секунд
    if timeout_check.interval_with_timeout(timeout=5):
        print('Current time is within the interval.') # Используем одинарные кавычки
    else:
        print('Current time is outside the interval or timeout occurred.') # Используем одинарные кавычки
```