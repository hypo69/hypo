# Анализ кода модуля `trap.py`

**Качество кода: 7/10**
 -  Плюсы
    -   Код хорошо структурирован и разбит на логические функции, что облегчает его понимание и поддержку.
    -   Присутствует подробная документация в виде многострочных комментариев, описывающих алгоритм игры, блок-схему и назначение каждой функции.
    -   Используются константы для определения размера игрового поля, что улучшает читаемость и облегчает модификацию размера поля.
    -   Логика игры реализована корректно, включая проверку ходов, захват клеток и подсчет очков.
 -  Минусы
    -  Отсутствуют необходимые импорты `src.utils.jjson`, `src.logger.logger`, хотя в инструкции они были указаны.
    -  В коде используются стандартные блоки `try-except`, которые лучше заменить на использование `logger.error` для обработки исключений.
    -  Комментарии не в формате reStructuredText (RST) как указано в инструкции.
    -  Некоторые переменные могут быть переименованы для большей ясности.

**Рекомендации по улучшению**
1.  Добавить импорты `j_loads_ns` и `logger`.
2.  Переписать все комментарии в формате RST.
3.  Заменить стандартные блоки `try-except` на обработку ошибок с помощью `logger.error`.
4.  Добавить docstring к каждой функции.
5.  Добавить проверку на ввод координат, если пользователь введет не целое число, и перенести эту проверку в отдельную функцию.
6.  Переименовать некоторые переменные для большей ясности.
7.  Изменить `print` для вывода состояния игрового поля на использование `logger.info`.
8.  Вынести логику ввода в отдельную функцию для удобства.

