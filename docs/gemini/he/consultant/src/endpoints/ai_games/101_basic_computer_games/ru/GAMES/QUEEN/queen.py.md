# Анализ кода модуля `queen.py`

**Качество кода**
* Соответствие требованиям к формату кода (1-10): 8
    * **Преимущества:**
        * Код игры "Ферзь" достаточно хорошо структурирован и соответствует алгоритму, представленному в начале.
        * Функции `print_board`, `is_valid_move` и `get_player_move` отвечают за конкретные задачи и упрощают понимание кода.
        * Алгоритм игры в целом понятен и реализован правильно.
        * Присутствуют базовые проверки корректности ввода и хода.
    * **Недостатки:**
        * Отсутствует подробное документирование кода в формате RST, а также нет использования `logger`.
        * Использование `sys` без явной необходимости.
        * Ошибки не обрабатываются с помощью `logger.error`.
        * Не хватает проверок на корректность ввода (например, выход за рамки 0-7).
        * Цикл `while True` для ввода может быть более элегантным, с возможностью прерывания по специальной команде.
        * Нет проверок на то, что ход не приведет к столкновению с другой фигурой (хотя в этой версии игры это невозможно).
        * Код использует прямые выводы `print`, без настройки на logger.

**Рекомендации по улучшению**
1. **Документирование:**
   -  Добавить полное документирование в формате RST для всех функций, классов и модуля.
   -  Использовать docstring для каждой функции с описанием параметров, возвращаемых значений и исключений.

2. **Обработка ошибок:**
   -  Заменить блоки `try-except` на `logger.error` для обработки ошибок.
   -  Проверять ввод пользователя на корректность и выводить соответствующие сообщения об ошибках через `logger`.
   -  Использовать явные исключения с `raise` для обработки ошибок.
   -  Применять `logger.debug` для отладочных сообщений.

3. **Структура кода:**
    - Использовать более осмысленные имена переменных (например `player1_position_x` вместо `player1_x`).
    - Вынести логику игры в отдельный класс `QueenGame` для лучшей организации и переиспользования кода.
    - Добавить проверку на корректность ввода координат от пользователя (например, убедиться, что ввод - числа).

4. **Улучшение пользовательского опыта:**
   - Добавить обработку команды выхода из игры (например, ввод `exit`).
   - Выводить больше информации для пользователя (например, текущие позиции ферзей перед каждым ходом).

5. **Форматирование:**
   -  Привести код в соответствие с PEP8.

6. **Логирование:**
   -  Использовать `logger` для записи всех ошибок, предупреждений и отладочных сообщений.

7. **Удалить ненужный импорт**
    - Удалить импорт `sys` так как он нигде не используется

