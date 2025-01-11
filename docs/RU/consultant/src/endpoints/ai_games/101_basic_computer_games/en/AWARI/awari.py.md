# Анализ кода модуля awari.py

**Качество кода**
9
-  Плюсы
        - Код хорошо структурирован и разбит на логические функции.
        - Присутствует подробная документация в виде docstring.
        - Алгоритм игры реализован в соответствии с правилами.
        - Используются осмысленные имена переменных и функций.
        - Есть проверка на корректность ввода данных пользователем.
        - Используется `random.choice` для выбора хода компьютера.
-  Минусы
    -  Не используются импорты из `src.utils.jjson`.
    -  Отсутствует логирование ошибок через `src.logger.logger`.
    -  Использование глобальной переменной `board` может быть улучшено.
    -  В docstring требуется использовать reStructuredText (RST) формат.

**Рекомендации по улучшению**

1.  **Импорты**: Добавить импорты `from src.utils.jjson import j_loads, j_loads_ns` и `from src.logger.logger import logger`.
2.  **Формат документации**: Переписать docstring в формате RST.
3.  **Логирование ошибок**: Заменить `print` на `logger.error` для отладки и обработки ошибок.
4.  **Глобальная переменная**: Можно инкапсулировать `board` в класс `AWARI`.
5. **Избегание избыточных `try-except`**: Использовать `logger.error` для обработки исключений.

**Оптимизированный код**