**Оптимизированный код**
```python
"""
Модуль для реализации игры "Ловушка".
=========================================================================================

Игра "Ловушка" - это игра для двух игроков, в которой каждый игрок по очереди ставит свои метки (цифры 1 и 2) на игровом поле.
Цель игры - окружить клетку противника своими клетками. Если игрок окружает клетку противника со всех сторон,
клетка противника захватывается.

Правила игры:
    1. Игровое поле - это квадратная сетка 7х7.
    2. Два игрока по очереди вводят координаты клетки для размещения своей метки (1 или 2).
    3. Если клетка окружена с четырех сторон метками противника, то метка захватывается и заменяется меткой захватившего игрока.
    4. Игра заканчивается, когда все клетки заняты. Выигрывает тот игрок, у кого больше меток на поле.

Пример использования
--------------------
    Пример запуска игры "Ловушка":

    .. code-block:: python

        if __name__ == "__main__":
            play_trap_game()

"""
import copy
from src.logger.logger import logger  # импортируем logger
# from src.utils.jjson import j_loads_ns # Не используется в коде

# Размер игрового поля
BOARD_SIZE = 7

def create_board() -> list[list[int]]:
    """
    Создает и возвращает пустое игровое поле.

    :return: Двумерный список, представляющий игровое поле, заполненный нулями (пустые клетки).
    :rtype: list[list[int]]
    """
    # Создаем двумерный список, представляющий игровое поле, заполненный нулями (пустые клетки)
    return [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def display_board(board: list[list[int]]) -> None:
    """
    Отображает текущее состояние игрового поля.

    :param board: Двумерный список, представляющий игровое поле.
    :type board: list[list[int]]
    """
    # Выводим номера колонок
    print("  ", end="")
    for col in range(BOARD_SIZE):
        print(f"{col} ", end="")
    print()
    # Для каждой строки игрового поля
    for row in range(BOARD_SIZE):
        # Выводим номер строки
        print(f"{row} ", end="")
        # Для каждой клетки в текущей строке
        for col in range(BOARD_SIZE):
             # Выводим содержимое клетки, заменяя 0 на '.', 1 на '1', 2 на '2'
            print(f"{\'.\' if board[row][col] == 0 else str(board[row][col])} ", end="")
        # Переход на новую строку
        print()

def is_valid_move(row: int, col: int) -> bool:
    """
    Проверяет, находятся ли координаты в пределах игрового поля.

    :param row: Номер строки.
    :type row: int
    :param col: Номер столбца.
    :type col: int
    :return: True, если координаты валидны, иначе False.
    :rtype: bool
    """
    # Проверяем, находятся ли координаты в допустимом диапазоне (от 0 до BOARD_SIZE - 1)
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE

def is_cell_empty(board: list[list[int]], row: int, col: int) -> bool:
    """
    Проверяет, является ли клетка пустой.

    :param board: Двумерный список, представляющий игровое поле.
    :type board: list[list[int]]
    :param row: Номер строки.
    :type row: int
    :param col: Номер столбца.
    :type col: int
    :return: True, если клетка пуста, иначе False.
    :rtype: bool
    """
    # Возвращаем True, если клетка пуста (значение 0), иначе False
    return board[row][col] == 0

def get_neighbors(row: int, col: int) -> list[tuple[int, int]]:
    """
    Возвращает список координат соседних клеток.

    :param row: Номер строки.
    :type row: int
    :param col: Номер столбца.
    :type col: int
    :return: Список координат соседних клеток (сверху, снизу, слева, справа).
    :rtype: list[tuple[int, int]]
    """
    # Возвращает список координат соседних клеток (сверху, снизу, слева, справа)
    neighbors = []
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = row + dr, col + dc
        if is_valid_move(new_row, new_col):
            neighbors.append((new_row, new_col))
    return neighbors

def can_capture(board: list[list[int]], row: int, col: int, current_player: int) -> bool:
    """
    Проверяет, может ли клетка противника быть захвачена.

    :param board: Двумерный список, представляющий игровое поле.
    :type board: list[list[int]]
    :param row: Номер строки проверяемой клетки.
    :type row: int
    :param col: Номер столбца проверяемой клетки.
    :type col: int
    :param current_player: Номер текущего игрока.
    :type current_player: int
    :return: True, если клетка может быть захвачена, иначе False.
    :rtype: bool
    """
    # Получаем номер противника (если текущий игрок 1, то противник 2, и наоборот)
    opponent_player = 3 - current_player
    # Если клетка не принадлежит противнику, то она не может быть захвачена
    if board[row][col] != opponent_player:
        return False
    # Получаем соседние клетки
    neighbors = get_neighbors(row, col)
    # Проверяем, окружена ли клетка противника клетками текущего игрока
    # Если соседних клеток меньше 4, то клетка не может быть захвачена
    if len(neighbors) < 4:
        return False
    # Проверяем, являются ли все соседние клетки метками текущего игрока
    for neighbor_row, neighbor_col in neighbors:
        if board[neighbor_row][neighbor_col] != current_player:
            return False
    # Если все проверки пройдены, клетка может быть захвачена
    return True

def capture_cell(board: list[list[int]], row: int, col: int, current_player: int) -> None:
    """
    Захватывает клетку противника.

    :param board: Двумерный список, представляющий игровое поле.
    :type board: list[list[int]]
    :param row: Номер строки захватываемой клетки.
    :type row: int
    :param col: Номер столбца захватываемой клетки.
    :type col: int
    :param current_player: Номер текущего игрока.
    :type current_player: int
    """
    # Меняем значение клетки на значение текущего игрока
    board[row][col] = current_player

def make_move(board: list[list[int]], row: int, col: int, current_player: int) -> None:
    """
    Выполняет ход игрока.

    :param board: Двумерный список, представляющий игровое поле.
    :type board: list[list[int]]
    :param row: Номер строки, куда игрок ставит метку.
    :type row: int
    :param col: Номер столбца, куда игрок ставит метку.
    :type col: int
    :param current_player: Номер текущего игрока.
    :type current_player: int
    """
    # Размещаем метку текущего игрока на выбранной клетке
    board[row][col] = current_player
    # Получаем список соседних клеток
    neighbors = get_neighbors(row, col)
    # Проверяем, может ли клетка противника быть захвачена
    for neighbor_row, neighbor_col in neighbors:
       # Если соседняя клетка может быть захвачена
       if can_capture(board, neighbor_row, neighbor_col, current_player):
            # Захватываем клетку
           capture_cell(board, neighbor_row, neighbor_col, current_player)

def switch_player(current_player: int) -> int:
    """
    Переключает текущего игрока.

    :param current_player: Номер текущего игрока.
    :type current_player: int
    :return: Номер следующего игрока.
    :rtype: int
    """
    # Переключаем игрока с 1 на 2 или с 2 на 1
    return 3 - current_player

def is_board_full(board: list[list[int]]) -> bool:
    """
    Проверяет, заполнено ли игровое поле.

    :param board: Двумерный список, представляющий игровое поле.
    :type board: list[list[int]]
    :return: True, если все клетки заполнены, иначе False.
    :rtype: bool
    """
    # Проходим по каждой клетке на поле
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            # Если клетка пуста (значение 0), возвращаем False (поле не заполнено)
            if board[row][col] == 0:
                return False
    # Если все клетки заполнены, возвращаем True
    return True

def calculate_scores(board: list[list[int]]) -> tuple[int, int]:
    """
    Подсчитывает очки каждого игрока.

    :param board: Двумерный список, представляющий игровое поле.
    :type board: list[list[int]]
    :return: Кортеж с количеством очков первого и второго игроков.
    :rtype: tuple[int, int]
    """
    # Инициализируем счетчики для каждого игрока
    player1_score = 0
    player2_score = 0
    # Проходим по каждой клетке на поле
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            # Если в клетке метка первого игрока, увеличиваем его счетчик
            if board[row][col] == 1:
                player1_score += 1
            # Если в клетке метка второго игрока, увеличиваем его счетчик
            elif board[row][col] == 2:
                player2_score += 1
    # Возвращаем счетчики игроков
    return player1_score, player2_score

def determine_winner(player1_score: int, player2_score: int) -> str:
    """
    Определяет победителя на основе набранных очков.

    :param player1_score: Количество очков первого игрока.
    :type player1_score: int
    :param player2_score: Количество очков второго игрока.
    :type player2_score: int
    :return: Сообщение о победителе или ничьей.
    :rtype: str
    """
    # Если у первого игрока больше очков, объявляем его победителем
    if player1_score > player2_score:
        return "Победил игрок 1!"
    # Если у второго игрока больше очков, объявляем его победителем
    elif player2_score > player1_score:
        return "Победил игрок 2!"
    # Если количество очков одинаковое, объявляем ничью
    else:
        return "Ничья!"

def get_player_move(current_player: int) -> tuple[int, int]:
    """
    Запрашивает ввод координат у текущего игрока.

    :param current_player: Номер текущего игрока.
    :type current_player: int
    :return: Кортеж с координатами (строка, столбец).
    :rtype: tuple[int, int]
    """
    while True:
        try:
            row = int(input(f"Игрок {current_player}, введите номер строки (0-{BOARD_SIZE - 1}): "))
            col = int(input(f"Игрок {current_player}, введите номер столбца (0-{BOARD_SIZE - 1}): "))
            return row, col
        except ValueError:
            logger.error("Некорректный ввод. Пожалуйста, введите целые числа.")
            print("Некорректный ввод. Пожалуйста, введите целые числа.")  # Сообщение для пользователя

def play_trap_game() -> None:
    """
    Основная функция, управляющая ходом игры.
    """
    # Создаем новое игровое поле
    board = create_board()
    # Устанавливаем первого игрока
    current_player = 1
    # Начинаем игровой цикл
    while not is_board_full(board):
        # Выводим текущее состояние игрового поля
        display_board(board)
        # Запрашиваем координаты хода у текущего игрока
        while True:
            row, col = get_player_move(current_player)
            # Проверяем, находится ли введенные координаты в пределах игрового поля
            if not is_valid_move(row, col):
                logger.error("Некорректный ход. Координаты выходят за пределы поля.")
                print("Некорректный ход. Координаты выходят за пределы поля.")
                continue
            # Проверяем, является ли выбранная клетка пустой
            if not is_cell_empty(board, row, col):
                logger.error("Некорректный ход. Клетка уже занята.")
                print("Некорректный ход. Клетка уже занята.")
                continue
            # Если все проверки пройдены, выходим из внутреннего цикла
            break
        # Выполняем ход игрока
        make_move(board, row, col, current_player)
        # Переключаем текущего игрока
        current_player = switch_player(current_player)

    # Выводим финальное состояние игрового поля
    display_board(board)
    # Подсчитываем количество очков каждого игрока
    player1_score, player2_score = calculate_scores(board)
    # Определяем победителя
    winner = determine_winner(player1_score, player2_score)
    # Выводим результат игры
    print(f"Игрок 1: {player1_score} очков")
    print(f"Игрок 2: {player2_score} очков")
    print(winner)

# Запускаем игру
if __name__ == "__main__":
    play_trap_game()
```