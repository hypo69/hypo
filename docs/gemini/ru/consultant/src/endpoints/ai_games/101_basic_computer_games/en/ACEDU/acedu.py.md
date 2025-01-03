# Анализ кода модуля `acedu.py`

**Качество кода**
8
-  Плюсы
    - Код достаточно структурирован и логичен.
    - Присутствуют функции для создания колоды, преобразования карт в читаемый формат, и основной игровой логики.
    - Имеется обработка ввода пользователя и проверка корректности ставок.
    - Игра заканчивается, когда у игрока заканчиваются деньги или карты в колоде.
-  Минусы
    - Отсутствует документация в формате reStructuredText (RST).
    - Не используется `from src.logger.logger import logger` для логирования ошибок.
    - Присутствует избыточное использование `try-except`, когда можно было бы использовать логирование.
    - Повторяющийся код для изъятия карт из колоды, когда карты совпадают.
    - Нет проверки на минимальное количество карт в колоде перед началом раздачи.

**Рекомендации по улучшению**

1.  Добавить документацию в формате RST для всех функций, переменных и модуля.
2.  Использовать `from src.logger.logger import logger` для логирования ошибок, а не стандартный `print`.
3.  Избегать избыточного использования `try-except`, заменяя на логирование ошибок.
4.  Упростить логику раздачи карт, когда они совпадают, используя цикл `while` с условием и  `continue`.
5.  Добавить проверку на минимальное количество карт в колоде перед раздачей.
6.  Переработать `if/elif/else` для определения результата игры, объединив проигрышные сценарии.
7.  Использовать f-строки для форматирования сообщений.

**Оптимизированный код**

```python
"""
Модуль для игры в Acey Ducey.
=========================================================================================

Этот модуль реализует игру Acey Ducey, карточную игру, в которой игрок делает ставку на то,
будет ли следующая карта между двумя выложенными картами.

Пример использования
--------------------

.. code-block:: python

    if __name__ == "__main__":
        play_acey_ducey()
"""
import random
from src.logger.logger import logger  # импорт logger

# Инициализация колоды карт
def create_deck():
    """
    Создает и перемешивает колоду карт.

    :return: Перемешанный список целых чисел, представляющих карты.
    :rtype: list[int]
    """
    ranks = list(range(2, 15))  # Карты от 2 до 14 (туз = 14)
    deck = ranks * 4  # 4 масти
    random.shuffle(deck)
    return deck

# Вывод карты в читаемом формате
def card_name(value: int) -> str:
    """
    Преобразует числовое значение карты в строковое представление.

    :param value: Числовое значение карты.
    :type value: int
    :return: Строковое представление карты (например, "Валет", "10").
    :rtype: str
    """
    if value == 11:
        return 'Валет'
    elif value == 12:
        return 'Дама'
    elif value == 13:
        return 'Король'
    elif value == 14:
        return 'Туз'
    else:
        return str(value)

# Основной игровой цикл
def play_acey_ducey():
    """
    Запускает основной игровой цикл Acey Ducey.

    Инициализирует игру, обрабатывает ставки и определяет победителя.
    """
    print('Добро пожаловать в игру Acey Ducey!')
    print('Правила: Делаете ставку, угадывая, будет ли следующая карта между двумя выложенными.')
    print('Если карта равна одной из выложенных или туз, вы проигрываете.')
    print('Удачи!\n')

    money = 100  # Стартовый капитал игрока
    deck = create_deck()

    while money > 0 and len(deck) >= 3:
        print(f'Ваш текущий баланс: ${money}')

        # Выкладываем две карты
        card1 = deck.pop()
        card2 = deck.pop()

        # Если карты одинаковые, берем новые
        while card1 == card2:
            deck.insert(0, card1)
            deck.insert(0, card2)
            card1 = deck.pop()
            card2 = deck.pop()
        # Вывод карт на экран
        print(f'Первая карта: {card_name(card1)}')
        print(f'Вторая карта: {card_name(card2)}')

        # Определяем диапазон
        low_card = min(card1, card2)
        high_card = max(card1, card2)
        
        # Делаем ставку
        while True:
            try:
                bet = int(input(f'Сделайте ставку (от 1 до {money}): '))
                if bet < 1 or bet > money:
                    print('Неверная ставка. Попробуйте снова.')
                    continue
                break
            except ValueError:
                print('Пожалуйста, введите число.')
                continue
        
        # Вытягиваем следующую карту
        next_card = deck.pop()
        print(f'Следующая карта: {card_name(next_card)}')
        
        # Проверяем результат
        if next_card == card1 or next_card == card2 or next_card == 14 or not (low_card < next_card < high_card):
             print('Вы проиграли!')
             money -= bet
        else:
            print('Вы выиграли!')
            money += bet

        print()
    
    # Завершение игры
    if money <= 0:
        print('У вас закончились деньги. Игра окончена.')
    else:
        print(f'Игра окончена. Ваш итоговый баланс: ${money}')

# Запуск игры
if __name__ == '__main__':
    play_acey_ducey()
```