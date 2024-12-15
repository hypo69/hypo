"""
ROCKSP:
=================
Сложность: 2
-----------------
Игра "Камень, ножницы, бумага" - это простая игра для двух игроков, в которой каждый игрок выбирает один из трех вариантов: камень, ножницы или бумага. Победитель определяется по правилам: камень бьет ножницы, ножницы бьют бумагу, бумага бьет камень. Если оба игрока выбирают одинаковый вариант, то объявляется ничья. В этой версии компьютер играет против игрока.
Правила игры:
1.  Игрок выбирает один из трех вариантов: камень (1), ножницы (2) или бумага (3), вводя соответствующую цифру.
2.  Компьютер случайным образом выбирает один из трех вариантов.
3.  Сравниваются выборы игрока и компьютера, и определяется победитель.
4.  Игра заканчивается после определения победителя или ничьей.
-----------------
Алгоритм:
1. Вывести на экран приветственное сообщение и список возможных ходов.
2. Запросить у игрока ввод варианта: камень(1), ножницы(2), бумага(3).
3. Сгенерировать случайный выбор компьютера (1, 2 или 3).
4. Вывести на экран выбор компьютера.
5. Сравнить выбор пользователя и компьютера.
    5.1 Если оба выбора одинаковые, вывести сообщение о ничьей.
    5.2 Если пользователь выбрал камень (1):
        5.2.1 Если компьютер выбрал ножницы (2), вывести сообщение, что пользователь выиграл.
        5.2.2 Если компьютер выбрал бумагу (3), вывести сообщение, что компьютер выиграл.
    5.3 Если пользователь выбрал ножницы (2):
        5.3.1 Если компьютер выбрал бумагу (3), вывести сообщение, что пользователь выиграл.
        5.3.2 Если компьютер выбрал камень (1), вывести сообщение, что компьютер выиграл.
    5.4 Если пользователь выбрал бумагу (3):
        5.4.1 Если компьютер выбрал камень (1), вывести сообщение, что пользователь выиграл.
        5.4.2 Если компьютер выбрал ножницы (2), вывести сообщение, что компьютер выиграл.
6. Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> DisplayOptions["Вывод: 
    <code><b>
    'ROCK, PAPER, SCISSORS'
    '1. ROCK'
    '2. SCISSORS'
    '3. PAPER'
    </b></code>"]
    DisplayOptions --> InputUserChoice["Ввод пользователя: <code><b>userChoice (1, 2 или 3)</b></code>"]
    InputUserChoice --> GenerateComputerChoice["<code><b>computerChoice = random(1, 3)</b></code>"]
    GenerateComputerChoice --> DisplayComputerChoice["Вывод: <code><b>computerChoice</b></code>"]
    DisplayComputerChoice --> CompareChoices{"Сравнение: <code><b>userChoice</b></code> и <code><b>computerChoice</b></code>"}
    CompareChoices -- Ничья --> OutputDraw["Вывод: <b>'IT'S A DRAW'</b>"]
    OutputDraw --> End["Конец"]
    CompareChoices -- userChoice = 1 --> CheckComputerRock["<code><b>computerChoice == 2?</b></code>"]
    CheckComputerRock -- Да --> OutputUserWinRock["Вывод: <b>'YOU WIN, ROCK BEATS SCISSORS'</b>"]
    OutputUserWinRock --> End
    CheckComputerRock -- Нет --> CheckComputerPaper["<code><b>computerChoice == 3?</b></code>"]
    CheckComputerPaper -- Да --> OutputComputerWinRock["Вывод: <b>'I WIN, PAPER BEATS ROCK'</b>"]
    OutputComputerWinRock --> End
    CheckComputerPaper -- Нет --> End
    CompareChoices -- userChoice = 2 --> CheckComputerScissors["<code><b>computerChoice == 3?</b></code>"]
    CheckComputerScissors -- Да --> OutputUserWinScissors["Вывод: <b>'YOU WIN, SCISSORS BEATS PAPER'</b>"]
     OutputUserWinScissors --> End
    CheckComputerScissors -- Нет --> CheckComputerRock2["<code><b>computerChoice == 1?</b></code>"]
    CheckComputerRock2 -- Да --> OutputComputerWinScissors["Вывод: <b>'I WIN, ROCK BEATS SCISSORS'</b>"]
    OutputComputerWinScissors --> End
     CheckComputerRock2 -- Нет --> End
    CompareChoices -- userChoice = 3 --> CheckComputerPaper2["<code><b>computerChoice == 1?</b></code>"]
    CheckComputerPaper2 -- Да --> OutputUserWinPaper["Вывод: <b>'YOU WIN, PAPER BEATS ROCK'</b>"]
    OutputUserWinPaper --> End
    CheckComputerPaper2 -- Нет --> CheckComputerScissors2["<code><b>computerChoice == 2?</b></code>"]
    CheckComputerScissors2 -- Да --> OutputComputerWinPaper["Вывод: <b>'I WIN, SCISSORS BEATS PAPER'</b>"]
     OutputComputerWinPaper --> End
     CheckComputerScissors2 -- Нет --> End
    

```

Legenda:
    Start - Начало игры.
    DisplayOptions - Вывод на экран приветствия и списка доступных ходов: "ROCK, PAPER, SCISSORS", "1. ROCK", "2. SCISSORS", "3. PAPER".
    InputUserChoice - Запрос у пользователя ввода варианта (1, 2 или 3) и сохранение его в переменной userChoice.
    GenerateComputerChoice - Генерация случайного выбора компьютера (1, 2 или 3) и сохранение его в переменной computerChoice.
    DisplayComputerChoice - Вывод на экран выбора компьютера.
    CompareChoices - Сравнение выбора пользователя и компьютера.
    OutputDraw - Вывод сообщения о ничьей, если выборы совпадают.
    CheckComputerRock - Проверка выбора компьютера, если пользователь выбрал камень (1).
    OutputUserWinRock - Вывод сообщения о победе пользователя, если компьютер выбрал ножницы (2) при выборе пользователя камень (1).
    CheckComputerPaper - Проверка выбора компьютера, если пользователь выбрал камень (1).
    OutputComputerWinRock - Вывод сообщения о победе компьютера, если компьютер выбрал бумагу (3) при выборе пользователя камень (1).
    CheckComputerScissors - Проверка выбора компьютера, если пользователь выбрал ножницы (2).
    OutputUserWinScissors - Вывод сообщения о победе пользователя, если компьютер выбрал бумагу (3) при выборе пользователя ножницы (2).
    CheckComputerRock2 - Проверка выбора компьютера, если пользователь выбрал ножницы (2).
    OutputComputerWinScissors - Вывод сообщения о победе компьютера, если компьютер выбрал камень (1) при выборе пользователя ножницы (2).
    CheckComputerPaper2 - Проверка выбора компьютера, если пользователь выбрал бумагу (3).
    OutputUserWinPaper - Вывод сообщения о победе пользователя, если компьютер выбрал камень (1) при выборе пользователя бумагу (3).
    CheckComputerScissors2 - Проверка выбора компьютера, если пользователь выбрал бумагу (3).
    OutputComputerWinPaper - Вывод сообщения о победе компьютера, если компьютер выбрал ножницы (2) при выборе пользователя бумагу (3).
    End - Конец игры.

"""
import random

