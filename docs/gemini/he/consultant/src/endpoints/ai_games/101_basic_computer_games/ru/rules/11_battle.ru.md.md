# Анализ кода модуля `11_battle.ru.md`

**Качество кода**

-  Соответствие требованиям к формату кода с 1 по 10:
    -  Преимущества:
        -   Документ содержит подробное описание игры "Морской бой" и ее правил.
        -   Присутствует пошаговая инструкция для реализации игры.
        -   Представлены примеры работы программы с различными сценариями.
        -   Описаны возможные ограничения и как их обрабатывать.
    -  Недостатки:
        -   Документ не содержит кода, а только описание игры.
        -   Не соблюдены требования по использованию reStructuredText (RST) для комментариев и docstring, поскольку это Markdown документ.
        -   Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson`, так как это описание, а не код.
        -   Отсутствуют импорты и логирование ошибок, так как это описание, а не код.

**Рекомендации по улучшению**

1.  **Перевести описание в код**:  Разработать код на Python, который реализует правила игры, описанные в данном документе.
2.  **Использовать reStructuredText (RST)**: Если необходимо сохранить данный документ как RST, то нужно будет переформатировать все секции и комментарии, чтобы они соответствовали RST синтаксису.
3.  **Добавить логику игры**:  Реализовать основные игровые механики, включая случайное размещение кораблей, проверку попаданий и подсчет результатов.
4.  **Реализовать ввод данных**: Предусмотреть механизм ввода координат игроком и валидацию вводимых данных.
5.  **Обработка ошибок**: Добавить обработку ошибок, таких как некорректные координаты ввода.
6.  **Применить форматирование кода**: Используйте f-strings и `format` для форматирования сообщений и вывода результатов.
7.  **Использовать Docstrings**:  Документировать каждую функцию и класс с помощью docstrings в стиле reStructuredText (RST).

**Улучшенный код**

```python
"""
Модуль для реализации игры "Морской бой".
=========================================================================================

Этот модуль содержит класс :class:`BattleGame` для игры в морской бой.
Он отвечает за инициализацию игрового поля, размещение кораблей,
обработку выстрелов и подсчет результатов.

Пример использования
--------------------

Пример использования класса `BattleGame`:

.. code-block:: python

    game = BattleGame()
    game.play()
"""

import random
from typing import List, Tuple, Dict
from src.logger.logger import logger  # Импорт логгера #
import json # Импорт json для возможной обработки данных #
from src.utils.jjson import j_loads, j_loads_ns  # Импорт j_loads и j_loads_ns #


