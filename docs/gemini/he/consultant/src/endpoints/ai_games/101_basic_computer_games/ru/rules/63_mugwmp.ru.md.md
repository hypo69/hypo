# Анализ кода модуля `63_mugwmp.ru.md`

**Качество кода**

- **Соответствие требованиям к формату кода (1-10)**:
    -  **Преимущества**:
        - Документ четко структурирован, используя Markdown, что облегчает чтение и понимание.
        - Даны пошаговые инструкции для реализации игры.
        - Присутствуют примеры работы программы, что помогает понять логику игры.
        - Описаны возможные ограничения и рекомендации по улучшению.
    - **Недостатки**:
        - Код представлен в виде инструкций и описаний, а не в виде исполняемого кода.
        - Отсутствуют docstring и reStructuredText (RST) комментарии, которые необходимы для документирования кода.
        - Нет обработки ошибок, так как это не код, а описание.

**Рекомендации по улучшению**

1.  **Преобразовать Markdown в Python:** Создать исполняемый файл Python на основе данных инструкций.
2.  **Добавить docstring и RST комментарии:** Каждая функция, метод и класс должны быть документированы с использованием docstring и RST-формата.
3.  **Использовать `logger`:** Все ошибки должны регистрироваться с использованием `src.logger.logger`.
4.  **Обработка ошибок:** Добавить обработку ошибок с помощью `try-except`, при этом использовать `logger.error` для записи ошибок.
5.  **Структура кода:** Разделить код на функции и классы для улучшения читаемости и поддержки.

**Улучшенный код**

