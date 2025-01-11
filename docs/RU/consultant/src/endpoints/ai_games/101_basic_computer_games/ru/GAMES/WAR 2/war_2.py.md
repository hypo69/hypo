# Анализ кода модуля war_2.py

**Качество кода: 7/10**

*   **Плюсы:**
    *   Код игры относительно хорошо структурирован и разбит на логические функции.
    *   Есть подробные docstring для каждой функции, что облегчает понимание кода.
    *   Присутствует описание алгоритма игры и блок-схема в комментариях.
    *   Логика игры в целом реализована корректно.
*   **Минусы:**
    *   Используются избыточные комментарии после `#`, которые можно перенести в docstring.
    *   Не используются логирование ошибок через `logger`.
    *   Смешение комментариев, reStructuredText docstrings и обычных комментариев в одном файле.
    *   Нет обработки исключений.
    *   Перемешивание карт в конце раунда выглядит избыточно и не влияет на логику игры.

**Рекомендации по улучшению**

1.  **Улучшить форматирование комментариев:** Перевести все комментарии в формат reStructuredText (RST) и включить их в docstring.
2.  **Добавить логирование:** Внедрить логирование ошибок через `from src.logger.logger import logger` вместо стандартного `try-except`.
3.  **Убрать избыточные комментарии:** Убрать комментарии после `#`, дублирующие информацию из docstring.
4.  **Убрать избыточное перемешивание карт:** Убрать перемешивание карт в конце раунда.
5.  **Обработка ошибок:** Добавить обработку исключений, особенно при работе с колодой карт.

**Оптимизированный код**

