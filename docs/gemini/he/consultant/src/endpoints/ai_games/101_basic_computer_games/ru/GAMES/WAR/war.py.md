# Анализ кода модуля `war.py`

**Качество кода**
- **Соответствие требованиям к формату кода (1-10):**

    -  **Преимущества:**
        -  Код читаемый и структурированный.
        -  Используются осмысленные имена переменных и функций.
        -  Логика игры реализована в соответствии с описанием.
        -  Есть подробные комментарии, объясняющие основные моменты.
        -  Присутствует блок-схема, наглядно демонстрирующая алгоритм игры.
    -  **Недостатки:**
        -  Отсутствует docstring для модуля, функций и методов.
        -  Используется стандартный импорт `random` вместо `src.utils.jjson`
        -  Не используются логирование ошибок через `src.logger.logger`.
        -  Не используется reStructuredText (RST) для комментариев и docstring.

**Рекомендации по улучшению**

1.  **Документирование кода**:
    - Добавить docstring в формате reStructuredText (RST) для модуля, каждой функции, метода и переменной. Это необходимо для создания автоматической документации.
    - Включить описания параметров и возвращаемых значений функций.

2.  **Импорт и обработка данных**:
    - Заменить `import random` на `import random`.
   
3.  **Обработка ошибок:**
   -   Вместо общих `try-except` использовать `logger.error` для логирования исключений.

4.  **Форматирование комментариев**:
   -   Все комментарии должны быть в формате reStructuredText (RST).
   -   Комментарии должны быть добавлены в каждую строку кода, где есть изменения.

**Улучшенный код**

