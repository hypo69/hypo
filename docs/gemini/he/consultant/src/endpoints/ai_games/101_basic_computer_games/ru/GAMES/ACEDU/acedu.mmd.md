# Анализ кода модуля `acedu.mmd`

**Качество кода**

-  **Соблюдение требований к формату кода (1-10):** 
    - Код представляет собой блок-схему, а не код Python, поэтому требования к оформлению кода Python и docstring не применимы.
    - Формат Markdown корректен для представления блок-схемы.
 -  **Преимущества:**
        - Блок-схема четко описывает логику игры Acey Ducey.
        - Легко понять последовательность действий в игре.
 -  **Недостатки:**
    - Код не является исполняемым кодом Python и не соответствует требованиям к оформлению кода Python.
    - Отсутствует использование `j_loads` или `j_loads_ns` и импорта logger, как указано в требованиях.

**Рекомендации по улучшению**

1. **Преобразование в исполняемый код**: Необходимо преобразовать блок-схему в исполняемый код Python, используя принципы, описанные в блок-схеме.
2. **Добавление документации**: Добавить docstring в формате RST для модуля, классов и методов.
3. **Обработка ошибок**: Использовать `logger.error` для обработки ошибок.
4. **Применение `j_loads` и `j_loads_ns`**: Если требуется загрузка данных из файлов, использовать соответствующие функции из `src.utils.jjson`.
5. **Импорт логгера**: Добавить импорт логгера: `from src.logger.logger import logger`.
6. **Форматирование**: Вставить код в блок форматирования `python` для удобства.

**Улучшенный код**

