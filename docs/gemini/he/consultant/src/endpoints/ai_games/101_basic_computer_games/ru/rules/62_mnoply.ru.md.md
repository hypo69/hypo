# Анализ кода модуля MNOPLY

**Качество кода**
- **Соответствие требованиям к формату кода (1-10):** 7/10
    - **Преимущества:**
        - Описание игры достаточно подробное, с разбиением на разделы.
        - Приведен пример работы программы, что облегчает понимание логики игры.
        - Есть описание возможных ограничений и реализации.
    - **Недостатки:**
        - Отсутствует конкретный код на Python.
        - Не используется reStructuredText для документации.
        - Нет импортов.
        - Не используются `j_loads` или `j_loads_ns`.
        - Отсутствуют docstring.

**Рекомендации по улучшению**
1. **Добавить docstring:**
   -  Добавить подробные docstring для всех функций и классов, включая описания параметров и возвращаемых значений, используя reStructuredText.
2. **Использовать `j_loads`:**
   - Заменить стандартный `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
3.  **Обработка ошибок:**
    - Использовать `logger.error` для записи ошибок вместо стандартных `try-except`.
4. **Оптимизация кода:**
   - Разбить код на функции для удобства чтения и поддержки.
   - Использовать константы для фиксированных значений (например, начальная сумма денег).
   - Добавить комментарии к коду, объясняющие логику работы.
5. **Форматирование:**
    -  Соблюдать PEP8 для форматирования кода.
6. **Унифицировать:**
    - Привести названия функций и переменных к единому стилю.
7. **Документация:**
     - Дополнить документацию к функциям и классам в формате reStructuredText.

**Улучшенный код**
```python
"""
Модуль для реализации упрощенной версии настольной игры "Монополия" - MNOPLY.
====================================================================================================

В этом модуле реализована базовая механика игры, включая перемещение по полю, покупку собственности,
уплату аренды, случайные события и налоги.

Пример использования
--------------------

Для запуска игры необходимо вызвать функцию :func:`start_game`.

.. code-block:: python

    start_game()
"""
import random
from typing import List, Dict, Any

from src.logger.logger import logger  # Импорт logger для обработки ошибок
from src.utils.jjson import j_loads  # Импорт j_loads для чтения JSON файлов

# константы для игры
INITIAL_BALANCE = 1500
NUMBER_OF_CELLS = 20
MIN_PLAYERS = 2
MAX_PLAYERS = 4


def get_player_names() -> List[str]:
    """
    Получает имена игроков.

    :return: Список имен игроков.
    """
    while True:
        try:
            num_players = int(input(f'Введите количество игроков ({MIN_PLAYERS}–{MAX_PLAYERS}): '))  # Запрос количества игроков
            if MIN_PLAYERS <= num_players <= MAX_PLAYERS:
                break
            else:
                logger.error(f"Неверное количество игроков. Введите от {MIN_PLAYERS} до {MAX_PLAYERS}.") # Логирование ошибки ввода
        except ValueError:
            logger.error("Неверный ввод. Введите целое число.")# Логирование ошибки ввода
    player_names = []
    for i in range(num_players):
        name = input(f'Введите имя Игрока {i + 1}: ')  # Запрос имени каждого игрока
        player_names.append(name)
    return player_names


def initialize_game(player_names: List[str]) -> Dict[str, Dict[str, Any]]:
    """
    Инициализирует игру.

    Создает начальное состояние игры, включая баланс игроков и список клеток.

    :param player_names: Список имен игроков.
    :return: Словарь с данными об игре.
    """
    players = {name: {'balance': INITIAL_BALANCE, 'position': 0, 'properties': []} for name in player_names} # Создание словаря игроков с начальным балансом и позицией
    game_board = _generate_game_board()
    return {'players': players, 'board': game_board}


def _generate_game_board() -> List[Dict[str, Any]]:
    """
     Генерирует игровое поле.

     :return: Список клеток игрового поля.
     """
    board = [
        {'type': 'property', 'name': 'Улица Вязов', 'cost': 200, 'rent': 50, 'owner': None},
        {'type': 'chance'},
        {'type': 'property', 'name': 'Тихая гавань', 'cost': 300, 'rent': 75, 'owner': None},
        {'type': 'tax', 'amount': 150},
        {'type': 'property', 'name': 'Солнечный переулок', 'cost': 250, 'rent': 60, 'owner': None},
        {'type': 'jail'},
        {'type': 'property', 'name': 'Зеленый проспект', 'cost': 350, 'rent': 80, 'owner': None},
        {'type': 'chance'},
        {'type': 'property', 'name': 'Красная площадь', 'cost': 400, 'rent': 100, 'owner': None},
        {'type': 'tax', 'amount': 200},
        {'type': 'property', 'name': 'Синяя аллея', 'cost': 300, 'rent': 70, 'owner': None},
        {'type': 'chance'},
        {'type': 'property', 'name': 'Желтый бульвар', 'cost': 450, 'rent': 110, 'owner': None},
        {'type': 'jail'},
        {'type': 'property', 'name': 'Оранжевый переезд', 'cost': 500, 'rent': 120, 'owner': None},
        {'type': 'chance'},
        {'type': 'property', 'name': 'Фиолетовый склон', 'cost': 600, 'rent': 150, 'owner': None},
        {'type': 'tax', 'amount': 250},
        {'type': 'property', 'name': 'Белая тропа', 'cost': 650, 'rent': 160, 'owner': None},
        {'type': 'chance'},
    ]
    return board


