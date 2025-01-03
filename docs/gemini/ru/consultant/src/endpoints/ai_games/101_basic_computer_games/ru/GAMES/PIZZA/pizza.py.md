# Анализ кода модуля pizza.py

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и логически понятен.
    - Присутствуют подробные комментарии, описывающие каждый шаг программы.
    - Используются циклы `while` и `for` для обработки ввода пользователя и вычисления стоимости.
    - Присутствует обработка исключений для ввода некорректных данных.
    - Форматированный вывод результатов.
- Минусы
    - Отсутствует reStructuredText (RST) для документирования кода.
    - Не используется `j_loads` или `j_loads_ns` для чтения данных из файлов (в данном случае это не требуется, но согласно инструкции, стоит помнить об этом).
    - Нет логирования ошибок с использованием `src.logger.logger`.
    -  Не стандартизированы имена переменных (например, `totalCost`, `pizzaCost`, `tipAmount` - есть разночтения в стиле, лучше использовать snake_case).

**Рекомендации по улучшению**

1.  **Документация**:
    - Переписать все комментарии в формате reStructuredText (RST).
    - Добавить docstring для модуля с описанием его назначения, параметров и возвращаемых значений.
2.  **Логирование**:
    - Добавить логирование ошибок с использованием `from src.logger.logger import logger`.
    - Заменить `print` на `logger.error` при обработке исключений.
3.  **Именование**:
    - Привести имена переменных к единому стилю snake_case (`total_cost`, `pizza_cost`, `tip_amount`).
4.  **Обработка ввода**:
    - Улучшить обработку ввода, вынеся логику проверки в отдельную функцию.
5.  **Форматирование**:
    - Привести форматирование вывода к единому стилю.
6. **Избегать дублирования**:
    -  Функционал валидации ввода можно вынести в отдельную функцию для переиспользования.

**Оптимизированный код**

```python
"""
Модуль для расчета стоимости заказа пиццы.
=========================================================================================

Этот модуль моделирует процесс заказа и доставки пиццы. Игрок отвечает на вопросы о количестве пицц, их стоимости, размере чаевых и т.д.
В конце программа выводит полную стоимость заказа, включая налог и чаевые.

Пример использования
--------------------

Пример запуска игры "Пицца":

.. code-block:: python

    python pizza.py
"""
__author__ = 'hypo69 (hypo69@davidka.net)'

from src.logger.logger import logger  # Подключаем модуль логирования

def get_valid_input(prompt: str, input_type: type, validation_func=None) -> any:
    """
    Получает ввод от пользователя и проверяет его корректность.

    :param prompt: Сообщение, которое будет показано пользователю.
    :param input_type: Тип ожидаемого ввода (int, float).
    :param validation_func: Функция валидации, которая принимает введенное значение и возвращает True, если значение корректно, и False в противном случае.
    :return: Корректно введенное значение.
    """
    while True:
        try:
            value = input_type(input(prompt))
            if validation_func is None or validation_func(value):
                 return value
            else:
                logger.error('Введено некорректное значение')
        except ValueError:
            logger.error(f'Некорректный ввод. Ожидается {input_type.__name__}')


# Запрашиваем у пользователя количество пицц
quantity = get_valid_input("Сколько пицц вы хотите заказать? ", int, lambda x: x > 0)

# Инициализируем общую стоимость
total_cost = 0

# Цикл для ввода стоимости каждой пиццы
for i in range(quantity):
    pizza_cost = get_valid_input(f"Введите стоимость пиццы {i + 1}: ", float, lambda x: x > 0)
    total_cost += pizza_cost  # Добавляем стоимость пиццы к общей сумме

# Запрашиваем процент чаевых
tip_percent = get_valid_input("Какой процент чаевых вы хотите оставить? ", float, lambda x: 0 <= x <= 100)

# Вычисляем налог (5%)
tax = total_cost * 0.05
# Вычисляем сумму чаевых
tip_amount = total_cost * tip_percent / 100
# Вычисляем полную стоимость заказа
grand_total = total_cost + tax + tip_amount

# Выводим результаты
print(f"Общая стоимость пицц: {total_cost:.2f}")
print(f"Налог: {tax:.2f}")
print(f"Чаевые: {tip_amount:.2f}")
print(f"Полная стоимость заказа: {grand_total:.2f}")

"""
Объяснение кода:
    1. **Инициализация**:
        - ``total_cost = 0``: Инициализирует переменную ``total_cost`` для хранения общей стоимости всех пицц.
        -  Функция ``get_valid_input``: обеспечивает ввод корректных данных от пользователя с использованием try-except и логированием ошибок.

    2. **Ввод количества пицц**:
        -  ``quantity = get_valid_input("Сколько пицц вы хотите заказать? ", int, lambda x: x > 0)``: Запрашивает у пользователя количество пицц и сохраняет его в переменную ``quantity``.
        - Проверка на положительное число: проверяем, что количество пицц больше нуля.

    3. **Цикл для ввода стоимости каждой пиццы**:
        - ``for i in range(quantity):``: Цикл выполняется ``quantity`` раз для каждой пиццы.
        - ``pizza_cost = get_valid_input(f"Введите стоимость пиццы {i + 1}: ", float, lambda x: x > 0)``: Запрашивает стоимость каждой пиццы и сохраняет ее в переменной ``pizza_cost``.
        - ``total_cost += pizza_cost``: Добавляет стоимость текущей пиццы к общей стоимости ``total_cost``.

    4. **Ввод процента чаевых**:
        - ``tip_percent = get_valid_input("Какой процент чаевых вы хотите оставить? ", float, lambda x: 0 <= x <= 100)``: Запрашивает у пользователя процент чаевых.
        - Проверяем, что процент чаевых находится в диапазоне от 0 до 100.

    5.  **Расчеты**:
        - ``tax = total_cost * 0.05``: Вычисляет налог как 5% от общей стоимости.
        - ``tip_amount = total_cost * tip_percent / 100``: Вычисляет сумму чаевых.
        - ``grand_total = total_cost + tax + tip_amount``: Вычисляет полную стоимость заказа, включая стоимость пицц, налог и чаевые.

    6.  **Вывод результатов**:
        - ``print(f"Общая стоимость пицц: {total_cost:.2f}")``: Выводит общую стоимость пицц, форматированную до двух знаков после запятой.
        - ``print(f"Налог: {tax:.2f}")``: Выводит сумму налога.
        - ``print(f"Чаевые: {tip_amount:.2f}")``: Выводит сумму чаевых.
        - ``print(f"Полная стоимость заказа: {grand_total:.2f}")``: Выводит полную стоимость заказа.
"""
```