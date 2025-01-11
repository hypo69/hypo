# Анализ кода модуля DOGS

**Качество кода**
8
-  Плюсы
    -   Четкое и понятное описание правил игры.
    -   Наличие пошаговой инструкции для реализации.
    -   Приведены примеры работы программы.
    -   Указаны возможные ограничения.
    -   Предложены рекомендации по реализации игры.
-  Минусы
    -   Отсутствует фактический код для анализа.
    -   Необходимо преобразовать текст в исполняемый код.
    -   Нет документации в формате reStructuredText (RST).

**Рекомендации по улучшению**

1.  Преобразовать текстовое описание игры в исполняемый код на Python.
2.  Добавить документацию в формате reStructuredText (RST) для функций, классов и переменных.
3.  Использовать `from src.logger.logger import logger` для логирования ошибок.
4.  Реализовать ввод данных с проверкой на корректность и обрабатывать ошибки ввода с помощью `logger.error`.
5.  Избегать использования стандартных блоков `try-except` там, где можно обойтись `logger.error`.
6.  Разделить логику игры на функции для улучшения читаемости и повторного использования.
7.  Применить `j_loads` или `j_loads_ns` из `src.utils.jjson` при работе с JSON-данными (если они есть).

**Оптимизированный код**

```python
"""
Модуль для реализации игры DOGS (Собачьи бега).
=========================================================================================

Этот модуль содержит реализацию игры в собачьи бега, где игрок делает ставки на одну из нескольких собак,
которые соревнуются на треке. После размещения ставок программа моделирует забег,
выводя на экран движение каждой собаки по треку. Побеждает собака, первой пересёкшая финишную черту.

Пример использования
--------------------

Пример использования:

.. code-block:: python

    game = DogsGame()
    game.run()
"""
import random
from src.logger.logger import logger


class DogsGame:
    """
    Класс, представляющий игру в собачьи бега.

    Содержит методы для инициализации игры, размещения ставок, проведения забега и объявления результатов.
    """

    def __init__(self):
        """
        Инициализирует игру с начальным балансом, количеством собак и длиной трека.
        """
        self.balance = 100  # Начальный баланс игрока
        self.num_dogs = 0  # Количество участвующих собак
        self.track_length = 50 # Длина трека
        self.dog_positions = {} # Словарь для хранения позиций собак
        self.bet_dog = None # Номер собаки на которую сделал ставку игрок
        self.bet_amount = None # Сумма ставки игрока

    def _get_valid_input(self, prompt: str, type_: type, min_: int = None, max_: int = None) -> any:
        """
        Запрашивает ввод данных у пользователя и проверяет его на корректность.

        :param prompt: Сообщение для пользователя.
        :param type_: Ожидаемый тип ввода.
        :param min_: Минимальное значение (если применимо).
        :param max_: Максимальное значение (если применимо).
        :return: Введенное пользователем значение, прошедшее проверку.
        """
        while True:
            try:
                value = type_(input(prompt))
                if min_ is not None and value < min_:
                    print(f'Значение должно быть не меньше {min_}.')
                    continue
                if max_ is not None and value > max_:
                    print(f'Значение должно быть не больше {max_}.')
                    continue
                return value
            except ValueError:
                logger.error('Неверный ввод. Пожалуйста, введите число.')
                print('Неверный ввод. Пожалуйста, введите число.')
            except Exception as e:
                logger.error('Произошла непредвиденная ошибка', e)
                print('Произошла непредвиденная ошибка. Попробуйте еще раз.')
                ...


    def _place_bet(self) -> None:
        """
        Позволяет пользователю сделать ставку на собаку.
        """
        # Запрашивает номер собаки для ставки
        self.bet_dog = self._get_valid_input(f'Укажите номер собаки, на которую хотите поставить (1-{self.num_dogs}): ', int, 1, self.num_dogs)
        # Запрашивает сумму ставки
        self.bet_amount = self._get_valid_input('Укажите сумму ставки: ', int, 1, self.balance)

        if self.bet_amount > self.balance:
            print('Сумма ставки превышает ваш баланс.')
            logger.error(f'Сумма ставки {self.bet_amount} превышает баланс {self.balance}.')
            ...
            self._place_bet()


    def _simulate_race(self) -> int:
        """
        Моделирует забег и возвращает номер собаки-победителя.

        :return: Номер собаки-победителя.
        """
        print('Забег начался!')
        # Инициализируем позиции собак
        self.dog_positions = {dog: 0 for dog in range(1, self.num_dogs + 1)}

        # Моделируем движение собак
        while True:
            for dog in range(1, self.num_dogs + 1):
                # Случайное перемещение собаки
                move = random.randint(1, 6)
                self.dog_positions[dog] += move

            # Выводим текущее положение собак
            for dog, position in self.dog_positions.items():
                print(f'Собака {dog}: {"=" * position}>')

            # Проверяем не пересекла ли какая-нибудь собака финишную черту
            for dog, position in self.dog_positions.items():
                 if position >= self.track_length:
                    return dog # Возвращаем номер собаки которая пересекла финишную черту


    def _calculate_winnings(self, winner_dog: int) -> None:
        """
        Вычисляет выигрыш и обновляет баланс пользователя.

        :param winner_dog: Номер собаки-победителя.
        """
        if self.bet_dog == winner_dog:
            # Коэффициент выигрыша
            multiplier = 2
            winnings = self.bet_amount * multiplier
            self.balance += winnings
            print(f'Вы выиграли! Ваш баланс: ${self.balance}')
        else:
            self.balance -= self.bet_amount
            print(f'Вы проиграли. Ваш баланс: ${self.balance}')


    def _play_again(self) -> bool:
        """
        Спрашивает пользователя, хочет ли он сыграть еще раз.

        :return: True, если пользователь хочет сыграть еще раз, False в противном случае.
        """
        # Запрашивает хочет ли пользователь сыграть еще раз
        answer = input('Хотите сыграть ещё раз? (да/нет): ')
        return answer.lower() == 'да'


    def run(self) -> None:
        """
        Запускает игровой процесс.
        """
        print('Добро пожаловать в игру DOGS!')
        # Запрашивает количество собак
        self.num_dogs = self._get_valid_input('Выберите количество собак (от 3 до 6): ', int, 3, 6)
        # Основной цикл игры
        while self.balance > 0:
            print(f'У вас ${self.balance}.')
            # Просит пользователя сделать ставку
            self._place_bet()
            # Моделирует забег
            winner_dog = self._simulate_race()
            # Выводит победителя
            print(f'Победила собака {winner_dog}!')
            # Вычисляет выигрыш
            self._calculate_winnings(winner_dog)
            if not self._play_again():
                break
            # Если пользователь захотел сыграть еще раз, обнуляем ставки
            self.bet_dog = None
            self.bet_amount = None

        print(f'Спасибо за игру! Ваш итоговый баланс: ${self.balance}')

# Запускаем игру
if __name__ == '__main__':
    game = DogsGame()
    game.run()
```