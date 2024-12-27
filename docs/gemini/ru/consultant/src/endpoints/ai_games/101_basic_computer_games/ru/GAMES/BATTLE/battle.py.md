# Анализ кода модуля `battle.py`

**Качество кода**
7
-  Плюсы
    - Код хорошо структурирован и разбит на функции, что облегчает его понимание и поддержку.
    -  Используются константы для размера игрового поля, что делает код более гибким.
    -  Логика игры достаточно простая и понятная, что делает ее доступной для понимания.
    -  Есть базовая обработка ввода пользователя и проверка на корректность координат.
    -  Хорошая визуализация игрового поля в консоли.
 -  Минусы
    - Отсутствует reStructuredText (RST) документация для функций и модуля.
    - Отсутствует обработка ошибок с использованием `logger.error`.
    - Не используются `j_loads` или `j_loads_ns` для чтения файлов.
    -  Нет импорта `from src.logger.logger import logger`.
    -  В оригинальном коде нет определения победителя, игра заканчивается после 30 ходов, но в правилах игры есть условие, что игра заканчивается после того, как все корабли одного из игроков не будут потоплены.
    -  Размер и количество кораблей не указаны в правилах игры и в коде, также корабли размещаются размером 1 клетка.
    -  Корабли игрока не размещаются на игровом поле.
    -  Отсутствует проверка на повторный выстрел в одну и ту же клетку.
    -  Обработка исключений `ValueError` не логируется.

**Рекомендации по улучшению**
1.  Добавить reStructuredText (RST) документацию для функций и модуля.
2.  Импортировать и использовать `from src.logger.logger import logger` для логирования ошибок.
3.  Заменить `json.load` на `j_loads` или `j_loads_ns` при чтении файлов (если это необходимо).
4.  Избегать избыточного использования блоков `try-except` и заменить на `logger.error`.
5.  Реализовать полноценное размещение кораблей для игрока и компьютера.
6.  Добавить проверку на победителя игры (когда все корабли одного игрока потоплены).
7.  Добавить проверку на повторный выстрел в одну и ту же клетку.
8.  Логировать ошибки `ValueError` при некорректном вводе.
9.  Соблюдать единый стиль именования переменных и функций.

