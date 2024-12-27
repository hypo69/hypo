# Анализ кода модуля KINEMA

**Качество кода**
9
- Плюсы
    - Описание игры и её механики представлено в структурированном и понятном виде.
    - Присутствуют примеры работы программы и возможные ограничения, что помогает в понимании логики игры.
    - Описаны необходимые модули для реализации на Python.
- Минусы
    - Отсутствует код реализации игры.
    - Не хватает инструкций по обработке ошибок ввода.
    - Дополнительные рекомендации по улучшению игры, такие как уровни сложности, представлены лишь в общих словах.

**Рекомендации по улучшению**

1.  **Добавить код реализации:** Включить реализацию игры на Python, используя описанные механики. Это позволит оценить конкретную реализацию и дать более точные рекомендации.
2.  **Реализовать обработку ввода:** Добавить проверку корректности ввода игроком (числовой формат), предусмотреть обработку ошибок ввода и нечисловых значений.
3.  **Уточнить рекомендации по уровням сложности:** Конкретизировать рекомендации по созданию уровней сложности, добавив примеры изменения физических параметров (например, ускорения).
4.  **Реализовать графическое отображение:** Уточнить рекомендацию по графическому отображению траектории мяча, добавив пример реализации.
5.  **Использовать reStructuredText (RST) в docstring:** Добавить docstring для всех функций, используя RST.
6.  **Использовать логгер:** Включить логирование ошибок и исключений, используя `from src.logger.logger import logger`.

**Оптимизированный код**

```python
"""
Модуль для реализации игры KINEMA (Кинематические вычисления).
==============================================================

Игра KINEMA проверяет знания кинематики, в частности, расчеты движения тела,
брошенного вертикально вверх. Программа задает задачу, в которой мяч брошен
вверх с произвольной скоростью, и игрок должен ответить на три вопроса о полете
мяча.

Пример использования
--------------------

.. code-block:: python

    game = KinemaGame()
    game.run()

"""

import random
import math
from src.logger.logger import logger #  Импортируем logger для логирования ошибок

class KinemaGame:
    """
    Класс, реализующий игру KINEMA.

    :ivar float gravity: Ускорение свободного падения (9.8 м/с^2).
    """
    def __init__(self):
        """
        Инициализирует игру KINEMA.
        """
        self.gravity = 9.8

    def calculate_max_height(self, initial_velocity: float) -> float:
        """
        Вычисляет максимальную высоту, на которую поднимется мяч.

        :param initial_velocity: Начальная скорость мяча.
        :return: Максимальная высота подъема мяча.
        """
        try:
            #  Вычисление максимальной высоты подъема мяча по формуле H = V^2 / (2 * g)
            return (initial_velocity ** 2) / (2 * self.gravity)
        except Exception as ex:
            logger.error(f'Ошибка при расчете максимальной высоты: {ex}')
            return 0

    def calculate_flight_time(self, initial_velocity: float) -> float:
        """
        Вычисляет время полета мяча (время подъема и спуска).

        :param initial_velocity: Начальная скорость мяча.
        :return: Общее время полета мяча.
        """
        try:
            #  Вычисление времени полета мяча по формуле T = 2 * V / g
            return (2 * initial_velocity) / self.gravity
        except Exception as ex:
            logger.error(f'Ошибка при расчете времени полета: {ex}')
            return 0

    def calculate_velocity_at_time(self, initial_velocity: float, time: float) -> float:
        """
        Вычисляет скорость мяча в заданный момент времени.

        :param initial_velocity: Начальная скорость мяча.
        :param time: Время, через которое необходимо вычислить скорость.
        :return: Скорость мяча в заданный момент времени.
        """
        try:
            # Вычисление скорости мяча через заданное время по формуле V_t = V - g * t
            return initial_velocity - (self.gravity * time)
        except Exception as ex:
            logger.error(f'Ошибка при расчете скорости в момент времени: {ex}')
            return 0

    def check_answer(self, user_answer: float, correct_answer: float) -> bool:
      """
      Проверяет, находится ли ответ пользователя в пределах 15% от правильного ответа.
      
      :param user_answer: Ответ пользователя.
      :param correct_answer: Правильный ответ.
      :return: True, если ответ пользователя в пределах допустимой погрешности, иначе False.
      """
      try:
        #  Расчет допустимого отклонения от правильного ответа
        tolerance = abs(correct_answer * 0.15)
        #  Проверка, находится ли ответ пользователя в пределах допустимого отклонения
        return abs(user_answer - correct_answer) <= tolerance
      except Exception as ex:
          logger.error(f'Ошибка проверки ответа: {ex}')
          return False

    def run(self):
        """
        Запускает основной процесс игры.
        """
        print("Добро пожаловать в игру KINEMA!")
        while True:
            # Генерация случайной начальной скорости мяча
            initial_velocity = random.randint(10, 20)
            print(f"Мяч был брошен вверх с начальной скоростью {initial_velocity} м/с.")

            # Вычисление правильных ответов
            correct_max_height = self.calculate_max_height(initial_velocity)
            correct_flight_time = self.calculate_flight_time(initial_velocity)
            random_time = random.uniform(0.5, correct_flight_time)
            correct_velocity_at_time = self.calculate_velocity_at_time(initial_velocity, random_time)

            # Вопрос 1: Максимальная высота
            while True:
                try:
                    user_max_height = float(input("Вопрос 1: Как высоко поднимется мяч?\n> "))
                    break
                except ValueError:
                   logger.error('Ошибка ввода: пожалуйста, введите числовое значение.')
                   print('Ошибка ввода: пожалуйста, введите числовое значение.')
            if self.check_answer(user_max_height, correct_max_height):
                print("Ответ: Близко! Правильный ответ:", round(correct_max_height, 5), "м")
            else:
                print("Ответ: Неверно! Правильный ответ:", round(correct_max_height, 5), "м")

            # Вопрос 2: Время полета
            while True:
               try:
                   user_flight_time = float(input("Вопрос 2: Как долго мяч будет в воздухе?\n> "))
                   break
               except ValueError:
                    logger.error('Ошибка ввода: пожалуйста, введите числовое значение.')
                    print('Ошибка ввода: пожалуйста, введите числовое значение.')
            if self.check_answer(user_flight_time, correct_flight_time):
                print("Ответ: Близко! Правильный ответ:", round(correct_flight_time, 5), "с")
            else:
                print("Ответ: Неверно! Правильный ответ:", round(correct_flight_time, 5), "с")

            # Вопрос 3: Скорость в случайный момент времени
            while True:
                try:
                    user_velocity_at_time = float(input(f"Вопрос 3: Какова будет скорость мяча через {round(random_time, 2)} секунд?\n> "))
                    break
                except ValueError:
                    logger.error('Ошибка ввода: пожалуйста, введите числовое значение.')
                    print('Ошибка ввода: пожалуйста, введите числовое значение.')
            if self.check_answer(user_velocity_at_time, correct_velocity_at_time):
                  print("Ответ: Правильно! Отлично, вы угадали.")
            else:
                  print("Ответ: Неверно! Правильный ответ:", round(correct_velocity_at_time, 5), "м/с")


            # Предложение сыграть снова
            play_again = input("Хотите сыграть снова? (да/нет)\n> ").lower()
            if play_again != "да":
                print("Спасибо за игру! До свидания!")
                break

if __name__ == "__main__":
    game = KinemaGame()
    game.run()