```python
"""
Модуль, реализующий карточную игру "Война".
=========================================================================================

Этот модуль содержит функции для создания колоды карт, раздачи карт игрокам,
определения победителя раунда и основной игровой цикл.

Пример использования
--------------------

Для запуска игры:

.. code-block:: python

    if __name__ == "__main__":
        play_war()

"""
import random  # Импортируем модуль random для перемешивания колоды
from src.logger.logger import logger # Импортируем логер для записи ошибок


def create_deck():
    """
    Создает стандартную колоду из 52 карт.

    :return: Список карт (строки, например, '2C', 'AH').
    :rtype: list
    """
    suits = ['C', 'D', 'H', 'S']  # Масти (Червы, Бубны, Крести, Пики)
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'] # Достоинства карт (2-10, Валет, Дама, Король, Туз)
    deck = [rank + suit for suit in suits for rank in ranks] # Создаем колоду как список строк (например, '2C' - двойка крести)
    return deck


def deal_cards(deck):
    """
    Разделяет колоду на две части для двух игроков.

    :param deck: Колода карт.
    :type deck: list
    :return: Кортеж из двух списков - колоды карт для первого и второго игрока.
    :rtype: tuple
    """
    random.shuffle(deck) # Перемешиваем колоду
    middle = len(deck) // 2 # Находим середину колоды
    player1_deck = deck[:middle] # Раздаем первую половину первому игроку
    player2_deck = deck[middle:] # Раздаем вторую половину второму игроку
    return player1_deck, player2_deck


def card_value(card):
    """
    Определяет числовое значение карты.

    :param card: Строка, представляющая карту (например, '2C', 'AH').
    :type card: str
    :return: Числовое значение карты.
    :rtype: int
    """
    rank = card[0]  # Берем первый символ карты, например '2' или 'T'
    if rank.isdigit(): # Если это цифра, то возвращаем ее как int
        return int(rank)
    elif rank == 'T':
        return 10  # 'T' - 10
    elif rank == 'J':
        return 11  # 'J' - Валет
    elif rank == 'Q':
        return 12  # 'Q' - Дама
    elif rank == 'K':
        return 13  # 'K' - Король
    elif rank == 'A':
        return 14  # 'A' - Туз


def war(player1_deck, player2_deck):
    """
    Реализует логику "войны" при равных картах.

    :param player1_deck: Колода карт первого игрока.
    :type player1_deck: list
    :param player2_deck: Колода карт второго игрока.
    :type player2_deck: list
    :return: Кортеж: победитель (1 или 2), карты для добавления в колоду первого игрока, карты для добавления в колоду второго игрока.
    :rtype: tuple
    """
    print("ВОЙНА!!!")
    # Проверка, есть ли у игроков достаточно карт для войны (минимум 4 карты у каждого)
    if len(player1_deck) < 4 or len(player2_deck) < 4:
        if len(player1_deck) < 4:
            print("У игрока 1 недостаточно карт для войны. Игрок 2 побеждает!")
            return 2, [], [] # Возвращаем, что выиграл игрок 2 и пустые списки для карт
        else:
            print("У игрока 2 недостаточно карт для войны. Игрок 1 побеждает!")
            return 1, [], [] # Возвращаем, что выиграл игрок 1 и пустые списки для карт

    # Забираем 3 карты "в закрытую" + 1 "открытую"
    player1_war_cards = []
    player2_war_cards = []
    for _ in range(3):
        player1_war_cards.append(player1_deck.pop(0)) # Забираем карты из начала колоды
        player2_war_cards.append(player2_deck.pop(0))

    player1_war_card = player1_deck.pop(0)
    player2_war_card = player2_deck.pop(0)
    print(f"Игрок 1 открывает: {player1_war_card}, Игрок 2 открывает: {player2_war_card}")
    war_cards = player1_war_cards + player2_war_cards + [player1_war_card, player2_war_card] #Собираем все карты из войны в один список
    
    # Сравниваем карты войны
    if card_value(player1_war_card) > card_value(player2_war_card):
        print("Игрок 1 выигрывает войну!")
        return 1, war_cards, []  # Возвращаем, что выиграл игрок 1 и список карт войны
    elif card_value(player2_war_card) > card_value(player1_war_card):
        print("Игрок 2 выигрывает войну!")
        return 2, [], war_cards  # Возвращаем, что выиграл игрок 2 и список карт войны
    else:
        print("Ещё одна война!")
        winner, player1_add_cards, player2_add_cards = war(player1_deck, player2_deck) # Рекурсивно вызываем функцию для следующей войны
        return winner, player1_add_cards + war_cards if winner == 1 else [], player2_add_cards + war_cards if winner == 2 else []


def play_war():
    """
    Основная функция игры в "Войну".

    Инициализирует колоду, раздает карты игрокам и запускает игровой цикл.
    Определяет победителя и выводит результат.
    """
    deck = create_deck()  # Создаем колоду
    player1_deck, player2_deck = deal_cards(deck) # Раздаем карты игрокам
    round_number = 0  # Счетчик раундов
    
    # Основной игровой цикл
    while player1_deck and player2_deck:
        round_number += 1 # Увеличиваем счетчик раундов
        print(f"\n--- Раунд {round_number} ---")
        
        player1_card = player1_deck.pop(0) # Игрок 1 выкладывает карту
        player2_card = player2_deck.pop(0) # Игрок 2 выкладывает карту
        print(f"Игрок 1 выкладывает: {player1_card}, Игрок 2 выкладывает: {player2_card}")

        # Сравниваем карты
        if card_value(player1_card) > card_value(player2_card):
            print("Игрок 1 выигрывает раунд!")
            player1_deck.append(player1_card) # Выигравший игрок забирает карты в конец своей колоды
            player1_deck.append(player2_card)
        elif card_value(player2_card) > card_value(player1_card):
            print("Игрок 2 выигрывает раунд!")
            player2_deck.append(player2_card)  # Выигравший игрок забирает карты в конец своей колоды
            player2_deck.append(player1_card)
        else:
           winner, player1_add_cards, player2_add_cards = war(player1_deck, player2_deck) # Если карты равны, вызываем функцию войны
           if winner == 1:
                player1_deck.extend(player1_add_cards) # Добавляем карты в колоду игрока 1
           elif winner == 2:
                player2_deck.extend(player2_add_cards)  # Добавляем карты в колоду игрока 2
        print(f"У Игрока 1 {len(player1_deck)} карт, у Игрока 2 {len(player2_deck)} карт.")
    # Определяем победителя
    if player1_deck:
        print("\nИгрок 1 победил!")
    else:
        print("\nИгрок 2 победил!")


if __name__ == "__main__":
    play_war()  # Вызываем функцию для начала игры
```