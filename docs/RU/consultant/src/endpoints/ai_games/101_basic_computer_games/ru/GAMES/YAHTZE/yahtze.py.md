# Анализ кода модуля yahtze.py

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и разбит на функции, что облегчает чтение и понимание.
    -  Функции имеют docstring, описывающие их назначение.
    -  Используется множество для хранения использованных категорий, что обеспечивает быстроту проверки.
    -  Код игры логически понятен и следует правилам игры Yahtzee.
    -  Обработка ввода пользователя осуществляется с проверкой на корректность.
-  Минусы
    -  Отсутствуют импорты из `src.utils.jjson` и `src.logger.logger`.
    -  Не все комментарии соответствуют стандарту reStructuredText.
    -  В коде используются стандартные `try-except` блоки, которые можно заменить на `logger.error`.
    -  В цикле переброса кубиков логика не совсем оптимальна.
    -  Не используется `j_loads` или `j_loads_ns` для работы с json (хотя json не используется)
    -  В комментариях присутствуют слова "получаем", "делаем".

**Рекомендации по улучшению**

1.  Добавить импорт `j_loads_ns` из `src.utils.jjson` и `logger` из `src.logger.logger`.
2.  Переписать все docstring в формате reStructuredText.
3.  Заменить `try-except` на использование `logger.error` для обработки исключений.
4.  Упростить логику переброса кубиков, убрав избыточное использование `if-else`.
5.  Переписать все комментарии в стиле reStructuredText.
6.  Избегать слов "получаем", "делаем" и т.д.
7.  Удалить неиспользуемые импорты `j_loads`

**Оптимизированный код**

```python
"""
Модуль для реализации игры Yahtzee.
=========================================================================================

Этот модуль содержит функции для игры в Yahtzee, включая бросание кубиков, подсчет очков и управление игровым процессом.

Пример использования
--------------------

.. code-block:: python

    play_yahtzee()
"""
import random
# Импортируем logger для логирования ошибок
from src.logger.logger import logger
# Импортируем j_loads_ns
from src.utils.jjson import j_loads_ns

def roll_dice() -> list[int]:
    """
    Бросает 5 кубиков и возвращает результаты.

    :return: Список из 5 случайных чисел от 1 до 6.
    :rtype: list[int]
    """
    # Код исполняет генерацию списка из 5 случайных чисел от 1 до 6
    return [random.randint(1, 6) for _ in range(5)]

def calculate_score(dice: list[int], category: str) -> int:
    """
    Вычисляет очки для выбранной категории.

    :param dice: Список результатов броска кубиков.
    :type dice: list[int]
    :param category: Выбранная категория для подсчета очков.
    :type category: str
    :return: Количество очков для выбранной категории.
    :rtype: int
    """
    # Код исполняет подсчет количества каждого значения на кубиках
    counts = {}
    for die in dice:
        counts[die] = counts.get(die, 0) + 1

    # Код проверяет категорию и подсчитывает очки
    if category in ['1', '2', '3', '4', '5', '6']:
        value = int(category)
        return sum(die for die in dice if die == value)
    elif category == '3 of a kind':
        for count in counts.values():
            if count >= 3:
                return sum(dice)
        return 0
    elif category == '4 of a kind':
        for count in counts.values():
            if count >= 4:
                return sum(dice)
        return 0
    elif category == 'full house':
        if 2 in counts.values() and 3 in counts.values():
            return 25
        return 0
    elif category == 'small straight':
        dice.sort()
        unique_dice = sorted(list(set(dice)))
        for i in range(len(unique_dice) - 3):
            if unique_dice[i+1] == unique_dice[i] + 1 and \
               unique_dice[i+2] == unique_dice[i] + 2 and \
               unique_dice[i+3] == unique_dice[i] + 3:
                return 30
        return 0
    elif category == 'large straight':
          dice.sort()
          unique_dice = sorted(list(set(dice)))
          if len(unique_dice) == 5:
              for i in range(len(unique_dice)-1):
                if unique_dice[i+1] != unique_dice[i]+1:
                  return 0
              return 40
          return 0
    elif category == 'yahtzee':
        if len(set(dice)) == 1:
            return 50
        return 0
    elif category == 'chance':
        return sum(dice)
    return 0

def play_yahtzee():
    """
    Основная функция для игры в Yahtzee.

    Управляет игровым процессом, включая броски кубиков, выбор категорий и подсчет очков.
    """
    # Код инициализирует категории и словарь очков
    categories = [
      '1', '2', '3', '4', '5', '6',
      '3 of a kind', '4 of a kind',
      'full house', 'small straight', 'large straight',
      'yahtzee', 'chance'
    ]
    scores = {category: None for category in categories}  # Словарь для хранения очков
    used_categories = set()  # Множество использованных категорий

    # Код запускает цикл раундов игры
    for round_num in range(1, 14):
        print(f"\n----- Раунд {round_num} -----")
        # Код исполняет бросок кубиков
        dice = roll_dice()
        print(f"Первый бросок: {dice}")

        # Код запускает цикл для дополнительных бросков
        for roll_attempt in range(1, 3):
            keep_dice_str = input(f"Попытка {roll_attempt}, какие кубики оставить (введите номера через пробел, от 1 до 5, 0 = перебросить все, n = ничего не перебрасывать)? ")
            
            # Проверка ввода пользователя
            if keep_dice_str.lower() == 'n':
              break
            if keep_dice_str == '0':
              dice = roll_dice()
              print(f"Новый бросок: {dice}")
              continue
            try:
                # Код получает индексы кубиков, которые нужно оставить
                keep_indices = [int(i) - 1 for i in keep_dice_str.split()]
                if not all(0 <= index < 5 for index in keep_indices):
                  print("Неверные индексы, попробуйте еще раз.")
                  continue
                # Код формирует новый бросок
                new_dice = [random.randint(1, 6) if i not in keep_indices else dice[i] for i in range(5)]
                dice = new_dice
                print(f"Новый бросок: {dice}")
            except ValueError:
                logger.error("Неверный ввод, попробуйте еще раз.")
                continue

        # Код формирует список доступных категорий
        available_categories = [cat for cat in categories if cat not in used_categories]
        print("Доступные категории:")
        for i, cat in enumerate(available_categories, start=1):
            print(f"{i}. {cat}")

        # Код запрашивает выбор категории
        while True:
            try:
                choice_index = int(input("Выберите номер категории для записи очков: "))-1
                if  0 <= choice_index < len(available_categories) :
                    category_choice = available_categories[choice_index]
                    break
                else:
                    print('Неверный номер категории, попробуйте еще раз.')
            except ValueError:
                logger.error('Неверный ввод, попробуйте еще раз.')
        
        # Код исполняет подсчет очков и сохранение результата
        score = calculate_score(dice, category_choice)
        scores[category_choice] = score
        used_categories.add(category_choice)
        print(f"Очки за категорию {category_choice}: {score}")

    # Код выводит итоговую таблицу очков
    print("\n----- Итоговая таблица очков -----")
    for category, score in scores.items():
      print(f"{category}: {score if score is not None else 0}")

    # Код исполняет подсчет итогового счета
    total_score = sum(score if score is not None else 0 for score in scores.values())
    print(f"Общий счет: {total_score}")

if __name__ == "__main__":
    play_yahtzee()
```