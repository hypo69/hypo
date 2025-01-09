# Анализ кода модуля `poker.py`

**Качество кода**
- Соответствие требованиям к формату кода (1-10): 8
    - Преимущества:
        - Код написан на Python и функционален.
        - Логика игры в покер реализована достаточно понятно.
        - Используются комментарии для объяснения кода.
        - Присутствует подробное описание игры, блок-схема и легенда в начале файла.
    - Недостатки:
        - Не используются `j_loads` или `j_loads_ns`.
        - Нет использования `reStructuredText (RST)` для комментариев и docstring.
        - Отсутствует обработка ошибок с использованием `logger.error`.
        - Не хватает импортов.
        - Нет использования констант для выигрышных комбинаций.
        - Некоторые функции не имеют docstring.
        - Слишком длинные комментарии.
        - Нет обработки исключений в функциях, кроме `get_cards_to_replace`

**Рекомендации по улучшению**

1.  **Форматирование документации**:
    *   Использовать `reStructuredText (RST)` для всех комментариев и docstring.
2.  **Использование `j_loads`**:
    *   В данном скрипте не происходит чтение файлов, поэтому применение `j_loads` не требуется.
3.  **Импорты**:
    *   Добавить `from src.logger.logger import logger` для логирования ошибок.
4.  **Обработка ошибок**:
    *   Использовать `logger.error` вместо стандартного `try-except` в функциях.
5.  **Документирование**:
    *   Добавить docstring в формате RST ко всем функциям.
6.  **Константы**:
    *   Использовать константы для значений очков за комбинации.
7.  **Улучшение структуры**:
    *   Разбить функцию `analyze_hand` на несколько более мелких функций для проверки каждой комбинации.
8.  **Удалить лишние комментарии**:
    *   Сократить длинные комментарии в конце кода, которые повторяют функционал функций.

**Улучшенный код**

