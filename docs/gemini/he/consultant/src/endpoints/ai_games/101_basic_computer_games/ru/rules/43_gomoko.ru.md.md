# Анализ кода модуля `43_gomoko.ru.md`

**Качество кода**

-   **Соответствие требованиям к формату кода (1-10):** 
    - **Плюсы:**
         - Документ хорошо структурирован и понятен для пользователя.
         - Описание игры, пошаговая инструкция, пример работы, ограничения и рекомендации по реализации представлены чётко.
         - Использование Markdown позволяет легко воспринимать текст.
    - **Минусы:**
        - Код не содержит reStructuredText (RST) для комментариев.
        - Отсутствует реализация на Python, только описание.
        - Нет использования `src.utils.jjson`, `src.logger.logger`.
        - Нет примеров использования функций, нет структуры модуля, классов и методов.
        - Описание является текстовым, а не кодом.

**Рекомендации по улучшению**

1.  **Перевести** текстовое описание в исполняемый код Python.
2.  **Создать** структуру модуля: создать класс для игры, методы для ходов, проверки победы и т.д.
3.  **Добавить** обработку ошибок с использованием `src.logger.logger`.
4.  **Использовать**  `src.utils.jjson` для загрузки данных, если необходимо.
5.  **Реализовать** базовую игровую логику для GOMOKO.
6.  **Добавить** примеры reStructuredText (RST) для функций и классов.

**Улучшенный код**

