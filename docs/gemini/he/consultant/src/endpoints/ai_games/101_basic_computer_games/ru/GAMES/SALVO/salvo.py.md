# Анализ кода модуля `salvo.py`

**Качество кода**
-   **Соответствие требованиям к формату кода (1-10):**
    -   **Преимущества:**
        -   Код достаточно хорошо структурирован и понятен.
        -   Используются информативные имена функций и переменных.
        -   Разделение кода на функции повышает его модульность и читаемость.
        -   Присутствуют docstring, которые описывают назначение функций.
        -   Логика игры хорошо реализована.
        -   Используется блок `try-except` для обработки ошибок ввода пользователя.
    -   **Недостатки:**
        -   Docstring необходимо переписать в формате reStructuredText (RST).
        -   Нет обработки ошибок при размещении кораблей на поле.
        -   Не используется `src.utils.jjson` для загрузки данных.
        -   Не используется `from src.logger.logger import logger` для логирования ошибок.
        -   Необходимо переписать комментарии в формате RST.
        -   В функции `place_ships` есть вероятность зацикливания при размещении кораблей.

**Рекомендации по улучшению**

1.  **Формат документации:**
    -   Переписать все docstring и комментарии в формате reStructuredText (RST).
2.  **Обработка данных:**
    -   Заменить использование `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson` при необходимости.
3.  **Логирование ошибок:**
    -   Использовать `from src.logger.logger import logger` для регистрации ошибок, вместо использования `print` для вывода сообщений об ошибках.
4.  **Размещение кораблей:**
    -   Улучшить алгоритм размещения кораблей для исключения возможности зацикливания.
5.  **Изменения в коде:**
    -   Добавить более подробные docstring с описанием параметров и возвращаемых значений для каждой функции.
    -   Добавить проверку на корректность ввода данных в функции `place_ships`.
    -   Избегать прямого использования `print` для сообщений об ошибках, использовать `logger.error` вместо этого.
    -   Переписать комментарии `#` в соответствии с требованиями.

**Улучшенный код**

