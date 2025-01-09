# Анализ кода модуля `input_output.md`

**Качество кода**

- **Соответствие требованиям к формату кода (1-10):**
    - **Преимущества:**
        - Описание игры представлено в виде markdown-текста, что облегчает его чтение.
        - Приведены конкретные правила и формат ввода/вывода для игры.
        - Есть примеры использования для лучшего понимания.
    - **Недостатки:**
        - Код не представлен в виде исполняемого скрипта Python, а скорее как описание правил игры.
        - Отсутствует обработка ошибок и логирование.
        - Нет четкой структуры для представления математических операций.
        - Не реализован алгоритм переключения между сложностью операций.

**Рекомендации по улучшению**

1.  **Преобразование в исполняемый код:**  Необходимо преобразовать markdown-описание в исполняемый код Python.
2.  **Реализация логики игры:** Необходимо реализовать логику, которая будет обрабатывать ввод пользователя и генерировать вывод в соответствии с правилами.
3.  **Хранение правил:** Нужно использовать переменные для хранения текущего правила игры, чтобы можно было его менять по запросу пользователя или по мере прогресса игры.
4.  **Функции для операций:** Реализовать математические операции как отдельные функции, которые можно легко вызывать.
5.  **Обработка пользовательского ввода:** Обеспечить корректную обработку пользовательского ввода, включая проверку на корректность числового ввода и команды.
6.  **Реализация логирования:** Добавить логирование для отслеживания ошибок и хода игры.
7.  **Добавление документации:** Добавить reStructuredText (RST) docstring для функций, классов и модулей.

**Улучшенный код**
```python
"""
Модуль для реализации математической игры "Ввод-Вывод".
=========================================================================================

Модуль содержит функции для обработки ввода пользователя, выполнения математических
операций и вывода результатов.

Пример использования
--------------------

.. code-block:: python

    game = InputOutputGame()
    game.start_game()

"""
import re # Импорт модуля re для обработки пользовательского ввода #
from src.logger.logger import logger # Импорт logger для записи ошибок и отладки #
from typing import Callable, Any # Импорт Callable и Any для аннотации типов #
from src.utils.jjson import j_loads_ns # Импорт j_loads_ns для чтения json файлов #

class InputOutputGame:
    """
    Класс для управления игрой "Ввод-Вывод".

    :ivar current_machine: Текущее правило, по которому выполняется преобразование числа.
    :vartype current_machine: Callable[[float], float]
    :ivar current_machine_description: Описание текущего правила.
    :vartype current_machine_description: str
    """
    def __init__(self):
        """
        Инициализация игры со стартовым правилом.
        """
        self.current_machine: Callable[[float], float] = self._add_three # Начальное правило - прибавить 3
        self.current_machine_description: str = "+3" # Описание начального правила

    def _add_three(self, number: float) -> float:
        """
        Выполняет операцию сложения с числом 3.

        :param number: Число для обработки.
        :type number: float
        :return: Результат сложения.
        :rtype: float
        """
        return number + 3

    def _multiply_by_two(self, number: float) -> float:
        """
        Выполняет операцию умножения на 2.

        :param number: Число для обработки.
        :type number: float
        :return: Результат умножения.
        :rtype: float
        """
        return number * 2

    def _multiply_by_two_add_one(self, number: float) -> float:
        """
        Выполняет операцию умножения на 2 и прибавления 1.

        :param number: Число для обработки.
        :type number: float
        :return: Результат операции.
        :rtype: float
        """
        return number * 2 + 1

    def _square_root(self, number: float) -> float:
        """
        Выполняет операцию квадратного корня.

        :param number: Число для обработки.
        :type number: float
        :return: Результат операции или None, если число отрицательное.
        :rtype: float
        """
        if number < 0:
            logger.error(f'Нельзя извлечь квадратный корень из отрицательного числа {number=}') # Логирование ошибки #
            return None
        return number ** 0.5

    def _set_machine(self, machine_str: str) -> str:
        """
        Устанавливает новое правило игры на основе строки.

        :param machine_str: Строка с описанием правила.
        :type machine_str: str
        :return: Сообщение об установленном правиле.
        :rtype: str
        """
        try: # Используем try-except блок для обработки возможных ошибок #
            if "x*2" in machine_str:
                self.current_machine = self._multiply_by_two
                self.current_machine_description = "x*2"
            elif "2x+1" in machine_str:
                self.current_machine = self._multiply_by_two_add_one
                self.current_machine_description = "2x+1"
            elif "квадратный корень" in machine_str:
                self.current_machine = self._square_root
                self.current_machine_description = "квадратный корень"
            else:
                logger.error(f"Неизвестное правило машины {machine_str=}") # Логирование ошибки #
                return f"Неизвестное правило машины {machine_str}." # Возвращаем сообщение об ошибке #
            return f"Окей, машина: {self.current_machine_description}" # Возвращаем сообщение об успешной установке правила #
        except Exception as ex:
            logger.error(f'Ошибка при установке машины {machine_str=}', ex) # Логирование ошибки #
            return f"Ошибка при установке машины {machine_str}." # Возвращаем сообщение об ошибке #

    def _process_input(self, user_input: str) -> str:
        """
        Обрабатывает ввод пользователя и выдает результат в соответствии с правилом.

        :param user_input: Строка ввода пользователя.
        :type user_input: str
        :return: Строка вывода с результатом.
        :rtype: str
        """
        try: # Используем try-except блок для обработки возможных ошибок #
            if "Задайте машину" in user_input:
               # Код вызывает _set_machine если в user_input есть "Задайте машину" #
                machine_str = user_input.replace("Задайте машину ", "").strip()
                return self._set_machine(machine_str)
            elif "Ввод:" in user_input:
               # Код извлекает число из user_input если есть "Ввод:" #
                number_str = user_input.replace("Ввод:", "").strip()
                number = float(number_str)
                result = self.current_machine(number)
                if result is not None: # Проверка на None, если квадратный корень от отрицательного числа #
                   # Код выводит результат если результат не None #
                    return f"Вывод: {result}, машина: {self.current_machine_description}"
                else:
                   # Код выводит сообщение об ошибке если результат None #
                    return "Ошибка: Невозможно выполнить операцию с введенным числом."
            else:
                logger.error(f"Некорректный ввод {user_input=}") # Логирование ошибки #
                return "Некорректный ввод." # Возвращаем сообщение об ошибке #

        except ValueError as ve:
            logger.error(f"Некорректный формат числа {user_input=}", ve) # Логирование ошибки ValueError #
            return "Ошибка: Некорректный формат числа." # Возвращаем сообщение об ошибке #
        except Exception as ex:
            logger.error(f"Непредвиденная ошибка {user_input=}", ex) # Логирование общей ошибки #
            return "Произошла непредвиденная ошибка." # Возвращаем сообщение об ошибке #

    def start_game(self) -> None:
        """
        Запускает игровой цикл.
        """
        print("Игра 'Ввод-Вывод' началась. Введите 'Ввод: <число>' или 'Задайте машину <правило>'")
        while True:
            user_input = input("Введите команду: ")
            output = self._process_input(user_input) # Вызов функции _process_input #
            print(output)


if __name__ == "__main__": # Код выполняется только при запуске файла напрямую #
    game = InputOutputGame()
    game.start_game()

```