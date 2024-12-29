# Анализ кода модуля `36_digits.ru.md`

**Качество кода**

- **Соответствие требованиям к формату кода (1-10):**

  - **Преимущества:**
    - Документ содержит подробное описание игры "DIGITS" на русском языке, включая правила, пошаговую инструкцию, примеры работы, ограничения и рекомендации по реализации.
    - Текст структурирован с использованием заголовков, списков и блоков кода, что обеспечивает хорошую читаемость.
    - Присутствуют примеры взаимодействия пользователя с программой, демонстрирующие основные сценарии игры.
    - Описаны возможные ограничения и рекомендации по реализации, что помогает понять, как должен работать код.
  - **Недостатки:**
    - Документ не является исполняемым кодом, а представляет собой текстовое описание игры в формате Markdown. Это не соответствует требованиям к преобразованию кода, которые включают в себя использование reStructuredText (RST) для комментариев и docstring, а также использование `j_loads` или `j_loads_ns` для чтения файлов.
    - Отсутствуют необходимые импорты, функции, классы и переменные, которые могли бы быть прокомментированы в формате RST.

**Рекомендации по улучшению**

1. **Преобразование в исполняемый код:** Необходимо реализовать игру "DIGITS" на Python, следуя описанной в документе логике.
2. **Добавление reStructuredText комментариев:** Все функции, методы, классы и переменные должны быть прокомментированы с использованием RST.
3. **Использование `j_loads` для чтения файлов:** Если в реализации потребуется чтение данных из файлов, следует использовать `j_loads` или `j_loads_ns`.
4. **Логирование ошибок:** Следует использовать `from src.logger.logger import logger` для логирования ошибок и избегать чрезмерного использования блоков `try-except`.
5. **Внедрение примеров и улучшений (TODO):** Добавить примеры документирования в RST и улучшения в формате TODO.

**Улучшенный код**