```python
"""
Модуль для реализации карточной игры "Война 2"
=========================================================================================

Этот модуль содержит функции для создания, раздачи, и игры в карточную игру "Война 2"
между двумя игроками.

Правила игры
-------------
1.  Стандартная колода из 52 карт делится поровну между двумя игроками.
2.  Каждый игрок одновременно выкладывает верхнюю карту из своей колоды.
3.  Игрок с более старшей картой забирает обе карты и добавляет их в конец своей колоды.
4.  Если карты равны, объявляется "война":
    4.1. Каждый игрок выкладывает три карты рубашкой вверх.
    4.2. Каждый игрок выкладывает еще по одной карте открытой.
    4.3. Игрок с более старшей открытой картой забирает все карты (включая карты войны).
    4.4. Если открытые карты снова равны, война повторяется.
5.  Игра продолжается до тех пор, пока один из игроков не соберет все карты.
6.  Масти в игре не учитываются, только ранг карт (2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A).

Пример использования
--------------------

.. code-block:: python

    play_war()
"""
import random
from src.logger.logger import logger

def create_deck() -> list[str]:
    """
    Создает стандартную колоду из 52 карт.

    :return: Список строк, представляющих карты.
    :rtype: list[str]
    """
    suits = ["C", "D", "H", "S"]  # Масти: Clubs, Diamonds, Hearts, Spades
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = [rank + suit for suit in suits for rank in ranks] # генерируем колоду
    return deck


def deal_cards(deck: list[str]) -> tuple[list[str], list[str]]:
    """
    Раздает карты двум игрокам.

    :param deck: Колода карт.
    :type deck: list[str]
    :return: Кортеж из двух списков, представляющих карты каждого игрока.
    :rtype: tuple[list[str], list[str]]
    """
    random.shuffle(deck) # перемешиваем колоду
    player_a = deck[:len(deck) // 2] # раздаем половину карт первому игроку
    player_b = deck[len(deck) // 2:] # раздаем вторую половину карт второму игроку
    return player_a, player_b


def get_card_value(card: str) -> int:
    """
    Возвращает числовое значение карты (без учета масти).

    :param card: Строка, представляющая карту.
    :type card: str
    :return: Числовое значение карты.
    :rtype: int
    """
    rank = card[:-1]  # получаем ранг карты, отбрасывая масть
    if rank.isdigit(): # если ранг это число
        return int(rank) # возвращаем числовое значение ранга
    elif rank == "J":   # если ранг валет
        return 11       # возвращаем 11
    elif rank == "Q":   # если ранг дама
        return 12       # возвращаем 12
    elif rank == "K":   # если ранг король
        return 13       # возвращаем 13
    elif rank == "A":   # если ранг туз
        return 14       # возвращаем 14
    return 0


def war(player_a: list[str], player_b: list[str], cards_on_table: list[str]) -> tuple[bool, bool, list[str], list[str], list[str]]:
    """
    Реализует логику "войны" в игре.

    :param player_a: Карты первого игрока.
    :type player_a: list[str]
    :param player_b: Карты второго игрока.
    :type player_b: list[str]
    :param cards_on_table: Карты на столе.
    :type cards_on_table: list[str]
    :return: Кортеж значений (a_win_war, b_win_war, cards_on_table, player_a, player_b), где
             a_win_war - True, если у игрока A не хватило карт, False иначе,
             b_win_war - True, если у игрока B не хватило карт, False иначе,
             cards_on_table - список оставшихся карт на столе,
             player_a - обновленный список карт игрока A,
             player_b - обновленный список карт игрока B.
    :rtype: tuple[bool, bool, list[str], list[str], list[str]]
    """
    while True:
         # Проверяем, есть ли у игроков достаточно карт для войны
        if len(player_a) < 4: # если у игрока А меньше 4 карт
            return True,False,cards_on_table,player_a, player_b # возвращаем, что игрок B победил, и карты
        if len(player_b) < 4: # если у игрока B меньше 4 карт
           return False,True, cards_on_table,player_a, player_b # возвращаем, что игрок A победил, и карты

        # Забираем карты для войны
        war_cards_a = player_a[:4] # первые 4 карты игрока А
        war_cards_b = player_b[:4] # первые 4 карты игрока B
        player_a = player_a[4:]    # удаляем первые 4 карты из колоды игрока A
        player_b = player_b[4:]    # удаляем первые 4 карты из колоды игрока B
        cards_on_table.extend(war_cards_a) # добавляем карты игрока А на стол
        cards_on_table.extend(war_cards_b) # добавляем карты игрока B на стол

        # Сравниваем открытые карты
        card_a_value = get_card_value(war_cards_a[-1]) # получаем значение последней карты игрока А
        card_b_value = get_card_value(war_cards_b[-1]) # получаем значение последней карты игрока B

        if card_a_value > card_b_value: # если карта игрока А старше
            player_a.extend(cards_on_table) # игрок А забирает все карты со стола
            return False,False,[],player_a, player_b  # возвращаем, что война закончилась, игрок A победил
        elif card_b_value > card_a_value: # если карта игрока B старше
            player_b.extend(cards_on_table) # игрок B забирает все карты со стола
            return False,False,[],player_a, player_b # возвращаем, что война закончилась, игрок B победил
        # если карты равны - повторяем войну


def play_war() -> None:
    """
    Основная логика игры в войну.
    """
    deck = create_deck()  # Создаем колоду
    player_a, player_b = deal_cards(deck) # раздаем карты

    round_number = 0 # счетчик раундов
    while player_a and player_b: # пока у обоих игроков есть карты
        round_number += 1 # увеличиваем счетчик раундов
        print(f"Раунд {round_number}. Карты игрока A: {len(player_a)}, Карты игрока B: {len(player_b)}")
        try:
             card_a = player_a.pop(0) # берем карту из колоды игрока А
             card_b = player_b.pop(0) # берем карту из колоды игрока B
        except IndexError as ex:
            logger.error(f'Ошибка при извлечении карты {ex}')
            break
        cards_on_table = [card_a, card_b] # карты на столе

        card_a_value = get_card_value(card_a) # получаем значение карты игрока А
        card_b_value = get_card_value(card_b) # получаем значение карты игрока B

        if card_a_value > card_b_value: # если карта игрока А старше
            player_a.extend(cards_on_table) # игрок А забирает карты
        elif card_b_value > card_a_value: # если карта игрока B старше
            player_b.extend(cards_on_table) # игрок B забирает карты
        else:  # если карты равны, начинаем войну
            a_win_war, b_win_war ,cards_on_table,player_a, player_b = war(player_a, player_b, cards_on_table) # запускаем войну
            if a_win_war == True: # если у игрока А не хватило карт
                print ("Игрок B победил в войне")
                break # выходим из цикла
            elif b_win_war == True: # если у игрока B не хватило карт
                print ("Игрок A победил в войне")
                break # выходим из цикла
        # для красоты, перемешиваем карты в конце каждой руки
        # random.shuffle(player_a)  # убираем избыточное перемешивание
        # random.shuffle(player_b)  # убираем избыточное перемешивание


    if not player_a: # если у игрока А нет карт
        print("Игрок B выиграл игру!") # выводим сообщение о победе игрока B
    elif not player_b: # если у игрока B нет карт
        print("Игрок A выиграл игру!") # выводим сообщение о победе игрока A


if __name__ == "__main__":
    play_war()
```