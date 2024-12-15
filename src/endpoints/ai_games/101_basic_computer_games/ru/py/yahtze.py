"""
YAHTZE:
=================
Сложность: 7
-----------------
Игра "Яхта" - это игра в кости, в которой игрок бросает пять игральных костей и пытается набрать как можно больше очков, комбинируя результаты бросков. 
Цель игры - заполнить все 13 категорий на листе счета, получая очки за каждую категорию.
Игрок может бросать кости до трех раз за ход, сохраняя любые кости между бросками.

Правила игры:
1.  Игрок бросает 5 игральных костей.
2.  Игрок может сделать до 3 бросков за ход, откладывая кости после каждого броска.
3.  После бросков игрок выбирает одну из 13 категорий на листе счета для записи очков.
4.  Каждая категория может быть использована только один раз.
5.  Игра заканчивается, когда все 13 категорий заполнены.
6.  Победитель определяется по наибольшей сумме очков.
-----------------
Алгоритм:
1.  Инициализировать список для хранения результатов броска костей.
2.  Для каждого раунда (13 раундов):
    2.1. Для каждого броска (до 3 бросков):
        2.1.1. Сбросить все кости, кроме отложенных.
        2.1.2. Выполнить бросок костей.
        2.1.3. Вывести результаты броска.
        2.1.4. Предложить игроку отложить кости, если это не третий бросок.
    2.2. Вывести доступные категории для записи очков.
    2.3. Запросить у игрока выбор категории.
    2.4. Рассчитать очки для выбранной категории.
    2.5. Записать очки в выбранную категорию на листе счета.
    2.6. Если все категории заполнены, закончить игру.
3.  Вывести итоговый счет и определить победителя.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> Initialize["Инициализация: <code><b>scorecard, dice, rolls</b></code>"]
    Initialize --> RoundStart{"Начало цикла: 13 раундов"}
    RoundStart -- Да --> RollStart{"Начало цикла: до 3 бросков"}
    RollStart --> RollDice["<code><b>roll_dice()</b></code>"]
    RollDice --> DisplayDice["Вывод результатов броска"]
    DisplayDice --> ThirdRoll{"Это 3-й бросок?"}
    ThirdRoll -- Нет --> HoldDice{"Предложить отложить кости"}
    HoldDice --> RollStart
    ThirdRoll -- Да --> DisplayCategories["Вывод доступных категорий"]
    DisplayCategories --> ChooseCategory["Выбор категории"]
    ChooseCategory --> CalculateScore["<code><b>calculate_score()</b></code>"]
    CalculateScore --> UpdateScorecard["Запись очков"]
     UpdateScorecard--> RoundEnd{"Все категории заполнены?"}
     RoundEnd -- Нет --> RoundStart
    RoundEnd -- Да --> CalculateTotalScore["<code><b>calculate_total_score()</b></code>"]
    CalculateTotalScore --> DisplayFinalScore["Вывод итогового счета"]
    DisplayFinalScore --> End["Конец"]
    RollStart -- Нет --> DisplayCategories

```

Legenda:
    Start - Начало программы.
    Initialize - Инициализация переменных: scorecard (лист счета), dice (кости), rolls (количество бросков).
    RoundStart - Начало цикла, который повторяется 13 раз (количество раундов в игре).
    RollStart - Начало цикла, который повторяется до 3 раз (количество бросков в раунде).
    RollDice - Бросок костей.
    DisplayDice - Вывод результатов броска костей.
    ThirdRoll - Проверка, был ли это третий бросок.
    HoldDice - Предложение игроку отложить кости.
    DisplayCategories - Вывод доступных категорий для записи очков.
    ChooseCategory - Выбор категории игроком.
    CalculateScore - Расчет очков для выбранной категории.
    UpdateScorecard - Запись очков в выбранную категорию.
    RoundEnd - Проверка, заполнены ли все категории на листе счета.
    CalculateTotalScore - Расчет итогового счета.
    DisplayFinalScore - Вывод итогового счета.
    End - Конец программы.
"""
import random

# Функция для броска костей
def roll_dice(dice_to_roll):
    """
    Имитирует бросок костей.

    Args:
    dice_to_roll (list): Список индексов костей, которые нужно бросить.

    Returns:
        list: Список результатов броска костей.
    """
    return [random.randint(1, 6) for _ in dice_to_roll]

# Функция для вывода результатов броска
def display_dice(dice):
    """
    Выводит результаты броска костей.

    Args:
        dice (list): Список результатов броска.
    """
    print("Результат броска:", dice)

# Функция для выбора костей, которые нужно оставить
def hold_dice(dice):
    """
    Предлагает игроку выбрать кости, которые нужно оставить, и возвращает индексы костей.

    Args:
        dice (list): Список результатов броска.

    Returns:
        list: Список индексов костей для откладывания.
    """
    while True:
        hold = input("Введите индексы костей, которые хотите оставить (через пробел, например, '1 3', или нажмите Enter, чтобы бросить все кости): ")
        if hold == "":
            return []
        try:
            hold_indices = [int(index) - 1 for index in hold.split()]
            if all(0 <= index < len(dice) for index in hold_indices):
                return hold_indices
            else:
                print("Неверные индексы. Попробуйте снова.")
        except ValueError:
            print("Неверный ввод. Введите индексы через пробел или нажмите Enter.")