# Вывод приветствия и списка возможных ходов
print("ROCK, PAPER, SCISSORS")
print("1. ROCK")
print("2. SCISSORS")
print("3. PAPER")

# Получение ввода от пользователя
try:
    userChoice = int(input("YOUR CHOICE? "))
except ValueError:
    print("Некорректный ввод. Пожалуйста, введите число 1, 2 или 3.")
    exit()

# Проверка ввода пользователя на допустимые значения
if userChoice < 1 or userChoice > 3:
    print("Некорректный ввод. Пожалуйста, введите число 1, 2 или 3.")
    exit()

# Генерация случайного выбора компьютера
computerChoice = random.randint(1, 3)

# Вывод выбора компьютера
print("MY CHOICE IS", computerChoice)

# Сравнение выбора пользователя и компьютера и определение победителя
if userChoice == computerChoice:
    print("IT'S A DRAW")
elif userChoice == 1: # Если пользователь выбрал камень
    if computerChoice == 2:
        print("YOU WIN, ROCK BEATS SCISSORS")
    else:
        print("I WIN, PAPER BEATS ROCK")
elif userChoice == 2: # Если пользователь выбрал ножницы
    if computerChoice == 3:
        print("YOU WIN, SCISSORS BEATS PAPER")
    else:
        print("I WIN, ROCK BEATS SCISSORS")
