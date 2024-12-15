"""
BOXING:
=================
Сложность: 5
-----------------
Игра "Бокс" - это текстовая игра, имитирующая боксерский поединок между игроком и компьютером. В игре используются случайные числа, чтобы определить, попал ли удар или нет. Игрок и компьютер поочередно наносят удары, и игра заканчивается, когда один из "боксеров" терпит поражение.

Правила игры:
1.  Игрок и компьютер поочередно наносят удары.
2.  Удар считается успешным, если случайно сгенерированное число меньше 5.
3.  Успешный удар уменьшает "здоровье" противника на 20 единиц.
4.  Игра продолжается до тех пор, пока "здоровье" одного из боксеров не упадет до 0 или ниже.
5.  Выводится сообщение о победителе.
-----------------
Алгоритм:
1.  Установить здоровье игрока (PL) и компьютера (CO) в 100.
2.  Начать цикл "пока здоровье игрока больше 0 и здоровье компьютера больше 0":
    2.1 Игрок наносит удар:
        2.1.1 Сгенерировать случайное число от 0 до 9.
        2.1.2 Если число меньше 5, уменьшить здоровье компьютера на 20 и вывести сообщение "HIT!".
        2.1.3 Иначе вывести сообщение "MISS!".
    2.2 Если здоровье компьютера <= 0, перейти к шагу 3.
    2.3 Компьютер наносит удар:
        2.3.1 Сгенерировать случайное число от 0 до 9.
        2.3.2 Если число меньше 5, уменьшить здоровье игрока на 20 и вывести сообщение "I HIT YOU!".
        2.3.3 Иначе вывести сообщение "I MISSED!".
    2.4 Если здоровье игрока <= 0, перейти к шагу 3.
3.  Если здоровье игрока <= 0, вывести сообщение "I WIN!".
4.  Иначе, вывести сообщение "YOU WIN!".
5.  Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeHealth["<p align='left'>Инициализация здоровья:
    <code><b>
    playerHealth = 100
    computerHealth = 100
    </b></code></p>"]
    InitializeHealth --> LoopStart{"Начало цикла: пока оба живы"}
    LoopStart -- Да --> PlayerTurn["Ход игрока"]
    PlayerTurn --> GenerateRandomPlayer["<code><b>randomPlayer = random(0,9)</b></code>"]
    GenerateRandomPlayer --> CheckPlayerHit{"<code><b>randomPlayer < 5?</b></code>"}
    CheckPlayerHit -- Да --> PlayerHit["<p align='left'>Удар игрока: 
    <code><b>
    computerHealth = computerHealth - 20
    </b></code><br>Вывод: <b>HIT!</b></p>"]
    PlayerHit --> CheckComputerHealth{"<code><b>computerHealth <= 0?</b></code>"}
    CheckPlayerHit -- Нет --> PlayerMiss["Вывод: <b>MISS!</b>"]
    PlayerMiss --> CheckComputerHealth
    CheckComputerHealth -- Да --> OutputPlayerWin["Вывод: <b>YOU WIN!</b>"]
    OutputPlayerWin --> End["Конец"]
    CheckComputerHealth -- Нет --> ComputerTurn["Ход компьютера"]
    ComputerTurn --> GenerateRandomComputer["<code><b>randomComputer = random(0,9)</b></code>"]
    GenerateRandomComputer --> CheckComputerHit{"<code><b>randomComputer < 5?</b></code>"}
    CheckComputerHit -- Да --> ComputerHit["<p align='left'>Удар компьютера: 
    <code><b>
    playerHealth = playerHealth - 20
    </b></code><br>Вывод: <b>I HIT YOU!</b></p>"]
    ComputerHit --> CheckPlayerHealth{"<code><b>playerHealth <= 0?</b></code>"}
    CheckComputerHit -- Нет --> ComputerMiss["Вывод: <b>I MISSED!</b>"]
    ComputerMiss --> CheckPlayerHealth
    CheckPlayerHealth -- Да --> OutputComputerWin["Вывод: <b>I WIN!</b>"]
    OutputComputerWin --> End
    CheckPlayerHealth -- Нет --> LoopStart
    LoopStart -- Нет --> End

```

Legenda:
    Start - Начало игры.
    InitializeHealth - Инициализация здоровья игрока и компьютера (оба по 100).
    LoopStart - Начало цикла, который продолжается, пока оба игрока имеют здоровье больше 0.
    PlayerTurn - Ход игрока.
    GenerateRandomPlayer - Генерация случайного числа (от 0 до 9) для хода игрока.
    CheckPlayerHit - Проверка, был ли удар игрока успешным (если случайное число меньше 5).
    PlayerHit - Уменьшение здоровья компьютера на 20 и вывод сообщения "HIT!".
    PlayerMiss - Вывод сообщения "MISS!", если удар игрока не попал.
    CheckComputerHealth - Проверка, не закончилось ли здоровье компьютера.
    OutputPlayerWin - Вывод сообщения "YOU WIN!", если здоровье компьютера закончилось.
    ComputerTurn - Ход компьютера.
    GenerateRandomComputer - Генерация случайного числа (от 0 до 9) для хода компьютера.
    CheckComputerHit - Проверка, был ли удар компьютера успешным (если случайное число меньше 5).
    ComputerHit - Уменьшение здоровья игрока на 20 и вывод сообщения "I HIT YOU!".
    ComputerMiss - Вывод сообщения "I MISSED!", если удар компьютера не попал.
    CheckPlayerHealth - Проверка, не закончилось ли здоровье игрока.
    OutputComputerWin - Вывод сообщения "I WIN!", если здоровье игрока закончилось.
    End - Конец игры.
"""
import random

