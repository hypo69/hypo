# Анализ кода модуля bingo.py

**Качество кода**
6/10
- Плюсы
    - Код хорошо структурирован, функции разделены по логике и каждая выполняет свою задачу.
    - Присутствуют docstring, объясняющие назначение функций.
    - Код в целом соответствует требованиям задания.
- Минусы
    - Комментарии не соответствуют формату RST.
    - Нет логирования ошибок.
    - Использованы магические числа (75, 5).
    - Нет констант для значений ('X').

**Рекомендации по улучшению**

1.  **Документация**:
    - Переписать docstring в формате reStructuredText (RST).
    - Добавить более подробные описания параметров и возвращаемых значений.
    - Добавить описание модуля в начале файла.

2.  **Логирование**:
    - Добавить логирование ошибок с использованием `logger.error`.
    - Избегать избыточных `try-except` блоков, используя `logger.error` для обработки ошибок.

3.  **Константы**:
    - Использовать константы для магических чисел (75, 5) и символа 'X'.

4. **Улучшения функций**:
    -  Переписать комментарии в теле функций, чтобы они соответствовали формату reStructuredText (RST).

**Оптимизированный код**

```python
"""
Модуль для игры в бинго.
========================

Этот модуль реализует классическую игру в бинго для одного игрока.
Игрок получает доску с случайными числами, а компьютер объявляет числа.
Цель игрока - отметить числа на своей доске, пока не будет сформирована полная
линия, столбец или диагональ, после чего игрок объявляет "Бинго" и побеждает.

Пример использования
--------------------

.. code-block:: python

    from bingo import play_bingo
    play_bingo()

"""
import random
from src.logger.logger import logger # Импорт logger

# Константы для размера доски и максимального числа
BOARD_SIZE = 5
MAX_NUMBER = 75
MARKED_CELL = 'X'


def create_bingo_board() -> list:
    """
    Создаёт доску бинго 5x5 с уникальными случайными числами от 1 до 75.

    :return: Двумерный список, представляющий доску бинго.
    :rtype: list
    """
    try:
        numbers = random.sample(range(1, MAX_NUMBER + 1), BOARD_SIZE * BOARD_SIZE) # Генерация уникальных чисел
        board = [numbers[i:i + BOARD_SIZE] for i in range(0, BOARD_SIZE * BOARD_SIZE, BOARD_SIZE)] # Создание доски
        return board
    except Exception as e:
        logger.error('Ошибка при создании доски бинго', exc_info=True)
        return []

def display_bingo_board(board: list):
    """
    Выводит доску бинго в консоль.

    :param board: Двумерный список, представляющий доску бинго.
    :type board: list
    """
    try:
        for row in board:
            print(' '.join(map(lambda x: f"{x:2}", row))) # Вывод каждой строки доски
    except Exception as e:
        logger.error('Ошибка при выводе доски бинго', exc_info=True)

def get_random_number(called_numbers: list) -> int:
    """
    Генерирует случайное число от 1 до 75, которое еще не было выбрано.

    :param called_numbers: Список уже выбранных чисел.
    :type called_numbers: list
    :return: Случайное число, которое еще не было выбрано.
    :rtype: int
    """
    try:
        while True:
            number = random.randint(1, MAX_NUMBER) # Генерация случайного числа
            if number not in called_numbers:
                return number
    except Exception as e:
         logger.error('Ошибка при получении случайного числа', exc_info=True)
         return None


def mark_number_on_board(board: list, number: int, called_numbers: list):
    """
    Отмечает число на доске бинго, заменяя его на 'X'.

    :param board: Двумерный список, представляющий доску бинго.
    :type board: list
    :param number: Число, которое нужно отметить.
    :type number: int
    :param called_numbers: Список уже выбранных чисел.
    :type called_numbers: list
    """
    try:
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == number:
                    board[row][col] = MARKED_CELL  # Отметка числа на доске
                    return
    except Exception as e:
        logger.error('Ошибка при отметке числа на доске', exc_info=True)


def check_winner(board: list, called_numbers: list) -> bool:
    """
    Проверяет, есть ли победитель на доске бинго.

    Победа засчитывается, если есть полная линия (строка, столбец или диагональ)
    с отмеченными числами ('X').

    :param board: Двумерный список, представляющий доску бинго.
    :type board: list
    :param called_numbers: Список уже выбранных чисел.
    :type called_numbers: list
    :return: True, если есть победитель, False в противном случае.
    :rtype: bool
    """
    try:
        # Проверка строк
        for row in board:
            if all(cell == MARKED_CELL for cell in row):
                return True
        # Проверка столбцов
        for col in range(len(board[0])):
            if all(board[row][col] == MARKED_CELL for row in range(len(board))):
                return True
        # Проверка диагоналей
        if all(board[i][i] == MARKED_CELL for i in range(len(board))):
            return True
        if all(board[i][len(board) - 1 - i] == MARKED_CELL for i in range(len(board))):
             return True

        return False  # Если нет победителя
    except Exception as e:
        logger.error('Ошибка при проверке победителя', exc_info=True)
        return False



def play_bingo():
    """
    Запускает игру в бинго.
    """
    try:
        bingo_board = create_bingo_board() # Создание доски бинго
        if not bingo_board:
            return # Выход, если доска не создана
        called_numbers = [] # Инициализация списка названных чисел
        display_bingo_board(bingo_board) # Вывод доски на экран
        while True:
            number = get_random_number(called_numbers) # Получение нового числа
            if number is None:
                return  # Завершение, если не удалось получить число
            called_numbers.append(number)
            print(f"Выпало число: {number}") # Вывод числа
            mark_number_on_board(bingo_board, number, called_numbers) # Отметка числа на доске
            display_bingo_board(bingo_board) # Вывод доски после отметки
            if check_winner(bingo_board, called_numbers): # Проверка на победу
                print("БИНГО!")
                break
    except Exception as e:
         logger.error('Произошла ошибка в процессе игры', exc_info=True)



if __name__ == "__main__":
    play_bingo()
```