```python
"""
Модуль для игры в покер.
=========================================================================================

Этот модуль реализует упрощенную версию карточного покера для одного игрока.
Игрок получает пять карт, может их заменить, после чего определяется выигрышная комбинация.

Пример использования
--------------------

.. code-block:: python

    from src.endpoints.ai_games.101_basic_computer_games.ru.GAMES.POKER import poker

    poker.play_poker()
"""
import random
from src.logger.logger import logger  # Добавлен импорт logger #
# Константы для выигрышных комбинаций #
FLUSH_POINTS = 20
FOUR_OF_A_KIND_POINTS = 25
FULL_HOUSE_POINTS = 15
THREE_OF_A_KIND_POINTS = 10
TWO_PAIRS_POINTS = 5
PAIR_POINTS = 2


def create_hand():
    """
    Создает руку из 5 случайных карт (числа от 1 до 13).

    :return: Список из 5 случайных карт.
    :rtype: list[int]
    """
    hand = [random.randint(1, 13) for _ in range(5)] #  Генерирует список из 5 случайных целых чисел в диапазоне от 1 до 13
    return hand


def display_hand(hand):
    """
    Выводит карты на экран, нумеруя их для удобства игрока.

    :param hand: Список карт.
    :type hand: list[int]
    """
    print("Ваши карты:")
    for i, card in enumerate(hand): # Цикл перебирает карты, нумеруя их
        print(f"{i+1}: {card}", end="  ") # Выводит номер карты и ее значение с пробелами для удобства
    print()


def get_cards_to_replace():
    """
    Запрашивает у игрока номера карт, которые нужно заменить.

    :return: Список индексов карт для замены.
    :rtype: list[int]
    """
    while True:
        try:
            replace_str = input("Введите номера карт для замены через пробел (или 0, чтобы оставить все): ")
            replace_cards = list(map(int, replace_str.split())) # Преобразует введенную строку в список целых чисел

            if len(replace_cards) == 1 and replace_cards[0] == 0:
                return []

            if all(1 <= card <= 5 for card in replace_cards) and len(replace_cards) <= 5: # Проверяет, что все введенные номера карт в диапазоне от 1 до 5
                return [card - 1 for card in replace_cards] # Возвращает список индексов карт для замены (индексы начинаются с 0)
            else:
                print("Неверный ввод. Введите номера карт от 1 до 5 или 0.")

        except ValueError:
            print("Неверный ввод. Пожалуйста, введите номера через пробел.")
        except Exception as ex:  # Добавлена обработка исключений
            logger.error('Ошибка ввода карт', exc_info=ex) # Записывает ошибку в лог
            return []


def replace_cards(hand, replace_indices):
    """
    Заменяет выбранные карты на новые случайные карты.

    :param hand: Список карт.
    :type hand: list[int]
    :param replace_indices: Список индексов карт для замены.
    :type replace_indices: list[int]
    :return: Обновленный список карт.
    :rtype: list[int]
    """
    try:
        for index in replace_indices: # Цикл перебирает индексы карт для замены
            hand[index] = random.randint(1, 13) # Заменяет карту в руке на случайное число
        return hand
    except Exception as ex: # Добавлена обработка исключений
        logger.error('Ошибка замены карт', exc_info=ex) # Записывает ошибку в лог
        return hand



def check_flush(hand):
    """
    Проверяет, является ли рука флешем (пять последовательных значений).

    :param hand: Список карт.
    :type hand: list[int]
    :return: True, если рука является флешем, False в противном случае.
    :rtype: bool
    """
    sorted_hand = sorted(hand)
    return len(set(sorted_hand)) == 5 and all(sorted_hand[i+1] - sorted_hand[i] == 1 for i in range(4))


def check_four_of_a_kind(counts):
     """
     Проверяет, есть ли в руке каре (четыре одинаковых значения).

     :param counts: Словарь с количеством повторений карт.
     :type counts: dict[int, int]
     :return: True, если есть каре, False в противном случае.
     :rtype: bool
     """
     values = list(counts.values())
     return 4 in values


def check_full_house(counts):
    """
    Проверяет, есть ли в руке фулл хаус (три одинаковых и пара).

    :param counts: Словарь с количеством повторений карт.
    :type counts: dict[int, int]
    :return: True, если есть фулл хаус, False в противном случае.
    :rtype: bool
    """
    values = list(counts.values())
    return 3 in values and 2 in values


def check_three_of_a_kind(counts):
    """
    Проверяет, есть ли в руке тройка (три одинаковых значения).

    :param counts: Словарь с количеством повторений карт.
    :type counts: dict[int, int]
    :return: True, если есть тройка, False в противном случае.
    :rtype: bool
    """
    values = list(counts.values())
    return 3 in values


def check_two_pairs(counts):
    """
    Проверяет, есть ли в руке две пары.

    :param counts: Словарь с количеством повторений карт.
    :type counts: dict[int, int]
    :return: True, если есть две пары, False в противном случае.
    :rtype: bool
    """
    values = list(counts.values())
    return values.count(2) == 2


def check_pair(counts):
    """
    Проверяет, есть ли в руке пара.

    :param counts: Словарь с количеством повторений карт.
    :type counts: dict[int, int]
    :return: True, если есть пара, False в противном случае.
    :rtype: bool
    """
    values = list(counts.values())
    return 2 in values


def analyze_hand(hand):
    """
    Анализирует руку и определяет выигрышную комбинацию.

    :param hand: Список карт.
    :type hand: list[int]
    """
    counts = {}  # Словарь для подсчета повторений карт
    for card in hand:
        counts[card] = counts.get(card, 0) + 1  # Подсчет количества каждой карты в руке
    try: # добавлена обработка исключений
        if check_flush(hand):
             print(f"Флеш! Выигрыш {FLUSH_POINTS} очков")
             return

        if check_four_of_a_kind(counts):
             print(f"Каре! Выигрыш {FOUR_OF_A_KIND_POINTS} очков")
             return

        if check_full_house(counts):
             print(f"Фулл Хаус! Выигрыш {FULL_HOUSE_POINTS} очков")
             return

        if check_three_of_a_kind(counts):
            print(f"Тройка! Выигрыш {THREE_OF_A_KIND_POINTS} очков")
            return

        if check_two_pairs(counts):
            print(f"Две пары! Выигрыш {TWO_PAIRS_POINTS} очков")
            return

        if check_pair(counts):
             print(f"Пара! Выигрыш {PAIR_POINTS} очка")
             return
    except Exception as ex: # Обрабатывает исключения
       logger.error('Ошибка при анализе комбинации', exc_info=ex) # Записывает ошибку в лог
       return


    print("Нет выигрыша.")



def play_poker():
    """Запускает игру в покер."""
    try: # добавлена обработка исключений
        hand = create_hand()  # Создаем руку из 5 карт
        display_hand(hand)  # Выводим карты на экран

        replace_indices = get_cards_to_replace()  # Запрашиваем карты для замены
        if replace_indices:
            hand = replace_cards(hand, replace_indices)  # Заменяем карты
            display_hand(hand)  # Выводим обновленные карты

        analyze_hand(hand)  # Анализируем руку на наличие комбинации и выводим результат
    except Exception as ex: # Обрабатывает исключения
       logger.error('Ошибка в процессе игры', exc_info=ex) # Записывает ошибку в лог


if __name__ == "__main__":
    play_poker()
```