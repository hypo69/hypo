# Анализ кода модуля POKER

**Качество кода**

- **Соответствие требованиям к формату кода (1-10):** 
    -  Документ в формате markdown, что соответствует заданию.
    -  Присутствует подробное описание игры, её правил и процесса.
    -  Есть пошаговая инструкция для реализации игры, пример работы программы и возможные ограничения.
    -  Содержит рекомендации по улучшению и использованию Python.
- **Преимущества:**
    -  Описание игры POKER достаточно подробное и понятное.
    -  Пошаговая инструкция хорошо структурирована и логична.
    -  Пример работы программы помогает понять процесс игры.
    -  Использует markdown для форматирования, что удобно для чтения.
- **Недостатки:**
    -  Нет явного программного кода на Python, только описание алгоритма.
    -  Не хватает конкретных примеров кода для функций и классов.
    -  Не используются reStructuredText для документирования кода, как это требовалось в задании.

**Рекомендации по улучшению**

1.  **Добавить программный код:**
    -  Необходимо добавить реализацию игры на Python с классами, функциями и методами.
    -  Обеспечить соответствие документации в формате reStructuredText (RST).

2.  **Использовать reStructuredText (RST) для документирования:**
    -  Вместо обычного markdown, использовать RST для документирования функций, классов и методов.
    -  Добавить docstrings для каждой функции и метода.

3.  **Добавить обработку ошибок:**
    -  Предусмотреть обработку некорректного ввода от пользователя.
    -  Использовать `logger.error` для логирования ошибок.

4.  **Разбить на модули:**
    -  Разделить код на модули для более удобной разработки и поддержки.
    -  Например, модуль для работы с колодой карт, модуль для оценки комбинаций, модуль для логики игры.

5.  **Использовать `j_loads` или `j_loads_ns`:**
    -  Если требуется загрузка данных из JSON, использовать `j_loads` или `j_loads_ns` из `src.utils.jjson`.

6.  **Реализовать классы и методы:**
    -  Создать классы, такие как `Card`, `Deck`, `Player` и `PokerGame`, для структурирования кода.
    -  Использовать методы для действий, таких как перемешивание колоды, раздача карт, оценка комбинаций.

7.  **Привести примеры документирования в формате RST**:
   - добавить примеры документирования в формате RST для функций и классов.

**Улучшенный код**

