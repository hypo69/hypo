# Анализ кода модуля `76_rocksp.ru.md`

**Качество кода**

- **Соответствие требованиям к формату кода (1-10):**
    - Код представлен в формате Markdown, что соответствует заданию.
    - Описаны основные этапы игры: инициализация, игровой процесс и завершение.
    - Приведен пример работы программы.
    - Обозначены возможные ограничения и рекомендуемые улучшения.
    - Инструкция четкая и понятная, все разделы хорошо структурированы.
- **Преимущества:**
    - Хорошо структурированный текст, разделенный на логические блоки.
    - Понятное описание правил игры и процесса.
    - Примеры работы программы помогают понять игровой процесс.
    - Указаны возможные ограничения и идеи для дальнейших улучшений.
- **Недостатки:**
    - Это не код, а описание правил игры в формате Markdown, а не Python код.
    - Нет конкретной реализации на Python, поэтому невозможно оценить код на соответствие стандартам Python.
    - Отсутствует docstring, поскольку данный файл не является Python кодом.

**Рекомендации по улучшению**

1. **Преобразование в Python:**
   - Необходимо реализовать логику игры в виде Python-кода.
   - Создать классы и функции для представления игровой доски, ходов игроков, проверки условий победы и т.д.
2. **Добавление docstring:**
   - Добавить docstring для каждого модуля, класса и функции, описывающие их назначение, параметры и возвращаемые значения.
3. **Обработка ошибок:**
   - Добавить обработку ошибок для ввода пользователя, таких как некорректный формат координат.
4. **Логирование:**
   - Использовать модуль logging для записи информации о ходе игры, ошибок и других важных событий.
5. **Модульность:**
   - Разбить код на отдельные модули и функции для улучшения читаемости и поддерживаемости.

**Улучшенный код**

