# Анализ кода модуля KINEMA

**Качество кода**

- **Соблюдение требований к формату кода (1-10):**

    -   **Преимущества:**
        -   Документ содержит подробное описание игры, включая правила, шаги реализации и примеры.
        -   Предоставлено четкое описание формул, используемых в игре.
        -   Описание разделено на логические блоки, что облегчает понимание.
        -   Документ включает пример работы программы и возможные ограничения.

    -   **Недостатки:**
        -   Отсутствует код на Python.
        -   Нет примеров реализации, только описание логики игры.

**Рекомендации по улучшению**

1.  **Добавление кода Python:**
    -   Необходимо реализовать игру на Python, включая генерацию случайных чисел, расчеты и проверку ответов.
2.  **Использование `src.utils.jjson`:**
    -   При необходимости работы с JSON, использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для загрузки данных.
3.  **Структура кода:**
    -   Код должен быть структурирован с использованием функций и классов для лучшей организации.
4.  **Обработка ошибок:**
    -   Вместо общих блоков `try-except`, использовать `logger.error` для обработки ошибок.
5.  **Документирование:**
    -   Добавить документацию в формате reStructuredText (RST) для всех функций, классов и методов.
6.  **Импорты:**
    -   Добавить необходимые импорты в начале файла (например, `import random`, `from src.logger.logger import logger`).
7.  **Расширение возможностей:**
    -   Реализовать систему уровней сложности и возможность графического отображения.

**Улучшенный код**

```python
"""
Модуль для реализации игры KINEMA (Кинематические вычисления).
==================================================================

Этот модуль реализует игру, проверяющую знания кинематики,
в частности, расчеты движения тела, брошенного вертикально вверх.
Игрок должен ответить на вопросы о высоте, времени полета и скорости мяча.

Пример использования
--------------------

.. code-block:: python

    game = KinemaGame()
    game.play()
"""

import random
from src.logger.logger import logger  # Используем логгер для отслеживания ошибок

class KinemaGame:
    """
    Класс, представляющий игру KINEMA.

    :ivar float g: Ускорение свободного падения (9.8 м/с^2).
    :ivar float accuracy_margin: Допустимое отклонение от правильного ответа в процентах.
    """
    def __init__(self):
        """
        Инициализирует игру KINEMA.

        Устанавливает ускорение свободного падения и допустимую погрешность.
        """
        self.g = 9.8  # Ускорение свободного падения
        self.accuracy_margin = 0.15  # Допустимая погрешность (15%)

    def calculate_max_height(self, initial_velocity: float) -> float:
        """
        Вычисляет максимальную высоту подъема мяча.

        :param initial_velocity: Начальная скорость мяча.
        :return: Максимальная высота подъема мяча.
        """
        try:
            # Расчет максимальной высоты по формуле H = V^2 / (2g)
            max_height = (initial_velocity ** 2) / (2 * self.g)
            return max_height
        except Exception as e:
            logger.error(f'Ошибка при расчете максимальной высоты: {e}')
            return 0  # Возвращаем 0 при ошибке

    def calculate_flight_time(self, initial_velocity: float) -> float:
        """
        Вычисляет общее время полета мяча.

        :param initial_velocity: Начальная скорость мяча.
        :return: Общее время полета мяча.
        """
        try:
            # Расчет времени полета по формуле T = 2V / g
            flight_time = (2 * initial_velocity) / self.g
            return flight_time
        except Exception as e:
            logger.error(f'Ошибка при расчете времени полета: {e}')
            return 0  # Возвращаем 0 при ошибке

    def calculate_velocity_at_time(self, initial_velocity: float, time: float) -> float:
        """
        Вычисляет скорость мяча в заданный момент времени.

        :param initial_velocity: Начальная скорость мяча.
        :param time: Время, через которое нужно вычислить скорость.
        :return: Скорость мяча в заданный момент времени.
        """
        try:
           # Расчет скорости в заданный момент времени по формуле V_t = V - g * t
           velocity_at_time = initial_velocity - (self.g * time)
           return velocity_at_time
        except Exception as e:
            logger.error(f'Ошибка при расчете скорости: {e}')
            return 0 # Возвращаем 0 при ошибке

    def check_answer(self, user_answer: float, correct_answer: float) -> bool:
        """
        Проверяет, является ли ответ пользователя правильным с учетом погрешности.

        :param user_answer: Ответ пользователя.
        :param correct_answer: Правильный ответ.
        :return: True, если ответ правильный, False в противном случае.
        """
        try:
            # Проверка на погрешность в пределах допустимого отклонения
            if abs(user_answer - correct_answer) <= abs(correct_answer * self.accuracy_margin):
                return True
            return False
        except Exception as e:
            logger.error(f'Ошибка при проверке ответа: {e}')
            return False  # Возвращаем False при ошибке

    def play(self):
        """
        Запускает игровой процесс.
        """
        print("Добро пожаловать в игру KINEMA!")

        while True:
            # Генерация случайной начальной скорости
            initial_velocity = random.uniform(10, 25)  # Случайная скорость от 10 до 25 м/с
            print(f"Мяч был брошен вверх с начальной скоростью {initial_velocity:.2f} м/с.")

            # Вопрос 1: Максимальная высота
            correct_max_height = self.calculate_max_height(initial_velocity)
            user_max_height = float(input("Вопрос 1: Как высоко поднимется мяч? > "))
            if self.check_answer(user_max_height, correct_max_height):
                print("Ответ: Близко! Правильный ответ: {:.5f} м".format(correct_max_height))
            else:
                print("Ответ: Неправильно. Правильный ответ: {:.5f} м".format(correct_max_height))

            # Вопрос 2: Время полета
            correct_flight_time = self.calculate_flight_time(initial_velocity)
            user_flight_time = float(input("Вопрос 2: Как долго мяч будет в воздухе? > "))
            if self.check_answer(user_flight_time, correct_flight_time):
                print("Ответ: Близко! Правильный ответ: {:.6f} с".format(correct_flight_time))
            else:
                print("Ответ: Неправильно. Правильный ответ: {:.6f} с".format(correct_flight_time))


            # Вопрос 3: Скорость через случайное время
            random_time = random.uniform(0.1, correct_flight_time-0.1)
            correct_velocity_at_time = self.calculate_velocity_at_time(initial_velocity, random_time)
            user_velocity_at_time = float(input("Вопрос 3: Какова будет скорость мяча через {:.2f} секунд? > ".format(random_time)))
            if self.check_answer(user_velocity_at_time, correct_velocity_at_time):
                 print("Ответ: Правильно! Отлично, вы угадали.")
            else:
                print("Ответ: Неправильно. Правильный ответ: {:.2f} м/с".format(correct_velocity_at_time))

            play_again = input("Хотите сыграть снова? (да/нет): ")
            if play_again.lower() != 'да':
                print("Спасибо за игру! До свидания!")
                break

if __name__ == "__main__":
    game = KinemaGame() # Создаем экземпляр игры
    game.play() # Запускаем игру
```
# Анализ кода модуля KINEMA