elif userChoice == 3: # Если пользователь выбрал бумагу
    if computerChoice == 1:
        print("YOU WIN, PAPER BEATS ROCK")
    else:
         print("I WIN, SCISSORS BEATS PAPER")
"""
Пояснения:
1.  **Импорт модуля `random`**:
   -  `import random`: Импортирует модуль `random`, который используется для генерации случайного числа, представляющего выбор компьютера.
2.  **Вывод приветствия и меню**:
    -   `print("ROCK, PAPER, SCISSORS")`: Выводит заголовок игры.
    -   `print("1. ROCK")`, `print("2. SCISSORS")`, `print("3. PAPER")`: Выводятся варианты выбора для пользователя.
3.  **Получение выбора пользователя**:
    -   `try...except ValueError`: Блок try-except обрабатывает возможные ошибки ввода. Если пользователь введет не целое число, то будет выведено сообщение об ошибке.
        - `userChoice = int(input("YOUR CHOICE? "))`: Запрашивает у пользователя ввод числа, преобразует его в целое число и сохраняет в `userChoice`.
    -   `if userChoice < 1 or userChoice > 3:`: Проверяет, находится ли ввод пользователя в допустимом диапазоне (1, 2 или 3).
        - `print("Некорректный ввод. Пожалуйста, введите число 1, 2 или 3.")`: Выводит сообщение об ошибке, если ввод некорректен.
        -   `exit()`: Завершает программу, если ввод некорректен.
4.  **Генерация выбора компьютера**:
    -   `computerChoice = random.randint(1, 3)`: Генерирует случайное целое число в диапазоне от 1 до 3 (включительно), представляющее выбор компьютера.
5.  **Вывод выбора компьютера**:
    -   `print("MY CHOICE IS", computerChoice)`: Выводит на экран выбор компьютера.
6.  **Определение победителя**:
    -   `if userChoice == computerChoice:`: Проверяет, одинаковы ли выборы пользователя и компьютера.
        -   `print("IT'S A DRAW")`: Если выборы совпадают, выводится сообщение о ничьей.
    -   **Серия `elif` блоков для проверки различных сценариев**:
    -   `elif userChoice == 1:`: Если пользователь выбрал камень:
        -   `if computerChoice == 2:`: Если компьютер выбрал ножницы, то выводится сообщение о победе пользователя.
        -   `else:`: Если компьютер выбрал бумагу, то выводится сообщение о победе компьютера.
    -    `elif userChoice == 2:`: Если пользователь выбрал ножницы:
        -   `if computerChoice == 3:`: Если компьютер выбрал бумагу, то выводится сообщение о победе пользователя.
        -   `else:`: Если компьютер выбрал камень, то выводится сообщение о победе компьютера.
    -   `elif userChoice == 3:`: Если пользователь выбрал бумагу:
        -  `if computerChoice == 1:`: Если компьютер выбрал камень, то выводится сообщение о победе пользователя.
        -  `else:`: Если компьютер выбрал ножницы, то выводится сообщение о победе компьютера.
"""
```