```python
"""
Модуль для реализации игры ROCKSP (Камни).
=========================================================================================

Этот модуль содержит функции и классы для создания и управления игрой ROCKSP.

Пример использования
--------------------

.. code-block:: python

    game = RockspGame()
    game.start_game()
"""
import logging  # Импортируем модуль logging #
from typing import List, Tuple

logger = logging.getLogger(__name__) # Инициализируем логгер #

class RockspGame:
    """
    Класс для управления игрой ROCKSP.

    :ivar board: Игровая доска, представленная в виде двумерного списка.
    :vartype board: List[List[str]]
    :ivar current_player: Текущий игрок ('1' или '2').
    :vartype current_player: str
    :ivar moves_count: Количество сделанных ходов.
    :vartype moves_count: int
    :ivar max_moves: Максимальное количество ходов до ничьей.
    :vartype max_moves: int
    """
    def __init__(self, board_size: int = 6, max_moves: int = 20):
        """
        Инициализирует игру.

        :param board_size: Размер игровой доски (по умолчанию 6).
        :param max_moves: Максимальное количество ходов (по умолчанию 20).
        """
        self.board_size = board_size
        self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)] # Создаем игровую доску #
        self.current_player = '1'
        self.moves_count = 0
        self.max_moves = max_moves
        logger.info('Игра инициализирована.') # Логируем начало игры #

    def display_board(self):
        """
        Отображает текущее состояние доски.
        """
        print('  ' + ' '.join(chr(ord('A') + i) for i in range(self.board_size))) # Выводим буквы колонок #
        for i, row in enumerate(self.board):
            print(f'{i + 1} {" ".join(f"[{cell}]" for cell in row)}') # Выводим строки с ячейками #
        logger.debug('Доска отображена.') # Логируем отображение доски #


    def get_move(self) -> Tuple[int, int]:
        """
        Получает ход игрока.

        :return: Кортеж координат (row, col).
        :rtype: Tuple[int, int]
        """
        while True:
            try:
                move = input(f'Игрок {self.current_player}, ваш ход. Введите координаты клетки (например, B2): ').strip().upper() # Получаем ввод игрока #
                col = ord(move[0]) - ord('A') # Получаем индекс столбца из введенной буквы #
                row = int(move[1:]) - 1 # Получаем индекс строки из введенного номера #
                if 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == ' ':
                    logger.debug(f'Игрок {self.current_player} выбрал клетку {move}') # Логируем выбор клетки #
                    return row, col
                else:
                    print('Недопустимый ход. Попробуйте снова.') # Сообщение об ошибке ввода #
                    logger.warning(f'Недопустимый ход игрока {self.current_player}: {move}') # Логируем неверный ход #
            except (ValueError, IndexError):
                print('Неверный формат ввода. Попробуйте снова.') # Сообщение об ошибке ввода #
                logger.error(f'Неверный формат ввода игрока {self.current_player}') # Логируем ошибку ввода #
    

    def make_move(self, row: int, col: int):
        """
        Размещает камень на доске.

        :param row: Индекс строки.
        :param col: Индекс столбца.
        """
        self.board[row][col] = 'R' if self.current_player == '1' else 'B'
        self.moves_count += 1 # Увеличиваем счетчик ходов #
        logger.debug(f'Игрок {self.current_player} разместил камень на клетку ({row}, {col})') # Логируем ход #

    def is_valid_move(self, row: int, col: int) -> bool:
        """
        Проверяет, допустим ли ход.

        :param row: Индекс строки.
        :param col: Индекс столбца.
        :return: True, если ход допустим, False иначе.
        :rtype: bool
        """
        if 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == ' ':
            return True # Возвращаем true, если ход возможен #
        return False  # Возвращаем false, если ход невозможен #


    def has_valid_moves(self) -> bool:
        """
        Проверяет, есть ли у текущего игрока допустимые ходы.

        :return: True, если есть допустимые ходы, False иначе.
        :rtype: bool
        """
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.is_valid_move(row,col):
                    return True  # Возвращаем true, если есть возможные ходы #
        return False  # Возвращаем false, если нет возможных ходов #


    def switch_player(self):
        """
        Меняет текущего игрока.
        """
        self.current_player = '2' if self.current_player == '1' else '1'
        logger.debug(f'Текущий игрок: {self.current_player}') # Логируем смену игрока #

    def check_game_end(self) -> str:
        """
        Проверяет, завершилась ли игра.

        :return: 'win' или 'draw', если игра завершена, None иначе.
        :rtype: str
        """
        if not self.has_valid_moves():
            winner = '1' if self.current_player == '2' else '2'
            logger.info(f'Игра окончена. Победил игрок {winner}.') # Логируем победу #
            return 'win'
        if self.moves_count >= self.max_moves:
            logger.info('Игра окончена. Ничья.') # Логируем ничью #
            return 'draw'
        return None  # Возвращаем None, если игра не окончена #

    def start_game(self):
        """
        Запускает игровой процесс.
        """
        print('Добро пожаловать в ROCKSP!')
        print('Ваша задача — заблокировать соперника, размещая камни на доске.')
        print('Игра продолжается до тех пор, пока один из игроков не заблокирует соперника или пока не будет достигнуто максимальное количество ходов.')
        print('Удачи!\n')
        while True:
            self.display_board()
            row, col = self.get_move()
            self.make_move(row, col)
            game_end = self.check_game_end()
            if game_end:
                self.display_board()
                if game_end == 'win':
                  print(f'Игра окончена! Победил Игрок {"1" if self.current_player == "2" else "2"}.')
                elif game_end == 'draw':
                  print('Игра окончена! Ничья.')
                break
            self.switch_player()
        if input('Хотите сыграть снова? (да/нет): ').strip().lower() == 'да':
            self.__init__()
            self.start_game()
        else:
            print('Спасибо за игру!') # Сообщение о завершении игры #
            logger.info('Игра завершена.') # Логируем завершение игры #


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') # Настраиваем логгер #
    game = RockspGame()
    game.start_game()
```