# Анализ кода модуля blkjak.py

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разбит на логические функции.
    - Присутствует подробное описание игры и алгоритм в начале файла.
    - Имеется блок-схема, что помогает визуализировать логику игры.
    - Функции имеют docstring, что облегчает понимание их назначения.
    - Код использует `random.shuffle` для перемешивания колоды.
- Минусы
    - Отсутствует обработка ошибок.
    - Не используются `j_loads` или `j_loads_ns`.
    - Не используются логи.
    - Код не полностью соответствует стандарту PEP 8.
    - Некоторые комментарии после `#` не соответствуют стандарту RST.
    - Не все функции имеют подробные docstring.

**Рекомендации по улучшению**

1.  **Импорты:**
    - Добавить `from src.logger.logger import logger` для логирования ошибок.
2.  **Обработка ошибок:**
    - Заменить стандартные блоки `try-except` на логирование ошибок с помощью `logger.error`.
3.  **Использование `j_loads` или `j_loads_ns`:**
    - В данном коде нет работы с json, поэтому это требование не применимо.
4.  **Комментарии и документация:**
    - Все комментарии после `#` переписать в формате reStructuredText (RST).
    - Добавить более подробные docstring к функциям.
    - Изменить комментарии, где используется слово "получаем" и т.д. на более конкретные формулировки.
5.  **Стиль кода:**
    - Привести код в соответствие со стандартами PEP 8.
    - Использовать константы вместо магических чисел.

**Оптимизированный код**

