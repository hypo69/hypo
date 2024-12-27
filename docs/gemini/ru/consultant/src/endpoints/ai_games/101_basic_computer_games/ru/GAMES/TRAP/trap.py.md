# Анализ кода модуля `trap.py`

**Качество кода**
9
 -  Плюсы
        - Код хорошо структурирован и разбит на логические функции, что облегчает понимание и сопровождение.
        - Присутствуют подробные комментарии, описывающие назначение основных блоков кода и алгоритмов.
        - Код реализует базовую логику игры "Ловушка" в соответствии с описанием.
        - Использование константы `BOARD_SIZE` делает код более гибким и удобным для модификации размера поля.
        - Есть проверка на ввод некорректных данных и ходов игроков.

 -  Минусы
    - Отсутствует явная обработка исключений в функциях, кроме ввода, что может привести к неожиданным ошибкам и завершению программы.
    - Нет логирования ошибок.
    - Не используется `j_loads` или `j_loads_ns` для чтения данных.
    - Комментарии не в формате RST.
    - Некоторые функции можно упростить и сделать более читабельными.

**Рекомендации по улучшению**

1.  **Документация в формате RST**:
    - Переписать все комментарии в формате RST, включая docstrings для функций и модуля.
2.  **Импорты**:
    - Добавить импорт `logger` из `src.logger.logger`.
3.  **Обработка ошибок**:
    - Заменить стандартные блоки `try-except` на `logger.error` для логирования ошибок и возврата из функций в случае некорректных данных.
4.  **Улучшение читаемости**:
    - Разбить функцию `get_neighbors` на более мелкие функции для облегчения понимания логики.
    - Упростить логику `can_capture`, разделив проверки на отдельные этапы.
5.  **Общая структура**:
    - Переписать код с учетом новых требований по обработке ошибок, логирования, документации и форматирования кода.
6.  **Унификация**:
    - Убедиться, что все функции, переменные и импорты соответствуют стилю ранее обработанных файлов.
    - Удалить излишнее использование `copy`.

**Оптимизированный код**

