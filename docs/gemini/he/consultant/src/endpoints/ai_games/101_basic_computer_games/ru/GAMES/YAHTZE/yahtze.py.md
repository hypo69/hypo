# Анализ кода модуля yahtze.py

**Качество кода**

-   **Соответствие требованиям к формату кода (1-10)**
    -   **Преимущества**:
        -   Код в целом хорошо структурирован и понятен, основные функции разбиты на логические блоки.
        -   Используется docstring для описания модуля и функций.
        -   Логика игры реализована в соответствии с правилами.
        -   Есть блок-схема в формате mermaid для визуализации алгоритма игры.
        -   Есть подробное текстовое описание алгоритма и процесса игры.
    -   **Недостатки**:
        -   Не используется reStructuredText (RST) для docstrings и комментариев.
        -   Используется `json.load` вместо `j_loads` или `j_loads_ns`.
        -   Отсутствует обработка ошибок через `logger.error`.
        -   Используется `input` для ввода данных, что может привести к ошибкам.
        -   Нет импорта необходимых библиотек из `src.utils.jjson` и `src.logger.logger`.
        -   Комментарии `#` не соответствуют формату RST и не дают подробного объяснения кода.
        -   Некоторые переменные и функции не имеют описания.
        -   Код перегружен проверками и логикой, которые можно упростить.

**Рекомендации по улучшению**

1.  **Перевести docstring и комментарии в формат reStructuredText (RST)**.
2.  **Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо `json.load`**.
3.  **Добавить обработку ошибок с использованием `logger.error`**.
4.  **Импортировать необходимые модули и настроить логгирование**.
5.  **Добавить детальные комментарии, объясняющие логику кода**.
6.  **Улучшить читаемость кода, используя более описательные имена переменных и функций**.
7.  **Рефакторинг функции `calculate_score` для большей читаемости и уменьшения дублирования кода**.
8.  **Улучшить обработку ввода пользователя, добавив проверку на нечисловые значения**.
9.  **Добавить примеры использования и возможные улучшения в виде TODO**.

**Улучшенный код**

