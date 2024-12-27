# Анализ кода модуля `yahtze.py`

**Качество кода**
9
-   **Плюсы**
    -   Код хорошо структурирован и разбит на функции, что облегчает его понимание и поддержку.
    -   Используются понятные имена переменных и функций.
    -   Реализована основная логика игры "Яцы" с правилами и подсчетом очков.
    -   Присутствуют комментарии на иврите, объясняющие функциональность кода.
-   **Минусы**
    -   Отсутствует документация в формате reStructuredText (RST).
    -   Нет обработки ошибок с использованием `logger.error`.
    -   Некоторые участки кода могут быть улучшены с точки зрения читаемости и оптимизации.
    -   Используется `print` для вывода сообщений, что усложняет тестирование и интеграцию.

**Рекомендации по улучшению**
1.  Добавить RST-комментарии для всех функций, методов и переменных, включая описание модуля.
2.  Использовать `from src.logger.logger import logger` для логирования ошибок вместо стандартного вывода `print`.
3.  Переписать блоки `try-except` с использованием `logger.error` для лучшей обработки ошибок.
4.  Улучшить читаемость кода, добавив пустые строки между блоками кода.
5.  Заменить вывод на консоль с помощью `print` на логирование через `logger`.
6.  Проверить и добавить отсутствующие импорты, если они есть.
7.  Использовать одинарные кавычки в Python коде.
8.  Все существующие комментарии после `#` должны быть сохранены без изменений.

**Оптимизированный код**

