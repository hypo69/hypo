# Анализ кода модуля `13_blkjak.ru.md`

**Качество кода**

- **Соблюдение требований к формату кода (1-10):**

  1.  **Формат документации**: Используется Markdown, а не reStructuredText (RST).
  2.  **Сохранение комментариев**: Комментарии в формате `#` отсутствуют.
  3.  **Обработка данных**: Нет операций с данными в коде.
  4.  **Анализ структуры**: Код представляет собой текстовое описание, а не программный код.
  5.  **Улучшение и рефакторинг**: Нет кода для рефакторинга.
  6.  **Логирование**: Нет использования логгера.
  7.  **Конечный код**: Код в формате Markdown, а не Python.
  8.  **Примеры кода**: Есть примеры, но они не в формате RST.
  9.  **Дополнительные инструкции**: Не все инструкции соблюдены, особенно касающиеся формата RST и логгирования.
  10. **Порядок блоков**: Соответствует структуре, но не содержит кода Python.
 -  **Преимущества**:
    -  Хорошо структурированное описание правил игры "Блэкджек" на русском языке.
    -  Понятные пошаговые инструкции для реализации игры.
    -  Примеры работы программы, которые помогают понять игровой процесс.
    -  Перечислены возможные ограничения в игре.
 - **Недостатки**:
    -  Представлен текст в формате Markdown, а не Python.
    -  Не используются reStructuredText (RST) для комментариев.
    -  Отсутствует код, который можно анализировать и улучшать.
    -  Не соблюдены требования по использованию `j_loads`, логгера и `try-except`.

**Рекомендации по улучшению**

1.  **Переписать на Python**: Необходимо реализовать код игры "Блэкджек" на языке Python.
2.  **Добавить документацию RST**: Добавить комментарии в формате RST для модуля, функций и классов.
3.  **Использовать j_loads**: Если потребуются загрузки данных, использовать `j_loads` или `j_loads_ns` из `src.utils.jjson`.
4.  **Реализовать логирование**: Добавить логирование ошибок с помощью `from src.logger.logger import logger`.
5.  **Реализовать обработку ошибок**: Использовать `logger.error` для обработки ошибок вместо чрезмерного использования `try-except`.
6.  **Привести в соответствие с требованиями**: Привести код в соответствие с требованиями, указанными в задании.

