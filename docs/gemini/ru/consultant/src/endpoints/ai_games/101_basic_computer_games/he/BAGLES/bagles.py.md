# Анализ кода модуля bagles.py

**Качество кода**
7
-  Плюсы
    - Код хорошо структурирован и легко читается.
    - Функции имеют четкое назначение и следуют принципу единой ответственности.
    - Используются осмысленные имена переменных и функций.
    -  Присутствует документация, описывающая логику работы программы.
    -  Код содержит подробные комментарии.
-  Минусы
    -  Отсутствует обработка исключений.
    -  Используется стандартный `print` для вывода, вместо `logger`.
    -  Документация не соответствует стандарту reStructuredText (RST).
    -  Нет импорта модуля `logger`.
    - Код написан на иврите, что затрудняет понимание для не говорящих на этом языке.
    - Код не соответствует инструкциям по стандарту кода.

**Рекомендации по улучшению**

1.  **Импорт модуля `logger`**:
    - Добавить импорт `from src.logger.logger import logger` для логирования.
2.  **Логирование ошибок**:
    -  Заменить `print` на `logger.info` для информационных сообщений и `logger.error` для ошибок.
3.  **Документация в формате RST**:
    - Переписать все комментарии и docstring в формате RST.
4.  **Улучшение обработки ошибок**:
    -  Заменить стандартные проверки на обработку исключений с использованием `logger.error`.
5. **Использовать английский язык для всех сообщений и комментариев**
    - Переписать все комментарии и сообщения на английский язык.

**Оптимизированный код**

```python
"""
Module for the Bagels guessing game.
=========================================================================================

This module implements the classic "Bagels" game, where the computer selects a secret
number and the player tries to guess it using clues.

The game uses clues like "FERMI" (correct digit in the correct position), "PICO" (correct
digit in the wrong position), and "BAGELS" (no correct digits).

Example of Usage
----------------

To play the game, simply run this script. The computer will choose a secret number and
prompt you to make guesses until you guess correctly.

.. code-block:: python

    if __name__ == "__main__":
        play_bagels_game()
"""

import random
from src.logger.logger import logger  #  Импортируем logger

def generate_secret_number(num_digits: int) -> str:
    """
    Generates a secret number with unique digits.

    :param num_digits: The number of digits for the secret number.
    :return: The secret number as a string.
    """
    try: # оборачиваем код в блок try-except для отлова возможных ошибок.
        digits = list(range(10)) #  создаем список цифр от 0 до 9
        random.shuffle(digits) #  перемешиваем список
        secret_number = "".join(map(str, digits[:num_digits])) #  формируем секретное число
        return secret_number # возвращаем секретное число
    except Exception as ex: #  отлавливаем ошибки
        logger.error('Error generating secret number', ex) #  логируем ошибку
        return "" #  возвращаем пустую строку в случае ошибки


def get_clues(user_guess: str, secret_number: str) -> str:
    """
    Generates clues for the user's guess.

    :param user_guess: The user's guess.
    :param secret_number: The secret number.
    :return: The clues as a string.
    """
    try: #  обертка try-except для отлова ошибок
        clues = "" #  инициализируем строку с подсказками
        for i, digit in enumerate(user_guess): #  проходимся по каждой цифре в предположении пользователя
            if digit == secret_number[i]: #  проверяем, есть ли цифра в нужном месте
                clues += "FERMI " #  добавляем подсказку FERMI
            elif digit in secret_number: #  проверяем, есть ли цифра в секретном числе, но в другом месте
                clues += "PICO " #  добавляем подсказку PICO
        if not clues: # если ни одна цифра не подходит
            clues = "BAGELS" #  добавляем подсказку BAGELS
        return clues #  возвращаем строку с подсказками
    except Exception as ex:  #  отлавливаем ошибки
        logger.error('Error generating clues', ex) #  логируем ошибку
        return "" #  возвращаем пустую строку


def play_bagels_game():
    """
    Manages the Bagels game.
    """
    try: #  обертка try-except для отлова ошибок
        number_of_digits = 3 #  задаем количество цифр в секретном числе
        secret_number = generate_secret_number(number_of_digits) # генерируем секретное число
        if not secret_number: # если секретное число не сгенерировалось
            logger.error('Failed to generate secret number, exiting game') #  логируем ошибку и выходим
            return
        number_of_guesses = 0 #  инициализируем счетчик попыток
        logger.info(f"I am thinking of a number that has {number_of_digits} unique digits. Try to guess it.") #  сообщение пользователю
        while True: #  цикл для игры
            number_of_guesses += 1 #  увеличиваем счетчик попыток
            user_guess = input(f"Guess {number_of_guesses}: Enter a {number_of_digits}-digit guess: ") #  запрашиваем ввод пользователя
            if not user_guess.isdigit() or len(user_guess) != number_of_digits: #  проверяем ввод пользователя на валидность
                logger.info(f"Please enter a {number_of_digits}-digit number.")  #  логируем невалидный ввод
                continue #  продолжаем цикл, запрашивая ввод снова
            if user_guess == secret_number: #  если ввод пользователя правильный
                logger.info(f"You got it in {number_of_guesses} guesses!") #  сообщение о победе
                break #  выходим из цикла
            else: #  если ввод пользователя не правильный
                clues = get_clues(user_guess, secret_number)  #  получаем подсказки
                logger.info(f"Clues: {clues}")  #  логируем подсказки
    except Exception as ex: #  отлавливаем ошибки
        logger.error('An error occurred during the game', ex)  #  логируем ошибку


if __name__ == "__main__":
    play_bagels_game() #  запускаем игру
```