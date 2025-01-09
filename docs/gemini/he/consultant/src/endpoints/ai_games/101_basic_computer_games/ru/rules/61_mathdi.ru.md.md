# Анализ кода модуля `61_mathdi.ru.md`

**Качество кода**
- **Соответствие требованиям к формату кода (1-10):**
  - **Плюсы:**
    - Код представляет собой подробное описание игровой логики и правил игры `MATHDI` на русском языке.
    - Структура документа хорошо организована и понятна, разделена на основные разделы и подпункты.
    - Приведены примеры работы программы, которые наглядно показывают процесс игры.
    - Описаны возможные ограничения и реализации игры, а также предложены улучшения.
  - **Минусы:**
    -  Представленный файл `markdown`, а не код на `python`.
    - Отсутствуют docstrings и аннотации типов.
    - Нет обработки ошибок и логирования.

**Рекомендации по улучшению**
- Необходимо преобразовать описание игры в код на Python.
- Добавить обработку исключений и логирование.
- Реализовать функции для генерации задач и подсчёта очков.
- Использовать docstrings и аннотации типов для улучшения читаемости и документирования кода.

**Улучшенный код**

```python
"""
Модуль для реализации математической дуэльной игры MATHDI.
============================================================

Этот модуль содержит функции для создания и управления игрой,
включая генерацию математических задач, оценку ответов и
ведение счета.

Пример использования
--------------------

    mathdi_game = MathDui()
    mathdi_game.start_game()

"""
import random
from typing import Tuple, List

from src.logger.logger import logger  # Импорт logger


class MathDui:
    """
    Класс для управления игрой "Математическая дуэль".

    :ivar player1_name: Имя первого игрока.
    :vartype player1_name: str
    :ivar player2_name: Имя второго игрока.
    :vartype player2_name: str
    :ivar rounds: Количество раундов в игре.
    :vartype rounds: int
    :ivar player1_score: Счет первого игрока.
    :vartype player1_score: int
    :ivar player2_score: Счет второго игрока.
    :vartype player2_score: int
    """

    def __init__(self):
        """
        Инициализирует игру, устанавливая начальные значения.
        """
        self.player1_name: str = ''
        self.player2_name: str = ''
        self.rounds: int = 0
        self.player1_score: int = 0
        self.player2_score: int = 0

    def _get_players_names(self) -> Tuple[str, str]:
        """
        Запрашивает и возвращает имена игроков.

        :return: Имена первого и второго игроков.
        :rtype: tuple[str, str]
        """
        try:
            player1_name = input('Введите имя Игрока 1: ')
            player2_name = input('Введите имя Игрока 2: ')
            return player1_name, player2_name
        except Exception as e:
            logger.error('Ошибка при вводе имен игроков', e)
            return '', ''

    def _get_rounds_number(self) -> int:
        """
        Запрашивает и возвращает количество раундов для игры.

        :return: Количество раундов.
        :rtype: int
        """
        while True:
            try:
                rounds = int(input('Введите количество раундов: '))
                if 1 <= rounds <= 50:
                    return rounds
                else:
                    print('Количество раундов должно быть от 1 до 50.')
            except ValueError:
                logger.error('Ошибка при вводе количества раундов. Введите целое число.')
                print('Ошибка ввода. Пожалуйста, введите целое число.')
            except Exception as e:
                logger.error('Неизвестная ошибка при вводе количества раундов', e)
                return 0

    def _generate_task(self, round_num: int) -> Tuple[str, int]:
        """
        Генерирует случайную математическую задачу.

        :param round_num: Номер текущего раунда (для возможного изменения сложности).
        :type round_num: int
        :return: Сгенерированная задача и правильный ответ.
        :rtype: tuple[str, int]
        """
        try:
            operation = random.choice(['+', '-', '*', '/'])
            if operation == '/':
                num1 = random.randint(2, 15) * random.randint(1, 10)
                num2 = random.randint(1, 10)
                if num2 == 0:
                    num2 = 1
            else:
                num1 = random.randint(1, 100)
                num2 = random.randint(1, 100)

            task = f'{num1} {operation} {num2} = ?'

            if operation == '+':
                answer = num1 + num2
            elif operation == '-':
                answer = num1 - num2
            elif operation == '*':
                answer = num1 * num2
            else:
                answer = int(num1 / num2)
            return task, answer
        except ZeroDivisionError:
            logger.error("Попытка деления на ноль при генерации задачи.")
            return '1 + 1 = ?', 2
        except Exception as e:
            logger.error('Неизвестная ошибка при генерации задачи', e)
            return '1 + 1 = ?', 2

    def _check_answer(self, answer: int, correct_answer: int) -> bool:
        """
        Проверяет правильность ответа игрока.

        :param answer: Ответ игрока.
        :type answer: int
        :param correct_answer: Правильный ответ.
        :type correct_answer: int
        :return: `True`, если ответ верный, иначе `False`.
        :rtype: bool
        """
        return answer == correct_answer

    def _play_round(self, player_name: str, round_num: int) -> int:
        """
        Проводит один раунд игры для одного игрока.

        :param player_name: Имя игрока.
        :type player_name: str
        :param round_num: Номер текущего раунда.
        :type round_num: int
        :return: Набранные игроком очки за раунд.
        :rtype: int
        """
        task, correct_answer = self._generate_task(round_num)
        print(f'Вопрос для {player_name}: {task}')
        try:
            answer = int(input('> '))
            if self._check_answer(answer, correct_answer):
                print('Правильно! Вы заработали 10 баллов.')
                return 10
            else:
                print(f'Неправильно. Правильный ответ: {correct_answer}.')
                return 0
        except ValueError:
            logger.error(f'Ошибка ввода ответа от игрока {player_name}. Введите целое число.')
            print('Ошибка ввода. Пожалуйста, введите целое число.')
            return 0
        except Exception as e:
            logger.error(f'Неизвестная ошибка при проверке ответа игрока {player_name}', e)
            return 0

    def _display_scores(self, round_num: int):
        """
        Выводит текущие результаты игры.

        :param round_num: Номер текущего раунда.
        :type round_num: int
        """
        print(f'Результаты после раунда {round_num}:')
        print(f'{self.player1_name}: {self.player1_score} баллов')
        print(f'{self.player2_name}: {self.player2_score} баллов')

    def _display_winner(self):
        """
        Выводит результаты игры и объявляет победителя.
        """
        print('Игра окончена!')
        print('Финальные результаты:')
        print(f'{self.player1_name}: {self.player1_score} баллов')
        print(f'{self.player2_name}: {self.player2_score} баллов')
        if self.player1_score > self.player2_score:
            print(f'Победитель: {self.player1_name}! Поздравляем!')
        elif self.player2_score > self.player1_score:
            print(f'Победитель: {self.player2_name}! Поздравляем!')
        else:
            print('Это ничья!')

    def start_game(self):
        """
        Запускает игру и управляет её ходом.
        """
        print('Добро пожаловать в MATHDI — Математическую дуэль!')
        print('Два игрока будут соревноваться, решая математические задачи.')
        print('За правильный ответ вы получаете 10 баллов.')
        print('Выигрывает тот, кто наберёт больше баллов за N раундов!')
        print('Удачи!')

        self.player1_name, self.player2_name = self._get_players_names()
        if not self.player1_name or not self.player2_name:
            print('Не удалось получить имена игроков. Завершение игры.')
            return

        self.rounds = self._get_rounds_number()
        if not self.rounds:
            print('Не удалось получить количество раундов. Завершение игры.')
            return

        print('Игра начинается!')

        for round_num in range(1, self.rounds + 1):
            self.player1_score += self._play_round(self.player1_name, round_num)
            self.player2_score += self._play_round(self.player2_name, round_num)
            self._display_scores(round_num)

        self._display_winner()
        self._play_again()

    def _play_again(self):
        """
        Спрашивает у пользователей, хотят ли они сыграть снова, и начинает новую игру, если ответ положительный.
        """
        while True:
            play_again = input('Хотите сыграть снова? (да/нет): ').lower()
            if play_again == 'да':
                self.__init__()
                self.start_game()
                break
            elif play_again == 'нет':
                print('Спасибо за игру!')
                break
            else:
                print('Некорректный ввод. Пожалуйста, введите "да" или "нет".')


if __name__ == '__main__':
    mathdi_game = MathDui()
    mathdi_game.start_game()
```