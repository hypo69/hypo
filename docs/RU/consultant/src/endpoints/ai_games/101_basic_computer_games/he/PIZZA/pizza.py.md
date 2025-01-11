# Анализ кода модуля `pizza.py`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и логически понятен.
    - Присутствуют необходимые проверки входных данных.
    - Используется `try-except` для обработки ошибок ввода.
    - Есть понятные комментарии на иврите, объясняющие логику кода.
    - Код соответствует требованиям задания.
-  Минусы
    - Отсутствует reStructuredText документация.
    - Не используются логирование ошибок.
    - Желательно переписать на английском
    - Есть избыточное использование `try-except`.

**Рекомендации по улучшению**

1.  **Документация**:
    - Добавить reStructuredText (RST) документацию для модуля и функции.
2.  **Логирование**:
    - Использовать `from src.logger.logger import logger` для логирования ошибок вместо `print`.
    - Убрать избыточное использование `try-except`, заменив на логирование.
3.  **Комментарии**:
    - Переписать комментарии на английский язык.
    - Переписать комментарии в формате reStructuredText (RST).
4.  **Именование**:
    - Переименовать переменные на английский язык.
5.  **Улучшение читаемости**:
    - Разделить код на более мелкие, логически понятные блоки.
6. **Стандартизация**:
    - Перевести текст, выводимый в консоль, на английский язык.

**Оптимизированный код**
```python
"""
Module for calculating the number of pizzas needed based on the number of people and pizza size.
================================================================================================

This module provides a function to calculate the recommended number of pizzas to order based
on the number of people and the chosen pizza size (small, medium, or large).

Example Usage
-------------

To use this module, simply call the ``calculate_pizza_amount`` function.

.. code-block:: python

    calculate_pizza_amount()
"""
from src.logger.logger import logger

def calculate_pizza_amount():
    """
    Calculates and prints the recommended number of pizzas to order based on user input.

    This function prompts the user to enter the number of people and the desired pizza size,
    then calculates and prints the recommended number of pizzas to order.

    :raises ValueError: If the user enters invalid input for the number of people.
    """
    # Prompt the user to enter the number of people
    try:
        num_people = int(input("Enter the number of people: "))
        # Check if the number of people is positive
        if num_people <= 0:
            logger.error("The number of people must be positive.")
            return
    except ValueError as ex:
        # Log error if the input is not a valid integer
        logger.error("Invalid input. Please enter a whole number.", exc_info=ex)
        return

    # Prompt the user to enter the pizza size (S, M, L)
    pizza_size = input("Enter the pizza size (S, M, L): ").upper()

    # Check the pizza size and calculate the number of pizzas
    if pizza_size == "S":
        # Small pizza: 1 pizza for every 3 people (rounded up)
        num_pizzas = (num_people + 2) // 3
        print(f"Recommended to order {num_pizzas} small pizzas.")
    elif pizza_size == "M":
        # Medium pizza: 1 pizza for every 2 people (rounded up)
        num_pizzas = (num_people + 1) // 2
        print(f"Recommended to order {num_pizzas} medium pizzas.")
    elif pizza_size == "L":
        # Large pizza: 1 pizza per person
        num_pizzas = num_people
        print(f"Recommended to order {num_pizzas} large pizzas.")
    else:
        logger.error("Invalid pizza size. Please enter S, M, or L.")


# Run the game if the script is executed
if __name__ == "__main__":
    calculate_pizza_amount()
```