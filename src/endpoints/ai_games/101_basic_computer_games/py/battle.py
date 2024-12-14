"""
<BATTLE>:
=================
Сложность: 4
-----------------
Игра "Битва" представляет собой простую стратегическую игру, где два игрока по очереди атакуют друг друга. Каждый игрок имеет определённое количество сил (единиц), и при атаке случайным образом наносится урон противнику. Цель игры - уничтожить силы противника. Игрок, у которого силы опускаются до нуля или ниже, проигрывает. 
Правила игры:
1. В начале игры каждому игроку присваивается 100 единиц сил.
2. Игроки ходят по очереди.
3. В свой ход игрок атакует противника, нанося ему случайный урон от 1 до 15 единиц.
4. Игра продолжается до тех пор, пока у одного из игроков количество сил не станет равным или меньше нуля.
5. Игрок, у которого силы оказались равными или меньше нуля, проигрывает.
-----------------
Алгоритм:
1. Установить начальное количество сил для игрока 1 (player1_strength) и игрока 2 (player2_strength) равным 100.
2. Начать игровой цикл.
3. Вывести на экран текущее количество сил каждого игрока.
4. Игрок 1 атакует:
    a. Сгенерировать случайное число (attack_damage) от 1 до 15.
    b. Вычесть damage_attack из player2_strength.
5. Вывести на экран результат атаки игрока 1 и новое количество сил игрока 2.
6. Если player2_strength <= 0, то вывести сообщение о победе игрока 1 и закончить игру.
7. Игрок 2 атакует:
    a. Сгенерировать случайное число (attack_damage) от 1 до 15.
    b. Вычесть attack_damage из player1_strength.
8. Вывести на экран результат атаки игрока 2 и новое количество сил игрока 1.
9. Если player1_strength <= 0, то вывести сообщение о победе игрока 2 и закончить игру.
10. Перейти к шагу 2.
-----------------
Блок-схема:
```mermaid
graph TD
    Start(Start) --> Initialize(Initialize Player Strengths);
    Initialize --> Player1TurnStart(Player 1 Turn Start);
    Player1TurnStart --> DisplayStrengths(Display Player Strengths);
    DisplayStrengths --> Player1Attack(Player 1 Attack);
    Player1Attack --> Player2StrengthUpdate(Update Player 2 Strength);
    Player2StrengthUpdate --> DisplayPlayer1AttackResult(Display Player 1 Attack Result);
    DisplayPlayer1AttackResult --> Player2LostCheck(Check if Player 2 Lost);
    Player2LostCheck -- Yes --> Player1Win(Player 1 Win);
    Player2LostCheck -- No --> Player2TurnStart(Player 2 Turn Start);
    Player1Win --> End(End);    
    Player2TurnStart --> Player2Attack(Player 2 Attack);
    Player2Attack --> Player1StrengthUpdate(Update Player 1 Strength);
    Player1StrengthUpdate --> DisplayPlayer2AttackResult(Display Player 2 Attack Result);
    DisplayPlayer2AttackResult --> Player1LostCheck(Check if Player 1 Lost);
    Player1LostCheck -- Yes --> Player2Win(Player 2 Win);
    Player1LostCheck -- No --> Player1TurnStart;
    Player2Win --> End;
```
"""
import random

# Устанавливаем начальное количество сил для обоих игроков
player1_strength = 100 # Сила первого игрока
player2_strength = 100 # Сила второго игрока

# Начинаем основной игровой цикл
while True:
    # Выводим текущее количество сил у обоих игроков
    print("Сила Игрока 1:", player1_strength) 
    print("Сила Игрока 2:", player2_strength)
    
    # Атака игрока 1
    attack_damage = random.randint(1, 15) # Генерируем случайное значение урона от 1 до 15
    player2_strength -= attack_damage # Уменьшаем силу игрока 2 на величину урона
    print("Игрок 1 атакует Игрока 2 и наносит", attack_damage, "урона.") # Выводим результат атаки
    print("Сила Игрока 2 теперь:", player2_strength)

    # Проверка на победу игрока 1
    if player2_strength <= 0:
        print("Игрок 1 победил!") # Выводим сообщение о победе
        break # Завершаем игру

    # Атака игрока 2
    attack_damage = random.randint(1, 15) # Генерируем случайное значение урона от 1 до 15
    player1_strength -= attack_damage # Уменьшаем силу игрока 1 на величину урона
    print("Игрок 2 атакует Игрока 1 и наносит", attack_damage, "урона.") # Выводим результат атаки
    print("Сила Игрока 1 теперь:", player1_strength)

    # Проверка на победу игрока 2
    if player1_strength <= 0:
        print("Игрок 2 победил!") # Выводим сообщение о победе
        break # Завершаем игру
"""
Пояснения:
1. `player1_strength` и `player2_strength`: переменные для хранения текущего количества сил у каждого игрока. Изначально установлено значение 100.
2. `while True:`: Бесконечный цикл, который продолжается до тех пор, пока не произойдет победа одного из игроков.
3. `random.randint(1, 15)`: Функция для генерации случайного целого числа от 1 до 15 включительно, представляющего собой урон от атаки.
4. Операторы `-=`: Уменьшают текущую силу игрока на величину нанесенного урона.
5. `if player1_strength <= 0` и `if player2_strength <= 0`: Условные операторы, которые проверяют, не опустилось ли количество сил у одного из игроков до нуля или ниже. Если да, то выводится сообщение о победе другого игрока, и игра завершается оператором `break`.
6. Каждая атака сопровождается выводом сообщения о том, кто атаковал, какой урон был нанесен и какое количество сил осталось у атакуемого игрока.
licence:MIT(../licence)
"""
__author__ = 'hypo69 (hypo69@davidka.net)'
```