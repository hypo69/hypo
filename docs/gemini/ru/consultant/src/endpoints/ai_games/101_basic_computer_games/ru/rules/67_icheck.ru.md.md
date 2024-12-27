# Анализ кода модуля `icheck.ru.md`

**Качество кода: 8/10**

- **Плюсы:**
    - Документ содержит подробное описание игры "ICHECK", включая правила, пошаговую инструкцию, примеры работы, возможные ограничения и рекомендации по реализации.
    - Текст хорошо структурирован с использованием Markdown, что делает его легким для чтения и понимания.
    - Присутствуют конкретные примеры и сценарии использования, что помогает понять механику игры.
- **Минусы:**
    - Отсутствует код, что является критичным, так как данный модуль должен содержать программную реализацию игры.
    - Нет reStructuredText (RST) документации, которая требуется по инструкции.
    - Нет примера использования `j_loads` или `j_loads_ns`.
    - Нет обработки ошибок через `logger.error`.
    - Нет импортов и не используются функции.

**Рекомендации по улучшению**

1.  **Добавить программный код:** Необходимо добавить реализацию игры на Python. Код должен соответствовать описанным правилам и инструкциям.
2.  **Применить RST:** Переписать все комментарии и документацию в формате reStructuredText (RST).
3.  **Использовать `j_loads`:** Если требуется чтение файлов, использовать `j_loads` или `j_loads_ns` из `src.utils.jjson`.
4.  **Логирование ошибок:** Использовать `from src.logger.logger import logger` и обрабатывать ошибки с помощью `logger.error`.
5.  **Добавить импорты:** Добавить все необходимые импорты.
6.  **Рефакторинг:** Разбить код на функции, добавить docstring к каждой функции.
7.  **Примеры:** Добавить примеры использования функций и классов, используя reStructuredText (RST) синтаксис.
8.  **Обработка ошибок:** Убрать try-except блоки и заменить их на обработку ошибок через `logger.error`.

**Оптимизированный код**
```markdown
# Анализ кода модуля `icheck.ru.md`

**Качество кода: 8/10**

- **Плюсы:**
    - Документ содержит подробное описание игры "ICHECK", включая правила, пошаговую инструкцию, примеры работы, возможные ограничения и рекомендации по реализации.
    - Текст хорошо структурирован с использованием Markdown, что делает его легким для чтения и понимания.
    - Присутствуют конкретные примеры и сценарии использования, что помогает понять механику игры.
- **Минусы:**
    - Отсутствует код, что является критичным, так как данный модуль должен содержать программную реализацию игры.
    - Нет reStructuredText (RST) документации, которая требуется по инструкции.
    - Нет примера использования `j_loads` или `j_loads_ns`.
    - Нет обработки ошибок через `logger.error`.
    - Нет импортов и не используются функции.

**Рекомендации по улучшению**

1.  **Добавить программный код:** Необходимо добавить реализацию игры на Python. Код должен соответствовать описанным правилам и инструкциям.
2.  **Применить RST:** Переписать все комментарии и документацию в формате reStructuredText (RST).
3.  **Использовать `j_loads`:** Если требуется чтение файлов, использовать `j_loads` или `j_loads_ns` из `src.utils.jjson`.
4.  **Логирование ошибок:** Использовать `from src.logger.logger import logger` и обрабатывать ошибки с помощью `logger.error`.
5.  **Добавить импорты:** Добавить все необходимые импорты.
6.  **Рефакторинг:** Разбить код на функции, добавить docstring к каждой функции.
7.  **Примеры:** Добавить примеры использования функций и классов, используя reStructuredText (RST) синтаксис.
8.  **Обработка ошибок:** Убрать try-except блоки и заменить их на обработку ошибок через `logger.error`.

**Оптимизированный код**
```python
"""
Модуль для реализации игры в шашки (ICHECK).
=========================================================================================

Этот модуль содержит функции для инициализации игры, обработки ходов, удаления шашек,
проверки условий завершения игры и предложения сыграть снова.

Пример использования
--------------------

Пример инициализации и начала игры:

.. code-block:: python

    game = ICheckGame()
    game.start_game()
"""

from typing import List, Tuple
from src.logger.logger import logger
# from src.utils.jjson import j_loads # TODO: пример использования j_loads, если требуется загрузка из файла

