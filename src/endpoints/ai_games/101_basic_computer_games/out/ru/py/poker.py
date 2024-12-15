"""
POKER:
=================
Сложность: 7
-----------------
Игра "Покер" представляет собой упрощенную версию карточного покера, в которой игрок играет против компьютера. Игроку и компьютеру раздается по пять карт, и они оцениваются на наличие покерных комбинаций (пара, две пары, тройка, стрит, флеш, фул-хаус, каре и стрит-флеш). Выигрывает тот, у кого комбинация старше. Если комбинаций нет, выигрывает игрок с самой старшей картой. В случае равенства комбинаций, побеждает игрок с более старшей картой в комбинации, или, если и они равны, происходит ничья.

Правила игры:
1.  Игроку и компьютеру раздается по 5 карт из стандартной колоды в 52 карты.
2.  Комбинации карт оцениваются по стандартным правилам покера (пара, две пары, тройка, стрит, флеш, фул-хаус, каре, стрит-флеш)
3.  Выигрывает тот, у кого комбинация старше.
4.  При равенстве комбинаций сравниваются старшие карты в комбинации.
5.  В случае полного равенства объявляется ничья.
-----------------
Алгоритм:
1.  Инициализация колоды карт и перемешивание.
2.  Раздача 5 карт игроку и 5 карт компьютеру.
3.  Определение комбинации карт игрока.
4.  Определение комбинации карт компьютера.
5.  Сравнение комбинаций игрока и компьютера.
    5.1 Если комбинация игрока старше, выводится сообщение о победе игрока.
    5.2 Если комбинация компьютера старше, выводится сообщение о победе компьютера.
    5.3 Если комбинации равны, сравниваются старшие карты в комбинации.
        5.3.1 Если старшая карта игрока старше, выводится сообщение о победе игрока.
        5.3.2 Если старшая карта компьютера старше, выводится сообщение о победе компьютера.
        5.3.3 Если старшие карты равны, выводится сообщение о ничье.
6. Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeDeck["<p align='left'>Инициализация и перемешивание колоды карт:
    <code><b>
    deck = create_deck()
    shuffle(deck)
    </b></code></p>"]
    InitializeDeck --> DealCards["<p align='left'>Раздача карт:
    <code><b>
    playerHand = deal_hand(deck)
    computerHand = deal_hand(deck)
    </b></code></p>"]
    DealCards --> EvaluatePlayerHand["<p align='left'>Оценка руки игрока:
    <code><b>playerRank, playerHighCard = evaluate_hand(playerHand)</b></code></p>"]
    EvaluatePlayerHand --> EvaluateComputerHand["<p align='left'>Оценка руки компьютера:
    <code><b>computerRank, computerHighCard = evaluate_hand(computerHand)</b></code></p>"]
    EvaluateComputerHand --> CompareHands{"<p align='left'>Сравнение комбинаций:
    <code><b>playerRank > computerRank?</b></code></p>"}
    CompareHands -- Да --> OutputPlayerWins["Вывод сообщения: <b>Игрок победил!</b>"]
    OutputPlayerWins --> End["Конец"]
    CompareHands -- Нет --> CompareRank{"<code><b>playerRank == computerRank?</b></code>"}
    CompareRank -- Да --> CompareHighCard{"<p align='left'>Сравнение старших карт:
    <code><b>playerHighCard > computerHighCard?</b></code></p>"}
    CompareHighCard -- Да --> OutputPlayerWinsHighCard["Вывод сообщения: <b>Игрок победил по старшей карте!</b>"]
    OutputPlayerWinsHighCard --> End
    CompareHighCard -- Нет --> CompareHighCardEqual{"<code><b>playerHighCard == computerHighCard?</b></code>"}
    CompareHighCardEqual -- Да --> OutputTie["Вывод сообщения: <b>Ничья!</b>"]
    OutputTie --> End
     CompareHighCardEqual -- Нет --> OutputComputerWinsHighCard["Вывод сообщения: <b>Компьютер победил по старшей карте!</b>"]
    OutputComputerWinsHighCard --> End
    CompareRank -- Нет --> OutputComputerWins["Вывод сообщения: <b>Компьютер победил!</b>"]
    OutputComputerWins --> End
```
**Legenda**:
    Start - Начало программы.
    InitializeDeck - Инициализация колоды карт и ее перемешивание.
    DealCards - Раздача карт игроку и компьютеру.
    EvaluatePlayerHand - Оценка комбинации карт игрока.
    EvaluateComputerHand - Оценка комбинации карт компьютера.
    CompareHands - Сравнение комбинаций карт игрока и компьютера.
    OutputPlayerWins - Вывод сообщения о победе игрока.
    End - Конец программы.
    CompareRank - Проверка на равенство рангов комбинаций.
    CompareHighCard - Сравнение старших карт, если ранги равны.
    OutputPlayerWinsHighCard - Вывод сообщения о победе игрока по старшей карте.
    CompareHighCardEqual - Проверка на равенство старших карт.
    OutputTie - Вывод сообщения о ничьей.
    OutputComputerWinsHighCard - Вывод сообщения о победе компьютера по старшей карте.
    OutputComputerWins - Вывод сообщения о победе компьютера.
"""
import random

# Функция для создания стандартной колоды карт
def create_deck():
    suits = ["H", "D", "C", "S"]  # Черви, бубны, трефы, пики
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"] # Номиналы карт
    deck = [rank + suit for suit in suits for rank in ranks] # Создаем колоду
    return deck

# Функция для раздачи карт
def deal_hand(deck, hand_size=5):
    hand = [] # Рука игрока
    for _ in range(hand_size): # Берем карты из колоды
        card = deck.pop(0)
        hand.append(card) # Добавляем карту в руку
    return hand

