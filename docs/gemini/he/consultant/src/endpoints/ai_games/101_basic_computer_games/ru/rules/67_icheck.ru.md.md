# Анализ кода модуля ICHECK

**Качество кода**
-  Соответствие требованиям к формату кода (с 1 по 10):
    -  Преимущества:
        -  Текст представляет собой подробное описание игры "ICHECK" в формате Markdown.
        -  Дано четкое описание правил, процесса игры, и возможных ограничений.
        -  Приведен пример работы программы, что помогает понять ход игры.
        -  Описаны рекомендации по реализации и улучшению игры.
    -  Недостатки:
        -  Код не содержит исполняемого Python кода.
        -  Отсутствуют docstring и комментарии в стиле reStructuredText (RST).
        -  Нет импортов и функций.
        -  Не используется `j_loads` или `j_loads_ns` для обработки данных.
        -  Не используется `logger.error` для обработки ошибок.

**Рекомендации по улучшению**

1. **Переход на Python:** Начать реализацию игры на Python, используя классы и функции для представления доски, шашек и логики игры.
2. **Структурированный код:** Разделить код на модули и функции, например, для инициализации игры, хода игрока, проверки правил и т.д.
3. **Обработка ошибок:** Добавить обработку ошибок, используя `try-except` блоки и `logger.error` для регистрации ошибок.
4. **Использование jjson:** Использовать `j_loads` или `j_loads_ns` для загрузки данных, если это необходимо.
5. **Формат RST:** Добавить docstring в формате RST для всех функций, классов и методов.
6. **Комментарии:** Добавить подробные комментарии к коду, чтобы пояснить логику.
7. **Тестирование:** Провести тестирование кода, чтобы проверить его корректность и соответствие требованиям.
8. **Использование `logger`:**  Использовать `from src.logger.logger import logger` для записи логов.

**Улучшенный код**

