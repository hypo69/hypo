# Анализ кода модуля `banner.py`

**Качество кода**
6
- Плюсы
    - Код игры достаточно простой для понимания и соответствует описанию.
    - Имеется блок-схема и описание алгоритма.
- Минусы
    - Отсутствует docstring для модуля.
    - Используются стандартные комментарии вместо reStructuredText (RST).
    - Имеется дублирование кода, например, в условиях `if action == "купить" or action == "buy":` и т.д.
    - Не используется логирование ошибок.
    - Использование `locals()` может быть небезопасным.
    - Отсутствуют проверки на ввод для количества меха при покупке и продаже на предмет не отрицательных значений.
    - При перемещении в тот же город не выводит сообщение "Вы уже находитесь в этом городе."

**Рекомендации по улучшению**
1. Добавить docstring для модуля в формате RST.
2. Заменить все комментарии на RST.
3. Устранить дублирование кода, например, можно создать функцию для обработки ввода.
4. Использовать логирование ошибок через `logger.error` вместо `print`.
5. Использовать более безопасный способ доступа к переменным вместо `locals()`.
6. Добавить проверки ввода для количества меха при покупке и продаже на неотрицательные значения.
7. При перемещении в тот же город выводить сообщение "Вы уже находитесь в этом городе."
8. Добавить обработку исключения для нечислового ввода в количествах покупаемого и продаваемого меха.

**Оптимизированный код**
```python
"""
Модуль имитации торговли мехом между городами.
=========================================================================================

Модуль предоставляет игру "Меховые Торговцы", экономическую симуляцию, где игрок торгует мехом
между тремя городами (А, Б и С). Цель игры - накопить как можно больше денег за 10 ходов.

Пример использования
--------------------

Пример запуска игры::

    python banner.py

"""
import random
from src.logger.logger import logger

# Инициализация переменных
playerMoney = 1000  # Начальное количество денег
playerFur = 10    # Начальное количество меха
currentCity = 'A' # Начальный город
turnNumber = 1    # Номер текущего хода


def get_price(city: str) -> int:
    """
    Получает цену на мех в указанном городе.

    :param city: Город, для которого нужно получить цену.
    :return: Цена на мех в указанном городе.
    """
    if city == 'A':
        return random.randint(100, 500)
    if city == 'B':
        return random.randint(100, 500)
    if city == 'C':
        return random.randint(100, 500)
    logger.error(f'Некорректный город: {city}')
    return 0



def process_action(action: str, current_city: str) -> None:
    """
    Обрабатывает действие игрока.

    :param action: Действие игрока (купить, продать, переместиться, ждать).
    :param current_city: Текущий город игрока.
    """
    global playerMoney, playerFur, currentCity  # Объявляем переменные как глобальные
    if action in ("купить", "buy"):
        try:
            amount = int(input("Сколько меха купить? "))
            if amount <=0:
                 print("Количество меха должно быть положительным числом.")
                 return
            price = get_price(current_city)
            if playerMoney >= amount * price:
                playerMoney -= amount * price
                playerFur += amount
                print("Покупка совершена.")
            else:
                print("Недостаточно денег.")
        except ValueError:
            print("Некорректный ввод.")
            logger.error("Некорректный ввод при покупке меха.")
            ...
    elif action in ("продать", "sell"):
        try:
            amount = int(input("Сколько меха продать? "))
            if amount <=0:
                 print("Количество меха должно быть положительным числом.")
                 return
            if playerFur >= amount:
                price = get_price(current_city)
                playerMoney += amount * price
                playerFur -= amount
                print("Продажа совершена.")
            else:
                print("Недостаточно меха.")
        except ValueError:
             print("Некорректный ввод.")
             logger.error("Некорректный ввод при продаже меха.")
             ...
    elif action in ("переместиться", "move"):
        city = input("В какой город переместиться (A, B, C)? ").upper()
        if city in ('A', 'B', 'C'):
            if city != currentCity:
                cost = playerMoney * 0.1
                playerMoney -= cost
                currentCity = city
                print(f"Перемещение в {currentCity}. Стоимость: {cost}")
            else:
                 print("Вы уже находитесь в этом городе.")
        else:
            print("Некорректный город.")
    elif action in ("ждать", "wait"):
        print("Ожидание...")
    else:
        print("Неверное действие.")

# Основной игровой цикл
while turnNumber <= 10:
    # Генерируем случайные цены для каждого города
    priceA = get_price('A')
    priceB = get_price('B')
    priceC = get_price('C')
    # Выводим текущие цены и состояние игрока
    print(f"\n--- Ход {turnNumber} ---")
    print(f"Цены на мех: A={priceA}, B={priceB}, C={priceC}")
    print(f"Деньги: {playerMoney}, Мех: {playerFur}, Город: {currentCity}")
    # Запрашиваем действие игрока
    action = input("Действие (купить/buy, продать/sell, переместиться/move, ждать/wait): ").lower()
    # Обрабатываем действие игрока
    process_action(action, currentCity)
    turnNumber += 1  # Переходим к следующему ходу

# Подсчитываем итоговый капитал
finalCapital = playerMoney + (playerFur * get_price(currentCity))
print(f"\n--- Итого ---")
print(f"Общий капитал: {finalCapital}")
```