# Функция для оценки покерной комбинации
def evaluate_hand(hand):
    ranks = [card[0] for card in hand] # Получаем все ранги карт
    suits = [card[1] for card in hand] # Получаем все масти карт
    rank_counts = {} # Словарь для подсчета рангов
    for rank in ranks: # Считаем количество карт каждого ранга
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
    
    values = list(rank_counts.values()) # Количество карт каждого ранга
    sorted_ranks = sorted(ranks, key="23456789TJQKA".index) # Сортируем ранги для определения стрита
    
    # Проверка на стрит
    is_straight = True
    for i in range(len(sorted_ranks) - 1):
      if "23456789TJQKA".index(sorted_ranks[i+1]) - "23456789TJQKA".index(sorted_ranks[i]) != 1:
         is_straight = False
         break
    # Проверка на флеш
    is_flush = len(set(suits)) == 1
    
    # Определение комбинации
    if is_straight and is_flush: # Стрит-флеш
       return 8, "23456789TJQKA".index(sorted_ranks[-1])
    elif 4 in values: # Каре
       return 7, max("23456789TJQKA".index(rank) for rank in ranks)
    elif 3 in values and 2 in values: # Фулл-хаус
       return 6, max("23456789TJQKA".index(rank) for rank in ranks)
    elif is_flush: # Флеш
       return 5, max("23456789TJQKA".index(rank) for rank in ranks)
    elif is_straight: # Стрит
       return 4, "23456789TJQKA".index(sorted_ranks[-1])
    elif 3 in values: # Тройка
       return 3, max("23456789TJQKA".index(rank) for rank in ranks)
    elif values.count(2) == 2: # Две пары
      return 2, max("23456789TJQKA".index(rank) for rank in ranks)
    elif 2 in values: # Пара
      return 1, max("23456789TJQKA".index(rank) for rank in ranks)
    else: # Старшая карта
       return 0, max("23456789TJQKA".index(rank) for rank in ranks)

# Функция для сравнения рук
def compare_hands(player_rank, player_high_card, computer_rank, computer_high_card):
    if player_rank > computer_rank:
        return "Игрок победил!" # Ранг комбинации игрока выше
    elif player_rank < computer_rank:
        return "Компьютер победил!" # Ранг комбинации компьютера выше
    else: # Если ранги равны, сравниваем старшие карты
       if player_high_card > computer_high_card:
           return "Игрок победил по старшей карте!" # Старшая карта игрока выше
       elif player_high_card < computer_high_card:
           return "Компьютер победил по старшей карте!" # Старшая карта компьютера выше
       else:
           return "Ничья!" # Старшие карты равны


# Основная функция игры
def play_poker():
    deck = create_deck() # Создание колоды
    random.shuffle(deck) # Перемешивание колоды
    player_hand = deal_hand(deck) # Раздача карт игроку
    computer_hand = deal_hand(deck) # Раздача карт компьютеру
    
    print("Карты игрока:", player_hand)
    print("Карты компьютера:", computer_hand)
    
    player_rank, player_high_card = evaluate_hand(player_hand) # Оценка руки игрока
    computer_rank, computer_high_card = evaluate_hand(computer_hand) # Оценка руки компьютера
    
    result = compare_hands(player_rank, player_high_card, computer_rank, computer_high_card) # Сравнение рук
    print(result) # Вывод результата


if __name__ == "__main__":
    play_poker() # Запуск игры
"""
Пояснения:
1. **Импорт модуля `random`**:
   - `import random`: Импортирует модуль `random`, который используется для перемешивания колоды карт.

2. **Функция `create_deck()`**:
   - Создает стандартную колоду из 52 карт.
   - Определяет списки мастей (`suits`) и рангов (`ranks`).
   - Использует генератор списков для создания колоды, где каждая карта представлена строкой вида "рангмасть" (например, "AH" - туз червей).

3. **Функция `deal_hand(deck, hand_size=5)`**:
   - Принимает колоду (`deck`) и размер руки (`hand_size`, по умолчанию 5).
   - Раздает карты из колоды в руку.
   - Удаляет розданные карты из колоды, чтобы они не были розданы снова.
   - Возвращает список карт в руке.

4. **Функция `evaluate_hand(hand)`**:
   - Принимает руку (`hand`) и анализирует ее, чтобы определить покерную комбинацию.
   - Получает списки рангов (`ranks`) и мастей (`suits`) из руки.
   - Считает количество карт каждого ранга с помощью словаря `rank_counts`.
   - Сортирует ранги карт для проверки на стрит.
   - Проверяет, является ли рука стритом или флешем.
   - Определяет комбинацию в соответствии с покерными правилами (стрит-флеш, каре, фулл-хаус, флеш, стрит, тройка, две пары, пара, старшая карта).
   - Возвращает ранг комбинации и старшую карту в комбинации.

5. **Функция `compare_hands(player_rank, player_high_card, computer_rank, computer_high_card)`**:
   - Принимает ранги и старшие карты игрока и компьютера.
   - Сравнивает ранги комбинаций. Если ранги равны, сравнивает старшие карты.
   - Возвращает результат сравнения в виде строки (победа игрока, победа компьютера или ничья).

6. **Функция `play_poker()`**:
   - Создает колоду карт, перемешивает ее, раздает руки игроку и компьютеру.
   - Выводит руки игрока и компьютера на экран.
   - Оценивает руки игрока и компьютера с помощью `evaluate_hand()`.
   - Сравнивает руки с помощью `compare_hands()` и выводит результат игры.

7. **Блок `if __name__ == "__main__":`**:
   - Гарантирует, что функция `play_poker()` будет запущена только при прямом запуске скрипта, а не при его импорте как модуля.
   - Вызывает функцию `play_poker()` для запуска игры.
"""
```