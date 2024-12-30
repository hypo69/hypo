# Анализ кода модуля `checkr.py`

**Качество кода**
  -  Соответствие требованиям к формату кода (1-10): 7
 -  Преимущества:
       - Код хорошо структурирован и разбит на функции, что облегчает его понимание и поддержку.
       - Присутствуют базовые проверки валидности ходов.
       - Есть комментарии, объясняющие основную логику работы.
 -  Недостатки:
    -  Отсутствуют docstring для функций, что затрудняет понимание их назначения и параметров.
    -  Используются глобальные переменные, что может привести к проблемам в более сложных программах.
    -  Обработка ошибок ввода не является полной (например, не проверяется ввод на нечисловые значения)
    -  Не используется `j_loads` или `j_loads_ns` для чтения данных.
    -  Нет логирования ошибок через `logger.error`.

**Рекомендации по улучшению**

1.  **Документация**: Добавить docstring в формате reStructuredText (RST) для всех функций, классов и методов.
2.  **Глобальные переменные**:  Избегать использования глобальных переменных, передавая их как параметры.
3.  **Обработка ошибок**: Добавить более надежную обработку ошибок, включая использование `logger.error` для логирования исключений.
4.  **Ввод данных**: Использовать `j_loads` или `j_loads_ns` для чтения данных.
5.  **Логика**: Улучшить логику проверки ходов, например, добавить возможность "съедать" шашки противника.
6.  **Именование**: Использовать более осмысленные имена для переменных и функций.
7. **Структура**: Разделить на классы для улучшение читаемости и возможность расширения.
8. **Типизация**: Добавить аннотацию типов для функций.

