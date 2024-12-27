# Анализ кода модуля war.py

**Качество кода**
    7
-   Плюсы
        - Код игры "Война" достаточно хорошо структурирован и разбит на функции, что облегчает понимание и модификацию.
        - Используются осмысленные имена переменных и функций.
        -  Игра корректно обрабатывает основные правила игры "Война", включая "войну" и рекурсивные "войны".
        -  Код содержит подробное описание алгоритма и блок-схему игры, что помогает понять логику работы.
        -  Присутствуют комментарии, объясняющие основные этапы работы кода.
-   Минусы
    -  Отсутствует документация в формате reStructuredText (RST).
    -  Не используется логирование ошибок.
    -  Код не соответствует pep8.

**Рекомендации по улучшению**
1.  Добавьте docstring в формате reStructuredText (RST) ко всем функциям для улучшения читаемости и генерации документации.
2.  Используйте логирование для отслеживания ошибок и других важных событий в коде с помощью `from src.logger.logger import logger`.
3.  Удалите избыточные комментарии (например, после строки кода, где и так понятно, что происходит).
4.  Используйте более точные формулировки в комментариях, избегая общих фраз, таких как "получаем" или "делаем".
5.  Код необходимо привести в соответствие с PEP 8.
6.  Для более корректной обработки "войны" можно переписать логику добавления карт в колоды игроков, чтобы не было дублирования кода.
7.  Применить проверку на корректность введенных данных (например, не должно быть пустых колод при старте игры).

