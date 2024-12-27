# Анализ кода модуля yahtze.py

**Качество кода**
7
- Плюсы
    - Код игры Yahtzee реализован в соответствии с правилами и логикой игры.
    - Присутствуют функции для броска кубиков (`roll_dice`) и расчета очков (`calculate_score`), что способствует модульности.
    - Основная логика игры (`play_yahtzee`) организована в виде циклов и условных операторов, что делает код читаемым.
    - Есть ввод данных от пользователя для выбора кубиков для переброса и выбора категории.
    - Результаты игры выводятся на экран в удобном формате.
    - Есть docstring для функций, объясняющий их назначение.

- Минусы
    - Отсутствуют docstring для модуля.
    - Использование `print` для вывода сообщений и `input` для ввода данных делает код менее гибким и не адаптированным к интеграции с другими частями системы.
    - Нет логирования ошибок.
    - В функциях используется стандартный блок `try-except`, который можно заменить на логирование ошибок.
    - Отсутствует явная проверка на корректность введенных данных.
    -  Используется стандартный `random.randint`, что не гарантирует криптографическую стойкость.
    - Код не соответствует PEP8.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля.
2.  Использовать `src.utils.jjson` для чтения файлов, если это необходимо.
3.  Применять `from src.logger.logger import logger` для логирования ошибок.
4.  Избегать избыточного использования стандартных блоков `try-except`, отдавая предпочтение `logger.error`.
5.  Заменить `print` на логирование через `logger.info` и `input` на методы, получающие ввод данных из вне.
6.  Добавить проверку на корректность введенных данных от пользователя.
7.  Улучшить форматирование кода в соответствии с PEP8.
8.  Уточнить комментарии, чтобы они соответствовали стандарту reStructuredText (RST).
9.  Вместо `random.randint` следует использовать `secrets.SystemRandom().randint`, что обеспечит криптографическую стойкость.
10. Использовать f-строки для форматирования вывода.

**Оптимизированный код**

