# Анализ кода модуля `4_awari.ru.md`

**Качество кода**
    -   **Соответствие требованиям к формату кода (1-10):** 
        -   **Преимущества:**
            -   Представлен четкий алгоритм игры.
            -   Хорошее описание правил игры.
            -   Присутствует пошаговая инструкция по реализации.
            -   Есть пример работы программы.
            -   Указаны возможные ограничения.
        -   **Недостатки:**
             -   Код в формате Markdown, а не Python.
             -   Нет комментариев в reStructuredText (RST) формате.
             -   Нет импортов.
             -   Не используется `j_loads` или `j_loads_ns`.
             -   Не реализованы функции и классы.
             -   Не используется `logger.error`.
             -   Нет примеров docstring в формате RST.

**Рекомендации по улучшению**

1.  **Преобразование в Python**: Необходимо преобразовать текстовое описание правил игры и алгоритма в исполняемый код на Python.
2.  **Формат документации**: Добавить docstrings в формате reStructuredText (RST) для всех функций, классов и методов.
3.  **Использование `j_loads`**: В случае работы с JSON файлами использовать `j_loads` или `j_loads_ns` из `src.utils.jjson`.
4.  **Обработка ошибок**: Применять `logger.error` для регистрации ошибок вместо стандартных `try-except` блоков, где это возможно.
5.  **Импорты**: Добавить необходимые импорты для `logger` и других используемых модулей.
6.  **Структура кода**: Разбить код на функции и классы для лучшей организации и переиспользования.
7.  **Комментарии**: Добавить комментарии в формате `#` для пояснения логики кода.

**Улучшенный код**

