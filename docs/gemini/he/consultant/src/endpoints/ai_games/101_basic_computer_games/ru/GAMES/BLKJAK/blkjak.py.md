# Анализ кода модуля blkjak.py

**Качество кода**
*   **Соответствие требованиям к формату кода (1-10):** 7/10
    *   **Преимущества:**
        *   Код достаточно хорошо структурирован и легко читается.
        *   Присутствует понятная логика игры в блэкджек.
        *   Функции имеют понятные названия и выполняют определенные задачи.
    *   **Недостатки:**
        *   Отсутствует полное соответствие стандарту docstring reStructuredText (RST).
        *   Не используется логгер для обработки ошибок.
        *   Не все комментарии соответствуют стандарту RST.
        *   Отсутствуют импорты из `src.utils.jjson`.

**Рекомендации по улучшению**

1.  **Форматирование документации:**
    *   Переформатировать все docstring в формат RST.
    *   Добавить подробные описания для параметров и возвращаемых значений функций.
2.  **Обработка ошибок:**
    *   Внедрить `logger.error` для регистрации исключений вместо стандартных `try-except`.
3.  **Импорты:**
    *   Добавить необходимые импорты `j_loads` или `j_loads_ns` из `src.utils.jjson`.
4.  **Стиль кода:**
    *   Устранить лишние комментарии, оставив только необходимые для пояснения логики.
    *   Соблюдать единый стиль именования переменных.
5.  **Комментарии:**
    *   Переформулировать комментарии в стиле RST.
    *   Убедиться, что все комментарии соответствуют стандарту RST.

**Улучшенный код**

