"""
NIM:
=================
Сложность: 2
-----------------
Игра "NIM" - это математическая игра для двух игроков. В начале игры на столе лежит некоторое количество спичек (или других предметов). Игроки по очереди берут со стола от одной до трех спичек. Проигрывает тот, кто заберет последнюю спичку. В данной реализации игрок играет против компьютера.
Правила игры:
1. На столе в начале игры 16 спичек.
2. Игроки ходят по очереди. На первом ходу ходит игрок.
3. За один ход можно взять от 1 до 3 спичек.
4. Проигрывает тот, кто заберет последнюю спичку.
-----------------
Алгоритм:
1. Установить начальное количество спичек в 16.
2. Начать цикл "пока количество спичек больше 0":
    2.1 Игрок делает ход:
        2.1.1 Запросить у игрока количество спичек для взятия (от 1 до 3).
        2.1.2 Вычесть выбранное количество спичек из общего количества.
        2.1.3 Если после хода игрока спичек не осталось, то вывести "YOU LOSE". Завершить игру.
    2.2 Компьютер делает ход:
        2.2.1 Вычислить количество спичек, которое нужно взять компьютеру (используя стратегию игры).
        2.2.2 Вычесть выбранное количество спичек из общего количества.
        2.2.3 Если после хода компьютера спичек не осталось, то вывести "I LOSE". Завершить игру.
3. Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeMatches["<p align='left'>Инициализация:
    <code><b>matches = 16</b></code></p>"]
    InitializeMatches --> GameLoopStart{"Начало игрового цикла: <code><b>matches > 0</b></code>"}
    GameLoopStart -- Да --> PlayerTurn["Ход игрока"]
    PlayerTurn --> InputMatches["<p align='left'>Запрос у игрока:
    Сколько спичек взять (1-3)?
    <code><b>playerTakes</b></code></p>"]
    InputMatches --> UpdateMatchesPlayer["<code><b>matches = matches - playerTakes</b></code>"]
    UpdateMatchesPlayer --> CheckMatchesPlayer{"Проверка: <code><b>matches <= 0</b></code>"}
   CheckMatchesPlayer -- Да --> OutputLose["Вывод: <b>YOU LOSE</b>"]
    OutputLose --> End["Конец"]
     CheckMatchesPlayer -- Нет --> ComputerTurn["Ход компьютера"]
    ComputerTurn --> CalculateComputerMove["<p align='left'>Расчет хода компьютера:
    <code><b>computerTakes = (matches - 1) % 4</b></code>
    Если <code><b>computerTakes = 0, computerTakes = 1</b></code></p>"]
    CalculateComputerMove --> UpdateMatchesComputer["<code><b>matches = matches - computerTakes</b></code>"]
    UpdateMatchesComputer --> CheckMatchesComputer{"Проверка: <code><b>matches <= 0</b></code>"}
    CheckMatchesComputer -- Да --> OutputWin["Вывод: <b>I LOSE</b>"]
    OutputWin --> End
    CheckMatchesComputer -- Нет --> GameLoopStart
     GameLoopStart -- Нет --> End
```
Legenda:
    Start - Начало игры.
    InitializeMatches - Инициализация начального количества спичек: matches = 16.
    GameLoopStart - Начало цикла игры: условие - количество спичек matches > 0.
    PlayerTurn - Начало хода игрока.
    InputMatches - Запрос у игрока, сколько спичек он хочет взять (от 1 до 3).
    UpdateMatchesPlayer - Обновление количества спичек после хода игрока: matches = matches - playerTakes.
    CheckMatchesPlayer - Проверка, не закончились ли спички после хода игрока: matches <= 0.
    OutputLose - Вывод сообщения о проигрыше игрока "YOU LOSE".
    End - Конец игры.
    ComputerTurn - Начало хода компьютера.
    CalculateComputerMove - Расчет хода компьютера по стратегии (matches - 1) % 4. Если остаток равен 0, то computerTakes = 1.
    UpdateMatchesComputer - Обновление количества спичек после хода компьютера: matches = matches - computerTakes.
    CheckMatchesComputer - Проверка, не закончились ли спички после хода компьютера: matches <= 0.
    OutputWin - Вывод сообщения о проигрыше компьютера "I LOSE".
"""
__author__ = 'hypo69 (hypo69@davidka.net)'
matches = 16 # Начальное количество спичек
print("Игра НИМ. На столе 16 спичек.")

while matches > 0:
    # Ход игрока
    while True:
      try:
          playerTakes = int(input("Сколько спичек возьмете (1-3)? "))
          if 1 <= playerTakes <= 3:
            break
          else:
            print("Вы должны взять от 1 до 3 спичек.")
      except ValueError:
          print("Пожалуйста, введите целое число.")

    matches -= playerTakes
    print(f"Вы взяли {playerTakes} спичек. Осталось {matches} спичек.")
    if matches <= 0:
        print("YOU LOSE")
        break
    
    # Ход компьютера
    computerTakes = (matches - 1) % 4
    if computerTakes == 0:
        computerTakes = 1
    matches -= computerTakes
    print(f"Я взял {computerTakes} спичек. Осталось {matches} спичек.")
    if matches <= 0:
        print("I LOSE")
        break
"""
Пояснения:
1.  **Инициализация**:
    -   `matches = 16`:  Устанавливает начальное количество спичек равным 16.
    -   `print("Игра НИМ. На столе 16 спичек.")`: Выводит приветственное сообщение.
2.  **Основной игровой цикл**:
    -   `while matches > 0:`: Цикл продолжается, пока на столе есть спички.
3.  **Ход игрока**:
    -   `while True:`: Внутренний цикл для обеспечения корректного ввода игрока.
    -   `playerTakes = int(input("Сколько спичек возьмете (1-3)? "))`: Запрашивает у игрока, сколько спичек он хочет взять.
    -   `if 1 <= playerTakes <= 3: break`: Проверка, что игрок ввел число от 1 до 3, и выход из внутреннего цикла.
    -   `else: print("Вы должны взять от 1 до 3 спичек.")`: Если игрок ввел некорректное число, выводит сообщение об ошибке.
    -   `except ValueError: print("Пожалуйста, введите целое число.")`: Обработка ошибки, если игрок ввел не число.
    -   `matches -= playerTakes`: Уменьшает общее количество спичек на число, которое взял игрок.
    -   `print(f"Вы взяли {playerTakes} спичек. Осталось {matches} спичек.")`: Выводит информацию о том, сколько спичек взял игрок и сколько осталось.
    -   `if matches <= 0: print("YOU LOSE"); break`: Проверка, не взял ли игрок последнюю спичку (он проиграл).
4.  **Ход компьютера**:
    -   `computerTakes = (matches - 1) % 4`: Вычисляет, сколько спичек должен взять компьютер, используя стратегию. Компьютер пытается оставить количество спичек кратным 4+1.
    -  `if computerTakes == 0: computerTakes = 1`: Если после расчета получилось 0 спичек, то берется одна спичка.
    -  `matches -= computerTakes`: Уменьшает общее количество спичек на число, которое взял компьютер.
    -  `print(f"Я взял {computerTakes} спичек. Осталось {matches} спичек.")`: Выводит информацию о том, сколько спичек взял компьютер и сколько осталось.
    -  `if matches <= 0: print("I LOSE"); break`: Проверка, не взял ли компьютер последнюю спичку (он проиграл).
"""
