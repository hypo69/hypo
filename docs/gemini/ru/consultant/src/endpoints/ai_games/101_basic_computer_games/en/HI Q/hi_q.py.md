# Анализ кода модуля `hi_q.py`

**Качество кода: 7/10**

*   **Плюсы:**
    *   Код хорошо структурирован и разбит на логические функции.
    *   Используются понятные имена переменных и функций.
    *   Реализована основная логика игры HI Q.
    *   Присутствуют проверки на допустимость хода и корректный ввод.
    *   Есть комментарии, объясняющие назначение основных частей кода.
*   **Минусы:**
    *   Отсутствует docstring у модуля.
    *   Не все функции имеют docstring, особенно те, которые могут быть сложнее для понимания.
    *   Не используется `j_loads` или `j_loads_ns` для чтения файлов (хотя в этом файле и нет чтения файлов, но замечание стоит учесть для будущих аналогичных файлов)
    *   Не используется `from src.logger.logger import logger` для логирования ошибок, и обработки ошибок
    *   Ввод пользователя обрабатывается через `try-except`, что можно улучшить.
    *   Отсутствуют проверки на корректность работы функций, кроме базовых проверок ввода.

**Рекомендации по улучшению**

1.  **Добавить docstring для модуля:** В начале файла необходимо добавить docstring в формате RST с описанием модуля.
2.  **Добавить docstring для каждой функции:** Необходимо добавить docstring в формате RST для каждой функции с описанием её назначения, параметров и возвращаемого значения.
3.  **Использовать `j_loads` или `j_loads_ns`:**  Хотя в данном коде нет операций с файлами, необходимо иметь ввиду использование `j_loads` или `j_loads_ns` из `src.utils.jjson` при чтении файлов в будущих аналогичных файлах.
4.  **Логирование ошибок:** Необходимо использовать `from src.logger.logger import logger` для логирования ошибок.  `try-except` заменить на `logger.error` для обработки исключений.
5.  **Рефакторинг ввода пользователя:** Убрать избыточное использование `try-except` при вводе пользователя, заменить на более конкретную проверку введенных данных
6.  **Добавить проверки:** Добавить проверки для корректной работы функций.
7.  **Использовать константы:**  Использовать константы для размеров доски и других магических чисел.
8.  **Улучшить читаемость `is_valid_move`:**  Упростить логику проверки хода.
9.  **Улучшить `has_moves`:** Избегать повторения вызова `is_valid_move`

**Оптимизированный код**

