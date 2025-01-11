# Анализ кода модуля `date_time`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован, есть класс `TimeoutCheck` с методами для проверки интервала времени и ввода с таймаутом.
    - Присутствуют docstring для функций.
    - Используется многопоточность для реализации таймаутов.
    - Логика проверки интервала времени корректна, включая случаи, когда интервал пересекает полночь.
- Минусы
    - Отсутствует импорт `from src.logger.logger import logger` для логирования ошибок.
    - Использование `print` для вывода сообщений о таймауте вместо `logger.error`.
    - Не хватает обработки исключений, особенно в методах с многопоточностью.
    - Отсутствует документация для класса.
    - Использование `self.result` в методе `interval` для сохранения результата, хотя метод `interval` выполняется в отдельном потоке, что может привести к проблемам с синхронизацией.

**Рекомендации по улучшению**

1. **Добавить импорт логгера:**  Импортировать `logger` из `src.logger.logger` для логирования ошибок.
2. **Заменить `print` на `logger.error`**: Использовать `logger.error` для вывода сообщений о таймауте.
3. **Обработка исключений**: Добавить обработку исключений в методах `interval` и `input_with_timeout`, особенно при работе с потоками.
4. **Документация класса**: Добавить docstring для класса `TimeoutCheck`.
5. **Убрать `self.result`**:  Передавать результат через `return` из метода `interval`.
6. **Улучшить docstrings**: Дополнить docstrings для функций, добавив примеры использования.
7. **Использовать `return None`**: В методе `input_with_timeout`  вернуть `None` при таймауте явно.
8. **Улучшить читаемость кода**: Добавить пустые строки для улучшения читаемости кода.

**Оптимизированный код**

```python
"""
.. module:: src.utils
    :platform: Windows, Unix
    :synopsis: function to check if the current time is within a specified interval with an optional timeout

"""
""" 
Модуль для работы с проверкой интервала времени и таймаутами.
=========================================================================================

Этот модуль содержит класс :class:`TimeoutCheck`, который предоставляет методы для проверки
находится ли текущее время в заданном интервале, а также для ожидания пользовательского ввода
с таймаутом.

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
from src.logger.logger import logger # Импорт логгера


class TimeoutCheck:
    """
    Класс для проверки интервала времени и ожидания с таймаутом.

    Предоставляет методы для проверки текущего времени на нахождение в заданном интервале,
    а также для ожидания пользовательского ввода с таймаутом.
    """
    def __init__(self):
        """
        Инициализирует класс TimeoutCheck.
        """
        self.user_input = None

    def interval(self, start: time = time(23, 0), end: time = time(6, 0)) -> bool:
        """
        Проверяет, находится ли текущее время в заданном интервале.

        Args:
            start (time): Начало интервала (по умолчанию 23:00).
            end (time): Конец интервала (по умолчанию 06:00).

        Returns:
            bool: True, если текущее время находится в интервале, иначе False.

        Example:
            >>> timeout_check = TimeoutCheck()
            >>> timeout_check.interval(time(8, 0), time(17, 0))
            False
        """
        current_time = datetime.now().time()

        if start < end:
            # Интервал в пределах одного дня (например, с 08:00 до 17:00)
            return start <= current_time <= end
        else:
            # Интервал, охватывающий полночь (например, с 23:00 до 06:00)
            return current_time >= start or current_time <= end

    def interval_with_timeout(self, timeout: int = 5, start: time = time(23, 0), end: time = time(6, 0)) -> bool:
        """
        Проверяет, находится ли текущее время в заданном интервале с таймаутом.

        Args:
            timeout (int): Время в секундах для ожидания проверки интервала.
            start (time): Начало интервала (по умолчанию 23:00).
            end (time): Конец интервала (по умолчанию 06:00).

        Returns:
            bool: True, если текущее время находится в интервале и ответ получен в пределах таймаута,
                  False, если нет или произошел таймаут.

         Example:
            >>> timeout_check = TimeoutCheck()
            >>> timeout_check.interval_with_timeout(timeout=1, start=time(0,0), end=time(23,59))
            True
        """
        thread = threading.Thread(target=self.interval, args=(start, end))
        thread.start()
        thread.join(timeout)
        
        if thread.is_alive():
             logger.error(f'Таймаут {timeout} секунд при проверке интервала времени') # логируем ошибку
             thread.join()  # Ensures thread stops after timeout
             return False  # Timeout occurred, so returning False

        return self.interval(start,end) #  Получаем результат через вызов метода

    def get_input(self):
        """ Запрашивает ввод от пользователя и сохраняет его в атрибут user_input."""
        try: #  блок try-except для перехвата возможных ошибок ввода.
            self.user_input = input('U:> ')
        except Exception as ex:
            logger.error(f'Ошибка при получении ввода от пользователя: {ex}')

    def input_with_timeout(self, timeout: int = 5) -> str | None:
        """
        Ожидает ввод от пользователя с таймаутом.

        Args:
            timeout (int): Время ожидания ввода в секундах.

        Returns:
            str | None: Введенные данные или None, если произошел таймаут.

         Example:
            >>> timeout_check = TimeoutCheck()
            >>> timeout_check.input_with_timeout(timeout=1)
            'Test input'
        """
        # Запускает поток для получения ввода от пользователя
        thread = threading.Thread(target=self.get_input)
        thread.start()

        # Ожидает завершения потока или таймаут
        thread.join(timeout)

        if thread.is_alive():
            logger.error(f'Таймаут {timeout} секунд при ожидании ввода от пользователя') #  логируем ошибку
            return None  # Возвращает None, если тайм-аут произошел
        
        return self.user_input


if __name__ == '__main__':
    # Пример использования
    timeout_check = TimeoutCheck()

    # Проверяем интервал с таймаутом 5 секунд
    if timeout_check.interval_with_timeout(timeout=5):
        print('Current time is within the interval.')
    else:
        print('Current time is outside the interval or timeout occurred.')

    # Пример использования ввода с таймаутом
    user_input = timeout_check.input_with_timeout(timeout=3)
    if user_input:
         print(f'User input: {user_input}')
    else:
         print('No input received or timeout occurred.')
```