# Анализ кода модуля `13_blkjak.ru.md`

**Качество кода**

- Соответствие требованиям к формату кода (1-10): 8

  -  **Преимущества:**
    - Документ содержит подробное описание правил игры в блэкджек, а также пошаговую инструкцию по реализации.
    - Примеры работы программы и возможные ограничения делают документ понятным для пользователя.
    - Документ написан на русском языке, что соответствует заданию.
  -  **Недостатки:**
    -   Не хватает структурного форматирования.
    -   Не хватает описания кода.
    -   Отсутствует какой-либо код.
    -   Файл `.md` не содержит кода Python, поэтому невозможно оценить его соответствие требованиям по форматированию, обработке данных, анализу структуры, рефакторингу, документации и пр.

**Рекомендации по улучшению**

1.  **Структурирование документа:**
    - Добавить заголовки более высокого уровня для разделения разделов (например, "# Описание игры", "## Инструкция по реализации", "## Пример игры" и т.д.).
    - Использовать более четкое форматирование списков и примеров кода.
2.  **Добавление кода:**
    - Реализовать логику игры в блэкджек на Python, следуя пошаговой инструкции.
    - Код должен быть снабжен комментариями в формате RST, которые объясняют каждую функцию и ее назначение.
    -  Необходимо добавить в код обработку ошибок с использованием `logger.error`.
3. **Документация кода:**
    -   Добавить документацию в формате reStructuredText (RST) для всех модулей, функций, методов и переменных.
    -   Включить примеры использования кода.

**Улучшенный код**

```markdown
# Игра: **BLKJAK** (Блэкджек)

## Описание игры

Игра "BLKJAK" является симуляцией игры в блэкджек (или 21) в стиле Лас-Вегаса. Игрок играет против дилера, с целью набрать сумму очков на своих картах, максимально близкую к 21, но не превышающую эту цифру. Если у игрока или дилера выпадает блэкджек (21 очко с двумя картами), игра заканчивается, и победитель определяется сразу. В игре доступны следующие особенности:
- Разделение карт на два набора при наличии двух одинаковых карт.
- Возможность сделать страховку при открытой карте дилера — туза.
- Лимит ставки в $500.

---

## Инструкция по реализации

### 1. Инициализация игры
   - Компьютер раздает две карты игроку и одну карту дилеру (с открытой картой).
   - Игрок делает начальную ставку.
   - В начале игры игрок может запросить страховку, если у дилера есть открытая карта — туз.

### 2. Основной цикл игры
   - **Ход игрока:**
     1. Игрок смотрит на свои карты и решает, хочет ли он:
        - Взять ещё одну карту (HIT).
        - Прекратить брать карты и остаться с текущей суммой очков (STAY).
        - Разделить пары карт и играть двумя руками, если начальная рука состоит из двух одинаковых карт (SPLIT).
        - Удвое увеличить ставку и получить одну дополнительную карту (DOUBLE).
     2. Игрок не может набрать больше 21 очка (если он набрал больше — проигрывает).
   
   - **Ход дилера:**
     1. Дилер открывает свою вторую карту.
     2. Если сумма очков дилера составляет 16 или меньше, дилер берет карту. Если сумма 17 или больше — он стоит.
     3. Если дилер превышает 21 очко, он теряет, и игрок выигрывает.
   
### 3. Подсчёт победителя
   - После хода дилера, если его сумма карт больше 21, игрок выигрывает.
   - Если у игрока больше очков, но меньше 22, чем у дилера, игрок выигрывает.
   - Если сумма очков у игрока и дилера одинаковая, игра считается ничьей.

### 4. Завершение игры
   - После завершения игры, игроку предлагается сыграть снова или выйти.
     ```
     Хотите сыграть ещё раз? (да/нет)
     ```

---

## Пример работы программы

### 1. Начало игры:
   ```
   Добро пожаловать в блэкджек!
   У вас есть $200. Сколько вы хотите поставить?
   > 50
   Ваши карты: 10, 7 (Сумма: 17)
   Карта дилера: туз
   Хотите сделать страховку? (да/нет)
   > да
   ```

### 2. Ход игрока:
   ```
   Ваши карты: 10, 7 (Сумма: 17)
   Карта дилера: туз
   Хотите взять карту? (да/нет)
   > нет
   ```

### 3. Ход дилера:
   ```
   Дилер берет карту... Дилер показывает карты: туз, 6 (Сумма: 17)
   Дилер берет еще одну карту... Дилер показывает карты: туз, 6, 9 (Сумма: 16)
   Дилер берет еще одну карту... Дилер показывает карты: туз, 6, 9, 10 (Сумма: 25)
   Дилер перебрал. Вы выигрываете!
   Ваш баланс: $250
   ```

### 4. Вывод результата:
   ```
   Хотите сыграть снова? (да/нет)
   > нет
   До свидания!
   ```

---

## Возможные ограничения
- Игрок не может поставить больше, чем у него есть на счёте.
- Страховка может быть куплена только в случае, если у дилера открыта карта — туз.
- Все ставки ограничены суммой $500.

---

## Реализация
Игра реализована с помощью базовых принципов игры в блэкджек, где карты генерируются случайным образом, а игровой процесс управляется через простое взаимодействие с игроком.

```python
"""
Модуль для игры в блэкджек.
=========================================================================================

Этот модуль реализует игру в блэкджек с возможностью разделения карт, страховки и ограничением ставок.

Пример использования
--------------------

.. code-block:: python

    game = Blackjack()
    game.play()
"""