**Оптимизиробанный код**
```python
"""
Модуль для игры в морской бой
=========================================================================================

Этот модуль реализует простую игру "Морской бой" между игроком и компьютером.
Игроки по очереди стреляют по игровому полю противника, пытаясь потопить корабли.
Игра продолжается до тех пор, пока не будет достигнуто 30 ходов или один из игроков не проиграет.

Пример использования
--------------------

Запуск игры:

.. code-block:: python

    if __name__ == "__main__":
        play_battle()

"""
import random
from src.logger.logger import logger  #  Импорт logger

# Константа, задающая размер игрового поля
BOARD_SIZE = 10

def create_board(size: int) -> list[list[int]]:
    """
    Создает игровое поле (матрицу) заданного размера, заполненное нулями.

    :param size: Размер игрового поля (сторона квадрата).
    :return: Двумерный список (матрица), представляющий игровое поле.
    """
    return [[0 for _ in range(size)] for _ in range(size)]

def place_ships(board: list[list[int]], num_ships: int, ship_size: int = 1) -> None:
    """
    Размещает корабли заданного размера на игровом поле случайным образом.

    :param board: Игровое поле (матрица), на котором размещаются корабли.
    :param num_ships: Количество кораблей для размещения.
    :param ship_size: Размер корабля (по умолчанию 1).
    """
    ships_placed = 0
    while ships_placed < num_ships:
        row = random.randint(0, BOARD_SIZE - 1)
        col = random.randint(0, BOARD_SIZE - 1)
        if board[row][col] == 0:
            for i in range(ship_size):
                if row + i < BOARD_SIZE:
                    board[row + i][col] = 1  # 1 обозначает наличие корабля
            ships_placed += 1

def display_board(board: list[list[int]], is_computer: bool = False) -> None:
    """
    Отображает игровое поле в консоли, скрывая корабли компьютера.

    :param board: Игровое поле (матрица) для отображения.
    :param is_computer: Флаг, определяющий, нужно ли скрывать корабли компьютера (по умолчанию False).
    """
    print("   " + " ".join(str(i) for i in range(BOARD_SIZE)))
    for i, row in enumerate(board):
        row_str = " ".join(
            "*" if is_computer and cell == 1 else  # Скрываем корабли компьютера
            "O" if cell == 0 else  # Пустое поле
            "X" if cell == 2 else  # Попадание
            "-" if cell == 3 else # Промах
            str(cell)
            for cell in row
        )
        print(f"{i:2} {row_str}")
    print()

def play_battle() -> None:
    """
    Запускает игру "Морской бой".
    
    Игроки по очереди вводят координаты для выстрела, пытаясь потопить корабли противника.
    Игра продолжается до 30 ходов или пока не будут потоплены все корабли одного из игроков.
    """
    # Создаем игровые поля для игрока и компьютера
    player_board = create_board(BOARD_SIZE)
    computer_board = create_board(BOARD_SIZE)

    # Размещаем корабли на поле компьютера
    place_ships(computer_board, 5)
    place_ships(player_board, 5)  # Размещаем корабли на поле игрока

    # Инициализируем счетчик ходов
    turn_count = 0

    # Основной игровой цикл
    while turn_count < 30:
        turn_count += 1
        print(f"Ход {turn_count}")

        # Ход игрока
        while True:
            try:
                player_row = int(input(f"Введите строку для выстрела (0-{BOARD_SIZE - 1}): "))
                player_col = int(input(f"Введите столбец для выстрела (0-{BOARD_SIZE - 1}): "))
                if 0 <= player_row < BOARD_SIZE and 0 <= player_col < BOARD_SIZE:
                    if computer_board[player_row][player_col] in [2, 3]: # Проверка на повторный выстрел
                        print("Вы уже стреляли в эту клетку, попробуйте еще раз.")
                    else:
                        break
                else:
                    print("Некорректные координаты, попробуйте еще раз.")
            except ValueError as e:
                logger.error(f"Некорректный ввод: {e}") # Логируем ошибку ввода
                print("Некорректный ввод, введите число.")

        # Обрабатываем выстрел игрока
        if computer_board[player_row][player_col] == 1:
            computer_board[player_row][player_col] = 2  # 2 = Попадание
            print("HIT!")
        else:
            computer_board[player_row][player_col] = 3  # 3 = промах
            print("MISS!")

        # Выводим игровое поле игрока после выстрела, показывая результаты выстрела
        print("Ваше поле:")
        display_board(player_board)

        # Проверяем, все ли корабли компьютера потоплены
        if all(cell != 1 for row in computer_board for cell in row):
           print("Вы победили! Все корабли компьютера потоплены.")
           break

        # Ход компьютера
        print("Ход компьютера...")
        while True:
            computer_row = random.randint(0, BOARD_SIZE - 1)
            computer_col = random.randint(0, BOARD_SIZE - 1)
            if player_board[computer_row][computer_col] not in [2, 3]: # Проверка на повторный выстрел
                break

        # Обрабатываем выстрел компьютера
        if player_board[computer_row][computer_col] == 1:
            player_board[computer_row][computer_col] = 2  # 2 = Попадание
            print("COMPUTER HITS!")
        else:
            player_board[computer_row][computer_col] = 3  # 3 = промах
            print("COMPUTER MISSES")

        # Выводим игровое поле игрока после выстрела компьютера
        print("Ваше поле:")
        display_board(player_board)
         # Проверяем, все ли корабли игрока потоплены
        if all(cell != 1 for row in player_board for cell in row):
           print("Компьютер победил! Все ваши корабли потоплены.")
           break
    # Сообщение об окончании игры
    print("END OF GAME")

# Запускаем игру, если скрипт запущен напрямую
if __name__ == "__main__":
    play_battle()
```