**Улучшенный код**
```python
"""
Модуль для реализации игры в шашки
=========================================================================================

Модуль содержит функции для инициализации, отрисовки, проверки ходов и
реализации логики игры в шашки. Игра происходит на доске 8x8, где игрок
играет против компьютера.

Пример использования
--------------------

.. code-block:: python

    if __name__ == "__main__":
        game = CheckersGame()
        game.play_checkers()

"""
import random # Импортирует модуль random для генерации случайных ходов компьютера
from typing import List, Tuple # Импортирует типы данных для аннотаций
from src.logger.logger import logger # Импортирует logger для логирования ошибок

# Константы для представления доски
BOARD_SIZE = 8
EMPTY = '.'
PLAYER = '1'
COMPUTER = '2'


class CheckersGame:
    """
    Класс для управления игрой в шашки.
    """

    def __init__(self):
        """
        Инициализирует игру с новой доской.

        :ivar board: Игровая доска в виде списка списков.
        """
        self.board = self.initialize_board() # Инициализирует игровую доску

    def initialize_board(self) -> List[List[str]]:
        """
        Инициализирует доску 8x8 с начальным расположением шашек.

        :return: Игровая доска в виде списка списков.
        """
        board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)] # Создает пустую доску
        # Размещаем шашки игрока и компьютера в начальных позициях
        for i in range(3):
            for j in range(BOARD_SIZE):
                if (i + j) % 2 != 0:
                    board[i][j] = PLAYER # Расставляет шашки игрока
        for i in range(BOARD_SIZE - 3, BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if (i + j) % 2 != 0:
                    board[i][j] = COMPUTER # Расставляет шашки компьютера
        return board

    def draw_board(self) -> None:
        """
        Отрисовывает текущее состояние доски в консоль.
        """
        print("  ", end="")
        for i in range(BOARD_SIZE):
            print(i, end=" ")
        print()
        for i, row in enumerate(self.board):
            print(i, " ".join(row)) # Выводит доску на экран

    def is_valid_move(self, row: int, col: int, new_row: int, new_col: int, player: str) -> bool:
        """
        Проверяет, является ли ход игрока допустимым.

        :param row: Текущая строка позиции шашки.
        :param col: Текущий столбец позиции шашки.
        :param new_row: Новая строка позиции шашки.
        :param new_col: Новый столбец позиции шашки.
        :param player: Символ игрока ('1' или '2').
        :return: True, если ход допустим, иначе False.
        """
        if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and 0 <= new_row < BOARD_SIZE and 0 <= new_col < BOARD_SIZE):
            return False # Проверяет, находится ли ход в пределах доски

        if self.board[row][col] != player:
            return False # Проверяет, принадлежит ли шашка игроку

        if self.board[new_row][new_col] != EMPTY:
            return False # Проверяет, является ли целевая клетка пустой

        row_diff = new_row - row
        col_diff = new_col - col

        if abs(row_diff) != 1 or abs(col_diff) != 1:
            return False # Проверяет, что ход на одну клетку по диагонали

        if player == PLAYER and row_diff > 0:
            return False  # Проверяет, что шашка игрока движется только вперед

        if player == COMPUTER and row_diff < 0:
             return False # Проверяет, что шашка компьютера движется только вперед

        return True

    def update_board(self, row: int, col: int, new_row: int, new_col: int) -> None:
        """
        Обновляет доску после хода.

        :param row: Текущая строка позиции шашки.
        :param col: Текущий столбец позиции шашки.
        :param new_row: Новая строка позиции шашки.
        :param new_col: Новый столбец позиции шашки.
        """
        self.board[new_row][new_col] = self.board[row][col] # Обновляет доску
        self.board[row][col] = EMPTY # Освобождает предыдущую клетку

    def check_win(self, player: str) -> bool:
        """
        Проверяет, достиг ли игрок или компьютер победы.

        :param player: Символ игрока ('1' или '2').
        :return: True, если игрок победил, иначе False.
        """
        if player == PLAYER:
            for j in range(BOARD_SIZE):
                if self.board[BOARD_SIZE-1][j] == PLAYER:
                    return True # Проверяет, достиг ли игрок конца доски
        if player == COMPUTER:
            for j in range(BOARD_SIZE):
                if self.board[0][j] == COMPUTER:
                    return True # Проверяет, достиг ли компьютер конца доски
        return False

    def get_computer_moves(self) -> List[Tuple[int, int, int, int]]:
        """
        Находит все возможные ходы компьютера.

        :return: Список возможных ходов в виде кортежей (row, col, new_row, new_col).
        """
        moves = []
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col] == COMPUTER: # Проверяет, является ли текущая клетка шашкой компьютера
                    for dr in [-1, 1]:
                        for dc in [-1, 1]:
                            new_row, new_col = row + dr, col + dc
                            if self.is_valid_move(row, col, new_row, new_col, COMPUTER):
                                moves.append((row, col, new_row, new_col)) # Добавляет допустимый ход в список
        return moves

    def computer_turn(self) -> None:
        """
        Выполняет ход компьютера.
        """
        possible_moves = self.get_computer_moves()
        if possible_moves:
            row, col, new_row, new_col = random.choice(possible_moves)
            self.update_board(row, col, new_row, new_col) # Выбирает случайный ход и обновляет доску

    def player_turn(self) -> None:
        """
        Запрашивает и выполняет ход игрока.
        """
        while True:
            try:
                current_row = int(input("Введите строку текущей позиции (0-7): "))
                current_col = int(input("Введите столбец текущей позиции (0-7): "))
                new_row = int(input("Введите строку новой позиции (0-7): "))
                new_col = int(input("Введите столбец новой позиции (0-7): "))
                if self.is_valid_move(current_row, current_col, new_row, new_col, PLAYER):
                    self.update_board(current_row, current_col, new_row, new_col) # Обновляет доску, если ход допустим
                    break
                else:
                    print("Недопустимый ход, попробуйте еще раз.")
            except ValueError as ex:
                logger.error(f'Ошибка ввода. Пожалуйста, введите целые числа.{ex}') # Логирует ошибку ввода
                print("Ошибка ввода. Пожалуйста, введите целые числа.")
                ...
                continue

    def play_checkers(self) -> None:
        """
        Основная функция игры в шашки.
        """
        self.draw_board()
        while True:
            self.player_turn()
            if self.check_win(PLAYER):
                print("Поздравляю! Вы выиграли!")
                break

            self.computer_turn()
            if self.check_win(COMPUTER):
                print("Компьютер выиграл!")
                break
            self.draw_board()


if __name__ == "__main__":
    game = CheckersGame()
    game.play_checkers()
```