import random
from src.logger.logger import logger # Импортируем logger для обработки ошибок

class Card:
    """
    Класс, представляющий игральную карту.
    
    :ivar suit: Масть карты.
    :vartype suit: str
    :ivar value: Значение карты.
    :vartype value: str or int
    """
    def __init__(self, suit: str, value: str or int):
        """
        Инициализирует карту.

        :param suit: Масть карты.
        :type suit: str
        :param value: Значение карты.
        :type value: str or int
        """
        self.suit = suit
        self.value = value

    def __str__(self) -> str:
        """
        Возвращает строковое представление карты.

        :return: Строковое представление карты.
        :rtype: str
        """
        return f'{self.value} {self.suit}'

class Deck:
    """
    Класс, представляющий колоду карт.

    :ivar cards: Список карт в колоде.
    :vartype cards: list[Card]
    """
    def __init__(self):
        """
        Инициализирует колоду карт.
        """
        suits = ['♥', '♦', '♣', '♠']
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, value) for suit in suits for value in values]
        random.shuffle(self.cards)

    def deal_card(self) -> Card:
        """
        Выдает карту из колоды.

        :return: Карта из колоды.
        :rtype: Card
        """
        if not self.cards:
            logger.error('Колода пуста') # Обработка случая пустой колоды
            return None
        return self.cards.pop()

class Player:
    """
    Класс, представляющий игрока.

    :ivar name: Имя игрока.
    :vartype name: str
    :ivar hand: Список карт в руке игрока.
    :vartype hand: list[Card]
    :ivar balance: Баланс игрока.
    :vartype balance: int
    """
    def __init__(self, name: str, balance: int = 100):
        """
        Инициализирует игрока.

        :param name: Имя игрока.
        :type name: str
        :param balance: Баланс игрока.
        :type balance: int
        """
        self.name = name
        self.hand = []
        self.balance = balance

    def add_card(self, card: Card):
        """
        Добавляет карту в руку игрока.

        :param card: Карта для добавления.
        :type card: Card
        """
        self.hand.append(card)

    def get_hand_value(self) -> int:
        """
        Вычисляет общую сумму очков в руке игрока.

        :return: Сумма очков в руке.
        :rtype: int
        """
        value = 0
        aces = 0
        for card in self.hand:
            if isinstance(card.value, int):
                value += card.value
            elif card.value in ['J', 'Q', 'K']:
                value += 10
            elif card.value == 'A':
                aces += 1
                value += 11

        while value > 21 and aces > 0:
            value -= 10
            aces -= 1
        return value

    def clear_hand(self):
        """
        Очищает руку игрока.
        """
        self.hand = []