class BattleGame:
    """
    Класс, реализующий игру "Морской бой".

    :ivar board_size: Размер игрового поля (по умолчанию 6x6).
    :vartype board_size: int
    :ivar ships: Словарь, определяющий количество и размер кораблей.
    :vartype ships: dict
    :ivar board: Игровое поле, представленное как список списков.
    :vartype board: List[List[str]]
    :ivar hits: Количество попаданий.
    :vartype hits: int
    :ivar splashes: Количество промахов.
    :vartype splashes: int
    """
    def __init__(self, board_size: int = 6, ships: Dict[str, int] = None):
        """
        Инициализирует игру "Морской бой".

        :param board_size: Размер игрового поля.
        :param ships: Словарь с описанием кораблей (тип: размер).
        """
        self.board_size = board_size # Размер игрового поля #
        self.ships = ships or {  # Определение кораблей по умолчанию #
            'destroyer': 2,
            'cruiser': 3,
            'carrier': 4
        }
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]  # Создание игрового поля #
        self.hits = 0  # Инициализация счетчика попаданий #
        self.splashes = 0 # Инициализация счетчика промахов #
        self.place_ships()  # Размещение кораблей на поле #

    def place_ships(self):
        """
        Размещает корабли на игровом поле случайным образом.
        """
        for ship_type, ship_size in self.ships.items(): # Итерирование по кораблям #
            for _ in range(2): # Размещение по два корабля каждого типа #
                placed = False
                while not placed:
                    orientation = random.choice(['horizontal', 'vertical'])  # Выбор ориентации корабля #
                    if orientation == 'horizontal':
                        row = random.randint(0, self.board_size - 1)  # Выбор случайной строки #
                        col = random.randint(0, self.board_size - ship_size) # Выбор случайной колонки #
                        if all(self.board[row][col + i] == ' ' for i in range(ship_size)):
                             # Проверка, что место под корабль свободно #
                            for i in range(ship_size):
                                self.board[row][col + i] = 'O' # Размещение корабля #
                            placed = True
                    else:  # Вертикальное размещение
                        row = random.randint(0, self.board_size - ship_size) # Выбор случайной строки #
                        col = random.randint(0, self.board_size - 1)  # Выбор случайной колонки #
                        if all(self.board[row + i][col] == ' ' for i in range(ship_size)):
                            # Проверка, что место под корабль свободно #
                            for i in range(ship_size):
                                self.board[row + i][col] = 'O' # Размещение корабля #
                            placed = True

    def print_board(self):
        """
        Выводит текущее состояние игрового поля в консоль.
        """
        print("   " + "  ".join(str(i + 1) for i in range(self.board_size))) # Вывод номеров столбцов #
        for i, row in enumerate(self.board): # Итерирование по строкам #
            print(f"{i + 1}  " + "  ".join(row)) # Вывод строк #

    def check_hit(self, row: int, col: int) -> str:
        """
        Проверяет, было ли попадание в корабль.

        :param row: Номер строки выстрела.
        :param col: Номер колонки выстрела.
        :return: Строка 'Splash', 'Hit' или 'Sunk'.
        """
        if self.board[row][col] == 'O': # Проверка попадания в корабль #
            self.board[row][col] = 'X'  # Отмечаем попадание #
            self.hits += 1 # Увеличиваем счетчик попаданий #
            if self.is_sunk(row, col): # Проверяем, не потоплен ли корабль #
                return 'Sunk'
            return 'Hit'
        else:
            self.splashes += 1 # Увеличиваем счетчик промахов #
            return 'Splash'

    def is_sunk(self, row: int, col: int) -> bool:
        """
        Проверяет, потоплен ли корабль в результате попадания.

        :param row: Строка попадания.
        :param col: Колонка попадания.
        :return: True, если корабль потоплен, иначе False.
        """
        for i in range(self.board_size): # Проверка горизонтальных соседей #
            for j in range(self.board_size): # Проверка вертикальных соседей #
              if self.board[i][j] == 'O': # Проверка, остались ли неподбитые части корабля #
                 return False
        return True

    def game_over(self) -> bool:
       """
       Проверяет, окончена ли игра.

       :return: True, если все корабли потоплены, иначе False.
       """
       for row in self.board:
          if "O" in row: # Проверяем, остались ли неподбитые корабли на поле #
              return False
       return True

    def play(self):
        """
        Запускает игровой процесс.
        """
        print("Добро пожаловать в игру 'Морской бой'!")
        while not self.game_over():
            self.print_board() # Вывод игрового поля #
            try:
                coord_input = input("Введите координаты выстрела (например, 1,2): ")  # Запрос координат от игрока #
                col, row = map(int, coord_input.split(',')) # Разделение координат на столбец и строку #
                if 1 <= row <= self.board_size and 1 <= col <= self.board_size: # Проверка валидности ввода #
                    result = self.check_hit(row - 1, col - 1)  # Вызов функции проверки попадания #
                    print(f"Компьютер: {result}!") # Вывод результата выстрела #
                else:
                    logger.error('Некорректный ввод. Координаты должны быть в диапазоне от 1 до {self.board_size}')
                    print(f'Некорректный ввод. Координаты должны быть в диапазоне от 1 до {self.board_size}') # Сообщение об ошибке #
            except ValueError as e:
                 logger.error(f"Ошибка ввода координат: {e}")
                 print("Некорректный формат ввода. Пожалуйста, введите координаты в формате 'x,y'.") # Сообщение об ошибке #
        print("Игра окончена!")  # Вывод сообщения об окончании игры #
        print("Вы потопили все корабли противника!") # Вывод сообщения о победе #
        print("Итоговый счет:")  # Вывод результатов игры #
        print(f"Попаданий: {self.hits}") # Вывод количества попаданий #
        print(f"Промахов: {self.splashes}") # Вывод количества промахов #
        if self.splashes != 0:
            ratio = self.hits / self.splashes # Расчет соотношения промахов к попаданиям #
            print(f"Соотношение попаданий к промахам: {self.hits}/{self.splashes} ({ratio:.2f})")  # Вывод соотношения #
        else:
             print(f"Соотношение попаданий к промахам: {self.hits}/{self.splashes}") # Если нет промахов, выводим без деления #
        


if __name__ == '__main__':
    game = BattleGame()
    game.play()
```