def player_turn(player_name: str, game_data: Dict[str, Any]) -> None:
    """
    Обрабатывает ход игрока.

    Игрок бросает кубик, перемещается по полю и обрабатываются события.

    :param player_name: Имя текущего игрока.
    :param game_data: Словарь с данными об игре.
    """
    player = game_data['players'][player_name]
    roll = random.randint(1, 6)  # Бросаем кубик
    print(f'Ход {player_name}. Бросок кубика: {roll}.')

    player['position'] = (player['position'] + roll) % NUMBER_OF_CELLS # Перемещаем игрока по полю с учетом циклического перехода
    cell = game_data['board'][player['position']] # Получаем клетку, на которую переместился игрок

    print(f'{player_name} перемещается на клетку {player["position"] + 1} ({cell.get("name", cell.get("type", "Неизвестно"))}).') # Вывод информации о клетке

    if cell['type'] == 'property':
        _handle_property(player_name, cell, game_data) # Обработка клетки с собственностью
    elif cell['type'] == 'chance':
        _handle_chance(player_name, game_data) # Обработка клетки с шансом
    elif cell['type'] == 'tax':
        _handle_tax(player_name, cell, game_data) # Обработка клетки с налогом
    elif cell['type'] == 'jail':
        _handle_jail(player_name, game_data) # Обработка клетки с тюрьмой


def _handle_property(player_name: str, cell: Dict[str, Any], game_data: Dict[str, Any]) -> None:
    """
    Обрабатывает ситуацию, когда игрок попадает на клетку с собственностью.

    Игрок может купить собственность или заплатить аренду, если она уже куплена.

    :param player_name: Имя текущего игрока.
    :param cell: Словарь с данными о клетке.
    :param game_data: Словарь с данными об игре.
    """
    player = game_data['players'][player_name]
    if cell['owner'] is None:  # Проверка, свободна ли собственность
        choice = input('Хотите купить? (да/нет): ').lower()  # Предложение игроку купить собственность
        if choice == 'да':
            if player['balance'] >= cell['cost']:  # Проверка баланса игрока для покупки
                player['balance'] -= cell['cost']
                cell['owner'] = player_name  # Присвоение собственности игроку
                player['properties'].append(cell) # Добавляем собственность в список игрока
                print(f'{player_name} покупает {cell["name"]} за {cell["cost"]} долларов. У {player_name} осталось {player["balance"]} долларов.') # Вывод сообщения о покупке
            else:
                print('Недостаточно средств для покупки.')  # Вывод сообщения о недостатке средств
    elif cell['owner'] != player_name:  # Проверка, не является ли игрок владельцем
        owner = game_data['players'][cell['owner']]
        player['balance'] -= cell['rent']
        owner['balance'] += cell['rent']  # Снятие денег с игрока и перечисление владельцу
        print(f'{player_name} платит аренду {cell["rent"]} долларов игроку {cell["owner"]}. У {player_name} осталось {player["balance"]} долларов.') # Вывод информации об уплате аренды
    else:
        print(f'{player_name} владеет {cell["name"]}')


def _handle_chance(player_name: str, game_data: Dict[str, Any]) -> None:
    """
    Обрабатывает событие "Шанс".

    Игрок получает случайное событие, которое может повлиять на его баланс или позицию.

    :param player_name: Имя текущего игрока.
    :param game_data: Словарь с данными об игре.
    """
    player = game_data['players'][player_name]
    chance = random.choice([
        {'text': 'Вы выиграли 100 долларов на лотерее!', 'money': 100, 'move': 0},
        {'text': 'Вы потеряли 50 долларов на штрафе.', 'money': -50, 'move': 0},
        {'text': 'Вы нашли 200 долларов!', 'money': 200, 'move': 0},
        {'text': 'Вас ограбили на 100 долларов!', 'money': -100, 'move': 0},
        {'text': 'Перемещаетесь на 3 клетки вперед.', 'money': 0, 'move': 3},
        {'text': 'Перемещаетесь на 2 клетки назад.', 'money': 0, 'move': -2},
    ])  # Случайный выбор события
    print(f'Событие: {chance["text"]}')
    player['balance'] += chance['money']
    player['position'] = (player['position'] + chance['move']) % NUMBER_OF_CELLS # Обновление позиции игрока
    print(f'У {player_name} теперь {player["balance"]} долларов. Новая позиция {player["position"] + 1}')


