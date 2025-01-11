# Анализ кода модуля `cursor_spinner`

**Качество кода**:
- **Соответствие стандартам**: 7
- **Плюсы**:
    - Простой и понятный код.
    - Использование генератора для курсора.
    - Наличие документации.
- **Минусы**:
    - Неполная документация в формате RST.
    - Отсутствие импорта `logger`.
    - Нет обработки ошибок.
    - Используются двойные кавычки в документации и в коде.

**Рекомендации по улучшению**:
- Дополнить документацию в формате RST для модуля и функций.
- Использовать одинарные кавычки в коде и двойные только для вывода.
- Добавить импорт `logger` из `src.logger`.
- Улучшить обработку ошибок, используя `logger.error` вместо `try-except`.
- Заменить обычные комментарии на комментарии в формате RST.
- Выровнять названия функций и переменных.

**Оптимизированный код**:

```python
"""
Модуль для отображения анимированного курсора в консоли.
======================================================

Этот модуль предоставляет утилиту для отображения вращающегося курсора в консоли
для имитации процесса загрузки или ожидания.

Пример использования
--------------------
.. code-block:: python

    from src.utils.cursor_spinner import show_spinner

    print('Spinner for 5 seconds:')
    show_spinner(duration=5.0, delay=0.1)
    print('\\nDone!')
"""
import time
import sys

from src.logger import logger  # импортируем logger из src.logger

def spinning_cursor():
    """
    Генератор для вращающегося курсора, который циклически перебирает символы |, /, -, \\.

    :yields: Следующий символ в последовательности курсора.
    :rtype: str

    :Example:
        >>> cursor = spinning_cursor()
        >>> next(cursor)  # '|'
        >>> next(cursor)  # '/'
        >>> next(cursor)  # '-'
        >>> next(cursor)  # '\\'
    """
    while True:
        for cursor in '|/-\\':
            yield cursor

def show_spinner(duration: float = 5.0, delay: float = 0.1) -> None:
    """
    Отображает вращающийся курсор в консоли в течение заданного времени.

    :param duration: Продолжительность работы курсора в секундах. По умолчанию 5.0.
    :type duration: float
    :param delay: Задержка между сменами символов курсора в секундах. По умолчанию 0.1.
    :type delay: float
    :raises Exception: В случае ошибки при выводе в консоль.
    
    :Example:
        >>> show_spinner(duration=3.0, delay=0.2)  # Отображает курсор в течение 3 секунд
    """
    spinner = spinning_cursor()
    end_time = time.time() + duration

    try:
        while time.time() < end_time:
            sys.stdout.write(next(spinner))  # выводим следующий символ курсора
            sys.stdout.flush()  # принудительно выводим в консоль
            time.sleep(delay)  # пауза
            sys.stdout.write('\b') # стираем символ в консоли
    except Exception as e: # обрабатываем ошибку
        logger.error(f"Ошибка при отображении спиннера: {e}")
        

if __name__ == "__main__":
    # пример использования спиннера
    print("Spinner for 5 seconds:")
    show_spinner(duration=5.0, delay=0.1)
    print("\nDone!")
```