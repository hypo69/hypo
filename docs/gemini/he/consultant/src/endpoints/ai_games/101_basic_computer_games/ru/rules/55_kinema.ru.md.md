# Анализ кода модуля `55_kinema.ru.md`

**Качество кода**

- **Соответствие требованиям к формату кода (1-10)**
    - **Плюсы:**
        - Документ представляет собой подробное описание игры "KINEMA" в формате Markdown, включая правила, инструкции по реализации, пример работы, ограничения и рекомендации.
        - Структура документа логична и хорошо организована с использованием заголовков и списков.
        - Описание игры понятное и чёткое, а формулы для расчётов представлены корректно.
        - Примеры кода и работы программы наглядны и помогают понять принцип игры.
    - **Минусы:**
        - Это текстовое описание, а не исполняемый код Python, поэтому невозможно оценить соответствие требованиям к формату кода Python.
        - Нет использования reStructuredText (RST) и docstring.
        - Не используются `j_loads` или `j_loads_ns`.
        - Нет импортов, функций, классов и т.д.

**Рекомендации по улучшению**

1.  **Преобразование в исполняемый код**: Необходимо реализовать описанную игру на Python, соблюдая требования к оформлению кода.
2.  **Документация reStructuredText (RST)**: Добавить docstring в формате RST для всех модулей, функций и классов, чтобы обеспечить качественную документацию.
3.  **Использование `j_loads` и `j_loads_ns`**: При чтении конфигурационных файлов (если таковые будут) использовать функции `j_loads` или `j_loads_ns` из `src.utils.jjson`.
4.  **Обработка ошибок**: Использовать `try-except` для обработки возможных ошибок, а также `logger.error` для их регистрации.
5.  **Структура кода**: Организовать код в виде функций и классов для обеспечения модульности и читаемости.
6.  **Примеры использования**: Добавить примеры использования функций и классов в формате reStructuredText.
7. **Проверка ввода данных:** Проверить ввод данных на корректность (числовой формат).
8.  **Расширение функциональности**: Добавить уровни сложности и графическое отображение, как было рекомендовано.

