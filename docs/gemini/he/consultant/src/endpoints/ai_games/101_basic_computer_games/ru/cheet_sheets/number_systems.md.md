# Анализ кода модуля `number_systems.md`

**Качество кода**

-   **Соответствие требованиям к формату кода (1-10):**
    -   **Преимущества:**
        -   Код хорошо структурирован и разбит на логические блоки.
        -   Используются информативные имена функций и переменных.
        -   Присутствуют docstring для функций.
        -   Реализованы функции для преобразования чисел между различными системами счисления.
        -   Представлены примеры использования функций.
        -   Код содержит комментарии, поясняющие основные шаги.
        -   Приведены интересные примеры использования, такие как преобразование фруктов и расчет дней недели.
    -   **Недостатки:**
        -   В коде используется не консистентно форматирование, например отсутствуют пустые строки, как разделители в некоторых частях кода.
        -   Комментарии в коде не соответствуют стандарту reStructuredText (RST).
        -   Не все функции имеют полное описание в docstring.
        -   Отсутствует обработка ошибок с использованием `logger.error`.
        -   Используются `count` для юникод символов.
        -   Используется `isdigit()` для проверки символов в hex.
        -   Избыточное использование `if/elif` в `hex_to_dec`.
        -   Вычисление total_apples не совсем корректно в `sub_fruits`.

**Рекомендации по улучшению**

1.  **Форматирование**: Необходимо привести все комментарии и docstring к стандарту reStructuredText (RST).
2.  **Обработка ошибок**: Заменить стандартные `try-except` блоки на использование `logger.error` для регистрации ошибок.
3.  **Улучшение docstring**: Добавить более подробное описание параметров и возвращаемых значений для каждой функции в формате RST.
4.  **Унификация кода**: Привести код к единому стилю оформления, добавить отступы и разделители для лучшей читаемости.
5.  **Использовать константы**: Заменить magic number на константы для юникод символов.
6.  **Изменить `sub_fruits`**: Переработать логику вычитания, чтобы она была более понятной и корректной, в том числе и для отрицательных значений.
7.  **Переписать `hex_to_dec`**: Использовать словарь для преобразования hex символов в integer значения.
8.  **Проверка входных данных**: Добавить проверку типов входных данных, чтобы избежать ошибок.
9.  **Добавить тесты**: Добавить тесты для каждой функции, чтобы убедиться в их корректной работе.
10. **Рефакторинг**: Рефакторить код для большей читаемости и производительности.

**Улучшенный код**

