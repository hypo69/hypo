# анализ кода модуля checkr.py

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и разбит на отдельные функции, каждая из которых выполняет конкретную задачу.
    - Присутствует документация на иврите, объясняющая логику работы игры и отдельных функций.
    - Код соответствует основным требованиям к игре "Шашки", включая правила передвижения фигур и определение победителя.
    -  Есть описание алгоритма, диаграмма состояний, и легенда к диаграмме.
    -   Логика игры реализована понятно, с проверками допустимости ходов и возможностью "повышения" фигуры до "дамки".
-  Минусы
    - Отсутствует документация в формате reStructuredText (RST).
    -  Используются стандартные `print` для вывода сообщений пользователю и сообщений об ошибках.
    -  Код не использует логирование ошибок.
    -  Не используется `j_loads` или `j_loads_ns` для чтения файлов (в данном коде файлов нет, но согласно инструкции это нужно учесть).
    -  Имена переменных и функций на иврите не соответствуют общепринятым стандартам Python (хотя это и специфика задания), и их следует переписать в соответствии с PEP8.
    -  Обработка ошибок ввода пользователя в цикле не очень эффективна, и следует использовать более удобные инструменты.
    -  Нет проверки на ввод букв или других недопустимых символов, только на `ValueError`.
    -  Отсутствует проверка на ввод отрицательных чисел или чисел больше 7.
    -  Невозможность отмены хода.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Переписать все комментарии и docstring в формате reStructuredText (RST).
    -   Добавить описания ко всем функциям, классам и методам, используя RST.
2.  **Логирование**:
    -   Использовать `from src.logger.logger import logger` для логирования ошибок и отладочной информации.
    -   Заменить `print` на `logger.info`, `logger.error` или `logger.debug` в зависимости от ситуации.
3.  **Обработка данных**:
    -  Хотя в текущем коде нет работы с файлами, следует учитывать требование использовать `j_loads` или `j_loads_ns` при работе с файлами в будущем.
4.  **Рефакторинг**:
    -   Переименовать функции и переменные в соответствии с PEP8, например, `initialize_board` -> `init_board`, `current_player` -> `current_player_id`
    -   Избавиться от магических чисел, например `8`, с помощью констант или переменных.
    -   Разделить функции на более мелкие и переиспользовать, если это возможно.
    -   Улучшить обработку ошибок ввода пользователя.
5.  **Улучшение функциональности**:
    -   Добавить возможность отмены хода.
    -   Добавить проверку на ввод отрицательных чисел или чисел больше 7.
6. **Безопасность**
    - Добавить проверку на ввод букв или других недопустимых символов, помимо `ValueError`.

**Оптимизиробанный код**

