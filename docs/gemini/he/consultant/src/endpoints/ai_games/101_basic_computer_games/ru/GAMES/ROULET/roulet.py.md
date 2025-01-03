# Анализ кода модуля roulet.py

**Качество кода**

-   **Соблюдение требований к формату кода (1-10):**

    -   **Преимущества:**
        -   Код прост для понимания и чтения.
        -   Используются комментарии для объяснения логики кода.
        -   Обработка ошибок ввода с помощью `try-except`.
        -   Проверка допустимого диапазона введенного числа.
    -   **Недостатки:**
        -   Отсутствует docstring в начале модуля.
        -   Не используется `j_loads` или `j_loads_ns`.
        -   Не используются логирование через `logger.error` при ошибках.
        -   Комментарии не в reStructuredText (RST) формате.
        -   Нет импорта `from src.logger.logger import logger`.
        -   Используется `exit()` вместо `logger.error` для обработки ошибок ввода.
        -   Отсутствие документации функций в формате reStructuredText (RST).

**Рекомендации по улучшению**

1.  Добавить docstring в начале модуля в формате RST для описания модуля.
2.  Импортировать `from src.logger.logger import logger` для логирования ошибок.
3.  Использовать `logger.error` для записи ошибок вместо `print` и `exit()`.
4.  Добавить docstring в формате RST для описания функциональности отдельных блоков кода, таких как ввод ставки, проверка допустимости и генерация числа рулетки.
5.  Использовать маркеры TODO для дальнейших улучшений, например, для добавления возможности ставок на чет/нечет или на диапазон чисел.
6.  Избегать использования `exit()` в пользу более корректной обработки ошибок с помощью `logger.error`.
7.  Изменить все комментарии на формат reStructuredText (RST).
8.  Заменить все `print` на использование `logger.info`, `logger.debug`, `logger.error` в зависимости от ситуации.
9.  Обернуть основные блоки кода в функции для лучшей читаемости.

**Улучшенный код**

