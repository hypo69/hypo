# Анализ кода модуля `59_life_2.ru.md`

**Качество кода**
-   **Соответствие требованиям к формату кода (1-10):** 7
    -   **Преимущества:**
        -   Документ предоставляет четкое и структурированное описание правил игры "LIFE-2".
        -   Приведены подробные пошаговые инструкции для реализации игры.
        -   Есть примеры работы программы, которые помогают понять игровой процесс.
    -   **Недостатки:**
        -   Отсутствует код на Python.
        -   Формат документа - markdown, а не reStructuredText (RST).
        -   Нет описания работы с `j_loads` или `j_loads_ns` для чтения файлов.
        -   Нет описания импортов.
        -   Нет комментариев в стиле RST для функций и классов.

**Рекомендации по улучшению**

1.  **Формат документа:** Перевести документ в формат reStructuredText (RST) для соответствия требованиям.
2.  **Код на Python:** Добавить код на Python, реализующий логику игры, с использованием массивов/списков для представления игрового поля и функций для обработки правил игры.
3.  **Чтение данных:** Если предполагается использование JSON для хранения данных, использовать `j_loads` или `j_loads_ns` из `src.utils.jjson`.
4.  **Импорты:** Добавить необходимые импорты в начало кода, например, для работы с JSON и логгированием ошибок.
5.  **Комментарии:** Добавить подробные комментарии в формате RST для всех функций, методов и классов.
6.  **Логирование:** Использовать `from src.logger.logger import logger` для регистрации ошибок.
7.  **Обработка ошибок:** Избегать чрезмерного использования `try-except`, предпочитать `logger.error` для регистрации ошибок.

**Улучшенный код**

