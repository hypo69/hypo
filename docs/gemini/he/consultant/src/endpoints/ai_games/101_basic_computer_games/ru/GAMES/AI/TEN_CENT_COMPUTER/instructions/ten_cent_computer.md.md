# Анализ кода модуля `ten_cent_computer.md`

**Качество кода**
  -  Соответствие требованиям к формату кода (1-10):
    -   **Преимущества:**
        - Документ представляет собой инструкцию для симулятора "10-центового компьютера", предназначенного для обучения двоичной системе счисления.
        - Четко описаны правила работы симулятора, форматы ввода/вывода, и приведены примеры.
        - Содержит понятные инструкции для пользователя.
        - Ориентирован на целевую аудиторию (дети) с простым и понятным языком.
    -  **Недостатки:**
        - Документ не является кодом Python, а представляет собой текстовое описание правил и примеров.
        - Отсутствует формат reStructuredText (RST) и docstrings, как требуется в инструкции.
        - Нет необходимости в использовании `j_loads` или `j_loads_ns`, так как это не Python-файл.
        - Невозможно добавить импорты или использовать логгер, так как это не исполняемый код.

**Рекомендации по улучшению**

1. **Перевести в исполняемый код:** Необходимо реализовать данный симулятор на Python, следуя приведенным правилам и форматам ввода/вывода.
2. **Документировать код:** Добавить docstring в формате RST для всех функций, классов и методов.
3. **Использовать логгер:** Использовать `from src.logger.logger import logger` для обработки ошибок.
4. **Обработка ошибок:** Добавить обработку исключений с использованием `logger.error`.
5. **Форматирование:** Привести код в соответствие PEP8, включая корректное именование переменных и функций.
6. **Добавить примеры:** Включить примеры использования функций и методов в docstring.
7. **Реализация логики:** Разработать логику преобразования десятичных чисел в двоичные и наоборот.
8. **Интерактивность:** Реализовать взаимодействие с пользователем через ввод и вывод.