```python
"""
Модуль для реализации игры Yahtzee
=========================================================================================

Модуль содержит функции для реализации игры в кости Yahtzee, включая бросок кубиков,
расчет очков и управление игровым процессом.

Пример использования
--------------------

Пример запуска игры:

.. code-block:: python

    if __name__ == "__main__":
        play_yahtzee()
"""
import random
from src.logger.logger import logger # Импортируем логгер #
from typing import List # Импортируем List из typing #


def roll_dice() -> List[int]:
    """
    Выполняет бросок 5 кубиков.

    :return: Список из 5 случайных чисел от 1 до 6, представляющих результаты броска.
    :rtype: List[int]
    """
    return [random.randint(1, 6) for _ in range(5)] # Бросаем 5 кубиков и возвращаем результаты


def calculate_score(dice: List[int], category: str) -> int:
    """
    Вычисляет очки для выбранной категории.

    :param dice: Список результатов броска кубиков.
    :type dice: List[int]
    :param category: Выбранная категория для расчета очков.
    :type category: str
    :return: Количество очков, набранных в данной категории.
    :rtype: int

    :raises ValueError: Если передана неверная категория.

    .. TODO::
       -  Упростить логику подсчета очков, возможно, с использованием словаря или enum для категорий.
       -  Добавить обработку неверных значений category.
    """
    counts = {}
    for die in dice: # Подсчитываем количество каждого значения на кубиках
        counts[die] = counts.get(die, 0) + 1

    if category in ['1', '2', '3', '4', '5', '6']: # Если категория - число, суммируем выпавшие кубики этого числа
        value = int(category) # преобразуем категорию к int для проверки
        return sum(die for die in dice if die == value)
    elif category == '3 of a kind': # Проверяем есть ли 3 одинаковых значения
        for count in counts.values():
            if count >= 3:
                return sum(dice) # Возвращаем сумму всех костей, если есть
        return 0
    elif category == '4 of a kind': # Проверяем есть ли 4 одинаковых значения
        for count in counts.values():
            if count >= 4:
                return sum(dice) # Возвращаем сумму всех костей, если есть
        return 0
    elif category == 'full house': # Проверяем есть ли фулл-хаус
        if 2 in counts.values() and 3 in counts.values():
            return 25 # Возвращаем 25 очков за фулл-хаус
        return 0
    elif category == 'small straight': # Проверяем есть ли малый стрейт
        dice.sort() # Сортируем кости
        unique_dice = sorted(list(set(dice))) # убираем дубликаты
        for i in range(len(unique_dice) - 3): # проверяем есть ли последовательность из 4 значений
            if unique_dice[i+1] == unique_dice[i] + 1 and \
               unique_dice[i+2] == unique_dice[i] + 2 and \
               unique_dice[i+3] == unique_dice[i] + 3:
                return 30 # Возвращаем 30 очков за малый стрейт
        return 0
    elif category == 'large straight': # Проверяем есть ли большой стрейт
          dice.sort() # Сортируем кости
          unique_dice = sorted(list(set(dice))) # убираем дубликаты
          if len(unique_dice) == 5: # Проверяем, что все кости уникальны
              for i in range(len(unique_dice)-1): # Проверяем последовательность из 5 значений
                if unique_dice[i+1] != unique_dice[i]+1:
                  return 0 # Возвращаем 0, если последовательности нет
              return 40 # Возвращаем 40 очков за большой стрейт
          return 0
    elif category == 'yahtzee': # Проверяем есть ли 5 одинаковых значений
        if len(set(dice)) == 1:
            return 50 # Возвращаем 50 очков за yahtzee
        return 0
    elif category == 'chance': # Возвращаем сумму всех костей
        return sum(dice)
    else:
        logger.error(f"Неизвестная категория: {category}") # Запись ошибки в лог
        return 0 # Возвращаем 0 в случае некорректной категории


def play_yahtzee():
    """
    Основная функция для игры в Yahtzee.

    Осуществляет игровой процесс, включая броски кубиков, выбор категорий,
    расчет очков и вывод результатов.

    .. TODO::
        -   Реализовать сохранение и загрузку состояния игры.
        -   Добавить возможность играть нескольким игрокам.
    """
    categories = [ # Список всех возможных категорий
      '1', '2', '3', '4', '5', '6',
      '3 of a kind', '4 of a kind',
      'full house', 'small straight', 'large straight',
      'yahtzee', 'chance'
    ]
    scores = {category: None for category in categories}  # Словарь для хранения очков #
    used_categories = set()  # Множество использованных категорий #

    for round_num in range(1, 14): # Основной цикл, который происходит 13 раз
        print(f"\n----- Раунд {round_num} -----")
        dice = roll_dice()  # Бросаем кубики #
        print(f"Первый бросок: {dice}")

        for roll_attempt in range(1, 3): # Даем 3 попытки #
            keep_dice_str = input(f"Попытка {roll_attempt}, какие кубики оставить (введите номера через пробел, от 1 до 5, 0 = перебросить все, n = ничего не перебрасывать)? ")

            if keep_dice_str.lower() == 'n': # Если игрок ввел 'n' пропускаем цикл #
              break
            if keep_dice_str == '0': # Если игрок ввел '0' перебрасываем все кости #
              dice = roll_dice()
              print(f"Новый бросок: {dice}")
              continue
            try:
                keep_indices = [int(i) - 1 for i in keep_dice_str.split()] # Получаем список индексов кубиков, которые нужно оставить #
                if not all(0 <= index < 5 for index in keep_indices): # Проверяем, все ли индексы в пределах допустимых значений #
                  print("Неверные индексы, попробуйте еще раз.")
                  continue
                new_dice = [] # Новый список кубиков #
                for i in range(5): # Проходим по всем кубикам #
                  if i not in keep_indices: # Если кубик не нужно оставлять, то бросаем его заново #
                    new_dice.append(random.randint(1, 6))
                  else: # Иначе, добавляем кубик в новый список из старого #
                    new_dice.append(dice[i])
                dice = new_dice # Обновляем список кубиков #
                print(f"Новый бросок: {dice}")
            except ValueError:
                logger.error(f"Некорректный ввод: {keep_dice_str}") # Запись ошибки в лог
                print("Неверный ввод, попробуйте еще раз.") # Выводим сообщение об ошибке

        available_categories = [cat for cat in categories if cat not in used_categories] # Список доступных категорий #
        print("Доступные категории:")
        for i, cat in enumerate(available_categories, start=1): # Выводим список категорий #
            print(f"{i}. {cat}")

        while True: # Бесконечный цикл для выбора категории #
            try:
                choice_index = int(input("Выберите номер категории для записи очков: "))-1 # Запрашиваем выбор #
                if  0 <= choice_index < len(available_categories) : # Проверяем, находится ли выбор в границах допустимых значений #
                    category_choice = available_categories[choice_index] # Сохраняем выбор пользователя #
                    break
                else:
                    print('Неверный номер категории, попробуйте еще раз.')
            except ValueError:
                logger.error("Некорректный ввод номера категории") # Запись ошибки в лог
                print('Неверный ввод, попробуйте еще раз.') # Выводим сообщение об ошибке

        score = calculate_score(dice, category_choice)  # Вычисляем очки #
        scores[category_choice] = score # Сохраняем очки в словаре #
        used_categories.add(category_choice) # Добавляем категорию в использованные #
        print(f"Очки за категорию {category_choice}: {score}")

    # Выводим таблицу очков #
    print("\n----- Итоговая таблица очков -----")
    for category, score in scores.items(): # Выводим результаты по категориям #
      print(f"{category}: {score if score is not None else 0}")

    total_score = sum(score if score is not None else 0 for score in scores.values()) # Подсчитываем общий счет #
    print(f"Общий счет: {total_score}")


if __name__ == "__main__":
    play_yahtzee()
```