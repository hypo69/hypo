# Анализ кода модуля trap.py

**Качество кода**
 - **Соблюдение требований к формату кода с 1 до 10:**
   - 1. **Формат документирования:** Используется docstring в начале файла, а также для функций, но не в формате RST. Необходимо переписать в RST.
   - 2. **Сохранение комментариев:** Сохраняются все комментарии `#`, это хорошо.
   - 3. **Обработка данных:** Не используется `j_loads` или `j_loads_ns`, но это и не требуется в данном коде.
   - 4. **Анализ структуры:** Импорты присутствуют, но нет импорта `logger` для логирования.
   - 5. **Рефакторинг и улучшение:** Отсутствует docstring в формате RST, отсутствует использование `logger`.
   - 6. **Тесты:** Нет тестов.
   - 7. **Финальный код:** Код представлен в полном объеме, но необходимо добавить изменения согласно рекомендациям.
   - 8. **Примеры кода:** Примеры docstring в формате RST отсутствуют.
   - 9. **Дополнительные инструкции:** Необходимо переписать docstring в RST.

 - **Преимущества:**
    - Код хорошо структурирован и разбит на логические функции.
    - Легко читаемый код с подробными комментариями.
    - Реализация логики игры "Ловушка" довольно понятная.
 - **Недостатки:**
    - Отсутствует документирование в формате reStructuredText (RST).
    - Не используется логгер для записи ошибок.
    - Чрезмерное использование `try-except` в `play_trap_game`.

**Рекомендации по улучшению**
1.  **Переписать docstring в RST**: Переписать все docstring в соответствии с форматом reStructuredText.
2.  **Использовать logger**: Добавить логирование ошибок с помощью `src.logger.logger.error`.
3.  **Удалить избыточный try-except**: Упростить обработку ошибок в `play_trap_game`, используя `logger.error` вместо `try-except`.
4. **Добавить импорт logger**:  Добавить `from src.logger.logger import logger` для логирования ошибок.
5. **Добавить примеры docstring в формате RST**: Включать в документацию примеры использования функций и классов с использованием reStructuredText.