```python
"""
Модуль для реализации карточной игры POKER.
=========================================================================================

Этот модуль содержит классы и функции для создания и управления карточной игрой POKER.
Включает в себя логику создания колоды, раздачи карт, оценки комбинаций и управления игровым процессом.

Пример использования
--------------------

Пример использования класса `PokerGame`:

.. code-block:: python

    game = PokerGame()
    game.start_game()
"""

import random
from typing import List, Tuple
from src.logger.logger import logger # Импорт логгера

class Card:
    """
    Представляет карту в колоде.

    :param suit: Масть карты (червы, бубны, трефы, пики).
    :type suit: str
    :param rank: Ранг карты (2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A).
    :type rank: str

    .. attribute:: suit
       :type: str
       Масть карты.

    .. attribute:: rank
       :type: str
       Ранг карты.
    """
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        """Возвращает строковое представление карты (например, '10 червы')."""
        return f"{self.rank} {self.suit}"

    def __repr__(self) -> str:
      """Возвращает строковое представление объекта карты для отладки."""
      return f"Card(suit='{self.suit}', rank='{self.rank}')"


class Deck:
    """
    Представляет колоду карт.

    .. attribute:: cards
       :type: list[Card]
       Список карт в колоде.
    """
    def __init__(self):
        suits = ['червы', 'бубны', 'трефы', 'пики']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        """Перемешивает колоду карт."""
        random.shuffle(self.cards)

    def deal_card(self) -> Card:
        """Раздает одну карту из колоды.

        :raises IndexError: Если колода пуста.
        :return: Карта из колоды.
        :rtype: Card
        """
        if not self.cards:
            logger.error("Колода пуста") #  Логируем ошибку, если колода пуста
            raise IndexError("Колода пуста")
        return self.cards.pop()

    def __len__(self) -> int:
      """Возвращает количество карт в колоде."""
      return len(self.cards)

class Player:
    """
    Представляет игрока в игре.

    :param name: Имя игрока.
    :type name: str

    .. attribute:: name
       :type: str
       Имя игрока.

    .. attribute:: hand
       :type: list[Card]
       Список карт на руках у игрока.

    .. attribute:: score
       :type: int
       Счет игрока.
    """
    def __init__(self, name: str):
        self.name = name
        self.hand: List[Card] = []
        self.score = 0

    def add_card(self, card: Card):
        """Добавляет карту в руку игрока.

        :param card: Карта для добавления.
        :type card: Card
        """
        self.hand.append(card)

    def discard_cards(self, card_indexes: List[int], deck: Deck) -> None:
      """
      Игрок сбрасывает выбранные карты и берёт новые из колоды.
      
      :param card_indexes: Список индексов карт для сброса.
      :type card_indexes: list[int]
      :param deck: Колода карт.
      :type deck: Deck
      
      """
      try:
          new_hand = []
          discarded_cards = []
          for i, card in enumerate(self.hand):
              if i+1 not in card_indexes:
                  new_hand.append(card)
              else:
                discarded_cards.append(card) # сохраняем сбрасываемые карты для отладки
          
          for _ in range(len(discarded_cards)): # добавляем новые карты на место сброшенных
              if len(deck) > 0:
                new_hand.append(deck.deal_card())
              else:
                logger.error('Недостаточно карт в колоде')
                raise IndexError("Недостаточно карт в колоде") # выводим ошибку, если в колоде нет карт
          self.hand = new_hand
      except Exception as ex:
        logger.error(f'Ошибка при сбросе карт {ex}')
        raise

    def show_hand(self) -> str:
      """Возвращает строковое представление руки игрока."""
      return f"{', '.join(map(str, self.hand))}"

class PokerGame:
    """
    Представляет основную логику игры в покер.

    .. attribute:: deck
       :type: Deck
       Колода карт для игры.

    .. attribute:: players
       :type: list[Player]
       Список игроков в игре.

    .. attribute:: rounds_played
       :type: int
       Количество сыгранных раундов.

    .. attribute:: max_rounds
       :type: int
       Максимальное количество раундов.

    .. attribute:: max_score
       :type: int
       Максимальное количество очков для победы.
    """
    def __init__(self, max_rounds: int = 10, max_score: int = 5):
        self.deck = Deck()
        self.players: List[Player] = []
        self.rounds_played = 0
        self.max_rounds = max_rounds
        self.max_score = max_score

    def add_player(self, player: Player):
        """Добавляет нового игрока в игру.

        :param player: Игрок для добавления.
        :type player: Player
        """
        self.players.append(player)

    def deal_initial_hands(self):
      """
      Раздаёт начальные карты всем игрокам.
      
      Каждому игроку раздаётся по 5 карт.
      """
      try:
          for player in self.players:
              player.hand = []
              for _ in range(5):
                if len(self.deck) > 0:
                  player.add_card(self.deck.deal_card())
                else:
                  logger.error("Недостаточно карт в колоде для раздачи")
                  raise IndexError("Недостаточно карт в колоде")
      except Exception as ex:
        logger.error(f'Ошибка при раздаче карт {ex}')
        raise

    def get_player_input(self, player: Player) -> List[int]:
      """
      Получает от игрока номера карт, которые он хочет заменить.

      :param player: Игрок, вводящий данные.
      :type player: Player
      :return: Список индексов карт для замены.
      :rtype: list[int]
      """
      while True:
          try:
              card_indexes_str = input(f"{player.name}, ваши карты: {player.show_hand()}\nВведите номера карт, которые хотите заменить (через запятую): ")
              card_indexes = [int(x.strip()) for x in card_indexes_str.split(',')]
              if all(1 <= index <= 5 for index in card_indexes):
                return card_indexes
              else:
                print("Неверный ввод. Введите номера карт от 1 до 5.") # выводим сообщение, если ввод неверный
          except ValueError:
              print("Неверный ввод. Введите числа через запятую.") # выводим сообщение, если ввод неверный

    def evaluate_hand(self, hand: List[Card]) -> Tuple[str, int]:
      """
      Оценивает комбинацию карт игрока.
      
      :param hand: Рука игрока.
      :type hand: list[Card]
      :return: Комбинация и ее ранг.
      :rtype: tuple[str, int]
      """
      ranks = [card.rank for card in hand]
      suits = [card.suit for card in hand]
      rank_counts = {}
      for rank in ranks:
          rank_counts[rank] = rank_counts.get(rank, 0) + 1
          
      is_flush = len(set(suits)) == 1
      
      rank_values = {
          '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
      }
      numeric_ranks = sorted([rank_values[rank] for rank in ranks])
      is_straight = all(numeric_ranks[i+1] - numeric_ranks[i] == 1 for i in range(4))
      
      if is_flush and is_straight and numeric_ranks == [10, 11, 12, 13, 14]:
          return "Роял-флеш", 10
      if is_flush and is_straight:
          return "Стрит-флеш", 9
      if 4 in rank_counts.values():
          return "Каре", 8
      if 3 in rank_counts.values() and 2 in rank_counts.values():
          return "Фулл-хаус", 7
      if is_flush:
          return "Флеш", 6
      if is_straight:
          return "Стрит", 5
      if 3 in rank_counts.values():
          return "Тройка", 4
      pairs = list(rank_counts.values()).count(2)
      if pairs == 2:
        return "Две пары", 3
      if pairs == 1:
        return "Пара", 2
      return "Старшая карта", 1

    def determine_winner(self) -> Player:
      """
      Определяет победителя раунда.
      
      Сравнивает комбинации карт всех игроков и выбирает победителя.
      Если есть несколько игроков с одинаковой комбинацией, выбирается игрок с самой старшей картой.
      
      :return: Победитель раунда.
      :rtype: Player
      """
      best_hand_value = -1
      winner = None
      
      for player in self.players:
        hand_name, hand_value = self.evaluate_hand(player.hand)
        print(f'{player.name}: {hand_name} ({player.show_hand()})')
        if hand_value > best_hand_value:
            best_hand_value = hand_value
            winner = player
        elif hand_value == best_hand_value: # если комбинация одинакова, выбираем по старшей карте
            if winner:
              current_best_card = max(card.rank for card in winner.hand) # выбираем старшую карту у текущего победителя
              new_player_best_card = max(card.rank for card in player.hand) # выбираем старшую карту у нового игрока
              if new_player_best_card > current_best_card: # сравниваем старшие карты
                winner = player
            else:
              winner = player
      return winner

    def play_round(self):
      """
      Проводит один раунд игры.
      
      Игроки по очереди меняют карты, оцениваются комбинации, определяется победитель раунда.
      """
      self.deck = Deck() # Создаем новую колоду для каждого раунда
      self.deck.shuffle() # Перемешиваем колоду
      self.deal_initial_hands() # Раздаем начальные карты
      
      for player in self.players:
        card_indexes = self.get_player_input(player)
        player.discard_cards(card_indexes, self.deck) # Меняем карты игрока
      
      winner = self.determine_winner()
      winner.score += 1 # Увеличиваем счет победителя
      print(f"Победил {winner.name}!") # Выводим имя победителя
      self.rounds_played += 1 # Увеличиваем счетчик раундов
      print(f"Итоговый счет:")
      for player in self.players:
        print(f'{player.name}: {player.score} очков')

    def start_game(self):
        """Запускает игру в покер."""
        print("Добро пожаловать в POKER!")
        player_names = input("Введите имена игроков (через запятую): ").split(',')
        for name in player_names:
            self.add_player(Player(name.strip()))

        while self.rounds_played < self.max_rounds:
          self.play_round() # Проводим раунд игры
          if any(player.score >= self.max_score for player in self.players): # Проверяем, не выиграл ли кто-то досрочно
              break
          play_again = input("Хотите сыграть снова? (да/нет): ")
          if play_again.lower() != "да":
              break
        
        # Определение окончательного победителя
        final_winner = max(self.players, key=lambda player: player.score) # Находим игрока с самым большим счётом
        print(f"Игра окончена! Победил {final_winner.name} с {final_winner.score} очками.") # Выводим имя победителя


if __name__ == "__main__":
    game = PokerGame()
    game.start_game()
```