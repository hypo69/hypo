# Анализ кода модуля blkjak

**Качество кода**
6
- Плюсы
    - Код содержит подробные комментарии, описывающие логику игры и основные шаги.
    - Присутствует блок-схема, помогающая понять последовательность действий в игре.
    - Функции хорошо структурированы и выполняют конкретные задачи.
    - Есть разделение на функции для раздачи карт, вычисления очков и отображения карт.
- Минусы
    - Отсутствует reStructuredText (RST) документация для функций и модуля.
    - Не используется логирование ошибок, что затрудняет отладку.
    - Используется стандартный `print` для вывода сообщений, что не очень удобно для отладки.
    - Использование `input` может привести к ошибкам, если пользователь введет что-то неожиданное.
    - Нет обработки исключений для случаев, если deck пуст.
    - Нет импортов `logger` и `j_loads`.

**Рекомендации по улучшению**
1.  Добавить RST документацию для модуля и всех функций.
2.  Использовать `logger` для логирования ошибок и отладки.
3.  Заменить `print` на `logger.info` или `logger.debug` для вывода сообщений.
4.  Добавить обработку исключений для `deck.pop()` если колода пуста.
5.  Добавить проверку ввода пользователя и обработку некорректных вводов.
6.  Использовать `j_loads` или `j_loads_ns` для чтения файлов, если это необходимо.
7.  Импортировать необходимые модули, такие как `logger` и `j_loads`.

