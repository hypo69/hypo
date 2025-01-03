# Анализ кода модуля CHECKR (Шашки)

**Качество кода**

8/10
- Плюсы
    - Документ подробно описывает правила игры в шашки, включая инициализацию, игровой процесс и условия победы.
    - Приведены примеры работы программы, что облегчает понимание взаимодействия пользователя с игрой.
    - Указаны возможные ограничения игры, что позволяет пользователям ожидать определенного поведения программы.
    - Текст логически разделен на разделы с использованием Markdown.

- Минусы
    - Отсутствует формальное описание кода, так как это текстовое описание правил игры, а не код.
    - Нет информации о том, какой язык программирования используется для реализации.
    - Документ не содержит reStructuredText (RST) форматирования.

**Рекомендации по улучшению**

1.  **Форматирование RST**: Необходимо перевести документ в формат reStructuredText (RST) для соответствия стандартам документации Python.
2.  **Указать язык**: Явно указать язык программирования, который будет использоваться для реализации игры.
3.  **Структура кода**: Добавить структуры кода, примеры классов, функций и методов с docstring в стиле reStructuredText (RST).
4.  **Описание данных**: Указать, как будут храниться данные игры (например, состояние доски, положение фигур).
5.  **Логирование**: Включить логирование для отслеживания ошибок и действий игры.
6.  **Обработка ошибок**: Детально продумать обработку ошибок при вводе некорректных данных от пользователя.
7.  **Анализ ходов**: Описать, как будет реализован анализ ходов компьютера (например, с использованием простых эвристик).
8.  **Примеры RST**: Добавить примеры документации в формате RST.

