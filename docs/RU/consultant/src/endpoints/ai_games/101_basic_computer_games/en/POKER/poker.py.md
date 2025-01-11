# Анализ кода модуля poker.py

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разбит на функции, что делает его читаемым и понятным.
    - Присутствуют docstring для функций, которые описывают их назначение.
    - Логика игры реализована в соответствии с описанием.
    - Используется обработка исключений для ввода пользователя, что делает программу более устойчивой к ошибкам.
- Минусы
    - Отсутствуют необходимые импорты.
    - Не используется `j_loads` или `j_loads_ns`.
    - Не используется логирование ошибок через `logger.error`.
    - Комментарии не приведены к формату reStructuredText (RST).
    - Код можно улучшить, добавив константы для выигрышных очков.
    - Нет обработки ситуаций, когда ввод пользователя содержит некорректные символы, кроме ValueError.

**Рекомендации по улучшению**

1.  **Импорт необходимых модулей:**
    - Добавить `from src.logger.logger import logger` для логирования.
    - Добавить `from typing import List` для аннотации типов.
2.  **Использование `j_loads` или `j_loads_ns`**:
    - В данном коде нет чтения файлов, поэтому это не требуется.
3.  **Логирование ошибок:**
    - Заменить `print` для вывода ошибок на `logger.error`.
    - Добавить логирование в `try-except` блоки.
4.  **Формат документации:**
    - Переписать все комментарии в формате reStructuredText (RST).
5.  **Константы:**
    - Вынести выигрышные очки в константы для удобства модификации.
6.  **Улучшение обработки ввода пользователя:**
    - Добавить проверку на некорректные символы в вводе пользователя.

**Оптимизированный код**
```python
"""
Модуль для игры в покер.
=========================================================================================

Этот модуль реализует упрощенную версию карточного покера для одного игрока.

Правила игры:
    1. Игрок получает пять случайных карт.
    2. Игрок может заменить любое количество карт один раз.
    3. После замены определяется комбинация карт и выводится выигрыш.

Комбинации:
    - Пара
    - Две пары
    - Тройка
    - Фулл хаус
    - Каре
    - Стрит
    - Флеш

Пример использования
--------------------

.. code-block:: python

    if __name__ == "__main__":
        play_poker()
"""
import random
from typing import List
from src.logger.logger import logger # Импорт логгера

# Константы для выигрышей
FLUSH_WIN = 20
FOUR_OF_A_KIND_WIN = 25
FULL_HOUSE_WIN = 15
THREE_OF_A_KIND_WIN = 10
TWO_PAIRS_WIN = 5
PAIR_WIN = 2


def create_hand() -> List[int]:
    """
    Создает руку из 5 случайных карт (числа от 1 до 13).

    :return: Список целых чисел, представляющих карты в руке.
    :rtype: List[int]
    """
    # Код исполняет генерацию списка из 5 случайных целых чисел от 1 до 13.
    hand = [random.randint(1, 13) for _ in range(5)]
    return hand


def display_hand(hand: List[int]) -> None:
    """
    Выводит карты на экран, нумеруя их для удобства игрока.

    :param hand: Список карт в руке.
    :type hand: List[int]
    """
    # Код исполняет вывод карт на экран с их номерами.
    print("Ваши карты:")
    for i, card in enumerate(hand):
        print(f"{i+1}: {card}", end="  ")
    print()


def get_cards_to_replace() -> List[int]:
    """
    Запрашивает у игрока номера карт, которые нужно заменить.

    :return: Список индексов карт для замены.
    :rtype: List[int]
    """
    # Код исполняет запрос ввода пользователя и обработку ошибок.
    while True:
        try:
            replace_str = input("Введите номера карт для замены через пробел (или 0, чтобы оставить все): ")
            replace_cards = list(map(int, replace_str.split()))

            if len(replace_cards) == 1 and replace_cards[0] == 0:
                return []

            if all(1 <= card <= 5 for card in replace_cards) and len(replace_cards) <= 5:
                return [card - 1 for card in replace_cards]
            else:
                logger.error("Неверный ввод. Введите номера карт от 1 до 5 или 0.")
                print("Неверный ввод. Введите номера карт от 1 до 5 или 0.")
        except ValueError:
             logger.error("Неверный ввод. Пожалуйста, введите номера через пробел.")
             print("Неверный ввод. Пожалуйста, введите номера через пробел.")


def replace_cards(hand: List[int], replace_indices: List[int]) -> List[int]:
    """
    Заменяет выбранные карты на новые случайные карты.

    :param hand: Список карт в руке.
    :type hand: List[int]
    :param replace_indices: Список индексов карт для замены.
    :type replace_indices: List[int]
    :return: Обновленный список карт в руке.
    :rtype: List[int]
    """
    # Код исполняет замену карт на новые случайные.
    for index in replace_indices:
        hand[index] = random.randint(1, 13)
    return hand


def analyze_hand(hand: List[int]) -> None:
    """
    Анализирует руку и определяет выигрышную комбинацию.

    :param hand: Список карт в руке.
    :type hand: List[int]
    """
    # Код исполняет анализ комбинаций карт.
    counts = {}  # Словарь для подсчета повторений карт
    for card in hand:
        counts[card] = counts.get(card, 0) + 1

    values = list(counts.values())  # Список количества повторений

    # Проверка на Флеш
    sorted_hand = sorted(hand)
    if len(set(sorted_hand)) == 5 and all(sorted_hand[i+1] - sorted_hand[i] == 1 for i in range(4)):
        print(f"Флеш! Выигрыш {FLUSH_WIN} очков")
        return

    # Проверка на Каре
    if 4 in values:
        print(f"Каре! Выигрыш {FOUR_OF_A_KIND_WIN} очков")
        return

    # Проверка на Фулл Хаус
    if 3 in values and 2 in values:
      print(f"Фулл Хаус! Выигрыш {FULL_HOUSE_WIN} очков")
      return

    # Проверка на Тройку
    if 3 in values:
        print(f"Тройка! Выигрыш {THREE_OF_A_KIND_WIN} очков")
        return

    # Проверка на Две пары
    if values.count(2) == 2:
        print(f"Две пары! Выигрыш {TWO_PAIRS_WIN} очков")
        return

    # Проверка на Пару
    if 2 in values:
        print(f"Пара! Выигрыш {PAIR_WIN} очка")
        return

    print("Нет выигрыша.")


def play_poker() -> None:
    """
    Запускает игру в покер.
    """
    # Код исполняет основную логику игры.
    hand = create_hand()  # Создаем руку из 5 карт
    display_hand(hand)  # Выводим карты на экран

    replace_indices = get_cards_to_replace()  # Запрашиваем карты для замены
    if replace_indices:
        hand = replace_cards(hand, replace_indices)  # Заменяем карты
        display_hand(hand)  # Выводим обновленные карты

    analyze_hand(hand)  # Анализируем руку на наличие комбинации и выводим результат


if __name__ == "__main__":
    play_poker()