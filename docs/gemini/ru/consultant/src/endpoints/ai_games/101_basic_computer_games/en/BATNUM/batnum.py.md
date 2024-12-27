# Анализ кода модуля `batnum.py`

**Качество кода**
8
-  Плюсы
    - Код содержит подробное описание игры и алгоритма.
    - Присутствует блок-схема игры в формате Mermaid.
    - Есть базовая обработка исключений при вводе.
    - Код игры достаточно понятен и прост для восприятия.
-  Минусы
    - Отсутствуют docstring для модуля.
    - Используется глобальная переменная `totalSum`.
    - Код не содержит логирование ошибок.
    - Повторяющийся код для ввода игроков.
    - Нет возможности настройки параметров игры.
    - Не используется форматирование строк f-string для вывода сообщений.

**Рекомендации по улучшению**
1. Добавить docstring для модуля в формате reStructuredText (RST).
2. Использовать функции для ввода и проверки ввода игроков, чтобы избежать дублирования кода.
3. Добавить обработку исключений с использованием `logger.error` для логирования ошибок.
4. Использовать форматирование строк f-string для вывода сообщений.
5. Инкапсулировать логику игры в класс `BatNumGame`, чтобы избежать использования глобальных переменных и добавить возможность настройки параметров игры.
6. Добавить возможность настройки параметров игры.

**Оптимизированный код**
```python
"""
BATNUM: BATNUM
=================
Модуль реализует игру "Битва чисел" (BATNUM), в которой два игрока по очереди вводят числа от 1 до 10.
Цель игры - не допустить, чтобы сумма достигла 100 или более.

:Особенности:
    -   Игра реализована с использованием цикла while и функций для ввода и проверки ввода игроков.
    -   Присутствует обработка исключений с использованием try-except для корректного ввода чисел.
    -   Используется форматирование строк f-string для вывода сообщений.
    -   Предусмотрена возможность настройки параметров игры.

:Пример использования:
    .. code-block:: python

        game = BatNumGame()
        game.play()

:Автор:
    hypo69 (hypo69@davidka.net)

"""
from src.logger.logger import logger

__author__ = 'hypo69 (hypo69@davidka.net)'


class BatNumGame:
    """
    Класс, реализующий игру "Битва чисел".

    :param max_sum: Максимальное значение суммы, при достижении которого игрок проигрывает.
    :type max_sum: int
    :param min_input: Минимальное значение, которое может ввести игрок.
    :type min_input: int
    :param max_input: Максимальное значение, которое может ввести игрок.
    :type max_input: int
    """
    def __init__(self, max_sum: int = 100, min_input: int = 1, max_input: int = 10):
        """
        Инициализирует игру с заданными параметрами.
        """
        self.total_sum = 0
        self.max_sum = max_sum
        self.min_input = min_input
        self.max_input = max_input

    def get_player_input(self, player_number: int) -> int:
        """
        Запрашивает ввод числа у игрока и проверяет его корректность.

        :param player_number: Номер игрока (1 или 2).
        :type player_number: int
        :return: Введенное число.
        :rtype: int
        """
        while True:
            try:
                player_input = int(input(f"Игрок {player_number}, введите число от {self.min_input} до {self.max_input}: "))
                if self.min_input <= player_input <= self.max_input:
                    return player_input
                else:
                    print(f"Пожалуйста, введите число от {self.min_input} до {self.max_input}.")
            except ValueError as e:
                logger.error(f"Ошибка ввода для игрока {player_number}: {e}")
                print("Пожалуйста, введите целое число.")

    def play(self) -> None:
        """
        Запускает игровой процесс.
        """
        while True:
            # Ход первого игрока
            print(f"Текущая сумма: {self.total_sum}")
            player1_input = self.get_player_input(1)
            self.total_sum += player1_input

            # Проверка, не проиграл ли первый игрок
            if self.total_sum >= self.max_sum:
                print("Игрок 1 проиграл!")
                break

            # Ход второго игрока
            print(f"Текущая сумма: {self.total_sum}")
            player2_input = self.get_player_input(2)
            self.total_sum += player2_input

            # Проверка, не проиграл ли второй игрок
            if self.total_sum >= self.max_sum:
                print("Игрок 2 проиграл!")
                break


if __name__ == "__main__":
    #  код исполняет запуск игры
    game = BatNumGame()
    game.play()
```