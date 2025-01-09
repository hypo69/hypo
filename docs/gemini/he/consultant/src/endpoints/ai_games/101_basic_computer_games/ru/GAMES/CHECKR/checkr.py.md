# Анализ кода модуля `checkr.py`

**Качество кода**
-  **Соответствие требованиям к формату кода (1-10)**
   -  *Преимущества:*
        - Код написан на языке Python.
        - Есть описание модуля, функций и алгоритма.
        - Присутствует блок-схема.
        - Код в целом структурирован.
   -  *Недостатки:*
        - Отсутствуют docstring в reStructuredText (RST) формате.
        - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
        - Нет обработки ошибок с помощью `logger.error`.
        - Отсутствуют импорты.
        - Отсутствует логирование.
        - Не все функции имеют docstring.
        - Комментарии не всегда соответствуют стандарту RST.
        - Не используется `from src.logger.logger import logger`.

**Рекомендации по улучшению**
1.  Добавить необходимые импорты.
2.  Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
3.  Добавить docstring в формате reStructuredText (RST) для всех функций, методов и классов.
4.  Использовать `from src.logger.logger import logger` для логирования ошибок.
5.  Заменить стандартные `try-except` блоки на логирование ошибок с помощью `logger.error`.
6.  Улучшить и унифицировать стиль комментариев.
7.  Добавить описание модуля в формате RST.
8.  Использовать кавычки `'` в коде.

