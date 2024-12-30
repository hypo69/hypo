# Анализ кода модуля `salvo.py`

**Качество кода**
-  **Соответствие требованиям к формату кода (1-10):**

    -  **Преимущества:**
        -   Код в целом написан на чистом и понятном Python.
        -   Используются осмысленные имена переменных и функций.
        -   Присутствует подробное описание алгоритма игры и блок-схема.
        -   Есть docstring для функций, что делает код более понятным.
        -   Реализована базовая логика игры "Морской бой".

    -  **Недостатки:**
        -   Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson`.
        -   Отсутствуют импорты из `src.logger.logger`.
        -   Не хватает подробных комментариев в стиле reStructuredText (RST) для функций, методов и классов.
        -   Избыточное использование try-except.
        -   Смешаны стили комментариев (`#` и docstring).
        -   Отсутствует обработка ошибок в функциях `place_ships` и `is_sunk` в случае некорректных входных данных.
        -   Слишком упрощенный алгоритм размещения кораблей (нет проверок на соприкосновение кораблей).
        -   Не реализована функциональность для сохранения состояния игры и возобновления игры.
        -   Нет комментариев RST для всех переменных.

**Рекомендации по улучшению**
1.  **Импорт `j_loads` и `logger`:**
    -   Импортируйте `j_loads` или `j_loads_ns` из `src.utils.jjson` и `logger` из `src.logger.logger`.
    -   Удалите `import random`, добавьте псевдоним  `from random import randint, choice`.
2.  **Формат комментариев RST:**
    -   Перепишите все комментарии и docstring в формате RST.
    -   Добавьте подробные docstring для всех функций, классов, методов.
3.  **Обработка ошибок:**
    -   Замените `try-except` блоки на использование `logger.error` для записи ошибок.
    -   Добавьте проверки на корректность входных данных в функциях `place_ships` и `is_sunk` с выводом ошибок через `logger.error`.
4.  **Улучшенный алгоритм размещения кораблей:**
    -   Улучшите алгоритм размещения кораблей, чтобы они не перекрывались.
5.  **Более подробные комментарии:**
    -   Добавьте более подробные комментарии к каждой строке кода, объясняя ее назначение.
6. **Удаление лишних строк**
     - Удалите лишнюю пустую строку в начале файла.
     - Удалите блок-схему, она не нужна.
7. **Переименование переменных и функций**
     -  Переименуйте переменную `numberOfShots` в `shots_count`.
     -  Переименуйте переменную `sunk_ships_count` в `sunk_ships`.
     - Переименуйте функцию `is_sunk` в `check_sunk`.
     - Переименуйте функцию `play_salvo` в `run_game`.
     - Переименуйте переменную `x` в `row`.
     - Переименуйте переменную `y` в `col`.
8. **Удаление дублирования кода**
    - Перенесите код проверки и пометки попадания по кораблю в отдельную функцию `process_hit`.