class Dealer(Player):
    """
    Класс, представляющий дилера.

    Наследует от класса Player и не имеет дополнительных атрибутов или методов.
    """
    def __init__(self):
       """
       Инициализирует дилера с именем "Дилер" и балансом 0
       """
       super().__init__("Дилер",0) # Вызываем конструктор родительского класса с именем "Дилер" и балансом 0

class Blackjack:
    """
    Класс, представляющий игру в блэкджек.

    :ivar player: Игрок.
    :vartype player: Player
    :ivar dealer: Дилер.
    :vartype dealer: Dealer
    :ivar deck: Колода карт.
    :vartype deck: Deck
    :ivar bet: Текущая ставка.
    :vartype bet: int
    """
    def __init__(self):
        """
        Инициализирует игру в блэкджек.
        """
        self.player = Player('Игрок')
        self.dealer = Dealer()
        self.deck = Deck()
        self.bet = 0

    def make_bet(self):
        """
        Запрашивает ставку у игрока.
        """
        while True:
            try:
                bet = int(input(f'У вас есть ${self.player.balance}. Сколько вы хотите поставить? '))
                if 0 < bet <= self.player.balance and bet <= 500: # проверка на допустимую ставку
                  self.bet = bet
                  return
                else:
                   print("Недопустимая ставка. Пожалуйста, введите корректную ставку") # Сообщение об ошибке ввода
            except ValueError as e:
                logger.error(f"Ошибка ввода ставки: {e}", exc_info=True) # Записываем ошибку в лог
                print("Некорректный ввод. Пожалуйста, введите число.") # Сообщение об ошибке ввода

    def deal_initial_cards(self):
        """
        Раздает начальные карты игроку и дилеру.
        """
        self.player.add_card(self.deck.deal_card())
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())

    def offer_insurance(self):
        """
        Предлагает страховку игроку, если у дилера открыта карта — туз.
        """
        if self.dealer.hand[0].value == 'A':
           while True:
              insurance = input("Хотите сделать страховку? (да/нет) ").lower()
              if insurance in ['да','нет']:
                 if insurance == 'да':
                     insurance_bet = self.bet // 2 # страховка 50% от ставки
                     if self.player.balance >= insurance_bet: # если баланс позволяет сделать страховку
                         self.player.balance -= insurance_bet
                         if self.dealer.get_hand_value() == 21: # если у дилера блекджек
                             self.player.balance += insurance_bet * 3  # выигрыш по страховке
                             print(f'У дилера блэкджек! Ваша страховка сыграла.')
                             return True
                         else:
                           print('У дилера нет блэкджека, страховка не сыграла.')
                           return False
                     else:
                        print('Недостаточно средств для страховки.')
                        return False
                 return False
              else:
                  print('Пожалуйста, введите "да" или "нет".')
        return False # Если у дилера не туз, страховка не предлагается

    def player_turn(self):
        """
        Обрабатывает ход игрока.
        """
        while True:
            print(f'Ваши карты: {", ".join(str(card) for card in self.player.hand)} (Сумма: {self.player.get_hand_value()})')
            print(f'Карта дилера: {self.dealer.hand[0]}') # Показываем открытую карту дилера
            if self.player.get_hand_value() > 21: # Если игрок перебрал, игра заканчивается
                print('У вас перебор!')
                return
            action = input('Хотите взять карту (HIT), остаться (STAY), разделить (SPLIT) или удвоить (DOUBLE)? ').lower()

            if action == 'hit':
                card = self.deck.deal_card()
                if card:
                    self.player.add_card(card)
                else:
                  return # колода пуста
            elif action == 'stay':
                return
            elif action == 'split' and len(self.player.hand) == 2 and self.player.hand[0].value == self.player.hand[1].value: # Если карты одинаковые, можно разделить
                self.split_hand()
            elif action == 'double':
                self.double_down()
                return
            else:
                print("Некорректный ввод. Пожалуйста, выберите одно из действий: HIT, STAY, SPLIT или DOUBLE")

    def split_hand(self):
        """
        Разделяет руку игрока на две, если это возможно.
        """
        if len(self.player.hand) == 2 and self.player.hand[0].value == self.player.hand[1].value and self.player.balance >= self.bet: # Проверка возможности разделения
            self.player.balance -= self.bet # Списываем ставку за вторую руку
            hand1 = [self.player.hand[0]]
            hand2 = [self.player.hand[1]]
            self.player.clear_hand() # Очищаем старую руку
            self.player.hand = hand1
            card = self.deck.deal_card()
            if card:
               self.player.add_card(card)
            else:
                return  # колода пуста
            self.player.hand.append(hand2[0])
            card = self.deck.deal_card()
            if card:
              self.player.add_card(card)
            else:
                return # колода пуста
            print("Карты разделены на две руки.")
        else:
             print('Разделение невозможно.')

    def double_down(self):
        """
        Удваивает ставку и дает игроку одну дополнительную карту.
        """
        if self.player.balance >= self.bet:
            self.player.balance -= self.bet
            self.bet *= 2
            card = self.deck.deal_card()
            if card:
              self.player.add_card(card)
            else:
                return # колода пуста
            print(f'Удвоили ставку. Ваша карта: {self.player.hand[-1]}')
        else:
            print('Недостаточно средств для удвоения.')


    def dealer_turn(self):
        """
        Обрабатывает ход дилера.
        """
        print("Ход дилера...")
        while self.dealer.get_hand_value() < 17:
            card = self.deck.deal_card()
            if card:
                self.dealer.add_card(card)
                print(f'Дилер берет карту... Дилер показывает карты: {", ".join(str(card) for card in self.dealer.hand)} (Сумма: {self.dealer.get_hand_value()})')
            else:
                return # колода пуста
        print(f'Дилер показывает карты: {", ".join(str(card) for card in self.dealer.hand)} (Сумма: {self.dealer.get_hand_value()})')

    def determine_winner(self):
      """
      Определяет победителя.
      """
      player_value = self.player.get_hand_value()
      dealer_value = self.dealer.get_hand_value()
      if player_value > 21:
        print('Дилер выигрывает, вы проиграли!')
        self.player.balance -= self.bet
      elif dealer_value > 21 or player_value > dealer_value:
          print('Вы выиграли!')
          self.player.balance += self.bet
      elif player_value == dealer_value:
          print('Ничья!')
      else:
          print('Дилер выигрывает, вы проиграли!')
          self.player.balance -= self.bet

    def play_again(self) -> bool:
      """
      Запрашивает у пользователя желание сыграть еще раз.

      :return: True, если игрок хочет сыграть снова, False в противном случае.
      :rtype: bool
      """
      while True:
        play_again = input("Хотите сыграть снова? (да/нет) ").lower()
        if play_again in ['да','нет']:
            return play_again == 'да'
        else:
            print("Пожалуйста, введите 'да' или 'нет'.") # Сообщение об ошибке ввода

    def play(self):
        """
        Запускает игровой процесс.
        """
        print('Добро пожаловать в блэкджек!')
        while True:
            self.player.clear_hand()
            self.dealer.clear_hand()
            self.deck = Deck()
            self.make_bet()
            self.deal_initial_cards()
            if self.offer_insurance(): # Предлагаем страховку
                if self.play_again():
                    continue # играем еще раз
                else:
                     break # игра заканчивается
            self.player_turn()
            if self.player.get_hand_value() > 21:
                 self.determine_winner()
            else:
                 self.dealer_turn()
                 self.determine_winner()
            print(f"Ваш баланс: ${self.player.balance}")
            if not self.play_again():
                break
        print('До свидания!')

if __name__ == '__main__':
    game = Blackjack()
    game.play()
```