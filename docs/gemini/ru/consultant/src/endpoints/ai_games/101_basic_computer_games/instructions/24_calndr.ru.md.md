# Анализ кода модуля `24_calndr.ru.md`

**Качество кода**
9
-  Плюсы
    - Документ содержит подробное описание игры, включая шаги реализации, примеры работы и возможные ограничения.
    - Структура документа четкая и понятная, что облегчает восприятие информации.
    - Приведены примеры взаимодействия пользователя с программой, что помогает понять, как она работает.

-  Минусы
    - Документ не является исполняемым кодом, а представляет собой инструкцию в формате Markdown.
    - Отсутствует код программы, который можно было бы проанализировать на предмет качества.
    - Нет возможности проверить соответствие документации и реального кода.

**Рекомендации по улучшению**
1.  Преобразовать инструкцию в исполняемый код Python с комментариями в формате RST.
2.  Добавить обработку ошибок при вводе данных пользователем.
3.  Реализовать автоматическое определение високосного года.
4.  Добавить логирование ошибок и важной информации.
5.  Разделить код на логические функции для лучшей читаемости и поддержки.
6.  Использовать `src.utils.jjson` для чтения внешних файлов, если это необходимо.
7.  Улучшить вывод календаря, чтобы он выглядел более аккуратно.
8.  Добавить проверку на корректность ввода дня недели.

**Оптимизированный код**
```markdown
# Анализ кода модуля `24_calndr.ru.md`

**Качество кода**
9
-  Плюсы
    - Документ содержит подробное описание игры, включая шаги реализации, примеры работы и возможные ограничения.
    - Структура документа четкая и понятная, что облегчает восприятие информации.
    - Приведены примеры взаимодействия пользователя с программой, что помогает понять, как она работает.

-  Минусы
    - Документ не является исполняемым кодом, а представляет собой инструкцию в формате Markdown.
    - Отсутствует код программы, который можно было бы проанализировать на предмет качества.
    - Нет возможности проверить соответствие документации и реального кода.

**Рекомендации по улучшению**
1.  Преобразовать инструкцию в исполняемый код Python с комментариями в формате RST.
2.  Добавить обработку ошибок при вводе данных пользователем.
3.  Реализовать автоматическое определение високосного года.
4.  Добавить логирование ошибок и важной информации.
5.  Разделить код на логические функции для лучшей читаемости и поддержки.
6.  Использовать `src.utils.jjson` для чтения внешних файлов, если это необходимо.
7.  Улучшить вывод календаря, чтобы он выглядел более аккуратно.
8.  Добавить проверку на корректность ввода дня недели.

**Оптимизированный код**
```python
"""
Модуль для вывода календаря на заданный год.
=========================================================================================

Этот модуль позволяет пользователю вывести календарь для любого года,
указав год и день недели, с которого он начинается.

Пример использования
--------------------

Пример запуска программы:

.. code-block:: python

    python calndr.py
"""
from src.logger.logger import logger
from datetime import date
def is_leap_year(year: int) -> bool:
    """
    Проверяет, является ли год високосным.

    :param year: Год для проверки.
    :return: True, если год високосный, иначе False.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def get_days_in_month(year: int, month: int) -> int:
    """
    Определяет количество дней в месяце.

    :param year: Год.
    :param month: Месяц (1-12).
    :return: Количество дней в месяце.
    """
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 31

def print_calendar(year: int, start_day: int):
    """
    Выводит календарь для заданного года.

    :param year: Год.
    :param start_day: День недели, с которого начинается год (0 - воскресенье, -1 - понедельник, ...).
    """
    try:
        # Проверка корректности начального дня недели
        if not -6 <= start_day <= 0:
             logger.error(f'Некорректный ввод дня недели: {start_day}. Допустимые значения от -6 до 0.')
             return
        month_names = [
            'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
            'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
        ]
        for month in range(1, 13):
            print(f'\n{month_names[month - 1]} {year}')
            print('Пн Вт Ср Чт Пт Сб Вс')

            days_in_month = get_days_in_month(year, month)
            day_of_week = (start_day + (date(year, month, 1).weekday() + 6) % 7 )%7
            for _ in range(day_of_week):
                 print('   ', end=' ')

            for day in range(1, days_in_month + 1):
                print(f'{day:2}', end=' ')
                day_of_week += 1
                if day_of_week % 7 == 0:
                    print()

            start_day = (start_day + days_in_month) % 7
    except Exception as ex:
        logger.error(f'Ошибка при выводе календаря: {ex}')


def main():
    """
     Основная функция для запуска программы.
    """
    print('Добро пожаловать в программу CALNDR!')
    while True:
        try:
            year = int(input('Введите год: '))
            start_day = int(input('Введите день недели, с которого начинается год (0 - воскресенье, -1 - понедельник и т.д.): '))
            print_calendar(year,start_day)
            
            continue_game = input('Хотите вывести календарь для другого года? (да/нет): ').lower()
            if continue_game != 'да':
                print('Спасибо за использование программы!')
                break
        except ValueError:
            logger.error('Некорректный ввод, введите целое число.')
        except Exception as ex:
            logger.error(f'Произошла непредвиденная ошибка: {ex}')

if __name__ == '__main__':
    main()
```