"""
<POKER>:
=================
Сложность: 4
-----------------
Игра "Покер" - это упрощенная версия карточной игры, где игрок получает 5 карт случайным образом из колоды, состоящей из чисел от 1 до 10. Цель игрока - собрать наилучшую покерную комбинацию из выпавших карт. Игрок имеет одну попытку замены карт. В конце игры определяется комбинация и сообщается игроку.
Правила игры:
1. Игроку выдается 5 случайных карт из колоды 1-10.
2. Игрок имеет возможность один раз заменить любое количество карт.
3. После замены карт, программа оценивает комбинацию игрока и выводит ее.
4. Возможные комбинации: пара, две пары, тройка, каре, фулл хаус, стрит, флеш, и "ничего" (старшая карта).
-----------------
Алгоритм:
1. Инициализация: Создать колоду карт (числа от 1 до 10), создать пустой набор карт игрока.
2. Раздача карт: Случайным образом выбрать 5 карт из колоды и поместить их в набор карт игрока.
3. Вывод карт игрока: Отобразить карты игрока на экране.
4. Запрос на замену: Спросить игрока, какие карты он хочет заменить (номера карт от 1 до 5).
5. Замена карт:
   - Удалить выбранные карты из набора карт игрока.
   - Случайным образом добавить новые карты из колоды, пока в наборе карт игрока не станет 5 карт.
6. Оценка комбинации:
   - Подсчитать количество повторений каждой карты.
   - Определить тип комбинации (пара, две пары, тройка, каре, фулл хаус, стрит, флеш или "ничего").
7. Вывод результата: Сообщить игроку его комбинацию.
-----------------
Блок-схема:
```mermaid
graph TD
    Start(Start) --> InitializeDeck(Initialize Deck);
    InitializeDeck --> DealCards(Deal 5 Cards to Player);
    DealCards --> DisplayCards(Display Player's Cards);
    DisplayCards --> AskForExchange(Ask for Cards to Exchange);
    AskForExchange --> ExchangeCards{Exchange Cards?};
    ExchangeCards -- Yes --> GetCardsToExchange(Get Card Numbers to Exchange);
    GetCardsToExchange --> RemoveCards(Remove Cards from Hand);
     RemoveCards --> DrawNewCards(Draw New Cards);
    DrawNewCards -->  ExchangeCardsDone(Exchange Done)

    ExchangeCards -- No --> EvaluateHand(Evaluate Hand);
    ExchangeCardsDone --> EvaluateHand;

    EvaluateHand --> DisplayResult(Display Result);
    DisplayResult --> End(End);
  
```
"""
import random

def create_deck():
    """Создает колоду карт от 1 до 10."""
    deck = list(range(1, 11))
    return deck

def deal_cards(deck, num_cards=5):
    """Раздает заданное количество карт из колоды."""
    hand = []
    for _ in range(num_cards):
        card = random.choice(deck)
        hand.append(card)
        deck.remove(card)
    return hand, deck

def display_hand(hand):
    """Выводит карты игрока на экран с их номерами."""
    print("Ваши карты:")
    for i, card in enumerate(hand):
        print(f"{i + 1}: {card}", end="  ")
    print()

def get_cards_to_exchange(hand):
    """Запрашивает у игрока номера карт для замены."""
    while True:
        try:
            cards_to_exchange = input("Введите номера карт для замены (через пробел, 0 для пропуска): ")
            if cards_to_exchange == '0':
                return []
            card_numbers = [int(num) for num in cards_to_exchange.split()]
            if all(1 <= num <= len(hand) for num in card_numbers):
                 return card_numbers
            else:
               print("Неверный номер карты. Введите номера от 1 до", len(hand))

        except ValueError:
             print("Неверный ввод. Введите номера карт через пробел.")


def exchange_cards(hand, deck, cards_to_exchange):
  """Заменяет выбранные карты на новые из колоды."""
  cards_to_exchange.sort(reverse=True) #сортируем номера карт по убыванию чтобы не было проблем при удалении
  for card_index in cards_to_exchange:
    if 0 < card_index <= len(hand): #проверка, что индекс в пределах длины набора карт
      removed_card = hand.pop(card_index-1)
      deck.append(removed_card) # возвращаем карту в колоду

  while len(hand) < 5:
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)

  return hand, deck


