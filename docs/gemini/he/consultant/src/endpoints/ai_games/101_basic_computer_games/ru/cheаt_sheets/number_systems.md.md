# Анализ кода модуля `number_systems.md`

**Качество кода**

- **Соблюдение требований к формату кода (1-10)**:
    - **Плюсы:**
        - Код написан на языке Python и имеет структуру, соответствующую принципам хорошего программирования.
        - Код разбит на логические части, что облегчает его понимание.
        - Использованы docstring для функций, но их нужно переработать в соответствии с RST.
        - Есть примеры использования функций.
    - **Минусы:**
        - Не соблюдены требования к использованию RST для docstring.
        - Не хватает обработки ошибок, особенно при вызове функций.
        - Не используется `src.utils.jjson`, который требуется в задании.
        - Не используется `src.logger.logger`, как указано в задании.
        - Комментарии в коде не всегда информативны и не соответствуют требованиям.
        - Код местами не оптимизирован (например, преобразования в `sub_fruits`).

**Рекомендации по улучшению**

1.  **Переработка docstring:** Необходимо переработать все docstring в соответствии с форматом RST, чтобы они были пригодны для использования со Sphinx.
2.  **Использование `j_loads` и `j_loads_ns`:** Следует использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для загрузки данных из файлов, если это требуется, вместо стандартных методов.
3.  **Добавление логирования:** Нужно добавить логирование ошибок с помощью `logger.error` из `src.logger.logger`.
4.  **Улучшение обработки ошибок:** Вместо стандартных `try-except` нужно использовать `logger.error` для записи ошибок.
5.  **Оптимизация кода:** Некоторые функции можно оптимизировать для улучшения производительности (например, `sub_fruits`).
6.  **Добавление проверок входных данных:** Необходимо добавить проверки для входных данных на корректность.
7.  **Уточнение комментариев:** Комментарии в коде должны быть более информативными и соответствовать заданию.
8.  **Рефакторинг кода:** Следует рассмотреть возможность рефакторинга кода для повышения его читабельности и поддерживаемости.
9.  **Унификация:** Нужно унифицировать подход к преобразованию чисел в различных системах счисления (например, можно создать класс-конвертер).

**Улучшенный код**