```python
"""
Игра HI Q
=========================================================================================

Эта игра представляет собой реализацию головоломки, в которой нужно удалить шарики с доски,
перепрыгивая через них. Цель игры - оставить на доске только один шарик.
Игрок выбирает шарик и направление, в котором он будет перепрыгивать.
Игра заканчивается, когда больше нет возможных ходов или остался только один шарик.

Пример использования
--------------------

.. code-block:: python

    play_hi_q()

"""
from src.logger.logger import logger

BOARD_SIZE = 7
PEG = 1
EMPTY = 0


def init_board():
    """
    Инициализирует игровое поле с начальным расположением шариков.

    :return: Список списков, представляющий доску.
    :rtype: list[list[int]]
    """
    board = [
        [EMPTY, EMPTY, PEG, PEG, PEG, EMPTY, EMPTY],
        [EMPTY, EMPTY, PEG, PEG, PEG, EMPTY, EMPTY],
        [PEG, PEG, PEG, PEG, PEG, PEG, PEG],
        [PEG, PEG, PEG, EMPTY, PEG, PEG, PEG],
        [PEG, PEG, PEG, PEG, PEG, PEG, PEG],
        [EMPTY, EMPTY, PEG, PEG, PEG, EMPTY, EMPTY],
        [EMPTY, EMPTY, PEG, PEG, PEG, EMPTY, EMPTY]
    ]
    return board


def print_board(board):
    """
    Выводит текущее состояние игрового поля на экран.

    :param board: Список списков, представляющий доску.
    :type board: list[list[int]]
    """
    for row in board:
        print(' '.join(map(str, row)))


def get_move():
    """
    Запрашивает у пользователя координаты шарика и направление хода.

    :return: Кортеж (row, col, direction), где direction: 'u', 'd', 'l', 'r'.
    :rtype: tuple[int, int, str]
    """
    while True:
        try:
            row = int(input(f"Введите строку шарика (0-{BOARD_SIZE - 1}): "))
            col = int(input(f"Введите столбец шарика (0-{BOARD_SIZE - 1}): "))
            direction = input("Введите направление (u/d/l/r): ").lower()
            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and direction in ['u', 'd', 'l', 'r']:
                return row, col, direction
            else:
                logger.error("Неверный ввод. Попробуйте еще раз.")
        except ValueError as e:
            logger.error(f"Неверный ввод. Попробуйте еще раз. Ошибка: {e}")

def is_valid_move(board, row, col, direction):
    """
    Проверяет, является ли ход допустимым.

    :param board: Список списков, представляющий доску.
    :type board: list[list[int]]
    :param row: Строка выбранного шарика.
    :type row: int
    :param col: Столбец выбранного шарика.
    :type col: int
    :param direction: Направление хода ('u', 'd', 'l', 'r').
    :type direction: str
    :return: True, если ход допустим, иначе False.
    :rtype: bool
    """
    if board[row][col] != PEG: # Проверяем, что в выбранной ячейке есть шарик
        return False

    if direction == 'u':
        if row < 2 or board[row - 1][col] != PEG or board[row - 2][col] != EMPTY:
            return False
    elif direction == 'd':
        if row > BOARD_SIZE - 3 or board[row + 1][col] != PEG or board[row + 2][col] != EMPTY:
            return False
    elif direction == 'l':
        if col < 2 or board[row][col - 1] != PEG or board[row][col - 2] != EMPTY:
            return False
    elif direction == 'r':
        if col > BOARD_SIZE - 3 or board[row][col + 1] != PEG or board[row][col + 2] != EMPTY:
            return False

    return True


def make_move(board, row, col, direction):
    """
    Выполняет ход, обновляя состояние игрового поля.

    :param board: Список списков, представляющий доску.
    :type board: list[list[int]]
    :param row: Строка выбранного шарика.
    :type row: int
    :param col: Столбец выбранного шарика.
    :type col: int
    :param direction: Направление хода ('u', 'd', 'l', 'r').
    :type direction: str
    :return: Обновленный список списков, представляющий доску.
    :rtype: list[list[int]]
    """
    if direction == 'u':
        board[row][col] = EMPTY
        board[row - 1][col] = EMPTY
        board[row - 2][col] = PEG
    elif direction == 'd':
        board[row][col] = EMPTY
        board[row + 1][col] = EMPTY
        board[row + 2][col] = PEG
    elif direction == 'l':
        board[row][col] = EMPTY
        board[row][col - 1] = EMPTY
        board[row][col - 2] = PEG
    elif direction == 'r':
        board[row][col] = EMPTY
        board[row][col + 1] = EMPTY
        board[row][col + 2] = PEG
    return board


def has_moves(board):
    """
    Проверяет, есть ли еще возможные ходы.

    :param board: Список списков, представляющий доску.
    :type board: list[list[int]]
    :return: True, если есть возможные ходы, иначе False.
    :rtype: bool
    """
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == PEG:
                for direction in ['u', 'd', 'l', 'r']:
                    if is_valid_move(board, row, col, direction):
                        return True
    return False


def count_pegs(board):
    """
    Считает количество шариков на доске.

    :param board: Список списков, представляющий доску.
    :type board: list[list[int]]
    :return: Количество шариков.
    :rtype: int
    """
    count = 0
    for row in board:
        count += row.count(PEG)
    return count


def play_hi_q():
    """
    Основная функция игры HI Q.

    Содержит игровой цикл, управление ходами и проверку на победу/проигрыш.
    """
    board = init_board()
    while True:
        print_board(board)
        row, col, direction = get_move()
        if is_valid_move(board, row, col, direction):
            board = make_move(board, row, col, direction)
            if count_pegs(board) == 1:
                print_board(board)
                print("Поздравляю! Вы выиграли!")
                break
            if not has_moves(board):
                print_board(board)
                print("Увы, ходов больше нет. Вы проиграли!")
                break
        else:
            print("Недопустимый ход. Попробуйте еще раз.")


if __name__ == "__main__":
    play_hi_q()
```