def _handle_tax(player_name: str, cell: Dict[str, Any], game_data: Dict[str, Any]) -> None:
    """
    Обрабатывает событие "Налог".

    Игрок платит фиксированную сумму налога.

    :param player_name: Имя текущего игрока.
    :param cell: Словарь с данными о клетке.
    :param game_data: Словарь с данными об игре.
    """
    player = game_data['players'][player_name]
    tax_amount = cell['amount']
    player['balance'] -= tax_amount # Снятие налога с игрока
    print(f'{player_name} платит {tax_amount} долларов налога. У {player_name} осталось {player["balance"]} долларов.')# Вывод информации об уплате налога


def _handle_jail(player_name: str, game_data: Dict[str, Any]) -> None:
    """
    Обрабатывает событие "Тюрьма".

    Игрок пропускает один ход.

    :param player_name: Имя текущего игрока.
    :param game_data: Словарь с данными об игре.
    """
    print(f'{player_name} попадает в тюрьму и пропускает ход.')# Вывод информации о попадании в тюрьму


def check_bankrupt(player_name: str, game_data: Dict[str, Any]) -> bool:
    """
    Проверяет, обанкротился ли игрок.

    :param player_name: Имя текущего игрока.
    :param game_data: Словарь с данными об игре.
    :return: True, если игрок обанкротился, False в противном случае.
    """
    player = game_data['players'][player_name]
    return player['balance'] <= 0 # Проверяем баланс игрока


def display_results(game_data: Dict[str, Any]) -> None:
    """
    Выводит результаты игры.

    :param game_data: Словарь с данными об игре.
    """
    players = game_data['players']
    print('\nФинальные результаты:')
    for name, data in players.items(): # Вывод баланса каждого игрока
        print(f'{name}: {data["balance"]} долларов')

    winner = _get_winner(game_data) # Получаем имя победителя

    if winner:
        print(f'\nПобедитель: {winner}! Поздравляем!')# Выводим поздравление победителю
    else:
        print('\nНикто не выиграл.')


def _get_winner(game_data: Dict[str, Any]) -> str | None:
    """
    Определяет победителя игры.

    :param game_data: Словарь с данными об игре.
    :return: Имя победителя или None, если нет победителя.
    """
    players = game_data['players']
    active_players = [name for name, data in players.items() if data['balance'] > 0] # Фильтрация активных игроков
    if len(active_players) == 1: # Если остался только один игрок, он победитель
        return active_players[0]
    return None


def play_again() -> bool:
    """
    Спрашивает пользователя, хочет ли он сыграть снова.

    :return: True, если хочет, False в противном случае.
    """
    choice = input('Хотите сыграть снова? (да/нет): ').lower() # Запрос на повтор игры
    return choice == 'да'


def start_game():
    """
    Запускает игру MNOPLY.

    Отображает приветственное сообщение, инициализирует игру,
    выполняет игровой процесс и выводит результаты.
    """
    print('Добро пожаловать в MNOPLY!')
    print('Цель игры — стать единственным игроком, который останется с деньгами.')
    print('Вы будете перемещаться по игровому полю, покупать недвижимость, платить аренду и участвовать в событиях.')
    print('Удачи!\n')

    player_names = get_player_names()  # Запрашиваем имена игроков
    game_data = initialize_game(player_names)  # Инициализируем игру
    print('Все игроки начинают с 1500 долларов. Игра начинается!\n')

    turn_count = 0
    while True:
        current_player_name = player_names[turn_count % len(player_names)] # Получаем имя текущего игрока
        if check_bankrupt(current_player_name, game_data): # Проверяем не обанкротился ли игрок
            print(f'{current_player_name} обанкротился! Он выходит из игры.')# Выводим сообщение о банкротстве
            game_data['players'].pop(current_player_name) # Удаляем игрока из списка
            player_names.remove(current_player_name) # Удаляем имя игрока из списка
            if len(player_names) == 1:
                break
            turn_count += 1
            continue
        player_turn(current_player_name, game_data) # Ход игрока
        turn_count += 1
        if _get_winner(game_data):
            break
        bankrupt_players = [name for name in player_names if check_bankrupt(name, game_data)]
        for player_name in bankrupt_players:
            print(f'{player_name} обанкротился! Он выходит из игры.')
            game_data['players'].pop(player_name)
            player_names.remove(player_name)
            if len(player_names) == 1:
                break
        if len(player_names) == 1:
             break


    display_results(game_data)  # Выводим результаты игры
    if play_again():
        start_game()  # Запускаем игру снова
    else:
        print('Спасибо за игру!')  # Завершение игры


if __name__ == '__main__':
    start_game()
```