# Анализ кода модуля hi_lo.py

**Качество кода**
8
-  Плюсы
    - Код реализует простую игру "Больше-Меньше" в соответствии с заданием.
    - Используется `try-except` для обработки исключений при вводе пользователя, что предотвращает падение программы при некорректном вводе.
    - Код хорошо структурирован, легко читается и понятен.
    - Есть комментарии, объясняющие основные этапы работы программы.
    -  Используется `random.randint` для генерации случайного числа.

-  Минусы
    - Отсутствует документация в формате reStructuredText (RST).
    - Не используется логгер для записи ошибок.
    - Не все комментарии достаточно подробны и не соответствуют формату RST.
    - Используется глобальная переменная `numberOfGuesses`.
    - Избыточное использование `try-except`.

**Рекомендации по улучшению**
1.  Добавить docstring для модуля и функций в формате RST.
2.  Использовать логгер для записи ошибок.
3.  Убрать глобальную переменную `numberOfGuesses`, сделав ее локальной в функции.
4.  Переписать комментарии в формате RST.
5.  Избегать избыточного использования `try-except`,  используя логирование.

**Оптимизированный код**
```python
"""
Модуль реализует игру "Больше-Меньше".
=========================================================================================

В этой игре компьютер загадывает случайное число от 1 до 100,
а игрок пытается его угадать. После каждой попытки компьютер сообщает,
было ли введенное число больше или меньше загаданного.

Игра продолжается, пока игрок не угадает число.
"""
import random
from src.logger.logger import logger
# from src.utils.jjson import j_loads, j_loads_ns # TODO удалить этот комент


def play_hi_lo():
    """
    Запускает игру "Больше-Меньше".

    Инициализирует игру, генерирует случайное число и запускает игровой цикл,
    пока пользователь не угадает загаданное число.
    """
    # Инициализация счетчика попыток
    number_of_guesses = 0
    # Загадывание случайного числа от 1 до 100
    target_number = random.randint(1, 100)

    # Начало основного игрового цикла
    while True:
        # Увеличиваем количество попыток на 1
        number_of_guesses += 1
        # Запрашиваем у пользователя ввод числа
        try:
            user_guess = int(input("Введите ваше предположение: "))
        except ValueError:
            logger.error("Пожалуйста, введите целое число.")
            continue

        # Проверка, угадал ли пользователь число
        if user_guess == target_number:
            print(f"Вы угадали число за {number_of_guesses} попыток!")
            break  # Завершаем цикл, если число угадано
        elif user_guess < target_number:
            print("Слишком низко")  # Сообщаем, что загаданное число больше
        else:
            print("Слишком высоко")  # Сообщаем, что загаданное число меньше


if __name__ == "__main__":
    play_hi_lo()
```