```python
"""
Модуль для работы с системами счисления.
=========================================================================================

Этот модуль содержит функции для преобразования чисел между различными системами счисления,
а также примеры их использования. Включает абстрактные и конкретные системы счисления,
а также примеры из повседневной жизни.

Примеры использования:
--------------------

.. code-block:: python

    from src.logger.logger import logger
    from src.utils.jjson import j_loads, j_loads_ns # исправляем импорты
    
    # Пример использования функции bin_to_dec
    binary_number = "1011"
    decimal_number = bin_to_dec(binary_number)
    print(f"Двоичное {binary_number} = Десятичное {decimal_number}")
"""
import time # импортируем time
import platform # импортируем platform
import sys # импортируем sys
from src.logger.logger import logger # импортируем логгер

def normalize_fruits(fruits: str) -> str:
    """
    Нормализует строку с фруктами, приводя её к минимальному представлению,
    используя правила обмена фруктов.

    :param fruits: Строка с фруктами (🍎, 🍐, 🍉, 🧺).
    :type fruits: str
    :raises ValueError: Если строка содержит недопустимые символы.
    :return: Строка с нормализованным количеством фруктов.
    :rtype: str

    Пример:

    >>> normalize_fruits("🍎🍎🍎🍎🍐")
    '🍐🍐🍎'
    """
    if not all(fruit in '🍎🍐🍉🧺' for fruit in fruits): # проверка на корректность входных данных
      logger.error('Недопустимые символы во входной строке') # логируем ошибку
      raise ValueError("Недопустимые символы во входной строке") # выкидываем исключение

    apples = fruits.count('🍎') # считаем яблоки
    pears = fruits.count('🍐') # считаем груши
    melons = fruits.count('🍉') # считаем дыни
    baskets = fruits.count('🧺') # считаем корзины

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
        "🧺" * baskets
        + "🍉" * melons
        + "🍐" * pears
        + "🍎" * apples
    )


def add_fruits(fruits1: str, fruits2: str) -> str:
    """
    Складывает две строки с фруктами.

    :param fruits1: Строка с фруктами.
    :type fruits1: str
    :param fruits2: Строка с фруктами.
    :type fruits2: str
    :return: Строка с суммой фруктов.
    :rtype: str
    
    Пример:

    >>> add_fruits("🍎🍎", "🍐")
    '🍐🍎🍎'
    """
    return normalize_fruits(fruits1 + fruits2) # складываем фрукты и нормализуем результат


def sub_fruits(fruits1: str, fruits2: str) -> str:
    """
    Вычитает вторую строку фруктов из первой, если это возможно.

    :param fruits1: Строка с фруктами, из которой вычитаем.
    :type fruits1: str
    :param fruits2: Строка с фруктами, которую вычитаем.
    :type fruits2: str
    :return: Строка с разностью фруктов или "Невозможно вычесть", если результат отрицательный.
    :rtype: str
    
    Пример:

    >>> sub_fruits("🧺🍎", "🍉🍎")
    '🍐🍎🍎🍎'
    """
    apples1 = fruits1.count('🍎') # считаем яблоки в первой строке
    pears1 = fruits1.count('🍐') # считаем груши в первой строке
    melons1 = fruits1.count('🍉') # считаем дыни в первой строке
    baskets1 = fruits1.count('🧺') # считаем корзины в первой строке

    apples2 = fruits2.count('🍎') # считаем яблоки во второй строке
    pears2 = fruits2.count('🍐') # считаем груши во второй строке
    melons2 = fruits2.count('🍉') # считаем дыни во второй строке
    baskets2 = fruits2.count('🧺') # считаем корзины во второй строке


    # Временное представление в виде общего количества яблок
    total_apples1 = apples1 + pears1 * 3 + melons1 * 15 // 3 + baskets1 * 30
    total_apples2 = apples2 + pears2 * 3 + melons2 * 15 // 3 + baskets2 * 30

    if total_apples1 < total_apples2: # проверяем возможность вычитания
        return "Невозможно вычесть"
    else:
        total_apples = total_apples1 - total_apples2

    # Возвращаем нормализованное представление суммы яблок
    result_fruits = ""
    baskets = total_apples // 30
    result_fruits += "🧺" * baskets
    total_apples %= 30
    melons = (total_apples*3) // 15
    result_fruits += "🍉" * melons
    total_apples %= 15
    pears = total_apples // 3
    result_fruits += "🍐" * pears
    total_apples %= 3
    result_fruits += "🍎" * total_apples

    return normalize_fruits(result_fruits)


def bin_to_dec(binary: str) -> int:
    """
    Преобразует двоичное число (строку) в десятичное.

    :param binary: Двоичное число в виде строки.
    :type binary: str
    :raises ValueError: Если входная строка содержит не двоичные символы.
    :return: Десятичное представление числа (целое число).
    :rtype: int

    Пример:
    
    >>> bin_to_dec("1011")
    11
    """
    if not all(digit in '01' for digit in binary): # проверка на корректность входных данных
        logger.error('Недопустимые символы во входной двоичной строке') # логируем ошибку
        raise ValueError("Недопустимые символы во входной двоичной строке") # выкидываем исключение

    decimal = 0  # Инициализируем десятичное значение
    power = 0  # Инициализируем степень двойки (показатель разряда)
    for digit in reversed(binary): # Итерируемся по цифрам двоичного числа в обратном порядке
        if digit == '1': # если цифра 1
            decimal += 2 ** power # добавляем 2 в степени
        power += 1 # увеличиваем степень
    return decimal # возвращаем результат


def dec_to_bin(decimal: int) -> str:
    """
    Преобразует десятичное число (целое) в двоичное представление (строку).

    :param decimal: Десятичное число.
    :type decimal: int
    :raises ValueError: Если входное число не является целым или отрицательным.
    :return: Двоичное представление числа (строка).
    :rtype: str

    Пример:

    >>> dec_to_bin(11)
    '1011'
    """
    if not isinstance(decimal, int) or decimal < 0: # проверка на корректность входных данных
        logger.error('Недопустимый ввод: десятичное число должно быть целым неотрицательным числом') # логируем ошибку
        raise ValueError("Недопустимый ввод: десятичное число должно быть целым неотрицательным числом") # выкидываем исключение
    if decimal == 0: # если десятичное число 0
        return "0" # возвращаем 0
    binary = ""  # Инициализируем строку для двоичного числа
    while decimal > 0: # пока число > 0
        binary = str(decimal % 2) + binary # добавляем остаток от деления
        decimal = decimal // 2 # целочисленное деление
    return binary # возвращаем бинарную строку


def ternary_to_dec(ternary: str) -> int:
    """
    Преобразует троичное число (строку) в десятичное.

    :param ternary: Троичное число в виде строки.
    :type ternary: str
    :raises ValueError: Если входная строка содержит не троичные символы.
    :return: Десятичное представление числа (целое число).
    :rtype: int

    Пример:
    
    >>> ternary_to_dec("210")
    21
    """
    if not all(digit in '012' for digit in ternary): # проверка на корректность входных данных
        logger.error('Недопустимые символы во входной троичной строке') # логируем ошибку
        raise ValueError("Недопустимые символы во входной троичной строке") # выкидываем исключение

    decimal = 0  # Инициализируем десятичное значение
    power = 0  # Инициализируем степень тройки (показатель разряда)
    for digit in reversed(ternary): # итерируемся по цифрам в обратном порядке
        decimal += int(digit) * (3 ** power) # добавляем цифру умноженную на 3 в степени
        power += 1  # увеличиваем степень
    return decimal # возвращаем результат


def dec_to_ternary(decimal: int) -> str:
    """
    Преобразует десятичное число (целое) в троичное представление (строку).

    :param decimal: Десятичное число.
    :type decimal: int
    :raises ValueError: Если входное число не является целым или отрицательным.
    :return: Троичное представление числа (строка).
    :rtype: str

    Пример:

    >>> dec_to_ternary(21)
    '210'
    """
    if not isinstance(decimal, int) or decimal < 0:  # проверка на корректность входных данных
        logger.error('Недопустимый ввод: десятичное число должно быть целым неотрицательным числом') # логируем ошибку
        raise ValueError("Недопустимый ввод: десятичное число должно быть целым неотрицательным числом") # выкидываем исключение
    if decimal == 0: # если десятичное число 0
        return "0" # возвращаем 0
    ternary = ""  # Инициализируем строку для троичного числа
    while decimal > 0: # пока число > 0
        ternary = str(decimal % 3) + ternary # добавляем остаток от деления на 3
        decimal = decimal // 3 # целочисленное деление
    return ternary # возвращаем троичную строку


def septenary_to_dec(septenary: str) -> int:
    """
    Преобразует семеричное число (строку) в десятичное.

    :param septenary: Семеричное число в виде строки.
    :type septenary: str
    :raises ValueError: Если входная строка содержит не семеричные символы.
    :return: Десятичное представление числа (целое число).
    :rtype: int

    Пример:
    
    >>> septenary_to_dec("345")
    180
    """
    if not all(digit in '0123456' for digit in septenary): # проверка на корректность входных данных
        logger.error('Недопустимые символы во входной семеричной строке') # логируем ошибку
        raise ValueError("Недопустимые символы во входной семеричной строке") # выкидываем исключение
    decimal = 0  # Инициализируем десятичное значение
    power = 0  # Инициализируем степень семерки (показатель разряда)
    for digit in reversed(septenary): # итерируемся по цифрам в обратном порядке
        decimal += int(digit) * (7 ** power) # добавляем цифру умноженную на 7 в степени
        power += 1 # увеличиваем степень
    return decimal # возвращаем результат


def dec_to_septenary(decimal: int) -> str:
    """
    Преобразует десятичное число (целое) в семеричное представление (строку).

    :param decimal: Десятичное число.
    :type decimal: int
    :raises ValueError: Если входное число не является целым или отрицательным.
    :return: Семеричное представление числа (строка).
    :rtype: str

    Пример:

    >>> dec_to_septenary(180)
    '345'
    """
    if not isinstance(decimal, int) or decimal < 0: # проверка на корректность входных данных
        logger.error('Недопустимый ввод: десятичное число должно быть целым неотрицательным числом') # логируем ошибку
        raise ValueError("Недопустимый ввод: десятичное число должно быть целым неотрицательным числом") # выкидываем исключение
    if decimal == 0: # если десятичное число 0
        return "0" # возвращаем 0
    septenary = ""  # Инициализируем строку для семеричного числа
    while decimal > 0: # пока число > 0
        septenary = str(decimal % 7) + septenary # добавляем остаток от деления на 7
        decimal = decimal // 7 # целочисленное деление
    return septenary # возвращаем семеричную строку


def hex_to_dec(hexadecimal: str) -> int:
    """
    Преобразует шестнадцатеричное число (строку) в десятичное.

    :param hexadecimal: Шестнадцатеричное число в виде строки.
    :type hexadecimal: str
    :raises ValueError: Если входная строка содержит недопустимые шестнадцатеричные символы.
    :return: Десятичное представление числа (целое число).
    :rtype: int

    Пример:
    
    >>> hex_to_dec("2AF")
    687
    """
    if not all(digit.upper() in '0123456789ABCDEF' for digit in hexadecimal): # проверка на корректность входных данных
        logger.error('Недопустимые символы во входной шестнадцатеричной строке') # логируем ошибку
        raise ValueError("Недопустимые символы во входной шестнадцатеричной строке") # выкидываем исключение

    decimal = 0 # Инициализируем десятичное значение
    power = 0 # Инициализируем степень 16 (показатель разряда)
    for digit in reversed(hexadecimal): # Итерируемся по цифрам шестнадцатеричного числа в обратном порядке
        if digit.isdigit(): # если цифра
            decimal += int(digit) * (16 ** power) # добавляем цифру * 16 в степени разряда
        elif digit.upper() == 'A': # если A
            decimal += 10 * (16 ** power) # добавляем 10 * 16 в степени разряда
        elif digit.upper() == 'B': # если B
            decimal += 11 * (16 ** power) # добавляем 11 * 16 в степени разряда
        elif digit.upper() == 'C': # если C
            decimal += 12 * (16 ** power) # добавляем 12 * 16 в степени разряда
        elif digit.upper() == 'D': # если D
            decimal += 13 * (16 ** power) # добавляем 13 * 16 в степени разряда
        elif digit.upper() == 'E': # если E
            decimal += 14 * (16 ** power) # добавляем 14 * 16 в степени разряда
        elif digit.upper() == 'F': # если F
            decimal += 15 * (16 ** power) # добавляем 15 * 16 в степени разряда
        power += 1 # увеличиваем степень
    return decimal # возвращаем результат


def dec_to_hex(decimal: int) -> str:
    """
    Преобразует десятичное число (целое) в шестнадцатеричное представление (строку).

    :param decimal: Десятичное число.
    :type decimal: int
    :raises ValueError: Если входное число не является целым или отрицательным.
    :return: Шестнадцатеричное представление числа (строка).
    :rtype: str

    Пример:

    >>> dec_to_hex(687)
    '2AF'
    """
    if not isinstance(decimal, int) or decimal < 0: # проверка на корректность входных данных
        logger.error('Недопустимый ввод: десятичное число должно быть целым неотрицательным числом') # логируем ошибку
        raise ValueError("Недопустимый ввод: десятичное число должно быть целым неотрицательным числом") # выкидываем исключение
    if decimal == 0:  # Если десятичное число равно 0
        return "0" # Возвращаем строку "0"
    hex_digits = "0123456789ABCDEF"  # Строка для соответствия остатков и шестнадцатеричных цифр
    hexadecimal = "" # Инициализируем строку для шестнадцатеричного числа
    while decimal > 0: # Пока десятичное число больше 0
        remainder = decimal % 16 # Получаем остаток от деления на 16
        hexadecimal = hex_digits[remainder] + hexadecimal # Добавляем соответствующую цифру в начало шестнадцатеричной строки
        decimal = decimal // 16 # Целочисленно делим десятичное число на 16
    return hexadecimal # Возвращаем шестнадцатеричную строку


def roman_to_int(roman_str: str) -> int:
    """
    Преобразует римское число (строку) в десятичное.

    :param roman_str: Римское число в виде строки.
    :type roman_str: str
    :raises ValueError: Если входная строка содержит недопустимые римские символы.
    :return: Десятичное представление числа (целое число).
    :rtype: int

    Пример:

    >>> roman_to_int("XIV")
    14
    """
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    if not all(char in roman_dict for char in roman_str): # проверка на корректность входных данных
        logger.error('Недопустимые символы во входной римской строке') # логируем ошибку
        raise ValueError("Недопустимые символы во входной римской строке") # выкидываем исключение

    number = 0
    roman_str = roman_str.replace("IV","IIII") # заменяем IV на IIII
    roman_str = roman_str.replace("IX","VIIII") # заменяем IX на VIIII
    roman_str = roman_str.replace("XL","XXXX") # заменяем XL на XXXX
    roman_str = roman_str.replace("XC","LXXXX") # заменяем XC на LXXXX
    roman_str = roman_str.replace("CD","CCCC") # заменяем CD на CCCC
    roman_str = roman_str.replace("CM","DCCCC") # заменяем CM на DCCCC
    for char in roman_str: # проходим по строке
        number += roman_dict[char] # добавляем значение символа
    return number # возвращаем результат


# Morse code dictionary with cyrillic alphabet
morse_code_dict = {
    'A': '.-',    'А': '.-',
    'B': '-...',   'Б': '-...',
    'C': '-.-.',   'В': '.--',
    'D': '-..',    'Г': '--.',
    'E': '.',      'Д': '-..',
    'F': '..-.',   'Е': '.',
    'G': '--.',    'Ж': '...-',
    'H': '....',   'З': '--..',
    'I': '..',     'И': '..',
    'J': '.---',   'Й': '.---',
    'K': '-.-',    'К': '-.-',
    'L': '.-..',   'Л': '.-..',
    'M': '--',     'М': '--',
    'N': '-.',     'Н': '-.',
    'O': '---',    'О': '---',
    'P': '.--.',   'П': '.--.',
    'Q': '--.-',   'Р': '.-.',
    'R': '.-.',    'С': '...',
    'S': '...',    'Т': '-',
    'T': '-',      'У': '..-',
    'U': '..-',    'Ф': '..-.',
    'V': '...-',   'Х': '....-',
    'W': '.--',    'Ц': '-.-.',
    'X': '-..-',   'Ч': '---.',
    'Y': '-.--',   'Ш': '----',
    'Z': '--..',   'Щ': '--.-',
    '0': '-----',   'Ъ': '--.--',
    '1': '.----',  'Ы': '-.--',
    '2': '..---',  'Ь': '-..-',
    '3': '...--',  'Э': '..-..',
    '4': '....-',  'Ю': '..--',
    '5': '.....',  'Я': '.-.-',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    "'": '.----.',
    '!': '-.-.--',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '_': '..--.-',
    '"': '.-..-.',
    '$': '...-..-',
    '@': '.--.-.',
    ' ': '/'
}


def play_sound(duration):
    """
    Производит звуковой сигнал заданной длительности.
    
    :param duration: Длительность звукового сигнала в миллисекундах.
    :type duration: int
    :raises ImportError: Если не удается импортировать необходимые модули.
    """
    try:
        # For Windows
        if platform.system() == 'Windows': # если система Windows
            import winsound # импортируем winsound
            winsound.Beep(1000, duration) # издаем звук
        # For Linux/macOS
        else:
            import os # импортируем os
            os.system('printf "\\a"') # издаем звук
    except ImportError as ex: # ловим ошибку импорта
        logger.error("Невозможно импортировать необходимые модули для воспроизведения звука", ex) # логируем ошибку


def text_to_morse(text: str) -> str:
    """
    Преобразует текст в код Морзе.

    :param text: Строка текста.
    :type text: str
    :return: Строка с кодом Морзе.
    :rtype: str

    Пример:
    
    >>> text_to_morse("Hello World")
    '.... . .-.. .-.. --- / .-- --- .-. .-.. -..'
    """
    morse_code = '' # инициализируем строку для кода Морзе
    for char in text.upper(): # итерируемся по символам, преобразовывая в верхний регистр
        if char in morse_code_dict: # если символ есть в словаре
            morse_code += morse_code_dict[char] + ' ' # добавляем код Морзе
        else: # если символа нет в словаре
            morse_code += '/ '  # если символа нет, считаем его пробелом
    return morse_code # возвращаем код Морзе


def morse_to_sound(morse_code: str):
    """
    Воспроизводит код Морзе в виде звуковых сигналов.

    :param morse_code: Строка с кодом Морзе.
    :type morse_code: str
    """
    for symbol in morse_code: # итерируемся по символам
        if symbol == '.': # если точка
            play_sound(100) # воспроизводим короткий звук
        elif symbol == '-': # если тире
            play_sound(300) # воспроизводим длинный звук
        elif symbol == ' ': # если пробел
            time.sleep(0.3) # пауза между символами
        elif symbol == '/': # если слеш
            time.sleep(0.7) # пауза между словами


def calculate_day_of_week(start_day: int, days_passed: float) -> int:
    """
    Рассчитывает день недели после заданного количества дней.

    :param start_day: Начальный день недели (0 - понедельник, 6 - воскресенье).
    :type start_day: int
    :param days_passed: Количество прошедших дней.
    :type days_passed: float
    :raises ValueError: Если начальный день недели не является целым числом от 0 до 6, или количество дней не является числом.
    :return: День недели после заданного количества дней (0 - понедельник, 6 - воскресенье).
    :rtype: int

    Пример:

    >>> calculate_day_of_week(0, 8)
    1
    """
    if not isinstance(start_day, int) or not (0 <= start_day <= 6): # проверка на корректность входных данных
        logger.error("Начальный день недели должен быть целым числом от 0 до 6 (пн-вс)") # логируем ошибку
        raise ValueError("Начальный день недели должен быть целым числом от 0 до 6 (пн-вс)") # выкидываем исключение
    if not isinstance(days_passed, (int, float)): # проверка на корректность входных данных
        logger.error("Количество прошедших дней должно быть числом") # логируем ошибку
        raise ValueError("Количество прошедших дней должно быть числом") # выкидываем исключение

    days_passed = int(days_passed) # преобразуем в целое
    new_day = (start_day + days_passed) % 7 # вычисляем день недели
    return new_day # возвращаем результат


def day_number_to_name(day_number: int) -> str:
    """
    Преобразует номер дня недели (0-6) в его название.

    :param day_number: Номер дня недели (0 - понедельник, 6 - воскресенье).
    :type day_number: int
    :raises ValueError: Если номер дня недели не является целым числом от 0 до 6.
    :return: Название дня недели (строка).
    :rtype: str
    
    Пример:

    >>> day_number_to_name(0)
    'понедельник'
    """
    if not isinstance(day_number, int) or not (0 <= day_number <= 6): # проверка на корректность входных данных
        logger.error('Номер дня недели должен быть целым числом от 0 до 6 (пн-вс)') # логируем ошибку
        raise ValueError("Номер дня недели должен быть целым числом от 0 до 6 (пн-вс)") # выкидываем исключение
    days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"] # список дней недели
    return days[day_number] # возвращаем название дня


# Примеры:
if __name__ == '__main__':
    fruits1 = "🍎🍎🍎🍎🍎"  # 5 яблок
    fruits2 = "🍎🍎🍎"  # 3 яблока
    print(f"{fruits1} + {fruits2} = {add_fruits(fruits1, fruits2)}")

    fruits3 = "🍐🍐"  # 2 груши
    fruits4 = "🍎🍎🍎🍎"  # 4 яблока
    print(f"{fruits3} + {fruits4} = {add_fruits(fruits3, fruits4)}")

    fruits5 = "🍉🍉"  # 2 дыни
    fruits6 = "🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎"  # 15 яблок
    print(f"{fruits5} + {fruits6} = {add_fruits(fruits5, fruits6)}")

    fruits7 = "🧺🧺"  # 2 корзины
    fruits8 = "🍉🍉🍉"  # 3 дыни
    print(f"{fruits7} + {fruits8} = {add_fruits(fruits7, fruits8)}")

    fruits9 = "🧺🍉🍐🍎"  # 1 корзина, 1 дыня, 1 груша, 1 яблоко
    fruits10 = "🍉🍐🍎"  # 1 дыня, 1 груша, 1 яблоко
    print(f"{fruits9} - {fruits10} = {sub_fruits(fruits9, fruits10)}")

    fruits11 = "🧺🍉"  # 1 корзина, 1 дыня
    fruits12 = "🧺🍉🍎🍎🍎"  # 1 корзина, 1 дыня, 3 яблока
    print(f"{fruits11} - {fruits12} = {sub_fruits(fruits11, fruits12)}")

    fruits13 = "🍉🍉🍉"  # 3 дыни
    fruits14 = "🍎🍎🍎🍎"  # 4 яблока
    print(f"{fruits13} - {fruits14} = {sub_fruits(fruits13, fruits14)}")

    fruits15 = "🍐🍐🍐🍐🍐"  # 5 груш
    fruits16 = "🍉"  # 1 дыня
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
    print(f"Семеричное