**Оптимизированный код**
```markdown
### Название игры: **CHECKR** (Шашки)

#### Описание
:mod:`checkr` - это модуль, реализующий классическую игру в шашки.

**CHECKR** — это классическая игра в шашки, где игрок и компьютер поочередно делают ходы. Игрок управляет фигурами, которые обозначены "O", в то время как фигуры компьютера обозначены "X". Игра проходит на стандартной доске 8x8, где фигуры могут двигаться по диагонали. Цель игры — захватить все фигуры противника или заблокировать их так, чтобы они не могли двигаться.

---

### Пошаговая инструкция для реализации

#### 1. **Инициализация игры**
    - В начале игры на доске размещаются фигуры:
        - Игрок управляет фигурами "O".
        - Компьютер управляет фигурами "X".
    - Игрок и компьютер делают ходы поочередно. Игрок начинает первым.

#### 2. **Основной цикл игры**
    - **Ход игрока:**
        1. Игрок вводит координаты фигуры, которую он хочет переместить, например, (3, 5).
        2. Затем игрок вводит координаты целевой клетки для перемещения, например, (4, 6).
        3. Программа проверяет, возможно ли выполнение хода. Если ход невозможен (например, если клетка занята), программа попросит игрока выбрать другой ход.
   
    - **Ход компьютера:**
        1. Компьютер делает свой ход по аналогии с игроком. Программа анализирует доску и выбирает оптимальное движение для своей фигуры.

    - **Победа:**
        - Игра продолжается до тех пор, пока один из игроков не останется без фигур или не заблокирует все фигуры противника.
        - Когда игрок или компьютер выигрывает, программа выводит сообщение о победе:
            ```
            ПОБЕДА! ВЫ ЗАХВАТИЛИ ВСЕ ФИГУРЫ ПРОТИВНИКА!
            ```

#### 3. **Подсчёт победителя**
    - Победителем становится тот, кто первым уничтожит все фигуры противника или заблокирует их так, что они не смогут двигаться.

#### 4. **Завершение игры**
    - После завершения игры программа предложит начать новую партию:
        ```
        Хотите сыграть снова? (да/нет)
        ```

---

### Пример работы программы

1. **Начало игры:**
    ```
    Добро пожаловать в игру Шашки!
    Вы играете за "O", компьютер за "X".
    Ваш ход.
    Введите координаты фигуры для перемещения (X,Y): 3,5
    Введите целевую клетку для перемещения (X,Y): 4,6
    ```

2. **После хода игрока:**
    ```
    Ход игрока: перемещена фигура с (3,5) на (4,6).
    Ход компьютера.
    ```

3. **Завершение игры:**
    ```
    ПОБЕДА! ВЫ ЗАХВАТИЛИ ВСЕ ФИГУРЫ ПРОТИВНИКА!
    Хотите сыграть снова? (да/нет)
    > нет
    Спасибо за игру!
    ```

---

### Возможные ограничения
- Компьютер не позволяет делать нелегальные ходы, такие как перескок через свою фигуру.
- Программа не поддерживает сложные варианты, такие как «двойные» или «тройные» прыжки, и может потерять фигуру, если игрок попытается выполнить такой ход.

---

### Реализация

Игра реализована с использованием базовых операций для перемещения фигур по доске и проверки валидности хода.
 
.. code-block:: python
    
    """
    Модуль для реализации игры в шашки.
    ==============================================================

    Модуль содержит описание правил игры, инициализации, игрового процесса и условий победы.
    Игра реализована с использованием базовых операций для перемещения фигур по доске и проверки валидности хода.

    Пример использования
    --------------------
    
    .. code-block:: python

        game = Checkers()
        game.start_game()
    
    """
    
    from typing import List, Tuple
    from src.logger.logger import logger  # Импорт логгера

    class Checkers:
        """
        Класс для управления игрой в шашки.
        
        :ivar board: Представляет игровое поле в виде списка списков.
        :vartype board: list[list[str]]
        :ivar player_turn: Указывает, чей сейчас ход, True - игрок, False - компьютер.
        :vartype player_turn: bool
        """
    
        def __init__(self):
            """
            Инициализирует доску и устанавливает начальное состояние игры.
            """
            self.board = [[' ' for _ in range(8)] for _ in range(8)]
            # Установка начального положения фигур
            for i in range(3):
                for j in range(8):
                    if (i + j) % 2 == 0:
                        self.board[i][j] = 'X'  # Компьютер
            for i in range(5,8):
                for j in range(8):
                    if (i + j) % 2 == 0:
                        self.board[i][j] = 'O'  # Игрок
            self.player_turn = True

        def display_board(self) -> None:
            """
            Выводит текущее состояние доски в консоль.
            """
            print('  0 1 2 3 4 5 6 7')
            for i, row in enumerate(self.board):
                print(f'{i} {" ".join(row)}')

        def is_valid_move(self, start: Tuple[int, int], end: Tuple[int, int]) -> bool:
            """
            Проверяет, является ли ход допустимым.

            :param start: Кортеж с координатами начальной позиции фигуры (строка, столбец).
            :type start: tuple[int, int]
            :param end: Кортеж с координатами целевой позиции фигуры (строка, столбец).
            :type end: tuple[int, int]
            :return: True, если ход допустим, иначе False.
            :rtype: bool
            """
            # Проверка, что координаты находятся в пределах доски
            if not (0 <= start[0] < 8 and 0 <= start[1] < 8 and 0 <= end[0] < 8 and 0 <= end[1] < 8):
                return False
            # Получение типа фигуры, которая будет перемещаться
            piece = self.board[start[0]][start[1]]
            # Проверка, что на начальной позиции есть фигура
            if piece == ' ':
                return False
            # Проверка, что целевая клетка свободна
            if self.board[end[0]][end[1]] != ' ':
                return False
            # Рассчитываем разницу в координатах
            row_diff = abs(end[0] - start[0])
            col_diff = abs(end[1] - start[1])
             # Проверяем, что ход является диагональным и на одну клетку
            if row_diff == 1 and col_diff == 1:
                # Проверяем направление движения для игрока ('O')
                if piece == 'O' and end[0] - start[0] < 0:
                    return False
                # Проверяем направление движения для компьютера ('X')
                if piece == 'X' and end[0] - start[0] > 0:
                     return False
                return True
            return False

        def make_move(self, start: Tuple[int, int], end: Tuple[int, int]) -> bool:
            """
            Выполняет ход, перемещая фигуру с начальной позиции в целевую.

            :param start: Кортеж с координатами начальной позиции фигуры.
            :type start: tuple[int, int]
            :param end: Кортеж с координатами целевой позиции фигуры.
            :type end: tuple[int, int]
            :return: True, если ход выполнен, иначе False.
            :rtype: bool
            """
            try:
                # Проверка валидности хода перед его выполнением
                if not self.is_valid_move(start, end):
                    logger.error(f'Недопустимый ход: {start=}, {end=}')
                    return False

                piece = self.board[start[0]][start[1]]
                # Код перемещает фигуру
                self.board[start[0]][start[1]] = ' '
                self.board[end[0]][end[1]] = piece
                return True
            except Exception as ex:
                logger.error(f'Ошибка выполнения хода: {start=}, {end=}', exc_info=ex)
                return False

        def check_winner(self) -> str:
            """
            Проверяет, есть ли победитель.

            :return: "Игрок", если победил игрок, "Компьютер", если победил компьютер, None, если победителя нет.
            :rtype: str | None
            """
            # Подсчитывает количество фигур игрока и компьютера
            player_pieces = 0
            computer_pieces = 0
            for row in self.board:
                for cell in row:
                    if cell == 'O':
                        player_pieces += 1
                    elif cell == 'X':
                        computer_pieces += 1
            # Если у игрока не осталось фигур, победил компьютер
            if player_pieces == 0:
                return 'Компьютер'
            # Если у компьютера не осталось фигур, победил игрок
            if computer_pieces == 0:
                return 'Игрок'
            return None

        def get_player_move(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
             """
             Запрашивает ход у игрока.

             :return: Кортеж из двух кортежей, представляющих начальную и конечную позиции хода.
             :rtype: tuple[tuple[int, int], tuple[int, int]]
             """
             while True:
                 try:
                    start_str = input('Введите координаты фигуры для перемещения (X,Y): ')
                    end_str = input('Введите целевую клетку для перемещения (X,Y): ')
                    start = tuple(map(int, start_str.split(',')))
                    end = tuple(map(int, end_str.split(',')))
                    # Проверка правильности ввода
                    if len(start) != 2 or len(end) != 2:
                         raise ValueError('Неверный формат ввода.')
                    return start, end
                 except ValueError as ve:
                      logger.error('Ошибка ввода координат', exc_info=ve)
                      print('Неверный формат ввода. Пожалуйста, введите координаты в формате "X,Y".')
                 except Exception as ex:
                    logger.error('Неизвестная ошибка ввода', exc_info=ex)
                    print('Неизвестная ошибка. Попробуйте ещё раз.')


        def get_computer_move(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
            """
            Определяет ход компьютера. 
            
             Сейчас компьютер делает случайный допустимый ход.

             :return: Кортеж из двух кортежей, представляющих начальную и конечную позиции хода.
             :rtype: tuple[tuple[int, int], tuple[int, int]]
            """
            import random
            possible_moves = []
            for r in range(8):
                for c in range(8):
                    if self.board[r][c] == 'X':
                        for dr in [-1, 1]:
                            for dc in [-1, 1]:
                                new_r, new_c = r + dr, c + dc
                                if self.is_valid_move((r, c), (new_r, new_c)):
                                    possible_moves.append(((r, c), (new_r, new_c)))
            if possible_moves:
                return random.choice(possible_moves)
            return None, None  # Возвращает None, если нет возможных ходов

        def start_game(self) -> None:
            """
            Запускает игру в шашки.
            """
            print('Добро пожаловать в игру Шашки!')
            print('Вы играете за "O", компьютер за "X".')
            self.display_board()
            while True:
                if self.player_turn:
                    print('Ваш ход.')
                    start, end = self.get_player_move()
                    if self.make_move(start, end):
                         print(f'Ход игрока: перемещена фигура с {start} на {end}.')
                         self.player_turn = False
                    else:
                        print('Недопустимый ход, попробуйте еще раз')
                else:
                    print('Ход компьютера.')
                    start, end = self.get_computer_move()
                    if start and end and self.make_move(start, end):
                        print(f'Ход компьютера: перемещена фигура с {start} на {end}.')
                        self.player_turn = True
                    else:
                        print('У компьютера нет доступных ходов')
                        self.player_turn = True
                self.display_board()
                winner = self.check_winner()
                if winner:
                    print(f'ПОБЕДА! {winner} захватил все фигуры противника!')
                    play_again = input('Хотите сыграть снова? (да/нет) ').lower()
                    if play_again != 'да':
                        print('Спасибо за игру!')
                        break
                    else:
                        self.__init__()
                        print('Начинаем новую игру!')
                        self.display_board()
```