class ICheckGame:
    """
    Класс для управления игрой в шашки (ICHECK).
    """
    def __init__(self):
        """
        Инициализация игры. Создает доску и расставляет шашки.
        """
        self.board = self._create_board() # Инициализация доски
        self.current_player = 'white' # Установка текущего игрока
        self.game_over = False # Флаг окончания игры

    def _create_board(self) -> List[List[str]]:
        """
        Создание стандартной доски 8x8 с шашками.

        :return: Список списков, представляющий доску.
        :rtype: List[List[str]]
        """
        board = [[' ' for _ in range(8)] for _ in range(8)]
        # Расставляем белые шашки
        for i in range(3):
            for j in range(8):
                if (i + j) % 2 != 0:
                    board[i][j] = 'w'
        # Расставляем черные шашки
        for i in range(5, 8):
            for j in range(8):
                if (i + j) % 2 != 0:
                    board[i][j] = 'b'
        return board

    def _print_board(self) -> None:
        """
        Вывод текущего состояния доски в консоль.
        """
        print('  a b c d e f g h')
        for i, row in enumerate(self.board):
            print(f'{8 - i} {" ".join(row)}')

    def _is_valid_move(self, start: Tuple[int, int], end: Tuple[int, int]) -> bool:
        """
        Проверка допустимости хода.

        :param start: Координаты начальной позиции (строка, столбец).
        :type start: Tuple[int, int]
        :param end: Координаты конечной позиции (строка, столбец).
        :type end: Tuple[int, int]
        :return: True, если ход допустим, False в противном случае.
        :rtype: bool
        """
        start_row, start_col = start
        end_row, end_col = end

        # Проверка выхода за границы доски
        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            logger.error(f'Неверные координаты: {start=} {end=}')
            return False

        piece = self.board[start_row][start_col] # Получаем фигуру из начальной клетки
        if piece == ' ':
            logger.error(f'Нет фигуры в стартовой позиции: {start=}')
            return False # Проверяем, что в стартовой клетке есть фигура
        if (piece == 'w' and self.current_player != 'white') or (piece == 'b' and self.current_player != 'black'):
             logger.error(f'Ход не текущего игрока: {piece=} {self.current_player=}')
             return False # Проверка, что фигура принадлежит текущему игроку


        if self.board[end_row][end_col] != ' ':
            logger.error(f'Конечная позиция занята: {end=}')
            return False # Проверка, что конечная клетка пуста


        row_diff = abs(end_row - start_row) # Расчет разницы строк
        col_diff = abs(end_col - start_col) # Расчет разницы столбцов

        if row_diff != col_diff or row_diff > 2:
             logger.error(f'Недопустимый ход (не по диагонали или слишком далеко): {start=} {end=}')
             return False # Ход должен быть по диагонали на одну или две клетки

        # Проверка прыжка
        if row_diff == 2:
             jumped_row = (start_row + end_row) // 2 # Определяем строку для прыжка
             jumped_col = (start_col + end_col) // 2 # Определяем столбец для прыжка
             jumped_piece = self.board[jumped_row][jumped_col] # Получаем фигуру, через которую прыгаем

             if jumped_piece == ' ':
                 logger.error(f'Не через кого прыгать: {start=} {end=}')
                 return False  # Проверка, что прыгаем через фигуру

             if (piece == 'w' and jumped_piece == 'w') or (piece == 'b' and jumped_piece == 'b'):
                 logger.error(f'Нельзя прыгать через свои фигуры: {start=} {end=}')
                 return False # Проверяем, что прыгаем через чужую фигуру
        return True


    def _move_piece(self, start: Tuple[int, int], end: Tuple[int, int]) -> None:
        """
        Перемещение шашки с начальной позиции на конечную.

        :param start: Координаты начальной позиции (строка, столбец).
        :type start: Tuple[int, int]
        :param end: Координаты конечной позиции (строка, столбец).
        :type end: Tuple[int, int]
        """
        start_row, start_col = start #  Получаем начальную позицию
        end_row, end_col = end #  Получаем конечную позицию
        piece = self.board[start_row][start_col] #  Получаем фигуру из стартовой клетки

        self.board[start_row][start_col] = ' ' #  Очищаем стартовую клетку
        self.board[end_row][end_col] = piece #  Ставим фигуру в конечную клетку

        #  Проверка прыжка
        if abs(end_row - start_row) == 2:
            jumped_row = (start_row + end_row) // 2 #  Определяем строку прыжка
            jumped_col = (start_col + end_col) // 2 #  Определяем столбец прыжка
            self.board[jumped_row][jumped_col] = ' ' #  Удаляем фигуру через которую прыгнули

            if self.current_player == 'white':
                print('Вы удалили шашку соперника!') # Выводим сообщение, если игрок удалил шашку
            else:
                print('Вы удалили шашку соперника!')

    def _parse_move(self, move_str: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        """
        Преобразование строкового ввода игрока в координаты.

        :param move_str: Строка ввода пользователя (например, "a1 b2").
        :type move_str: str
        :return: Кортеж из начальной и конечной координат.
        :rtype: Tuple[Tuple[int, int], Tuple[int, int]]
        """
        try:
            start_str, end_str = move_str.split() # Разделяем ввод пользователя
            start_col = ord(start_str[0].lower()) - ord('a') #  Преобразовываем буквы в индексы столбцов
            start_row = 8 - int(start_str[1]) #  Преобразовываем цифры в индексы строк
            end_col = ord(end_str[0].lower()) - ord('a') #  Преобразовываем буквы в индексы столбцов
            end_row = 8 - int(end_str[1]) #  Преобразовываем цифры в индексы строк
            return (start_row, start_col), (end_row, end_col) # Возвращаем координаты
        except (ValueError, IndexError) as ex:
            logger.error(f'Ошибка парсинга ввода: {move_str=}', ex) # Логируем ошибку
            return None, None

    def _check_game_over(self) -> bool:
        """
        Проверка условий завершения игры.

        :return: True, если игра завершена, False в противном случае.
        :rtype: bool
        """
        white_pieces = 0 # Счетчик белых шашек
        black_pieces = 0 # Счетчик черных шашек

        for row in self.board:
            for piece in row:
                if piece == 'w':
                    white_pieces += 1 # Считаем белые шашки
                elif piece == 'b':
                    black_pieces += 1 # Считаем черные шашки

        if white_pieces == 0:
            print('Игра окончена! Победил игрок с черными шашками.') # Выводим сообщение о победе черных
            self.game_over = True # Ставим флаг окончания игры
            return True
        if black_pieces == 0:
            print('Игра окончена! Победил игрок с белыми шашками.') # Выводим сообщение о победе белых
            self.game_over = True # Ставим флаг окончания игры
            return True
        return False


    def start_game(self) -> None:
        """
        Запуск игры.
        """
        print('Добро пожаловать в ICHECK!')
        print('Ваша задача — удалить как можно больше шашек соперника, совершая диагональные прыжки.')
        print('Игра продолжается до тех пор, пока у одного из игроков не останется шашек или не будет возможных ходов.')
        print('Удачи!')

        while not self.game_over:
            self._print_board() # Выводим доску
            print(f'Игрок с {self.current_player} шашками, ваш ход.')

            while True:
                move_str = input('Введите координаты шашки и клетки, куда хотите переместить её (например, A1 B2): ') # Получаем ввод игрока
                start, end = self._parse_move(move_str) #  Преобразуем ввод пользователя в координаты

                if start is None or end is None:
                    print('Неверный ввод. Попробуйте снова.') # Сообщаем об ошибке ввода
                    continue

                if self._is_valid_move(start, end):
                    self._move_piece(start, end) # Перемещаем фигуру
                    break
                else:
                    print('Недопустимый ход. Попробуйте снова.') # Сообщаем о неверном ходе

            if self._check_game_over():
                break

            self.current_player = 'black' if self.current_player == 'white' else 'white' #  Меняем текущего игрока

        while True:
             play_again = input('Хотите сыграть снова? (да/нет): ').lower() #  Предлагаем сыграть снова
             if play_again == 'да':
                 self.__init__() # Перезапускаем игру
                 self.start_game()
                 break
             elif play_again == 'нет':
                 print('Спасибо за игру!')
                 break
             else:
                 print('Неверный ввод. Пожалуйста, введите "да" или "нет".') # Сообщаем о неверном вводе

if __name__ == '__main__':
    game = ICheckGame()
    game.start_game()
```