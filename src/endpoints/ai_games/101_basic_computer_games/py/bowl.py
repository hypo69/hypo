"""
<BOWL>:
=================
Сложность: 3
-----------------
Игра в боулинг. Игрок вводит количество сбитых кеглей за каждый бросок в 10 раундах. Программа выводит счет после каждого раунда. 
Игра использует стандартную систему подсчета очков в боулинге, включая страйки и спэры.

Правила игры:
-----------------
1. Игра состоит из 10 раундов.
2. В каждом раунде игрок делает один или два броска.
3. Если игрок сбивает все 10 кеглей первым броском (страйк), то он не делает второй бросок, а следующий раунд. Очки за страйк считаются как 10 + сумма очков за следующие два броска (из следующего раунда).
4. Если игрок сбивает все 10 кеглей за два броска (спэр), то очки за этот раунд считаются как 10 + очки за первый бросок следующего раунда.
5. Если игрок не сбивает все кегли в 2 броска, то его счет за раунд просто равен сумме сбитых кеглей в раунде.

Алгоритм:
-----------------
1. Инициализация: Обнулить счет (totalScore), номер текущего раунда (roundNumber) и список очков по раундам (roundScores).
2. Цикл по 10 раундам:
   - Вывести номер текущего раунда (roundNumber).
   - Спросить у игрока, сколько кеглей он сбил первым броском (pinsFirstThrow).
   - Если pinsFirstThrow равно 10 (страйк):
     - Записать в roundScores количество очков за этот раунд 10.
   - Иначе (не страйк):
     - Спросить у игрока, сколько кеглей он сбил вторым броском (pinsSecondThrow).
     - Записать в roundScores сумму pinsFirstThrow и pinsSecondThrow.
   - Вычислить суммарное количество очков, используя таблицу roundScores.
     - Пройти по всем раундам.
     - Для каждого раунда:
       - Если в раунде страйк, посмотреть два следующих раунда и добавить очки от них.
       - Если в раунде спэр, посмотреть следующий раунд и добавить очки от него.
       - Иначе, добавить очки от текущего раунда.
   - Вывести текущий счет.
3. Конец игры

-----------------
Блок-схема: 
```mermaid
flowchart TD
    Start(Начало) --> Init(Инициализация: totalScore = 0, roundNumber = 1, roundScores = [])
    Init --> LoopStart(Цикл по 10 раундам: roundNumber <= 10)
    LoopStart -- Да --> OutputRound(Вывести номер раунда: roundNumber)
    OutputRound --> InputFirst(Ввод: pinsFirstThrow)
    InputFirst --> StrikeCheck{pinsFirstThrow == 10?}
    StrikeCheck -- Да --> AddStrike(Добавить в roundScores: 10)
    AddStrike --> CalculateScore(Вычислить totalScore)
    CalculateScore --> OutputScore(Вывести totalScore)
    OutputScore --> IncrementRound(roundNumber = roundNumber + 1)
    IncrementRound --> LoopStart
    StrikeCheck -- Нет --> InputSecond(Ввод: pinsSecondThrow)
    InputSecond --> AddRoundScore(Добавить в roundScores: pinsFirstThrow + pinsSecondThrow)
    AddRoundScore --> CalculateScore
    LoopStart -- Нет --> End(Конец)
    
```
"""
def calculate_score(round_scores):
    """
    Вычисляет общий счет по раундам с учетом страйков и спэров.

    Args:
        round_scores (list): Список очков по раундам.

    Returns:
        int: Общий счет.
    """
    total_score = 0 # Итоговый счет
    for round_index in range(len(round_scores)): # Проходимся по всем раундам
        if round_scores[round_index] == 10:  # Проверка на страйк
            if round_index < len(round_scores) - 1: # Проверка есть ли следующий раунд
                next_round_score = round_scores[round_index+1] # получаем очки следующего раунда
                total_score += 10 + next_round_score # Добавляем 10 + очки следующего раунда
                if next_round_score == 10 and round_index < len(round_scores) - 2:
                  total_score += round_scores[round_index+2]
                elif round_index < len(round_scores) - 1 and round_scores[round_index+1]!=10:
                  total_score += round_scores[round_index+1]
            else:
              total_score += 10
        elif round_scores[round_index] > 0: # если не страйк и не 0
            if round_index < len(round_scores) - 1 and round_scores[round_index] + round_scores[round_index+1] == 10:
              if round_index < len(round_scores) -1:
                total_score += 10 # Добавляем 10 + очки следующего раунда
                if round_index < len(round_scores) -2:
                  total_score+=round_scores[round_index+2]
              else:
                total_score+=round_scores[round_index]

            else:
                total_score += round_scores[round_index] # Добавляем очки этого раунда
           
    return total_score


def bowl_game():
    """
    Функция, реализующая игру в боулинг.
    """
    total_score = 0 # Инициализируем общий счет
    round_number = 1 # Инициализируем номер раунда
    round_scores = [] # Инициализируем список очков по раундам

    while round_number <= 10: # Начинаем цикл игры по 10 раундам
        print(f"Раунд {round_number}") # Выводим номер текущего раунда
        pins_first_throw = int(input("Сколько кеглей вы сбили первым броском? ")) # Запрашиваем у пользователя количество сбитых кеглей первым броском
        if pins_first_throw == 10: # Если страйк
            round_scores.append(10) # Добавляем 10 очков в список
            total_score = calculate_score(round_scores) # Высчитываем общий счет
            print(f"Текущий счет: {total_score}") # Выводим текущий счет
            round_number += 1 # Переходим к следующему раунду
        else: # Если не страйк
            pins_second_throw = int(input("Сколько кеглей вы сбили вторым броском? "))  # Запрашиваем у пользователя количество сбитых кеглей вторым броском
            round_scores.append(pins_first_throw + pins_second_throw) # Добавляем сумму сбитых кеглей в список
            total_score = calculate_score(round_scores) # Высчитываем общий счет
            print(f"Текущий счет: {total_score}") # Выводим текущий счет
            round_number += 1 # Переходим к следующему раунду
    
    print("Игра закончена!") # Сообщение об окончании игры

# Запускаем игру
bowl_game()
"""
Пояснения:
calculate_score(round_scores):
    Функция calculate_score принимает список round_scores, содержащий очки за каждый раунд, и вычисляет общий счет с учетом правил начисления очков за страйки и спэры.
    
    - total_score: накапливает итоговый счет
    - round_index: индекс текущего раунда в списке round_scores.
    - Проверка на страйк: если очки в раунде == 10, то это страйк, нужно посчитать очки за два следующих броска.
    - Проверка на спэр: если сумма очков в раунде + следующий раунд == 10 то это спэр, нужно посчитать очки за следующий бросок
    - если не страйк и не спэр добавляем очки текущего раунда.
    - возвращает общий счет.
bowl_game():
    - total_score: накапливает общий счет
    - round_number: хранит номер текущего раунда.
    - round_scores: список хранит набранные очки за каждый раунд.
    - Цикл while обеспечивает прохождение 10 раундов игры.
    - Выводится номер текущего раунда.
    - input(): запрашивает количество сбитых кеглей первым и вторым броском.
    - Добавляем очки за раунд в round_scores.
    - calculate_score вычисляет текущий счет на основе данных в round_scores.
    - текущий счет выводится на экран.
    - round_number увеличивается.
    - После 10 раундов игра заканчивается.
licence:MIT(../licence)
"""
__author__ = 'hypo69 (hypo69@davidka.net)'