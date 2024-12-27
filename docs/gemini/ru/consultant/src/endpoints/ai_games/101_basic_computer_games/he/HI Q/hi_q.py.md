# Анализ кода модуля `hi_q.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и разделен на отдельные функции, каждая из которых выполняет свою задачу.
    - Логика игры реализована корректно, включая проверку ходов и обновление доски.
    - Код достаточно читаемый, с использованием понятных имен переменных и функций.
    - Присутствуют docstring для функций.
    - Используется проверка ввода пользователя с обработкой ошибок.
- Минусы
    - Отсутствуют необходимые импорты.
    - Комментарии не соответствуют стандарту reStructuredText.
    - Нет логирования ошибок.
    - Не используются константы для магических значений (например, размер доски).

**Рекомендации по улучшению**

1.  **Импорты**: Добавить необходимые импорты, если таковые требуются.
2.  **Форматирование docstring**: Переписать docstring в формате reStructuredText.
3.  **Логирование**: Добавить логирование ошибок с помощью `src.logger.logger`.
4.  **Константы**: Использовать константы для магических значений, таких как размер доски.
5.  **Обработка ошибок**: Убрать избыточное использование `try-except`, заменить их на логирование ошибок.
6.  **Общая стилистика кода**: Привести в соответствие с остальными файлами проекта (использовать одинарные кавычки, избегать лишних комментариев).

**Оптимизированный код**

```python
"""
Модуль для реализации игры "HI Q".
====================================

Игра "HI Q" - это настольная игра для одного игрока, цель которой - оставить на доске только один колышек.
Идеальным завершением считается, когда этот колышек остается в центре доски.

Алгоритм:
    1. Инициализируется доска 5x3 с 14 колышками и 1 пустой клеткой в центре.
    2. Игроку предлагается ввести координаты колышка, который он хочет переместить, и направление перемещения.
    3. Проверяется, является ли перемещение допустимым.
    4. Если перемещение допустимо, колышек перемещается, колышек через который перепрыгнули удаляется, и доска обновляется.
    5. Если перемещение недопустимо, игроку сообщается об ошибке.
    6. Игра продолжается, пока на доске не останется только один колышек.
    7. Если последний колышек находится в центре доски, игрок выигрывает, иначе проигрывает.

Пример использования
--------------------

.. code-block:: python

    python hi_q.py

"""

from typing import List
from src.logger.logger import logger

BOARD_SIZE = 15
"""Константа для размера доски."""
CENTER_POSITION = 7
"""Константа для позиции центральной клетки."""
def print_board(board: List[str]) -> None:
    """
    Выводит игровое поле в консоль.

    :param board: Список, представляющий игровое поле.
    :return: None
    """
    print("  1 2 3 4 5")
    print("----------")
    row_num = 0
    for i in range(0, len(board), 5):
        row_num += 1
        print(row_num, end='|')
        print(*board[i:i + 5], sep='|')
    print("----------")

def is_valid_move(board: List[str], start: int, direction: str) -> bool:
    """
    Проверяет, является ли ход допустимым.

    :param board: Список, представляющий игровое поле.
    :param start: Индекс клетки, с которой начинается ход.
    :param direction: Направление хода ('u', 'd', 'l', 'r').
    :return: True, если ход допустим, иначе False.
    """
    if start < 0 or start >= len(board) or board[start] == '.':
        return False

    if direction == 'u':
        if start - 10 >= 0 and board[start - 5] != '.' and board[start - 10] == '.':
            return True
    elif direction == 'd':
        if start + 10 < len(board) and board[start + 5] != '.' and board[start + 10] == '.':
            return True
    elif direction == 'l':
        if (start % 5) > 1 and board[start - 1] != '.' and board[start - 2] == '.':
            return True
    elif direction == 'r':
        if (start % 5) < 3 and board[start + 1] != '.' and board[start + 2] == '.':
            return True
    return False

def make_move(board: List[str], start: int, direction: str) -> None:
    """
    Выполняет ход на игровом поле.

    :param board: Список, представляющий игровое поле.
    :param start: Индекс клетки, с которой начинается ход.
    :param direction: Направление хода ('u', 'd', 'l', 'r').
    :return: None
    """
    board[start] = '.'
    if direction == 'u':
        board[start - 5] = '.'
        board[start - 10] = 'o'
    elif direction == 'd':
        board[start + 5] = '.'
        board[start + 10] = 'o'
    elif direction == 'l':
        board[start - 1] = '.'
        board[start - 2] = 'o'
    elif direction == 'r':
        board[start + 1] = '.'
        board[start + 2] = 'o'

def check_win(board: List[str]) -> bool:
    """
    Проверяет, выиграл ли игрок.

    :param board: Список, представляющий игровое поле.
    :return: True, если игрок выиграл, иначе False.
    """
    count = 0
    last_position = 0
    for i in range(len(board)):
        if board[i] == 'o':
            count += 1
            last_position = i
    return count == 1 and last_position == CENTER_POSITION

def play_hi_q() -> None:
    """
    Запускает игру "HI Q".
    """
    board = ['o'] * BOARD_SIZE
    # Инициализация доски с колышками и пустой клеткой в центре.
    board[CENTER_POSITION] = '.'
    print("משחק HI Q")
    print_board(board)

    while True:
        count_pieces = board.count('o')
        if count_pieces == 1:
            break
        try:
            start = int(input("בחר את מיקום הכלי שממנו תרצה לקפוץ (1-15):")) - 1
            direction = input("בחר את כיוון הקפיצה (u/d/l/r):").lower()
            if direction not in ['u', 'd', 'l', 'r']:
                print("כיוון לא חוקי. בחר כיוון מתוך u, d, l, r")
                continue
        except (ValueError, IndexError) as e:
            logger.error(f'Некорректный ввод пользователя: {e}')
            print("קלט לא חוקי. הזן מספר משבצת וכיוון תקינים")
            continue
        if is_valid_move(board, start, direction):
            make_move(board, start, direction)
            print_board(board)
        else:
            print("מהלך לא חוקי. נסה שוב.")

    if check_win(board):
        print("ניצחת! נשאר כלי אחד במרכז!")
    else:
        print("הפסדת! לא הצלחת להשאיר כלי אחד במרכז.")


if __name__ == "__main__":
    play_hi_q()
```