def evaluate_hand(hand):
    """Оценивает покерную комбинацию игрока."""
    counts = {}
    for card in hand:
        counts[card] = counts.get(card, 0) + 1

    values = list(counts.values())
    values.sort(reverse=True)
    hand.sort()

    # Определяем комбинации
    if values == [5]:
      return "Каре"
    elif values == [3, 2]:
      return "Фулл хаус"
    elif values == [4, 1]:
      return "Тройка"
    elif values == [2,2,1]:
       return "Две пары"
    elif values == [2,1,1,1]:
       return "Пара"
    elif  all(hand[i] == hand[0] + i for i in range(5)):
       return "Стрит"
    else:
        return "Ничего"

def play_poker():
    """Основная функция игры в покер."""
    print("Добро пожаловать в игру Покер!")

    # 1. Инициализация колоды
    deck = create_deck()
    
    # 2. Раздача карт
    player_hand, deck = deal_cards(deck)
    
    # 3. Вывод карт игрока
    display_hand(player_hand)

    # 4. Запрос на замену карт
    cards_to_exchange = get_cards_to_exchange(player_hand)
    
    # 5. Замена карт
    if cards_to_exchange:
      player_hand, deck = exchange_cards(player_hand, deck, cards_to_exchange)
      print("Вы обменяли карты.")
      display_hand(player_hand)
    else:
       print("Вы решили не менять карты.")
    
    # 6. Оценка комбинации
    combination = evaluate_hand(player_hand)
    
    # 7. Вывод результата
    print(f"Ваша комбинация: {combination}")

# Запуск игры
if __name__ == "__main__":
    play_poker()
"""
Пояснения:
1. **`create_deck()`**:
   - Создает колоду карт, представляющую собой список чисел от 1 до 10.
   - Возвращает список `deck`.

2. **`deal_cards(deck, num_cards=5)`**:
   - Принимает колоду `deck` и количество карт `num_cards` для раздачи (по умолчанию 5).
   - Создает пустой список `hand` для хранения карт игрока.
   - Выбирает случайные карты из колоды `deck` и добавляет их в `hand`.
   - Удаляет выданные карты из колоды `deck`.
   - Возвращает список карт игрока `hand` и обновленную колоду `deck`.

3. **`display_hand(hand)`**:
   - Принимает список карт `hand`.
   - Выводит карты игрока на экран, указывая номер каждой карты в списке (начиная с 1).

4. **`get_cards_to_exchange(hand)`**:
   - Запрашивает у игрока номера карт для замены, разделенные пробелами.
    -Возвращает список номеров карт, которые нужно заменить, или пустой список, если игрок не хочет менять карты.
   - Проверяет корректность ввода, просит повторить ввод в случае ошибки.

5. **`exchange_cards(hand, deck, cards_to_exchange)`**:
  - Заменяет выбранные карты на новые из колоды.
  - Сначала удаляет указанные карты из руки игрока и возвращает их обратно в колоду
   - Затем добавляет новые карты из колоды до тех пор пока в руке не окажется 5 карт.

6. **`evaluate_hand(hand)`**:
   - Принимает список карт `hand`.
   - Создает словарь `counts` для подсчета количества повторений каждой карты.
   - Определяет тип комбинации (пара, две пары, тройка, каре, фулл хаус, стрит или "ничего").
   - Возвращает строку с названием комбинации.

7. **`play_poker()`**:
   - Основная функция, управляющая ходом игры.
   - Выводит приветствие.
   - Инициализирует колоду.
   - Раздает карты игроку.
   - Выводит карты игрока на экран.
   - Запрашивает номера карт для замены.
   - Заменяет карты, если нужно.
   - Оценивает комбинацию игрока.
   - Выводит результат игры.

8.  **`if __name__ == "__main__":`**
     - Запускает игру, если файл запущен как скрипт.

licence:MIT(../licence)
"""
__author__ = 'hypo69 (hypo69@davidka.net)'
```