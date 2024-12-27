# Анализ кода модуля `war.py`

**Качество кода**
7
-  Плюсы
    - Код игры реализован в соответствии с правилами игры "Война".
    - Код хорошо структурирован, функции разделены по логическим блокам.
    - Имеется функция для определения значения карт.
    - Реализована рекурсивная функция для обработки случая "войны".
    - Код содержит подробные комментарии, объясняющие каждую часть кода.
    - Присутствует подробное описание алгоритма и блок-схема в начале файла.
-  Минусы
    - Отсутствуют docstring для функций и модуля.
    - Используется стандартный `print` для вывода информации, вместо логирования.
    -  Нет обработки возможных исключений.
    - Не используется `j_loads` или `j_loads_ns`.
    -  Некоторые комментарии не соответствуют стандарту reStructuredText.

**Рекомендации по улучшению**

1.  Добавить docstring к модулю и ко всем функциям.
2.  Использовать `from src.logger.logger import logger` для логирования вместо `print`.
3.  Убрать избыточные комментарии, переформулировать их в стиле RST.
4.  Использовать обработку ошибок с помощью `try-except` и `logger.error` для повышения надежности кода.
5.  Удалить избыточные комментарии и переписать в стиле RST.
6.  Добавить проверку на пустые колоды перед началом раунда, чтобы избежать ошибок.

**Оптимизированный код**