```python
"""
Модуль для игры в рулетку.
=========================================================================================

Модуль представляет собой упрощенную версию игры в рулетку, где игрок делает ставку на число от 0 до 36.
Компьютер "вращает" рулетку и выбирает случайное число из этого же диапазона.
Если число игрока совпадает с числом, выпавшим на рулетке, игрок выигрывает.

Пример использования
--------------------

.. code-block:: python

    from src.endpoints.ai_games.101_basic_computer_games.ru.GAMES.ROULET.roulet import play_roulette

    play_roulette()
"""
import random
from src.logger.logger import logger  # Импортируем logger для логирования


def get_user_bet() -> int:
    """
    Запрашивает ввод числа у пользователя и проверяет его корректность.

    :return: Число, выбранное пользователем.
    :raises ValueError: Если ввод пользователя не является целым числом.
    :raises SystemExit: Если число выходит за допустимый диапазон (0-36).
    """
    try:
        user_number = int(input('Введите число от 0 до 36: '))  # Запрашиваем у пользователя ввод числа, на которое он ставит
        logger.debug(f'Пользователь ввел число: {user_number}') # Логируем ввод пользователя
        
    except ValueError as e:
        logger.error('Пожалуйста, введите целое число.', exc_info=e) # Логируем ошибку ввода
        raise SystemExit(1) # Завершаем программу, если введен неверный тип данных.

    if user_number < 0 or user_number > 36: # Проверяем, что введенное число находится в допустимом диапазоне
        logger.error('Число должно быть в диапазоне от 0 до 36.') # Логируем ошибку ввода
        raise SystemExit(1) # Завершаем программу, если число вне диапазона.
    return user_number


def generate_roulette_number() -> int:
    """
    Генерирует случайное число для рулетки.

    :return: Случайное число в диапазоне от 0 до 36.
    """
    roulette_number = random.randint(0, 36) # Генерируем случайное число от 0 до 36 (выпавшее на рулетке)
    logger.debug(f'Выпавшее число рулетки: {roulette_number}') # Логируем выпавшее число
    return roulette_number


def check_win(user_number: int, roulette_number: int) -> bool:
    """
    Проверяет, выиграл ли пользователь.

    :param user_number: Число, выбранное пользователем.
    :param roulette_number: Число, выпавшее на рулетке.
    :return: True, если пользователь выиграл, False в противном случае.
    """
    if user_number == roulette_number: # Проверяем, совпало ли число пользователя с числом рулетки
        logger.info('ПОЗДРАВЛЯЮ! Вы выиграли!')  # Выводим сообщение о выигрыше
        return True
    else:
        logger.info(f'Вы проиграли. Число было {roulette_number}') # Выводим сообщение о проигрыше и выпавшее число
        return False


def play_roulette():
    """
    Запускает игру в рулетку.
    """
    try:
        user_number = get_user_bet()
        roulette_number = generate_roulette_number()
        check_win(user_number, roulette_number)
    except SystemExit as e:
        logger.error("Игра завершена из-за ошибки ввода.", exc_info=e) # Обработка ошибок ввода
    except Exception as e:
        logger.error("Непредвиденная ошибка в игре", exc_info=e)  # Логируем непредвиденную ошибку
    # TODO: Добавить возможность ставок на чет/нечет или на диапазон чисел.
    # TODO: Добавить возможность повторить игру.


if __name__ == '__main__':
    play_roulette()
    
"""
Объяснение кода:
1.  **Импорт модуля `random`**::
    -   ``import random``: Импортирует модуль ``random``, который используется для генерации случайного числа.
    -   ``from src.logger.logger import logger``: Импортирует логгер для логирования событий.
2.  **Функция `get_user_bet`**::
    -   ``def get_user_bet() -> int:``: Определяет функцию для ввода ставки пользователя.
    -  ``try...except ValueError``: Блок try-except обрабатывает возможные ошибки ввода. Если пользователь введет не целое число, то будет выведена ошибка в лог, и программа завершится.
    -   ``user_number = int(input('Введите число от 0 до 36: '))``: Запрашивает у пользователя число, на которое он хочет поставить, и преобразует его в целое число, сохраняя результат в ``user_number``.
    -  ``logger.debug(f'Пользователь ввел число: {user_number}')``: Выводит в лог значение введенного пользователем числа
    -   ``if user_number < 0 or user_number > 36:``: Проверяет, находится ли введенное число в допустимом диапазоне от 0 до 36.
    -  ``logger.error('Число должно быть в диапазоне от 0 до 36.')``: Выводит сообщение об ошибке в лог, если число вне диапазона.
    - ``raise SystemExit(1)``: Завершает программу, если число вне диапазона.
3. **Функция `generate_roulette_number`**::
    -   ``def generate_roulette_number() -> int:``: Определяет функцию для генерации случайного числа рулетки.
    -   ``roulette_number = random.randint(0, 36)``: Генерирует случайное целое число в диапазоне от 0 до 36, представляющее результат "вращения" рулетки, и сохраняет его в ``roulette_number``.
    - ``logger.debug(f'Выпавшее число рулетки: {roulette_number}')``:  Выводит в лог выпавшее число рулетки
4.  **Функция `check_win`**::
    -  ``def check_win(user_number: int, roulette_number: int) -> bool:``: Определяет функцию для проверки выигрыша.
    -   ``if user_number == roulette_number:``: Проверяет, совпадает ли число, введенное пользователем, с числом, выпавшим на рулетке.
    -   ``logger.info('ПОЗДРАВЛЯЮ! Вы выиграли!')``: Если числа совпадают, выводит сообщение о выигрыше в лог.
    -   ``else:``: Если числа не совпадают, выполняет следующий блок кода.
    -   ``logger.info(f'Вы проиграли. Число было {roulette_number}')``: Выводит сообщение о проигрыше и выпавшее число на рулетке в лог.
5.  **Функция `play_roulette`**::
    -  ``def play_roulette():``: Определяет основную функцию для запуска игры
    -  ``try...except``: Блок try-except обрабатывает возможные ошибки в процессе игры.
    - ``user_number = get_user_bet()``: Вызов функции для ввода ставки пользователя.
    - ``roulette_number = generate_roulette_number()``: Вызов функции для генерации числа рулетки.
    - ``check_win(user_number, roulette_number)``: Вызов функции для проверки выигрыша.
    -  ``except SystemExit as e:``: Обработка выхода из программы через SystemExit.
    -  ``except Exception as e:``: Обработка непредвиденных ошибок в игре.
6. **Условный запуск**::
   - ``if __name__ == '__main__':``: Проверка, запущен ли скрипт напрямую.
   - ``play_roulette()``: Запуск игры в рулетку.
"""
```