**Оптимизированный код**
```python
"""
Модуль для реализации карточной игры "Война".
=================================================

Этот модуль содержит функции для создания колоды, раздачи карт,
определения значения карт, реализации логики войны и основной игровой логики.

Пример использования
--------------------

.. code-block:: python

   if __name__ == "__main__":
        play_war()
"""
import random
#  Импортируем логгер для записи ошибок и отладочной информации.
from src.logger.logger import logger


def create_deck() -> list:
    """
    Создает стандартную колоду из 52 игральных карт.

    :return: Список строк, представляющих игральные карты.
    :rtype: list
    """
    suits = ["C", "D", "H", "S"]  # Масти (Червы, Бубны, Крести, Пики)
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]  # Достоинства карт (2-10, Валет, Дама, Король, Туз)
    deck = [rank + suit for suit in suits for rank in ranks] # Создает колоду как список строк (например, '2C' - двойка крести)
    return deck


def deal_cards(deck: list) -> tuple:
    """
    Перемешивает колоду и раздает карты двум игрокам.

    :param deck: Список карт для раздачи.
    :type deck: list
    :return: Кортеж из двух списков, представляющих колоды игроков.
    :rtype: tuple
    """
    random.shuffle(deck)  #  Перемешивает колоду
    middle = len(deck) // 2  #  Определяет середину колоды
    player1_deck = deck[:middle]  #  Раздает первую половину первому игроку
    player2_deck = deck[middle:]  #  Раздает вторую половину второму игроку
    return player1_deck, player2_deck


def card_value(card: str) -> int:
    """
    Определяет числовое значение игральной карты.

    :param card: Строка, представляющая игральную карту (например, '2C', 'AH').
    :type card: str
    :return: Числовое значение карты.
    :rtype: int
    """
    rank = card[0]  #  Берет первый символ карты, например '2' или 'T'
    if rank.isdigit():  # Если это цифра, то возвращаем ее как int
        return int(rank)
    elif rank == 'T':
        return 10   # 'T' - 10
    elif rank == 'J':
        return 11  # 'J' - Валет
    elif rank == 'Q':
        return 12  # 'Q' - Дама
    elif rank == 'K':
        return 13  # 'K' - Король
    elif rank == 'A':
        return 14  # 'A' - Туз
    else:
        logger.error(f'Неверный формат карты {card}')
        return 0


def war(player1_deck: list, player2_deck: list) -> tuple:
    """
    Реализует логику "войны" в игре.

    :param player1_deck: Список карт первого игрока.
    :type player1_deck: list
    :param player2_deck: Список карт второго игрока.
    :type player2_deck: list
    :return: Кортеж, содержащий победителя (1 или 2), список карт для добавления первому игроку и список карт для добавления второму игроку.
    :rtype: tuple
    """
    print("ВОЙНА!!!")
    # Проверяет, достаточно ли карт у игроков для войны (минимум 4 карты у каждого).
    if len(player1_deck) < 4 or len(player2_deck) < 4:
        if len(player1_deck) < 4:
            print("У игрока 1 недостаточно карт для войны. Игрок 2 побеждает!")
            return 2, [], []  # Возвращает, что выиграл игрок 2 и пустые списки для карт
        else:
            print("У игрока 2 недостаточно карт для войны. Игрок 1 побеждает!")
            return 1, [], []  # Возвращает, что выиграл игрок 1 и пустые списки для карт

    # Забирает 3 карты "в закрытую" + 1 "открытую".
    player1_war_cards = []
    player2_war_cards = []
    for _ in range(3):
        player1_war_cards.append(player1_deck.pop(0))  # Забирает карты из начала колоды
        player2_war_cards.append(player2_deck.pop(0))

    player1_war_card = player1_deck.pop(0)
    player2_war_card = player2_deck.pop(0)
    print(f"Игрок 1 открывает: {player1_war_card}, Игрок 2 открывает: {player2_war_card}")
    war_cards = player1_war_cards + player2_war_cards + [player1_war_card, player2_war_card]  # Собирает все карты из войны в один список

    # Сравнивает карты войны.
    if card_value(player1_war_card) > card_value(player2_war_card):
        print("Игрок 1 выигрывает войну!")
        return 1, war_cards, []  # Возвращает, что выиграл игрок 1 и список карт войны
    elif card_value(player2_war_card) > card_value(player1_war_card):
        print("Игрок 2 выигрывает войну!")
        return 2, [], war_cards  # Возвращает, что выиграл игрок 2 и список карт войны
    else:
        print("Ещё одна война!")
        winner, player1_add_cards, player2_add_cards = war(player1_deck, player2_deck)  # Рекурсивно вызывает функцию для следующей войны
        return winner, player1_add_cards + war_cards if winner == 1 else [], player2_add_cards + war_cards if winner == 2 else []


def play_war():
    """
    Основная функция для запуска игры "Война".
    """
    deck = create_deck()    # Создает колоду
    player1_deck, player2_deck = deal_cards(deck)  # Раздает карты игрокам
    round_number = 0    # Счетчик раундов

    # Основной игровой цикл.
    while player1_deck and player2_deck:
        round_number += 1  # Увеличивает счетчик раундов
        print(f"\n--- Раунд {round_number} ---")

        player1_card = player1_deck.pop(0)  # Игрок 1 выкладывает карту
        player2_card = player2_deck.pop(0)  # Игрок 2 выкладывает карту
        print(f"Игрок 1 выкладывает: {player1_card}, Игрок 2 выкладывает: {player2_card}")

        # Сравнивает карты.
        if card_value(player1_card) > card_value(player2_card):
            print("Игрок 1 выигрывает раунд!")
            player1_deck.append(player1_card)  # Выигравший игрок забирает карты в конец своей колоды
            player1_deck.append(player2_card)
        elif card_value(player2_card) > card_value(player1_card):
            print("Игрок 2 выигрывает раунд!")
            player2_deck.append(player2_card) # Выигравший игрок забирает карты в конец своей колоды
            player2_deck.append(player1_card)
        else:
            winner, player1_add_cards, player2_add_cards = war(player1_deck, player2_deck)  # Если карты равны, вызывается функция войны
            if winner == 1:
                 player1_deck.extend(player1_add_cards)  # Добавляет карты в колоду игрока 1
            elif winner == 2:
                 player2_deck.extend(player2_add_cards)  # Добавляет карты в колоду игрока 2
        print(f"У Игрока 1 {len(player1_deck)} карт, у Игрока 2 {len(player2_deck)} карт.")

    # Определяет победителя.
    if player1_deck:
        print("\nИгрок 1 победил!")
    else:
        print("\nИгрок 2 победил!")


if __name__ == "__main__":
    play_war()
```