**Улучшенный код**
```python
"""
Модуль CHECKR:
=================

Реализация упрощенной текстовой игры в шашки, где игрок играет против компьютера.
Игра ведется на доске 8x8.

Описание игры:
    - Игрок и компьютер ходят по очереди.
    - Игрок управляет шашками, обозначаемыми '1'.
    - Компьютер управляет шашками, обозначаемыми '2'.
    - Ход шашки - перемещение на одну клетку по диагонали вперед.
    - Шашка может перепрыгивать через шашку противника, если за ней есть свободное место.
    - Цель игры - достичь противоположного конца доски одной из своих шашек.
    - Компьютер делает случайный допустимый ход.
    - Игра заканчивается при достижении конца доски или отсутствия допустимых ходов.

Алгоритм:
    1. Инициализация доски 8x8 с начальным расположением шашек.
    2. Отрисовка доски.
    3. Игровой цикл:
        3.1. Запрос хода игрока.
        3.2. Проверка валидности ввода.
        3.3. Выполнение хода игрока.
        3.4. Проверка на победу игрока.
        3.5. Ход компьютера.
        3.6. Проверка на победу компьютера.
        3.7. Отрисовка доски.
    4. Вывод сообщения о победе или поражении.
"""
import random  # Импорт модуля random
from src.logger.logger import logger # Импорт logger для логирования ошибок
from typing import List, Tuple  # Импорт для аннотации типов
#from src.utils.jjson import j_loads #TODO если понадобится загрузка json

# Глобальные переменные для представления доски
BOARD_SIZE = 8
EMPTY = '.'
PLAYER = '1'
COMPUTER = '2'

def initialize_board() -> List[List[str]]:
    """
    Инициализирует доску 8x8 с начальным расположением шашек.

    :return: Двумерный список, представляющий доску.
    :rtype: List[List[str]]
    """
    board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)] # Создание пустой доски
    # Размещение шашек игрока и компьютера в начальных позициях
    for i in range(3):
        for j in range(BOARD_SIZE):
            if (i + j) % 2 != 0:
                board[i][j] = PLAYER  # Размещение шашек игрока
    for i in range(BOARD_SIZE - 3, BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if (i + j) % 2 != 0:
                board[i][j] = COMPUTER # Размещение шашек компьютера
    return board


def draw_board(board: List[List[str]]) -> None:
    """
    Отрисовывает текущее состояние доски в консоль.

    :param board: Двумерный список, представляющий доску.
    :type board: List[List[str]]
    """
    print("  ", end="")
    for i in range(BOARD_SIZE):
        print(i, end=" ") # Вывод номеров столбцов
    print()
    for i, row in enumerate(board):
        print(i, " ".join(row)) # Вывод строк доски с номерами строк


def is_valid_move(board: List[List[str]], row: int, col: int, new_row: int, new_col: int, player: str) -> bool:
    """
    Проверяет, является ли ход игрока допустимым.

    :param board: Двумерный список, представляющий доску.
    :type board: List[List[str]]
    :param row: Текущая строка.
    :type row: int
    :param col: Текущий столбец.
    :type col: int
    :param new_row: Новая строка.
    :type new_row: int
    :param new_col: Новый столбец.
    :type new_col: int
    :param player: Символ игрока ('1' или '2').
    :type player: str
    :return: True, если ход допустим, иначе False.
    :rtype: bool
    """
    if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and 0 <= new_row < BOARD_SIZE and 0 <= new_col < BOARD_SIZE):
        return False # Проверка нахождения в пределах доски

    if board[row][col] != player:
        return False # Проверка, принадлежит ли шашка игроку

    if board[new_row][new_col] != EMPTY:
        return False # Проверка, является ли целевая клетка пустой

    row_diff = new_row - row
    col_diff = new_col - col

    if abs(row_diff) != 1 or abs(col_diff) != 1:
        return False # Проверка на движение только по диагонали на одну клетку

    if player == PLAYER and row_diff > 0:
        return False # Проверка на движение шашки игрока только вперед

    if player == COMPUTER and row_diff < 0:
        return False # Проверка на движение шашки компьютера только вперед

    return True

def update_board(board: List[List[str]], row: int, col: int, new_row: int, new_col: int) -> None:
    """
    Обновляет доску после хода.

    :param board: Двумерный список, представляющий доску.
    :type board: List[List[str]]
    :param row: Текущая строка.
    :type row: int
    :param col: Текущий столбец.
    :type col: int
    :param new_row: Новая строка.
    :type new_row: int
    :param new_col: Новый столбец.
    :type new_col: int
    """
    board[new_row][new_col] = board[row][col] # Перемещение шашки
    board[row][col] = EMPTY # Освобождение старой позиции

def check_win(board: List[List[str]], player: str) -> bool:
    """
    Проверяет, достиг ли игрок или компьютер победы.

    :param board: Двумерный список, представляющий доску.
    :type board: List[List[str]]
    :param player: Символ игрока ('1' или '2').
    :type player: str
    :return: True, если игрок победил, иначе False.
    :rtype: bool
    """
    if player == PLAYER:
        for j in range(BOARD_SIZE):
          if board[BOARD_SIZE-1][j] == PLAYER:
            return True # Проверка достижения последней строки для игрока
    if player == COMPUTER:
        for j in range(BOARD_SIZE):
          if board[0][j] == COMPUTER:
            return True # Проверка достижения первой строки для компьютера
    return False


def get_computer_moves(board: List[List[str]]) -> List[Tuple[int, int, int, int]]:
    """
    Находит все возможные ходы компьютера.

    :param board: Двумерный список, представляющий доску.
    :type board: List[List[str]]
    :return: Список кортежей (row, col, new_row, new_col) доступных ходов.
    :rtype: List[Tuple[int, int, int, int]]
    """
    moves = []
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == COMPUTER:
                for dr in [-1, 1]:
                    for dc in [-1, 1]:
                       new_row, new_col = row + dr , col + dc
                       if is_valid_move(board, row, col, new_row, new_col,COMPUTER):
                            moves.append((row, col, new_row, new_col))# Добавление допустимого хода в список
    return moves


def computer_turn(board: List[List[str]]) -> None:
    """
    Выполняет ход компьютера.

    :param board: Двумерный список, представляющий доску.
    :type board: List[List[str]]
    """
    possible_moves = get_computer_moves(board)
    if possible_moves:
        row, col, new_row, new_col = random.choice(possible_moves) # Выбор случайного хода
        update_board(board, row, col, new_row, new_col) # Обновление доски


def player_turn(board: List[List[str]]) -> None:
    """
    Запрашивает и выполняет ход игрока.

    :param board: Двумерный список, представляющий доску.
    :type board: List[List[str]]
    """
    while True:
        try:
            current_row = int(input("Введите строку текущей позиции (0-7): "))
            current_col = int(input("Введите столбец текущей позиции (0-7): "))
            new_row = int(input("Введите строку новой позиции (0-7): "))
            new_col = int(input("Введите столбец новой позиции (0-7): "))
            if is_valid_move(board, current_row, current_col, new_row, new_col, PLAYER):
                update_board(board, current_row, current_col, new_row, new_col) # Обновление доски, если ход допустим
                break
            else:
              print("Недопустимый ход, попробуйте еще раз.") # Сообщение о недопустимом ходе
        except ValueError as e:
            logger.error('Ошибка ввода. Пожалуйста, введите целые числа.', exc_info=e)  # Логирование ошибки ввода
            print("Ошибка ввода. Пожалуйста, введите целые числа.")


def play_checkers() -> None:
    """
    Основная функция игры в шашки.
    """
    board = initialize_board() # Инициализация доски
    draw_board(board)  # Отрисовка доски
    while True:
        player_turn(board) # Ход игрока
        if check_win(board, PLAYER):
            print("Поздравляю! Вы выиграли!") # Вывод сообщения о победе игрока
            break

        computer_turn(board) # Ход компьютера
        if check_win(board, COMPUTER):
            print("Компьютер выиграл!") # Вывод сообщения о победе компьютера
            break
        draw_board(board) # Отрисовка доски после каждого хода


if __name__ == "__main__":
    play_checkers() # Запуск игры
```