```python
"""
Модуль для игры "Угадай число" (DIGITS)
=========================================================================================

Этот модуль реализует игру, в которой компьютер загадывает случайное число, а пользователь пытается его угадать.

Пример использования:

.. code-block:: python

   game = DigitsGame()
   game.start_game()
"""
import random
from src.logger.logger import logger # Добавлен импорт logger #
from typing import List, Tuple

class DigitsGame:
    """
    Класс, реализующий игру "Угадай число" (DIGITS).

    :ivar min_digits: Минимальное количество цифр в загаданном числе.
    :vartype min_digits: int
    :ivar max_digits: Максимальное количество цифр в загаданном числе.
    :vartype max_digits: int
    """
    def __init__(self, min_digits: int = 2, max_digits: int = 5):
        """
        Инициализирует игру с заданным минимальным и максимальным количеством цифр.

        :param min_digits: Минимальное количество цифр в загаданном числе (по умолчанию 2).
        :param max_digits: Максимальное количество цифр в загаданном числе (по умолчанию 5).
        :raises ValueError: Если `min_digits` меньше 1 или `max_digits` меньше `min_digits`.
        """
        if min_digits < 1 or max_digits < min_digits:
            raise ValueError('Количество цифр должно быть больше 0 и min_digits <= max_digits') # Добавлена проверка на валидность количества цифр
        self.min_digits = min_digits
        self.max_digits = max_digits
    
    def generate_secret_number(self, num_digits: int) -> str:
        """
        Генерирует случайное число заданной длины с уникальными цифрами.

        :param num_digits: Количество цифр в загаданном числе.
        :type num_digits: int
        :return: Загаданное число в виде строки.
        :rtype: str
        """
        digits = list(range(10))
        random.shuffle(digits)
        return ''.join(map(str, digits[:num_digits]))

    def get_user_input(self, num_digits: int) -> str:
        """
        Запрашивает у пользователя ввод числа и проверяет его корректность.

        :param num_digits: Количество цифр в числе, которое нужно ввести.
        :type num_digits: int
        :return: Число, введенное пользователем, в виде строки.
        :rtype: str
        """
        while True:
            try:
                user_input = input(f'Введите ваше предположение (число из {num_digits} цифр): ')
                if not user_input.isdigit():
                    print('Ошибка: Ввод должен содержать только цифры.') # Сообщение об ошибке при вводе не цифр #
                    continue
                if len(user_input) != num_digits:
                    print(f'Ошибка: Число должно содержать {num_digits} цифр.') # Сообщение об ошибке при неверной длине #
                    continue
                if len(set(user_input)) != num_digits:
                    print('Ошибка: Цифры в числе должны быть уникальными.') # Сообщение об ошибке при повторяющихся цифрах #
                    continue
                return user_input
            except Exception as ex: # Обработка ошибок ввода
                logger.error(f'Ошибка ввода: {ex}') # Логирование ошибки ввода #
                print('Произошла ошибка при обработке ввода. Попробуйте еще раз.') # Сообщение об ошибке

    def compare_numbers(self, secret_number: str, user_guess: str) -> Tuple[int, int]:
        """
        Сравнивает загаданное число с предположением пользователя и возвращает количество угаданных цифр на своих местах и не на своих местах.

        :param secret_number: Загаданное число.
        :type secret_number: str
        :param user_guess: Предположение пользователя.
        :type user_guess: str
        :return: Кортеж из количества угаданных на своих местах и количества угаданных не на своих местах.
        :rtype: Tuple[int, int]
        """
        correct_place = 0
        correct_number = 0
        for i, digit in enumerate(user_guess):
            if digit == secret_number[i]:
                correct_place += 1
            elif digit in secret_number:
                correct_number += 1
        return correct_place, correct_number

    def play_again(self) -> bool:
        """
        Спрашивает пользователя, хочет ли он сыграть еще раз.

        :return: True, если пользователь хочет сыграть снова, False в противном случае.
        :rtype: bool
        """
        while True:
            try:
                choice = input('Хотите сыграть снова? (да/нет): ').lower()
                if choice in ['да', 'нет']:
                    return choice == 'да'
                else:
                    print('Пожалуйста, введите "да" или "нет".')
            except Exception as ex: # Обработка ошибки ввода
                logger.error(f'Ошибка ввода: {ex}') # Логирование ошибки
                print('Произошла ошибка при обработке ввода. Попробуйте еще раз.') # Сообщение об ошибке

    def start_game(self):
        """
        Запускает игру DIGITS.
        """
        print('Добро пожаловать в игру DIGITS!') # Приветствие
        while True:
            try:
                num_digits = int(input(f'Укажите количество цифр в загаданном числе (от {self.min_digits} до {self.max_digits}): '))
                if not self.min_digits <= num_digits <= self.max_digits: # Проверка ввода кол-ва цифр
                     print(f'Ошибка: Количество цифр должно быть от {self.min_digits} до {self.max_digits}.') # Сообщение об ошибке
                     continue
                
                secret_number = self.generate_secret_number(num_digits)
                print(f'Компьютер загадал число из {num_digits} уникальных цифр. Попробуйте угадать!')
                attempts = 0
                while True:
                    user_guess = self.get_user_input(num_digits) # Получение ввода пользователя
                    attempts += 1
                    correct_place, correct_number = self.compare_numbers(secret_number, user_guess) # Сравнение чисел
                    print(f'Угадано и на правильном месте: {correct_place}')
                    print(f'Угадано, но не на своём месте: {correct_number}')

                    if correct_place == num_digits:
                         print(f'Поздравляем! Вы угадали число: {secret_number}')
                         print(f'Количество попыток: {attempts}') # Вывод количества попыток
                         break
            except Exception as ex: # Обработка ошибок ввода и генерации числа
                logger.error(f'Произошла ошибка в ходе игры: {ex}') # Логирование ошибки
                print('Произошла непредвиденная ошибка. Пожалуйста, попробуйте еще раз.') # Сообщение об ошибке
            if not self.play_again():
                print('Спасибо за игру!')
                break

if __name__ == '__main__':
    game = DigitsGame()
    game.start_game()
```