```python
"""
Модуль для реализации игры Авари
====================================

Игра "Авари" - это настольная игра, имитирующая традиционную игру Манкала.
В этом модуле реализована упрощенная версия игры, где игрок играет против компьютера.

Правила игры:
  1. Игровое поле состоит из 14 ячеек, пронумерованных от 0 до 13.
     Ячейки 6 и 13 - это "амбары" игроков.
  2. В начале игры в каждой из 12 ячеек (0-5 и 7-12) находится по 4 камня.
  3. Игрок (человек) начинает игру.
  4. Игрок выбирает ячейку со своими камнями (0-5).
  5. Все камни из выбранной ячейки перемещаются по одному в каждую
     следующую ячейку по часовой стрелке, включая свой "амбар".
  6. Если последний камень попал в амбар игрока, игрок имеет право
     сделать еще один ход.
  7. Если последний камень попал в пустую ячейку на стороне игрока, и
     напротив этой ячейки есть камни, то игрок забирает камни из этой
     ячейки и из противоположной в свой амбар.
  8. Компьютер ходит аналогично.
  9. Игра заканчивается, когда все ячейки с камнями становятся пустыми.
  10. Выигрывает игрок, у которого больше камней в амбаре.

Алгоритм:
  1. Инициализировать доску (массив) 14 ячеек с 4 камнями в каждой,
     кроме ячеек 6 и 13, которые равны 0.
  2. Начать цикл "пока не закончена игра".
  3. Ход игрока:
      3.1 Запросить ввод номера ячейки от игрока (от 0 до 5).
      3.2 Переместить камни из выбранной ячейки по часовой стрелке.
      3.3 Проверить, попал ли последний камень в амбар игрока
          (ячейка 6). Если да, то дать игроку еще один ход.
      3.4 Проверить, попал ли последний камень в пустую ячейку
          на стороне игрока. Если да, то захватить камни из этой
          ячейки и из противоположной ячейки.
  4. Ход компьютера (аналогично ходу игрока, но выбор ячейки
     случайный от 7 до 12).
  5. Если все ячейки с камнями пусты, завершить игру.
  6. Вывести результат (количество камней в амбарах игрока и
     компьютера).
  7. Определить победителя (у кого больше камней в амбаре).
"""
import random
from src.logger.logger import logger
# from src.utils.jjson import j_loads, j_loads_ns #TODO delete this line after fix j_loads
# Объявление класса AWARI
class AWARI:
    """
    Класс, реализующий игру Авари.

    :ivar board: Список, представляющий игровое поле.
    """
    def __init__(self):
        """
        Инициализация игровой доски.
        """
        self.board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

    def display_board(self):
        """
        Выводит текущее состояние игровой доски.
        """
        print("----------------------------------------------------")
        print(f"  {self.board[12]:2}  {self.board[11]:2}  {self.board[10]:2}  {self.board[9]:2}  {self.board[8]:2}  {self.board[7]:2}   ")
        print("----------------------------------------------------")
        print(f"{self.board[13]:2}                                 {self.board[6]:2}")
        print("----------------------------------------------------")
        print(f"  {self.board[0]:2}  {self.board[1]:2}  {self.board[2]:2}  {self.board[3]:2}  {self.board[4]:2}  {self.board[5]:2}  ")
        print("----------------------------------------------------")

    def player_turn(self):
        """
        Обрабатывает ход игрока.
        """
        while True:
            try:
                cell = int(input("Выберите ячейку (0-5): "))
                if 0 <= cell <= 5 and self.board[cell] > 0:
                    break
                else:
                    print("Недопустимый выбор. Выберите ячейку с камнями от 0 до 5.")
            except ValueError:
                logger.error("Неверный ввод. Пожалуйста, введите число.")
                print("Неверный ввод. Пожалуйста, введите число.")
                
        stones = self.board[cell]
        self.board[cell] = 0
        current_cell = cell
        
        while stones > 0:
            current_cell = (current_cell + 1) % 14
            self.board[current_cell] += 1
            stones -= 1
    
        # Проверка на дополнительный ход если последний камень попал в амбар игрока
        if current_cell == 6:
            print("Игрок получает дополнительный ход.")
            self.display_board()
            self.player_turn()
            return
            
        # Захват камней
        if 0 <= current_cell <= 5 and self.board[current_cell] == 1:
            opposite_cell = 12 - current_cell
            if self.board[opposite_cell] > 0:
                self.board[6] += self.board[opposite_cell] + 1
                self.board[opposite_cell] = 0
                self.board[current_cell] = 0
                print(f"Игрок захватывает камни из ячеек {current_cell} и {opposite_cell}")
             
    def computer_turn(self):
        """
        Обрабатывает ход компьютера.
        """
        possible_moves = [i for i in range(7, 13) if self.board[i] > 0]
        if not possible_moves:
            return  # Если нет доступных ходов для компьютера, выйти
        
        cell = random.choice(possible_moves)
        print(f"Компьютер выбирает ячейку {cell}")
        stones = self.board[cell]
        self.board[cell] = 0
        current_cell = cell

        while stones > 0:
            current_cell = (current_cell + 1) % 14
            self.board[current_cell] += 1
            stones -= 1

        # Проверка на дополнительный ход если последний камень попал в амбар компьютера
        if current_cell == 13:
            print("Компьютер получает дополнительный ход.")
            self.display_board()
            self.computer_turn()
            return

        # Захват камней
        if 7 <= current_cell <= 12 and self.board[current_cell] == 1:
            opposite_cell = 12 - current_cell
            if self.board[opposite_cell] > 0:
                self.board[13] += self.board[opposite_cell] + 1
                self.board[opposite_cell] = 0
                self.board[current_cell] = 0
                print(f"Компьютер захватывает камни из ячеек {current_cell} и {opposite_cell}")

    def is_game_over(self):
        """
        Проверяет, закончена ли игра.

        :return: True, если игра окончена, иначе False.
        """
        player_side_empty = all(self.board[i] == 0 for i in range(0, 6))
        computer_side_empty = all(self.board[i] == 0 for i in range(7, 13))
        return player_side_empty or computer_side_empty

    def calculate_winner(self):
        """
        Определяет победителя и выводит результаты.
        """
        player_score = self.board[6]
        computer_score = self.board[13]
    
        print(f"Игрок: {player_score} очков")
        print(f"Компьютер: {computer_score} очков")
    
        if player_score > computer_score:
            print("Вы победили!")
        elif computer_score > player_score:
            print("Компьютер победил!")
        else:
            print("Ничья!")
            
# Инициализация игры
game = AWARI()
# Основной игровой цикл
while True:
    game.display_board()
    game.player_turn()
    if game.is_game_over():
        break
    game.display_board()
    game.computer_turn()
    if game.is_game_over():
       break
    
# После завершения игры
game.display_board()
game.calculate_winner()
```