```python
"""
Модуль для реализации игры "Ловушка".
====================================

Игра "Ловушка" - это игра для двух игроков на поле 7x7.
Цель игры - захватить как можно больше клеток противника.

Правила игры:
    1. Игроки по очереди ставят метки на пустые клетки.
    2. Когда клетка противника окружена метками текущего игрока, она захватывается.
    3. Игра заканчивается, когда все клетки заняты.
    4. Выигрывает игрок с наибольшим количеством захваченных клеток.

Пример использования:
--------------------

.. code-block:: python

   if __name__ == "__main__":
       play_trap_game()
"""
import copy
from src.logger.logger import logger  #  Импортируем logger

# Размер игрового поля
BOARD_SIZE = 7

def create_board() -> list[list[int]]:
    """
    Создает и возвращает пустое игровое поле.

    :return: Двумерный список, представляющий игровое поле, заполненный нулями.
    :rtype: list[list[int]]
    """
    # Создаем двумерный список, представляющий игровое поле, заполненный нулями (пустые клетки)
    return [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def display_board(board: list[list[int]]) -> None:
    """
    Выводит текущее состояние игрового поля в консоль.

    :param board: Игровое поле.
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
    :return: True, если координаты действительны, иначе False.
    :rtype: bool
    """
    # Проверяем, находятся ли координаты в допустимом диапазоне (от 0 до BOARD_SIZE - 1)
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE


def is_cell_empty(board: list[list[int]], row: int, col: int) -> bool:
    """
    Проверяет, является ли клетка пустой.

    :param board: Игровое поле.
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


def _get_neighbor_coordinates(row: int, col: int, dr: int, dc: int) -> tuple[int, int] | None:
    """
    Вспомогательная функция для получения координат соседней клетки.

    :param row: Номер строки.
    :type row: int
    :param col: Номер столбца.
    :type col: int
    :param dr: Изменение строки.
    :type dr: int
    :param dc: Изменение столбца.
    :type dc: int
    :return: Координаты соседней клетки или None, если они недействительны.
    :rtype: tuple[int, int] | None
    """
    new_row, new_col = row + dr, col + dc
    if is_valid_move(new_row, new_col):
        return new_row, new_col
    return None


def get_neighbors(row: int, col: int) -> list[tuple[int, int]]:
    """
    Возвращает список координат соседних клеток.

    :param row: Номер строки.
    :type row: int
    :param col: Номер столбца.
    :type col: int
    :return: Список координат соседних клеток.
    :rtype: list[tuple[int, int]]
    """
    # Возвращает список координат соседних клеток (сверху, снизу, слева, справа)
    neighbors = []
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        neighbor_coord = _get_neighbor_coordinates(row, col, dr, dc)
        if neighbor_coord:
           neighbors.append(neighbor_coord)
    return neighbors


def _is_opponent_cell(board: list[list[int]], row: int, col: int, current_player: int) -> bool:
    """
    Проверяет, является ли клетка клеткой противника.
    
    :param board: Игровое поле.
    :type board: list[list[int]]
    :param row: Номер строки.
    :type row: int
    :param col: Номер столбца.
    :type col: int
    :param current_player: Текущий игрок.
    :type current_player: int
    :return: True, если клетка принадлежит противнику, иначе False.
    :rtype: bool
    """
    opponent_player = 3 - current_player
    return board[row][col] == opponent_player

def _is_cell_surrounded(board: list[list[int]], row: int, col: int, current_player: int, neighbors: list[tuple[int, int]]) -> bool:
    """
    Проверяет, окружена ли клетка противника метками текущего игрока.

    :param board: Игровое поле.
    :type board: list[list[int]]
    :param row: Номер строки.
    :type row: int
    :param col: Номер столбца.
    :type col: int
    :param current_player: Текущий игрок.
    :type current_player: int
    :param neighbors: Список соседних клеток.
    :type neighbors: list[tuple[int, int]]
    :return: True, если клетка окружена, иначе False.
    :rtype: bool
    """
    if len(neighbors) < 4:
        return False
    for neighbor_row, neighbor_col in neighbors:
        if board[neighbor_row][neighbor_col] != current_player:
            return False
    return True

def can_capture(board: list[list[int]], row: int, col: int, current_player: int) -> bool:
    """
    Проверяет, может ли клетка противника быть захвачена.

    :param board: Игровое поле.
    :type board: list[list[int]]
    :param row: Номер строки.
    :type row: int
    :param col: Номер столбца.
    :type col: int
    :param current_player: Текущий игрок.
    :type current_player: int
    :return: True, если клетка может быть захвачена, иначе False.
    :rtype: bool
    """
    if not _is_opponent_cell(board, row, col, current_player):
        return False
    neighbors = get_neighbors(row, col)
    return _is_cell_surrounded(board, row, col, current_player, neighbors)


def capture_cell(board: list[list[int]], row: int, col: int, current_player: int) -> None:
    """
    Захватывает клетку противника.

    :param board: Игровое поле.
    :type board: list[list[int]]
    :param row: Номер строки.
    :type row: int
    :param col: Номер столбца.
    :type col: int
    :param current_player: Текущий игрок.
    :type current_player: int
    """
    # Меняем значение клетки на значение текущего игрока
    board[row][col] = current_player


def make_move(board: list[list[int]], row: int, col: int, current_player: int) -> None:
    """
    Выполняет ход игрока.

    :param board: Игровое поле.
    :type board: list[list[int]]
    :param row: Номер строки.
    :type row: int
    :param col: Номер столбца.
    :type col: int
    :param current_player: Текущий игрок.
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

    :param current_player: Текущий игрок.
    :type current_player: int
    :return: Номер следующего игрока.
    :rtype: int
    """
    # Переключаем игрока с 1 на 2 или с 2 на 1
    return 3 - current_player


def is_board_full(board: list[list[int]]) -> bool:
    """
    Проверяет, заполнено ли игровое поле.

    :param board: Игровое поле.
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

    :param board: Игровое поле.
    :type board: list[list[int]]
    :return: Кортеж с очками первого и второго игроков.
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
    Определяет победителя игры.

    :param player1_score: Очки первого игрока.
    :type player1_score: int
    :param player2_score: Очки второго игрока.
    :type player2_score: int
    :return: Сообщение о победителе.
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


def play_trap_game() -> None:
    """
    Основная функция для запуска игры "Ловушка".
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
            try:
                row = int(input(f"Игрок {current_player}, введите номер строки (0-{BOARD_SIZE - 1}): "))
                col = int(input(f"Игрок {current_player}, введите номер столбца (0-{BOARD_SIZE - 1}): "))
            except ValueError as ex:
                logger.error('Некорректный ввод. Пожалуйста, введите целые числа.', exc_info=ex)
                continue
            # Проверяем, находится ли введенные координаты в пределах игрового поля
            if not is_valid_move(row, col):
                print("Некорректный ход. Координаты выходят за пределы поля.")
                continue
            # Проверяем, является ли выбранная клетка пустой
            if not is_cell_empty(board, row, col):
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
"""
Объяснение кода:
1.  **Импорт модуля `copy` и `logger`**::
    - `import copy`:  Импортирует модуль `copy` для создания глубоких копий списков (игрового поля).
    - `from src.logger.logger import logger`: Импортирует логгер для обработки ошибок.
2.  **Константы**::
    - `BOARD_SIZE = 7`: Определяет размер игрового поля (7x7).
3.  **Функция `create_board()`**::
    -  Создает и возвращает пустое игровое поле в виде двумерного списка, заполненного нулями.
4.  **Функция `display_board(board)`**::
    -  Принимает игровое поле в качестве аргумента.
    -  Выводит текущее состояние игрового поля в консоль, используя символы '.' для пустых клеток, '1' для меток первого игрока и '2' для меток второго игрока.
5.  **Функция `is_valid_move(row, col)`**::
    -  Проверяет, находятся ли координаты (row, col) в пределах игрового поля.
    -  Возвращает `True`, если координаты действительны, иначе `False`.
6.  **Функция `is_cell_empty(board, row, col)`**::
    -  Проверяет, является ли клетка с координатами (row, col) пустой (равна 0).
    -  Возвращает `True`, если клетка пуста, иначе `False`.
7.  **Функция `_get_neighbor_coordinates(row, col, dr, dc)`**::
    -   Вспомогательная функция для вычисления координат соседней клетки.
    -   Возвращает координаты соседней клетки, если они в пределах игрового поля.
8.  **Функция `get_neighbors(row, col)`**::
    -  Возвращает список координат соседних клеток для заданной клетки (сверху, снизу, слева и справа).
    -  Исключает координаты, выходящие за границы игрового поля.
9.  **Функция `_is_opponent_cell(board, row, col, current_player)`**::
    -  Проверяет, принадлежит ли клетка противнику.
10. **Функция `_is_cell_surrounded(board, row, col, current_player, neighbors)`**::
    -  Проверяет, окружена ли клетка противника метками текущего игрока.
11. **Функция `can_capture(board, row, col, current_player)`**::
    -  Проверяет, может ли клетка противника (с координатами row, col) быть захвачена текущим игроком.
    -  Возвращает `True`, если клетка может быть захвачена, иначе `False`.
12. **Функция `capture_cell(board, row, col, current_player)`**::
    -  Захватывает клетку противника, изменяя её значение на значение текущего игрока.
13. **Функция `make_move(board, row, col, current_player)`**::
    -   Размещает метку текущего игрока на выбранной клетке.
    -   Проверяет и захватывает соседние клетки противника, если они могут быть захвачены.
14. **Функция `switch_player(current_player)`**::
    -  Меняет текущего игрока (с 1 на 2 или с 2 на 1).
15. **Функция `is_board_full(board)`**::
    -  Проверяет, заполнено ли все игровое поле.
    -  Возвращает `True`, если все клетки заняты, иначе `False`.
16. **Функция `calculate_scores(board)`**::
    -  Подсчитывает количество меток каждого игрока на игровом поле.
    -  Возвращает количество очков для каждого игрока.
17. **Функция `determine_winner(player1_score, player2_score)`**::
    -  Определяет победителя на основе подсчитанных очков.
    -  Возвращает сообщение о победителе или ничьей.
18. **Функция `play_trap_game()`**::
    -   Основная функция, управляющая ходом игры.
    -   Инициализирует игровое поле, текущего игрока, и запускает основной игровой цикл.
    -   Запрашивает ходы игроков, обрабатывает их, проверяет на корректность, захватывает клетки и переключает игроков.
    -   Выводит текущее состояние игрового поля и результаты игры.
19. **Запуск игры**::
    -  `if __name__ == "__main__":`: Этот блок гарантирует, что функция `play_trap_game()` будет запущена, только если файл исполняется напрямую, а не импортируется как модуль.
    -  `play_trap_game()`: Вызывает функцию для начала игры.
"""
```