**Улучшенный код**
```python
"""
Модуль для реализации игры "Ловушка"
====================================

Модуль предоставляет функции для создания, отображения и управления игровым процессом в игре "Ловушка".
Игра представляет собой стратегическую игру для двух игроков, цель которой - захватить как можно больше клеток противника.

Пример использования
--------------------

.. code-block:: python

    from trap import play_trap_game

    if __name__ == "__main__":
        play_trap_game()
"""
import copy # Импортирует модуль copy для создания глубоких копий списков
from src.logger.logger import logger  # Импортирует логгер для записи ошибок

# Размер игрового поля
BOARD_SIZE = 7

def create_board() -> list[list[int]]:
    """
    Создает пустое игровое поле.

    :return: Двумерный список, представляющий игровое поле, заполненный нулями.
    :rtype: list[list[int]]
    """
    return [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)] # Создаем двумерный список, представляющий игровое поле, заполненный нулями (пустые клетки)

def display_board(board: list[list[int]]):
    """
    Отображает текущее состояние игрового поля.

    :param board: Двумерный список, представляющий игровое поле.
    :type board: list[list[int]]
    """
    print("  ", end="") # Выводим номера колонок
    for col in range(BOARD_SIZE):
        print(f"{col} ", end="")
    print()
    for row in range(BOARD_SIZE): # Для каждой строки игрового поля
        print(f"{row} ", end="") # Выводим номер строки
        for col in range(BOARD_SIZE): # Для каждой клетки в текущей строке
            print(f"{\'.\' if board[row][col] == 0 else str(board[row][col])} ", end="") # Выводим содержимое клетки, заменяя 0 на '.', 1 на '1', 2 на '2'
        print() # Переход на новую строку

def is_valid_move(row: int, col: int) -> bool:
    """
    Проверяет, находится ли координата в пределах игрового поля.

    :param row: Номер строки.
    :type row: int
    :param col: Номер столбца.
    :type col: int
    :return: True, если координаты действительны, иначе False.
    :rtype: bool
    """
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE # Проверяем, находятся ли координаты в допустимом диапазоне (от 0 до BOARD_SIZE - 1)

def is_cell_empty(board: list[list[int]], row: int, col: int) -> bool:
    """
    Проверяет, является ли клетка пустой.

    :param board: Двумерный список, представляющий игровое поле.
    :type board: list[list[int]]
    :param row: Номер строки.
    :type row: int
    :param col: Номер столбца.
    :type col: int
    :return: True, если клетка пуста (значение 0), иначе False.
    :rtype: bool
    """
    return board[row][col] == 0 # Возвращаем True, если клетка пуста (значение 0), иначе False

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
    neighbors = [] # Возвращает список координат соседних клеток (сверху, снизу, слева, справа)
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
    :param row: Номер строки клетки противника.
    :type row: int
    :param col: Номер столбца клетки противника.
    :type col: int
    :param current_player: Номер текущего игрока.
    :type current_player: int
    :return: True, если клетка может быть захвачена, иначе False.
    :rtype: bool
    """
    opponent_player = 3 - current_player # Получаем номер противника (если текущий игрок 1, то противник 2, и наоборот)
    if board[row][col] != opponent_player: # Если клетка не принадлежит противнику, то она не может быть захвачена
        return False
    neighbors = get_neighbors(row, col) # Получаем соседние клетки
    if len(neighbors) < 4: # Если соседних клеток меньше 4, то клетка не может быть захвачена
        return False
    for neighbor_row, neighbor_col in neighbors: # Проверяем, являются ли все соседние клетки метками текущего игрока
        if board[neighbor_row][neighbor_col] != current_player:
            return False
    return True # Если все проверки пройдены, клетка может быть захвачена

def capture_cell(board: list[list[int]], row: int, col: int, current_player: int):
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
    board[row][col] = current_player # Меняем значение клетки на значение текущего игрока

def make_move(board: list[list[int]], row: int, col: int, current_player: int):
    """
    Выполняет ход игрока.

    :param board: Двумерный список, представляющий игровое поле.
    :type board: list[list[int]]
    :param row: Номер строки хода.
    :type row: int
    :param col: Номер столбца хода.
    :type col: int
    :param current_player: Номер текущего игрока.
    :type current_player: int
    """
    board[row][col] = current_player # Размещаем метку текущего игрока на выбранной клетке
    neighbors = get_neighbors(row, col) # Получаем список соседних клеток
    for neighbor_row, neighbor_col in neighbors: # Проверяем, может ли клетка противника быть захвачена
       if can_capture(board, neighbor_row, neighbor_col, current_player): # Если соседняя клетка может быть захвачена
           capture_cell(board, neighbor_row, neighbor_col, current_player) # Захватываем клетку

def switch_player(current_player: int) -> int:
    """
    Переключает текущего игрока.

    :param current_player: Номер текущего игрока.
    :type current_player: int
    :return: Номер следующего игрока.
    :rtype: int
    """
    return 3 - current_player # Переключаем игрока с 1 на 2 или с 2 на 1

def is_board_full(board: list[list[int]]) -> bool:
    """
    Проверяет, заполнено ли игровое поле.

    :param board: Двумерный список, представляющий игровое поле.
    :type board: list[list[int]]
    :return: True, если все клетки заняты, иначе False.
    :rtype: bool
    """
    for row in range(BOARD_SIZE): # Проходим по каждой клетке на поле
        for col in range(BOARD_SIZE):
            if board[row][col] == 0: # Если клетка пуста (значение 0), возвращаем False (поле не заполнено)
                return False
    return True # Если все клетки заполнены, возвращаем True

def calculate_scores(board: list[list[int]]) -> tuple[int, int]:
    """
    Подсчитывает количество очков каждого игрока.

    :param board: Двумерный список, представляющий игровое поле.
    :type board: list[list[int]]
    :return: Кортеж с количеством очков первого и второго игрока.
    :rtype: tuple[int, int]
    """
    player1_score = 0 # Инициализируем счетчики для каждого игрока
    player2_score = 0
    for row in range(BOARD_SIZE): # Проходим по каждой клетке на поле
        for col in range(BOARD_SIZE):
            if board[row][col] == 1: # Если в клетке метка первого игрока, увеличиваем его счетчик
                player1_score += 1
            elif board[row][col] == 2: # Если в клетке метка второго игрока, увеличиваем его счетчик
                player2_score += 1
    return player1_score, player2_score # Возвращаем счетчики игроков

def determine_winner(player1_score: int, player2_score: int) -> str:
    """
    Определяет победителя игры.

    :param player1_score: Количество очков первого игрока.
    :type player1_score: int
    :param player2_score: Количество очков второго игрока.
    :type player2_score: int
    :return: Строка, объявляющая победителя или ничью.
    :rtype: str
    """
    if player1_score > player2_score: # Если у первого игрока больше очков, объявляем его победителем
        return "Победил игрок 1!"
    elif player2_score > player1_score: # Если у второго игрока больше очков, объявляем его победителем
        return "Победил игрок 2!"
    else: # Если количество очков одинаковое, объявляем ничью
        return "Ничья!"

def play_trap_game():
    """
    Основная функция игры "Ловушка".

    Инициализирует игровое поле, устанавливает текущего игрока и запускает игровой цикл.
    Запрашивает ходы игроков, обрабатывает их, проверяет на корректность, захватывает клетки и переключает игроков.
    Выводит текущее состояние игрового поля и результаты игры.
    """
    board = create_board() # Создаем новое игровое поле
    current_player = 1 # Устанавливаем первого игрока
    while not is_board_full(board): # Начинаем игровой цикл
        display_board(board) # Выводим текущее состояние игрового поля
        while True:
            try:
                row = int(input(f"Игрок {current_player}, введите номер строки (0-{BOARD_SIZE - 1}): ")) # Запрашиваем координаты хода у текущего игрока
                col = int(input(f"Игрок {current_player}, введите номер столбца (0-{BOARD_SIZE - 1}): "))
            except ValueError as ex: # Ловим ошибку ввода
                logger.error("Некорректный ввод. Пожалуйста, введите целые числа.", exc_info=ex)
                print("Некорректный ввод. Пожалуйста, введите целые числа.")
                continue
            if not is_valid_move(row, col): # Проверяем, находится ли введенные координаты в пределах игрового поля
                print("Некорректный ход. Координаты выходят за пределы поля.")
                continue
            if not is_cell_empty(board, row, col): # Проверяем, является ли выбранная клетка пустой
                print("Некорректный ход. Клетка уже занята.")
                continue
            break # Если все проверки пройдены, выходим из внутреннего цикла
        make_move(board, row, col, current_player) # Выполняем ход игрока
        current_player = switch_player(current_player) # Переключаем текущего игрока
    display_board(board) # Выводим финальное состояние игрового поля
    player1_score, player2_score = calculate_scores(board) # Подсчитываем количество очков каждого игрока
    winner = determine_winner(player1_score, player2_score) # Определяем победителя
    print(f"Игрок 1: {player1_score} очков") # Выводим результат игры
    print(f"Игрок 2: {player2_score} очков")
    print(winner)


if __name__ == "__main__":
    play_trap_game() # Запускаем игру
"""
Объяснение кода:
1. **Импорт модуля `copy`**
    - `import copy`: Импортирует модуль `copy` для создания глубоких копий списков (игрового поля).
2. **Импорт логгера**
    - `from src.logger.logger import logger`: Импортирует модуль логгера для записи ошибок.
3. **Константы**
    - `BOARD_SIZE = 7`: Определяет размер игрового поля (7x7).
4. **Функция `create_board()`**
    - Создает и возвращает пустое игровое поле в виде двумерного списка, заполненного нулями.
5. **Функция `display_board(board)`**
     - Принимает игровое поле в качестве аргумента.
     - Выводит текущее состояние игрового поля в консоль, используя символы '.' для пустых клеток, '1' для меток первого игрока и '2' для меток второго игрока.
6. **Функция `is_valid_move(row, col)`**
   - Проверяет, находятся ли координаты (row, col) в пределах игрового поля.
   - Возвращает `True`, если координаты действительны, иначе `False`.
7. **Функция `is_cell_empty(board, row, col)`**
   - Проверяет, является ли клетка с координатами (row, col) пустой (равна 0).
   - Возвращает `True`, если клетка пуста, иначе `False`.
8. **Функция `get_neighbors(row, col)`**
   - Возвращает список координат соседних клеток для заданной клетки (сверху, снизу, слева и справа).
   - Исключает координаты, выходящие за границы игрового поля.
9. **Функция `can_capture(board, row, col, current_player)`**
   - Проверяет, может ли клетка противника (с координатами row, col) быть захвачена текущим игроком.
   - Возвращает `True`, если клетка может быть захвачена, иначе `False`.
10. **Функция `capture_cell(board, row, col, current_player)`**
    - Захватывает клетку противника, изменяя её значение на значение текущего игрока.
11. **Функция `make_move(board, row, col, current_player)`**
      - Размещает метку текущего игрока на выбранной клетке.
      - Проверяет и захватывает соседние клетки противника, если они могут быть захвачены.
12. **Функция `switch_player(current_player)`**
     - Меняет текущего игрока (с 1 на 2 или с 2 на 1).
13. **Функция `is_board_full(board)`**
    - Проверяет, заполнено ли все игровое поле.
    - Возвращает `True`, если все клетки заняты, иначе `False`.
14. **Функция `calculate_scores(board)`**
     - Подсчитывает количество меток каждого игрока на игровом поле.
     - Возвращает количество очков для каждого игрока.
15. **Функция `determine_winner(player1_score, player2_score)`**
     - Определяет победителя на основе подсчитанных очков.
     - Возвращает сообщение о победителе или ничьей.
16. **Функция `play_trap_game()`**
     - Основная функция, управляющая ходом игры.
     - Инициализирует игровое поле, текущего игрока, и запускает основной игровой цикл.
     - Запрашивает ходы игроков, обрабатывает их, проверяет на корректность, захватывает клетки и переключает игроков.
     - Выводит текущее состояние игрового поля и результаты игры.
17. **Запуск игры**
    - `if __name__ == "__main__":`: Этот блок гарантирует, что функция `play_trap_game()` будет запущена, только если файл исполняется напрямую, а не импортируется как модуль.
    - `play_trap_game()`: Вызывает функцию для начала игры.
"""
```