```python
"""
Модуль для игры MUGWMP (Охота на Магвампов).
=========================================================================================

Модуль содержит логику игры, включая инициализацию, основной игровой процесс и завершение.
Используются случайные числа для размещения Магвампов и расчет расстояния до них.

Пример использования
--------------------

Пример запуска игры:

.. code-block:: python

    game = MugwmpGame()
    game.start_game()
"""
import random # Импорт модуля random для генерации случайных чисел
import math # Импорт модуля math для математических операций
from src.logger.logger import logger # Импорт логгера

class MugwmpGame:
    """
    Класс, реализующий игру "Охота на Магвампов".

    :ivar grid_size: Размер сетки (10x10 по умолчанию).
    :vartype grid_size: int
    :ivar num_mugwumps: Количество Магвампов в игре (4 по умолчанию).
    :vartype num_mugwumps: int
    :ivar mugwump_positions: Список координат Магвампов.
    :vartype mugwump_positions: list[tuple[int, int]]
    :ivar moves: Количество сделанных ходов.
    :vartype moves: int
    :ivar caught_mugwumps: Количество пойманных Магвампов.
    :vartype caught_mugwumps: int
    """

    def __init__(self, grid_size: int = 10, num_mugwumps: int = 4) -> None:
        """
        Инициализирует игру с заданным размером сетки и количеством Магвампов.

        :param grid_size: Размер сетки.
        :type grid_size: int
        :param num_mugwumps: Количество Магвампов.
        :type num_mugwumps: int
        """
        self.grid_size = grid_size # Размер игровой сетки
        self.num_mugwumps = num_mugwumps # Количество Магвампов
        self.mugwump_positions = [] # Позиции Магвампов
        self.moves = 0 # Количество ходов
        self.caught_mugwumps = 0 # Количество пойманных Магвампов

    def _generate_mugwump_positions(self) -> None:
        """
        Генерирует случайные позиции для Магвампов на игровой сетке.
        Позиции хранятся в self.mugwump_positions
        """
        self.mugwump_positions = [] # Очистка старых позиций
        while len(self.mugwump_positions) < self.num_mugwumps: # Генерация новых позиций
            x = random.randint(1, self.grid_size) # Случайная координата x
            y = random.randint(1, self.grid_size) # Случайная координата y
            if (x, y) not in self.mugwump_positions: # Проверка на уникальность
                self.mugwump_positions.append((x, y)) # Добавление позиции в список

    def _calculate_distance(self, x1: int, y1: int, x2: int, y2: int) -> float:
        """
        Вычисляет расстояние между двумя точками.

        :param x1: Координата X первой точки.
        :type x1: int
        :param y1: Координата Y первой точки.
        :type y1: int
        :param x2: Координата X второй точки.
        :type x2: int
        :param y2: Координата Y второй точки.
        :type y2: int
        :return: Расстояние между точками.
        :rtype: float
        """
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2) # Вычисление расстояния

    def _get_closest_mugwump_distance(self, x: int, y: int) -> float:
        """
        Вычисляет расстояние до ближайшего Магвампа.

        :param x: Координата X игрока.
        :type x: int
        :param y: Координата Y игрока.
        :type y: int
        :return: Расстояние до ближайшего Магвампа.
        :rtype: float
        """
        if not self.mugwump_positions:
            return float('inf') # Если нет Магвампов, возвращаем бесконечность

        min_distance = float('inf') # Инициализация минимального расстояния
        for mx, my in self.mugwump_positions: # Перебор всех позиций Магвампов
            distance = self._calculate_distance(x, y, mx, my) # Расчет расстояния
            min_distance = min(min_distance, distance) # Находим минимальное расстояние
        return min_distance # Возврат минимального расстояния

    def _is_mugwump_caught(self, x: int, y: int) -> bool:
        """
        Проверяет, пойман ли Магвамп.

        :param x: Координата X игрока.
        :type x: int
        :param y: Координата Y игрока.
        :type y: int
        :return: True, если Магвамп пойман, иначе False.
        :rtype: bool
        """
        if (x, y) in self.mugwump_positions: # Проверка на совпадение координат
            self.mugwump_positions.remove((x, y)) # Удаление Магвампа из списка
            self.caught_mugwumps += 1 # Увеличение количества пойманных Магвампов
            return True # Возврат True, если Магвамп пойман
        return False # Возврат False, если Магвамп не пойман

    def start_game(self) -> None:
        """
        Начинает игру MUGWMP.
        """
        print("Добро пожаловать в MUGWMP!") # Приветствие
        print(f"Ваша задача — найти и поймать {self.num_mugwumps} Магвампов, спрятанных на сетке {self.grid_size}x{self.grid_size}.")
        print("Каждый ход вы вводите координаты, а программа сообщает, насколько близко вы к Магвампу.")
        print("Выигрывает тот, кто поймает всех Магвампов за минимальное количество ходов!")
        print("Удачи!\n")

        while True: # Основной цикл игры
            self._generate_mugwump_positions() # Генерация позиций Магвампов
            self.moves = 0 # Обнуление количества ходов
            self.caught_mugwumps = 0 # Обнуление количества пойманных Магвампов
            while self.caught_mugwumps < self.num_mugwumps:  # Игра продолжается, пока все Магвампы не будут пойманы
                self.moves += 1 # Увеличение количества ходов
                try:
                    coord_input = input("Введите координаты (X, Y): ") # Запрос координат
                    x, y = map(int, coord_input.split(',')) # Разделение координат
                    if not (1 <= x <= self.grid_size and 1 <= y <= self.grid_size):
                      logger.error(f"Недопустимые координаты: {x=}, {y=}. Координаты должны быть от 1 до {self.grid_size}.") # Логгирование ошибки
                      print(f"Недопустимые координаты. Координаты должны быть от 1 до {self.grid_size}.")
                      continue # Повторный ввод координат
                except ValueError as ex:
                    logger.error(f"Ошибка ввода: {ex}", exc_info=True) # Логгирование ошибки
                    print("Неверный формат ввода. Пожалуйста, введите координаты в формате 'X, Y'.")
                    continue # Повторный ввод координат
                except Exception as ex:
                    logger.error(f"Неизвестная ошибка: {ex}", exc_info=True) # Логгирование ошибки
                    print("Произошла неизвестная ошибка. Попробуйте еще раз.")
                    continue # Повторный ввод координат
                if self._is_mugwump_caught(x, y): # Проверка на поимку Магвампа
                    print(f"Вы поймали Магвампа! Осталось: {self.num_mugwumps - self.caught_mugwumps}.") # Сообщение о поимке
                else:
                    distance = self._get_closest_mugwump_distance(x, y) # Расчет расстояния
                    print(f"Расстояние до ближайшего Магвампа: {distance:.1f}") # Сообщение о расстоянии
            print(f"Поздравляем! Вы поймали всех Магвампов!") # Сообщение о победе
            print(f"Вам потребовалось {self.moves} ходов.") # Вывод количества ходов
            play_again = input("Хотите сыграть снова? (да/нет): ").lower() # Запрос на повтор игры
            if play_again != 'да': # Проверка ответа
                print("Спасибо за игру!")
                break # Завершение игры

if __name__ == '__main__':
    game = MugwmpGame() # Создание экземпляра игры
    game.start_game() # Запуск игры
```