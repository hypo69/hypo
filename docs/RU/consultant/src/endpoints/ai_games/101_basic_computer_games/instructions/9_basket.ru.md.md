# Анализ кода модуля basket.ru.md

**Качество кода**
7
-  Плюсы
    - Документ предоставляет четкие инструкции для реализации игры "Basketball".
    - Описаны основные правила игры, структура игрового цикла, обработки ходов игрока и определения результатов.
    - Приведен пример диалога, демонстрирующий ход игры.

-  Минусы
    - Документ не является кодом, а скорее инструкцией для разработки кода, поэтому не соответствует всем критериям, относящимся к структуре кода.
    - Отсутствуют reStructuredText комментарии, так как это инструкция, а не код.
    - Не используется `j_loads` или `j_loads_ns`, так как это инструкция, а не код.
    - Отсутствует обработка ошибок, поскольку это не код.
    - Отсутствуют импорты, т.к. это инструкция, а не код.

**Рекомендации по улучшению**

-   Преобразовать инструкцию в исполняемый код Python с использованием предоставленных указаний.
-   Добавить reStructuredText комментарии для всех функций, классов и методов.
-   Использовать `j_loads` или `j_loads_ns` для чтения файлов, если потребуется.
-   Включить логирование ошибок с помощью `from src.logger.logger import logger`.
-   Обработать возможные ошибки с помощью `logger.error`.
-   Обеспечить возможность повторного запуска игры.
-   Реализовать функции для всех этапов игры: инициализация, основной игровой цикл, обработка ввода игрока, определение результата, завершение игры.

**Оптимизированный код**
```python
"""
Модуль для реализации игры "Basketball".
=========================================================================================

Этот модуль содержит функции для симуляции баскетбольной игры,
включая инициализацию игры, основной игровой цикл, обработку хода игрока
и определение результата броска или защиты.

Пример использования
--------------------

Пример запуска игры:

.. code-block:: python

    game = BasketBallGame()
    game.play_game()
"""
import random
from src.logger.logger import logger  # Добавлен импорт logger


class BasketBallGame:
    """
    Класс для управления игрой в баскетбол.

    :ivar team1_score: Счет первой команды.
    :vartype team1_score: int
    :ivar team2_score: Счет второй команды.
    :vartype team2_score: int
    :ivar current_quarter: Текущая четверть.
    :vartype current_quarter: int
    :ivar current_team: Текущая команда (0 - атакует, 1 - защищается).
    :vartype current_team: int
    """
    def __init__(self):
        """
        Инициализирует игру, устанавливая начальные значения счета, четверти и текущей команды.
        """
        self.team1_score = 0
        self.team2_score = 0
        self.current_quarter = 1
        self.current_team = 0  # 0 - атакует, 1 - защищается

    def play_game(self):
        """
        Запускает основной игровой цикл.
        """
        logger.info('Игра началась')  # Логирование начала игры
        while self.current_quarter <= 4:
            logger.info(f'Четверть {self.current_quarter}.')  # Логирование начала четверти
            if self.current_team == 0:
                self.handle_attack()
            else:
                self.handle_defense()
            self.switch_teams()

        self.end_game()

    def handle_attack(self):
        """
        Обрабатывает атакующий ход игрока.
        """
        try:
            # Код запрашивает ввод типа броска у игрока
            print('Ваша команда атакует.')
            choice = input('Выберите тип броска (1 - длинный, 2 - средний, 3 - подбор): ')
            if not choice.isdigit():
                print('Некорректный ввод. Пожалуйста, введите число.')
                self.handle_attack()
                return
            choice = int(choice)

            # Код определяет результат броска
            result = self.determine_shot_result(choice)
            if result == 2:
                self.team1_score += 2
                print('Средний бросок! Вы заработали два очка.')
            elif result == 3:
                self.team1_score += 3
                print('Длинный бросок! Вы заработали три очка.')
            else:
                print('Промах!')
            logger.info(f'Результат броска: {result}. Счет: {self.team1_score}-{self.team2_score}')

        except Exception as ex:
            logger.error('Ошибка обработки атаки.', ex)
            ...

    def handle_defense(self):
        """
        Обрабатывает защитный ход игрока.
        """
        try:
            # Код запрашивает ввод типа защиты у игрока
            print('Ваша команда защищается.')
            choice = input('Выберите тип защиты (1 - зона, 2 - человек на человеке, 3 - прессинг): ')

            if not choice.isdigit():
                print('Некорректный ввод. Пожалуйста, введите число.')
                self.handle_defense()
                return
            choice = int(choice)
            # Код определяет результат защиты
            result = self.determine_defense_result(choice)
            if result == 'блок':
                print('Блок! Противник потерял мяч.')
            elif result == 'перехват':
                print('Перехват! Вы завладели мячом.')
            elif result == 'фол':
                print('Фол! Противник получает штрафной.')
            else:
                 print('Успешная защита.')

            logger.info(f'Результат защиты: {result}. Счет: {self.team1_score}-{self.team2_score}')
        except Exception as ex:
            logger.error('Ошибка обработки защиты.', ex)
            ...

    def determine_shot_result(self, choice):
        """
        Определяет результат броска на основе выбора игрока и случайного числа.

        :param choice: Выбор типа броска игроком.
        :type choice: int
        :return: Результат броска (0 - промах, 2 - двухочковый, 3 - трехочковый).
        :rtype: int
        """
        # Код возвращает результат броска
        if choice == 1:  # Длинный бросок
            return random.choice([0, 0, 3])
        elif choice == 2:  # Средний бросок
            return random.choice([0, 0, 2])
        elif choice == 3:  # Подбор
            return random.choice([0, 0, 2])  # Подбор может дать 2 очка
        else:
            return 0

    def determine_defense_result(self, choice):
        """
        Определяет результат защиты на основе выбора игрока и случайного числа.

        :param choice: Выбор типа защиты игроком.
        :type choice: int
        :return: Результат защиты (блок, перехват, фол или успешная защита).
        :rtype: str
        """
        # Код возвращает результат защиты
        if choice == 1:  # Зона
            return random.choice(['успешная защита','успешная защита', 'блок'])
        elif choice == 2:  # Человек на человеке
           return random.choice(['успешная защита', 'успешная защита', 'перехват'])
        elif choice == 3:  # Прессинг
           return random.choice(['успешная защита', 'успешная защита', 'фол'])
        else:
             return 'успешная защита'

    def switch_teams(self):
        """
        Переключает текущую команду и увеличивает номер четверти.
        """
        # Код переключает команды и увеличивает номер четверти
        self.current_team = 1 - self.current_team
        if self.current_team == 0:
            self.current_quarter += 1
        logger.info(f'Команда переключена. Текущая команда: {self.current_team}, Четверть: {self.current_quarter}')

    def end_game(self):
        """
        Завершает игру, определяет победителя и выводит результаты.
        """
        # Код определяет победителя и выводит результат
        print('Игра завершена.')
        print(f'Счет: {self.team1_score}-{self.team2_score}')
        if self.team1_score > self.team2_score:
            print('Ваша команда победила!')
        elif self.team1_score < self.team2_score:
            print('Команда противника победила!')
        else:
            print('Ничья!')
        logger.info('Игра завершена.')


if __name__ == '__main__':
    game = BasketBallGame()
    game.play_game()