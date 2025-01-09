# Анализ кода модуля `65_nim.ru.md`

**Качество кода**
 -  Соответствие требованиям к формату кода: 1-2
    -  **Преимущества:**
        - Документ представляет собой подробное описание правил игры NIM на русском языке.
        - Содержит пошаговую инструкцию, примеры работы программы и возможные ограничения.
    -  **Недостатки:**
        - Документ не является кодом Python, поэтому не применимы требования к форматированию кода, docstring и обработке ошибок.
        - Отсутствуют импорты, функции, переменные, которые нужно анализировать и улучшать.
        - Нет инструкций по использованию `j_loads` или `j_loads_ns`, нет необходимости заменять `json.load`.
        - Отсутствуют места для вставки `logger.error` и `try-except`.

**Рекомендации по улучшению**
 - Данный файл содержит только описание игры в формате Markdown, и не является исполняемым кодом Python.
 - Для соответствия требованиям, необходимо реализовать саму игру на Python и встроить необходимые docstring, обработку ошибок и т.д., после чего можно будет провести анализ и дать рекомендации.
 - Сейчас файл можно использовать как основу для реализации игры, но для оценки качества кода и внесения улучшений, нужно предоставить исполняемый код Python.

**Улучшенный код**
```python
"""
Модуль для реализации игры NIM.
=========================================================================================

Модуль содержит функции для инициализации игры, управления ходами игроков
и проверки условий завершения игры NIM.

Пример использования
--------------------

Пример запуска игры:

.. code-block:: python

    if __name__ == '__main__':
        play_nim()
"""
import random  # импорт модуля random для генерации случайных чисел
from src.logger.logger import logger  # импорт логгера для записи ошибок
from typing import List, Tuple  # импорт типов данных для аннотаций
# Функция для инициализации игры
def initialize_game() -> Tuple[List[int], List[str]]:
    """
    Инициализирует игру NIM.

    :return: Кортеж, содержащий список куч и список имен игроков.
    :rtype: Tuple[List[int], List[str]]
    """
    print('Добро пожаловать в NIM!')  # выводит приветствие
    player1_name = input('Введите имя Игрока 1: ')  # получает имя первого игрока
    player2_name = input('Введите имя Игрока 2: ')  # получает имя второго игрока
    players = [player1_name, player2_name]  # формирует список игроков

    num_piles = random.randint(3, 5)  # генерирует случайное количество куч
    piles = [random.randint(5, 15) for _ in range(num_piles)]  # генерирует случайное количество камней в каждой куче

    print('Игра начинается!')  # выводит сообщение о начале игры
    return piles, players  # возвращает список куч и список имен игроков


def print_piles(piles: List[int]) -> None:
    """
    Выводит текущее состояние куч.

    :param piles: Список, представляющий состояние куч.
    :type piles: List[int]
    :return: None
    """
    for i, stones in enumerate(piles):  # проходит по всем кучам
        print(f'Куча {i + 1}: {stones} камней')  # выводит текущее состояние куч


def get_player_move(player_name: str, piles: List[int]) -> Tuple[int, int]:
    """
    Запрашивает ход игрока.

    :param player_name: Имя текущего игрока.
    :type player_name: str
    :param piles: Список, представляющий текущее состояние куч.
    :type piles: List[int]
    :return: Кортеж, содержащий номер кучи и количество камней, которые игрок хочет взять.
    :rtype: Tuple[int, int]
    """
    while True:  # бесконечный цикл до корректного ввода
        try:
            print(f'{player_name}, ваш ход!')  # выводит сообщение с именем игрока
            pile_number = int(input('Введите номер кучи: ')) - 1  # получает номер кучи от пользователя
            stones_to_take = int(input('Введите количество камней: '))  # получает количество камней от пользователя

            if not (0 <= pile_number < len(piles)):  # проверяет номер кучи
                print('Ошибка! Неверный номер кучи. Попробуйте снова.')  # выводит сообщение об ошибке
                continue

            if stones_to_take <= 0 or stones_to_take > piles[pile_number]:  # проверяет количество камней
                print(f'Ошибка! В куче {pile_number + 1} всего {piles[pile_number]} камней. Попробуйте снова.')  # выводит сообщение об ошибке
                continue

            return pile_number, stones_to_take  # возвращает номер кучи и количество камней

        except ValueError:  # ловит ошибку ввода не числа
            print('Ошибка! Введите число.')  # выводит сообщение об ошибке
        except Exception as e:  # ловит все остальные ошибки
             logger.error('Ошибка при получении хода игрока', exc_info=True)  # записывает ошибку в лог
             ... # точка остановки
             continue # возвращаемся в начало цикла

def update_piles(piles: List[int], pile_number: int, stones_to_take: int) -> List[int]:
    """
     Обновляет состояние куч.

    :param piles: Список, представляющий текущее состояние куч.
    :type piles: List[int]
    :param pile_number: Индекс кучи, из которой игрок берет камни.
    :type pile_number: int
    :param stones_to_take: Количество камней, которые игрок берет.
    :type stones_to_take: int
    :return: Обновленный список куч.
    :rtype: List[int]
    """
    piles[pile_number] -= stones_to_take  # уменьшает количество камней в куче
    return piles  # возвращает обновленный список куч


def check_game_over(piles: List[int]) -> bool:
    """
     Проверяет, завершена ли игра.

    :param piles: Список, представляющий текущее состояние куч.
    :type piles: List[int]
    :return: True, если игра завершена, False в противном случае.
    :rtype: bool
    """
    return all(stones == 0 for stones in piles)  # проверяет, все ли кучи пустые


def play_nim():
    """
    Запускает игру NIM.

    :return: None
    """
    piles, players = initialize_game() # инициализирует игру и получает список куч и игроков
    current_player_index = 0  # устанавливает индекс текущего игрока

    while True: # основной цикл игры
        print_piles(piles) # выводит текущее состояние куч
        player_name = players[current_player_index] # получает имя текущего игрока

        pile_number, stones_to_take = get_player_move(player_name, piles) # получает ход игрока
        piles = update_piles(piles, pile_number, stones_to_take)  # обновляет состояние куч

        if check_game_over(piles): # проверяет, закончилась ли игра
            print(f'Игрок {player_name} взял последний камень.')  # выводит сообщение о конце игры
            winner_index = 1 - current_player_index # определяет победителя
            print(f'Победитель: {players[winner_index]}! Поздравляем!')  # выводит сообщение о победителе
            break # выходит из цикла игры
        current_player_index = 1 - current_player_index  # переключает на следующего игрока

    play_again = input('Хотите сыграть снова? (да/нет): ') # спрашивает, хотят ли игроки играть снова
    if play_again.lower() == 'да': # если хотят играть снова
        play_nim()  # запускает игру снова

if __name__ == '__main__':
    play_nim()  # запускает игру, если файл запущен напрямую