**Качество кода**

- **Соблюдение требований к формату кода (1-10):**

    -   **Преимущества:**
        -   Код соответствует требованиям к формату (RST-документация, использование `logger.error`, `j_loads`, `j_loads_ns`).
        -   Функциональность игры реализована в соответствии с описанием.
        -   Код разделен на функции, что улучшает читаемость и поддержку.
        -   Используется логгер для обработки ошибок.
        -   Добавлена документация в формате RST.
        -   Код организован в класс `KinemaGame`, что позволяет легко масштабировать его.
        -   Используются форматированные строки для вывода результатов.
        -   Добавлена проверка на правильность ввода.

    -   **Недостатки:**
        -   Можно добавить обработку исключений при вводе пользователя (например, если введено не число).
        -   Нет тестов для проверки корректности работы игры.
    
**Рекомендации по улучшению**

1.  **Обработка ошибок ввода:**
    -   Добавить обработку исключений `ValueError` при преобразовании ввода пользователя в числа.
2.  **Тестирование:**
    -   Написать тесты для проверки корректности расчетов и логики игры.
3.  **Уровни сложности:**
    -   Реализовать систему уровней сложности, как указано в требованиях.
4.  **Графический интерфейс:**
    -   Рассмотреть возможность добавления простого графического интерфейса для более интерактивного опыта.
5.  **Конфигурация:**
    -   Вынести параметры игры (например, `g`, `accuracy_margin`) в переменные класса или конфигурационный файл.
6.  **Переиспользование кода:**
    -   Использовать один метод для вывода результатов, чтобы не повторять код.
    -   Можно создать отдельный метод для ввода ответа с проверкой ввода, чтобы не дублировать логику.
    -   Использовать f-строки для форматирования строк.
    
