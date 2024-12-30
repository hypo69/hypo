## Анализ кода модуля 86_stock.ru.md

**Качество кода**
- **Соответствие требованиям к формату кода с 1 по 10:**
    -  **Преимущества:**
        -  Описание игры и инструкции представлены в формате Markdown, что обеспечивает хорошую читаемость.
        -  Четко разделены основные этапы реализации игры.
        -  Приведены примеры работы программы, которые помогают понять игровой процесс.
    -  **Недостатки:**
        -  Отсутствует код на языке Python, требуются дополнительные усилия для реализации игры на основе предоставленной документации.
        -  Не используется reStructuredText (RST) для оформления документации, как требуется.
        -  Нет примеров кода для работы с `j_loads` или `j_loads_ns`.
        -  Не указаны импорты, которые необходимы для реализации игры.
        -  Отсутствуют docstring для функций и классов.
        -  Нет обработки ошибок в примерах кода.
        -  Не используется `from src.logger.logger import logger` для регистрации ошибок.
        -  Не используется reStructuredText (RST) для оформления документации.

**Рекомендации по улучшению**

1.  **Преобразование в reStructuredText (RST):** Необходимо перевести все комментарии и инструкции в формат RST для соответствия требованиям.
2.  **Реализация кода:**  Необходимо написать код на Python для реализации описанной логики игры, включая все необходимые функции и классы.
3.  **Использование `j_loads` или `j_loads_ns`:**  В коде при работе с JSON файлами необходимо использовать `j_loads` или `j_loads_ns` из `src.utils.jjson`.
4.  **Добавление docstring:** Добавить docstring для всех функций, методов и классов в формате RST.
5.  **Обработка ошибок:**  Использовать `logger.error` для регистрации ошибок вместо стандартных `try-except` блоков.
6.  **Импорты:** Добавить необходимые импорты для работы с кодом, например, `random`, `json` и другие.
7.  **Логирование:**  Использовать `from src.logger.logger import logger` для логирования ошибок и отладки.
8.  **Примеры кода:**  Привести примеры кода с использованием RST для документации и примеры реализации функций.
9.  **Тестирование:**  Необходимо проверить код на соответствие требованиям и исправить найденные ошибки.

**Улучшенный код**