```python
"""
Модуль для реализации игры в шашки ICHECK
==========================================================

Этот модуль содержит реализацию игры в шашки ICHECK,
включая инициализацию доски, логику ходов и проверку
условий победы.

Пример использования:
--------------------
   
.. code-block:: python

    game = ICheckGame()
    game.start_game()
"""
from typing import List, Tuple, Optional, Any # Импорт необходимых типов
from src.logger.logger import logger # импорт logger

class ICheckGame:
    """
    Класс для управления игрой ICHECK.

    :ivar board: Представление доски в виде двумерного списка.
    :vartype board: List[List[Optional[str]]]
    :ivar current_player: Текущий игрок ('white' или 'black').
    :vartype current_player: str
    """
    def __init__(self):
        """
        Инициализирует игру ICHECK, создавая доску и устанавливая начальные значения.
        """
        self.board: List[List[Optional[str]]] = self._create_board() # Создание доски
        self.current_player = 'white' # Первый игрок - белые

    def _create_board(self) -> List[List[Optional[str]]]:
        """
        Создает начальную доску для игры.
        
        :return: Двумерный список, представляющий доску.
        :rtype: List[List[Optional[str]]]
        """
        board = [[None for _ in range(8)] for _ in range(8)] # Инициализация доски пустыми клетками
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    board[row][col] = 'black' # Заполнение черными шашками в начале игры
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                     board[row][col] = 'white' # Заполнение белыми шашками в начале игры
        return board

    def start_game(self):
        """
        Запускает игру и управляет процессом игры, пока не будет победителя.
        """
        print('Добро пожаловать в ICHECK!')
        print('Ваша задача — удалить как можно больше шашек соперника, совершая диагональные прыжки.')
        print('Игра продолжается до тех пор, пока у одного из игроков не останется шашек или не будет возможных ходов.')
        print('Удачи!')
        self.print_board() # Вывод доски в начале игры

        while True:
            self.player_turn() # Ход игрока
            if self.check_game_over(): # Проверка на завершение игры
                self.end_game() # Завершение игры
                break
            self.switch_player() # Переход хода

    def print_board(self):
        """
        Выводит текущее состояние доски в консоль.
        """
        for row in self.board:
            print(' '.join(str(piece) if piece else '-' for piece in row))

    def player_turn(self):
        """
        Обрабатывает ход текущего игрока.
        """
        while True:
             try:
                start_pos_str, end_pos_str = input(f'{self.current_player.capitalize()}, ваш ход. Введите координаты шашки и клетки, куда хотите переместить её (например, A1 B2): ').split() # Получение ввода игрока
                start_pos = self.parse_position(start_pos_str) # Обработка начала позиции
                end_pos = self.parse_position(end_pos_str) # Обработка конечной позиции
                if self.is_valid_move(start_pos, end_pos): # Проверка валидности хода
                    self.make_move(start_pos, end_pos) # Выполнение хода
                    break
                else:
                    print('Недопустимый ход. Попробуйте снова.')
             except (ValueError, IndexError) as ex:
                logger.error(f'Неверный ввод, ожидался формат \'A1 B2\'', exc_info=ex)
                print('Неверный ввод, ожидался формат \'A1 B2\'.')
    
    def parse_position(self, pos_str: str) -> Tuple[int, int]:
        """
        Преобразует позицию в виде строки в кортеж координат (строка, столбец).
         
        :param pos_str: Позиция в виде строки (например, 'A1').
        :type pos_str: str
        :return: Кортеж (строка, столбец).
        :rtype: Tuple[int, int]
        """
        col = ord(pos_str[0].upper()) - ord('A') # Вычисление номера колонки из буквы
        row = int(pos_str[1]) - 1 # Вычисление номера строки из цифры
        if not (0 <= col < 8 and 0 <= row < 8):
           raise IndexError('Неправильные координаты.')
        return row, col # Возвращение координаты

    def is_valid_move(self, start_pos: Tuple[int, int], end_pos: Tuple[int, int]) -> bool:
        """
        Проверяет, является ли ход допустимым.
        
        :param start_pos: Начальная позиция шашки (строка, столбец).
        :type start_pos: Tuple[int, int]
        :param end_pos: Конечная позиция шашки (строка, столбец).
        :type end_pos: Tuple[int, int]
        :return: True, если ход допустим, False иначе.
        :rtype: bool
        """
        start_row, start_col = start_pos # Разделение начальной позиции на координаты строки и столбца
        end_row, end_col = end_pos # Разделение конечной позиции на координаты строки и столбца
        
        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
             return False # Проверка на то, что координаты находятся в пределах доски

        piece = self.board[start_row][start_col] # Получение шашки из стартовой позиции
        if piece != self.current_player:
           return False # Проверка, что игрок двигает свою шашку
        
        if self.board[end_row][end_col] is not None:
            return False # Проверка, что конечная клетка не занята
        
        row_diff = abs(end_row - start_row) # Вычисление разницы строк
        col_diff = abs(end_col - start_col) # Вычисление разницы столбцов
        
        if row_diff != col_diff:
            return False # Проверка, что ход по диагонали
    
        if row_diff == 1:
            return True # Ход на одну клетку
        elif row_diff == 2:
            jumped_row = (start_row + end_row) // 2 # Вычисление строки для шашки, через которую был совершен прыжок
            jumped_col = (start_col + end_col) // 2 # Вычисление столбца для шашки, через которую был совершен прыжок
            if self.board[jumped_row][jumped_col] and self.board[jumped_row][jumped_col] != self.current_player:
                return True # Проверка, что прыжок совершен через шашку противника
            
        return False
       
    def make_move(self, start_pos: Tuple[int, int], end_pos: Tuple[int, int]):
        """
        Выполняет ход, перемещая шашку и удаляя шашки противника при прыжке.

        :param start_pos: Начальная позиция шашки (строка, столбец).
        :type start_pos: Tuple[int, int]
        :param end_pos: Конечная позиция шашки (строка, столбец).
        :type end_pos: Tuple[int, int]
        """
        start_row, start_col = start_pos # Разделение начальной позиции на координаты строки и столбца
        end_row, end_col = end_pos # Разделение конечной позиции на координаты строки и столбца
        
        piece = self.board[start_row][start_col] # Получение шашки из стартовой позиции
        self.board[start_row][start_col] = None # Очистка стартовой позиции
        self.board[end_row][end_col] = piece # Перемещение шашки в конечную позицию
        
        if abs(end_row - start_row) == 2:
            jumped_row = (start_row + end_row) // 2 # Вычисление строки шашки, через которую был совершен прыжок
            jumped_col = (start_col + end_col) // 2 # Вычисление столбца шашки, через которую был совершен прыжок
            self.board[jumped_row][jumped_col] = None # Удаление шашки противника, через которую был совершен прыжок
            print('Вы удалили шашку соперника!')

    def check_game_over(self) -> bool:
         """
         Проверяет, завершилась ли игра (нет ходов или нет шашек).

         :return: True, если игра окончена, False иначе.
         :rtype: bool
         """
         if not self.can_move(): # Если нет возможных ходов
              return True # Завершение игры
         
         white_pieces = 0 # Счетчики количества шашек
         black_pieces = 0
         for row in self.board: # Проверка каждой клетки на наличие шашек
            for piece in row:
                 if piece == 'white':
                     white_pieces+=1
                 elif piece == 'black':
                    black_pieces+=1
         if white_pieces == 0 or black_pieces == 0: # Если шашки одного из игроков закончились
            return True # Завершение игры
         return False # Игра продолжается
    
    def can_move(self) -> bool:
       """
       Проверяет, есть ли у текущего игрока возможные ходы.
       
       :return: True, если есть хотя бы один возможный ход, False иначе.
       :rtype: bool
       """
       for row in range(8):
           for col in range(8):
               if self.board[row][col] == self.current_player: # Проверяем, принадлежит ли шашка текущему игроку
                   for row_offset in [-1, 1]: # Проверяем все возможные ходы по диагонали
                      for col_offset in [-1, 1]:
                        new_row = row + row_offset # Вычисление новой строки
                        new_col = col + col_offset # Вычисление нового столбца
                        if 0 <= new_row < 8 and 0 <= new_col < 8 and self.is_valid_move((row, col), (new_row, new_col)): # Проверка возможности хода
                           return True # Если хотя бы один ход есть, возвращаем true
                        
                        if 0 <= row + row_offset*2 < 8 and 0 <= col + col_offset*2 < 8 and self.is_valid_move((row, col), (row + row_offset*2, col+ col_offset*2)):# Проверяем возможность прыжка
                            return True # Если хотя бы один ход есть, возвращаем true

       return False # Если нет ходов, возвращаем false

    def end_game(self):
        """
        Завершает игру, объявляя победителя и предлагая сыграть снова.
        """
        white_pieces = 0
        black_pieces = 0

        for row in self.board:
           for piece in row:
                if piece == 'white':
                     white_pieces+=1
                elif piece == 'black':
                     black_pieces+=1
        
        if white_pieces > black_pieces:
            print('Игра окончена! Победил игрок с белыми шашками.')
        elif black_pieces > white_pieces:
            print('Игра окончена! Победил игрок с черными шашками.')
        else:
           print('Игра окончена! Ничья!')

        while True:
            play_again = input('Хотите сыграть снова? (да/нет): ').lower() # Запрос на повтор игры
            if play_again in ['да', 'нет']:
                break
            else:
                print('Некорректный ввод. Введите "да" или "нет".')
        if play_again == 'да':
            self.__init__() # Инициализация новой игры
            self.start_game() # Запуск новой игры
        else:
            print('Спасибо за игру!')

    def switch_player(self):
        """
        Переключает текущего игрока.
        """
        self.current_player = 'black' if self.current_player == 'white' else 'white' # Переключение текущего игрока


if __name__ == '__main__':
    game = ICheckGame() # Создание объекта игры
    game.start_game() # Запуск игры
```