# Инициализация здоровья игрока и компьютера
playerHealth = 100
computerHealth = 100

# Основной игровой цикл
while playerHealth > 0 and computerHealth > 0:
    # Ход игрока
    print("Ваш ход:")
    randomPlayer = random.randint(0, 9) # Генерируем случайное число для удара игрока
    if randomPlayer < 5: # Проверяем, был ли удар успешным
        computerHealth -= 20 # Уменьшаем здоровье компьютера на 20
        print("HIT!")
    else:
        print("MISS!")
        
    # Проверка, не победил ли игрок
    if computerHealth <= 0:
        break
    
    # Ход компьютера
    print("Мой ход:")
    randomComputer = random.randint(0, 9) # Генерируем случайное число для удара компьютера
    if randomComputer < 5: # Проверяем, был ли удар успешным
        playerHealth -= 20 # Уменьшаем здоровье игрока на 20
        print("I HIT YOU!")
    else:
        print("I MISSED!")
        
    # Проверка, не победил ли компьютер
    if playerHealth <= 0:
        break

# Вывод результата игры
if playerHealth <= 0:
    print("I WIN!")
else:
    print("YOU WIN!")
"""
Пояснения:
1.  **Импорт модуля `random`**:
    - `import random`: Импортирует модуль `random`, который используется для генерации случайных чисел.
2. **Инициализация переменных**:
    -   `playerHealth = 100`: Устанавливает начальное значение здоровья игрока на 100.
    -   `computerHealth = 100`: Устанавливает начальное значение здоровья компьютера на 100.
3. **Основной игровой цикл**:
   -  `while playerHealth > 0 and computerHealth > 0:`: Цикл продолжается, пока здоровье обоих игроков больше 0.
4.  **Ход игрока**:
    -   `print("Ваш ход:")`: Выводит сообщение о начале хода игрока.
    -   `randomPlayer = random.randint(0, 9)`: Генерирует случайное целое число в диапазоне от 0 до 9 (включительно) для удара игрока.
    -   `if randomPlayer < 5:`: Проверяет, меньше ли случайное число 5, что означает успешный удар.
        -   `computerHealth -= 20`: Уменьшает здоровье компьютера на 20.
        -   `print("HIT!")`: Выводит сообщение об успешном ударе.
    -   `else:`: Если удар не был успешным.
        -   `print("MISS!")`: Выводит сообщение о промахе.
    - `if computerHealth <= 0: break`: Проверяет, не закончилось ли здоровье компьютера, и если да, то выходит из цикла.
5.  **Ход компьютера**:
    -   `print("Мой ход:")`: Выводит сообщение о начале хода компьютера.
    -   `randomComputer = random.randint(0, 9)`: Генерирует случайное целое число в диапазоне от 0 до 9 для удара компьютера.
    -   `if randomComputer < 5:`: Проверяет, был ли удар успешным.
        -   `playerHealth -= 20`: Уменьшает здоровье игрока на 20.
        -   `print("I HIT YOU!")`: Выводит сообщение об ударе компьютера.
    -   `else:`: Если удар не был успешным.
        -   `print("I MISSED!")`: Выводит сообщение о промахе компьютера.
     -   `if playerHealth <= 0: break`: Проверяет, не закончилось ли здоровье игрока, и если да, то выходит из цикла.
6.  **Вывод результатов**:
    -   `if playerHealth <= 0:`: Проверяет, закончилось ли здоровье игрока.
        -   `print("I WIN!")`: Выводит сообщение о победе компьютера.
    -  `else:`: Если здоровье игрока не закончилось.
        -   `print("YOU WIN!")`: Выводит сообщение о победе игрока.
"""