# Функция для расчета очков за категорию
def calculate_score(dice, category):
  """
    Рассчитывает очки за выбранную категорию.

    Args:
        dice (list): Результаты броска костей.
        category (str): Выбранная категория.

    Returns:
        int: Количество очков за категорию.
  """
  counts = {}
  for d in dice:
    counts[d] = counts.get(d, 0) + 1
  
  if category == "1": # еденицы
      return sum(d for d in dice if d == 1)
  elif category == "2":  # двойки
      return sum(d for d in dice if d == 2)
  elif category == "3":  # тройки
      return sum(d for d in dice if d == 3)
  elif category == "4": # четверки
      return sum(d for d in dice if d == 4)
  elif category == "5": # пятерки
      return sum(d for d in dice if d == 5)
  elif category == "6": # шестерки
      return sum(d for d in dice if d == 6)
  elif category == "три_одинаковых": # три одинаковых
      for count in counts.values():
          if count >= 3:
              return sum(dice)
      return 0
  elif category == "четыре_одинаковых": # четыре одинаковых
      for count in counts.values():
          if count >= 4:
              return sum(dice)
      return 0
  elif category == "фулл_хаус": # фулл хаус
    if len(counts) == 2 and (3 in counts.values()) and (2 in counts.values()):
        return 25
    return 0
  elif category == "малый_стрит": # малый стрит (4 последовательные)
      dice.sort()
      unique_dice = sorted(list(set(dice)))
      for i in range(len(unique_dice) - 3):
        if unique_dice[i+1] == unique_dice[i] + 1 and \
           unique_dice[i+2] == unique_dice[i] + 2 and \
           unique_dice[i+3] == unique_dice[i] + 3:
              return 30
      return 0
  elif category == "большой_стрит": # большой стрит (5 последовательных)
      dice.sort()
      unique_dice = sorted(list(set(dice)))
      if len(unique_dice) == 5:
        if unique_dice[4] - unique_dice[0] == 4:
              return 40
      return 0
  elif category == "яцзы": # яцзы (все одинаковые)
      if len(counts) == 1:
          return 50
      return 0
  elif category == "шанс": # шанс
      return sum(dice)
  else:
      return 0

# Функция для отображения категорий
def display_categories(scorecard):
    """
    Выводит список доступных категорий и предлагает пользователю выбрать одну.

    Args:
        scorecard (dict): Словарь с категориями и очками.
    """
    categories = {
    "1": "Единицы",
    "2": "Двойки",
    "3": "Тройки",
    "4": "Четверки",
    "5": "Пятерки",
    "6": "Шестерки",
    "три_одинаковых": "Три одинаковых",
    "четыре_одинаковых": "Четыре одинаковых",
    "фулл_хаус": "Фулл хаус",
    "малый_стрит": "Малый стрит",
    "большой_стрит": "Большой стрит",
    "яцзы": "Яцзы",
    "шанс": "Шанс",
    }
    print("Доступные категории:")
    for key, value in categories.items():
      if key not in scorecard:
          print(f"{key}: {value}")

# Функция для выбора категории
def choose_category(scorecard):
    """
    Позволяет игроку выбрать категорию для записи очков.

    Args:
        scorecard (dict): Словарь с категориями и очками.

    Returns:
        str: Выбранная категория.
    """
    while True:
      display_categories(scorecard)
      category = input("Выберите категорию для записи очков: ")
      if category in [
        "1", "2", "3", "4", "5", "6",
         "три_одинаковых", "четыре_одинаковых",
         "фулл_хаус", "малый_стрит", "большой_стрит",
         "яцзы", "шанс"
         ] and category not in scorecard:
          return category
      else:
          print("Неверная категория, либо категория уже занята. Попробуйте снова.")


# Функция для обновления листа счета
def update_scorecard(scorecard, category, score):
    """
    Обновляет лист счета выбранными очками.

    Args:
        scorecard (dict): Словарь с категориями и очками.
        category (str): Выбранная категория.
        score (int): Количество очков за категорию.
    """
    scorecard[category] = score

# Функция для подсчета итогового счета
def calculate_total_score(scorecard):
    """
    Рассчитывает итоговый счет игрока.

    Args:
        scorecard (dict): Словарь с категориями и очками.

    Returns:
        int: Итоговый счет.
    """
    return sum(scorecard.values())

