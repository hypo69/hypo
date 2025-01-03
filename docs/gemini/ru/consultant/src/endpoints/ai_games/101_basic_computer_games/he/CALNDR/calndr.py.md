# Анализ кода модуля `calndr.py`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и разбит на функции, что повышает читаемость и поддерживаемость.
    - Используются понятные имена переменных и функций.
    - Код корректно рассчитывает дни недели и количество дней в месяце, включая високосные годы.
    - Код обрабатывает ошибки ввода, проверяя корректность месяца.
-  Минусы
    - Отсутствуют docstring для модуля и функций, что затрудняет понимание назначения кода.
    - Нет обработки исключений для невалидного ввода года.
    - Не используется логирование.
    - Код содержит комментарии на иврите, что не соответствует стандарту.

**Рекомендации по улучшению**
1. Добавить docstring в формате reStructuredText (RST) для модуля и каждой функции, включая описание параметров и возвращаемых значений.
2. Использовать `from src.logger.logger import logger` для логирования ошибок вместо `print`.
3. Избегать избыточного использования `try-except`, отдавая предпочтение `logger.error`.
4. Добавить проверку на валидность ввода года.
5. Переписать комментарии на английский язык, чтобы они соответствовали стандартам.
6. Использовать константы для дней недели и названий месяцев.
7. Вместо прямого `print` использовать форматированный вывод через f-строки с выравниванием.

**Оптимизированный код**

```python
"""
Модуль для отображения календаря на месяц.
==========================================

Этот модуль позволяет пользователю ввести месяц и год и отображает календарь
на этот месяц, включая дни недели.

Пример использования
--------------------

.. code-block:: python

    python calndr.py

"""
__author__ = 'hypo69 (hypo69@davidka.net)'

from src.logger.logger import logger
#from src.utils.jjson import j_loads, j_loads_ns # TODO: добавить импорт если нужен
"""
    Модуль реализует вывод календаря на месяц.
    Пользователь вводит месяц и год, а программа выводит календарь на экран.
    licence:MIT(../licence)
"""


def is_leap_year(year: int) -> bool:
    """
    Проверяет, является ли год високосным.

    :param year: Год для проверки.
    :return: True, если год високосный, False в противном случае.
    """
    # Код проверяет, является ли год високосным
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(month: int, year: int) -> int:
    """
    Определяет количество дней в месяце с учетом високосного года.

    :param month: Номер месяца (1-12).
    :param year: Год.
    :return: Количество дней в месяце.
    """
    # Код возвращает количество дней в указанном месяце
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 31


def day_of_week(day: int, month: int, year: int) -> int:
    """
    Вычисляет день недели для заданной даты, используя алгоритм Zeller's congruence.

    :param day: День месяца.
    :param month: Номер месяца.
    :param year: Год.
    :return: День недели (0 - воскресенье, 6 - суббота).
    """
    # Код вычисляет день недели для заданной даты
    if month < 3:
        month += 12
        year -= 1
    century = year // 100
    year_of_century = year % 100
    day_number = (day + ((13 * (month + 1)) // 5) + year_of_century + (year_of_century // 4) + (century // 4) - 2 * century) % 7
    # Код возвращает 0 для воскресенья
    return day_number


# Получение ввода от пользователя
try:
    # Код запрашивает у пользователя номер месяца
    month = int(input("Enter month number (1-12): "))
    # Код запрашивает у пользователя год
    year = int(input("Enter year: "))
except ValueError:
    # Код обрабатывает ошибку, если ввод не является целым числом
    logger.error("Invalid input. Please enter integer numbers.")
    exit()

# Проверка валидности ввода
if not 1 <= month <= 12:
    # Код обрабатывает ошибку, если введен некорректный номер месяца
    logger.error("Invalid month number. Please enter a number between 1 and 12.")
    exit()

# TODO: Добавить проверку на валидный ввод года
if not isinstance(year, int) or year <= 0:
    logger.error("Invalid year. Please enter a valid year.")
    exit()

# Расчет количества дней в месяце
days = days_in_month(month, year)

# Расчет дня недели, с которого начинается месяц
first_day = day_of_week(1, month, year)

# Вывод заголовка дней недели
print("Su Mo Tu We Th Fr Sa")

# Вывод пробелов до первого дня месяца
for i in range(first_day):
    print("   ", end="")

# Вывод чисел дней месяца
for day in range(1, days + 1):
    print(f"{day:2} ", end="")  # Код печатает день с выравниванием вправо
    if (day + first_day) % 7 == 0:
        print()  # Код переходит на новую строку каждые 7 дней

print()  # Код переходит на новую строку в конце
```