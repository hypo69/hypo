# Анализ кода модуля `mnoply.py`

**Качество кода**
7/10
 -  Плюсы
    - Код игры логически структурирован и понятен.
    -  Используются списки для хранения данных об игроках, их позициях, и владениях.
    -  Есть обработка ввода пользователя.
    -  Используются комментарии, хоть и не в формате RST.
 -  Минусы
    - Отсутствуют импорты из `src.utils.jjson` и `src.logger.logger`.
    -  Некоторые переменные и функции не имеют docstring.
    - Комментарии не в формате reStructuredText (RST).
    - Используется `try-except` без логирования ошибок.
    - Имена переменных не соответствуют стандартам.

**Рекомендации по улучшению**

1.  **Импорты**: Добавить необходимые импорты:
    -  `from src.utils.jjson import j_loads, j_loads_ns`
    -  `from src.logger.logger import logger`
2.  **Формат документации**: Переписать все комментарии и docstring в формате RST.
3.  **Логирование**: Заменить `try-except` на использование `logger.error` для обработки ошибок.
4.  **Обработка данных**: Использовать `j_loads` или `j_loads_ns` для чтения файлов, если это потребуется.
5.  **Стиль кода**:
    -  Переименовать переменные, используя snake_case.
    -  Добавить docstring для всех функций.
    - Избегать использования `while True` для ввода данных.
6. **Улучшение читаемости**:
    - Разделить код на более мелкие функции для большей модульности.
    - Добавить константы для магических значений (например, 12 для количества свойств).

**Оптимизиробанный код**

