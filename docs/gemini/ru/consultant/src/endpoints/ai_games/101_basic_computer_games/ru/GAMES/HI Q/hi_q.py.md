# Анализ кода модуля hi_q.py

**Качество кода**
10
-  Плюсы
    - Код хорошо структурирован, разбит на логические функции, каждая из которых выполняет свою задачу.
    -  Используются понятные имена переменных и функций, что облегчает чтение и понимание кода.
    -  Реализация логики игры соответствует правилам головоломки HI Q.
    -  Ввод данных от пользователя обрабатывается с проверкой на корректность, что предотвращает ошибки.
    -  Код имеет подробное текстовое описание алгоритма, блок-схему и легенду, что способствует лучшему пониманию работы игры.
    -  Добавлены подробные комментарии к коду, которые описывают работу функций и блоков кода.
 -  Минусы
    - Отсутствует логирование ошибок.
    - Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson`, так как не происходит чтения файлов.
    -  Комментарии не в формате reStructuredText (RST).

**Рекомендации по улучшению**
1. **Логирование ошибок:**
   -  Добавить логирование ошибок с использованием `from src.logger.logger import logger`. Это позволит отслеживать ошибки во время выполнения кода.
2. **Формат документации:**
   -  Переписать комментарии в формате reStructuredText (RST) для соответствия стандартам документации.
3.  **Улучшение обработки ошибок:**
    -  Убрать избыточные блоки `try-except` и использовать `logger.error` для регистрации ошибок.
4. **Соответствие стандартам:**
   -  Привести в соответствие имена переменных и функций со стандартами проекта.

**Оптимизиробанный код**
```python
"""
Модуль реализует игру HI Q.
=========================================================================================

Игра HI Q представляет собой головоломку, в которой нужно удалить шарики с доски, перепрыгивая через них.
Цель игры - оставить на доске только один шарик. Игрок выбирает шарик и направление,
в котором он будет перепрыгивать. Игра заканчивается, когда больше нет возможных ходов или остался только один шарик.

Пример использования
--------------------

.. code-block:: python

    if __name__ == "__main__":
        play_hi_q()
"""
from src.logger.logger import logger # добавляем импорт для логирования

