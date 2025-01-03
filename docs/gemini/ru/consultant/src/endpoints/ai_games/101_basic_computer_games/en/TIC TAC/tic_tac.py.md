# Анализ кода модуля tic_tac.py

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован, логически разделен на функции.
    - Имеется подробная документация в виде блок-схемы и описания алгоритма.
    - Используются осмысленные имена переменных и функций.
    - Реализованы все основные функции для игры в крестики-нолики.
- Минусы
    - Отсутствует явная обработка ошибок, кроме проверки ввода пользователя.
    - Не используется логирование.
    - Отсутствуют docstring для модуля, а также для переменных.
    - Не используется `j_loads` или `j_loads_ns` для чтения каких-либо файлов (что не является ошибкой, так как в данном коде нет работы с файлами).
    - Отсутствуют проверки на корректность ввода номера ячейки.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля с описанием назначения модуля.
2.  Добавить docstring для всех переменных.
3.  Добавить логирование для отслеживания ошибок и событий.
4.  Использовать `logger.error` вместо общих `except` для обработки ошибок.
5.  Улучшить валидацию ввода пользователя, чтобы исключить ошибки.
6.  Переписать все комментарии в формате reStructuredText.

**Оптимизированный код**

```python
"""
Модуль для реализации игры "Крестики-нолики".
=========================================================================================

Этот модуль предоставляет функции для игры в крестики-нолики между пользователем и компьютером.
Он включает в себя логику игрового поля, проверки победы и ничьи, а также основной игровой цикл.

Пример использования
--------------------

Пример запуска игры "Крестики-нолики":

.. code-block:: python

    if __name__ == "__main__":
        play_tic_tac_toe()
"""
__author__ = 'hypo69 (hypo69@davidka.net)'

from src.logger.logger import logger

def print_board(board: list) -> None:
    """
    Выводит текущее состояние игрового поля.

    :param board: Список, представляющий игровое поле.
    :type board: list
    :return: None
    """
    print("\n   " + board[1] + " | " + board[2] + " | " + board[3])
    print("  ---+---+---")
    print("   " + board[4] + " | " + board[5] + " | " + board[6])
    print("  ---+---+---")
    print("   " + board[7] + " | " + board[8] + " | " + board[9] + "\n")


def check_win(board: list, player: str) -> bool:
    """
    Проверяет, есть ли выигрышная комбинация для данного игрока.

    :param board: Список, представляющий игровое поле.
    :type board: list
    :param player: Символ игрока ('X' или 'O').
    :type player: str
    :return: True, если игрок выиграл, иначе False.
    :rtype: bool
    """
    # Все возможные выигрышные комбинации
    winning_combinations: list = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Горизонтальные
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Вертикальные
        [1, 5, 9], [3, 5, 7]  # Диагональные
    ]
    # Проходим по каждой комбинации и проверяем, соответствует ли она символам игрока
    for combination in winning_combinations:
        if (board[combination[0]] == board[combination[1]] ==
                board[combination[2]] == player):
            return True
    return False


def check_draw(board: list) -> bool:
    """
    Проверяет, является ли текущая игра ничьей.

    :param board: Список, представляющий игровое поле.
    :type board: list
    :return: True, если ничья, иначе False.
    :rtype: bool
    """
    # Если все клетки заполнены и нет победителя, то игра заканчивается ничьей
    return ' ' not in board[1:]


def play_tic_tac_toe() -> None:
    """
    Основная функция для запуска игры "Крестики-нолики".
    """
    # Инициализируем игровое поле
    board: list = [' '] * 10  # 0 индекс не используется
    # Основной игровой цикл
    while True:
        # Выводим игровое поле
        print_board(board)

        # Ход игрока (человека)
        while True:
            try:
                # Запрашивает у пользователя ввод номера клетки
                cellNumber: int = int(input("Введите номер клетки (1-9) для 'O': "))
                # Проверяем ввод на корректность
                if 1 <= cellNumber <= 9 and board[cellNumber] == ' ':
                    board[cellNumber] = 'O'
                    break
                else:
                    print("Неверный ввод. Пожалуйста, введите номер свободной клетки от 1 до 9.")
            except ValueError as e:
                # Логируем ошибку, если ввод не является целым числом
                logger.error(f'Неверный ввод. Ошибка: {e}')
                print("Неверный ввод. Пожалуйста, введите целое число от 1 до 9.")
            except Exception as e:
                # Логируем любую другую ошибку
                logger.error(f'Произошла ошибка: {e}')
                print("Произошла ошибка, попробуйте еще раз.")


        # Проверяем, выиграл ли игрок
        if check_win(board, 'O'):
            print_board(board)
            print("Вы выиграли! Поздравляю!")
            break

        # Проверяем, не ничья ли
        if check_draw(board):
            print_board(board)
            print("Ничья!")
            break

        # Ход компьютера
        # Ищем первую свободную клетку
        for i in range(1, 10):
            if board[i] == ' ':
                board[i] = 'X'
                break

        # Проверяем, выиграл ли компьютер
        if check_win(board, 'X'):
            print_board(board)
            print("Компьютер выиграл!")
            break
        # Проверяем, не ничья ли
        if check_draw(board):
            print_board(board)
            print("Ничья!")
            break


# Запуск игры
if __name__ == "__main__":
    play_tic_tac_toe()


"""
Объяснение кода:
1.  **Функция `print_board(board)`**:
    -   Принимает список `board`, представляющий игровое поле.
    -   Выводит текущее состояние поля в консоль, разделяя клетки линиями для наглядности.
2.  **Функция `check_win(board, player)`**:
    -   Принимает `board` и символ `player` ('X' или 'O').
    -   Содержит список `winning_combinations`, описывающий все возможные выигрышные комбинации.
    -   Проверяет каждую комбинацию на наличие трех символов игрока.
    -   Возвращает `True`, если есть выигрышная комбинация для данного игрока, иначе `False`.
3.  **Функция `check_draw(board)`**:
    -   Принимает список `board`.
    -   Проверяет, есть ли свободные клетки на игровом поле.
    -   Возвращает `True`, если все клетки заполнены (ничья), иначе `False`.
4.  **Функция `play_tic_tac_toe()`**:
    -   Инициализирует `board` как список из 10 элементов, где первые 9 представляют клетки, а 0 не используется.
    -   Основной цикл `while True:` продолжается до тех пор, пока не будет объявлен победитель или не будет ничья.
    -   Выводит текущее состояние доски с помощью `print_board(board)`.
    -   **Ход игрока**:
        -   Внутренний цикл `while True:` обеспечивает повторный ввод, пока не будет введен корректный ход.
        -   Запрашивает ввод номера клетки у игрока и проверяет его корректность (число от 1 до 9 и клетка свободна).
        -   Устанавливает символ 'O' в выбранную клетку.
        -   Выходит из внутреннего цикла, если ввод корректен.
    -   **Проверка победы игрока**:
        -   Вызывает функцию `check_win` для проверки победы игрока.
        -   Выводит сообщение о победе и заканчивает игру, если игрок выиграл.
    -   **Проверка ничьей**:
        -   Вызывает `check_draw`, чтобы проверить, не ничья ли игра.
        -   Выводит сообщение о ничьей и заканчивает игру, если ничья.
    -   **Ход компьютера**:
        -   Ищет первую свободную клетку в списке `board`.
        -   Устанавливает символ 'X' в найденную свободную клетку.
    -   **Проверка победы компьютера**:
        -   Вызывает `check_win`, чтобы проверить победу компьютера.
        -   Выводит сообщение о победе и заканчивает игру, если компьютер выиграл.
    -   **Проверка ничьей после хода компьютера**:
        -   Вызывает `check_draw` для проверки ничьи после хода компьютера.
        -   Выводит сообщение о ничьей, если игра завершилась вничью.
5.  **Запуск игры**:
    -  `if __name__ == "__main__":`: Этот блок гарантирует, что функция `play_tic_tac_toe()` будет запущена, только если файл исполняется напрямую, а не импортируется как модуль.
    - `play_tic_tac_toe()`: Вызывает функцию для начала игры.
"""