```python
"""
Модуль для реализации игры Acey Ducey.
=========================================================================================

Модуль содержит логику для игры Acey Ducey, включая создание колоды,
обработку ставок и проверку результатов.

Пример использования
--------------------

Пример запуска игры:

.. code-block:: python

    game = AceyDucey()
    game.play()
"""
import random
from src.logger.logger import logger # Добавлен импорт логгера
from typing import List # Добавлен импорт List

class AceyDucey:
    """
    Класс для представления игры Acey Ducey.

    :ivar deck: Список карт в колоде.
    :vartype deck: List[str]
    :ivar balance: Баланс игрока.
    :vartype balance: int
    """
    def __init__(self):
        """
        Инициализирует игру, создавая колоду и устанавливая начальный баланс.
        """
        self.deck: List[str] = self._create_deck() # Инициализация колоды
        self.balance: int = 100  # Начальный баланс игрока
        logger.info('Игра Acey Ducey инициализирована') # Запись в лог о начале игры

    def _create_deck(self) -> List[str]:
        """
        Создает стандартную колоду из 52 карт.

        :return: Список карт в колоде.
        :rtype: List[str]
        """
        suits = ['♥', '♦', '♣', '♠'] # Масти карт
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] # Значения карт
        deck: List[str] = [rank + suit for suit in suits for rank in ranks] # Создание колоды
        random.shuffle(deck) # Перемешивание колоды
        logger.debug('Создана и перемешана колода') # Запись в лог о создании колоды
        return deck

    def _deal_cards(self) -> List[str]:
        """
        Выдает две карты из колоды.

        :return: Список из двух карт.
        :rtype: List[str]
        :raises IndexError: Если в колоде меньше двух карт.
        """
        if len(self.deck) < 2: # Проверка наличия карт в колоде
            logger.error('Недостаточно карт в колоде для раздачи') # Запись об ошибке в лог
            raise IndexError('Недостаточно карт в колоде') # Вызов ошибки
        cards = self.deck[:2] # Выбор первых двух карт
        self.deck = self.deck[2:] # Удаление выбранных карт из колоды
        logger.debug(f'Выданы карты: {cards}') # Запись в лог о выданных картах
        return cards

    def _get_card_value(self, card: str) -> int:
         """
         Возвращает числовое значение карты.

         :param card: Строка, представляющая карту (например, '10♥', 'A♠').
         :type card: str
         :return: Числовое значение карты (2-14).
         :rtype: int
         """
         rank = card[:-1] # Извлечение значения карты
         if rank.isdigit(): # Если значение - число
            return int(rank) # Возвращаем значение как int
         elif rank == 'J': # Если значение - валет
            return 11 # Возвращаем 11
         elif rank == 'Q': # Если значение - дама
            return 12 # Возвращаем 12
         elif rank == 'K': # Если значение - король
            return 13 # Возвращаем 13
         elif rank == 'A': # Если значение - туз
            return 14 # Возвращаем 14
         logger.error(f'Некорректное значение карты: {card}') # Запись об ошибке в лог
         return 0 # Возврат 0 в случае ошибки

    def _check_result(self, cards: List[str], next_card: str) -> bool:
        """
        Проверяет, выиграл ли игрок.

        :param cards: Список из двух карт.
        :type cards: List[str]
        :param next_card: Следующая вытянутая карта.
        :type next_card: str
        :return: True, если игрок выиграл, False - в противном случае.
        :rtype: bool
        """
        card1_val = self._get_card_value(cards[0]) # Получение значения первой карты
        card2_val = self._get_card_value(cards[1]) # Получение значения второй карты
        next_card_val = self._get_card_value(next_card) # Получение значения следующей карты

        if card1_val > card2_val: # Проверка порядка карт
           card1_val, card2_val = card2_val, card1_val

        if card1_val < next_card_val < card2_val: # Проверка выигрыша
            logger.debug(f'Выигрыш. Карты: {cards}, следующая карта: {next_card}') # Запись в лог о выигрыше
            return True # Игрок выиграл
        logger.debug(f'Проигрыш. Карты: {cards}, следующая карта: {next_card}') # Запись в лог о проигрыше
        return False # Игрок проиграл

    def play(self):
        """
        Запускает игровой цикл.
        """
        print('Добро пожаловать в Acey Ducey!') # Приветствие игрока
        while self.balance > 0 and len(self.deck) >= 3: # Основной цикл игры
            print(f'Ваш баланс: ${self.balance}') # Вывод баланса
            cards = self._deal_cards() # Раздача двух карт

            if self._get_card_value(cards[0]) == self._get_card_value(cards[1]): # Проверка на одинаковые карты
                 logger.warning(f'Выпали одинаковые карты, пересдача: {cards}') # Предупреждение о пересдаче
                 self.deck.extend(cards) # Возврат карт в колоду
                 random.shuffle(self.deck) # Перемешивание колоды
                 continue # Переход к следующему циклу

            print(f'Карты: {cards[0]}, {cards[1]}') # Вывод карт

            while True:
                try:
                   bet = int(input('Сделайте ставку (0 для пропуска): ')) # Запрос ставки
                   if bet < 0:
                      print('Ставка должна быть неотрицательной') # Сообщение о неправильной ставке
                      continue
                   if bet > self.balance:
                     print('Ставка не может превышать баланс') # Сообщение о превышении баланса
                     continue
                   break
                except ValueError:
                    print('Некорректный ввод. Введите целое число.') # Сообщение об ошибке ввода

            if bet == 0:
                print('Ход пропущен.') # Сообщение о пропуске хода
                continue # Переход к следующему циклу

            next_card = self.deck.pop(0) # Вытягивание следующей карты
            print(f'Следующая карта: {next_card}') # Вывод следующей карты

            if self._check_result(cards, next_card): # Проверка результата
                self.balance += bet # Увеличение баланса
                print('Вы выиграли!') # Сообщение о выигрыше
            else:
                self.balance -= bet # Уменьшение баланса
                print('Вы проиграли.') # Сообщение о проигрыше
            logger.debug(f'Баланс после раунда: {self.balance}') # Запись в лог о текущем балансе

        print(f'Игра окончена. Ваш итоговый баланс: ${self.balance}') # Сообщение о конце игры

if __name__ == '__main__':
    game = AceyDucey() # Создание экземпляра игры
    game.play() # Запуск игры
```