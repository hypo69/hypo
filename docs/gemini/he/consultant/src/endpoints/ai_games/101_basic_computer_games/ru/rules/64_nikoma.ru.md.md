# Анализ кода модуля `64_nikoma.ru.md`

**Качество кода**
   - Соответствие требованиям к формату кода (1-10): 8
   - Преимущества:
      - Описание игры и пошаговые инструкции хорошо структурированы.
      - Приведены примеры работы программы, что облегчает понимание процесса игры.
      - Описаны ограничения и рекомендуемые улучшения.
   - Недостатки:
      - Отсутствует код на Python.
      - Документ содержит инструкции в формате markdown, а не reStructuredText.
      - Нет явного указания на использование `j_loads` или `j_loads_ns`.
      - Не хватает подробностей о структуре данных (классы, функции) для реализации.
      - Нет примеров кода с комментариями в стиле RST.

**Рекомендации по улучшению**
1. **Перевести markdown в reStructuredText:** Все комментарии и описания должны быть в формате reStructuredText (RST).
2. **Добавить Python код:** Необходимо предоставить пример кода на Python для реализации игры, а не только описание.
3. **Использовать `j_loads` или `j_loads_ns`**: Пока нет необходимости, но стоит указать это для будущего использования при работе с файлами.
4. **Структурировать код:** Код должен быть разделен на функции и классы для улучшения читаемости и поддержки.
5. **Добавить Docstring:** Все функции, методы и классы должны иметь docstring в формате RST.
6. **Обработка ошибок:** Включить обработку ошибок с использованием `logger.error` вместо стандартных блоков `try-except`.
7. **Комментирование:** Добавить комментарии к коду с использованием `#` с подробными объяснениями.
8. **Примеры кода:** Добавить примеры использования функций и классов в формате RST.

**Улучшенный код**
```markdown
# Анализ кода модуля `64_nikoma.ru.md`

**Качество кода**
   - Соответствие требованиям к формату кода (1-10): 3
   - Преимущества:
      - Описание игры и пошаговые инструкции хорошо структурированы.
      - Приведены примеры работы программы, что облегчает понимание процесса игры.
      - Описаны ограничения и рекомендуемые улучшения.
   - Недостатки:
      - Отсутствует код на Python.
      - Документ содержит инструкции в формате markdown, а не reStructuredText.
      - Нет явного указания на использование `j_loads` или `j_loads_ns`.
      - Не хватает подробностей о структуре данных (классы, функции) для реализации.
      - Нет примеров кода с комментариями в стиле RST.

**Рекомендации по улучшению**
1.  **Перевести markdown в reStructuredText:** Все комментарии и описания должны быть в формате reStructuredText (RST).
2.  **Добавить Python код:** Необходимо предоставить пример кода на Python для реализации игры, а не только описание.
3.  **Использовать `j_loads` или `j_loads_ns`**: Пока нет необходимости, но стоит указать это для будущего использования при работе с файлами.
4.  **Структурировать код:** Код должен быть разделен на функции и классы для улучшения читаемости и поддержки.
5.  **Добавить Docstring:** Все функции, методы и классы должны иметь docstring в формате RST.
6.  **Обработка ошибок:** Включить обработку ошибок с использованием `logger.error` вместо стандартных блоков `try-except`.
7.  **Комментирование:** Добавить комментарии к коду с использованием `#` с подробными объяснениями.
8.  **Примеры кода:** Добавить примеры использования функций и классов в формате RST.

