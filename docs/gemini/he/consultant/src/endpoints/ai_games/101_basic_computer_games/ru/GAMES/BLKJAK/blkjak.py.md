# Анализ кода модуля blkjak.py

**Качество кода**
  - **Соответствие требованиям к формату кода (1-10)**
     -  _Преимущества_:
        - Код хорошо структурирован и логически разделен на функции.
        -  Используются осмысленные имена переменных и функций.
        -  Есть подробные комментарии и описание алгоритма игры.
        -  Присутствует блок-схема, визуализирующая логику игры.
     -  _Недостатки_:
         -  Не используются docstring в формате reStructuredText (RST).
         -  Отсутствует обработка ошибок.
         -  Нет импорта логгера.
         -  Не используется `j_loads` или `j_loads_ns`.
         -  Слишком много комментариев в стиле `#`, что усложняет восприятие кода.
         -  Не все переменные и функции описаны с помощью reStructuredText (RST)

**Рекомендации по улучшению**
1.  **Документация**:
    - Добавить docstring в формате RST для всех модулей, функций и переменных.
    - Заменить комментарии в стиле `#` на docstring.
2.  **Обработка ошибок**:
    -  Использовать `try-except` блоки для обработки возможных ошибок и логировать их с помощью `logger.error`.
3.  **Импорты**:
     -  Добавить импорт логгера `from src.logger.logger import logger`.
4. **Использование `j_loads`**:
    - Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`, если это необходимо. В данном случае `json.load` не используется, но это рекомендуется для будущих случаев.
5.  **Комментарии**:
    -  Сохранить существующие комментарии после `#`, но дополнить их с помощью docstring в формате RST.
    -  Избегать общих фраз в комментариях, формулировать описания точнее.
6.  **Структура**:
    -  Убедиться, что все функции и переменные соответствуют стандартам именования.

**Улучшенный код**

```python
"""
Модуль для реализации игры в блэкджек
=======================================

Этот модуль реализует карточную игру в блэкджек, где игрок соревнуется с дилером.

Описание игры:
    Игрок и дилер получают по две карты, цель игрока набрать 21 очко или как можно ближе к 21, но не превысить это значение.
    Игрок может брать еще карты или остановиться. После того, как игрок останавливается, дилер берет карты, пока его сумма не станет больше 16.
    Игрок побеждает, если сумма его карт больше, чем у дилера, но меньше или равна 21.

Пример использования:
    >>> play_blackjack()
    Карты дилера:
    <закрытая карта>  7
    Карты игрока: 10 8 Сумма: 18
    Хотите взять еще карту? (HIT/STAND): stand

    Ход дилера:
    Карты дилера: 9 7 Сумма: 16
    Карты игрока: 10 8 Сумма: 18
    Вы выиграли!
"""
import random
from src.logger.logger import logger  # Импортируем logger # Добавили импорт логгера

def deal_card(deck: list) -> int:
    """
    Выдает карту из колоды.

    :param deck: Колода карт.
    :type deck: list
    :return: Значение карты.
    :rtype: int
    """
    # Возвращает и удаляет последнюю карту из колоды
    return deck.pop()

def calculate_hand_value(hand: list) -> int:
    """
    Вычисляет значение руки.

    :param hand: Список карт на руках.
    :type hand: list
    :return: Сумма очков карт на руках.
    :rtype: int
    """
    ace_count = hand.count(11) # Считаем количество тузов (11)
    total = sum(hand)  # Считаем общую сумму очков

    # Преобразуем туз из 11 в 1, если сумма больше 21
    while total > 21 and ace_count > 0:
        total -= 10  # Превращаем туз из 11 в 1
        ace_count -= 1
    return total

def display_cards(player_hand: list, dealer_hand: list, show_dealer_full: bool = False) -> None:
    """
    Отображает карты игрока и дилера.

    :param player_hand: Карты игрока.
    :type player_hand: list
    :param dealer_hand: Карты дилера.
    :type dealer_hand: list
    :param show_dealer_full: Флаг, показывающий все карты дилера. По умолчанию False.
    :type show_dealer_full: bool
    """
    print("\nКарты дилера:")
    if show_dealer_full:
        print(" ".join(map(str, dealer_hand)), f"Сумма: {calculate_hand_value(dealer_hand)}")  # Если show_dealer_full=True, показываем все карты дилера и сумму
    else:
        print("<закрытая карта> ", dealer_hand[1])  # Показываем первую карту дилера, вторая скрыта

    print("Карты игрока:", " ".join(map(str, player_hand)), f"Сумма: {calculate_hand_value(player_hand)}") # Отображает карты игрока и их сумму


def play_blackjack() -> None:
    """
    Запускает игру в блэкджек.
    """
    # Создание колоды из 52 карт: числовые значения (2-10) и туз (11)
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    random.shuffle(deck) # Перемешиваем колоду

    # Раздача карт игроку и дилеру (по 2 карты)
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    # Отображение карт (одна карта дилера скрыта)
    display_cards(player_hand, dealer_hand)

    # Ход игрока
    while True:
        player_value = calculate_hand_value(player_hand)
        if player_value == 21:  # Если у игрока сразу 21
            print("Блэкджек! Вы выиграли!")
            return

        if player_value > 21:  # Если игрок проиграл
            print("Перебор! Вы проиграли!")
            return

        action = input("Хотите взять еще карту? (HIT/STAND): ").upper() # Запрашивает действие игрока
        if action == "HIT":
            player_hand.append(deal_card(deck))  # Даем карту игроку
            display_cards(player_hand, dealer_hand) # Отображаем карты
        elif action == "STAND":
            break  # Переходим к ходу дилера
        else:
            print("Некорректный ввод. Пожалуйста, введите HIT или STAND.") # Обработка некорректного ввода

    # Ход дилера
    print("\nХод дилера:")
    while calculate_hand_value(dealer_hand) <= 16:
        dealer_hand.append(deal_card(deck)) # Дилер берет карту

    display_cards(player_hand, dealer_hand, True)  # показываем все карты дилера

    player_value = calculate_hand_value(player_hand)  # Сумма игрока
    dealer_value = calculate_hand_value(dealer_hand)  # Сумма дилера

    # Проверка условий победы
    if dealer_value > 21: # Если у дилера перебор
        print("Дилер перебрал! Вы выиграли!")
    elif player_value > dealer_value or dealer_value > 21:  # Если у игрока больше очков
        print("Вы выиграли!")
    elif dealer_value > player_value: # Если у дилера больше очков
        print("Вы проиграли!")
    else:
        print("Ничья!")  # Ничья

if __name__ == "__main__":
    play_blackjack()  # Запуск игры
```