```python
"""
Модуль для реализации игры "LIFE-2" - двухпользовательской адаптации игры "Жизнь".
===============================================================================

Этот модуль предоставляет реализацию игры "LIFE-2", где два игрока размещают клетки на поле 5x5,
стремясь уничтожить клетки противника, следуя правилам, аналогичным классической игре "Жизнь".

Пример использования
--------------------

.. code-block:: python

    game = Life2Game()
    game.start_game()
"""

from typing import List, Tuple
from src.logger.logger import logger # Импорт логгера для записи ошибок
from src.utils.jjson import j_loads # Импорт j_loads для чтения JSON файлов (если нужно)

class Life2Game:
    """
    Класс для управления игрой "LIFE-2".

    :ivar board: Игровое поле в виде списка списков, где '*' - клетки игрока 1, '#' - клетки игрока 2, '.' - пустые клетки.
    :vartype board: List[List[str]]
    :ivar size: Размер игрового поля (по умолчанию 5x5).
    :vartype size: int
    :ivar player1_symbol: Символ для клеток первого игрока.
    :vartype player1_symbol: str
    :ivar player2_symbol: Символ для клеток второго игрока.
    :vartype player2_symbol: str
    """
    def __init__(self, size: int = 5):
        """
        Инициализирует игру "LIFE-2" с заданным размером игрового поля.

        :param size: Размер игрового поля (по умолчанию 5).
        :type size: int
        """
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.player1_symbol = '*'
        self.player2_symbol = '#'

    def print_board(self):
        """
        Выводит текущее состояние игрового поля.
        """
        print("  ", end="")
        for i in range(1, self.size + 1):
            print(f"{i} ", end="") # Вывод номеров столбцов
        print()
        for i, row in enumerate(self.board):
            print(f"{i+1} ", end="") # Вывод номеров строк
            print("  ".join(row)) # Вывод содержимого строк

    def place_initial_cells(self, player: int) -> None:
        """
        Размещает начальные клетки для заданного игрока.

        :param player: Номер игрока (1 или 2).
        :type player: int
        """
        player_symbol = self.player1_symbol if player == 1 else self.player2_symbol
        print(f"Игрок {player} размещает 3 клетки. Введите координаты:")
        placed_cells = 0
        while placed_cells < 3:
            try:
                coords_str = input(f"Клетка {placed_cells + 1} (строка, столбец): ")
                row, col = map(int, coords_str.split(","))
                if not (1 <= row <= self.size and 1 <= col <= self.size):
                    print("Некорректные координаты. Попробуйте еще раз.")
                    continue
                row -= 1
                col -= 1
                if self.board[row][col] != '.':
                    print("Эта клетка уже занята. Попробуйте другую.")
                    continue
                self.board[row][col] = player_symbol
                placed_cells += 1
            except Exception as e: # Ловим ошибки при вводе координат
                logger.error("Ошибка ввода координат", exc_info=True) # Логируем ошибку
                print("Неверный формат ввода. Попробуйте еще раз (формат: строка,столбец).")

    def get_neighbors_count(self, row: int, col: int) -> dict:
        """
        Определяет количество соседей каждого типа для заданной клетки.

        :param row: Номер строки клетки.
        :type row: int
        :param col: Номер столбца клетки.
        :type col: int
        :return: Словарь с количеством соседей каждого типа ('*' и '#').
        :rtype: dict
        """
        neighbors = {'*': 0, '#': 0}
        for i in range(max(0, row - 1), min(row + 2, self.size)):
            for j in range(max(0, col - 1), min(col + 2, self.size)):
                if (i, j) != (row, col):
                    if self.board[i][j] == self.player1_symbol:
                        neighbors['*'] += 1
                    elif self.board[i][j] == self.player2_symbol:
                        neighbors['#'] += 1
        return neighbors

    def update_board(self) -> None:
        """
        Обновляет состояние игрового поля, применяя правила игры "LIFE-2".
        """
        new_board = [['.' for _ in range(self.size)] for _ in range(self.size)]
        for row in range(self.size):
            for col in range(self.size):
                neighbors = self.get_neighbors_count(row, col)
                cell_value = self.board[row][col]

                if cell_value != '.': # Клетка жива
                    if neighbors['*'] + neighbors['#'] in (2, 3):
                         new_board[row][col] = cell_value # Клетка выживает
                elif neighbors['*'] + neighbors['#'] == 3:  # Пустая клетка, может родиться новая
                     if neighbors['*'] > neighbors['#']:
                         new_board[row][col] = self.player1_symbol
                     elif neighbors['#'] > neighbors['*']:
                         new_board[row][col] = self.player2_symbol

        self.board = new_board # Обновление текущего поля

    def add_cell(self, player: int) -> None:
         """
         Добавляет клетку на поле для заданного игрока.

         :param player: Номер игрока (1 или 2).
         :type player: int
         """
         player_symbol = self.player1_symbol if player == 1 else self.player2_symbol # Определяем символ игрока
         while True:
              try:
                  coords_str = input(f"Игрок {player}, введите координаты клетки (строка, столбец): ") # Получение координат от игрока
                  row, col = map(int, coords_str.split(',')) # Разделение и преобразование координат
                  if not (1 <= row <= self.size and 1 <= col <= self.size): # Проверка валидности координат
                      print("Некорректные координаты. Попробуйте еще раз.") # Сообщение об ошибке, если координаты не валидны
                      continue # Повторный запрос ввода
                  row -= 1 # Коррекция индексов, так как начинаем с 0
                  col -= 1
                  if self.board[row][col] != '.': # Проверка занятости клетки
                      print("Эта клетка уже занята. Попробуйте другую.") # Сообщение об ошибке, если клетка занята
                      continue # Повторный запрос ввода
                  self.board[row][col] = player_symbol # Установка символа игрока на доску
                  break # Выход из цикла если все корректно
              except Exception as e: # Обработка ошибок ввода
                  logger.error("Ошибка ввода координат", exc_info=True) # Логирование ошибки
                  print("Неверный формат ввода. Попробуйте еще раз (формат: строка,столбец).") # Сообщение об ошибке

    def check_winner(self) -> int:
        """
        Проверяет наличие победителя в игре.

        :return: 0, если нет победителя, 1, если победил игрок 1, 2, если победил игрок 2.
        :rtype: int
        """
        player1_alive = any(self.player1_symbol in row for row in self.board) # Проверяем наличие клеток игрока 1
        player2_alive = any(self.player2_symbol in row for row in self.board) # Проверяем наличие клеток игрока 2
        if not player1_alive: # Если у первого игрока нет клеток
            return 2  # Победил второй игрок
        if not player2_alive: # Если у второго игрока нет клеток
            return 1  # Победил первый игрок
        return 0  # Нет победителя

    def start_game(self):
        """
        Запускает игру "LIFE-2".
        """
        print("Добро пожаловать в LIFE-2 — двухпользовательскую адаптацию Игры жизни!") # Приветствие
        print("Игроки по очереди будут размещать клетки на поле 5x5.") # Инструкция
        print("Цель игры — уничтожить клетки соперника, следуя правилам жизни. Удачи!") # Мотивация

        self.place_initial_cells(1) # Начальное размещение клеток для первого игрока
        self.print_board() # Вывод текущей доски
        self.place_initial_cells(2) # Начальное размещение клеток для второго игрока
        self.print_board() # Вывод текущей доски

        winner = 0 # Инициализируем победителя
        while winner == 0: # Игровой цикл, пока нет победителя
            self.add_cell(1) # Добавление клетки для первого игрока
            self.update_board() # Обновление состояния доски
            self.print_board() # Вывод текущей доски
            winner = self.check_winner() # Проверка победителя
            if winner != 0: # Проверка если есть победитель
                break # Выход из цикла если есть победитель
            self.add_cell(2) # Добавление клетки для второго игрока
            self.update_board() # Обновление состояния доски
            self.print_board() # Вывод текущей доски
            winner = self.check_winner() # Проверка победителя
        print(f"Победитель: Игрок {winner}!") # Вывод победителя

if __name__ == "__main__":
    game = Life2Game() # Создаем экземпляр класса игры
    game.start_game() # Запускаем игру
```