```python
"""
Модуль для реализации игры в шашки.
=====================================

Модуль содержит функции для инициализации игрового поля, отображения доски,
проверки ходов, выполнения ходов, проверки повышения в дамки и определения победителя.

Пример использования
--------------------

.. code-block:: python

    if __name__ == "__main__":
        play_checkers()
"""

import copy
from src.logger.logger import logger # импорт модуля для логирования

BOARD_SIZE = 8 # размер доски
PLAYER1 = '1' # представление первого игрока
PLAYER2 = '2' # представление второго игрока
EMPTY_CELL = ' ' # представление пустой ячейки

# TODO: добавьте константы для дамки (например, KING1 = 'A', KING2 = 'B')

def init_board() -> list[list[str]]:
    """
    Инициализирует игровое поле.

    :return: Двумерный список, представляющий игровое поле.
    :rtype: list[list[str]]
    """
    board = [[EMPTY_CELL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    # Инициализация доски с начальными позициями фигур
    for row in range(0, 3):
        for col in range(BOARD_SIZE):
            if (row + col) % 2 == 1:
                board[row][col] = PLAYER1
    for row in range(5, BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if (row + col) % 2 == 1:
                board[row][col] = PLAYER2
    return board

def display_board(board: list[list[str]]):
    """
    Выводит текущее состояние игрового поля.

    :param board: Двумерный список, представляющий игровое поле.
    :type board: list[list[str]]
    """
    print("  0 1 2 3 4 5 6 7")
    for i, row in enumerate(board):
        print(i, " ".join(row))

def validate_move(board: list[list[str]], start_row: int, start_col: int, end_row: int, end_col: int, current_player_id: int) -> bool:
    """
    Проверяет, является ли ход допустимым.

    :param board: Двумерный список, представляющий игровое поле.
    :type board: list[list[str]]
    :param start_row: Начальная строка.
    :type start_row: int
    :param start_col: Начальный столбец.
    :type start_col: int
    :param end_row: Конечная строка.
    :type end_row: int
    :param end_col: Конечный столбец.
    :type end_col: int
    :param current_player_id: Идентификатор текущего игрока (1 или 2).
    :type current_player_id: int
    :return: True, если ход допустим, False в противном случае.
    :rtype: bool
    """
    # Проверка на допустимость координат
    if not (0 <= start_row < BOARD_SIZE and 0 <= start_col < BOARD_SIZE and 0 <= end_row < BOARD_SIZE and 0 <= end_col < BOARD_SIZE):
        logger.error("Недопустимые координаты") # логирование ошибки
        return False

    piece = board[start_row][start_col]
    # Проверка принадлежности фигуры текущему игроку
    if piece != str(current_player_id) and piece != str(current_player_id).upper():
        logger.error("Это не ваша фигура")# логирование ошибки
        return False

    row_diff = end_row - start_row
    col_diff = end_col - start_col
    abs_row_diff = abs(row_diff)
    abs_col_diff = abs(col_diff)
    # Проверка простого хода
    if abs_row_diff == 1 and abs_col_diff == 1:
        if board[end_row][end_col] == EMPTY_CELL:
             if current_player_id == 1:
                 if row_diff > 0:
                      return True
             elif current_player_id == 2:
                 if row_diff < 0:
                      return True
        else:
             logger.error("Ячейка назначения не пуста")# логирование ошибки
             return False
    # Проверка хода с прыжком
    elif abs_row_diff == 2 and abs_col_diff == 2:
        jumped_row = (start_row + end_row) // 2
        jumped_col = (start_col + end_col) // 2

        if board[end_row][end_col] != EMPTY_CELL:
             logger.error("Ячейка назначения не пуста") # логирование ошибки
             return False
        jumped_piece = board[jumped_row][jumped_col]
        if jumped_piece == EMPTY_CELL or jumped_piece == str(current_player_id) or jumped_piece == str(current_player_id).upper():
            logger.error("Нет фигуры для прыжка") # логирование ошибки
            return False
        return True

    logger.error("Недопустимый ход") # логирование ошибки
    return False


def execute_move(board: list[list[str]], start_row: int, start_col: int, end_row: int, end_col: int, current_player_id: int):
    """
    Выполняет ход на игровом поле.

    :param board: Двумерный список, представляющий игровое поле.
    :type board: list[list[str]]
    :param start_row: Начальная строка.
    :type start_row: int
    :param start_col: Начальный столбец.
    :type start_col: int
    :param end_row: Конечная строка.
    :type end_row: int
    :param end_col: Конечный столбец.
    :type end_col: int
    :param current_player_id: Идентификатор текущего игрока (1 или 2).
    :type current_player_id: int
    """
    piece = board[start_row][start_col]
    board[start_row][start_col] = EMPTY_CELL
    board[end_row][end_col] = piece

    row_diff = abs(end_row - start_row)
    col_diff = abs(end_col - start_col)
    # Если ход был прыжком, удаляем съеденную фигуру
    if row_diff == 2 and col_diff == 2:
         jumped_row = (start_row + end_row) // 2
         jumped_col = (start_col + end_col) // 2
         board[jumped_row][jumped_col] = EMPTY_CELL


def check_promotion(board: list[list[str]], end_row: int, end_col: int, current_player_id: int) -> bool:
    """
    Проверяет, достигла ли фигура конца доски и должна ли быть повышена.

    :param board: Двумерный список, представляющий игровое поле.
    :type board: list[list[str]]
    :param end_row: Конечная строка.
    :type end_row: int
    :param end_col: Конечный столбец.
    :type end_col: int
    :param current_player_id: Идентификатор текущего игрока (1 или 2).
    :type current_player_id: int
    :return: True если фигура была повышена, False в противном случае
    :rtype: bool
    """
    if current_player_id == 1 and end_row == 7:
         board[end_row][end_col] = '1'.upper() # TODO: заменить на константу
         return True
    elif current_player_id == 2 and end_row == 0:
         board[end_row][end_col] = '2'.upper()  # TODO: заменить на константу
         return True
    return False


def has_valid_moves(board: list[list[str]], current_player_id: int) -> bool:
    """
    Проверяет, есть ли у игрока доступные ходы.

    :param board: Двумерный список, представляющий игровое поле.
    :type board: list[list[str]]
    :param current_player_id: Идентификатор текущего игрока (1 или 2).
    :type current_player_id: int
    :return: True если ходы доступны, False в противном случае
    :rtype: bool
    """
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            piece = board[row][col]
            if piece == str(current_player_id) or piece == str(current_player_id).upper():
                for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                      new_row, new_col = row + dr, col + dc
                      if validate_move(board, row, col, new_row, new_col, current_player_id):
                         return True
                for dr, dc in [(-2, -2), (-2, 2), (2, -2), (2, 2)]:
                      new_row, new_col = row + dr, col + dc
                      if validate_move(board, row, col, new_row, new_col, current_player_id):
                         return True
    return False


def check_winner(board: list[list[str]]) -> int:
    """
    Проверяет, есть ли победитель в игре.

    :param board: Двумерный список, представляющий игровое поле.
    :type board: list[list[str]]
    :return: Идентификатор победителя (1 или 2), или 0 если победителя нет
    :rtype: int
    """
    player1_pieces = 0
    player2_pieces = 0

    for row in board:
        for cell in row:
            if cell == PLAYER1 or cell == PLAYER1.upper():
                player1_pieces += 1
            elif cell == PLAYER2 or cell == PLAYER2.upper():
                player2_pieces += 1

    if player1_pieces == 0:
        return 2
    elif player2_pieces == 0:
        return 1
    else:
        return 0


def play_checkers():
    """
    Запускает игровой процесс.
    """
    board = init_board()
    current_player_id = 1 # первый игрок начинает
    display_board(board)

    while True:
        if not has_valid_moves(board, current_player_id):
            other_player_id = 3 - current_player_id
            winner = check_winner(board)
            if winner != 0:
                print(f"Игрок {winner} победил!")
                break
            else:
                print(f"У игрока {current_player_id} нет доступных ходов, игрок {other_player_id} победил!")
                break

        print(f"Ход игрока {current_player_id}")
        while True:
            try:
                start_row = int(input("Выберите строку фигуры: "))
                start_col = int(input("Выберите столбец фигуры: "))
                end_row = int(input("Выберите строку ячейки назначения: "))
                end_col = int(input("Выберите столбец ячейки назначения: "))
                if validate_move(board, start_row, start_col, end_row, end_col, current_player_id):
                  break
            except ValueError:
                print("Недопустимый ввод, пожалуйста введите целые числа.")
            except Exception as e: # Общая обработка ошибок ввода
                logger.error(f"Неизвестная ошибка ввода: {e}")

        execute_move(board, start_row, start_col, end_row, end_col, current_player_id)
        check_promotion(board, end_row, end_col, current_player_id)
        display_board(board)

        current_player_id = 3 - current_player_id # смена игрока


if __name__ == "__main__":
    play_checkers()