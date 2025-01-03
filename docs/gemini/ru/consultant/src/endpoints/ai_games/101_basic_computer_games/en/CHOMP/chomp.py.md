# Анализ кода модуля chomp.py

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован, функции разделены по логике (инициализация, отображение, ход, проверка окончания игры).
    - Наличие docstring для каждой функции, что улучшает понимание кода.
    - Использование reStructuredText (RST) в комментариях и docstring, что соответствует требованиям.
    - Блок-схема игры в формате mermaid
    - Код содержит обработку ошибок ввода, что делает игру более надежной.
    - Логика игры реализована корректно в соответствии с правилами игры CHOMP.
-  Минусы
    - Избыточное использование `try-except` блоков, можно заменить логированием ошибок с помощью `logger.error`.
    - Отсутствуют некоторые импорты
    - Не все комментарии после `#` объясняют блоки кода, некоторые повторяют docstring
    - Нет логирования
    - Имена некоторых переменных и функций не соответствуют общепринятым нормам (например, `row_move`, `col_move`)
    - Отсутствует описание модуля в формате RST.

**Рекомендации по улучшению**

1. **Импорты**: Добавить необходимые импорты `from src.logger.logger import logger`.
2. **Логирование**: Заменить избыточные `try-except` блоки на использование `logger.error`.
3. **Комментарии**: Уточнить комментарии после `#`, чтобы они действительно объясняли код, а не повторяли docstring.
4. **Именование**: Привести имена переменных и функций к более понятному виду (например, `row_move` заменить на `move_row`).
5. **Описание модуля**: Добавить описание модуля в формате RST.

**Оптимизированный код**
```python
"""
Модуль для реализации игры "CHOMP"
=========================================================================================

Этот модуль реализует игру "CHOMP" для двух игроков на прямоугольной доске,
представляющей собой шоколадную плитку. Цель игры - заставить противника
съесть отравленную дольку, расположенную в нижнем левом углу.

Пример использования
--------------------

Для запуска игры необходимо вызвать функцию `play_chomp()`:

.. code-block:: python

   if __name__ == "__main__":
        play_chomp()

"""
__author__ = 'hypo69 (hypo69@davidka.net)'

from src.logger.logger import logger

def initialize_board(rows: int, cols: int) -> list[list[str]]:
    """
    Инициализирует игровое поле (шоколадную плитку).

    :param rows: Количество строк на доске.
    :param cols: Количество столбцов на доске.
    :return: Список списков, представляющий игровую доску, где 'X' - шоколад, ' ' - пустое место.
    """
    board = [['X' for _ in range(cols)] for _ in range(rows)]
    return board

def display_board(board: list[list[str]]) -> None:
    """
    Выводит текущее состояние доски на экран.

    :param board: Игровая доска.
    """
    for row in board:
        print(' '.join(row))

def make_move(board: list[list[str]], move_row: int, move_col: int) -> list[list[str]]:
    """
    Обновляет состояние доски после хода игрока.
    Все клетки справа и выше выбранной позиции удаляются.

    :param board: Игровая доска.
    :param move_row: Строка, на которую игрок сделал ход.
    :param move_col: Столбец, на который игрок сделал ход.
    :return: Обновленная игровая доска.
    """
    rows = len(board)
    cols = len(board[0])
    for row in range(move_row, rows):
        for col in range(move_col, cols):
            board[row][col] = ' '
    return board

def is_game_over(board: list[list[str]]) -> bool:
    """
    Проверяет, закончилась ли игра.
    Игра заканчивается, если ядовитая долька (верхний левый угол) съедена.

    :param board: Игровая доска.
    :return: True, если игра окончена, иначе False.
    """
    return board[0][0] == ' '

def play_chomp() -> None:
    """
    Основная функция игры "CHOMP".
    Реализует игровой процесс, включая ввод размеров доски, отображение доски,
    и обработку ходов игроков.
    """
    while True:
        try:
            rows = int(input("Введите количество строк на доске: "))
            cols = int(input("Введите количество столбцов на доске: "))
            if rows <= 0 or cols <= 0:
                 print("Размер доски должен быть положительным числом.")
                 continue
            break
        except ValueError as e:
            logger.error("Ошибка ввода: Пожалуйста, введите целое число.", exc_info=e)
            print("Пожалуйста, введите целое число.")

    board = initialize_board(rows, cols)
    current_player = 1  # Начинает первый игрок

    while True:
        print(f"\nХод игрока {current_player}:")
        display_board(board)
        
        while True:
            try:
                move_row = int(input("Введите строку для откусывания (начиная с 0): "))
                move_col = int(input("Введите столбец для откусывания (начиная с 0): "))
                if move_row < 0 or move_col < 0 or move_row >= rows or move_col >= cols:
                    print("Неверный ход. Укажите строку и столбец в пределах доски")
                    continue
                if board[move_row][move_col] == ' ':
                     print("Вы не можете откусить пустое место. Попробуйте еще раз")
                     continue
                break
            except ValueError as e:
                logger.error("Ошибка ввода: Пожалуйста, введите целое число.", exc_info=e)
                print("Пожалуйста, введите целые числа.")
            except IndexError as e:
                 logger.error("Ошибка хода: Неверный ход. Укажите строку и столбец в пределах доски.", exc_info=e)
                 print("Неверный ход. Укажите строку и столбец в пределах доски")
            

        board = make_move(board, move_row, move_col)

        if is_game_over(board):
          print(f"Победил игрок {3-current_player}!")
          display_board(board)
          break
        
        current_player = 3 - current_player # Переключаем игрока

if __name__ == "__main__":
    play_chomp()

"""
Объяснение кода:
1.  **Инициализация**:
   -  `initialize_board(rows, cols)`: Функция создает игровую доску размером `rows` x `cols`. Изначально все ячейки заполнены символом 'X', представляющим шоколад.
2.  **Отображение доски**:
   -  `display_board(board)`: Функция выводит текущее состояние доски на экран, построчно отображая каждый ряд.
3.  **Ход игрока**:
   -  `make_move(board, move_row, move_col)`: Функция обновляет доску, удаляя все 'X' справа и ниже указанных координат `move_row` и `move_col`, заменяя их на ' '.
4.  **Проверка окончания игры**:
    -  `is_game_over(board)`: Проверяет, съедена ли отравленная долька (верхний левый угол). Если ячейка `board[0][0]` содержит ' ', то игра окончена.
5.  **Основная логика игры `play_chomp()`**:
    -   Запрашивает у пользователя размеры доски.
    -   Инициализирует доску.
    -   Организует цикл игры, в котором игроки по очереди делают ходы.
    -   Выводит текущее состояние доски.
    -   Запрашивает ввод координат хода у игрока.
    -   Обновляет доску после хода.
    -   Проверяет, закончилась ли игра.
    -   Выводит сообщение о победе одного из игроков.
    -   Переключает текущего игрока.
6.  **Обработка исключений**:
   -   Код содержит `try-except` блоки для обработки ошибок ввода (нечисловые значения), а также логирование с помощью `logger.error`
7.  **Запуск игры**:
   -  `if __name__ == "__main__":`:  Этот блок гарантирует, что функция `play_chomp()` будет запущена только при непосредственном запуске скрипта.
"""
```