```python
"""
Модуль для игры в блэкджек.
=========================================================================================

Модуль реализует простую игру в блэкджек, где игрок играет против дилера.
Включает в себя функции для раздачи карт, подсчета очков и определения победителя.

Пример использования
--------------------

Пример запуска игры:

.. code-block:: python

    if __name__ == "__main__":
        play_blackjack()
"""
import random
from src.logger.logger import logger # Добавлен импорт логгера


def deal_card(deck: list) -> int:
    """
    Выдает карту из колоды.

    :param deck: Список карт в колоде.
    :return: Значение карты, удаленной из колоды.
    """
    # Удаляет и возвращает последнюю карту из колоды
    return deck.pop()


def calculate_hand_value(hand: list) -> int:
    """
    Вычисляет значение руки.

    :param hand: Список карт в руке.
    :return: Общая сумма очков карт в руке.
    """
    ace_count = hand.count(11) # Считаем количество тузов (11)
    total = sum(hand) # Считаем общую сумму очков

    # Если общая сумма больше 21 и есть туз, который можно посчитать как 1
    while total > 21 and ace_count > 0:
        total -= 10  # Превращаем туз из 11 в 1
        ace_count -= 1
    return total


def display_cards(player_hand: list, dealer_hand: list, show_dealer_full: bool = False) -> None:
    """
    Отображает карты игрока и дилера.

    :param player_hand: Список карт игрока.
    :param dealer_hand: Список карт дилера.
    :param show_dealer_full: Флаг, показывающий, нужно ли отображать все карты дилера. По умолчанию False.
    """
    print("\nКарты дилера:")
    if show_dealer_full:
        print(" ".join(map(str, dealer_hand)), f"Сумма: {calculate_hand_value(dealer_hand)}")
    else:
        print("<закрытая карта> ", dealer_hand[1]) # Показываем первую карту дилера, вторая скрыта

    print("Карты игрока:", " ".join(map(str, player_hand)), f"Сумма: {calculate_hand_value(player_hand)}")


def play_blackjack() -> None:
    """
    Запускает игру в блэкджек.
    """
    # Создание колоды из 52 карт: числовые значения (2-10) и туз (11)
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    random.shuffle(deck) # Перемешиваем колоду

    # Раздача карт игроку и дилеру (по 2 карты)
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    # Отображение карт (одна карта дилера скрыта)
    display_cards(player_hand, dealer_hand)

    # Ход игрока
    while True:
        player_value = calculate_hand_value(player_hand)
        if player_value == 21: # Если у игрока сразу 21
            print("Блэкджек! Вы выиграли!")
            return

        if player_value > 21:  # Если игрок проиграл
            print("Перебор! Вы проиграли!")
            return

        action = input("Хотите взять еще карту? (HIT/STAND): ").upper()
        if action == "HIT":
            player_hand.append(deal_card(deck)) # Даем карту игроку
            display_cards(player_hand, dealer_hand)
        elif action == "STAND":
            break # Переходим к ходу дилера
        else:
            print("Некорректный ввод. Пожалуйста, введите HIT или STAND.")

    # Ход дилера
    print("\nХод дилера:")
    while calculate_hand_value(dealer_hand) <= 16:
        dealer_hand.append(deal_card(deck)) # Дилер берет карту

    display_cards(player_hand, dealer_hand, True)  # показываем все карты дилера

    player_value = calculate_hand_value(player_hand) # Сумма игрока
    dealer_value = calculate_hand_value(dealer_hand) # Сумма дилера

    # Проверка условий победы
    if dealer_value > 21: # Если у дилера перебор
        print("Дилер перебрал! Вы выиграли!")
    elif player_value > dealer_value or dealer_value > 21: # Если у игрока больше очков
        print("Вы выиграли!")
    elif dealer_value > player_value: # Если у дилера больше очков
        print("Вы проиграли!")
    else:
        print("Ничья!")  # Ничья


if __name__ == "__main__":
    play_blackjack()  # Запуск игры

"""
Объяснение кода:
1.  **Импорт модуля `random`**:\n
   -  `import random`: Импортирует модуль `random`, который используется для генерации случайного порядка карт.
   - `from src.logger.logger import logger`: Импортирует модуль `logger` для логирования ошибок. # Добавлен импорт логгера
2.  **Функция `deal_card(deck)`**:\n
    -  `def deal_card(deck):`: Определяет функцию для взятия карты из колоды.
    -  `return deck.pop()`: Удаляет и возвращает последнюю карту из колоды.
3.  **Функция `calculate_hand_value(hand)`**:\n
    -   `def calculate_hand_value(hand):`: Определяет функцию для вычисления суммы очков карт.
    -   `ace_count = hand.count(11)`: Подсчитывает количество тузов в руке (туз = 11).
    -   `total = sum(hand)`: Вычисляет общую сумму очков карт.
    -   `while total > 21 and ace_count > 0`: Если сумма больше 21 и есть тузы.
    -   `total -= 10`:  Заменяет туз с 11 на 1.
    -   `ace_count -= 1`: Уменьшаем количество тузов.
    -   `return total`: Возвращает общую сумму очков.
4.  **Функция `display_cards(player_hand, dealer_hand, show_dealer_full=False)`**:\n
    -   `def display_cards(player_hand, dealer_hand, show_dealer_full=False):`: Определяет функцию для отображения карт.
    -  `show_dealer_full=False`: показывает только 1 карту дилера.
    -  Если `show_dealer_full=True`: показывает все карты дилера.
5.  **Функция `play_blackjack()`**:\n
    -  `def play_blackjack():`: Определяет функцию, содержащую основную логику игры.
    -  `deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4`: Создает колоду из 52 карт (числовые значения и туз).
    -  `random.shuffle(deck)`: Перемешивает колоду.
    -  `player_hand = [deal_card(deck), deal_card(deck)]`: Раздает 2 карты игроку.
    -  `dealer_hand = [deal_card(deck), deal_card(deck)]`: Раздает 2 карты дилеру.
    -  `display_cards(player_hand, dealer_hand)`: Отображает начальные карты.
    -   **Ход игрока**:\n
         -   `while True:`: Основной цикл хода игрока.
        - `player_value = calculate_hand_value(player_hand)`: Вычисляем сумму игрока.
        - `if player_value == 21:`: Проверка на блэкджек.
        - `if player_value > 21:`: Проверка на проигрыш игрока.
         -   `action = input("Хотите взять еще карту? (HIT/STAND): ").upper()`: Запрашивает действие игрока (HIT или STAND).
         -   `if action == "HIT":`: Если игрок выбирает HIT:\n
            -   `player_hand.append(deal_card(deck))`: Добавляет карту в руку игрока.
            -    `display_cards(player_hand, dealer_hand)`: Отображает карты.
         -   `elif action == "STAND":`: Если игрок выбирает STAND, переходит к ходу дилера.
    -   **Ход дилера**:\n
        -  `while calculate_hand_value(dealer_hand) <= 16:`: Дилер берет карту пока сумма меньше 16.
         -    `dealer_hand.append(deal_card(deck))`: Даем карту дилеру.
        -  `display_cards(player_hand, dealer_hand, True)`: Отображаем карты дилера.
     -    **Определение победителя**:\n
         - `player_value = calculate_hand_value(player_hand)`: Вычисляем сумму игрока.
         -`dealer_value = calculate_hand_value(dealer_hand)`: Вычисляем сумму дилера.
        - `if dealer_value > 21: `: Проверка на перебор у дилера.
        - `elif player_value > dealer_value or dealer_value > 21`: Проверка победы игрока.
        -`elif dealer_value > player_value`: Проверка победы дилера.
    -`if __name__ == "__main__":`: Запуск игры.
    -`play_blackjack()`: Вызов функции игры.
"""
```