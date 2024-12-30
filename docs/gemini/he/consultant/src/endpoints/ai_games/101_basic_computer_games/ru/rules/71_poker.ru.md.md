# Анализ кода модуля `71_poker.ru.md`

**Качество кода**
* Соответствие требованиям к формату кода (1-10): 7
    * Преимущества:
        *  Текст хорошо структурирован и понятен.
        *  Присутствует подробное описание шагов реализации игры в покер.
        *  Представлены примеры работы программы.
    * Недостатки:
        *  Формат кода не соответствует требованиям, поскольку отсутствует код на Python.
        *  В тексте нет использования reStructuredText (RST) для документации.
        *  Не хватает детального описания реализации на Python, только общие рекомендации.
        *  Отсутствуют импорты, которые нужно было бы добавить.
        *  Нет примеров использования `j_loads` или `j_loads_ns`.
        *  Нет использования `logger.error` для обработки ошибок.
        *  Нет docstring и аннотаций типов.

**Рекомендации по улучшению**

1.  **Преобразование в формат Python:**
    *   Необходимо создать Python-скрипт на основе предоставленного описания игры.
    *   Включать в него функции для создания колоды, раздачи карт, оценки комбинаций и т.д.
2.  **Документация в формате reStructuredText (RST):**
    *   Добавить docstring в формате RST для модуля, функций и методов.
    *   Использовать RST для всех комментариев и документации.
3.  **Обработка ошибок:**
    *   Использовать `logger.error` для обработки ошибок.
    *   Избегать чрезмерного использования `try-except` блоков.
4.  **Импорты:**
    *   Добавить необходимые импорты (например, `random`, `src.utils.jjson`, `src.logger.logger`).
5.  **Адаптация к предыдущим файлам:**
    *   Использовать соглашения об именах, принятые в предыдущих файлах.
6.  **Улучшения:**
    *   Добавить возможность ставок.
    *   Реализовать режим игры с компьютером.
    *   Добавить графический интерфейс.

**Улучшенный код**