```python
"""
Модуль для реализации игры Yahtzee.
=========================================================================================

Этот модуль содержит функции для игры в Yahtzee, включая бросок кубиков, подсчет очков и управление игровым процессом.

Пример использования
--------------------

.. code-block:: python

    from src.endpoints.ai_games.101_basic_computer_games.en.YAHTZE.yahtze import play_yahtzee

    play_yahtzee()
"""
import secrets
from typing import List
from src.logger.logger import logger # Импортируем логгер

def roll_dice() -> List[int]:
    """
    Имитирует бросок пяти игральных костей.

    :return: Список из 5 случайных целых чисел в диапазоне от 1 до 6.
    :rtype: List[int]
    """
    # Код генерирует 5 случайных чисел от 1 до 6, представляющих бросок игральных костей.
    return [secrets.SystemRandom().randint(1, 6) for _ in range(5)]

def calculate_score(dice: List[int], category: str) -> int:
    """
    Вычисляет очки для выбранной категории.

    :param dice: Список результатов броска кубиков.
    :type dice: List[int]
    :param category: Выбранная категория для подсчета очков.
    :type category: str
    :return: Количество очков, полученных за выбранную категорию.
    :rtype: int
    """
    # Код создает словарь для подсчета количества каждого значения на кубиках.
    counts = {}
    for die in dice:
        counts[die] = counts.get(die, 0) + 1

    # Код проверяет категорию и вычисляет очки.
    if category in ['1', '2', '3', '4', '5', '6']:
        value = int(category)
        # Код суммирует значения кубиков, соответствующих выбранной категории.
        return sum(die for die in dice if die == value)
    elif category == '3 of a kind':
         # Код проверяет, есть ли 3 одинаковых значения.
        for count in counts.values():
            if count >= 3:
                # Код возвращает сумму всех кубиков, если есть 3 одинаковых значения.
                return sum(dice)
        return 0
    elif category == '4 of a kind':
        # Код проверяет, есть ли 4 одинаковых значения.
        for count in counts.values():
            if count >= 4:
                # Код возвращает сумму всех кубиков, если есть 4 одинаковых значения.
                return sum(dice)
        return 0
    elif category == 'full house':
        # Код проверяет наличие пары и тройки.
        if 2 in counts.values() and 3 in counts.values():
            return 25
        return 0
    elif category == 'small straight':
        # Код проверяет наличие малого стрейта (4 последовательных числа).
        dice.sort()
        unique_dice = sorted(list(set(dice)))
        for i in range(len(unique_dice) - 3):
            if unique_dice[i + 1] == unique_dice[i] + 1 and \
               unique_dice[i + 2] == unique_dice[i] + 2 and \
               unique_dice[i + 3] == unique_dice[i] + 3:
                return 30
        return 0
    elif category == 'large straight':
        # Код проверяет наличие большого стрейта (5 последовательных чисел).
        dice.sort()
        unique_dice = sorted(list(set(dice)))
        if len(unique_dice) == 5:
            for i in range(len(unique_dice) - 1):
                if unique_dice[i + 1] != unique_dice[i] + 1:
                    return 0
            return 40
        return 0
    elif category == 'yahtzee':
        # Код проверяет, все ли значения одинаковые.
        if len(set(dice)) == 1:
            return 50
        return 0
    elif category == 'chance':
        # Код возвращает сумму всех кубиков.
        return sum(dice)
    return 0

def play_yahtzee():
    """
    Запускает игру Yahtzee.

    Организует игровой процесс, включая броски кубиков, выбор категорий и подсчет очков.
    """
    # Код определяет список возможных категорий.
    categories = [
        '1', '2', '3', '4', '5', '6',
        '3 of a kind', '4 of a kind',
        'full house', 'small straight', 'large straight',
        'yahtzee', 'chance'
    ]
    # Код создает словарь для хранения очков по категориям.
    scores = {category: None for category in categories}
    # Код создает множество для хранения использованных категорий.
    used_categories = set()

    # Код запускает основной игровой цикл (13 раундов).
    for round_num in range(1, 14):
        logger.info(f"\n----- Раунд {round_num} -----")
        # Код выполняет бросок кубиков.
        dice = roll_dice()
        logger.info(f"Первый бросок: {dice}")

        # Код выполняет цикл дополнительных бросков (до 2 раз).
        for roll_attempt in range(1, 3):
            # Код запрашивает ввод от пользователя, какие кубики оставить.
            keep_dice_str = input(
                f"Попытка {roll_attempt}, какие кубики оставить (введите номера через пробел, от 1 до 5, 0 = перебросить все, n = ничего не перебрасывать)? "
            )
            # Код проверяет ввод пользователя.
            if keep_dice_str.lower() == 'n':
                break
            if keep_dice_str == '0':
                dice = roll_dice()
                logger.info(f"Новый бросок: {dice}")
                continue
            try:
                # Код преобразует ввод пользователя в список индексов кубиков для сохранения.
                keep_indices = [int(i) - 1 for i in keep_dice_str.split()]
                if not all(0 <= index < 5 for index in keep_indices):
                    logger.error("Неверные индексы, попробуйте еще раз.")
                    continue
                new_dice = []
                for i in range(5):
                    if i not in keep_indices:
                        # Код перебрасывает кубик.
                        new_dice.append(secrets.SystemRandom().randint(1, 6))
                    else:
                        # Код сохраняет кубик.
                        new_dice.append(dice[i])
                dice = new_dice
                logger.info(f"Новый бросок: {dice}")
            except ValueError as e:
                logger.error(f"Неверный ввод, попробуйте еще раз. Ошибка: {e}")

        # Код формирует список доступных категорий.
        available_categories = [
            cat for cat in categories if cat not in used_categories
        ]
        logger.info("Доступные категории:")
        for i, cat in enumerate(available_categories, start=1):
            logger.info(f"{i}. {cat}")
        # Код запрашивает выбор категории.
        while True:
            try:
                choice_index = int(input("Выберите номер категории для записи очков: ")) - 1
                if 0 <= choice_index < len(available_categories):
                    category_choice = available_categories[choice_index]
                    break
                else:
                    logger.error('Неверный номер категории, попробуйте еще раз.')
            except ValueError as e:
                 logger.error(f'Неверный ввод, попробуйте еще раз. Ошибка: {e}')

        # Код вычисляет очки.
        score = calculate_score(dice, category_choice)
        # Код сохраняет очки в словаре.
        scores[category_choice] = score
        # Код добавляет выбранную категорию в список использованных.
        used_categories.add(category_choice)
        logger.info(f"Очки за категорию {category_choice}: {score}")

    # Код выводит итоговую таблицу очков.
    logger.info("\n----- Итоговая таблица очков -----")
    for category, score in scores.items():
        logger.info(f"{category}: {score if score is not None else 0}")
    # Код подсчитывает и выводит общий счет.
    total_score = sum(score if score is not None else 0 for score in scores.values())
    logger.info(f"Общий счет: {total_score}")


if __name__ == "__main__":
    play_yahtzee()
```