```python
"""
Модуль реализации текстовой версии игры "Монополия".
=====================================================

Этот модуль реализует упрощенную версию настольной игры "Монополия" в текстовом формате.
Игра предназначена для 2-4 игроков. Игроки по очереди бросают кубик, перемещаются по игровому полю,
могут покупать недвижимость и платить ренту другим игрокам. Цель игры - остаться последним игроком
с денежными средствами.

Пример использования
--------------------

.. code-block:: python

    play_monopoly()
"""
import random
# import sys
from src.logger.logger import logger #  импортируем logger для логирования ошибок
# from src.utils.jjson import j_loads, j_loads_ns # импортируем для работы с json (не используется)


def get_number_of_players() -> int:
    """
    Запрашивает у пользователя количество игроков (2-4).

    :return: Количество игроков.
    :rtype: int
    """
    while True:
        try:
            num_players = int(input("Введите количество игроков (2-4): "))
            if 2 <= num_players <= 4:
                return num_players
            else:
                print("Количество игроков должно быть между 2 и 4.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")


def initialize_game(num_players: int) -> tuple[list[int], list[int], list[int]]:
    """
    Инициализирует начальные параметры игры.

    :param num_players: Количество игроков.
    :type num_players: int
    :return: Кортеж, содержащий:
        - player_balances: Список балансов игроков.
        - player_positions: Список позиций игроков на поле.
        - property_owners: Список владельцев недвижимости.
    :rtype: tuple[list[int], list[int], list[int]]
    """
    player_balances = [1000] * num_players  # начальный баланс для каждого игрока
    player_positions = [0] * num_players  # начальная позиция на доске для каждого игрока
    property_owners = [-1] * 12  # -1 означает, что собственность не принадлежит никому
    return player_balances, player_positions, property_owners


def player_turn(player: int, player_balances: list[int], player_positions: list[int], property_owners: list[int],
                properties_prices: list[int], properties_rent: list[int]) -> None:
    """
    Выполняет ход игрока.

    :param player: Индекс текущего игрока.
    :type player: int
    :param player_balances: Список балансов игроков.
    :type player_balances: list[int]
    :param player_positions: Список позиций игроков на поле.
    :type player_positions: list[int]
    :param property_owners: Список владельцев недвижимости.
    :type property_owners: list[int]
    :param properties_prices: Список цен на недвижимость.
    :type properties_prices: list[int]
    :param properties_rent: Список стоимости аренды недвижимости.
    :type properties_rent: list[int]
    """
    if player_balances[player] <= 0:
        return  # если у игрока нет денег, пропускаем его ход

    print(f"\nХод игрока {player + 1}:")

    dice_roll = random.randint(1, 6)  # бросаем кубик
    print(f"Выпало {dice_roll}.")

    player_positions[player] = (player_positions[player] + dice_roll) % 12  # перемещаем игрока по полю
    current_position = player_positions[player]
    print(f"Вы находитесь на позиции {current_position + 1}.")

    if property_owners[current_position] == -1:  # если недвижимость свободна
        buy_property(player, current_position, player_balances, property_owners, properties_prices) # вызываем функцию покупки
    elif property_owners[current_position] != player:  # если недвижимость принадлежит другому игроку
        pay_rent(player, current_position, player_balances, property_owners, properties_rent) # вызываем функцию оплаты ренты


def buy_property(player: int, current_position: int, player_balances: list[int], property_owners: list[int], properties_prices: list[int]) -> None:
    """
    Предлагает игроку купить недвижимость.

    :param player: Индекс текущего игрока.
    :type player: int
    :param current_position: Текущая позиция игрока на поле.
    :type current_position: int
    :param player_balances: Список балансов игроков.
    :type player_balances: list[int]
    :param property_owners: Список владельцев недвижимости.
    :type property_owners: list[int]
    :param properties_prices: Список цен на недвижимость.
    :type properties_prices: list[int]
    """
    while True:
        buy_choice = input(
            f"Хотите купить недвижимость за {properties_prices[current_position]}? (да/нет): ").lower()
        if buy_choice == 'да':
            if player_balances[player] >= properties_prices[current_position]:
                player_balances[player] -= properties_prices[current_position]
                property_owners[current_position] = player
                print(f"Вы приобрели недвижимость, ваш баланс: {player_balances[player]}.")
            else:
                print("У вас недостаточно средств для покупки.")
            break
        elif buy_choice == 'нет':
            break
        else:
            print("Некорректный ввод, пожалуйста, выберите 'да' или 'нет'.")


def pay_rent(player: int, current_position: int, player_balances: list[int], property_owners: list[int], properties_rent: list[int]) -> None:
    """
    Производит оплату ренты за недвижимость.

    :param player: Индекс текущего игрока.
    :type player: int
    :param current_position: Текущая позиция игрока на поле.
    :type current_position: int
    :param player_balances: Список балансов игроков.
    :type player_balances: list[int]
    :param property_owners: Список владельцев недвижимости.
    :type property_owners: list[int]
    :param properties_rent: Список стоимости аренды недвижимости.
    :type properties_rent: list[int]
    """
    owner = property_owners[current_position]
    rent = properties_rent[current_position]
    if player_balances[player] >= rent:
        player_balances[player] -= rent
        player_balances[owner] += rent
        print(f"Вы заплатили ренту игроку {owner + 1}, ваш баланс: {player_balances[player]}.")
    else:
        print("У вас недостаточно средств для оплаты ренты, вы выбываете из игры!")
        player_balances[player] = 0  # игрок выбывает


def print_player_balances(num_players: int, player_balances: list[int]) -> None:
    """
    Выводит текущий баланс каждого игрока.

    :param num_players: Количество игроков.
    :type num_players: int
    :param player_balances: Список балансов игроков.
    :type player_balances: list[int]
    """
    for i in range(num_players):
        print(f"Баланс игрока {i + 1} = {player_balances[i]}")


def announce_winner(player_balances: list[int]) -> None:
    """
    Определяет и выводит победителя игры.

    :param player_balances: Список балансов игроков.
    :type player_balances: list[int]
    """
    winner = [i + 1 for i, balance in enumerate(player_balances) if balance > 0][0]
    print(f"\nИгрок {winner} победил в игре!")

def play_monopoly():
    """
    Основная функция для запуска игры в монополию.
    """
    num_players = get_number_of_players() # получаем количество игроков
    player_balances, player_positions, property_owners = initialize_game(num_players) # инициализируем игру

    properties_prices = [60, 60, 100, 100, 120, 140, 150, 180, 200, 220, 240, 300] # цены на недвижимость
    properties_rent = [50, 50, 75, 75, 100, 120, 125, 150, 175, 200, 225, 250] # цены на ренту

    while sum(1 for balance in player_balances if balance > 0) > 1: # пока не останется один игрок
        for player in range(num_players): # для каждого игрока
            player_turn(player, player_balances, player_positions, property_owners, properties_prices, properties_rent) # ход игрока
            print_player_balances(num_players, player_balances) # печатаем балансы

    announce_winner(player_balances) # объявляем победителя


if __name__ == "__main__":
    play_monopoly()
```