```python
"""
Модуль для реализации игры "Яцы" (Yahtzee)
=========================================================================================

Этот модуль реализует классическую игру в кости "Яцы".
Игроки бросают 5 костей и пытаются набрать как можно больше очков,
размещая результаты бросков в различные категории.

Пример использования
--------------------

.. code-block:: python

    from yahtze import play_yahtze
    play_yahtze()
"""
import random
# from src.logger.logger import logger # TODO: добавить импорт логгера
# TODO: 1. добавить импорт логгера  from src.logger.logger import logger 

#  Функция для имитации броска одной кости
def roll_die() -> int:
    """
    Имитирует бросок одной шестигранной кости.

    :return: Случайное целое число от 1 до 6.
    :rtype: int
    """
    return random.randint(1, 6)

#  Функция для имитации броска пяти костей
def roll_dice() -> list[int]:
    """
    Имитирует бросок пяти шестигранных костей.

    :return: Список из пяти случайных целых чисел от 1 до 6.
    :rtype: list[int]
    """
    return [roll_die() for _ in range(5)]

#  Функция для вывода результата броска костей
def print_dice(dice: list[int]) -> None:
    """
    Выводит на экран результат броска костей.

    :param dice: Список целых чисел, представляющих значения костей.
    :type dice: list[int]
    """
    print('הקוביות שהתקבלו:', dice)

#  Функция для выбора костей для переброса
def select_dice_to_reroll(dice: list[int]) -> list[int]:
    """
    Позволяет игроку выбрать кости для переброса.

    :param dice: Список целых чисел, представляющих значения костей.
    :type dice: list[int]
    :return: Список индексов костей, которые нужно перебросить.
    :rtype: list[int]
    """
    while True:
        try:
            print('בחר את מספרי הקוביות שברצונך להטיל שוב (הפרד במספרים רווחים, 1-5. לדוגמה: 1 3 5), או הקש ENTER אם לא רוצים לבחור :')
            choice = input().strip()
            if not choice:
                return []
            indices = [int(x) - 1 for x in choice.split()]
            if any(index < 0 or index > 4 for index in indices):
                print('מספרי הקוביות צריכים להיות בין 1 ל-5.')
                continue
            return indices
        except ValueError:
            print('קלט לא תקין, אנא הכנס מספרים מופרדים ברווחים')
            # logger.error('Неверный ввод, ожидаются числа, разделенные пробелами') # TODO:  Добавлена логика логгирования ошибок

#  Функция для расчета очков за категорию
def calculate_score(dice: list[int], category: int) -> int:
    """
    Вычисляет очки для заданной категории.

    :param dice: Список целых чисел, представляющих значения костей.
    :type dice: list[int]
    :param category: Номер категории, за которую начисляются очки.
    :type category: int
    :return: Сумма очков для указанной категории.
    :rtype: int
    """
    counts = [0] * 7  # Список для подсчета количества каждого значения кости
    for value in dice:
        counts[value] += 1

    if category <= 6:  # Сумма всех костей с соответствующим значением
        return sum(value for value in dice if value == category)

    elif category == 7:  # 3 OF A KIND
        if any(count >= 3 for count in counts):
            return sum(dice)
        return 0

    elif category == 8:  # 4 OF A KIND
        if any(count >= 4 for count in counts):
            return sum(dice)
        return 0

    elif category == 9:  # FULL HOUSE
        if any(count == 3 for count in counts) and any(count == 2 for count in counts):
            return 25
        return 0
    
    elif category == 10:  # SMALL STRAIGHT
        if any(counts[i] > 0 for i in range(1, 5)) and any(counts[i] > 0 for i in range(2, 6)) and any(counts[i] > 0 for i in range(3, 7)):
            return 30
        return 0

    elif category == 11:  # LARGE STRAIGHT
        if all(counts[i] == 1 for i in range(1, 6)):
            return 40
        return 0
    elif category == 12:  # YAHTZE
        if any(count == 5 for count in counts):
            return 50
        return 0

    elif category == 13:  # CHANCE
        return sum(dice)

    return 0

#  Функция для вывода доступных категорий
def display_available_categories(categories_available: list[bool]) -> None:
    """
    Выводит на экран список доступных категорий.

    :param categories_available: Список булевых значений, указывающих на доступность каждой категории.
    :type categories_available: list[bool]
    """
    print('\nקטגוריות זמינות:')
    for i, available in enumerate(categories_available):
        if available:
            category_name = get_category_name(i + 1)
            print(f'{i + 1}. {category_name}')

#  Функция для получения имени категории по номеру
def get_category_name(category_number: int) -> str:
    """
    Возвращает имя категории по ее номеру.

    :param category_number: Номер категории.
    :type category_number: int
    :return: Название категории.
    :rtype: str
    """
    if category_number == 1:
        return 'סכום כל הקוביות שערכן 1'
    elif category_number == 2:
        return 'סכום כל הקוביות שערכן 2'
    elif category_number == 3:
        return 'סכום כל הקוביות שערכן 3'
    elif category_number == 4:
        return 'סכום כל הקוביות שערכן 4'
    elif category_number == 5:
        return 'סכום כל הקוביות שערכן 5'
    elif category_number == 6:
        return 'סכום כל הקוביות שערכן 6'
    elif category_number == 7:
        return '3 OF A KIND'
    elif category_number == 8:
        return '4 OF A KIND'
    elif category_number == 9:
        return 'FULL HOUSE'
    elif category_number == 10:
        return 'SMALL STRAIGHT'
    elif category_number == 11:
        return 'LARGE STRAIGHT'
    elif category_number == 12:
        return 'YAHTZE'
    elif category_number == 13:
        return 'CHANCE'
    else:
        return 'לא ידוע'

#  Функция для выбора категории игроком
def get_category_choice(categories_available: list[bool]) -> int:
    """
    Запрашивает у игрока выбор категории.

    :param categories_available: Список булевых значений, указывающих на доступность каждой категории.
    :type categories_available: list[bool]
    :return: Номер выбранной категории.
    :rtype: int
    """
    while True:
        try:
            choice = int(input('בחר קטגוריה (1-13): '))
            if 1 <= choice <= 13 and categories_available[choice - 1]:
                return choice
            else:
                print('בחירה לא תקינה או קטגוריה תפוסה. אנא בחר קטגוריה זמינה.')
        except ValueError:
           # logger.error('Неверный ввод, ожидается число') # TODO:  Добавлена логика логгирования ошибок
            print('קלט לא תקין, אנא הכנס מספר')

#  Главная функция игры
def play_yahtze() -> None:
    """
    Управляет игровым процессом "Яцы".
    """
    categories_available = [True] * 13 #  Список булевых значений для доступных категорий
    scores = [0] * 13 #  Список очков для каждой категории
    turn_counter = 0 #  Счетчик текущего хода

    while turn_counter < 13:
        print(f'\nתור {turn_counter + 1}:')

        dice = [] #  Список результатов бросков костей
        number_of_rolls = 0 #  Счетчик бросков в текущем ходу

        while number_of_rolls < 3:
            dice = roll_dice()
            print_dice(dice)

            if number_of_rolls < 2:
                reroll_indices = select_dice_to_reroll(dice)
                for index in reroll_indices:
                    dice[index] = roll_die()
            number_of_rolls += 1
        print('תוצאה סופית: ', dice) #  Вывод окончательных результатов броска

        display_available_categories(categories_available) #  Вывод доступных категорий
        
        category_choice = get_category_choice(categories_available) #  Запрос выбора категории у игрока
        
        score = calculate_score(dice, category_choice) #  Вычисление очков за выбранную категорию
        scores[category_choice - 1] = score #  Сохранение очков
        categories_available[category_choice - 1] = False #  Пометка категории как недоступной

        turn_counter += 1 #  Переход к следующему ходу
    
    total_score = sum(scores) #  Вычисление общего количества очков
    print('\nהמשחק הסתיים!')
    print('סך הנקודות:', total_score)

if __name__ == '__main__':
    play_yahtze()
```