**Улучшенный код**
```python
"""
Модуль для игры в NICOMA (Морской бой)
=========================================================================================

Модуль реализует игру NICOMA (Морской бой) с возможностью игры против компьютера или другого игрока.
Игра включает в себя размещение кораблей на поле, атаку противника и проверку попаданий.

Пример использования
--------------------
.. code-block:: python

    game = NicomaGame()
    game.start_game()
"""
from typing import List, Tuple, Optional
import random
from src.logger.logger import logger # импортируем логгер

class NicomaGame:
    """
    Класс для управления игрой NICOMA (Морской бой).

    :ivar player1_board: Игровое поле первого игрока.
    :vartype player1_board: List[List[str]]
    :ivar player2_board: Игровое поле второго игрока.
    :vartype player2_board: List[List[str]]
    :ivar player1_ships: Корабли первого игрока.
    :vartype player1_ships: List[List[Tuple[int, int]]]
    :ivar player2_ships: Корабли второго игрока.
    :vartype player2_ships: List[List[Tuple[int, int]]]
    :ivar game_mode: Режим игры (1 - одиночный, 2 - двухпользовательский).
    :vartype game_mode: int
    :ivar current_player: Текущий игрок (1 или 2).
    :vartype current_player: int
    """
    def __init__(self):
        """
        Инициализирует игру NICOMA.
        Создает игровые поля, корабли и устанавливает начальные значения.
        """
        self.player1_board: List[List[str]] = [[' ' for _ in range(10)] for _ in range(10)]
        # Создаем пустое игровое поле для первого игрока размером 10x10.
        self.player2_board: List[List[str]] = [[' ' for _ in range(10)] for _ in range(10)]
        # Создаем пустое игровое поле для второго игрока размером 10x10.
        self.player1_ships: List[List[Tuple[int, int]]] = []
        # Список кораблей первого игрока (каждый корабль - список координат).
        self.player2_ships: List[List[Tuple[int, int]]] = []
        # Список кораблей второго игрока (каждый корабль - список координат).
        self.game_mode: int = 0
        # Режим игры: 1 - одиночный, 2 - двухпользовательский.
        self.current_player: int = 1
        # Текущий игрок (1 или 2).

    def _print_board(self, board: List[List[str]]):
        """
        Выводит на экран игровое поле.

        :param board: Игровое поле для вывода.
        :type board: List[List[str]]
        """
        print('  | ' + ' | '.join(map(str, range(10))) + ' |') # Выводим заголовки столбцов
        print('---------------------------------------')
        for i, row in enumerate(board): # Итерируем по строкам поля
            print(f'{i} | ' + ' | '.join(row) + ' |') # Выводим каждую строку поля с номером

    def _place_ships(self, player_num: int) -> List[List[Tuple[int, int]]]:
        """
        Размещает корабли на игровом поле.

        :param player_num: Номер игрока (1 или 2).
        :type player_num: int
        :return: Список координат кораблей игрока.
        :rtype: List[List[Tuple[int, int]]]
        """
        ships: List[List[Tuple[int, int]]] = [] # Инициализируем пустой список кораблей
        board = self.player1_board if player_num == 1 else self.player2_board # Получаем поле текущего игрока
        print(f'Игрок {player_num}, разместите свои корабли:') # Сообщаем игроку о начале размещения
        ship_lengths = [3, 2, 2, 1, 1, 1, 1] # Список длин кораблей
        for length in ship_lengths: # Итерируем по длинам кораблей
            while True: # Бесконечный цикл для ввода координат до корректного
                try:
                    coords_str = input(f'Введите координаты для корабля длиной {length} (например, A1,A2): ') # Запрашиваем координаты
                    coords_list = [coord.strip().upper() for coord in coords_str.split(',')] # Разбиваем строку на координаты
                    if len(coords_list) != length:
                        print('Неверное количество координат. Пожалуйста, попробуйте еще раз.') # Проверяем количество координат
                        continue # Переходим к следующей итерации цикла while

                    coords: List[Tuple[int, int]] = [] # Инициализируем список координат
                    for coord in coords_list:
                        if len(coord) < 2:
                            raise ValueError()
                        row_str = coord[0] # Получаем буквенный номер строки
                        col_str = coord[1:] # Получаем номер столбца
                        if not row_str.isalpha() or not col_str.isdigit():
                            raise ValueError()
                        row = ord(row_str) - ord('A') # Преобразуем букву в номер строки
                        col = int(col_str) # Преобразуем строку в номер столбца
                        if not (0 <= row < 10 and 0 <= col < 10):
                            raise ValueError()
                        coords.append((row, col))  # добавляем координаты в список координат корабля
                    is_valid_ship = True
                    if len(coords) > 1: # Если длина корабля больше 1 клетки
                         if all(coord[0] == coords[0][0] for coord in coords): # проверка что корабль в одной строке
                            if any(abs(coords[i][1] - coords[i+1][1]) != 1 for i in range(len(coords)-1)): # Проверка что клетки последовательны
                                is_valid_ship = False
                         elif all(coord[1] == coords[0][1] for coord in coords): # проверка что корабль в одном столбце
                            if any(abs(coords[i][0] - coords[i+1][0]) != 1 for i in range(len(coords)-1)): # Проверка что клетки последовательны
                                is_valid_ship = False
                         else:
                            is_valid_ship = False # Если координаты не по прямой

                    if not is_valid_ship:
                         print('Корабль должен быть размещен по прямой линии.') # Выводим сообщение об ошибке
                         continue # Переходим к следующей итерации цикла while
                    if any(board[row][col] == 'X' for row,col in coords):
                        print('Корабль не должен пересекаться с другими кораблями') # Выводим сообщение об ошибке
                        continue # Переходим к следующей итерации цикла while
                    for row, col in coords:
                         board[row][col] = 'X'
                    ships.append(coords) # Добавляем корабль в список
                    break # Выходим из цикла, если все корректно
                except ValueError:
                    print('Неверный формат координат. Пожалуйста, попробуйте еще раз.') # Сообщение об ошибке ввода
            self._print_board(board) # Выводим игровое поле после размещения корабля
        return ships # Возвращаем список кораблей

    def _get_attack_coords(self, player_num: int) -> Tuple[int, int]:
        """
        Получает координаты атаки от игрока.

        :param player_num: Номер игрока (1 или 2).
        :type player_num: int
        :return: Координаты атаки (строка, столбец).
        :rtype: Tuple[int, int]
        """
        while True:
            try:
                coord_str = input(f'Игрок {player_num}, введите координаты для атаки (например, B5): ') # Запрашиваем координаты атаки
                coord_str = coord_str.strip().upper() # Удаляем пробелы и приводим к верхнему регистру
                if len(coord_str) < 2:
                    raise ValueError()
                row_str = coord_str[0] # Получаем букву строки
                col_str = coord_str[1:] # Получаем номер столбца
                if not row_str.isalpha() or not col_str.isdigit(): # Проверяем правильность формата
                    raise ValueError()
                row = ord(row_str) - ord('A') # Преобразуем букву в номер строки
                col = int(col_str) # Преобразуем номер столбца
                if not (0 <= row < 10 and 0 <= col < 10): # Проверяем что координаты в пределах поля
                    raise ValueError()
                return row, col # Возвращаем координаты
            except ValueError:
                 print('Неверный формат координат. Пожалуйста, попробуйте еще раз.') # Сообщение об ошибке

    def _computer_attack(self) -> Tuple[int, int]:
        """
        Генерирует случайные координаты атаки для компьютера.

        :return: Координаты атаки (строка, столбец).
        :rtype: Tuple[int, int]
        """
        row = random.randint(0, 9) # генерируем случайную строку
        col = random.randint(0, 9) # генерируем случайный столбец
        return row, col # возвращаем координаты

    def _process_attack(self, row: int, col: int, opponent_board: List[List[str]], opponent_ships: List[List[Tuple[int, int]]]) -> bool:
        """
        Обрабатывает атаку по заданным координатам.

        :param row: Строка атаки.
        :type row: int
        :param col: Столбец атаки.
        :type col: int
        :param opponent_board: Игровое поле противника.
        :type opponent_board: List[List[str]]
        :param opponent_ships: Корабли противника.
        :type opponent_ships: List[List[Tuple[int, int]]]
        :return: True если есть попадание, иначе False.
        :rtype: bool
        """
        if opponent_board[row][col] == 'X':  # проверка попадания
            opponent_board[row][col] = 'H'  # помечаем как подбитый корабль
            for ship in opponent_ships:  # итерируем по кораблям
                if (row, col) in ship:  # проверка на попадание в конкретный корабль
                    ship.remove((row, col)) # удаляем координаты корабля
                    if not ship: # если корабль уничтожен
                        print('Вы потопили корабль противника!') # сообщаем игроку об уничтожении корабля
                        opponent_ships.remove(ship) # удаляем корабль из списка кораблей
                        return True
                    print('Попадание! Корабль противника поврежден.') # сообщаем о попадании в корабль
                    return True
        else:
            opponent_board[row][col] = 'O' # если промах, то помечаем как промах
            print('Промах!')
            return False  # если промах

    def _is_game_over(self, ships: List[List[Tuple[int, int]]]) -> bool:
        """
        Проверяет, завершена ли игра.

        :param ships: Список кораблей игрока.
        :type ships: List[List[Tuple[int, int]]]
        :return: True если игра завершена, иначе False.
        :rtype: bool
        """
        return not ships # если корабли закончились, игра закончена

    def start_game(self):
        """
        Запускает игру NICOMA.
        """
        print('Добро пожаловать в NICOMA — Морское сражение!')  # приветствие
        print('Вы управляете флотом кораблей. Цель игры — уничтожить флот противника.') # правила игры
        print('Игра проводится на сетке размером 10x10.') # размер сетки
        while True:
            try:
                 self.game_mode = int(input('Выберите режим игры:\n1. Одиночный (против компьютера)\n2. Двухпользовательский\n> ')) # выбор режима игры
                 if self.game_mode not in [1, 2]: # проверка правильности ввода
                     raise ValueError
                 break
            except ValueError:
                 print('Некорректный ввод. Введите 1 или 2.') # Сообщение об ошибке
        self.player1_ships = self._place_ships(1) # размещаем корабли первого игрока
        if self.game_mode == 2:
           self.player2_ships = self._place_ships(2) # размещаем корабли второго игрока
        else:
            self.player2_ships = self._place_ships(2) # размещаем корабли второго игрока
        self.current_player = 1 # устанавливаем текущего игрока на первого

        while True: # основной цикл игры
            if self.current_player == 1: # если текущий игрок первый
                print('Ход игрока 1:')
                self._print_board(self.player2_board) # выводим поле противника
                row, col = self._get_attack_coords(1)  # получаем координаты атаки
                if self._process_attack(row, col, self.player2_board, self.player2_ships):
                    if self._is_game_over(self.player2_ships): # проверка на завершение игры
                        print('Все корабли противника уничтожены!') # Сообщаем о победе
                        print('Победитель: Игрок 1! Поздравляем с победой!')  # Выводим победителя
                        break
                else: # меняем игрока если промах
                    self.current_player = 2
            elif self.game_mode == 2: # если двухпользовательский режим
                print('Ход игрока 2:')
                self._print_board(self.player1_board)  # выводим поле противника
                row, col = self._get_attack_coords(2)   # получаем координаты атаки
                if self._process_attack(row, col, self.player1_board, self.player1_ships): # обрабатываем атаку
                    if self._is_game_over(self.player1_ships): # проверка на завершение игры
                        print('Все корабли противника уничтожены!') # Сообщаем о победе
                        print('Победитель: Игрок 2! Поздравляем с победой!') # Выводим победителя
                        break
                else: # меняем игрока если промах
                    self.current_player = 1

            else:  # если одиночный режим
                print('Ход компьютера:')
                row, col = self._computer_attack() # получаем координаты атаки от компьютера
                print(f'Компьютер атакует: {chr(ord("A") + row)}{col}') # выводим атаку компьютера
                if self._process_attack(row, col, self.player1_board, self.player1_ships): # обрабатываем атаку
                   if self._is_game_over(self.player1_ships): # проверка на завершение игры
                        print('Все корабли противника уничтожены!') # Сообщаем о победе
                        print('Победитель: Компьютер! Поздравляем с победой!')  # Выводим победителя
                        break
                else: # меняем игрока если промах
                    self.current_player = 1

        while True:
            play_again = input('Хотите сыграть снова? (да/нет): ').strip().lower() # запрос на новую игру
            if play_again == 'да': # если да, то начинаем новую игру
                self.__init__() # сбрасываем игру
                self.start_game() # запускаем заново
                break
            elif play_again == 'нет': # если нет, то заканчиваем игру
                print('Спасибо за игру!')
                break
            else:
                print('Некорректный ввод. Введите "да" или "нет".') # Сообщение об ошибке


if __name__ == '__main__':
    game = NicomaGame() # создаем экземпляр игры
    game.start_game() # запускаем игру

```
```python
# -*- coding: utf-8 -*-
"""
Модуль для игры в NICOMA (Морской бой)
=========================================================================================

Модуль реализует игру NICOMA (Морской бой) с возможностью игры против компьютера или другого игрока.
Игра включает в себя размещение кораблей на поле, атаку противника и проверку попаданий.

Пример использования
--------------------
.. code-block:: python

    game = NicomaGame()
    game.start_game()
"""
from typing import List, Tuple, Optional
import random
from src.logger.logger import logger # импортируем логгер

class NicomaGame:
    """
    Класс для управления игрой NICOMA (Морской бой).

    :ivar player1_board: Игровое поле первого игрока.
    :vartype player1_board: List[List[str]]
    :ivar player2_board: Игровое поле второго игрока.
    :vartype player2_board: List[List[str]]
    :ivar player1_ships: Корабли первого игрока.
    :vartype player1_ships: List[List[Tuple[int, int]]]
    :ivar player2_ships: Корабли второго игрока.
    :vartype player2_ships: List[List[Tuple[int, int]]]
    :ivar game_mode: Режим игры (1 - одиночный, 2 - двухпользовательский).
    :vartype game_mode: int
    :ivar current_player: Текущий игрок (1 или 2).
    :vartype current_player: int
    """
    def __init__(self):
        """
        Инициализирует игру NICOMA.
        Создает игровые поля, корабли и устанавливает начальные значения.
        """
        self.player1_board: List[List[str]] = [[' ' for _ in range(10)] for _ in range(10)]
        # Создаем пустое игровое поле для первого игрока размером 10x10.
        self.player2_board: List[List[str]] = [[' ' for _ in range(10)] for _ in range(10)]
        # Создаем пустое игровое поле для второго игрока размером 10x10.
        self.player1_ships: List[List[Tuple[int, int]]] = []
        # Список кораблей первого игрока (каждый корабль - список координат).
        self.player2_ships: List[List[Tuple[int, int]]] = []
        # Список кораблей второго игрока (каждый корабль - список координат).
        self.game_mode: int = 0
        # Режим игры: 1 - одиночный, 2 - двухпользовательский.
        self.current_player: int = 1
        # Текущий игрок (1 или 2).

    def _print_board(self, board: List[List[str]]):
        """
        Выводит на экран игровое поле.

        :param board: Игровое поле для вывода.
        :type board: List[List[str]]
        """
        print('  | ' + ' | '.join(map(str, range(10))) + ' |') # Выводим заголовки столбцов
        print('---------------------------------------')
        for i, row in enumerate(board): # Итерируем по строкам поля
            print(f'{i} | ' + ' | '.join(row) + ' |') # Выводим каждую строку поля с номером

    def _place_ships(self, player_num: int) -> List[List[Tuple[int, int]]]:
        """
        Размещает корабли на игровом поле.

        :param player_num: Номер игрока (1 или 2).
        :type player_num: int
        :return: Список координат кораблей игрока.
        :rtype: List[List[Tuple[int, int]]]
        """
        ships: List[List[Tuple[int, int]]] = [] # Инициализируем пустой список кораблей
        board = self.player1_board if player_num == 1 else self.player2_board # Получаем поле текущего игрока
        print(f'Игрок {player_num}, разместите свои корабли:') # Сообщаем игроку о начале размещения
        ship_lengths = [3, 2, 2, 1, 1, 1, 1] # Список длин кораблей
        for length in ship_lengths: # Итерируем по длинам кораблей
            while True: # Бесконечный цикл для ввода координат до корректного
                try:
                    coords_str = input(f'Введите координаты для корабля длиной {length} (например, A1,A2): ') # Запрашиваем координаты
                    coords_list = [coord.strip().upper() for coord in coords_str.split(',')] # Разбиваем строку на координаты
                    if len(coords_list) != length:
                        print('Неверное количество координат. Пожалуйста, попробуйте еще раз.') # Проверяем количество координат
                        continue # Переходим к следующей итерации цикла while

                    coords: List[Tuple[int, int]] = [] # Инициализируем список координат
                    for coord in coords_list:
                        if len(coord) < 2:
                            raise ValueError()
                        row_str = coord[0] # Получаем буквенный номер строки
                        col_str = coord[1:] # Получаем номер столбца
                        if not row_str.isalpha() or not col_str.isdigit():
                            raise ValueError()
                        row = ord(row_str) - ord('A') # Преобразуем букву в номер строки
                        col = int(col_str) # Преобразуем строку в номер столбца
                        if not (0 <= row < 10 and 0 <= col < 10):
                            raise ValueError()
                        coords.append((row, col))  # добавляем координаты в список координат корабля
                    is_valid_ship = True
                    if len(coords) > 1: # Если длина корабля больше 1 клетки
                         if all(coord[0] == coords[0][0] for coord in coords): # проверка что корабль в одной строке
                            if any(abs(coords[i][1] - coords[i+1][1]) != 1 for i in range(len(coords)-1)): # Проверка что клетки последовательны
                                is_valid_ship = False
                         elif all(coord[1] == coords[0][1] for coord in coords): # проверка что корабль в одном столбце
                            if any(abs(coords[i][0] - coords[i+1][0]) != 1 for i in range(len(coords)-1)): # Проверка что клетки последовательны
                                is_valid_ship = False
                         else:
                            is_valid_ship = False # Если координаты не по прямой

                    if not is_valid_ship:
                         print('Корабль должен быть размещен по прямой линии.') # Выводим сообщение об ошибке
                         continue # Переходим к следующей итерации цикла while
                    if any(board[row][col] == 'X' for row,col in coords):
                        print('Корабль не должен пересекаться с другими кораблями') # Выводим сообщение об ошибке
                        continue # Переходим к следующей итерации цикла while
                    for row, col in coords:
                         board[row][col] = 'X'
                    ships.append(coords) # Добавляем корабль в список
                    break # Выходим из цикла, если все корректно
                except ValueError:
                    print('Неверный формат координат. Пожалуйста, попробуйте еще раз.') # Сообщение об ошибке ввода
            self._print_board(board) # Выводим игровое поле после размещения корабля
        return ships # Возвращаем список кораблей

    def _get_attack_coords(self, player_num: int) -> Tuple[int, int]:
        """
        Получает координаты атаки от игрока.

        :param player_num: Номер игрока (1 или 2).
        :type player_num: int
        :return: Координаты атаки (строка, столбец).
        :rtype: Tuple[int, int]
        """
        while True:
            try:
                coord_str = input(f'Игрок {player_num}, введите координаты для атаки (например, B5): ') # Запрашиваем координаты атаки
                coord_str = coord_str.strip().upper() # Удаляем пробелы и приводим к верхнему регистру
                if len(coord_str) < 2:
                    raise ValueError()
                row_str = coord_str[0] # Получаем букву строки
                col_str = coord_str[1:] # Получаем номер столбца
                if not row_str.isalpha() or not col_str.isdigit(): # Проверяем правильность формата
                    raise ValueError()
                row = ord(row_str) - ord('A') # Преобразуем букву в номер строки
                col = int(col_str) # Преобразуем номер столбца
                if not (0 <= row < 10 and 0 <= col < 10): # Проверяем что координаты в пределах поля
                    raise ValueError()
                return row, col # Возвращаем координаты
            except ValueError:
                 print('Неверный формат координат. Пожалуйста, попробуйте еще раз.') # Сообщение об ошибке

    def _computer_attack(self) -> Tuple[int, int]:
        """
        Генерирует случайные координаты атаки для компьютера.

        :return: Координаты атаки (строка, столбец).
        :rtype: Tuple[int, int]
        """
        row = random.randint(0, 9) # генерируем случайную строку
        col = random.randint(0, 9) # генерируем случайный столбец
        return row, col # возвращаем координаты

    def _process_attack(self, row: int, col: int, opponent_board: List[List[str]], opponent_ships: List[List[Tuple[int, int]]]) -> bool:
        """
        Обрабатывает атаку по заданным координатам.

        :param row: Строка атаки.
        :type row: int
        :param col: Столбец атаки.
        :type col: int
        :param opponent_board: Игровое поле противника.
        :type opponent_board: List[List[str]]
        :param opponent_ships: Корабли противника.
        :type opponent_ships: List[List[Tuple[int, int]]]
        :return: True если есть попадание, иначе False.
        :rtype: bool
        """
        if opponent_board[row][col] == 'X':  # проверка попадания
            opponent_board[row][col] = 'H'  # помечаем как подбитый корабль
            for ship in opponent_ships:  # итерируем по кораблям
                if (row, col) in ship:  # проверка на попадание в конкретный корабль
                    ship.remove((row, col)) # удаляем координаты корабля
                    if not ship: # если корабль уничтожен
                        print('Вы потопили корабль противника!') # сообщаем игроку об уничтожении корабля
                        opponent_ships.remove(ship) # удаляем корабль из списка кораблей
                        return True
                    print('Попадание! Корабль противника поврежден.') # сообщаем о попадании в корабль
                    return True
        else:
            opponent_board[row][col] = 'O' # если промах, то помечаем как промах
            print('Промах!')
            return False  # если промах

    def _is_game_over(self, ships: List[List[Tuple[int, int]]]) -> bool:
        """
        Проверяет, завершена ли игра.

        :param ships: Список кораблей игрока.
        :type ships: List[List[Tuple[int, int]]]
        :return: True если игра завершена, иначе False.
        :rtype: bool
        """
        return not ships # если корабли закончились, игра закончена

    def start_game(self):
        """
        Запускает игру NICOMA.
        """
        print('Добро пожаловать в NICOMA — Морское сражение!')  # приветствие
        print('Вы управляете флотом кораблей. Цель игры — уничтожить флот противника.') # правила игры
        print('Игра проводится на сетке размером 10x10.') # размер сетки
        while True:
            try:
                 self.game_mode = int(input('Выберите режим игры:\n1. Одиночный (против компьютера)\n2. Двухпользовательский\n> ')) # выбор режима игры
                 if self.game_mode not in [1, 2]: # проверка правильности ввода
                     raise ValueError
                 break
            except ValueError:
                 print('Некорректный ввод. Введите 1 или 2.') # Сообщение об ошибке
        self.player1_ships = self._place_ships(1) # размещаем корабли первого игрока
        if self.game_mode == 2:
           self.player2_ships = self._place_ships(2) # размещаем корабли второго игрока
        else:
            self.player2_ships = self._place_ships(2) # размещаем корабли второго игрока
        self.current_player = 1 # устанавливаем текущего игрока на первого

        while True: # основной цикл игры
            if self.current_player == 1: # если текущий игрок первый
                print('Ход игрока 1:')
                self._print_board(self.player2_board) # выводим поле противника
                row, col = self._get_attack_coords(1)  # получаем координаты атаки
                if self._process_attack(row, col, self.player2_board, self.player2_ships):
                    if self._is_game_over(self.player2_ships): # проверка на завершение игры
                        print('Все корабли противника уничтожены!') # Сообщаем о победе
                        print('Победитель: Игрок 1! Поздравляем с победой!')  # Выводим победителя
                        break
                else: # меняем игрока если промах
                    self.current_player = 2
            elif self.game_mode == 2: # если двухпользовательский режим