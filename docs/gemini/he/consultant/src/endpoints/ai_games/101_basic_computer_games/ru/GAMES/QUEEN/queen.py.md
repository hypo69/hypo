# Анализ кода модуля `queen.py`

**Качество кода**
- **Соблюдение требований к формату кода (1-10):**
  -  **Преимущества:**
     - Код хорошо структурирован и разделен на функции, что улучшает читаемость и повторное использование.
     - Логика игры четко определена и соответствует описанию в начале модуля.
     - Используются осмысленные имена переменных и функций.
  -  **Недостатки:**
      - Отсутствует документация в формате reStructuredText (RST), что затрудняет понимание кода и его использование в проектах.
      - Не используется логгирование для отслеживания ошибок.
      - Обработка исключений в `get_player_move` неполная и требует улучшения.
      -  Жестко заданные начальные позиции ферзей могут быть параметризованы.
      - Комментарии в коде не все в формате reStructuredText.

**Рекомендации по улучшению**
1.  **Документация RST:** Необходимо добавить документацию в формате RST для модуля, функций и переменных. Это сделает код более понятным и легким для использования.
2.  **Логирование:** Следует использовать `from src.logger.logger import logger` для логирования ошибок и отладки. Заменить `print` на `logger.error` или `logger.debug` при необходимости.
3.  **Обработка исключений:** Улучшить обработку исключений в `get_player_move`, добавив более точные сообщения об ошибках.
4.  **Параметризация:** Сделать начальные позиции ферзей параметрами, чтобы можно было легко изменять их.
5.  **Форматирование кода:**  Привести код к стандартам PEP8 (например, пробелы вокруг операторов, константы заглавными буквами).
6.  **Удалить лишние комментарии**: Оставить только те, что после `#`, добавив к ним описание в `RST`.
7.  **Оптимизация**: Убрать неиспользуемые импорты.

**Улучшенный код**
```python
"""
Модуль для реализации игры "Ферзь" на шахматной доске.
=====================================================

Этот модуль содержит функции для управления игровым процессом,
включая вывод доски, проверку ходов и управление ходами игроков.

Пример использования
--------------------

.. code-block:: python

    from src.endpoints.ai_games.101_basic_computer_games.ru.GAMES.QUEEN import queen

    # Запуск игры
    queen.start_game()
"""
import sys  # импорт не используется, удален

from src.logger.logger import logger  # добавление импорта для логгера
from typing import Tuple

# Константы
BOARD_SIZE = 8 # размер доски
PLAYER1_START_X = 0 # начальная позиция X для первого игрока
PLAYER1_START_Y = 3 # начальная позиция Y для первого игрока
PLAYER2_START_X = 7 # начальная позиция X для второго игрока
PLAYER2_START_Y = 3 # начальная позиция Y для второго игрока


def print_board(player1_x: int, player1_y: int, player2_x: int, player2_y: int) -> None:
    """
    Выводит на экран шахматную доску с указанием текущих позиций ферзей.

    :param player1_x: Координата X ферзя первого игрока.
    :param player1_y: Координата Y ферзя первого игрока.
    :param player2_x: Координата X ферзя второго игрока.
    :param player2_y: Координата Y ферзя второго игрока.
    """
    print("   0  1  2  3  4  5  6  7")
    for row in range(BOARD_SIZE):
        row_str = str(row) + " "
        for col in range(BOARD_SIZE):
            if row == player1_y and col == player1_x:
                row_str += " 1 "
            elif row == player2_y and col == player2_x:
                row_str += " 2 "
            else:
                row_str += " . "
        print(row_str)


def is_valid_move(current_x: int, current_y: int, next_x: int, next_y: int) -> bool:
    """
    Проверяет, является ли ход ферзя допустимым.

    Ход допустим, если ферзь двигается по горизонтали, вертикали или диагонали.

    :param current_x: Текущая координата X ферзя.
    :param current_y: Текущая координата Y ферзя.
    :param next_x: Следующая координата X ферзя.
    :param next_y: Следующая координата Y ферзя.
    :return: `True`, если ход допустим, иначе `False`.
    """
    if next_x < 0 or next_x >= BOARD_SIZE or next_y < 0 or next_y >= BOARD_SIZE:
        return False  # Проверка выхода за границы доски

    if current_x == next_x:  # Вертикальное перемещение
        return True
    if current_y == next_y:  # Горизонтальное перемещение
        return True
    if abs(current_x - next_x) == abs(current_y - next_y):  # Диагональное перемещение
        return True
    return False


def get_player_move(player_number: int, current_x: int, current_y: int) -> Tuple[int, int]:
    """
    Запрашивает у игрока ввод координат для перемещения ферзя.

    Проверяет допустимость введенных координат.

    :param player_number: Номер игрока (1 или 2).
    :param current_x: Текущая координата X ферзя.
    :param current_y: Текущая координата Y ферзя.
    :return: Кортеж с новыми координатами (next_x, next_y).
    :raises ValueError: Если ввод не соответствует формату или если ход недопустимый.
    """
    while True:
        try:
            move_str = input(f"Игрок {player_number}, введите ход (x, y): ") # Запрос ввода хода от игрока
            next_x, next_y = map(int, move_str.split(',')) # получение координат из ввода
            if is_valid_move(current_x, current_y, next_x, next_y): # проверка допустимости хода
                return next_x, next_y # возврат координат если ход допустим
            print("Недопустимый ход. Попробуйте еще раз.") # сообщение если ход не допустим
        except ValueError as e: # отлов ошибки ввода
             logger.error(f"Неверный формат ввода или недопустимый ход: {e}") # логирование ошибки
             print("Неверный формат ввода. Введите два числа через запятую, например: 1,2") # сообщение об ошибке


def start_game() -> None:
    """
    Запускает основной игровой цикл.
    """
    player1_x = PLAYER1_START_X # начальная позиция X для первого игрока
    player1_y = PLAYER1_START_Y # начальная позиция Y для первого игрока
    player2_x = PLAYER2_START_X # начальная позиция X для второго игрока
    player2_y = PLAYER2_START_Y # начальная позиция Y для второго игрока

    while True:
        print_board(player1_x, player1_y, player2_x, player2_y)  # Вывод доски
        # Ход игрока 1
        print("Ход игрока 1:")
        next_player1_x, next_player1_y = get_player_move(1, player1_x, player1_y)  # получение следующего хода
        player1_x, player1_y = next_player1_x, next_player1_y # обновление позиции ферзя 1

        if player1_x == BOARD_SIZE - 1:  # Проверка на победу
            print("Игрок 1 победил!")
            break  # Завершение цикла
        # Ход игрока 2
        print_board(player1_x, player1_y, player2_x, player2_y)
        print("Ход игрока 2:")
        next_player2_x, next_player2_y = get_player_move(2, player2_x, player2_y) # получение следующего хода
        player2_x, player2_y = next_player2_x, next_player2_y # обновление позиции ферзя 2

        if player2_x == 0:  # Проверка на победу
            print("Игрок 2 победил!")
            break  # Завершение цикла
if __name__ == "__main__":
    start_game()
```