**Оптимизированный код**
```python
"""
Модуль для реализации игры в блэкджек.
======================================

Этот модуль содержит функции для управления игрой в блэкджек,
включая раздачу карт, вычисление стоимости руки, отображение карт,
и определения победителя.

Пример использования
--------------------

.. code-block:: python

    if __name__ == "__main__":
        play_blackjack()
"""
import random
# импортируем logger для логирования
from src.logger.logger import logger
#TODO добавить импорт j_loads если необходимо


def deal_card(deck: list) -> int:
    """
    Выдает карту из колоды.

    :param deck: Список карт в колоде.
    :return: Значение карты (int).
    """
    # код исполняет извлечение и удаление последней карты из колоды
    try:
        return deck.pop()
    except IndexError as e:
        logger.error('Колода пуста', exc_info=True)
        return None # Возвращаем None если колода пуста

def calculate_hand_value(hand: list) -> int:
    """
    Вычисляет значение руки.

    :param hand: Список карт в руке.
    :return: Общая сумма очков руки (int).
    """
    # Считаем количество тузов (11)
    ace_count = hand.count(11)
    # Считаем общую сумму очков
    total = sum(hand)

    # Если общая сумма больше 21 и есть туз, который можно посчитать как 1
    while total > 21 and ace_count > 0:
        # Превращаем туз из 11 в 1
        total -= 10
        ace_count -= 1
    # Возвращает общую сумму очков
    return total


def display_cards(player_hand: list, dealer_hand: list, show_dealer_full: bool = False) -> None:
    """
    Отображает карты игрока и дилера.

    :param player_hand: Список карт игрока.
    :param dealer_hand: Список карт дилера.
    :param show_dealer_full: Если True, показывает все карты дилера, иначе только одну.
    """
    logger.info("\\nКарты дилера:")
    # код исполняет отображение карт дилера
    if show_dealer_full:
        logger.info(f" {' '.join(map(str, dealer_hand))} Сумма: {calculate_hand_value(dealer_hand)}")
    else:
      # код исполняет вывод первой карты дилера
      logger.info(f"<закрытая карта>  {dealer_hand[1]}")

    # код исполняет отображение карт игрока
    logger.info(f"Карты игрока: {' '.join(map(str, player_hand))} Сумма: {calculate_hand_value(player_hand)}")


def play_blackjack() -> None:
    """
    Запускает игру в блэкджек.
    """
    # Создание колоды из 52 карт: числовые значения (2-10) и туз (11)
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    # Перемешиваем колоду
    random.shuffle(deck)

    # Раздача карт игроку и дилеру (по 2 карты)
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    # Отображение карт (одна карта дилера скрыта)
    display_cards(player_hand, dealer_hand)

    # Ход игрока
    while True:
        player_value = calculate_hand_value(player_hand)
        # Если у игрока сразу 21
        if player_value == 21:
            logger.info("Блэкджек! Вы выиграли!")
            return

        # Если игрок проиграл
        if player_value > 21:
            logger.info("Перебор! Вы проиграли!")
            return
        # Запрашиваем действие игрока (HIT или STAND)
        action = input("Хотите взять еще карту? (HIT/STAND): ").upper()
        if action == "HIT":
            # Даем карту игроку
            player_hand.append(deal_card(deck))
            display_cards(player_hand, dealer_hand)
        elif action == "STAND":
            # Переходим к ходу дилера
            break
        else:
            logger.info("Некорректный ввод. Пожалуйста, введите HIT или STAND.")

    # Ход дилера
    logger.info("\\nХод дилера:")
    # Дилер берет карту пока сумма меньше 16
    while calculate_hand_value(dealer_hand) <= 16:
        dealer_hand.append(deal_card(deck))

    # показываем все карты дилера
    display_cards(player_hand, dealer_hand, True)

    player_value = calculate_hand_value(player_hand) # Сумма игрока
    dealer_value = calculate_hand_value(dealer_hand) # Сумма дилера

    # Проверка условий победы
    if dealer_value > 21:
        # Если у дилера перебор
        logger.info("Дилер перебрал! Вы выиграли!")
    # Если у игрока больше очков
    elif player_value > dealer_value or dealer_value > 21:
        logger.info("Вы выиграли!")
    # Если у дилера больше очков
    elif dealer_value > player_value:
      logger.info("Вы проиграли!")
    else:
      # Ничья
      logger.info("Ничья!")


if __name__ == "__main__":
    # Запуск игры
    play_blackjack()


"""
Объяснение кода:
1.  **Импорт модуля `random`**:\n
   -  `import random`: Импортирует модуль `random`, который используется для генерации случайного порядка карт.\n
2.  **Импорт модуля `logger`**:\n
   - `from src.logger.logger import logger`: Импортирует модуль `logger` для логирования ошибок.\n
3.  **Функция `deal_card(deck)`**:\n
    -  `def deal_card(deck):`: Определяет функцию для взятия карты из колоды.\n
    -  `return deck.pop()`: Удаляет и возвращает последнюю карту из колоды.\n
4.  **Функция `calculate_hand_value(hand)`**:\n
    -   `def calculate_hand_value(hand):`: Определяет функцию для вычисления суммы очков карт.\n
    -   `ace_count = hand.count(11)`: Подсчитывает количество тузов в руке (туз = 11).\n
    -   `total = sum(hand)`: Вычисляет общую сумму очков карт.\n
    -   `while total > 21 and ace_count > 0`: Если сумма больше 21 и есть тузы.\n
    -   `total -= 10`:  Заменяет туз с 11 на 1.\n
    -   `ace_count -= 1`: Уменьшаем количество тузов.\n
    -   `return total`: Возвращает общую сумму очков.\n
5.  **Функция `display_cards(player_hand, dealer_hand, show_dealer_full=False)`**:\n
    -   `def display_cards(player_hand, dealer_hand, show_dealer_full=False):`: Определяет функцию для отображения карт.\n
    -  `show_dealer_full=False`: показывает только 1 карту дилера.\n
    -  Если `show_dealer_full=True`: показывает все карты дилера.\n
6.  **Функция `play_blackjack()`**:\n
    -  `def play_blackjack():`: Определяет функцию, содержащую основную логику игры.\n
    -  `deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4`: Создает колоду из 52 карт (числовые значения и туз).\n
    -  `random.shuffle(deck)`: Перемешивает колоду.\n
    -  `player_hand = [deal_card(deck), deal_card(deck)]`: Раздает 2 карты игроку.\n
    -  `dealer_hand = [deal_card(deck), deal_card(deck)]`: Раздает 2 карты дилеру.\n
    -  `display_cards(player_hand, dealer_hand)`: Отображает начальные карты.\n
    -   **Ход игрока**:\n
         -   `while True:`: Основной цикл хода игрока.\n
        - `player_value = calculate_hand_value(player_hand)`: Вычисляем сумму игрока.\n
        - `if player_value == 21:`: Проверка на блэкджек.\n
        - `if player_value > 21:`: Проверка на проигрыш игрока.\n
         -   `action = input("Хотите взять еще карту? (HIT/STAND): ").upper()`: Запрашивает действие игрока (HIT или STAND).\n
         -   `if action == "HIT":`: Если игрок выбирает HIT:\n
            -   `player_hand.append(deal_card(deck))`: Добавляет карту в руку игрока.\n
            -    `display_cards(player_hand, dealer_hand)`: Отображает карты.\n
         -   `elif action == "STAND":`: Если игрок выбирает STAND, переходит к ходу дилера.\n
    -   **Ход дилера**:\n
        -  `while calculate_hand_value(dealer_hand) <= 16:`: Дилер берет карту пока сумма меньше 16.\n
         -    `dealer_hand.append(deal_card(deck))`: Даем карту дилеру.\n
        -  `display_cards(player_hand, dealer_hand, True)`: Отображаем карты дилера.\n
     -    **Определение победителя**:\n
         - `player_value = calculate_hand_value(player_hand)`: Вычисляем сумму игрока.\n
         -`dealer_value = calculate_hand_value(dealer_hand)`: Вычисляем сумму дилера.\n
        - `if dealer_value > 21: `: Проверка на перебор у дилера.\n
        - `elif player_value > dealer_value or dealer_value > 21`: Проверка победы игрока.\n
        -`elif dealer_value > player_value`: Проверка победы дилера.\n
    -`if __name__ == "__main__":`: Запуск игры.\n
    -`play_blackjack()`: Вызов функции игры.\n
"""