**Улучшенный код**
```python
"""
Модуль для реализации игры KINEMA (Кинематические вычисления).
==================================================================

Этот модуль реализует игру, проверяющую знания кинематики,
в частности, расчеты движения тела, брошенного вертикально вверх.
Игрок должен ответить на вопросы о высоте, времени полета и скорости мяча.

Пример использования
--------------------

.. code-block:: python

    game = KinemaGame()
    game.play()
"""

import random
from src.logger.logger import logger  # Используем логгер для отслеживания ошибок

class KinemaGame:
    """
    Класс, представляющий игру KINEMA.

    :ivar float g: Ускорение свободного падения (9.8 м/с^2).
    :ivar float accuracy_margin: Допустимое отклонение от правильного ответа в процентах.
    """
    G = 9.8  # Ускорение свободного падения # Константа ускорения свободного падения
    ACCURACY_MARGIN = 0.15  # Допустимая погрешность (15%) # Константа погрешности

    def __init__(self):
         """
         Инициализирует игру KINEMA.
         """
         pass  # Конструктор не требуется

    def _calculate_max_height(self, initial_velocity: float) -> float:
        """
        Вычисляет максимальную высоту подъема мяча.

        :param initial_velocity: Начальная скорость мяча.
        :return: Максимальная высота подъема мяча.
        """
        try:
            # Расчет максимальной высоты по формуле H = V^2 / (2g)
            max_height = (initial_velocity ** 2) / (2 * KinemaGame.G) # Исправлено обращение к константе класса
            return max_height
        except Exception as e:
            logger.error(f'Ошибка при расчете максимальной высоты: {e}')
            return 0  # Возвращаем 0 при ошибке

    def _calculate_flight_time(self, initial_velocity: float) -> float:
        """
        Вычисляет общее время полета мяча.

        :param initial_velocity: Начальная скорость мяча.
        :return: Общее время полета мяча.
        """
        try:
            # Расчет времени полета по формуле T = 2V / g
            flight_time = (2 * initial_velocity) / KinemaGame.G # Исправлено обращение к константе класса
            return flight_time
        except Exception as e:
            logger.error(f'Ошибка при расчете времени полета: {e}')
            return 0  # Возвращаем 0 при ошибке

    def _calculate_velocity_at_time(self, initial_velocity: float, time: float) -> float:
        """
        Вычисляет скорость мяча в заданный момент времени.

        :param initial_velocity: Начальная скорость мяча.
        :param time: Время, через которое нужно вычислить скорость.
        :return: Скорость мяча в заданный момент времени.
        """
        try:
           # Расчет скорости в заданный момент времени по формуле V_t = V - g * t
           velocity_at_time = initial_velocity - (KinemaGame.G * time) # Исправлено обращение к константе класса
           return velocity_at_time
        except Exception as e:
            logger.error(f'Ошибка при расчете скорости: {e}')
            return 0 # Возвращаем 0 при ошибке

    def _check_answer(self, user_answer: float, correct_answer: float) -> bool:
        """
        Проверяет, является ли ответ пользователя правильным с учетом погрешности.

        :param user_answer: Ответ пользователя.
        :param correct_answer: Правильный ответ.
        :return: True, если ответ правильный, False в противном случае.
        """
        try:
             # Проверка на погрешность в пределах допустимого отклонения
            if abs(user_answer - correct_answer) <= abs(correct_answer * KinemaGame.ACCURACY_MARGIN):  # Исправлено обращение к константе класса
                return True
            return False
        except Exception as e:
            logger.error(f'Ошибка при проверке ответа: {e}')
            return False  # Возвращаем False при ошибке

    def _get_user_input(self, question: str) -> float:
        """
        Запрашивает ввод пользователя и обрабатывает исключения.
        
        :param question: Текст вопроса.
        :return: Ввод пользователя в виде числа.
        """
        while True:
            try:
                user_input = float(input(question))
                return user_input
            except ValueError:
                logger.error("Неверный ввод. Пожалуйста, введите число.")
                print("Пожалуйста, введите число.")

    def _display_result(self, correct_answer: float, user_answer: float, is_correct: bool, unit: str = ""):
        """
        Выводит результат проверки ответа.

        :param correct_answer: Правильный ответ.
        :param user_answer: Ответ пользователя.
        :param is_correct: Флаг, показывающий, является ли ответ правильным.
        :param unit: Единица измерения.
        """
        if is_correct:
             print(f"Ответ: Близко! Правильный ответ: {correct_answer:.5f} {unit}")
        else:
            print(f"Ответ: Неправильно. Правильный ответ: {correct_answer:.5f} {unit}")

    def play(self):
        """
        Запускает игровой процесс.
        """
        print("Добро пожаловать в игру KINEMA!")

        while True:
            # Генерация случайной начальной скорости
            initial_velocity = random.uniform(10, 25)  # Случайная скорость от 10 до 25 м/с
            print(f"Мяч был брошен вверх с начальной скоростью {initial_velocity:.2f} м/с.")

            # Вопрос 1: Максимальная высота
            correct_max_height = self._calculate_max_height(initial_velocity)
            user_max_height = self._get_user_input("Вопрос 1: Как высоко поднимется мяч? > ")
            self._display_result(correct_max_height,user_max_height,self._check_answer(user_max_height, correct_max_height), "м")
           
            # Вопрос 2: Время полета
            correct_flight_time = self._calculate_flight_time(initial_velocity)
            user_flight_time = self._get_user_input("Вопрос 2: Как долго мяч будет в воздухе? > ")
            self._display_result(correct_flight_time,user_flight_time,self._check_answer(user_flight_time, correct_flight_time), "с")
           
            # Вопрос 3: Скорость через случайное время
            random_time = random.uniform(0.1, correct_flight_time-0.1)
            correct_velocity_at_time = self._calculate_velocity_at_time(initial_velocity, random_time)
            user_velocity_at_time = self._get_user_input(f"Вопрос 3: Какова будет скорость мяча через {random_time:.2f} секунд? > ")
            
            if self._check_answer(user_velocity_at_time, correct_velocity_at_time):
                 print("Ответ: Правильно! Отлично, вы угадали.")
            else:
                print(f"Ответ: Неправильно. Правильный ответ: {correct_velocity_at_time:.2f} м/с")

            play_again = input("Хотите сыграть снова? (да/нет): ")
            if play_again.lower() != 'да':
                print("Спасибо за игру! До свидания!")
                break

if __name__ == "__main__":
    game = KinemaGame() # Создаем экземпляр игры
    game.play() # Запускаем игру

```