```python
"""
Модуль для игры Гомоку (GOMOKO)
=================================

Модуль содержит класс GomokuGame для реализации логики игры Гомоку.
Игра ведется на поле 15x15, игроки поочередно ставят свои фишки
(обычно черные и белые). Цель - составить линию из пяти фишек по
вертикали, горизонтали или диагонали.

Пример использования:
--------------------

.. code-block:: python

    game = GomokuGame()
    game.play()

"""
from src.logger.logger import logger #  Импортируем logger для логирования ошибок
import random # Импортируем модуль random для случайных ходов компьютера

class GomokuGame:
    """
    Класс для управления игрой Гомоку.

    :ivar board: Представляет игровое поле в виде двумерного списка.
    :vartype board: list[list[str]]
    :ivar current_player: Символ текущего игрока ('X' или 'O').
    :vartype current_player: str
    :ivar board_size: Размер игрового поля (15x15).
    :vartype board_size: int
    """
    def __init__(self, board_size: int = 15):
        """
        Инициализирует игру Гомоку.

        :param board_size: Размер игрового поля.
        :type board_size: int
        """
        self.board_size = board_size # Сохраняем размер игрового поля
        self.board = [['.' for _ in range(board_size)] for _ in range(board_size)] # Создаем пустое игровое поле
        self.current_player = 'X' #  Начинаем с игрока 'X'

    def print_board(self):
        """
        Выводит текущее состояние игрового поля в консоль.
        """
        # Выводим координаты столбцов
        print("  " + " ".join(chr(65 + i) for i in range(self.board_size)))
        for i, row in enumerate(self.board): # Проходим по строкам игрового поля
            print(f"{i+1:2} {' '.join(row)}")  #  Выводим номер строки и саму строку

    def is_valid_move(self, row: int, col: int) -> bool:
        """
        Проверяет, является ли ход в данную клетку допустимым.

        :param row: Номер строки хода.
        :type row: int
        :param col: Номер столбца хода.
        :type col: int
        :return: True если ход допустим, иначе False.
        :rtype: bool
        """
        if 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == '.': #  Проверяем, что клетка находится в пределах доски и не занята
            return True
        return False

    def make_move(self, row: int, col: int):
        """
        Выполняет ход игрока на доске.

        :param row: Номер строки хода.
        :type row: int
        :param col: Номер столбца хода.
        :type col: int
        """
        self.board[row][col] = self.current_player #  Ставим фишку текущего игрока в выбранную клетку

    def check_winner(self, row: int, col: int) -> bool:
        """
        Проверяет, есть ли победитель после последнего хода.

        :param row: Номер строки последнего хода.
        :type row: int
        :param col: Номер столбца последнего хода.
        :type col: int
        :return: True если есть победитель, иначе False.
        :rtype: bool
        """
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # Все возможные направления для проверки
        for dr, dc in directions: # Проходим по всем направлениям
            count = 1 # Считаем количество фишек в линии
            # Проверяем в одну сторону от хода
            for i in range(1, 5): # Проверяем 4 клетки в направлении
                nr, nc = row + dr * i, col + dc * i # Вычисляем новые координаты
                if 0 <= nr < self.board_size and 0 <= nc < self.board_size and self.board[nr][nc] == self.current_player: # Проверяем, что координаты в пределах доски и фишка та же
                   count += 1 # Увеличиваем счетчик
                else:
                    break

            # Проверяем в другую сторону от хода
            for i in range(1, 5): # Проверяем 4 клетки в направлении
                nr, nc = row - dr * i, col - dc * i # Вычисляем новые координаты
                if 0 <= nr < self.board_size and 0 <= nc < self.board_size and self.board[nr][nc] == self.current_player: # Проверяем, что координаты в пределах доски и фишка та же
                    count += 1
                else:
                    break
            if count >= 5:  # Если есть 5 фишек в ряд
                return True
        return False

    def switch_player(self):
        """
        Переключает текущего игрока.
        """
        self.current_player = 'O' if self.current_player == 'X' else 'X' # Меняем текущего игрока

    def get_player_move(self) -> tuple[int, int]:
        """
        Запрашивает ввод хода от игрока.

        :return: Координаты хода в виде кортежа (row, col).
        :rtype: tuple[int, int]
        """
        while True: # Запрашиваем ввод пока не получим валидный ход
            try:
                move = input(f"Игрок {self.current_player}, введите ход (например, D4): ").strip().upper() #  Запрашиваем ход у игрока
                if len(move) < 2:
                    print("Неверный формат хода. Пример: D4")
                    continue #  Если формат хода неверный, запрашиваем ввод снова

                col = ord(move[0]) - ord('A')  # Преобразуем букву столбца в число
                row = int(move[1:]) - 1  # Преобразуем номер строки в число

                if self.is_valid_move(row, col): # Проверяем валидность хода
                     return row, col # Возвращаем координаты
                else:
                    print("Недопустимый ход. Попробуйте еще раз.") # Выводим сообщение, если ход недопустимый
            except (ValueError, IndexError) as ex:
                logger.error('Неверный формат ввода хода.', ex) # Регистрируем ошибку, если ввод некорректен
                print("Неверный формат хода. Пример: D4")

    def get_computer_move(self) -> tuple[int, int]:
        """
        Генерирует случайный ход для компьютера.

        :return: Координаты хода в виде кортежа (row, col).
        :rtype: tuple[int, int]
        """
        while True: # Ищем свободную клетку
            row = random.randint(0, self.board_size - 1) # Генерируем случайную строку
            col = random.randint(0, self.board_size - 1) # Генерируем случайный столбец
            if self.is_valid_move(row, col):
                return row, col # Возвращаем координаты, если клетка свободна

    def play(self):
        """
        Основной метод для запуска игры.
        """
        print("Добро пожаловать в игру GOMOKO!") # Выводим приветствие
        player_choice = input("Выберите цвет фишек (черные - X, белые - O): ").strip().upper() # Запрашиваем выбор цвета фишек
        if player_choice == 'O':
              self.current_player = 'O'
        while True:
            self.print_board() #  Выводим игровое поле
            if self.current_player == 'X':
                row, col = self.get_player_move() # Получаем ход от игрока
            else:
                print("Ход компьютера:") # Указываем, что ход компьютера
                row, col = self.get_computer_move() # Получаем ход от компьютера

            self.make_move(row, col)  #  Делаем ход
            if self.check_winner(row, col): # Проверяем победителя
                self.print_board() #  Выводим поле
                print(f"Игрок {self.current_player} победил!") #  Выводим сообщение о победе
                break # Завершаем игру

            if all(cell != '.' for row in self.board for cell in row): # Проверяем, не заполнено ли поле
                self.print_board()
                print("Ничья!") # Выводим сообщение о ничьей
                break  # Завершаем игру

            self.switch_player() #  Переключаем игрока
        if input("Хотите сыграть снова? (да/нет): ").lower() == 'да':
            self.__init__(self.board_size)
            self.play() # Начинаем новую игру

if __name__ == "__main__":
    game = GomokuGame() # Создаем объект игры
    game.play() # Запускаем игру
```