**Улучшенный код**
```python
"""
Модуль для реализации игры Блэкджек (21).
=========================================================================================

Модуль содержит функции для симуляции игры в блэкджек, включая раздачу карт,
обработку ходов игрока и дилера, а также подсчет результатов.

Пример использования
--------------------

Пример запуска игры:

.. code-block:: python

   from src.endpoints.ai_games.101_basic_computer_games.ru.rules.blkjak import play_blackjack

   play_blackjack()
"""
import random
from typing import List, Tuple
from src.logger.logger import logger  # импортируем логгер #
from src.utils.jjson import j_loads, j_loads_ns # импортируем json загрузку #


def calculate_hand_value(hand: List[str]) -> int:
    """
    Вычисляет стоимость карт в руке.

    :param hand: Список карт в руке.
    :return: Общая стоимость карт в руке.
    """
    ace_count = 0
    total = 0
    card_values = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 10, 'Q': 10, 'K': 10, 'A': 11
    }
    for card in hand:
        try:
            total += card_values[card]
            if card == 'A':
                ace_count += 1
        except KeyError as ex: # обрабатываем ошибку ключа
             logger.error(f'Неизвестная карта {card}', ex) # логируем ошибку
             return 0 # возвращаем 0 в случае ошибки
    
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    return total


def deal_card(deck: List[str]) -> Tuple[str, List[str]]:
    """
    Выдает карту из колоды.

    :param deck: Колода карт.
    :return: Выданная карта и обновленная колода.
    """
    if not deck:
         logger.error('Колода пуста') # логируем ошибку
         return '', deck # возвращаем пустую карту и колоду
    card = deck.pop()
    return card, deck


def create_deck() -> List[str]:
    """
    Создает стандартную колоду из 52 карт.

    :return: Новая колода карт.
    """
    suits = ['H', 'D', 'C', 'S']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [rank for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck


def display_cards(player_hand: List[str], dealer_hand: List[str], hide_dealer: bool = True) -> None:
    """
    Отображает карты игрока и дилера.

    :param player_hand: Рука игрока.
    :param dealer_hand: Рука дилера.
    :param hide_dealer: Если True, то скрывает первую карту дилера.
    """
    print("Ваши карты:", ', '.join(player_hand), f"(Сумма: {calculate_hand_value(player_hand)})")
    if hide_dealer:
        print("Карта дилера: <скрыто>,", dealer_hand[1])
    else:
        print("Карты дилера:", ', '.join(dealer_hand), f"(Сумма: {calculate_hand_value(dealer_hand)})")


def player_turn(deck: List[str], player_hand: List[str], balance: int, bet: int) -> Tuple[List[str], int, bool]:
        """
        Обрабатывает ход игрока.

        :param deck: Колода карт.
        :param player_hand: Рука игрока.
        :param balance: Баланс игрока.
        :param bet: Ставка игрока.
        :return: Обновленные рука игрока, баланс и флаг проигрыша.
        """
        while True:
            display_cards(player_hand, [], True)
            action = input("Хотите взять карту? (да/нет/удвоить): ").lower()
            if action in ['да', 'д']: # действие взять карту #
               card, deck = deal_card(deck)
               player_hand.append(card)
               if calculate_hand_value(player_hand) > 21:
                    print("Вы проиграли, перебор!")
                    return player_hand, balance - bet, True # игрок проиграл #
            elif action in ['нет', 'н']: # действие не брать карту #
                return player_hand, balance, False # ход закончен #
            elif action in ['удвоить', 'у']: # действие удвоить ставку #
                if balance < bet * 2: # проверка достаточно ли баланса #
                  print('Недостаточно средств')
                  continue
                card, deck = deal_card(deck)
                player_hand.append(card)
                if calculate_hand_value(player_hand) > 21: # если перебор #
                    print("Вы проиграли, перебор!")
                    return player_hand, balance - bet*2, True # проигрыш #
                return player_hand, balance, False
            else:
                print('Неверный ввод') # сообщение при неверном вводе #


def dealer_turn(deck: List[str], dealer_hand: List[str]) -> List[str]:
        """
        Обрабатывает ход дилера.

        :param deck: Колода карт.
        :param dealer_hand: Рука дилера.
        :return: Обновленная рука дилера.
        """
        while calculate_hand_value(dealer_hand) < 17:
            card, deck = deal_card(deck)
            dealer_hand.append(card)
            print("Дилер берет карту...")
        return dealer_hand


def determine_winner(player_hand: List[str], dealer_hand: List[str], bet: int, balance: int) -> Tuple[str, int]:
        """
        Определяет победителя игры.

        :param player_hand: Рука игрока.
        :param dealer_hand: Рука дилера.
        :param bet: Ставка игрока.
        :param balance: Баланс игрока.
        :return: Результат игры и обновленный баланс.
        """
        player_value = calculate_hand_value(player_hand)
        dealer_value = calculate_hand_value(dealer_hand)
        if dealer_value > 21:
            print("Дилер перебрал. Вы выигрываете!")
            return "win", balance + bet
        elif player_value > dealer_value:
            print("Вы выигрываете!")
            return "win", balance + bet
        elif player_value == dealer_value:
            print("Ничья.")
            return "draw", balance
        else:
            print("Вы проигрываете.")
            return "lose", balance - bet


def play_blackjack():
    """
    Запускает игру в Блэкджек.
    """
    balance = 200
    while True:
        print("Добро пожаловать в блэкджек!")
        print(f"У вас есть ${balance}. Сколько вы хотите поставить?")
        while True:
            try:
               bet = int(input("> "))
               if bet > balance:
                    print("Недостаточно средств на балансе.")
               elif bet <= 0 or bet > 500:
                   print("Ставка должна быть от 1 до 500")
               else:
                 break
            except ValueError as ex: # обрабатываем ошибку если ввели не число #
                logger.error('Неверный ввод, необходимо ввести число', ex) # логируем ошибку
        deck = create_deck()
        player_hand = []
        dealer_hand = []
        for _ in range(2):
           card, deck = deal_card(deck)
           player_hand.append(card)
        card, deck = deal_card(deck)
        dealer_hand.append(card)
        card, deck = deal_card(deck)
        dealer_hand.append(card)
        display_cards(player_hand, dealer_hand, True)

        # Страховка если у дилера туз
        if dealer_hand[0] == 'A': # проверяем если первая карта дилера туз #
          insurance = input("Хотите сделать страховку? (да/нет) ").lower()
          if insurance in ['да', 'д']:
            if balance < bet / 2: # проверяем хватит ли баланса на страховку #
                print('Недостаточно средств')
            else:
                insurance_bet = bet / 2
                balance -= insurance_bet
                if calculate_hand_value(dealer_hand) == 21: # если у дилера блекджек #
                   print('У дилера блекджек, страховка сыграла')
                   balance += insurance_bet * 2
                else:
                    print("Страховка не сыграла.")
        
        player_hand, balance, player_lost = player_turn(deck, player_hand, balance, bet)
        if player_lost:
            display_cards(player_hand, dealer_hand, False) # показываем карты в случае проигрыша #
            if balance <= 0: # если баланс 0 то игра закончена #
                print('У вас закончились деньги. Игра окончена')
                break
        else:
            dealer_hand = dealer_turn(deck, dealer_hand) # если игрок не проиграл то играет дилер #
            display_cards(player_hand, dealer_hand, False)
            result, balance = determine_winner(player_hand, dealer_hand, bet, balance)
        
            if balance <= 0: # если баланс 0 то игра закончена #
                print('У вас закончились деньги. Игра окончена')
                break

        play_again = input("Хотите сыграть еще раз? (да/нет) ").lower()
        if play_again in ['нет', 'н']: # если не хочет играть дальше #
           print("До свидания!")
           break # выходим из цикла #
```