```python
"""
Модуль для реализации игры в покер.
=========================================================================================

Модуль содержит функции для создания колоды, раздачи карт, оценки комбинаций,
и управления игровым процессом.

Пример использования:
--------------------

Пример запуска игры:

.. code-block:: python

    game = PokerGame()
    game.start_game()
"""
import random # Импорт модуля random для перемешивания карт #
from typing import List, Tuple # Импорт типов для аннотации #
from src.logger.logger import logger # Импорт логера для обработки ошибок #
from src.utils.jjson import j_loads_ns # Импорт для загрузки JSON #


class Card:
    """
    Представляет игральную карту.

    :param suit: Масть карты.
    :type suit: str
    :param rank: Достоинство карты.
    :type rank: str
    """
    def __init__(self, suit: str, rank: str):
        """
        Инициализирует карту.
        """
        self.suit = suit # Устанавливает масть карты #
        self.rank = rank # Устанавливает достоинство карты #

    def __str__(self) -> str:
        """
        Возвращает строковое представление карты.

        :return: Строковое представление карты.
        :rtype: str
        """
        return f"{self.rank} {self.suit}" # Возвращает строку в формате "достоинство масть" #


class PokerGame:
    """
    Класс для управления игрой в покер.
    """
    def __init__(self):
        """
        Инициализирует игру.
        """
        self.suits = ["червы", "бубны", "трефы", "пики"] # Список мастей #
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] # Список достоинств #
        self.deck = self._create_deck() # Создаем колоду #
        self.players = [] # Инициализируем список игроков #

    def _create_deck(self) -> List[Card]:
         """
         Создает колоду из 52 карт.

         :return: Колода карт.
         :rtype: List[Card]
         """
         deck = [] # Создаем пустой список для колоды #
         for suit in self.suits: # Проходим по всем мастям #
             for rank in self.ranks: # Проходим по всем достоинствам #
                 deck.append(Card(suit, rank)) # Добавляем карту в колоду #
         return deck # Возвращаем колоду #

    def _shuffle_deck(self) -> None:
        """
        Перемешивает колоду.
        """
        random.shuffle(self.deck) # Перемешиваем колоду #

    def _deal_cards(self, num_players: int) -> List[List[Card]]:
        """
        Раздает карты игрокам.

        :param num_players: Количество игроков.
        :type num_players: int
        :return: Список карт для каждого игрока.
        :rtype: List[List[Card]]
        """
        hands = [[] for _ in range(num_players)] # Создаем пустые руки для каждого игрока #
        for _ in range(5): # Раздаем по 5 карт каждому игроку #
            for i in range(num_players): # Проходим по каждому игроку #
                try:
                    hands[i].append(self.deck.pop()) # Раздаем карту игроку #
                except IndexError as ex:
                    logger.error("Недостаточно карт в колоде", ex) # Логируем ошибку если в колоде недостаточно карт #
                    return [] # Возвращаем пустой список если произошла ошибка #
        return hands # Возвращаем список рук #


    def _evaluate_hand(self, hand: List[Card]) -> Tuple[str, int]:
        """
        Оценивает комбинацию карт.

        :param hand: Рука игрока.
        :type hand: List[Card]
        :return: Комбинация и её ранг.
        :rtype: Tuple[str, int]
        """
        ranks = [card.rank for card in hand] # Получаем список достоинств карт #
        suits = [card.suit for card in hand] # Получаем список мастей карт #
        rank_counts = {} # Словарь для подсчета количества одинаковых достоинств #
        for rank in ranks: # Проходим по всем достоинствам #
            rank_counts[rank] = rank_counts.get(rank, 0) + 1 # Подсчитываем количество карт каждого достоинства #
        sorted_ranks = sorted([self.ranks.index(rank) for rank in ranks]) # Сортируем индексы достоинств #
        is_flush = len(set(suits)) == 1 # Проверяем на флеш (все карты одной масти) #
        is_straight = all(sorted_ranks[i+1] - sorted_ranks[i] == 1 for i in range(len(sorted_ranks)-1)) # Проверяем на стрит (последовательные значения) #
        if is_flush and is_straight and sorted_ranks[0] == 8:
            return "Роял-флэш", 10 # Роял-флеш #
        if is_flush and is_straight:
            return "Стрит-флэш", 9 # Стрит-флеш #
        if 4 in rank_counts.values():
            return "Каре", 8 # Каре #
        if 3 in rank_counts.values() and 2 in rank_counts.values():
            return "Фулл-хаус", 7 # Фулл-хаус #
        if is_flush:
            return "Флэш", 6 # Флэш #
        if is_straight:
             return "Стрит", 5 # Стрит #
        if 3 in rank_counts.values():
            return "Тройка", 4 # Тройка #
        pairs = list(rank_counts.values()).count(2) # Подсчитываем количество пар #
        if pairs == 2:
            return "Две пары", 3 # Две пары #
        if pairs == 1:
            return "Пара", 2 # Пара #
        return "Старшая карта", 1 # Старшая карта #

    def start_game(self):
        """
        Запускает игровой процесс.
        """
        print("Добро пожаловать в POKER!") # Приветствие #
        num_players = 2 # Устанавливаем количество игроков #
        self.players = [input(f"Игрок {i+1}, введите ваше имя: ") for i in range(num_players)] # Запрашиваем имена игроков #
        max_score = 5 # Максимальное количество очков для победы #
        player_scores = {player: 0 for player in self.players} # Инициализация очков игроков #
        round_num = 1 # Счетчик раундов #

        while max(player_scores.values()) < max_score: # Пока никто не набрал нужное кол-во очков #
             print(f"\nРаунд {round_num}")
             self.deck = self._create_deck() # Создаем колоду для раунда #
             self._shuffle_deck() # Перемешиваем колоду #
             hands = self._deal_cards(num_players) # Раздаем карты игрокам #
             if not hands:
                return # Завершаем игру, если не удалось раздать карты #
             for i, player in enumerate(self.players): # Проходим по каждому игроку #
                print(f"\n{player}, ваши карты:") # Выводим карты игрока #
                for j, card in enumerate(hands[i]): # Выводим карты #
                    print(f"{j+1}. {card}")
                while True:
                     try:
                        cards_to_replace = input("Введите номера карт, которые хотите заменить (через запятую): ") # Запрос номеров карт на замену #
                        cards_to_replace_list = [int(x.strip()) - 1 for x in cards_to_replace.split(',')] # Получаем список индексов карт на замену #
                        if all(0 <= index < 5 for index in cards_to_replace_list):
                             break # Выходим из цикла, если ввод корректен #
                        else:
                             print("Неверный ввод. Пожалуйста, введите номера карт от 1 до 5.")
                     except (ValueError, IndexError) as ex:
                         logger.error("Неверный ввод, введите номера карт через запятую", ex)
                         print("Неверный ввод. Пожалуйста, введите корректные номера карт.")

                for index in sorted(cards_to_replace_list, reverse=True):
                    if self.deck:
                      try:
                           hands[i][index] = self.deck.pop() # Заменяем карты #
                      except IndexError as ex:
                           logger.error("Недостаточно карт в колоде", ex) # Логируем ошибку если в колоде недостаточно карт #
                           return # Завершаем игру, если не удалось раздать карты #
                    else:
                         print("Недостаточно карт в колоде.")
                         return

                print("Ваши новые карты:") # Выводим новые карты #
                for j, card in enumerate(hands[i]): # Выводим новые карты #
                    print(f"{j+1}. {card}") #

             player_combinations = {} # Словарь для комбинаций игроков #
             for i, player in enumerate(self.players): # Проходим по каждому игроку #
                 combination, _ = self._evaluate_hand(hands[i]) # Оцениваем комбинацию #
                 print(f"\n{player}: {combination}") # Выводим комбинацию #
                 player_combinations[player] = (combination, _)  # Сохраняем комбинацию и ее ранг #

             winner = self._determine_winner(player_combinations) # Определяем победителя раунда #
             print(f"\nПобедил {winner}!")
             player_scores[winner] += 1 # Обновляем очки победителя #
             print("\nИтоговый счёт:") # Выводим счет #
             for player, score in player_scores.items(): # Проходим по всем игрокам #
                 print(f"{player}: {score} очка") # Выводим счет #
             round_num += 1 # Увеличиваем счетчик раундов #
        print(f"\nИгра окончена! Победил {max(player_scores, key=player_scores.get)} с {max(player_scores.values())} очками.") # Выводим победителя игры #
        play_again = input("Хотите сыграть снова? (да/нет): ") # Предлагаем сыграть снова #
        if play_again.lower() == 'да': # Если игрок хочет сыграть еще раз #
            self.start_game()  # Начинаем игру заново #
        else:
            print("Спасибо за игру!") # Выводим сообщение #

    def _determine_winner(self, player_combinations: dict) -> str:
        """
        Определяет победителя раунда.

        :param player_combinations: Словарь комбинаций игроков.
        :type player_combinations: dict
        :return: Имя победителя.
        :rtype: str
        """
        best_player = None # Переменная для имени лучшего игрока #
        best_rank = 0 # Переменная для ранга лучшей комбинации #

        for player, (combination, rank) in player_combinations.items(): # Проходим по каждому игроку #
            if rank > best_rank: # Если текущий ранг больше лучшего ранга #
                 best_rank = rank # Обновляем лучший ранг #
                 best_player = player  # Обновляем лучшего игрока #
        return best_player # Возвращаем лучшего игрока #

if __name__ == "__main__": # Запускаем игру если скрипт запустился напрямую #
    game = PokerGame()
    game.start_game()
```