# Анализ кода модуля `war_2.py`

**Качество кода**
- **Соблюдение требований к формату кода (1-10):**
  - **Преимущества:**
        - Код хорошо структурирован и разбит на функции, что облегчает чтение и понимание.
        - Есть подробное описание логики игры в комментариях.
        - Присутствует базовая документация в формате docstring, хотя требуется ее доработка.
  - **Недостатки:**
        - Не используется reStructuredText (RST) для docstring.
        - Не используются `j_loads` или `j_loads_ns` для загрузки данных (в данном случае это не требуется, но стоит отметить для будущего).
        - Отсутствует импорт логгера и обработка ошибок через `logger.error`.
        - Есть избыточное использование комментариев в конце строк.
        - Не везде имена функций и переменных соответствуют ранее обработанным файлам (не критично, но желательно).

**Рекомендации по улучшению**
1. **Формат docstring:**
   - Заменить существующие docstring на формат RST.
   - Добавить более подробные описания параметров и возвращаемых значений в docstring.
2. **Импорт и логирование:**
   - Добавить импорт логгера: `from src.logger.logger import logger`.
   - Заменить использование `print` на `logger.info` для вывода сообщений, а для ошибок использовать `logger.error`.
3. **Комментарии:**
   - Улучшить комментарии, избегая фраз вроде "код выполняет", "мы получаем".
   - Комментарии должны описывать, что происходит в коде, а не пересказывать его.
   - Убрать избыточные комментарии в конце строк, если они не несут дополнительной информации.
4. **Структура кода:**
   - Проверить имена функций и переменных на соответствие ранее обработанным файлам.
   - Разбить длинные функции на более мелкие, если это улучшит читаемость.

**Улучшенный код**
```python
"""
Модуль для реализации карточной игры "Война 2"
=================================================

Этот модуль содержит функции и логику для игры в "Войну 2" между двумя игроками.
Игра состоит в сравнении карт, и игрок с более старшей картой забирает карты.
Если карты равны, начинается "война".

Пример использования:
---------------------
    
    .. code-block:: python

        if __name__ == "__main__":
            play_war()
"""

import random
from src.logger.logger import logger # импорт логгера

def create_deck():
    """
    Создает стандартную колоду из 52 карт.

    :return: Список строк, представляющих колоду карт.
    :rtype: list[str]
    """
    suits = ['C', 'D', 'H', 'S']  # Масти: Clubs, Diamonds, Hearts, Spades
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [rank + suit for suit in suits for rank in ranks] # генерируем колоду
    return deck

def deal_cards(deck):
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

def get_card_value(card):
    """
    Возвращает числовое значение карты (без учета масти).

    :param card: Строка, представляющая карту.
    :type card: str
    :return: Числовое значение карты.
    :rtype: int
    """
    rank = card[:-1]  # получаем ранг карты, отбрасывая масть
    if rank.isdigit():  # если ранг это число
        return int(rank)  # возвращаем числовое значение ранга
    elif rank == 'J':    # если ранг валет
        return 11        # возвращаем 11
    elif rank == 'Q':    # если ранг дама
        return 12        # возвращаем 12
    elif rank == 'K':    # если ранг король
        return 13        # возвращаем 13
    elif rank == 'A':    # если ранг туз
        return 14        # возвращаем 14
    return 0

def war(player_a, player_b, cards_on_table):
    """
    Реализует процесс "войны" в игре.

    :param player_a: Список карт первого игрока.
    :type player_a: list[str]
    :param player_b: Список карт второго игрока.
    :type player_b: list[str]
    :param cards_on_table: Список карт на столе.
    :type cards_on_table: list[str]
    :return: Кортеж, содержащий флаги победы, карты на столе и обновленные колоды игроков.
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
            return False,False,[],player_a, player_b  # возвращаем, что война закончилась, игрок B победил
        # если карты равны - повторяем войну

def play_war():
    """
    Основная логика игры "Война".
    """
    deck = create_deck()  # Создаем колоду
    player_a, player_b = deal_cards(deck) # раздаем карты

    round_number = 0 # счетчик раундов
    while player_a and player_b: # пока у обоих игроков есть карты
        round_number += 1 # увеличиваем счетчик раундов
        logger.info(f'Раунд {round_number}. Карты игрока A: {len(player_a)}, Карты игрока B: {len(player_b)}') # выводим информацию о раунде
        card_a = player_a.pop(0) # берем карту из колоды игрока А
        card_b = player_b.pop(0) # берем карту из колоды игрока B
        cards_on_table = [card_a, card_b] # карты на столе

        card_a_value = get_card_value(card_a) # получаем значение карты игрока А
        card_b_value = get_card_value(card_b) # получаем значение карты игрока B

        if card_a_value > card_b_value: # если карта игрока А старше
            player_a.extend(cards_on_table) # игрок А забирает карты
        elif card_b_value > card_a_value:  # если карта игрока B старше
            player_b.extend(cards_on_table) # игрок B забирает карты
        else:  # если карты равны, начинаем войну
            a_win_war, b_win_war ,cards_on_table,player_a, player_b = war(player_a, player_b, cards_on_table) # запускаем войну
            if a_win_war: # если у игрока А не хватило карт
                logger.info('Игрок B победил в войне')
                break # выходим из цикла
            elif b_win_war: # если у игрока B не хватило карт
                logger.info('Игрок A победил в войне')
                break # выходим из цикла
        
        # для красоты, перемешиваем карты в конце каждой руки
        random.shuffle(player_a)
        random.shuffle(player_b)

    if not player_a: # если у игрока А нет карт
        logger.info('Игрок B выиграл игру!')  # выводим сообщение о победе игрока B
    elif not player_b: # если у игрока B нет карт
        logger.info('Игрок A выиграл игру!') # выводим сообщение о победе игрока A

if __name__ == '__main__':
    play_war()
```