# Анализ кода модуля `27_checkr.ru.md`

**Качество кода**

1/10
- Плюсы
  - Документ содержит подробное описание правил игры в шашки.
  - Представлена пошаговая инструкция по реализации игры.
  - Приведены примеры работы программы и возможные ограничения.
- Минусы
  - Код отсутствует.
  - Инструкция не содержит RST комментарии и docstring.
  - Нет импортов.
  - Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson`.
  - Не используется `from src.logger.logger import logger`.
  - Нет обработки ошибок с помощью `logger.error`.
  - Формат документации не соответствует RST.
  - Не соответствует требуемой структуре ответа.
  -  Нельзя использовать как рабочий код.

**Рекомендации по улучшению**

1.  **Добавить код:** Необходимо добавить реализацию игры в шашки на Python, следуя инструкциям, описанным в документе.
2.  **Форматирование документации:** Применить reStructuredText (RST) для всех комментариев и docstring.
3.  **Импорты:** Добавить необходимые импорты для работы кода, например, для работы с JSON, если это потребуется.
4.  **Использовать `j_loads`:** Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
5.  **Логирование:** Использовать `from src.logger.logger import logger` для логирования ошибок.
6.  **Обработка ошибок:** Заменить `try-except` на обработку ошибок с помощью `logger.error`.
7.  **Комментарии:** Переписать все комментарии в формате reStructuredText (RST).
8.  **Улучшение логики:** Реализовать проверку хода, логику компьютера, подсчет победителя и другие игровые моменты.
9.  **Полный код:** Предоставить полный код в конце ответа в одном блоке, который можно скопировать и вставить.
10. **Структура ответа**: Привести в соответствие структуру ответа.
11. **Примеры кода:** Добавить примеры использования функций и классов.

**Оптимизированный код**

```markdown
# Анализ кода модуля `27_checkr.ru.md`

**Качество кода**

1/10
- Плюсы
  - Документ содержит подробное описание правил игры в шашки.
  - Представлена пошаговая инструкция по реализации игры.
  - Приведены примеры работы программы и возможные ограничения.
- Минусы
  - Код отсутствует.
  - Инструкция не содержит RST комментарии и docstring.
  - Нет импортов.
  - Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson`.
  - Не используется `from src.logger.logger import logger`.
  - Нет обработки ошибок с помощью `logger.error`.
  - Формат документации не соответствует RST.
  - Не соответствует требуемой структуре ответа.
  - Нельзя использовать как рабочий код.

**Рекомендации по улучшению**

1.  **Добавить код:** Необходимо добавить реализацию игры в шашки на Python, следуя инструкциям, описанным в документе.
2.  **Форматирование документации:** Применить reStructuredText (RST) для всех комментариев и docstring.
3.  **Импорты:** Добавить необходимые импорты для работы кода, например, для работы с JSON, если это потребуется.
4.  **Использовать `j_loads`:** Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
5.  **Логирование:** Использовать `from src.logger.logger import logger` для логирования ошибок.
6.  **Обработка ошибок:** Заменить `try-except` на обработку ошибок с помощью `logger.error`.
7.  **Комментарии:** Переписать все комментарии в формате reStructuredText (RST).
8.  **Улучшение логики:** Реализовать проверку хода, логику компьютера, подсчет победителя и другие игровые моменты.
9.  **Полный код:** Предоставить полный код в конце ответа в одном блоке, который можно скопировать и вставить.
10. **Структура ответа**: Привести в соответствие структуру ответа.
11. **Примеры кода:** Добавить примеры использования функций и классов.

**Оптимизированный код**
```python
"""
Модуль для реализации игры в шашки.
=========================================================================================

Этот модуль содержит функции и классы для игры в шашки,
где игрок играет против компьютера.

Пример использования
--------------------

Пример запуска игры:

.. code-block:: python

    if __name__ == "__main__":
        game = Checkers()
        game.play()
"""
from src.logger.logger import logger
# from src.utils.jjson import j_loads, j_loads_ns # TODO: import if needed