**Улучшенный код**
```python
"""
Модуль для реализации игры "Ферзь".
=========================================================================================

В этом модуле реализована игра "Ферзь" для двух игроков. Каждый игрок управляет
ферзем на шахматной доске 8x8. Цель игры - первым достичь противоположного края доски.

Пример использования
--------------------

.. code-block:: python

    game = QueenGame()
    game.play()
"""
from src.logger.logger import logger # Импорт logger для логирования ошибок
from typing import Tuple

class QueenGame:
    """
    Класс, представляющий игру "Ферзь".
    """
    def __init__(self):
        """
        Инициализирует начальные позиции ферзей.
        """
        self.player1_position_x = 0
        self.player1_position_y = 3
        self.player2_position_x = 7
        self.player2_position_y = 3

    def print_board(self) -> None:
        """
        Выводит на экран шахматную доску с текущими позициями ферзей.
        """
        print("   0  1  2  3  4  5  6  7")
        for row in range(8):
            row_str = str(row) + " "
            for col in range(8):
                if row == self.player1_position_y and col == self.player1_position_x:
                    row_str += " 1 "
                elif row == self.player2_position_y and col == self.player2_position_x:
                    row_str += " 2 "
                else:
                    row_str += " . "
            print(row_str)

    def is_valid_move(self, current_x: int, current_y: int, next_x: int, next_y: int) -> bool:
        """
        Проверяет, является ли ход ферзя допустимым.

        :param current_x: Текущая координата x ферзя.
        :param current_y: Текущая координата y ферзя.
        :param next_x: Следующая координата x ферзя.
        :param next_y: Следующая координата y ферзя.
        :return: True, если ход допустим, False в противном случае.
        """
        if not (0 <= next_x <= 7 and 0 <= next_y <= 7):
            return False  # Проверка выхода за границы доски

        if current_x == next_x:  # Вертикальное перемещение
            return True
        if current_y == next_y:  # Горизонтальное перемещение
            return True
        if abs(current_x - next_x) == abs(current_y - next_y):  # Диагональное перемещение
            return True
        return False

    def get_player_move(self, player_number: int, current_x: int, current_y: int) -> Tuple[int, int]:
        """
        Запрашивает у игрока ввод координат для перемещения ферзя.
        Проверяет допустимость введенных координат.
        Возвращает новые координаты.

        :param player_number: Номер игрока (1 или 2).
        :param current_x: Текущая координата x ферзя.
        :param current_y: Текущая координата y ферзя.
        :return: Кортеж (next_x, next_y) с новыми координатами.
        """
        while True:
            try:
                move_str = input(f"Игрок {player_number}, введите ход (x, y) или 'exit' для выхода: ")
                if move_str.lower() == 'exit':
                    print("Игра завершена по запросу пользователя.")
                    exit()
                next_x, next_y = map(int, move_str.split(','))
                if self.is_valid_move(current_x, current_y, next_x, next_y):
                    return next_x, next_y
                else:
                    logger.error("Недопустимый ход. Попробуйте еще раз.")
            except ValueError as e:
                logger.error(f"Неверный формат ввода. Введите два числа через запятую, например: 1,2. {e}")
            except Exception as e:
                logger.error(f"Непредвиденная ошибка: {e}")

    def play(self) -> None:
        """
        Запускает игровой цикл.
        """
        while True:
            self.print_board()  # Выводим доску
            # Ход игрока 1
            print("Ход игрока 1:")
            next_player1_x, next_player1_y = self.get_player_move(1, self.player1_position_x, self.player1_position_y)
            self.player1_position_x, self.player1_position_y = next_player1_x, next_player1_y

            if self.player1_position_x == 7:  # Проверка на победу
                print("Игрок 1 победил!")
                break  # Завершаем цикл

            # Ход игрока 2
            self.print_board()
            print("Ход игрока 2:")
            next_player2_x, next_player2_y = self.get_player_move(2, self.player2_position_x, self.player2_position_y)
            self.player2_position_x, self.player2_position_y = next_player2_x, next_player2_y

            if self.player2_position_x == 0:  # Проверка на победу
                print("Игрок 2 победил!")
                break  # Завершаем цикл


if __name__ == '__main__':
    game = QueenGame()
    game.play()
```
```python
"""
Модуль для реализации игры "Ферзь".
=========================================================================================

В этом модуле реализована игра "Ферзь" для двух игроков. Каждый игрок управляет
ферзем на шахматной доске 8x8. Цель игры - первым достичь противоположного края доски.

Пример использования
--------------------

.. code-block:: python

    game = QueenGame()
    game.play()
"""
from src.logger.logger import logger # Импорт logger для логирования ошибок # Добавлен импорт логгера
from typing import Tuple # Добавлен импорт Tuple

class QueenGame:
    """
    Класс, представляющий игру "Ферзь".
    """
    def __init__(self):
        """
        Инициализирует начальные позиции ферзей.
        """
        self.player1_position_x = 0 # Инициализация начальной позиции x первого игрока
        self.player1_position_y = 3 # Инициализация начальной позиции y первого игрока
        self.player2_position_x = 7 # Инициализация начальной позиции x второго игрока
        self.player2_position_y = 3 # Инициализация начальной позиции y второго игрока

    def print_board(self) -> None:
        """
        Выводит на экран шахматную доску с текущими позициями ферзей.
        """
        print("   0  1  2  3  4  5  6  7")
        for row in range(8):
            row_str = str(row) + " "
            for col in range(8):
                if row == self.player1_position_y and col == self.player1_position_x:
                    row_str += " 1 "
                elif row == self.player2_position_y and col == self.player2_position_x:
                    row_str += " 2 "
                else:
                    row_str += " . "
            print(row_str)

    def is_valid_move(self, current_x: int, current_y: int, next_x: int, next_y: int) -> bool:
        """
        Проверяет, является ли ход ферзя допустимым.

        :param current_x: Текущая координата x ферзя.
        :param current_y: Текущая координата y ферзя.
        :param next_x: Следующая координата x ферзя.
        :param next_y: Следующая координата y ферзя.
        :return: True, если ход допустим, False в противном случае.
        """
        if not (0 <= next_x <= 7 and 0 <= next_y <= 7): # Проверка выхода за границы доски
            return False  # Проверка выхода за границы доски

        if current_x == next_x:  # Вертикальное перемещение
            return True
        if current_y == next_y:  # Горизонтальное перемещение
            return True
        if abs(current_x - next_x) == abs(current_y - next_y):  # Диагональное перемещение
            return True
        return False

    def get_player_move(self, player_number: int, current_x: int, current_y: int) -> Tuple[int, int]:
        """
        Запрашивает у игрока ввод координат для перемещения ферзя.
        Проверяет допустимость введенных координат.
        Возвращает новые координаты.

        :param player_number: Номер игрока (1 или 2).
        :param current_x: Текущая координата x ферзя.
        :param current_y: Текущая координата y ферзя.
        :return: Кортеж (next_x, next_y) с новыми координатами.
        """
        while True:
            try:
                move_str = input(f"Игрок {player_number}, введите ход (x, y) или 'exit' для выхода: ") # Запрашиваем ввод хода
                if move_str.lower() == 'exit': # Проверяем команду выхода
                    print("Игра завершена по запросу пользователя.") # Вывод сообщения о завершении игры
                    exit() # Завершаем игру
                next_x, next_y = map(int, move_str.split(',')) # Преобразуем ввод в координаты
                if self.is_valid_move(current_x, current_y, next_x, next_y): # Проверка допустимости хода
                    return next_x, next_y # Возвращаем новые координаты
                else:
                    logger.error("Недопустимый ход. Попробуйте еще раз.") # Логируем ошибку если ход не допустим
            except ValueError as e:
                logger.error(f"Неверный формат ввода. Введите два числа через запятую, например: 1,2. {e}") # Логируем ошибку ввода
            except Exception as e:
                logger.error(f"Непредвиденная ошибка: {e}") # Логируем непредвиденную ошибку

    def play(self) -> None:
        """
        Запускает игровой цикл.
        """
        while True:
            self.print_board()  # Выводим доску # Выводим доску перед ходом игрока 1
            # Ход игрока 1
            print("Ход игрока 1:")
            next_player1_x, next_player1_y = self.get_player_move(1, self.player1_position_x, self.player1_position_y) # Получаем ход от игрока 1
            self.player1_position_x, self.player1_position_y = next_player1_x, next_player1_y # Обновляем позицию игрока 1

            if self.player1_position_x == 7:  # Проверка на победу # Проверяем достиг ли игрок 1 конца доски
                print("Игрок 1 победил!") # Выводим сообщение о победе
                break  # Завершаем цикл # Завершаем игру

            # Ход игрока 2
            self.print_board() # Выводим доску перед ходом игрока 2
            print("Ход игрока 2:")
            next_player2_x, next_player2_y = self.get_player_move(2, self.player2_position_x, self.player2_position_y) # Получаем ход от игрока 2
            self.player2_position_x, self.player2_position_y = next_player2_x, next_player2_y # Обновляем позицию игрока 2

            if self.player2_position_x == 0:  # Проверка на победу # Проверяем достиг ли игрок 2 конца доски
                print("Игрок 2 победил!") # Выводим сообщение о победе
                break  # Завершаем цикл # Завершаем игру


if __name__ == '__main__':
    game = QueenGame() # Создаем экземпляр игры
    game.play() # Запускаем игру
```