```python
"""
Модуль для реализации игры Авари (Awari)
=======================================

Модуль содержит функции и классы для управления
игровым процессом Авари, включая инициализацию,
ходы игроков, проверку условий и завершение игры.

Пример использования
---------------------

.. code-block:: python

    game = AwariGame()
    game.play()
"""

import random # импортируем модуль random для хода компьютера
from src.logger.logger import logger # импортируем логгер для обработки ошибок
from typing import List, Tuple # импортируем типы данных

class AwariGame:
    """
    Класс, представляющий игру Авари.

    :ivar board: Список, представляющий игровую доску.
    :vartype board: List[int]
    :ivar player_house_index: Индекс дома игрока на доске.
    :vartype player_house_index: int
    :ivar computer_house_index: Индекс дома компьютера на доске.
    :vartype computer_house_index: int
    """

    def __init__(self):
        """
        Инициализирует игровую доску и начальные параметры.
        """
        self.board = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4] # Инициализация доски
        self.player_house_index = 0 # Индекс дома игрока
        self.computer_house_index = 7 # Индекс дома компьютера

    def display_board(self):
        """
        Выводит текущее состояние игровой доски.
        """
        print("Текущая доска:") # Вывод заголовка
        print(self.board) # Вывод текущего состояния доски

    def is_valid_move(self, player: str, pit_index: int) -> bool:
        """
        Проверяет, является ли выбранный ход валидным.

        :param player: Строка, представляющая игрока ('player' или 'computer').
        :type player: str
        :param pit_index: Индекс выбранной ямы на доске.
        :type pit_index: int
        :return: True, если ход валидный, иначе False.
        :rtype: bool
        """
        if pit_index < 1 or pit_index > 6 and player == 'player': # Проверка для игрока
            logger.error(f"Неверный выбор ямы: {pit_index} для игрока.") # Логирование ошибки
            return False
        if pit_index < 8 or pit_index > 13 and player == 'computer': # Проверка для компьютера
            logger.error(f"Неверный выбор ямы: {pit_index} для компьютера.") # Логирование ошибки
            return False
        if self.board[pit_index] == 0: # Проверка, не пустая ли яма
            logger.error(f"Выбранная яма {pit_index} пуста.")  # Логирование ошибки
            return False
        return True # Возврат True, если ход валиден

    def make_move(self, player: str, pit_index: int) -> bool:
        """
        Выполняет ход игрока или компьютера.

        :param player: Строка, представляющая игрока ('player' или 'computer').
        :type player: str
        :param pit_index: Индекс выбранной ямы на доске.
        :type pit_index: int
        :return: True, если ход выполнен, иначе False.
        :rtype: bool
        """
        try: # обработка ошибок при ходе
            if not self.is_valid_move(player, pit_index): # Проверка на валидность хода
                return False # Возврат False если ход не валиден

            stones = self.board[pit_index] # Получение количества камней из ямы
            self.board[pit_index] = 0  # Очистка ямы

            current_index = pit_index # Установка текущего индекса
            while stones > 0: # Пока есть камни
                current_index = (current_index + 1) % len(self.board) # Увеличение индекса, пропускаем дома противников
                if player == 'player' and current_index == self.computer_house_index: # если ход игрока и текущий индекс - дом компьютера
                     continue # пропускаем дом компьютера
                if player == 'computer' and current_index == self.player_house_index: # если ход компьютера и текущий индекс - дом игрока
                    continue # пропускаем дом игрока
                self.board[current_index] += 1 # Добавление камня
                stones -= 1 # Уменьшение количества камней

            # Проверка захвата
            if player == 'player' and 1 <= current_index <=6 and self.board[current_index] == 1:
               opposite_index = 14-current_index # Вычисление противоположного индекса
               if self.board[opposite_index] > 0: # проверка на наличие камней в противоположной яме
                    self.board[self.player_house_index] += self.board[current_index] + self.board[opposite_index] # перемещение камней в дом игрока
                    self.board[current_index] = 0 # очистка текущей ямы
                    self.board[opposite_index] = 0 # очистка противоположной ямы

            if player == 'computer' and 8 <= current_index <=13 and self.board[current_index] == 1:
               opposite_index = 14-current_index # Вычисление противоположного индекса
               if self.board[opposite_index] > 0: # проверка на наличие камней в противоположной яме
                    self.board[self.computer_house_index] += self.board[current_index] + self.board[opposite_index] # перемещение камней в дом компьютера
                    self.board[current_index] = 0 # очистка текущей ямы
                    self.board[opposite_index] = 0 # очистка противоположной ямы


            # Проверка дополнительного хода
            if player == 'player' and current_index == self.player_house_index:
                return True # Возврат True для дополнительного хода
            if player == 'computer' and current_index == self.computer_house_index:
                return True # Возврат True для дополнительного хода


            return False # Возврат False если доп хода нет
        except Exception as e: # перехват ошибок
            logger.error(f"Ошибка при выполнении хода игрока: {e}") # логирование ошибки
            return False # Возврат False в случае ошибки

    def computer_move(self) -> int:
         """
         Осуществляет ход компьютера.

         :return: Индекс выбранной ямы для хода компьютера.
         :rtype: int
         """
         for i in range(8, 14): # Цикл по ямам компьютера
            if self.board[i] > 0:  # Выбор первой непустой ямы
                return i # Возврат индекса ямы
         return -1 # Возврат -1 если нет доступных ходов

    def check_game_end(self) -> bool:
        """
        Проверяет, закончилась ли игра.

        :return: True, если игра закончилась, иначе False.
        :rtype: bool
        """
        player_side_empty = all(self.board[i] == 0 for i in range(1, 7)) # проверка пуста ли сторона игрока
        computer_side_empty = all(self.board[i] == 0 for i in range(8, 14)) # проверка пуста ли сторона компьютера
        if player_side_empty or computer_side_empty:
             return True # Возврат True если игра окончена
        return False # Возврат False если игра не окончена

    def calculate_scores(self) -> Tuple[int, int]:
        """
        Подсчитывает очки игроков.

        :return: Кортеж, содержащий количество очков игрока и компьютера.
        :rtype: Tuple[int, int]
        """
        player_score = self.board[self.player_house_index] # Получение счета игрока
        computer_score = self.board[self.computer_house_index] # Получение счета компьютера
        return player_score, computer_score # Возврат счета игроков

    def announce_winner(self, player_score: int, computer_score: int):
        """
        Объявляет победителя игры.

        :param player_score: Количество очков игрока.
        :type player_score: int
        :param computer_score: Количество очков компьютера.
        :type computer_score: int
        """
        print("Игра окончена!") # Вывод сообщения об окончании игры
        print(f"Вы набрали {player_score} бобов. Компьютер набрал {computer_score} бобов.") # Вывод счета игроков
        if player_score > computer_score: # Сравнение очков
            print("Вы победили!") # Вывод сообщения о победе игрока
        elif computer_score > player_score:
            print("Компьютер победил!") # Вывод сообщения о победе компьютера
        else:
            print("Ничья!") # Вывод сообщения о ничьей

    def play(self):
        """
        Запускает основной игровой цикл.
        """
        print("Добро пожаловать в игру Awari!") # Приветствие игрока
        self.display_board() # Отображение доски
        player_turn = True # Установка хода игрока

        while not self.check_game_end(): # Пока игра не закончена
             if player_turn: # Если ход игрока
                while True: # Бесконечный цикл для хода игрока
                    try: # обработка ошибок ввода
                        pit = int(input("Ваш ход. Выберите яму (1-6): ")) # запрос на ввод ямы
                        if self.make_move('player', pit): # Выполнение хода
                             self.display_board() # Отображение доски
                             continue # дополнительный ход
                        break # выход из цикла если хода нет
                    except ValueError: # обработка ошибки при вводе
                        logger.error("Некорректный ввод, введите число от 1 до 6.") # Логирование ошибки
                player_turn = False # Передача хода компьютеру
             else: # Если ход компьютера
                 print("Ход компьютера...") # Вывод сообщения
                 pit = self.computer_move() # Выбор ямы для хода
                 if pit == -1: # Если компьютер не может сделать ход
                     player_turn = True # Передача хода игроку
                 else:
                     if self.make_move('computer', pit): # Выполнение хода компьютера
                         self.display_board() # Отображение доски
                         continue  # Дополнительный ход
                     player_turn = True # Передача хода игроку
                 self.display_board() # Отображение доски

        player_score, computer_score = self.calculate_scores()  # Получение счета игроков
        self.announce_winner(player_score, computer_score) # Объявление победителя

if __name__ == "__main__":
    game = AwariGame() # создание объекта игры
    game.play() # начало игры
```