```python
"""
Модуль для работы с системами счисления и преобразованиями чисел.
==================================================================

Этот модуль содержит функции для работы с различными системами счисления,
включая двоичную, троичную, семеричную, десятичную и шестнадцатеричную.
Также в модуле присутствуют функции для работы с фруктами и днями недели,
которые могут быть рассмотрены как примеры систем счисления.

Примеры использования:
----------------------
    Примеры использования функций представлены в конце файла.

"""
from typing import Any
from src.logger.logger import logger  # Добавлен импорт logger


# Константы для юникода фруктов
APPLE = '🍎'
PEAR = '🍐'
MELON = '🍉'
BASKET = '🧺'

def normalize_fruits(fruits: str) -> str:
    """
    Нормализует строку с фруктами, приводя её к минимальному представлению,
    используя правила обмена фруктов.

    :param fruits: Строка с фруктами (🍎, 🍐, 🍉, 🧺).
    :type fruits: str
    :return: Строка с нормализованным количеством фруктов.
    :rtype: str
    :raises TypeError: Если входные данные не являются строкой.
    """
    if not isinstance(fruits, str): # проверка типа данных
        logger.error(f"Ожидается строка, получено: {type(fruits)}")
        raise TypeError("Ожидается строка")
    apples = fruits.count(APPLE) # подсчет яблок
    pears = fruits.count(PEAR) # подсчет груш
    melons = fruits.count(MELON) # подсчет дынь
    baskets = fruits.count(BASKET) # подсчет корзин

    # Преобразование яблок в груши
    pears += apples // 3
    apples %= 3

    # Преобразование груш в дыни
    melons += (pears * 3) // 5
    pears %= 5

    # Преобразование дынь в корзины
    baskets += melons // 2
    melons %= 2

    # Собираем строку обратно, сначала корзины, потом дыни, груши, яблоки
    return (
        BASKET * baskets
        + MELON * melons
        + PEAR * pears
        + APPLE * apples
    )


def add_fruits(fruits1: str, fruits2: str) -> str:
    """
    Складывает две строки с фруктами.

    :param fruits1: Первая строка с фруктами.
    :type fruits1: str
    :param fruits2: Вторая строка с фруктами.
    :type fruits2: str
    :return: Строка с суммой фруктов.
    :rtype: str
    :raises TypeError: Если входные данные не являются строкой.
    """
    if not isinstance(fruits1, str) or not isinstance(fruits2, str): # проверка типа данных
        logger.error(f"Ожидается строка, получено: {type(fruits1)}, {type(fruits2)}")
        raise TypeError("Ожидается строка")
    return normalize_fruits(fruits1 + fruits2) # складываем строки и нормализуем результат


def sub_fruits(fruits1: str, fruits2: str) -> str:
    """
    Вычитает вторую строку фруктов из первой.

    :param fruits1: Строка с фруктами, из которой вычитаем.
    :type fruits1: str
    :param fruits2: Строка с фруктами, которую вычитаем.
    :type fruits2: str
    :return: Строка с разностью фруктов или "Невозможно вычесть", если результат отрицательный.
    :rtype: str
    :raises TypeError: Если входные данные не являются строкой.
    """
    if not isinstance(fruits1, str) or not isinstance(fruits2, str): # проверка типа данных
        logger.error(f"Ожидается строка, получено: {type(fruits1)}, {type(fruits2)}")
        raise TypeError("Ожидается строка")
    apples1 = fruits1.count(APPLE) # подсчет яблок
    pears1 = fruits1.count(PEAR) # подсчет груш
    melons1 = fruits1.count(MELON) # подсчет дынь
    baskets1 = fruits1.count(BASKET) # подсчет корзин

    apples2 = fruits2.count(APPLE) # подсчет яблок
    pears2 = fruits2.count(PEAR) # подсчет груш
    melons2 = fruits2.count(MELON) # подсчет дынь
    baskets2 = fruits2.count(BASKET) # подсчет корзин


    # Временное представление в виде общего количества яблок
    total_apples1 = apples1 + pears1 * 3 + melons1 * 15 // 3 + baskets1 * 30
    total_apples2 = apples2 + pears2 * 3 + melons2 * 15 // 3 + baskets2 * 30

    if total_apples1 < total_apples2:
        return "Невозможно вычесть"
    else:
        total_apples = total_apples1 - total_apples2

    # Возвращаем нормализованное представление суммы яблок
    result_fruits = ""
    baskets = total_apples // 30
    result_fruits += BASKET * baskets
    total_apples %= 30
    melons = (total_apples * 3) // 15
    result_fruits += MELON * melons
    total_apples %= 15
    pears = total_apples // 3
    result_fruits += PEAR * pears
    total_apples %= 3
    result_fruits += APPLE * total_apples

    return normalize_fruits(result_fruits)



def bin_to_dec(binary: str) -> int:
    """
    Преобразует двоичное число (строку) в десятичное.

    :param binary: Двоичное число в виде строки.
    :type binary: str
    :return: Десятичное представление числа (целое число).
    :rtype: int
    :raises TypeError: Если входные данные не являются строкой.
    :raises ValueError: Если входные данные содержат не двоичные символы.
    """
    if not isinstance(binary, str): # проверка типа данных
        logger.error(f"Ожидается строка, получено: {type(binary)}")
        raise TypeError("Ожидается строка")
    if not all(digit in '01' for digit in binary): # проверка на двоичные символы
        logger.error(f"Входная строка содержит недопустимые символы: {binary}")
        raise ValueError("Двоичное число должно содержать только 0 и 1")
    decimal = 0  # Инициализируем десятичное значение
    power = 0  # Инициализируем степень двойки (показатель разряда)
    for digit in reversed(binary): # Итерируемся по цифрам двоичного числа в обратном порядке
        if digit == '1':
            decimal += 2 ** power # Если цифра '1', добавляем 2 в степени разряда
        power += 1 # Увеличиваем степень для следующего разряда
    return decimal # Возвращаем десятичное значение


def dec_to_bin(decimal: int) -> str:
    """
    Преобразует десятичное число (целое) в двоичное представление (строку).

    :param decimal: Десятичное число.
    :type decimal: int
    :return: Двоичное представление числа (строка).
    :rtype: str
    :raises TypeError: Если входные данные не являются целым числом.
    :raises ValueError: Если входные данные являются отрицательным числом.
    """
    if not isinstance(decimal, int): # проверка типа данных
        logger.error(f"Ожидается целое число, получено: {type(decimal)}")
        raise TypeError("Ожидается целое число")
    if decimal < 0: # проверка на неотрицательность
        logger.error(f"Входное число должно быть неотрицательным: {decimal}")
        raise ValueError("Десятичное число должно быть неотрицательным")
    if decimal == 0: # Если десятичное число равно 0
        return "0"  # Возвращаем строку "0"
    binary = ""  # Инициализируем строку для двоичного числа
    while decimal > 0: # Пока десятичное число больше 0
        binary = str(decimal % 2) + binary  # Добавляем остаток от деления на 2 в начало двоичной строки
        decimal = decimal // 2 # Целочисленно делим десятичное число на 2
    return binary # Возвращаем двоичную строку


def ternary_to_dec(ternary: str) -> int:
    """
    Преобразует троичное число (строку) в десятичное.

    :param ternary: Троичное число в виде строки.
    :type ternary: str
    :return: Десятичное представление числа (целое число).
    :rtype: int
    :raises TypeError: Если входные данные не являются строкой.
    :raises ValueError: Если входные данные содержат не троичные символы.
    """
    if not isinstance(ternary, str): # проверка типа данных
        logger.error(f"Ожидается строка, получено: {type(ternary)}")
        raise TypeError("Ожидается строка")
    if not all(digit in '012' for digit in ternary): # проверка на троичные символы
        logger.error(f"Входная строка содержит недопустимые символы: {ternary}")
        raise ValueError("Троичное число должно содержать только 0, 1 и 2")
    decimal = 0  # Инициализируем десятичное значение
    power = 0 # Инициализируем степень тройки (показатель разряда)
    for digit in reversed(ternary): # Итерируемся по цифрам троичного числа в обратном порядке
        decimal += int(digit) * (3 ** power) # Добавляем цифру * 3 в степени разряда
        power += 1 # Увеличиваем степень для следующего разряда
    return decimal # Возвращаем десятичное значение


def dec_to_ternary(decimal: int) -> str:
    """
    Преобразует десятичное число (целое) в троичное представление (строку).

    :param decimal: Десятичное число.
    :type decimal: int
    :return: Троичное представление числа (строка).
    :rtype: str
    :raises TypeError: Если входные данные не являются целым числом.
    :raises ValueError: Если входные данные являются отрицательным числом.
    """
    if not isinstance(decimal, int): # проверка типа данных
        logger.error(f"Ожидается целое число, получено: {type(decimal)}")
        raise TypeError("Ожидается целое число")
    if decimal < 0: # проверка на неотрицательность
        logger.error(f"Входное число должно быть неотрицательным: {decimal}")
        raise ValueError("Десятичное число должно быть неотрицательным")
    if decimal == 0: # Если десятичное число равно 0
        return "0"  # Возвращаем строку "0"
    ternary = ""  # Инициализируем строку для троичного числа
    while decimal > 0: # Пока десятичное число больше 0
        ternary = str(decimal % 3) + ternary  # Добавляем остаток от деления на 3 в начало троичной строки
        decimal = decimal // 3  # Целочисленно делим десятичное число на 3
    return ternary # Возвращаем троичную строку


def septenary_to_dec(septenary: str) -> int:
    """
    Преобразует семеричное число (строку) в десятичное.

    :param septenary: Семеричное число в виде строки.
    :type septenary: str
    :return: Десятичное представление числа (целое число).
    :rtype: int
    :raises TypeError: Если входные данные не являются строкой.
    :raises ValueError: Если входные данные содержат не семеричные символы.
    """
    if not isinstance(septenary, str): # проверка типа данных
        logger.error(f"Ожидается строка, получено: {type(septenary)}")
        raise TypeError("Ожидается строка")
    if not all(digit in '0123456' for digit in septenary): # проверка на семеричные символы
        logger.error(f"Входная строка содержит недопустимые символы: {septenary}")
        raise ValueError("Семеричное число должно содержать только цифры от 0 до 6")
    decimal = 0  # Инициализируем десятичное значение
    power = 0 # Инициализируем степень семерки (показатель разряда)
    for digit in reversed(septenary): # Итерируемся по цифрам семеричного числа в обратном порядке
        decimal += int(digit) * (7 ** power) # Добавляем цифру * 7 в степени разряда
        power += 1 # Увеличиваем степень для следующего разряда
    return decimal # Возвращаем десятичное значение


def dec_to_septenary(decimal: int) -> str:
    """
    Преобразует десятичное число (целое) в семеричное представление (строку).

    :param decimal: Десятичное число.
    :type decimal: int
    :return: Семеричное представление числа (строка).
    :rtype: str
    :raises TypeError: Если входные данные не являются целым числом.
    :raises ValueError: Если входные данные являются отрицательным числом.
    """
    if not isinstance(decimal, int): # проверка типа данных
        logger.error(f"Ожидается целое число, получено: {type(decimal)}")
        raise TypeError("Ожидается целое число")
    if decimal < 0: # проверка на неотрицательность
        logger.error(f"Входное число должно быть неотрицательным: {decimal}")
        raise ValueError("Десятичное число должно быть неотрицательным")
    if decimal == 0: # Если десятичное число равно 0
        return "0"  # Возвращаем строку "0"
    septenary = ""  # Инициализируем строку для семеричного числа
    while decimal > 0: # Пока десятичное число больше 0
        septenary = str(decimal % 7) + septenary  # Добавляем остаток от деления на 7 в начало семеричной строки
        decimal = decimal // 7  # Целочисленно делим десятичное число на 7
    return septenary # Возвращаем семеричную строку



def hex_to_dec(hexadecimal: str) -> int:
    """
    Преобразует шестнадцатеричное число (строку) в десятичное.

    :param hexadecimal: Шестнадцатеричное число в виде строки.
    :type hexadecimal: str
    :return: Десятичное представление числа (целое число).
    :rtype: int
    :raises TypeError: Если входные данные не являются строкой.
    :raises ValueError: Если входные данные содержат не шестнадцатеричные символы.
    """
    if not isinstance(hexadecimal, str): # проверка типа данных
        logger.error(f"Ожидается строка, получено: {type(hexadecimal)}")
        raise TypeError("Ожидается строка")
    hex_digits = "0123456789ABCDEF"
    if not all(digit.upper() in hex_digits for digit in hexadecimal):  # проверка на hex символы
        logger.error(f"Входная строка содержит недопустимые символы: {hexadecimal}")
        raise ValueError("Шестнадцатеричное число должно содержать только цифры от 0 до 9 и буквы от A до F")
    decimal = 0  # Инициализируем десятичное значение
    power = 0 # Инициализируем степень 16 (показатель разряда)
    hex_values = {str(i): i for i in range(10)} # значения для цифр
    hex_values.update({'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}) # добавляем значения для букв
    for digit in reversed(hexadecimal):  # Итерируемся по цифрам шестнадцатеричного числа в обратном порядке
        decimal += hex_values[digit.upper()] * (16 ** power)  # Добавляем цифру * 16 в степени разряда
        power += 1 # Увеличиваем степень для следующего разряда
    return decimal # Возвращаем десятичное значение


def dec_to_hex(decimal: int) -> str:
    """
    Преобразует десятичное число (целое) в шестнадцатеричное представление (строку).

    :param decimal: Десятичное число.
    :type decimal: int
    :return: Шестнадцатеричное представление числа (строка).
    :rtype: str
    :raises TypeError: Если входные данные не являются целым числом.
    :raises ValueError: Если входные данные являются отрицательным числом.
    """
    if not isinstance(decimal, int): # проверка типа данных
        logger.error(f"Ожидается целое число, получено: {type(decimal)}")
        raise TypeError("Ожидается целое число")
    if decimal < 0: # проверка на неотрицательность
        logger.error(f"Входное число должно быть неотрицательным: {decimal}")
        raise ValueError("Десятичное число должно быть неотрицательным")
    if decimal == 0: # Если десятичное число равно 0
        return "0" # Возвращаем строку "0"
    hex_digits = "0123456789ABCDEF" # Строка для соответствия остатков и шестнадцатеричных цифр
    hexadecimal = ""  # Инициализируем строку для шестнадцатеричного числа
    while decimal > 0:  # Пока десятичное число больше 0
        remainder = decimal % 16 # Получаем остаток от деления на 16
        hexadecimal = hex_digits[remainder] + hexadecimal # Добавляем соответствующую цифру в начало шестнадцатеричной строки
        decimal = decimal // 16  # Целочисленно делим десятичное число на 16
    return hexadecimal  # Возвращаем шестнадцатеричную строку


def calculate_day_of_week(start_day: int, days_passed: float) -> int:
    """
    Рассчитывает день недели после заданного количества дней.

    :param start_day: Начальный день недели (0 - понедельник, 6 - воскресенье).
    :type start_day: int
    :param days_passed: Количество прошедших дней.
    :type days_passed: float
    :return: День недели после заданного количества дней (0 - понедельник, 6 - воскресенье).
    :rtype: int
    :raises TypeError: Если start_day не является целым числом или days_passed не является числом.
    :raises ValueError: Если start_day не находится в диапазоне от 0 до 6.
    """
    if not isinstance(start_day, int):  # проверка типа данных
        logger.error(f"Ожидается целое число, получено: {type(start_day)}")
        raise TypeError("Начальный день недели должен быть целым числом")
    if not isinstance(days_passed, (int, float)): # проверка типа данных
        logger.error(f"Ожидается число, получено: {type(days_passed)}")
        raise TypeError("Количество прошедших дней должно быть числом")
    if not (0 <= start_day <= 6): # проверка на допустимый диапазон
        logger.error(f"Начальный день недели должен быть целым числом от 0 до 6 (пн-вс), получено: {start_day}")
        raise ValueError("Начальный день недели должен быть целым числом от 0 до 6 (пн-вс)")

    days_passed = int(days_passed)
    new_day = (start_day + days_passed) % 7
    return new_day


def day_number_to_name(day_number: int) -> str:
    """
    Преобразует номер дня недели (0-6) в его название.

    :param day_number: Номер дня недели (0 - понедельник, 6 - воскресенье).
    :type day_number: int
    :return: Название дня недели (строка).
    :rtype: str
    :raises TypeError: Если входные данные не являются целым числом.
    :raises ValueError: Если входные данные не находятся в диапазоне от 0 до 6.
    """
    if not isinstance(day_number, int): # проверка типа данных
        logger.error(f"Ожидается целое число, получено: {type(day_number)}")
        raise TypeError("Ожидается целое число")
    if not (0 <= day_number <= 6): # проверка на допустимый диапазон
        logger.error(f"Номер дня недели должен быть целым числом от 0 до 6 (пн-вс), получено: {day_number}")
        raise ValueError("Номер дня недели должен быть целым числом от 0 до 6 (пн-вс)")
    days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    return days[day_number]


# Примеры:
fruits1 = "🍎🍎🍎🍎🍎" # 5 яблок
fruits2 = "🍎🍎🍎" # 3 яблока
print(f"{fruits1} + {fruits2} = {add_fruits(fruits1, fruits2)}")

fruits3 = "🍐🍐"  # 2 груши
fruits4 = "🍎🍎🍎🍎" # 4 яблока
print(f"{fruits3} + {fruits4} = {add_fruits(fruits3, fruits4)}")

fruits5 = "🍉🍉" # 2 дыни
fruits6 = "🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎" # 15 яблок
print(f"{fruits5} + {fruits6} = {add_fruits(fruits5, fruits6)}")

fruits7 = "🧺🧺" # 2 корзины
fruits8 = "🍉🍉🍉" # 3 дыни
print(f"{fruits7} + {fruits8} = {add_fruits(fruits7, fruits8)}")

fruits9 = "🧺🍉🍐🍎" # 1 корзина, 1 дыня, 1 груша, 1 яблоко
fruits10 = "🍉🍐🍎" # 1 дыня, 1 груша, 1 яблоко
print(f"{fruits9} - {fruits10} = {sub_fruits(fruits9, fruits10)}")

fruits11 = "🧺🍉" # 1 корзина, 1 дыня
fruits12 = "🧺🍉🍎🍎🍎" # 1 корзина, 1 дыня, 3 яблока
print(f"{fruits11} - {fruits12} = {sub_fruits(fruits11, fruits12)}")

fruits13 = "🍉🍉🍉" # 3 дыни
fruits14 = "🍎🍎🍎🍎" # 4 яблока
print(f"{fruits13} - {fruits14} = {sub_fruits(fruits13, fruits14)}")

fruits15 = "🍐🍐🍐🍐🍐" # 5 груш
fruits16 = "🍉" # 1 дыня
print(f"{fruits15} - {fruits16} = {sub_fruits(fruits15, fruits16)}")

binary_number = "1011"
decimal_number = bin_to_dec(binary_number)
print(f"Двоичное {binary_number} = Десятичное {decimal_number}")

decimal_number = 11
binary_number = dec_to_bin(decimal_number)
print(f"Десятичное {decimal_number} = Двоичное {binary_number}")

ternary_number = "210"
decimal_number = ternary_to_dec(ternary_number)
print(f"Троичное {ternary_number} = Десятичное {decimal_number}")

decimal_number = 21
ternary_number = dec_to_ternary(decimal_number)
print(f"Десятичное {decimal_number} = Троичное {ternary_number}")

septenary_number = "345"
decimal_number = septenary_to_dec(septenary_number)
print(f"Семеричное {septenary_number} = Десятичное {decimal_number}")

decimal_number = 180
septenary_number = dec_to_septenary(decimal_number)
print(f"Десятичное {decimal_number} = Семеричное {septenary_number}")

hex_number = "2AF"
decimal_number = hex_to_dec(hex_number)
print(f"Шестнадцатеричное {hex_number} = Десятичное {decimal_number}")

decimal_number = 687
hex_number = dec_to_hex(decimal_number)
print(f"Десятичное {decimal_number} = Шестнадцатеричное {hex_number}")

start_day = 0  # Понедельник
days = 10.5 #Полторы недели
new_day = calculate_day_of_week(start_day, days)
print(f"{days} дня после {day_number_to_name(start_day)}: {day_number_to_name(new_day)}")
days = 120 # Четыре месяца (приблизительно)
new_day = calculate_day_of_week(start_day, days)
print(f"{days} дня после {day_number_to_name(start_day)}: {day_number_to_name(new_day)}")

# можно начинать отсчет от другого дня
start_day = 4  # Пятница
days = 365 # Год
new_day = calculate_day_of_week(start_day, days)
print(f"{days} дня после {day_number_to_name(start_day)}: {day_number_to_name(new_day)}")
```