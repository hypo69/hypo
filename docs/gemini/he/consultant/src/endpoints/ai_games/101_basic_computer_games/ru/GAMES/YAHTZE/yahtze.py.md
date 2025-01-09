# Анализ кода модуля yahtze.py

**Качество кода**
-   **Соответствие требованиям к формату кода (1-10):**
    -   **Преимущества:**
        -   Код хорошо структурирован и разбит на логические функции, что повышает читаемость.
        -   Логика игры реализована в соответствии с правилами Yahtzee.
        -   Используются понятные имена переменных и функций.
        -   Код содержит подробные комментарии, объясняющие различные части программы.
        -   Реализована обработка ввода пользователя с проверкой на корректность.
    -   **Недостатки:**
        -   Отсутствует docstring для модуля.
        -   Не используется `j_loads` или `j_loads_ns` для загрузки JSON.
        -   Не используется `logger` для обработки ошибок.
        -   Некоторые комментарии после `#` не соответствуют стандарту reStructuredText (RST).
        -   В коде встречаются излишние комментарии.
        -   Отсутствуют комментарии в формате RST для функций и классов.
        -   Некоторые блоки `try-except` могут быть заменены на использование `logger.error`.
        -   Ввод пользователя не обрабатывается для чисел с плавающей запятой, может вызвать ошибку.
        -   В функции `calculate_score` можно добавить более лаконичную запись подсчета очков.
        -   В блоке else в цикле бросков `new_dice.append(dice[i])` можно оптимизировать запись.

**Рекомендации по улучшению**

1.  **Добавить docstring для модуля в формате RST.**
2.  **Импортировать и использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` (если требуется).**
3.  **Импортировать и использовать `logger` из `src.logger.logger` для обработки ошибок вместо `try-except`.**
4.  **Переписать все комментарии в формат RST и добавить docstring для всех функций, классов и переменных.**
5.  **Убрать излишние комментарии и оставить только те, что описывают логику кода.**
6.  **Улучшить обработку ввода пользователя, чтобы избежать ошибок при вводе некорректных данных.**
7.  **Оптимизировать код для более компактной записи и улучшенной читаемости.**
8.  **Провести рефакторинг функции `calculate_score` для более лаконичной записи.**

**Улучшенный код**

```python
"""
Модуль для игры в Yahtzee.
=========================================================================================

Модуль реализует игру в кости Yahtzee.
Игрок бросает пять кубиков и пытается набрать очки, составляя комбинации.
В конце игры очки суммируются.

Пример использования:
---------------------

.. code-block:: python

    if __name__ == "__main__":
        play_yahtzee()
"""
import random
from src.logger.logger import logger  # Импорт модуля для логирования

def roll_dice() -> list:
    """
    Бросает 5 кубиков и возвращает результаты.

    :return: Список из 5 случайных чисел в диапазоне от 1 до 6.
    :rtype: list
    """
    # Функция возвращает список случайных чисел от 1 до 6
    return [random.randint(1, 6) for _ in range(5)]

def calculate_score(dice: list, category: str) -> int:
    """
    Вычисляет очки для выбранной категории.

    :param dice: Список результатов броска кубиков.
    :type dice: list
    :param category: Выбранная категория для подсчета очков.
    :type category: str
    :return: Количество очков для выбранной категории.
    :rtype: int
    """
    # Подсчет количества каждого значения на кубиках
    counts = {}
    for die in dice:
        counts[die] = counts.get(die, 0) + 1

    # Вычисление очков для категорий 1-6
    if category in ['1', '2', '3', '4', '5', '6']:
        value = int(category)
        return sum(die for die in dice if die == value)
    # Вычисление очков для "3 of a kind"
    elif category == '3 of a kind':
        return sum(dice) if any(count >= 3 for count in counts.values()) else 0
    # Вычисление очков для "4 of a kind"
    elif category == '4 of a kind':
        return sum(dice) if any(count >= 4 for count in counts.values()) else 0
    # Вычисление очков для "full house"
    elif category == 'full house':
        return 25 if 2 in counts.values() and 3 in counts.values() else 0
    # Вычисление очков для "small straight"
    elif category == 'small straight':
        unique_dice = sorted(set(dice))
        for i in range(len(unique_dice) - 3):
            if all(unique_dice[i+j] == unique_dice[i] + j for j in range(4)):
                return 30
        return 0
    # Вычисление очков для "large straight"
    elif category == 'large straight':
        unique_dice = sorted(set(dice))
        if len(unique_dice) == 5 and all(unique_dice[i+1] == unique_dice[i] + 1 for i in range(4)):
            return 40
        return 0
    # Вычисление очков для "yahtzee"
    elif category == 'yahtzee':
        return 50 if len(set(dice)) == 1 else 0
    # Вычисление очков для "chance"
    elif category == 'chance':
        return sum(dice)
    return 0

