# Анализ кода модуля `10_batnum.ru.md`

**Качество кода**

- **Соответствие требованиям к формату кода с 1 по 10:**
    -   **Преимущества:**
        - Документ хорошо структурирован и содержит подробное описание игры, ее правил и стратегии.
        - Приведены примеры работы программы, что помогает понять игровой процесс.
        -  Текст написан на русском языке, что соответствует заданию.
    -   **Недостатки:**
         - Документ представлен в формате Markdown, а не в виде Python кода.
         - В тексте отсутствуют docstring, reStructuredText форматирование, и другие элементы, которые должны были присутствовать, согласно инструкции.
         - Не используются `j_loads` или `j_loads_ns`.
         - Нет импортов.
         - Отсутствует обработка ошибок с использованием `logger.error`.

**Рекомендации по улучшению**

1.  **Преобразование в Python:**
    - Необходимо преобразовать текст в Python-скрипт, реализующий логику игры.
    - Добавить необходимые импорты (например, `random`, `src.utils.jjson`, `src.logger.logger`).
2.  **Документация:**
    - Добавить docstring в формате reStructuredText для модуля, функций и классов.
    -   Добавить поясняющие комментарии к коду.
3.  **Обработка ошибок:**
    - Использовать `try-except` блоки с `logger.error` для обработки возможных ошибок при вводе данных пользователем.
4.  **Использование `j_loads`:**
    - Использовать `j_loads` или `j_loads_ns` при загрузке данных, если это необходимо.
5.  **Стратегия компьютера:**
    - Реализовать стратегию компьютера с использованием арифметики по модулю.
6.  **Форматирование:**
    - Соблюдать стандарты PEP 8 для Python кода.

**Улучшенный код**

```python
"""
Модуль для игры в "Butnum" (Битва чисел).
=========================================================================================

Модуль реализует игру, где игрок и компьютер по очереди убирают объекты из кучки.
Цель игры - забрать последний объект или не забрать его, в зависимости от выбранного правила.

Пример использования
--------------------

.. code-block:: python

    game = Batnum()
    game.start_game()
"""

import random # Импорт модуля для генерации случайных чисел
from src.utils.jjson import j_loads_ns # Импорт функции для загрузки данных из JSON
from src.logger.logger import logger # Импорт логгера для обработки ошибок


class Batnum:
    """
    Класс, представляющий игру "Butnum".
    """
    def __init__(self):
        """
        Инициализация параметров игры.
        """
        self.total_objects = 20 # Общее количество объектов в начале игры
        self.min_take = 1 # Минимальное количество объектов, которые можно забрать за один ход
        self.max_take = 3 # Максимальное количество объектов, которые можно забрать за один ход
        self.player_turn = True # Определяет, чей ход: True - игрока, False - компьютера
        self.win_rule = 1 # Правило победы: 1 - забрать последний, 2 - не забрать последний

    def start_game(self):
        """
        Запускает игровой процесс.
        """
        print(f'Игра начинается с {self.total_objects} объектов.')
        self.set_min_max()
        self.choose_first_turn()
        self.set_win_rule()
        self.play_game()

    def set_min_max(self):
        """
        Устанавливает минимальное и максимальное количество объектов для забора.
        """
        while True:
            try:
                self.min_take = int(input('Введите минимальное количество объектов для забора (например, 1): ')) # Получение минимального количества объектов от пользователя
                self.max_take = int(input('Введите максимальное количество объектов для забора (например, 3): ')) # Получение максимального количества объектов от пользователя
                if 1 <= self.min_take <= self.max_take:
                    break
                else:
                    print("Минимальное количество должно быть больше 0 и меньше или равно максимальному.")
            except ValueError:
                 logger.error('Ошибка: Некорректный ввод. Введите целое число.') # Обработка ошибки некорректного ввода

    def choose_first_turn(self):
        """
        Определяет, кто ходит первым: игрок или компьютер.
        """
        while True:
            try:
                choice = int(input('Кто ходит первым? (1 - игрок, 2 - компьютер): ')) # Получение выбора пользователя, кто ходит первым
                if choice in [1, 2]:
                    self.player_turn = choice == 1
                    break
                else:
                    print('Введите 1 или 2.')
            except ValueError:
                 logger.error('Ошибка: Некорректный ввод. Введите целое число.') # Обработка ошибки некорректного ввода

    def set_win_rule(self):
        """
        Устанавливает правило победы в игре.
        """
        while True:
            try:
                self.win_rule = int(input('Выберите правило победы (1 - забрать последний, 2 - не забрать последний): ')) # Получение от пользователя выбранного правила победы
                if self.win_rule in [1, 2]:
                    break
                else:
                    print('Введите 1 или 2.')
            except ValueError:
                 logger.error('Ошибка: Некорректный ввод. Введите целое число.') # Обработка ошибки некорректного ввода

    def play_game(self):
        """
        Основной цикл игры.
        """
        while self.total_objects > 0:
            if self.player_turn:
                self.player_move()
            else:
                self.computer_move()
            self.player_turn = not self.player_turn # Переключение хода между игроком и компьютером

        self.check_winner()
        self.play_again()

    def player_move(self):
        """
        Ход игрока.
        """
        while True:
             try:
                take = int(input(f'Ваш ход: Сколько объектов вы хотите забрать? ({self.min_take}, {self.min_take + 1} ... {self.max_take}): ')) # Получение от пользователя кол-во объектов, которые он хочет забрать
                if self.min_take <= take <= self.max_take and take <= self.total_objects:
                    self.total_objects -= take # Уменьшение кол-ва объектов на столе
                    print(f'Оставшиеся объекты: {self.total_objects}')
                    break
                else:
                    print(f'Введите число от {self.min_take} до {min(self.max_take, self.total_objects)}.')
             except ValueError:
                  logger.error('Ошибка: Некорректный ввод. Введите целое число.') # Обработка ошибки некорректного ввода

    def computer_move(self):
        """
        Ход компьютера.
        """
        optimal_take = self.calculate_optimal_move()
        self.total_objects -= optimal_take # Уменьшение кол-ва объектов на столе
        print(f'Компьютер забрал {optimal_take} объект(а).')
        print(f'Оставшиеся объекты: {self.total_objects}')

    def calculate_optimal_move(self):
         """
        Вычисляет оптимальный ход для компьютера.

        :return: Оптимальное количество объектов для забора.
        :rtype: int
        """
         if self.total_objects > self.max_take:
            for take in range(self.min_take, self.max_take + 1): # Перебор всех возможных вариантов
                if (self.total_objects - take) % (self.max_take + 1) == 0: # Проверка, кратно ли M+1
                   return take # Возврат оптимального варианта хода
         return random.randint(self.min_take, min(self.max_take, self.total_objects)) # Возврат случайного варианта хода

    def check_winner(self):
        """
        Проверяет победителя и выводит сообщение.
        """
        if (self.win_rule == 1 and not self.player_turn) or (self.win_rule == 2 and self.player_turn): # Проверка на победителя
           print('Поздравляем! Вы выиграли!')
        else:
           print('Жаль, вы проиграли!')

    def play_again(self):
        """
        Предлагает сыграть ещё раз.
        """
        while True:
             play_again = input('Хотите сыграть снова? (да/нет): ').lower() # Получение от пользователя решения о начале новой игры
             if play_again == 'да':
                 self.__init__() # Инициализация параметров новой игры
                 self.start_game()
                 break
             elif play_again == 'нет':
                 print('Спасибо за игру!')
                 break
             else:
                  print('Введите "да" или "нет".')

if __name__ == "__main__":
    game = Batnum()
    game.start_game()
```