**Улучшенный код**
```python
"""
Модуль для симулятора "10-центового компьютера"
=========================================================================================

Этот модуль реализует симулятор, который обучает детей двоичной системе счисления,
представляя числа в двоичной форме с помощью 4 "лампочек".

Примеры использования
--------------------

.. code-block:: python

    simulator = TenCentComputerSimulator()
    simulator.run()
"""

from src.logger.logger import logger  # Импортируем логгер
from typing import Any, List # Импортируем типы для аннотаций

class TenCentComputerSimulator:
    """
    Класс для симулятора "10-центового компьютера".

    Этот класс позволяет конвертировать десятичные числа в двоичные и наоборот,
    используя представление с 4 "лампочками".
    """

    def __init__(self) -> None:
        """
        Инициализирует симулятор.
        """
        self.lamp_values = [1, 2, 4, 8] # Значения лампочек

    def decimal_to_binary(self, decimal: int) -> str:
        """
        Конвертирует десятичное число в двоичное представление с 4 "лампочками".

        :param decimal: Десятичное число для конвертации.
        :return: Строка с двоичным представлением (например, '0101').
        """
        if not isinstance(decimal, int):
             logger.error(f"Некорректный тип данных: {type(decimal)}. Ожидается int.")  # Используем logger.error для обработки ошибок
             return '0000'
        
        if decimal < 0 or decimal > 15:
            logger.error(f"Число {decimal} вне допустимого диапазона [0-15]") # Используем logger.error для обработки ошибок
            return '0000'

        binary_representation = ""
        for value in reversed(self.lamp_values):
            if decimal >= value:
                binary_representation += "1"
                decimal -= value
            else:
                binary_representation += "0"
        return binary_representation[::-1] # Переворачиваем строку

    def binary_to_decimal(self, binary: str) -> int:
        """
        Конвертирует двоичное представление с 4 "лампочками" в десятичное число.

        :param binary: Строка с двоичным представлением (например, '0101').
        :return: Десятичное число.
        """
        if not isinstance(binary, str):
            logger.error(f"Некорректный тип данных: {type(binary)}. Ожидается str.") # Используем logger.error для обработки ошибок
            return 0
        if len(binary) != 4 or not all(bit in '01' for bit in binary):
            logger.error(f"Некорректный формат двоичного числа: {binary}. Ожидается строка из 4 символов 0 или 1.")# Используем logger.error для обработки ошибок
            return 0

        decimal_value = 0
        for i, bit in enumerate(reversed(binary)):
            if bit == '1':
                decimal_value += self.lamp_values[i]
        return decimal_value

    def explain_binary(self, binary: str) -> str:
        """
        Объясняет, какие "лампочки" включены в двоичном представлении.

        :param binary: Строка с двоичным представлением (например, '0101').
        :return: Строка с объяснением включенных лампочек.
        """
        explanation = "Включены лампочки "
        included_lamps = []
        for i, bit in enumerate(reversed(binary)):
            if bit == '1':
                included_lamps.append(str(self.lamp_values[i]))
        
        if not included_lamps:
            return "Нет включенных лампочек."

        explanation += ", ".join(included_lamps)
        explanation += f". {'+'.join(included_lamps)}={self.binary_to_decimal(binary)}"

        return explanation

    def explain_decimal(self, decimal: int) -> str:
        """
        Объясняет, какие "лампочки" нужно включить для представления десятичного числа.

        :param decimal: Десятичное число.
        :return: Строка с объяснением, какие лампочки включены.
        """
        binary = self.decimal_to_binary(decimal)
        explanation = self.explain_binary(binary)
        return explanation

    def process_input(self, input_str: str) -> str:
        """
        Обрабатывает ввод пользователя и возвращает результат.

        :param input_str: Строка ввода от пользователя.
        :return: Строка с результатом работы симулятора.
        """
        try:
            if input_str.startswith("Десятичное:"):
                decimal_str = input_str.split(": ")[1]
                decimal = int(decimal_str)
                binary = self.decimal_to_binary(decimal)
                explanation = self.explain_decimal(decimal)
                return f"Двоичное: {binary}, объяснение: {explanation}"
            elif input_str.startswith("Лампочки:"):
                binary = input_str.split(": ")[1]
                decimal = self.binary_to_decimal(binary)
                explanation = self.explain_binary(binary)
                return f"Десятичное: {decimal}, объяснение: {explanation}"
            elif input_str.startswith("Объясните как "):
                decimal_str = input_str.split("Объясните как ")[1]
                decimal = int(decimal_str)
                binary = self.decimal_to_binary(decimal)
                explanation = self.explain_decimal(decimal)
                return f"Двоичное: {binary}, объяснение: {explanation}"
            else:
                return "Некорректный формат ввода."
        except Exception as ex:
            logger.error(f"Ошибка при обработке ввода: {input_str}", ex)
            return "Ошибка при обработке ввода. Проверьте формат ввода."
    
    def run(self):
        """
        Запускает симулятор в интерактивном режиме.
        """
        print("Симулятор 10-центового компьютера запущен.")
        while True:
            user_input = input("Введите команду (или 'exit' для выхода): ")
            if user_input.lower() == 'exit':
                print("Симулятор завершен.")
                break
            response = self.process_input(user_input)
            print(response)

if __name__ == "__main__":
    simulator = TenCentComputerSimulator() # Создаем экземпляр класса
    simulator.run() # Запускаем симулятор
```
```python
# """
# Модуль для симулятора "10-центового компьютера" #  
# ========================================================================================= # 
# 
# Этот модуль реализует симулятор, который обучает детей двоичной системе счисления, #
# представляя числа в двоичной форме с помощью 4 "лампочек". #
# 
# Примеры использования #
# -------------------- #
# 
# .. code-block:: python #
# 
#     simulator = TenCentComputerSimulator() #
#     simulator.run() #
# """
# 
# from src.logger.logger import logger  # Импортируем логгер #
# from typing import Any, List # Импортируем типы для аннотаций #
# 
# class TenCentComputerSimulator:
#     """
#     Класс для симулятора "10-центового компьютера". #
# 
#     Этот класс позволяет конвертировать десятичные числа в двоичные и наоборот, #
#     используя представление с 4 "лампочками". #
#     """
# 
#     def __init__(self) -> None:
#         """
#         Инициализирует симулятор. #
#         """
#         self.lamp_values = [1, 2, 4, 8] # Значения лампочек #
# 
#     def decimal_to_binary(self, decimal: int) -> str:
#         """
#         Конвертирует десятичное число в двоичное представление с 4 "лампочками". #
# 
#         :param decimal: Десятичное число для конвертации. #
#         :return: Строка с двоичным представлением (например, '0101'). #
#         """
#         if not isinstance(decimal, int):
#              logger.error(f"Некорректный тип данных: {type(decimal)}. Ожидается int.")  # Используем logger.error для обработки ошибок #
#              return '0000' #
#         
#         if decimal < 0 or decimal > 15:
#             logger.error(f"Число {decimal} вне допустимого диапазона [0-15]") # Используем logger.error для обработки ошибок #
#             return '0000' #
# 
#         binary_representation = ""
#         for value in reversed(self.lamp_values):
#             if decimal >= value:
#                 binary_representation += "1"
#                 decimal -= value
#             else:
#                 binary_representation += "0"
#         return binary_representation[::-1] # Переворачиваем строку #
# 
#     def binary_to_decimal(self, binary: str) -> int:
#         """
#         Конвертирует двоичное представление с 4 "лампочками" в десятичное число. #
# 
#         :param binary: Строка с двоичным представлением (например, '0101'). #
#         :return: Десятичное число. #
#         """
#         if not isinstance(binary, str):
#             logger.error(f"Некорректный тип данных: {type(binary)}. Ожидается str.") # Используем logger.error для обработки ошибок #
#             return 0 #
#         if len(binary) != 4 or not all(bit in '01' for bit in binary):
#             logger.error(f"Некорректный формат двоичного числа: {binary}. Ожидается строка из 4 символов 0 или 1.")# Используем logger.error для обработки ошибок #
#             return 0 #
# 
#         decimal_value = 0
#         for i, bit in enumerate(reversed(binary)):
#             if bit == '1':
#                 decimal_value += self.lamp_values[i]
#         return decimal_value
# 
#     def explain_binary(self, binary: str) -> str:
#         """
#         Объясняет, какие "лампочки" включены в двоичном представлении. #
# 
#         :param binary: Строка с двоичным представлением (например, '0101'). #
#         :return: Строка с объяснением включенных лампочек. #
#         """
#         explanation = "Включены лампочки "
#         included_lamps = []
#         for i, bit in enumerate(reversed(binary)):
#             if bit == '1':
#                 included_lamps.append(str(self.lamp_values[i]))
#         
#         if not included_lamps:
#             return "Нет включенных лампочек."
# 
#         explanation += ", ".join(included_lamps)
#         explanation += f". {'+'.join(included_lamps)}={self.binary_to_decimal(binary)}"
# 
#         return explanation
# 
#     def explain_decimal(self, decimal: int) -> str:
#         """
#         Объясняет, какие "лампочки" нужно включить для представления десятичного числа. #
# 
#         :param decimal: Десятичное число. #
#         :return: Строка с объяснением, какие лампочки включены. #
#         """
#         binary = self.decimal_to_binary(decimal)
#         explanation = self.explain_binary(binary)
#         return explanation
# 
#     def process_input(self, input_str: str) -> str:
#         """
#         Обрабатывает ввод пользователя и возвращает результат. #
# 
#         :param input_str: Строка ввода от пользователя. #
#         :return: Строка с результатом работы симулятора. #
#         """
#         try:
#             if input_str.startswith("Десятичное:"):
#                 decimal_str = input_str.split(": ")[1]
#                 decimal = int(decimal_str)
#                 binary = self.decimal_to_binary(decimal)
#                 explanation = self.explain_decimal(decimal)
#                 return f"Двоичное: {binary}, объяснение: {explanation}"
#             elif input_str.startswith("Лампочки:"):
#                 binary = input_str.split(": ")[1]
#                 decimal = self.binary_to_decimal(binary)
#                 explanation = self.explain_binary(binary)
#                 return f"Десятичное: {decimal}, объяснение: {explanation}"
#             elif input_str.startswith("Объясните как "):
#                 decimal_str = input_str.split("Объясните как ")[1]
#                 decimal = int(decimal_str)
#                 binary = self.decimal_to_binary(decimal)
#                 explanation = self.explain_decimal(decimal)
#                 return f"Двоичное: {binary}, объяснение: {explanation}"
#             else:
#                 return "Некорректный формат ввода."
#         except Exception as ex:
#             logger.error(f"Ошибка при обработке ввода: {input_str}", ex) #
#             return "Ошибка при обработке ввода. Проверьте формат ввода." #
#     
#     def run(self):
#         """
#         Запускает симулятор в интерактивном режиме. #
#         """
#         print("Симулятор 10-центового компьютера запущен.")
#         while True:
#             user_input = input("Введите команду (или 'exit' для выхода): ")
#             if user_input.lower() == 'exit':
#                 print("Симулятор завершен.")
#                 break
#             response = self.process_input(user_input)
#             print(response)
# 
# if __name__ == "__main__":
#     simulator = TenCentComputerSimulator() # Создаем экземпляр класса #
#     simulator.run() # Запускаем симулятор #
```