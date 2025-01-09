# Анализ кода модуля `pizza.py`

**Качество кода**
-   **Соответствие требованиям к формату кода (1-10):** 
    -   Требования 1 (формат документации RST) не соблюдены.
    -   Требование 2 (сохранение комментариев) соблюдено.
    -   Требование 3 (использование `j_loads` или `j_loads_ns`) не применимо в данном коде.
    -   Требование 4 (анализ структуры, импорты) соблюдено.
    -   Требование 5 (документация RST, логирование ошибок) частично соблюдено.
    -   Требование 6 (избегание `try-except`) не везде соблюдено.
    -   Требование 7 (вывод полного кода) соблюдено.
    -   Требование 8 (примеры документации) не соблюдено.
    -   Требование 9 (RST для всех элементов) не соблюдено.
-   **Преимущества:**
    -   Код читаемый и понятный.
    -   Логика программы соответствует описанию.
    -   Есть обработка некорректного ввода пользователя.
-   **Недостатки:**
    -   Отсутствует документация в формате reStructuredText (RST).
    -   Используются избыточные блоки `try-except`, что делает код более громоздким.
    -   Нет логирования ошибок.
    -   Комментарии не соответствуют стандарту RST.

**Рекомендации по улучшению**
1.  **Документирование**: Переписать все комментарии и docstring в формате RST. Добавить подробное описание модуля, функций и переменных.
2.  **Логирование**: Использовать `from src.logger.logger import logger` для логирования ошибок вместо блоков `try-except`.
3.  **Обработка ошибок**: Упростить обработку ошибок, заменив `try-except` на `logger.error` для регистрации исключений.
4.  **Улучшить читаемость**: Разбить код на более мелкие функции.
5.  **Форматирование**: Привести код к единому стилю.

**Улучшенный код**
```python
"""
Модуль для моделирования процесса заказа и доставки пиццы.
=========================================================================================

Модуль позволяет пользователю ввести количество пицц, их стоимость и процент чаевых.
После чего программа вычисляет общую стоимость заказа, включая налог и чаевые.

Пример использования
--------------------

Пример запуска программы:

.. code-block:: python

    python pizza.py

"""
from src.logger.logger import logger # импортируем logger для логирования ошибок

def get_positive_int_input(prompt: str) -> int:
    """
    Запрашивает у пользователя целое положительное число.

    :param prompt: Сообщение для пользователя.
    :return: Целое положительное число.
    :raises ValueError: Если введено некорректное значение.
    """
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Пожалуйста, введите положительное число.")
        except ValueError:
            print("Пожалуйста, введите целое число.")
            logger.error('Введено некорректное значение, ожидается целое число') # логирование ошибки

def get_positive_float_input(prompt: str) -> float:
    """
    Запрашивает у пользователя положительное число с плавающей точкой.

    :param prompt: Сообщение для пользователя.
    :return: Положительное число с плавающей точкой.
    :raises ValueError: Если введено некорректное значение.
    """
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Пожалуйста, введите положительную стоимость.")
        except ValueError:
            print("Пожалуйста, введите числовое значение.")
            logger.error('Введено некорректное значение, ожидается число с плавающей точкой') # логирование ошибки

def get_tip_percentage() -> float:
    """
    Запрашивает у пользователя процент чаевых.

    :return: Процент чаевых от 0 до 100.
    :raises ValueError: Если введено некорректное значение.
    """
    while True:
        try:
            tip_percent = float(input("Какой процент чаевых вы хотите оставить? "))
            if 0 <= tip_percent <= 100:
                return tip_percent
            else:
                print("Пожалуйста, введите процент от 0 до 100.")
        except ValueError:
            print("Пожалуйста, введите числовое значение.")
            logger.error('Введено некорректное значение, ожидается число с плавающей точкой') # логирование ошибки

def calculate_total_cost(quantity: int) -> float:
    """
    Вычисляет общую стоимость пицц.

    :param quantity: Количество пицц.
    :return: Общая стоимость пицц.
    """
    total_cost = 0
    for i in range(quantity):
       pizza_cost = get_positive_float_input(f"Введите стоимость пиццы {i + 1}: ") # получаем стоимость пиццы
       total_cost += pizza_cost # добавляем к общей стоимости
    return total_cost

def calculate_tax(total_cost: float) -> float:
    """
    Вычисляет налог (5% от общей стоимости).

    :param total_cost: Общая стоимость пицц.
    :return: Сумма налога.
    """
    tax = total_cost * 0.05 # рассчитываем налог
    return tax

def calculate_tip_amount(total_cost: float, tip_percent: float) -> float:
    """
    Вычисляет сумму чаевых.

    :param total_cost: Общая стоимость пицц.
    :param tip_percent: Процент чаевых.
    :return: Сумма чаевых.
    """
    tip_amount = total_cost * tip_percent / 100 # вычисляем чаевые
    return tip_amount

def calculate_grand_total(total_cost: float, tax: float, tip_amount: float) -> float:
    """
    Вычисляет полную стоимость заказа.

    :param total_cost: Общая стоимость пицц.
    :param tax: Сумма налога.
    :param tip_amount: Сумма чаевых.
    :return: Полная стоимость заказа.
    """
    grand_total = total_cost + tax + tip_amount # вычисляем общую стоимость
    return grand_total

def print_order_summary(total_cost: float, tax: float, tip_amount: float, grand_total: float):
    """
    Выводит сводку по заказу.

    :param total_cost: Общая стоимость пицц.
    :param tax: Сумма налога.
    :param tip_amount: Сумма чаевых.
    :param grand_total: Полная стоимость заказа.
    """
    print(f"Общая стоимость пицц: {total_cost:.2f}")
    print(f"Налог: {tax:.2f}")
    print(f"Чаевые: {tip_amount:.2f}")
    print(f"Полная стоимость заказа: {grand_total:.2f}")

# Запрашиваем у пользователя количество пицц
quantity = get_positive_int_input("Сколько пицц вы хотите заказать? ") # получаем количество пицц

# Вычисляем общую стоимость пицц
total_cost = calculate_total_cost(quantity) # вычисляем общую стоимость

# Запрашиваем процент чаевых
tip_percent = get_tip_percentage() # получаем процент чаевых

# Вычисляем налог
tax = calculate_tax(total_cost) # вычисляем налог

# Вычисляем сумму чаевых
tip_amount = calculate_tip_amount(total_cost, tip_percent) # вычисляем сумму чаевых

# Вычисляем полную стоимость заказа
grand_total = calculate_grand_total(total_cost, tax, tip_amount) # вычисляем полную стоимость

# Выводим результаты
print_order_summary(total_cost, tax, tip_amount, grand_total) # выводим результаты

```