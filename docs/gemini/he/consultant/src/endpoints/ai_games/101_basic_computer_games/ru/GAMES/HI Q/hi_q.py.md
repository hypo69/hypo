# Анализ кода модуля hi_q.py

**Качество кода**
-   **Соблюдение требований к формату кода (1-10):**
    -   **Преимущества:**
        - Код хорошо структурирован и разбит на функции, что облегчает его понимание и поддержку.
        - Присутствуют комментарии, объясняющие логику работы каждой функции.
        - Имена функций и переменных интуитивно понятны и соответствуют их назначению.
        - Реализация игры соответствует описанию и правилам.
        - Используется цикл `while True` для обеспечения корректного ввода пользовательских данных.
    -   **Недостатки:**
        - Отсутствует документация в формате reStructuredText (RST).
        - Не используются `j_loads` или `j_loads_ns` для загрузки данных (хотя это не требуется в данном коде, поскольку нет загрузки файлов).
        - Нет обработки ошибок с использованием `logger.error`.
        - Нет импорта `logger`.
        - Отсутствует описание модуля в формате reStructuredText.

**Рекомендации по улучшению**
1. Добавить документацию в формате RST для модуля, функций и методов, включая подробное описание параметров и возвращаемых значений.
2.  Использовать `from src.logger.logger import logger` для регистрации ошибок.
3.  Обрабатывать ошибки с помощью `try-except` и записывать их в лог через `logger.error`.
4.  Добавить проверку ввода пользователя для предотвращения ошибок, связанных с некорректным вводом.
5.  Упростить код, например, вынести логику проверки допустимости хода в отдельные функции для каждого направления.
6.  Улучшить читаемость кода, добавив пустые строки для разделения логических блоков.
7.  Заменить многократные проверки на допустимость хода на более компактную структуру.

**Улучшенный код**
```python
"""
Модуль реализует игру HI Q.
=========================================================================================

Игра представляет собой головоломку, в которой необходимо удалить все шарики с доски,
перепрыгивая через них, оставив в конце только один. Игрок выбирает шарик и направление
перемещения. Игра завершается, когда не остается возможных ходов или на доске остается
только один шарик.

Пример использования
--------------------

.. code-block:: python

    if __name__ == "__main__":
        play_hi_q()
"""
from src.logger.logger import logger # импорт logger #
def init_board():
    """
    Инициализирует игровое поле с начальным расположением шариков.

    :return: Список списков, представляющий доску.
    :rtype: list[list[int]]
    """
    board = [
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 0, 0]
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
            row = int(input("Введите строку шарика (0-6): ")) # получение строки от пользователя #
            col = int(input("Введите столбец шарика (0-6): ")) # получение столбца от пользователя #
            direction = input("Введите направление (u/d/l/r): ").lower() # получение направления от пользователя #
            if 0 <= row <= 6 and 0 <= col <= 6 and direction in ['u', 'd', 'l', 'r']: # проверка корректности ввода #
                return row, col, direction
            else:
                print("Неверный ввод. Попробуйте еще раз.")
        except ValueError: # Обработка ошибки ввода нечисловых значений
             print("Неверный ввод. Попробуйте еще раз.") # сообщение об ошибке ввода #

def _is_valid_move_direction(board, row, col, direction): # приватная функция для проверки допустимости хода #
    """
    Вспомогательная функция для проверки допустимости хода в заданном направлении.
    :param board: Текущее состояние игрового поля
    :type board: list[list[int]]
    :param row: Индекс строки выбранного шарика.
    :type row: int
    :param col: Индекс столбца выбранного шарика.
    :type col: int
    :param direction: Направление хода ('u', 'd', 'l', 'r').
    :type direction: str
    :return: True, если ход допустим в заданном направлении, иначе False.
    :rtype: bool
    """
    if direction == 'u':
        return row >= 2 and board[row - 1][col] == 1 and board[row - 2][col] == 0
    if direction == 'd':
        return row <= 4 and board[row + 1][col] == 1 and board[row + 2][col] == 0
    if direction == 'l':
        return col >= 2 and board[row][col - 1] == 1 and board[row][col - 2] == 0
    if direction == 'r':
        return col <= 4 and board[row][col + 1] == 1 and board[row][col + 2] == 0
    return False # если направление неверное - то ход невозможен #

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
    if board[row][col] != 1: # проверка, что в выбранной ячейке есть шарик #
        return False

    return _is_valid_move_direction(board, row, col, direction) # Используем приватную функцию #

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
    try: # обработка возможных ошибок
        if direction == 'u':
            board[row][col] = 0
            board[row - 1][col] = 0
            board[row - 2][col] = 1
        elif direction == 'd':
            board[row][col] = 0
            board[row + 1][col] = 0
            board[row + 2][col] = 1
        elif direction == 'l':
            board[row][col] = 0
            board[row][col - 1] = 0
            board[row][col - 2] = 1
        elif direction == 'r':
            board[row][col] = 0
            board[row][col + 1] = 0
            board[row][col + 2] = 1
    except Exception as ex: # обработка ошибок
        logger.error(f"Ошибка при выполнении хода: {ex}") # запись ошибки в лог #
    return board

def has_moves(board):
    """
    Проверяет, есть ли еще возможные ходы.

    :param board: Список списков, представляющий доску.
    :type board: list[list[int]]
    :return: True, если есть возможные ходы, иначе False.
    :rtype: bool
    """
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 1:
                if any( # проверка есть ли доступные ходы #
                    _is_valid_move_direction(board, row, col, direction) for direction in ['u', 'd', 'l', 'r']
                ):
                    return True
    return False

def count_pegs(board):
    """
    Считает количество шариков на доске.

    :param board: Список списков, представляющий доску.
    :type board: list[list[int]]
    :return: Количество шариков на доске.
    :rtype: int
    """
    count = 0
    for row in board:
        count += row.count(1)
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
        if is_valid_move(board, row, col, direction): # проверка допустимости хода #
            board = make_move(board, row, col, direction) # делаем ход #
            if count_pegs(board) == 1: # проверка остался ли один шарик #
                print_board(board)
                print("Поздравляю! Вы выиграли!")
                break
            if not has_moves(board): # проверяем есть ли еще ходы #
                print_board(board)
                print("Увы, ходов больше нет. Вы проиграли!")
                break
        else:
            print("Недопустимый ход. Попробуйте еще раз.")

if __name__ == "__main__":
    play_hi_q()
```