**Улучшенный код**
```python
"""
Модуль для игры в "Морской бой"
=========================================================================================

Модуль реализует логику игры "Морской бой", где игрок пытается потопить корабли противника,
расположенные на сетке 10x10.

Принципы игры:
    - Игровое поле представлено в виде сетки 10x10.
    - Корабли противника размещаются случайным образом.
    - Игрок вводит координаты выстрела (строка и столбец).
    - Игра сообщает о результате выстрела: "MISS", "HIT" или "SINK".
    - Цель игры - потопить все корабли противника.

Пример использования
--------------------

.. code-block:: python

    from src.endpoints.ai_games.101_basic_computer_games.ru.GAMES.SALVO.salvo import run_game
    run_game()
"""
from src.logger.logger import logger  # Импорт логгера для записи ошибок
from random import randint, choice # Импорт функций randint и choice из модуля random


def create_board(size: int) -> list[list[int]]:
    """
    Создает игровое поле заданного размера.

    :param size: Размер игрового поля (сторона квадрата).
    :type size: int
    :return: Игровое поле, заполненное нулями.
    :rtype: list[list[int]]

    Пример использования:

    .. code-block:: python

        board = create_board(10)
        print(board)
        # Вывод: [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    """
    # Создание и возврат игрового поля, заполненного нулями.
    return [[0 for _ in range(size)] for _ in range(size)]


def place_ships(board: list[list[int]], ships_lengths: list[int]) -> list[tuple[int, int, str, int]]:
    """
    Размещает корабли на игровом поле.

    :param board: Игровое поле.
    :type board: list[list[int]]
    :param ships_lengths: Список длин кораблей.
    :type ships_lengths: list[int]
    :return: Список с данными о размещенных кораблях (строка, столбец, ориентация, длина).
    :rtype: list[tuple[int, int, str, int]]

    Пример использования:

    .. code-block:: python

        board = create_board(10)
        ships = place_ships(board, [2, 3, 4])
        print(ships)
        # Вывод: [(2, 2, 'horizontal', 2), (5, 0, 'vertical', 3), (1, 1, 'horizontal', 4)]
    """
    ships = [] # Инициализация списка для хранения данных о размещенных кораблях.
    for length in ships_lengths: #  Цикл по длинам кораблей.
        placed = False # Инициализация флага для контроля размещения корабля.
        while not placed: # Цикл пока корабль не будет успешно размещен.
            orientation = choice(['horizontal', 'vertical']) # Выбор случайного направления (горизонтальное или вертикальное) для размещения корабля.
            if orientation == 'horizontal': # Условие для размещения корабля горизонтально.
                row = randint(0, len(board) - 1) # Генерация случайной начальной строки.
                col = randint(0, len(board) - length) # Генерация случайного начального столбца.
                if all(board[row][col + i] == 0 for i in range(length)): # Проверка, что все клетки, необходимые для размещения корабля, свободны.
                    for i in range(length): # Цикл для размещения корабля на поле.
                         board[row][col + i] = 1 #  Размещение корабля на поле.
                    ships.append((row, col, orientation, length)) # Добавление данных о корабле в список.
                    placed = True # Установка флага, что корабль размещен.

            elif orientation == 'vertical': # Условие для размещения корабля вертикально.
                row = randint(0, len(board) - length) # Генерация случайной начальной строки.
                col = randint(0, len(board) - 1) # Генерация случайного начального столбца.
                if all(board[row + i][col] == 0 for i in range(length)): # Проверка, что все клетки, необходимые для размещения корабля, свободны.
                    for i in range(length): # Цикл для размещения корабля на поле.
                        board[row + i][col] = 1 # Размещение корабля на поле.
                    ships.append((row, col, orientation, length)) # Добавление данных о корабле в список.
                    placed = True # Установка флага, что корабль размещен.

    return ships # Возврат списка с данными о размещенных кораблях.


def check_sunk(board: list[list[str]], ship: tuple[int, int, str, int]) -> bool:
    """
    Проверяет, потоплен ли корабль.

    :param board: Игровое поле.
    :type board: list[list[str]]
    :param ship: Данные о корабле (строка, столбец, ориентация, длина).
    :type ship: tuple[int, int, str, int]
    :return: True, если корабль потоплен, иначе False.
    :rtype: bool

    Пример использования:

    .. code-block:: python

        board = [['hit', 0], ['hit', 0]]
        ship = (0, 0, 'horizontal', 2)
        is_sunk(board, ship) # True
    """
    row, col, orientation, length = ship # Распаковка данных о корабле.
    if orientation == 'horizontal': # Проверка ориентации корабля (горизонтальная).
      return all(board[row][col + i] == 'hit' for i in range(length)) #  Проверка, что все части корабля помечены как 'hit'.
    else: # Проверка ориентации корабля (вертикальная).
       return all(board[row + i][col] == 'hit' for i in range(length)) # Проверка, что все части корабля помечены как 'hit'.

def process_hit(board: list[list[str]], ships: list[tuple[int, int, str, int]], row: int, col: int, sunk_ships: int) -> tuple[bool, int]:
    """
    Обрабатывает попадание в корабль.

    :param board: Игровое поле.
    :type board: list[list[str]]
    :param ships: Список кораблей.
    :type ships: list[tuple[int, int, str, int]]
    :param row: Строка выстрела.
    :type row: int
    :param col: Столбец выстрела.
    :type col: int
    :param sunk_ships: Счетчик потопленных кораблей.
    :type sunk_ships: int
    :return: Кортеж из (потоплен ли корабль, обновленный счетчик потопленных кораблей)
    :rtype: tuple[bool, int]
    """
    board[row][col] = 'hit' # Помечает клетку как "hit".
    ship_sunk = False # Инициализация флага, что корабль не потоплен.
    for ship in ships: # Цикл по всем кораблям.
        if check_sunk(board, ship): # Проверка, потоплен ли корабль.
            print("SINK") # Вывод сообщения, что корабль потоплен.
            ship_sunk = True # Установка флага, что корабль потоплен.
            sunk_ships += 1 # Увеличение счетчика потопленных кораблей.
            ships.remove(ship) # Удаление потопленного корабля из списка.
            break # Выход из цикла.
    if not ship_sunk: # Если корабль не потоплен.
        print("HIT") # Вывод сообщения о попадании.
    return ship_sunk, sunk_ships # Возврат кортежа (потоплен ли корабль, обновленный счетчик потопленных кораблей)

def print_board(board: list[list[str]]) -> None:
    """
    Выводит игровое поле в консоль.

    :param board: Игровое поле.
    :type board: list[list[str]]
    :return: None
    :rtype: None

    Пример использования:

    .. code-block:: python

        board = [['~', 0], ['hit', 'miss']]
        print_board(board)
        # Вывод:
        #   0 1
        # 0 ~ 0
        # 1 hit miss
    """
    size = len(board) # Получение размера игрового поля.
    print("  " + " ".join(str(i) for i in range(size))) # Вывод номеров столбцов.
    for i, row in enumerate(board): # Цикл по строкам игрового поля.
        print(str(i) + " " + " ".join('~' if cell == 0 or cell == 1 else cell for cell in row)) # Вывод номера строки и ячеек игрового поля.

def run_game():
    """
    Основная функция игры Salvo.

    :return: None
    :rtype: None

    Пример использования:

    .. code-block:: python

        run_game()
    """
    board_size = 10 # Задание размера игрового поля.
    ships_lengths = [2, 3, 4, 5] # Задание длин кораблей.
    board = create_board(board_size) # Создание игрового поля.
    ships = place_ships(board, ships_lengths) # Размещение кораблей на поле.
    shots_count = 0 # Инициализация счетчика выстрелов.
    sunk_ships = 0 # Инициализация счетчика потопленных кораблей.
    print_board(board) # Вывод начального состояния игрового поля.

    while sunk_ships < len(ships): # Игровой цикл, пока не потоплены все корабли.
        try: # Обработка исключения при вводе некорректных данных.
            row = int(input("Введите координату X (0-9): ")) # Запрос координаты X.
            col = int(input("Введите координату Y (0-9): ")) # Запрос координаты Y.
            if not (0 <= row < board_size and 0 <= col < board_size): # Проверка, что координаты корректны.
                print("Неверные координаты. Попробуйте снова.") # Вывод сообщения об ошибке.
                continue # Переход к следующей итерации цикла.
        except ValueError as ex: # Обработка исключения ValueError.
            logger.error('Неверный ввод. Пожалуйста, введите числа от 0 до 9.', ex) # Запись ошибки в лог.
            continue  # Переход к следующей итерации цикла.

        shots_count += 1  # Увеличение счетчика выстрелов.
        if board[row][col] == 1: # Проверка, что выстрел попал в корабль.
           ship_sunk, sunk_ships = process_hit(board, ships, row, col, sunk_ships)
        elif board[row][col] == 0: # Проверка, что выстрел не попал в корабль.
            board[row][col] = 'miss' # Пометка ячейки как "miss".
            print("MISS") # Вывод сообщения о промахе.
        else: #  Проверка, что по этим координатам уже стреляли.
            print("Вы уже стреляли по этим координатам") # Вывод сообщения об этом.

        print_board(board)  # Вывод текущего состояния игрового поля.

    print(f"YOU SUNK ALL MY SHIPS IN {shots_count} SHOTS") # Вывод сообщения о победе и количестве выстрелов.


if __name__ == "__main__": # Проверка, что скрипт запущен как основной.
    run_game() # Запуск игры.
```