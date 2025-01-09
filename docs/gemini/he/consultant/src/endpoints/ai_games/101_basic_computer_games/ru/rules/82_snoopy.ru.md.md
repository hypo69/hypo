# Анализ кода модуля `82_snoopy.ru.md`

**Качество кода**
- **Соответствие требованиям к формату кода с 1 по 10:**
    - **Преимущества:**
        - Документ содержит подробное описание игры "SNOOPY", включая правила, пошаговую инструкцию, примеры работы и возможные ограничения.
        - Присутствуют рекомендации по реализации игры на Python с указанием используемых модулей и структур.
        - Предложены варианты улучшений игры.
    - **Недостатки:**
        - Код отсутствует. Это не Python, а Markdown, следовательно, не может быть выполнено никаких проверок или преобразований, специфичных для Python.
        - Документ не имеет никаких инструкций по формату reStructuredText (RST) или docstring, так как это не код Python.

**Рекомендации по улучшению**
- Документ необходимо преобразовать в исполняемый файл Python.
- Создать структуру кода, который реализует описанные правила игры.
- Добавить reStructuredText комментарии к модулям, функциям, методам и переменным после реализации кода.
- Реализовать базовую логику игры.
- Добавить обработку ошибок и логирование с помощью `from src.logger.logger import logger`.
- Продумать структуру модулей и классов.
- Добавить тесты для проверки корректности кода.

**Улучшенный код**
```python
"""
Модуль для реализации игры SNOOPY.
=========================================================================================

Этот модуль содержит логику для игры SNOOPY, в которой игрок ищет спрятанный дом на сетке.

Пример использования
--------------------

Пример запуска игры:

.. code-block:: python

    from src.game.snoopy import SnoopyGame

    game = SnoopyGame()
    game.start_game()
"""
import random
import math
from src.logger.logger import logger # Импорт логгера для логирования ошибок

class SnoopyGame:
    """
    Класс, реализующий игру SNOOPY.

    :ivar int grid_size: Размер игровой сетки.
    :ivar tuple home_coordinates: Координаты дома на сетке.
    :ivar int moves: Количество ходов, сделанных игроком.
    :ivar bool game_over: Флаг, указывающий, закончилась ли игра.
    """
    def __init__(self, grid_size: int = 10):
        """
        Инициализирует игру SNOOPY.

        :param grid_size: Размер игровой сетки (по умолчанию 10).
        """
        self.grid_size = grid_size # Инициализация размера сетки
        self.home_coordinates = self._generate_home_coordinates() # Генерация случайных координат дома
        self.moves = 0 # Инициализация количества ходов
        self.game_over = False # Инициализация флага конца игры

    def _generate_home_coordinates(self) -> tuple:
        """
        Генерирует случайные координаты дома на сетке.

        :return: Координаты дома в формате (x, y).
        """
        try:
            x = random.randint(1, self.grid_size) # Генерация случайной координаты x
            y = random.randint(1, self.grid_size) # Генерация случайной координаты y
            return (x, y)
        except Exception as ex:
            logger.error('Ошибка при генерации координат дома', ex)
            return (1, 1) # Возвращает дефолтные координаты в случае ошибки

    def _calculate_distance(self, player_x: int, player_y: int) -> float:
        """
        Вычисляет расстояние между игроком и домом.

        :param player_x: Координата X игрока.
        :param player_y: Координата Y игрока.
        :return: Расстояние между игроком и домом.
        """
        try:
            home_x, home_y = self.home_coordinates # Получение координат дома
            distance = math.sqrt((player_x - home_x)**2 + (player_y - home_y)**2) # Вычисление расстояния по формуле
            return distance
        except Exception as ex:
            logger.error('Ошибка при вычислении расстояния', ex)
            return 0.0 # Возвращает 0 в случае ошибки

    def _check_win(self, player_x: int, player_y: int) -> bool:
        """
        Проверяет, угадал ли игрок координаты дома.

        :param player_x: Координата X игрока.
        :param player_y: Координата Y игрока.
        :return: True, если игрок угадал координаты дома, False иначе.
        """
        return (player_x, player_y) == self.home_coordinates # Сравнение координат игрока и дома

    def start_game(self):
         """
         Начинает игру SNOOPY.
         """
         print("Добро пожаловать в SNOOPY!")
         print("Ваша задача — найти спрятанный дом, выбирая координаты на сетке.")
         print("Каждый ход вы вводите координаты, а программа сообщает, насколько близко вы к дому.")
         print("Выигрывает тот, кто найдёт дом за минимальное количество ходов!")
         print("Удачи!")

         while not self.game_over:
            try:
                player_input = input("Введите координаты (X, Y): ") # Запрос координат у игрока
                player_x, player_y = map(int, player_input.split(',')) # Разделение ввода на координаты
                if not (1 <= player_x <= self.grid_size and 1 <= player_y <= self.grid_size):
                    print(f"Координаты должны быть в диапазоне от 1 до {self.grid_size}.")
                    continue

                self.moves += 1 # Увеличение количества ходов
                distance = self._calculate_distance(player_x, player_y) # Вычисление расстояния
                print(f"Расстояние до дома: {distance:.1f}")

                if self._check_win(player_x, player_y): # Проверка, угадал ли игрок
                    print("Вы нашли дом! Поздравляем!")
                    self.game_over = True
            except ValueError:
                 logger.error('Некорректный ввод. Пожалуйста, введите координаты в формате "X, Y".')
            except Exception as ex:
                 logger.error('Произошла ошибка во время игры', ex)
                 break

         print(f"Вам потребовалось {self.moves} ходов.")
         play_again = input("Хотите сыграть снова? (да/нет): ") # Запрос на повторную игру

         if play_again.lower() == "да":
            self.__init__() # Перезапуск игры с новыми параметрами
            self.start_game()
         else:
            print("Спасибо за игру!")

if __name__ == "__main__":
    game = SnoopyGame() # Создание объекта игры
    game.start_game() # Запуск игры
```