# Функция для отображения итогового счета
def display_final_score(scorecard):
  """
    Выводит итоговый счет игрока.

    Args:
        scorecard (dict): Словарь с категориями и очками.
  """
  print("Итоговый счет:")
  for key, value in scorecard.items():
    categories = {
    "1": "Единицы",
    "2": "Двойки",
    "3": "Тройки",
    "4": "Четверки",
    "5": "Пятерки",
    "6": "Шестерки",
    "три_одинаковых": "Три одинаковых",
    "четыре_одинаковых": "Четыре одинаковых",
    "фулл_хаус": "Фулл хаус",
    "малый_стрит": "Малый стрит",
    "большой_стрит": "Большой стрит",
    "яцзы": "Яцзы",
    "шанс": "Шанс",
    }
    print(f"{categories[key]}: {value}")
  print("Общий счет:", calculate_total_score(scorecard))

# Основная функция игры
def play_yahtzee():
    """
    Запускает игру в Yahtzee.
    """
    scorecard = {}  # Инициализация листа счета
    
    for round_num in range(1, 14): # 13 раундов
      print(f"\n----- Раунд {round_num} -----")
      dice = []
      dice_to_roll = [0, 1, 2, 3, 4] # Индексы костей для броска
      for roll_num in range(1,4): # До 3х бросков
        print(f"\nБросок {roll_num}:")
        new_roll = roll_dice(dice_to_roll) # Бросаем кости
        for i, value in enumerate(new_roll):
            if len(dice) > dice_to_roll[i]:
                dice[dice_to_roll[i]] = value
            else:
                 dice.append(value) # Записываем результаты броска
        display_dice(dice) # Выводим результаты броска

        if roll_num < 3: # предлагаем сохранить кости, если не последний бросок
          hold_indices = hold_dice(dice)
          dice_to_roll = [i for i in range(5) if i not in hold_indices] # обновляем список костей для следующего броска
        else:
          dice_to_roll = []
          
      # Выбор категории и запись очков
      category = choose_category(scorecard) # Выбор категории
      score = calculate_score(dice, category) # Расчет очков
      update_scorecard(scorecard, category, score) # Обновляем счет
      
      # Проверка на завершение игры
      if len(scorecard) == 13:
          break
      
    # Подсчет и вывод итогового счета
    display_final_score(scorecard)

if __name__ == "__main__":
    play_yahtzee()
"""
Объяснение кода:
1.  **Импорт модуля `random`**:
    -   `import random`: Импортирует модуль `random`, необходимый для генерации случайных чисел (бросков костей).
2.  **Функция `roll_dice(dice_to_roll)`**:
    -   Принимает список индексов `dice_to_roll` костей, которые нужно бросить.
    -   Возвращает новый список случайных результатов броска костей от 1 до 6.
3.  **Функция `display_dice(dice)`**:
    -   Принимает список `dice` с результатами броска.
    -   Выводит на экран результаты броска костей.
4.  **Функция `hold_dice(dice)`**:
    -   Принимает список `dice` с результатами броска.
    -   Запрашивает у пользователя индексы костей, которые нужно оставить.
    -   Проверяет корректность ввода.
    -   Возвращает список индексов костей, которые нужно сохранить.
5.  **Функция `calculate_score(dice, category)`**:
    -   Принимает список `dice` с результатами броска и выбранную `category`.
    -   Вычисляет очки в зависимости от выбранной категории:
        -   Считает сумму единиц, двоек и так далее.
        -   Считает очки за комбинации: три и четыре одинаковых, фулл хаус, малый и большой стриты, яцзы и шанс.
    -   Возвращает набранные очки.
6.  **Функция `display_categories(scorecard)`**:
    -   Принимает лист счета `scorecard`.
    -   Выводит список доступных категорий, которые еще не были использованы.
7.  **Функция `choose_category(scorecard)`**:
    -   Принимает лист счета `scorecard`.
    -   Позволяет игроку выбрать категорию для записи очков.
    -   Проверяет корректность ввода.
    -   Возвращает выбранную категорию.
8.  **Функция `update_scorecard(scorecard, category, score)`**:
    -   Принимает лист счета `scorecard`, выбранную `category` и полученные `score`.
    -   Обновляет лист счета, добавляя очки в выбранную категорию.
9. **Функция `calculate_total_score(scorecard)`**:
    -   Принимает лист счета `scorecard`.
    -   Рассчитывает и возвращает общий счет, суммируя все очки на листе.
10. **Функция `display_final_score(scorecard)`**:
    -   Принимает лист счета `scorecard`.
    -   Выводит на экран итоговый счет с разбивкой по категориям.
11. **Функция `play_yahtzee()`**:
     -   Основная функция, реализующая игровой процесс.
     -   Инициализирует лист счета `scorecard`.
     -   Запускает 13 раундов.
     -   В каждом раунде выполняется до 3 бросков костей, предлагая игроку оставить кости между бросками.
     -   Вызывает функции для отображения костей, выбора категории и подсчета очков.
     -   Выводит итоговый счет после завершения всех раундов.
12. **Условие `if __name__ == "__main__":`**:
    -   Гарантирует, что функция `play_yahtzee()` будет запущена, только если файл исполняется напрямую, а не импортируется как модуль.
"""