```python
"""
Модуль для игры в блэкджек.
=========================================================================================

Этот модуль реализует игру в блэкджек, где игрок соревнуется с дилером.
Цель игры - набрать 21 очко или как можно ближе к 21, не превышая этого значения.

Правила игры:
1.  Игрок и дилер получают по две карты. Одна из карт дилера открыта.
2.  Игрок может взять ещё карту (HIT) или остановиться (STAND).
3.  Если сумма карт игрока больше 21, он проигрывает.
4.  Дилер берет карты до тех пор, пока его сумма не станет больше 16.
5.  Если сумма карт дилера больше 21, он проигрывает.
6.  Побеждает тот, у кого сумма ближе к 21, но не больше 21.
7.  При равенстве очков объявляется ничья (PUSH).

Алгоритм:
1. Инициализация колоды: Создание колоды из 52 карт.
2. Перемешивание колоды.
3. Раздача по две карты игроку и дилеру.
4. Отображение карт игрока и открытой карты дилера.
5. Ход игрока: Запрос действия HIT или STAND.
6. Ход дилера: Дилер берет карты, пока его сумма не станет больше 16.
7. Определение победителя: Сравнение сумм карт игрока и дилера.
"""
import random
from src.logger.logger import logger

CARD_VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
"""Список числовых значений карт (2-10, валет, дама, король и туз)"""
DECK_MULTIPLIER = 4
"""Множитель для создания полной колоды (4 масти)"""
DEALER_STAND_VALUE = 16
"""Значение, при котором дилер прекращает брать карты"""

def deal_card(deck: list) -> int:
    """
    Извлекает и возвращает последнюю карту из колоды.

    :param deck: Колода карт.
    :return: Значение карты.
    """
    return deck.pop()

def calculate_hand_value(hand: list) -> int:
    """
    Вычисляет сумму очков карт в руке, учитывая тузы (1 или 11).

    :param hand: Список карт в руке.
    :return: Общая сумма очков карт.
    """
    ace_count = hand.count(11)
    total = sum(hand)

    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    return total

def display_cards(player_hand: list, dealer_hand: list, show_dealer_full: bool = False) -> None:
    """
    Отображает карты игрока и дилера.

    :param player_hand: Карты игрока.
    :param dealer_hand: Карты дилера.
    :param show_dealer_full: Флаг для отображения всех карт дилера.
    """
    print('\nКарты дилера:')
    if show_dealer_full:
        print(" ".join(map(str, dealer_hand)), f"Сумма: {calculate_hand_value(dealer_hand)}")
    else:
        print("<закрытая карта> ", dealer_hand[1])
    print("Карты игрока:", " ".join(map(str, player_hand)), f"Сумма: {calculate_hand_value(player_hand)}")

def play_blackjack():
    """
    Запускает игру в блэкджек.
    
    Эта функция выполняет основные шаги игры, включая раздачу карт, ходы игрока и дилера,
    а также определение победителя.
    """
    # Создание колоды из 52 карт
    deck = CARD_VALUES * DECK_MULTIPLIER
    random.shuffle(deck)

    # Раздача начальных карт
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    # Отображение начальных карт
    display_cards(player_hand, dealer_hand)

    # Ход игрока
    while True:
        player_value = calculate_hand_value(player_hand)
        if player_value == 21:
            print("Блэкджек! Вы выиграли!")
            return
        if player_value > 21:
            print("Перебор! Вы проиграли!")
            return

        action = input("Хотите взять еще карту? (HIT/STAND): ").upper()
        if action == "HIT":
            player_hand.append(deal_card(deck))
            display_cards(player_hand, dealer_hand)
        elif action == "STAND":
            break
        else:
            print("Некорректный ввод. Пожалуйста, введите HIT или STAND.")

    # Ход дилера
    print("\nХод дилера:")
    while calculate_hand_value(dealer_hand) <= DEALER_STAND_VALUE:
        dealer_hand.append(deal_card(deck))

    display_cards(player_hand, dealer_hand, True)

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    # Определение победителя
    if dealer_value > 21:
        print("Дилер перебрал! Вы выиграли!")
    elif player_value > dealer_value or dealer_value > 21:
        print("Вы выиграли!")
    elif dealer_value > player_value:
        print("Вы проиграли!")
    else:
        print("Ничья!")

if __name__ == "__main__":
    play_blackjack()
    
"""
Объяснение кода:
1.  **Импорт модуля `random`**::
    - `import random`: Импортирует модуль `random`, который используется для генерации случайного порядка карт.
2.  **Импорт модуля `logger`**::
    - `from src.logger.logger import logger`: Импортирует модуль `logger`, для логирования ошибок.
3.  **Константы**::
    - `CARD_VALUES`: Список числовых значений карт (2-10, валет, дама, король и туз).
    - `DECK_MULTIPLIER`: Множитель для создания полной колоды (4 масти).
    - `DEALER_STAND_VALUE`: Значение, при котором дилер прекращает брать карты.
4.  **Функция `deal_card(deck)`**::
    - `def deal_card(deck):`: Определяет функцию для взятия карты из колоды.
    - `return deck.pop()`: Удаляет и возвращает последнюю карту из колоды.
5.  **Функция `calculate_hand_value(hand)`**::
    - `def calculate_hand_value(hand):`: Определяет функцию для вычисления суммы очков карт.
    - `ace_count = hand.count(11)`: Подсчитывает количество тузов в руке (туз = 11).
    - `total = sum(hand)`: Вычисляет общую сумму очков карт.
    - `while total > 21 and ace_count > 0`: Если сумма больше 21 и есть тузы.
    - `total -= 10`: Заменяет туз с 11 на 1.
    - `ace_count -= 1`: Уменьшаем количество тузов.
    - `return total`: Возвращает общую сумму очков.
6.  **Функция `display_cards(player_hand, dealer_hand, show_dealer_full=False)`**::
    - `def display_cards(player_hand, dealer_hand, show_dealer_full=False):`: Определяет функцию для отображения карт.
    - `show_dealer_full=False`: показывает только 1 карту дилера.
    - Если `show_dealer_full=True`: показывает все карты дилера.
7.  **Функция `play_blackjack()`**::
    - `def play_blackjack():`: Определяет функцию, содержащую основную логику игры.
    - `deck = CARD_VALUES * DECK_MULTIPLIER`: Создает колоду из 52 карт (числовые значения и туз).
    - `random.shuffle(deck)`: Перемешивает колоду.
    - `player_hand = [deal_card(deck), deal_card(deck)]`: Раздает 2 карты игроку.
    - `dealer_hand = [deal_card(deck), deal_card(deck)]`: Раздает 2 карты дилеру.
    - `display_cards(player_hand, dealer_hand)`: Отображает начальные карты.
    -   **Ход игрока**:
        - `while True:`: Основной цикл хода игрока.
        - `player_value = calculate_hand_value(player_hand)`: Вычисляем сумму игрока.
        - `if player_value == 21:`: Проверка на блэкджек.
        - `if player_value > 21:`: Проверка на проигрыш игрока.
        - `action = input("Хотите взять еще карту? (HIT/STAND): ").upper()`: Запрашивает действие игрока (HIT или STAND).
        - `if action == "HIT":`: Если игрок выбирает HIT:
            - `player_hand.append(deal_card(deck))`: Добавляет карту в руку игрока.
            - `display_cards(player_hand, dealer_hand)`: Отображает карты.
        - `elif action == "STAND":`: Если игрок выбирает STAND, переходит к ходу дилера.
    -   **Ход дилера**:
        - `while calculate_hand_value(dealer_hand) <= DEALER_STAND_VALUE:`: Дилер берет карту пока сумма меньше 16.
        - `dealer_hand.append(deal_card(deck))`: Даем карту дилеру.
        - `display_cards(player_hand, dealer_hand, True)`: Отображаем карты дилера.
     -    **Определение победителя**:
         - `player_value = calculate_hand_value(player_hand)`: Вычисляем сумму игрока.
         -`dealer_value = calculate_hand_value(dealer_hand)`: Вычисляем сумму дилера.
        - `if dealer_value > 21: `: Проверка на перебор у дилера.
        - `elif player_value > dealer_value or dealer_value > 21`: Проверка победы игрока.
        -`elif dealer_value > player_value`: Проверка победы дилера.
    -`if __name__ == "__main__":`: Запуск игры.
    -`play_blackjack()`: Вызов функции игры.
"""
```