**Улучшенный код**
```python
"""
Модуль для игры "KINEMA" - кинематические вычисления.
=======================================================

Этот модуль реализует игру, в которой игрок должен угадать
параметры полёта мяча, брошенного вертикально вверх.
Используются кинематические формулы для вычисления правильных ответов.

Пример использования
--------------------

.. code-block:: python

    game = KinemaGame()
    game.play()
"""

import random
import math  # TODO: добавить импорт для math.isclose
from src.logger.logger import logger  # Импортируем логгер
from typing import Any, List  # TODO: Добавить импорты типов

class KinemaGame:
    """
    Класс, представляющий игру KINEMA.
    
    Содержит методы для инициализации игры, генерации задач,
    проверки ответов и управления игровым процессом.
    """
    def __init__(self):
        """
        Инициализирует игру, задаёт начальные параметры.
        """
        self.gravity = 9.8  # ускорение свободного падения
        self.initial_speed = 0.0  # начальная скорость мяча
        self.time = 0.0 # случайное время для вопроса о скорости

    def _generate_initial_speed(self) -> float:
        """
        Генерирует случайную начальную скорость мяча.
        
        :return: Случайная начальная скорость.
        """
        return random.uniform(10, 25)  #  скорость в диапазоне от 10 до 25 м/с

    def _calculate_max_height(self, initial_speed: float) -> float:
        """
        Вычисляет максимальную высоту, на которую поднимется мяч.
        
        :param initial_speed: Начальная скорость мяча.
        :return: Максимальная высота подъема.
        """
        try: # Проверка для обработки ошибок расчета
            return (initial_speed ** 2) / (2 * self.gravity)
        except Exception as ex:
            logger.error(f'Ошибка при расчете максимальной высоты: {ex}')
            return 0.0

    def _calculate_flight_time(self, initial_speed: float) -> float:
        """
        Вычисляет общее время полета мяча.
        
        :param initial_speed: Начальная скорость мяча.
        :return: Общее время полета.
        """
        try: # Проверка для обработки ошибок расчета
            return (2 * initial_speed) / self.gravity
        except Exception as ex:
            logger.error(f'Ошибка при расчете времени полета: {ex}')
            return 0.0
    
    def _generate_random_time(self, flight_time: float) -> float:
        """
        Генерирует случайное время для вопроса о скорости
        
        :param flight_time: Общее время полета мяча
        :return: Случайное время
        """
        try: # Проверка для обработки ошибок расчета
            return random.uniform(0, flight_time)
        except Exception as ex:
            logger.error(f'Ошибка при генерации случайного времени: {ex}')
            return 0.0

    def _calculate_speed_at_time(self, initial_speed: float, time: float) -> float:
        """
        Вычисляет скорость мяча в заданное время.
        
        :param initial_speed: Начальная скорость мяча.
        :param time: Время, для которого нужно рассчитать скорость.
        :return: Скорость мяча в заданное время.
        """
        try:  # Проверка для обработки ошибок расчета
            return initial_speed - (self.gravity * time)
        except Exception as ex:
            logger.error(f'Ошибка при расчете скорости в заданное время: {ex}')
            return 0.0


    def _check_answer(self, user_answer: float, correct_answer: float) -> bool:
        """
        Проверяет, находится ли ответ игрока в пределах допустимой погрешности.
        
        :param user_answer: Ответ пользователя.
        :param correct_answer: Правильный ответ.
        :return: True, если ответ верен, False - в противном случае.
        """
        if not isinstance(user_answer, (int, float)) or not isinstance(correct_answer, (int, float)):
            logger.error(f'Некорректный тип данных в ответе: {user_answer=}, {correct_answer=}')
            return False

        if math.isclose(user_answer, correct_answer, rel_tol=0.15): #TODO: заменить на math.isclose
             return True
        else:
            return False
    
    def _get_user_input(self, question: str) -> float:
      """
      Получает ввод пользователя, проверяет, что введено число
      
      :param question: Вопрос, задаваемый пользователю
      :return: Введенное число, либо 0.0 в случае некорректного ввода
      """
      while True:
        try:
          user_input = input(question)
          return float(user_input)
        except ValueError:
            logger.error(f'Неверный ввод: {user_input=}, введите число')
            print ('Введите число, пожалуйста!')

    def play(self):
        """
        Запускает игровой процесс.
        
        Организует цикл игры, задаёт вопросы, проверяет ответы и выводит результаты.
        """
        print("Добро пожаловать в игру KINEMA!")
        while True:
            self.initial_speed = self._generate_initial_speed()
            print(f"Мяч был брошен вверх с начальной скоростью {self.initial_speed:.2f} м/с.")

            # Вопрос 1: Максимальная высота
            correct_max_height = self._calculate_max_height(self.initial_speed)
            user_max_height = self._get_user_input("Вопрос 1: Как высоко поднимется мяч? ")
            if self._check_answer(user_max_height, correct_max_height):
                print("Ответ: Близко! Правильный ответ:", f"{correct_max_height:.2f} м")
            else:
                print("Ответ неверный, правильный ответ:", f"{correct_max_height:.2f} м")

            # Вопрос 2: Время полёта
            correct_flight_time = self._calculate_flight_time(self.initial_speed)
            user_flight_time = self._get_user_input("Вопрос 2: Как долго мяч будет в воздухе? ")
            if self._check_answer(user_flight_time, correct_flight_time):
                print("Ответ: Близко! Правильный ответ:", f"{correct_flight_time:.2f} c")
            else:
               print("Ответ неверный, правильный ответ:", f"{correct_flight_time:.2f} c")

            # Вопрос 3: Скорость в случайный момент времени
            self.time = self._generate_random_time(correct_flight_time)
            correct_speed_at_time = self._calculate_speed_at_time(self.initial_speed, self.time)
            user_speed_at_time = self._get_user_input(f"Вопрос 3: Какова будет скорость мяча через {self.time:.2f} секунд? ")
            if self._check_answer(user_speed_at_time, correct_speed_at_time):
                print("Ответ: Близко! Правильный ответ:", f"{correct_speed_at_time:.2f} м/с")
            else:
                 print("Ответ неверный, правильный ответ:", f"{correct_speed_at_time:.2f} м/с")
            
            play_again = input("Хотите сыграть снова? (да/нет): ").lower()
            if play_again != 'да':
                print("Спасибо за игру! До свидания!")
                break

if __name__ == "__main__":
    game = KinemaGame()
    game.play()
```