def play_yahtzee():
    """
    Основная функция для игры в Yahtzee.

    Инициализирует игру, обрабатывает ввод пользователя, подсчитывает очки и выводит результаты.
    """
    # Определение категорий
    categories = [
      '1', '2', '3', '4', '5', '6',
      '3 of a kind', '4 of a kind',
      'full house', 'small straight', 'large straight',
      'yahtzee', 'chance'
    ]
    # Инициализация словаря для хранения очков
    scores = {category: None for category in categories}
    # Инициализация множества для хранения использованных категорий
    used_categories = set()

    # Основной игровой цикл
    for round_num in range(1, 14):
        print(f"\n----- Раунд {round_num} -----")
        dice = roll_dice() # Бросаем кубики
        print(f"Первый бросок: {dice}")

        # Цикл для дополнительных бросков (до двух раз)
        for roll_attempt in range(1, 3):
            keep_dice_str = input(f"Попытка {roll_attempt}, какие кубики оставить (введите номера через пробел, от 1 до 5, 0 = перебросить все, n = ничего не перебрасывать)? ")

            if keep_dice_str.lower() == 'n':
                break # Завершаем цикл бросков, если игрок вводит 'n'
            if keep_dice_str == '0':
                dice = roll_dice()
                print(f"Новый бросок: {dice}")
                continue # Перебрасываем все кубики, если игрок вводит '0'
            try:
                # Получаем список индексов кубиков, которые нужно оставить
                keep_indices = [int(i) - 1 for i in keep_dice_str.split()]
                # Проверяем, что индексы находятся в допустимом диапазоне
                if not all(0 <= index < 5 for index in keep_indices):
                    print("Неверные индексы, попробуйте еще раз.")
                    continue
                # Создаем новый список кубиков
                new_dice = [random.randint(1, 6) if i not in keep_indices else dice[i] for i in range(5)]
                dice = new_dice # Обновляем массив кубиков
                print(f"Новый бросок: {dice}")
            except ValueError:
                logger.error("Неверный ввод, попробуйте еще раз.") # Логируем ошибку ввода
                print("Неверный ввод, попробуйте еще раз.")

        # Формирование списка доступных категорий
        available_categories = [cat for cat in categories if cat not in used_categories]
        print("Доступные категории:")
        for i, cat in enumerate(available_categories, start=1):
            print(f"{i}. {cat}")

        # Цикл для выбора категории игроком
        while True:
            try:
                choice_index = int(input("Выберите номер категории для записи очков: ")) - 1 # Запрашиваем выбор
                if 0 <= choice_index < len(available_categories):
                    category_choice = available_categories[choice_index]
                    break # Завершаем цикл, если ввод корректен
                else:
                    print('Неверный номер категории, попробуйте еще раз.')
            except ValueError:
                 logger.error('Неверный ввод, попробуйте еще раз.') # Логируем ошибку ввода
                 print('Неверный ввод, попробуйте еще раз.')

        # Вычисляем и записываем очки
        score = calculate_score(dice, category_choice)
        scores[category_choice] = score
        used_categories.add(category_choice) # Добавляем категорию в список использованных
        print(f"Очки за категорию {category_choice}: {score}")

    # Выводим таблицу очков
    print("\n----- Итоговая таблица очков -----")
    for category, score in scores.items():
      print(f"{category}: {score if score is not None else 0}")

    # Подсчет общего количества очков
    total_score = sum(score if score is not None else 0 for score in scores.values())
    print(f"Общий счет: {total_score}")

if __name__ == "__main__":
    play_yahtzee()
```