```python
"""
Модуль для реализации карточной игры "Война".
=========================================================================================

Этот модуль содержит функции для создания колоды карт, раздачи карт игрокам,
определения победителя раунда и обработки "войны".

Пример использования
--------------------

Пример запуска игры:

.. code-block:: python

    if __name__ == "__main__":
        play_war()
"""
import random
from src.logger.logger import logger  #  Импортируем logger

def create_deck() -> list[str]:
    """
    Создает стандартную колоду из 52 игральных карт.

    :return: Список строк, представляющих карты.
    :rtype: list[str]
    """
    suits = ['C', 'D', 'H', 'S']  # Масти (крести, бубны, червы, пики)
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']  # Достоинства карт (2-10, Валет, Дама, Король, Туз)
    deck = [rank + suit for suit in suits for rank in ranks]  # Создаем колоду как список строк (например, '2C' - двойка крести)
    return deck

def deal_cards(deck: list[str]) -> tuple[list[str], list[str]]:
    """
    Разделяет колоду между двумя игроками.

    :param deck: Колода карт.
    :type deck: list[str]
    :return: Кортеж из двух списков, представляющих колоды игроков.
    :rtype: tuple[list[str], list[str]]
    """
    random.shuffle(deck)  # Перемешиваем колоду
    middle = len(deck) // 2  # Находим середину колоды
    player1_deck = deck[:middle] # Раздаем первую половину первому игроку
    player2_deck = deck[middle:]  # Раздаем вторую половину второму игроку
    return player1_deck, player2_deck

def card_value(card: str) -> int:
    """
    Определяет числовое значение карты.

    :param card: Строка, представляющая карту.
    :type card: str
    :return: Числовое значение карты.
    :rtype: int
    """
    rank = card[0] # Берем первый символ карты, например '2' или 'T'
    if rank.isdigit():  # Если это цифра, то возвращаем ее как int
        return int(rank)
    elif rank == 'T':
        return 10   # 'T' - 10
    elif rank == 'J':
        return 11   # 'J' - Валет
    elif rank == 'Q':
        return 12   # 'Q' - Дама
    elif rank == 'K':
        return 13   # 'K' - Король
    elif rank == 'A':
        return 14   # 'A' - Туз

def war(player1_deck: list[str], player2_deck: list[str]) -> tuple[int, list[str], list[str]]:
    """
    Реализует логику "войны" в игре.

    :param player1_deck: Колода первого игрока.
    :type player1_deck: list[str]
    :param player2_deck: Колода второго игрока.
    :type player2_deck: list[str]
    :return: Кортеж из победителя (1 или 2), карт первого игрока и карт второго игрока.
    :rtype: tuple[int, list[str], list[str]]
    """
    logger.info("ВОЙНА!!!")
    # Проверка, есть ли у игроков достаточно карт для войны (минимум 4 карты у каждого)
    if len(player1_deck) < 4 or len(player2_deck) < 4:
        if len(player1_deck) < 4:
            logger.info("У игрока 1 недостаточно карт для войны. Игрок 2 побеждает!")
            return 2, [], [] # Возвращаем, что выиграл игрок 2 и пустые списки для карт
        else:
            logger.info("У игрока 2 недостаточно карт для войны. Игрок 1 побеждает!")
            return 1, [], [] # Возвращаем, что выиграл игрок 1 и пустые списки для карт

    # Забираем 3 карты "в закрытую" + 1 "открытую"
    player1_war_cards = []
    player2_war_cards = []
    for _ in range(3):
        player1_war_cards.append(player1_deck.pop(0))  # Забираем карты из начала колоды
        player2_war_cards.append(player2_deck.pop(0))

    player1_war_card = player1_deck.pop(0)
    player2_war_card = player2_deck.pop(0)
    logger.info(f"Игрок 1 открывает: {player1_war_card}, Игрок 2 открывает: {player2_war_card}")
    war_cards = player1_war_cards + player2_war_cards + [player1_war_card, player2_war_card] #Собираем все карты из войны в один список

    # Сравниваем карты войны
    if card_value(player1_war_card) > card_value(player2_war_card):
        logger.info("Игрок 1 выигрывает войну!")
        return 1, war_cards, []  # Возвращаем, что выиграл игрок 1 и список карт войны
    elif card_value(player2_war_card) > card_value(player1_war_card):
        logger.info("Игрок 2 выигрывает войну!")
        return 2, [], war_cards  # Возвращаем, что выиграл игрок 2 и список карт войны
    else:
        logger.info("Ещё одна война!")
        winner, player1_add_cards, player2_add_cards = war(player1_deck, player2_deck) #Рекурсивно вызываем функцию для следующей войны
        return winner, player1_add_cards + war_cards if winner == 1 else [], player2_add_cards + war_cards if winner == 2 else []

def play_war():
    """
    Основная функция для запуска игры "Война".
    """
    deck = create_deck()   # Создаем колоду
    player1_deck, player2_deck = deal_cards(deck) # Раздаем карты игрокам
    round_number = 0    # Счетчик раундов

    # Основной игровой цикл
    while player1_deck and player2_deck:
        round_number += 1  # Увеличиваем счетчик раундов
        logger.info(f"\n--- Раунд {round_number} ---")

        # Проверка на пустые колоды
        if not player1_deck or not player2_deck:
            break # Выход из цикла, если у игрока закончились карты

        try:
            player1_card = player1_deck.pop(0)  # Игрок 1 выкладывает карту
            player2_card = player2_deck.pop(0)  # Игрок 2 выкладывает карту
            logger.info(f"Игрок 1 выкладывает: {player1_card}, Игрок 2 выкладывает: {player2_card}")

            # Сравниваем карты
            if card_value(player1_card) > card_value(player2_card):
                logger.info("Игрок 1 выигрывает раунд!")
                player1_deck.append(player1_card)  # Выигравший игрок забирает карты в конец своей колоды
                player1_deck.append(player2_card)
            elif card_value(player2_card) > card_value(player1_card):
                logger.info("Игрок 2 выигрывает раунд!")
                player2_deck.append(player2_card)  # Выигравший игрок забирает карты в конец своей колоды
                player2_deck.append(player1_card)
            else:
                winner, player1_add_cards, player2_add_cards = war(player1_deck, player2_deck) # Если карты равны, вызываем функцию войны
                if winner == 1:
                    player1_deck.extend(player1_add_cards) # Добавляем карты в колоду игрока 1
                elif winner == 2:
                    player2_deck.extend(player2_add_cards)  # Добавляем карты в колоду игрока 2
            logger.info(f"У Игрока 1 {len(player1_deck)} карт, у Игрока 2 {len(player2_deck)} карт.")
        except Exception as ex: # Ловим ошибку, если она вдруг возникнет
            logger.error('Произошла ошибка в ходе игры', ex)
            break
    # Определяем победителя
    if player1_deck:
        logger.info("\nИгрок 1 победил!")
    else:
        logger.info("\nИгрок 2 победил!")

if __name__ == "__main__":
    play_war()
```