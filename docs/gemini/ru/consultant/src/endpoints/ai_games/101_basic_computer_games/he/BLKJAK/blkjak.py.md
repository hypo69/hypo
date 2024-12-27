# Анализ кода модуля `blkjak.py`

**Качество кода**
8/10
-  Плюсы
    - Код хорошо структурирован и логически разделен на функции, что улучшает читаемость и поддерживаемость.
    -  Используются информативные имена переменных и функций, что облегчает понимание кода.
    -   Присутствуют комментарии, объясняющие логику работы кода.
    -   Код следует основным принципам игры "Блэкджек".
-  Минусы
    -  Комментарии не соответствуют стандарту reStructuredText (RST).
    -   Отсутствует обработка ошибок и логирование.
    -  Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`, хотя в данном коде нет работы с JSON.
    -  Нет документации в формате docstring для функций и модуля.
    -  Не все переменные и функции имеют поясняющие комментарии.
    -  Используется избыточное количество комментариев в конце файла, которые можно было бы включить в docstring модуля.

**Рекомендации по улучшению**

1. **Документация**:
    -   Переписать все комментарии в формате RST, включая docstring для модуля, функций и методов.
    -   Включить в docstring подробное описание параметров и возвращаемых значений функций.
2.  **Логирование**:
    -   Использовать `from src.logger.logger import logger` для логирования ошибок.
    -   Заменить стандартные `try-except` блоки на логирование с `logger.error` для отслеживания проблем.
3.  **Импорты**:
    -   Добавить отсутствующие импорты, если они необходимы.
4. **Обработка данных**:
   - Убедиться, что используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для работы с файлами, если это необходимо.
5.  **Рефакторинг**:
    -   Избегать избыточных комментариев, перенеся их в docstring, где это уместно.
    -   Улучшить читаемость кода, переименовав переменные, если это необходимо, для большей ясности.
6. **Форматирование**:
    -  Привести код к единому стандарту форматирования (например, PEP 8).

**Оптимизиробанный код**

```python
"""
Модуль для игры в Блэкджек
=========================================================================================

Этот модуль реализует игру в Блэкджек против дилера.

Правила игры:
1. Цель игры - набрать сумму очков карт как можно ближе к 21, но не превышая это значение.
2. Числовые карты имеют значение, равное их номиналу.
3. Карты-картинки (валет, дама, король) имеют значение 10.
4. Туз может иметь значение 1 или 11, в зависимости от того, что лучше для руки игрока.
5. Игрок начинает с двумя картами, и дилер также получает две карты, одна из которых скрыта.
6. Игрок может брать дополнительные карты (hit) или остаться с текущими картами (stand).
7. После того как игрок заканчивает, дилер открывает свою скрытую карту и берет карты, пока его сумма очков не достигнет 17 или более.
8. Выигрывает рука с наибольшей суммой очков, не превышающей 21. Если сумма очков превышает 21, игрок проигрывает.

Пример использования
--------------------

Пример запуска игры:

.. code-block:: python

    if __name__ == "__main__":
        play_blackjack()
"""
import random
from src.logger.logger import logger

def card_value(card: str) -> int:
    """
    Определяет численное значение карты.

    :param card: Строка, представляющая карту (например, '2', 'K', 'A').
    :return: Целое число, представляющее значение карты.
    """
    if card in ['J', 'Q', 'K']:
        return 10
    if card == 'A':
        return 11  # Туз первоначально равен 11, но может быть изменен на 1
    return int(card)


def calculate_hand_value(hand: list[str]) -> int:
    """
    Вычисляет сумму очков карт в руке, обрабатывая тузы.

    :param hand: Список строк, представляющих карты в руке.
    :return: Суммарное значение карт в руке.
    """
    value = 0
    aces = 0
    for card in hand:
        card_val = card_value(card)
        value += card_val
        if card == 'A':
            aces += 1
    # Изменяет значение туза с 11 на 1, если сумма превышает 21.
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1
    return value


def create_deck() -> list[str]:
    """
    Создает и возвращает перемешанную колоду карт.

    :return: Список строк, представляющих карты в колоде.
    """
    suits = ['H', 'D', 'C', 'S']  # Hearts, Diamonds, Clubs, Spades
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [rank + suit for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck


def deal_card(deck: list[str]) -> str:
    """
    Извлекает и возвращает верхнюю карту из колоды.

    :param deck: Список строк, представляющих колоду карт.
    :return: Строка, представляющая выданную карту.
    """
    return deck.pop()


def display_hand(hand: list[str], hide_first_card: bool = False) -> None:
    """
    Выводит на экран карты в руке игрока или дилера.

    :param hand: Список строк, представляющих карты в руке.
    :param hide_first_card: Если True, то первая карта будет скрыта, по умолчанию False.
    """
    if hide_first_card:
        print(" [Hidden], " + ", ".join(hand[1:]))
    else:
        print(", ".join(hand))


def play_blackjack() -> None:
    """
    Запускает игровой процесс в Блэкджек.
    """
    deck = create_deck()
    player_hand = []
    dealer_hand = []

    # Раздача 2 карт игроку и дилеру
    for _ in range(2):
        player_hand.append(deal_card(deck))
        dealer_hand.append(deal_card(deck))

    player_score = calculate_hand_value(player_hand)
    dealer_score = calculate_hand_value(dealer_hand)

    print("Твои карты: ")
    display_hand(player_hand)
    print("Карты дилера: ")
    display_hand(dealer_hand, hide_first_card=True)

    # Ход игрока
    while True:
        print("Твой счет: ", player_score)
        action = input("Хочешь 'Hit' (взять карту) или 'Stand' (остановиться)? (h/s): ").lower()

        if action == 'h':
            player_hand.append(deal_card(deck))
            player_score = calculate_hand_value(player_hand)
            print("Твои карты: ")
            display_hand(player_hand)
            if player_score > 21:
                print("Твой счет: ", player_score)
                print("Перебор! Ты проиграл!")
                return
        elif action == 's':
            break
        else:
            print("Пожалуйста, выбери между 'h' и 's'")

    # Ход дилера
    print("Ход дилера")
    print("Карты дилера: ")
    display_hand(dealer_hand)
    while dealer_score < 17:
        dealer_hand.append(deal_card(deck))
        dealer_score = calculate_hand_value(dealer_hand)
        print("Карты дилера: ")
        display_hand(dealer_hand)

    print("Твой счет: ", player_score)
    print("Счет дилера: ", dealer_score)

    # Определение победителя
    if dealer_score > 21:
        print("У дилера перебор! Ты выиграл!")
    elif player_score > dealer_score or dealer_score > 21:
        print("Ты выиграл!")
    elif dealer_score > player_score:
        print("Дилер выиграл!")
    else:
        print("Ничья!")


if __name__ == "__main__":
    play_blackjack()
```