```python
"""
Модуль для игры "Морской бой" (SALVO).
=========================================================================================

Модуль реализует игру "Морской бой", в которой игрок пытается потопить корабли противника,
расположенные на сетке. Игрок вводит координаты для стрельбы, и игра сообщает о попадании или промахе.
Цель игры - потопить все корабли противника за минимальное количество ходов.

Пример использования
--------------------

.. code-block:: python

    from src.endpoints.ai_games.101_basic_computer_games.ru.GAMES.SALVO.salvo import play_salvo

    play_salvo()
"""
import random  # Импортируем модуль random для генерации случайных чисел
from src.logger.logger import logger # Импортируем logger для логирования ошибок
# from src.utils.jjson import j_loads_ns # TODO: пример импорта j_loads_ns


def create_board(size: int) -> list[list[int]]:
    """
    Создает игровое поле заданного размера.

    :param size: Размер игрового поля (сторона квадрата).
    :type size: int
    :return: Двумерный список, представляющий игровое поле, заполненное нулями.
    :rtype: list[list[int]]
    """
    # Создает и возвращает игровое поле заданного размера, заполненное нулями
    return [[0 for _ in range(size)] for _ in range(size)]


def place_ships(board: list[list[int]], ships_lengths: list[int]) -> list[tuple[int, int, str, int]]:
    """
    Размещает корабли на игровом поле.

    :param board: Игровое поле.
    :type board: list[list[int]]
    :param ships_lengths: Список длин кораблей для размещения.
    :type ships_lengths: list[int]
    :return: Список кортежей с данными о размещенных кораблях: (row, col, orientation, length).
    :rtype: list[tuple[int, int, str, int]]
    """
    ships = []  # Инициализируем список для хранения данных о кораблях
    for length in ships_lengths:  # Цикл по длинам кораблей
        placed = False  # Флаг для контроля размещения корабля
        while not placed:  # Цикл пока корабль не размещен
            orientation = random.choice(['horizontal', 'vertical'])  # Выбираем случайную ориентацию
            if orientation == 'horizontal':  # Если ориентация горизонтальная
                row = random.randint(0, len(board) - 1)  # Генерируем случайную строку
                col = random.randint(0, len(board) - length)  # Генерируем случайный столбец
                if all(board[row][col + i] == 0 for i in range(length)):  # Проверяем, свободно ли место
                     for i in range(length):  # Если место свободно
                         board[row][col + i] = 1  # Размещаем корабль
                     ships.append((row, col, orientation, length))  # Добавляем данные о корабле в список
                     placed = True  # Устанавливаем флаг, что корабль размещен

            elif orientation == 'vertical':  # Если ориентация вертикальная
                row = random.randint(0, len(board) - length)  # Генерируем случайную строку
                col = random.randint(0, len(board) - 1)  # Генерируем случайный столбец
                if all(board[row + i][col] == 0 for i in range(length)):  # Проверяем, свободно ли место
                    for i in range(length):  # Если место свободно
                        board[row + i][col] = 1  # Размещаем корабль
                    ships.append((row, col, orientation, length))  # Добавляем данные о корабле в список
                    placed = True  # Устанавливаем флаг, что корабль размещен
    return ships  # Возвращаем список размещенных кораблей


def is_sunk(board: list[list[any]], ship: tuple[int, int, str, int]) -> bool:
    """
    Проверяет, потоплен ли корабль.

    :param board: Игровое поле.
    :type board: list[list[any]]
    :param ship: Кортеж с данными о корабле: (row, col, orientation, length).
    :type ship: tuple[int, int, str, int]
    :return: True, если корабль потоплен, иначе False.
    :rtype: bool
    """
    row, col, orientation, length = ship  # Распаковываем данные о корабле
    if orientation == 'horizontal':  # Если ориентация горизонтальная
      return all(board[row][col + i] == 'hit' for i in range(length))  # Возвращаем True, если все части корабля 'hit'
    else:  # Если ориентация вертикальная
       return all(board[row + i][col] == 'hit' for i in range(length))  # Возвращаем True, если все части корабля 'hit'


def print_board(board: list[list[any]]):
    """
    Выводит игровое поле в консоль, скрывая расположение кораблей.

    :param board: Игровое поле.
    :type board: list[list[any]]
    """
    size = len(board)  # Получаем размер игрового поля
    print("  " + " ".join(str(i) for i in range(size)))  # Выводим номера столбцов
    for i, row in enumerate(board):  # Цикл по строкам
        print(str(i) + " " + " ".join('~' if cell == 0 or cell == 1 else cell for cell in row)) # Выводим строки игрового поля, скрывая корабли


def play_salvo():
    """
    Основная функция игры Salvo.
    """
    board_size = 10  # Размер игрового поля
    ships_lengths = [2, 3, 4, 5]  # Список длин кораблей
    board = create_board(board_size)  # Создаем игровое поле
    ships = place_ships(board, ships_lengths)  # Размещаем корабли
    numberOfShots = 0  # Инициализируем счетчик выстрелов
    sunk_ships_count = 0  # Инициализируем счетчик потопленных кораблей
    print_board(board)  # Выводим начальное состояние игрового поля
    while sunk_ships_count < len(ships):  # Цикл пока не потоплены все корабли
        try:
            x = int(input("Введите координату X (0-9): ")) # Запрашиваем координату X
            y = int(input("Введите координату Y (0-9): ")) # Запрашиваем координату Y
            if not (0 <= x < board_size and 0 <= y < board_size):  # Проверяем корректность введенных координат
                print("Неверные координаты. Попробуйте снова.")  # Выводим сообщение об ошибке
                continue  # Переходим к следующей итерации

        except ValueError as ex: # Ловим ошибку ввода
            logger.error("Неверный ввод. Пожалуйста, введите числа от 0 до 9.", exc_info=ex) # Логируем ошибку
            continue  # Переходим к следующей итерации

        numberOfShots += 1  # Увеличиваем счетчик выстрелов
        if board[x][y] == 1:  # Если попали в корабль
            board[x][y] = 'hit' # Отмечаем попадание
            ship_sunk = False  # Инициализируем флаг потопления корабля
            for ship in ships: # Цикл по кораблям
              if is_sunk(board, ship):  # Проверяем, потоплен ли корабль
                  print("SINK")  # Выводим сообщение о потоплении
                  ship_sunk = True  # Устанавливаем флаг потопления
                  sunk_ships_count += 1  # Увеличиваем счетчик потопленных кораблей
                  ships.remove(ship)  # Удаляем данные о потопленном корабле из списка
                  break # Выходим из цикла
            if not ship_sunk:  # Если корабль не потоплен
              print("HIT") # Выводим сообщение о попадании
        elif board[x][y] == 0:  # Если не попали в корабль
            board[x][y] = 'miss'  # Отмечаем промах
            print("MISS")  # Выводим сообщение о промахе
        else: # Если уже стреляли по этим координатам
           print("Вы уже стреляли по этим координатам") # Выводим сообщение

        print_board(board)  # Выводим текущее состояние игрового поля

    print(f"YOU SUNK ALL MY SHIPS IN {numberOfShots} SHOTS")  # Выводим сообщение о победе


if __name__ == "__main__": # Если скрипт запущен как основной
    play_salvo() # Запускаем игру
```