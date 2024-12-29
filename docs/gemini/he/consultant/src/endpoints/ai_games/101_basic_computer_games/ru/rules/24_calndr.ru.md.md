# Анализ кода модуля CALNDR

**Качество кода**
    
-  Соответствие требованиям к формату кода с 1 по 10:
    -   Преимущества
        -  Описание игры и пошаговая инструкция хорошо структурированы с использованием Markdown.
        -  Приведены примеры работы программы, включая ввод и вывод данных.
        -  Описаны ограничения и возможные проблемы в использовании программы.
    -   Недостатки
        - Отсутствует код на Python.
        -  Не используется reStructuredText для комментариев и docstring.
        -  Нет обработки ошибок.
        -  Нет конкретной реализации с использованием `j_loads` или `j_loads_ns`.
        -  Нет  использования `logger.error`.

**Рекомендации по улучшению**
1.  Добавить реализацию кода на Python.
2.  Использовать reStructuredText для комментариев и docstring.
3.  Применить  `j_loads` или `j_loads_ns` для чтения файлов.
4.  Добавить обработку ошибок с использованием `logger.error`.
5.  Преобразовать Markdown-разметку в reStructuredText, где это уместно.
6.  Добавить недостающие импорты.
7.  Добавить функцию расчета дня недели.
8.  Добавить функцию для определения високосного года.
9.  Добавить функцию для вывода календаря.
10.  Добавить цикл для запроса у пользователя продолжения игры.

**Улучшенный код**

```python
"""
Модуль для вывода календаря на заданный год.
=========================================================================================

Этот модуль позволяет пользователю вывести календарь для любого года,
указав день недели, с которого начинается год.

Пример использования:
--------------------
.. code-block:: python

    calendar = Calendar()
    calendar.run()
"""

from src.utils.jjson import j_loads  # импорт j_loads из utils.jjson #
from src.logger.logger import logger # импорт logger из src.logger.logger #

def is_leap_year(year: int) -> bool:
    """
    Проверяет, является ли год високосным.

    :param year: Год для проверки.
    :return: True, если год високосный, иначе False.
    """
    # Код проверяет, является ли год високосным. #
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_days_in_month(month: int, year: int) -> int:
    """
    Возвращает количество дней в заданном месяце года.

    :param month: Номер месяца (1-12).
    :param year: Год.
    :return: Количество дней в месяце.
    """
    # Код определяет количество дней в месяце с учетом високосного года для февраля. #
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        return 29 if is_leap_year(year) else 28
    return 31


def get_start_day(year: int) -> int:
    """
    Вычисляет день недели, с которого начинается год (0 - воскресенье, -1 - понедельник и т.д.).

    :param year: Год.
    :return: День недели, с которого начинается год.
    """
    # Код вычисляет день недели, с которого начинается год #
    # Алгоритм Сакея для вычисления дня недели первого января
    d = (year + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400) % 7
    return -d if d != 0 else 0

class Calendar:
    """
    Класс для вывода календаря.

    :ivar months: Список названий месяцев.
    """
    months = [
        'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
        'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
    ]

    def __init__(self):
        """Инициализация класса Calendar."""
        # Инициализирует класс Calendar #
        pass

    def print_month(self, year: int, month: int, start_day: int):
        """
        Выводит календарь для заданного месяца.

        :param year: Год.
        :param month: Номер месяца (1-12).
        :param start_day: День недели, с которого начинается месяц (0 - воскресенье, -1 - понедельник и т.д.).
        """
        # Код выводит календарь для заданного месяца. #
        days_in_month = get_days_in_month(month, year)
        print(f'{self.months[month - 1]} {year}')
        print('Пн Вт Ср Чт Пт Сб Вс')

        day_of_week = start_day
        for _ in range(abs(start_day)):
            print('   ', end='')
            day_of_week += 1

        for day in range(1, days_in_month + 1):
            print(f'{day:2} ', end='')
            day_of_week += 1
            if day_of_week % 7 == 0:
                print()
        print('\n')

    def run(self):
        """Запускает игру."""
        # Код запускает игру и обрабатывает ввод пользователя #
        print('Добро пожаловать в программу CALNDR!')
        while True:
            try:
                year = int(input('Введите год: '))
                start_day = get_start_day(year)
                print(f'День начала года: {start_day}')
                for month in range(1, 13):
                    self.print_month(year, month, start_day)
                    start_day = (start_day + get_days_in_month(month, year)) % 7
                    if start_day == 0:
                         start_day = 0
                    else:
                         start_day = -start_day
                
                continue_game = input('Хотите вывести календарь для другого года? (да/нет) ')
                if continue_game.lower() != 'да':
                    print('Спасибо за использование программы!')
                    break

            except ValueError as e:
                logger.error(f'Ошибка ввода: {e}')
                print('Некорректный ввод. Пожалуйста, введите число.')


if __name__ == '__main__':
    # Код создает экземпляр класса Calendar и запускает игру #
    calendar = Calendar()
    calendar.run()
```