class Checkers:
    """
    Класс для управления игрой в шашки.

    :ivar board: Представление доски в виде списка списков.
    :vartype board: list[list[str]]
    :ivar player_piece: Символ, представляющий фигуру игрока ('O').
    :vartype player_piece: str
    :ivar computer_piece: Символ, представляющий фигуру компьютера ('X').
    :vartype computer_piece: str
    """
    def __init__(self):
        """
        Инициализирует игру в шашки с начальной расстановкой фигур.
        """
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.player_piece = 'O'
        self.computer_piece = 'X'
        self._initialize_board()

    def _initialize_board(self):
        """
        Устанавливает начальную позицию шашек на доске.
        """
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = self.computer_piece
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = self.player_piece
    
    def print_board(self):
        """
        Выводит текущее состояние доски в консоль.
        """
        print("   0 1 2 3 4 5 6 7")
        for i, row in enumerate(self.board):
            print(f"{i}  {' '.join(row)}")

    def is_valid_move(self, start_row, start_col, end_row, end_col):
        """
        Проверяет, является ли ход валидным.

        :param start_row: Начальная строка.
        :type start_row: int
        :param start_col: Начальный столбец.
        :type start_col: int
        :param end_row: Конечная строка.
        :type end_row: int
        :param end_col: Конечный столбец.
        :type end_col: int
        :return: True, если ход валиден, иначе False.
        :rtype: bool
        """
        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            return False
        if self.board[start_row][start_col] == ' ':
            return False
        if self.board[end_row][end_col] != ' ':
            return False
        if abs(end_row - start_row) != 1 or abs(end_col - start_col) != 1: # TODO: Implement jump logic
            return False

        return True

    def move_piece(self, start_row, start_col, end_row, end_col):
        """
        Перемещает фигуру с начальной позиции на конечную.

        :param start_row: Начальная строка.
        :type start_row: int
        :param start_col: Начальный столбец.
        :type start_col: int
        :param end_row: Конечная строка.
        :type end_row: int
        :param end_col: Конечный столбец.
        :type end_col: int
        """
        piece = self.board[start_row][start_col]
        self.board[start_row][start_col] = ' '
        self.board[end_row][end_col] = piece

    def get_player_move(self):
        """
        Запрашивает у игрока координаты хода и обрабатывает ввод.

        :return: Координаты начальной и конечной позиций хода.
        :rtype: tuple[int, int, int, int]
        """
        while True:
            try:
                start_pos = input("Введите координаты фигуры для перемещения (строка, столбец) через запятую (например: 3,5): ")
                start_row, start_col = map(int, start_pos.split(','))

                end_pos = input("Введите целевую клетку для перемещения (строка, столбец) через запятую (например: 4,6): ")
                end_row, end_col = map(int, end_pos.split(','))

                if self.is_valid_move(start_row, start_col, end_row, end_col):
                    return start_row, start_col, end_row, end_col
                else:
                     print("Недопустимый ход. Попробуйте еще раз.")
            except ValueError:
                logger.error('Неверный формат ввода, требуется ввести два числа через запятую')
                print("Неверный формат ввода. Пожалуйста, введите координаты через запятую.")
    
    def _get_computer_move(self):
       """
       Определяет ход компьютера.

       В текущей версии компьютер выбирает случайный ход.

       :return: Координаты начальной и конечной позиций хода.
       :rtype: tuple[int, int, int, int]
       """
       import random
       possible_moves = []
       for row in range(8):
           for col in range(8):
                if self.board[row][col] == self.computer_piece:
                    for dr in [-1, 1]:
                        for dc in [-1, 1]:
                            new_row, new_col = row + dr, col + dc
                            if self.is_valid_move(row, col, new_row, new_col):
                                possible_moves.append((row, col, new_row, new_col))
       if not possible_moves:
            return None
       return random.choice(possible_moves)

    def check_winner(self):
        """
        Проверяет, есть ли победитель.

        :return: 'player', если игрок выиграл, 'computer', если выиграл компьютер, иначе None.
        :rtype: str | None
        """
        player_pieces = 0
        computer_pieces = 0
        for row in self.board:
            for piece in row:
                if piece == self.player_piece:
                    player_pieces += 1
                elif piece == self.computer_piece:
                    computer_pieces += 1

        if player_pieces == 0:
            return 'computer'
        if computer_pieces == 0:
            return 'player'
        
        #TODO: Add stalemate check
        
        return None

    def play(self):
       """
       Основной игровой цикл.
       """
       print("Добро пожаловать в игру Шашки!")
       print(f"Вы играете за '{self.player_piece}', компьютер за '{self.computer_piece}'.")
       self.print_board()

       while True:
            # Ход игрока
            print("Ваш ход.")
            start_row, start_col, end_row, end_col = self.get_player_move()
            self.move_piece(start_row, start_col, end_row, end_col)
            self.print_board()

            winner = self.check_winner()
            if winner:
               break

           # Ход компьютера
            print("Ход компьютера.")
            computer_move = self._get_computer_move()
            if computer_move:
                start_row, start_col, end_row, end_col = computer_move
                self.move_piece(start_row, start_col, end_row, end_col)
                self.print_board()
            else:
                winner = 'player' #No moves available for the computer, so the player wins
                break

            winner = self.check_winner()
            if winner:
                break


       if winner == 'player':
            print("ПОБЕДА! Вы захватили все фигуры противника!")
       elif winner == 'computer':
            print("ПОБЕДИЛ КОМПЬЮТЕР!")
        

       while True:
            play_again = input("Хотите сыграть снова? (да/нет): ")
            if play_again.lower() == 'да':
                self.__init__()
                self.play()
                break
            elif play_again.lower() == 'нет':
               print("Спасибо за игру!")
               break
            else:
               print("Некорректный ввод. Пожалуйста введите 'да' или 'нет'.")


if __name__ == "__main__":
    game = Checkers()
    game.play()
```