```python
"""
Модуль для реализации игры "Акции"
=========================================================================================

Модуль содержит функции и классы для управления игровым процессом в игре "Акции",
включая инициализацию игры, совершение ходов и обновление данных.

Пример использования
--------------------

Пример запуска игры "Акции":

.. code-block:: python

    game = StockGame()
    game.start_game()
"""
import random # Импортируем модуль random для генерации случайных чисел
from src.logger.logger import logger # Импортируем logger для регистрации ошибок
from src.utils.jjson import j_loads # Импортируем j_loads для загрузки JSON
#from typing import Dict, List # Импортируем Dict, List для аннотации типов


class StockGame:
    """
    Класс, представляющий игру "Акции".

    :ivar stocks: Словарь, содержащий информацию об акциях (название: цена).
    :vartype stocks: dict
    :ivar player_balance: Баланс игрока.
    :vartype player_balance: int
    :ivar player_stocks: Словарь, содержащий количество акций игрока (название: количество).
    :vartype player_stocks: dict
    :ivar days_left: Количество дней до конца игры.
    :vartype days_left: int
    """
    def __init__(self, initial_balance: int = 1000, game_days: int = 10):
        """
        Инициализирует игру "Акции".

        :param initial_balance: Начальный баланс игрока.
        :type initial_balance: int
        :param game_days: Количество дней игры.
        :type game_days: int
        """
        self.stocks = {
            'A': random.randint(30, 80),  # Начальная цена акции A
            'B': random.randint(20, 60),  # Начальная цена акции B
            'C': random.randint(50, 100) # Начальная цена акции C
        }
        self.player_balance = initial_balance
        self.player_stocks = {stock: 0 for stock in self.stocks}
        self.days_left = game_days

    def display_game_info(self):
        """
        Выводит текущую информацию об игре: цены на акции, баланс игрока и количество акций в наличии.
        """
        print(f'День: {10 - self.days_left + 1}')
        for stock, price in self.stocks.items():
            print(f'Акции компании {stock}: ${price}')
        print(f'Ваш баланс: ${self.player_balance}')
        print('Ваши акции:')
        for stock, count in self.player_stocks.items():
             print(f'Компания {stock}: {count}')
        print()

    def update_stock_prices(self):
        """
        Обновляет цены на акции случайным образом.
        """
        for stock in self.stocks:
            change = random.randint(-10, 10)
            self.stocks[stock] = max(1, self.stocks[stock] + change) # Устанавливаем минимальную цену 1

    def buy_stock(self, stock: str, quantity: int):
        """
        Покупает акции.

        :param stock: Название акции для покупки.
        :type stock: str
        :param quantity: Количество акций для покупки.
        :type quantity: int
        """
        price = self.stocks[stock]
        cost = price * quantity
        if self.player_balance >= cost:
            self.player_balance -= cost
            self.player_stocks[stock] += quantity
            print(f'Куплено {quantity} акций компании {stock} за ${cost}.')
        else:
           logger.error('Недостаточно средств для покупки.') # Используем logger для регистрации ошибки
           print('Недостаточно средств для покупки. Попробуйте снова.')

    def sell_stock(self, stock: str, quantity: int):
        """
        Продает акции.

        :param stock: Название акции для продажи.
        :type stock: str
        :param quantity: Количество акций для продажи.
        :type quantity: int
        """
        if self.player_stocks[stock] >= quantity:
            price = self.stocks[stock]
            revenue = price * quantity
            self.player_balance += revenue
            self.player_stocks[stock] -= quantity
            print(f'Продано {quantity} акций компании {stock} за ${revenue}.')
        else:
            logger.error('Недостаточно акций для продажи.') # Используем logger для регистрации ошибки
            print('Недостаточно акций для продажи. Попробуйте снова.')

    def player_turn(self):
        """
        Обрабатывает ход игрока: выбор действия (купить, продать, ничего не делать) и ввод данных.
        """
        while True: # Запускаем цикл для обработки действий
            self.display_game_info() # Выводим информацию об игре
            print('Выберите действие:')
            print('1. Купить акции')
            print('2. Продать акции')
            print('3. Ничего не делать')

            try:
                choice = int(input('> ')) # Получаем ввод от игрока
                if choice not in [1, 2, 3]: # Если выбор неверный
                    logger.error('Неверный выбор действия') # Регистрируем ошибку
                    print('Неверный ввод. Попробуйте снова.')
                    continue
            except ValueError:
                logger.error('Неверный ввод. Попробуйте снова.') # Регистрируем ошибку
                print('Неверный ввод. Попробуйте снова.')
                continue

            if choice == 1:
                while True: # Запускаем цикл для выбора акций
                    stock = input('Введите название компании для покупки: ').upper()
                    if stock not in self.stocks:
                       logger.error('Неверный выбор компании.') # Регистрируем ошибку
                       print('Неверный выбор компании. Попробуйте снова.')
                       continue
                    try:
                        quantity = int(input('Введите количество акций для покупки: ')) # Получаем количество акций
                        if quantity <= 0:
                           logger.error('Количество акций должно быть больше нуля') # Регистрируем ошибку
                           print('Количество акций должно быть больше нуля. Попробуйте снова.')
                           continue
                        break
                    except ValueError:
                        logger.error('Неверный ввод количества акций') # Регистрируем ошибку
                        print('Неверный ввод количества акций. Попробуйте снова.')
                self.buy_stock(stock, quantity)
                break
            elif choice == 2:
                while True:
                    stock = input('Введите название компании для продажи: ').upper()
                    if stock not in self.stocks:
                       logger.error('Неверный выбор компании') # Регистрируем ошибку
                       print('Неверный выбор компании. Попробуйте снова.')
                       continue
                    try:
                        quantity = int(input('Введите количество акций для продажи: '))
                        if quantity <= 0:
                           logger.error('Количество акций должно быть больше нуля') # Регистрируем ошибку
                           print('Количество акций должно быть больше нуля. Попробуйте снова.')
                           continue
                        break
                    except ValueError:
                       logger.error('Неверный ввод количества акций') # Регистрируем ошибку
                       print('Неверный ввод количества акций. Попробуйте снова.')
                self.sell_stock(stock, quantity)
                break
            else:
                print('Вы решили ничего не делать.')
                break

    def end_game(self):
        """
        Завершает игру, выводит итоговый баланс игрока.
        """
        total_value = self.player_balance
        for stock, count in self.player_stocks.items():
            total_value += count * self.stocks[stock]
        print('Игра окончена!')
        print(f'Ваш итоговый баланс: ${total_value}')

    def start_game(self):
        """
        Запускает игру и управляет игровым процессом.
        """
        print('Добро пожаловать в STOCK!')
        print(
            'Ваша задача — управлять портфелем акций, покупая и продавая акции на основе прогнозов рынка.'
        )
        print(
            'Цель игры — максимизировать прибыль, покупая акции по низкой цене и продавая их по высокой.'
        )
        print(f'Игра продолжается в течение {10} дней.')
        print('Удачи!')
        while self.days_left > 0:
            self.player_turn()
            self.update_stock_prices()
            self.days_left -= 1
        self.end_game()
        play_again = input('Хотите сыграть снова? (да/нет): ').lower()
        if play_again == 'да':
            self.__init__()
            self.start_game()
        else:
            print('Спасибо за игру!')