def init_board() -> list[list[int]]:
    """
    Инициализирует игровое поле с начальным расположением шариков.

    :return: Список списков, представляющий доску.
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

def print_board(board: list[list[int]]) -> None:
    """
    Выводит текущее состояние игрового поля на экран.

    :param board: Список списков, представляющий доску.
    """
    for row in board:
        print(' '.join(map(str, row)))

def get_move() -> tuple[int, int, str]:
    """
    Запрашивает у пользователя координаты шарика и направление хода.

    :return: Кортеж (row, col, direction), где direction: 'u', 'd', 'l', 'r'.
    """
    while True:
        try:
            row = int(input("Введите строку шарика (0-6): "))
            col = int(input("Введите столбец шарика (0-6): "))
            direction = input("Введите направление (u/d/l/r): ").lower()
            if 0 <= row <= 6 and 0 <= col <= 6 and direction in ['u', 'd', 'l', 'r']:
                return row, col, direction
            else:
                print("Неверный ввод. Попробуйте еще раз.")
        except ValueError as e: # обрабатываем ошибку ValueError
            logger.error(f"Неверный ввод: {e}") # логируем ошибку
            print("Неверный ввод. Попробуйте еще раз.")

def is_valid_move(board: list[list[int]], row: int, col: int, direction: str) -> bool:
    """
    Проверяет, является ли ход допустимым.

    :param board: Игровое поле.
    :param row: Строка выбранного шарика.
    :param col: Столбец выбранного шарика.
    :param direction: Направление хода ('u', 'd', 'l', 'r').
    :return: True, если ход допустим, иначе False.
    """
    if board[row][col] != 1: # Проверка, есть ли шарик в выбранной ячейке
        return False

    if direction == 'u':
        if row < 2 or board[row - 1][col] != 1 or board[row - 2][col] != 0:
            return False
    elif direction == 'd':
        if row > 4 or board[row + 1][col] != 1 or board[row + 2][col] != 0:
            return False
    elif direction == 'l':
        if col < 2 or board[row][col - 1] != 1 or board[row][col - 2] != 0:
             return False
    elif direction == 'r':
         if col > 4 or board[row][col + 1] != 1 or board[row][col + 2] != 0:
             return False

    return True

def make_move(board: list[list[int]], row: int, col: int, direction: str) -> list[list[int]]:
    """
    Выполняет ход, обновляя состояние игрового поля.

    :param board: Игровое поле.
    :param row: Строка выбранного шарика.
    :param col: Столбец выбранного шарика.
    :param direction: Направление хода ('u', 'd', 'l', 'r').
    :return: Обновленный board.
    """
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
    return board

def has_moves(board: list[list[int]]) -> bool:
    """
    Проверяет, есть ли еще возможные ходы.

    :param board: Игровое поле.
    :return: True, если есть возможные ходы, иначе False.
    """
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 1:
                if is_valid_move(board, row, col, 'u') or \
                   is_valid_move(board, row, col, 'd') or \
                   is_valid_move(board, row, col, 'l') or \
                   is_valid_move(board, row, col, 'r'):
                    return True
    return False

def count_pegs(board: list[list[int]]) -> int:
    """
    Считает количество шариков на доске.

    :param board: Игровое поле.
    :return: Количество шариков.
    """
    count = 0
    for row in board:
        count += row.count(1)
    return count

def play_hi_q() -> None:
    """
    Основная функция игры HI Q.

    Содержит игровой цикл, управление ходами и проверку на победу/проигрыш.
    """
    board = init_board() # инициализация доски
    while True: # игровой цикл
        print_board(board) # вывод текущего состояния доски
        row, col, direction = get_move() # запрос координат и направления
        if is_valid_move(board, row, col, direction): # проверка допустимости хода
            board = make_move(board, row, col, direction) # выполнение хода
            if count_pegs(board) == 1: # проверка остался ли один шарик
                print_board(board)
                print("Поздравляю! Вы выиграли!")
                break
            if not has_moves(board): # проверка наличия ходов
                print_board(board)
                print("Увы, ходов больше нет. Вы проиграли!")
                break
        else:
            print("Недопустимый ход. Попробуйте еще раз.")

if __name__ == "__main__":
    play_hi_q()
```
```
Объяснение кода:
1. **Модуль `hi_q.py`:**
   -   Модуль реализует игру HI Q, головоломку, в которой нужно удалить шарики с доски, перепрыгивая через них.
2. **Функция `init_board()`:**
   -   Инициализирует игровое поле (доску) как список списков (матрицу) и возвращает его.
   -   Игровое поле имеет размер 7x7, где `1` обозначает наличие шарика, а `0` - отсутствие.
   -   Начальное расположение шариков соответствует правилам игры HI Q.
3.  **Функция `print_board(board)`:**
    -   Принимает текущее состояние доски (`board`) в качестве аргумента.
    -   Выводит текущее состояние доски на экран, отображая `1` как шарики и `0` как пустые места.
4.  **Функция `get_move()`:**
    -   Запрашивает у пользователя координаты шарика (строка и столбец) и направление перемещения (`u` - вверх, `d` - вниз, `l` - влево, `r` - вправо).
    -   Использует цикл `while True` для повторного запроса ввода, если введенные данные некорректны.
    -   Добавлено логирование ошибки `ValueError`.
    -   Возвращает кортеж из строки, столбца и направления.
5.  **Функция `is_valid_move(board, row, col, direction)`:**
    -   Проверяет, является ли выбранный ход допустимым согласно правилам игры.
    -   Принимает игровое поле (`board`), строку, столбец и направление как аргументы.
    -   Проверяет, есть ли шарик в выбранной позиции.
    -   Проверяет, есть ли шарик для перепрыгивания и свободное место для приземления в выбранном направлении.
    -   Возвращает `True`, если ход допустим, и `False` в противном случае.
6.  **Функция `make_move(board, row, col, direction)`:**
    -   Выполняет ход, обновляя состояние игрового поля.
    -   Принимает игровое поле (`board`), строку, столбец и направление как аргументы.
    -   Удаляет перепрыгнутый шарик, перемещает выбранный шарик на новое место.
    -   Возвращает обновленное игровое поле.
7.  **Функция `has_moves(board)`:**
    -   Проверяет, есть ли еще возможные ходы на игровом поле.
    -   Проходит по всем ячейкам, проверяя, может ли шарик в данной ячейке совершить допустимый ход.
    -   Возвращает `True`, если есть хотя бы один возможный ход, иначе `False`.
8.  **Функция `count_pegs(board)`:**
    -   Считает количество шариков (единиц) на игровом поле.
    -   Проходит по всем строкам и подсчитывает общее количество `1`.
    -   Возвращает общее количество шариков на доске.
9.  **Функция `play_hi_q()`:**
    -   Содержит основной игровой цикл.
    -   Инициализирует доску, вызывает функции ввода хода, проверки допустимости хода, выполнения хода, и проверки на победу/проигрыш.
    -   Выводит сообщения о победе или поражении.
10. **Условие `if __name__ == "__main__":`:**
    -  Запускает функцию `play_hi_q()` только при непосредственном запуске скрипта.
```