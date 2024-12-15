"""
STARS:
=================
Сложность: 5
-----------------
Игра "Звезды" - это текстовая игра, в которой игрок вводит количество звезд, которое он хочет увидеть. Компьютер рисует звезды в несколько столбцов, при этом количество звезд может быть до 100.
Цель игры - посмотреть, как программа выводит звезды в зависимости от введенного числа.

Правила игры:
1. Игрок вводит количество звезд, которое нужно нарисовать.
2. Если количество звезд меньше или равно 0, программа выводит сообщение "NOT POSSIBLE".
3. Если количество звезд больше 0, программа рисует звезды в несколько столбцов, в зависимости от введенного числа.
4. Программа завершается после вывода звезд или сообщения "NOT POSSIBLE".

-----------------
Алгоритм:
1. Запросить у игрока количество звезд, которое нужно нарисовать.
2. Если введенное количество звезд меньше или равно 0, вывести сообщение "NOT POSSIBLE" и перейти к шагу 6.
3. Если введенное количество звезд больше 0, установить делитель (divisor) в 20.
4. Вывести "STAR PATTERN", а затем начать цикл "пока количество звезд больше 0":
  4.1. Вычислить количество звезд для текущей строки (stars_to_print) как остаток от деления количества звезд на делитель (divisor).
  4.2. Если stars_to_print равно 0, установить его в divisor.
  4.3. Вывести stars_to_print звезд.
  4.4. Уменьшить общее количество звезд на stars_to_print.
5.  Перейти к шагу 6
6. Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InputStars["Ввод количества звезд: <code><b>totalStars</b></code>"]
    InputStars --> CheckStars["Проверка: <code><b>totalStars <= 0</b></code>?"]
    CheckStars -- Да --> OutputNotPossible["Вывод сообщения: <b>NOT POSSIBLE</b>"]
    OutputNotPossible --> End["Конец"]
    CheckStars -- Нет --> InitializeDivisor["<p align='left'>Инициализация:
    <code><b>divisor = 20</b></code></p>"]
    InitializeDivisor --> OutputPattern["Вывод сообщения: <b>STAR PATTERN</b>"]
    OutputPattern --> LoopStart{"Начало цикла: пока <code><b>totalStars > 0</b></code>"}
    LoopStart -- Да --> CalculateStarsToPrint["<code><b>starsToPrint = totalStars % divisor</b></code>"]
    CalculateStarsToPrint --> CheckStarsToPrint{"Проверка: <code><b>starsToPrint == 0</b></code> ?"}
    CheckStarsToPrint -- Да --> SetStarsToPrint["<code><b>starsToPrint = divisor</b></code>"]
    SetStarsToPrint --> OutputStars["Вывод <code><b>starsToPrint</b></code> звезд"]
    CheckStarsToPrint -- Нет --> OutputStars
    OutputStars --> DecreaseTotalStars["<code><b>totalStars = totalStars - starsToPrint</b></code>"]
    DecreaseTotalStars --> LoopStart
     LoopStart -- Нет --> End
```
Legenda:
    Start - Начало программы.
    InputStars - Запрос у пользователя ввода количества звезд и сохранение его в переменной totalStars.
    CheckStars - Проверка, меньше или равно ли введенное количество звезд 0.
    OutputNotPossible - Вывод сообщения "NOT POSSIBLE", если количество звезд не положительно.
    End - Конец программы.
    InitializeDivisor - Инициализация переменной divisor значением 20.
    OutputPattern - Вывод сообщения "STAR PATTERN".
    LoopStart - Начало цикла, который продолжается, пока totalStars больше 0.
    CalculateStarsToPrint - Вычисление количества звезд для текущей строки как остаток от деления totalStars на divisor.
    CheckStarsToPrint - Проверка, равно ли starsToPrint 0.
    SetStarsToPrint - Установка starsToPrint в значение divisor, если starsToPrint равно 0.
    OutputStars - Вывод starsToPrint звезд.
    DecreaseTotalStars - Уменьшение общего количества звезд totalStars на starsToPrint.
"""
__author__ = 'hypo69 (hypo69@davidka.net)'

# Запрашиваем у пользователя количество звезд
try:
    totalStars = int(input("Введите количество звезд: "))
except ValueError:
    print("Пожалуйста, введите целое число.")
    exit()

# Проверяем, является ли количество звезд положительным
if totalStars <= 0:
    print("NOT POSSIBLE")
else:
    divisor = 20  # Устанавливаем делитель
    print("STAR PATTERN") # Выводим сообщение "STAR PATTERN"
    while totalStars > 0: # Основной цикл, пока количество звезд больше 0
        starsToPrint = totalStars % divisor # Вычисляем количество звезд для текущей строки
        if starsToPrint == 0: # Если остаток от деления равен 0
            starsToPrint = divisor # устанавливаем starsToPrint в divisor
        print("*" * starsToPrint) # Выводим звезды
        totalStars -= starsToPrint # уменьшаем количество звезд
"""
Пояснения:
1.  **Ввод количества звезд**:
    -   `try...except ValueError`: Блок try-except обрабатывает возможные ошибки ввода. Если пользователь введет не целое число, то будет выведено сообщение об ошибке и программа завершится.
    -   `totalStars = int(input("Введите количество звезд: "))`: Запрашивает у пользователя количество звезд и преобразует его в целое число, сохраняя результат в `totalStars`.
2. **Проверка на корректность ввода**:
    -   `if totalStars <= 0:`: Проверяет, является ли введенное количество звезд положительным.
    -   `print("NOT POSSIBLE")`: Если количество звезд меньше или равно нулю, выводится сообщение "NOT POSSIBLE", и программа завершается.
3. **Вывод звездного узора**:
    -   `else:`: Если количество звезд положительное, начинается выполнение этого блока.
    -  `divisor = 20`:  Устанавливает делитель в 20
    -   `print("STAR PATTERN")`: Выводит сообщение "STAR PATTERN".
    -   `while totalStars > 0:`: Начинается цикл `while`, который выполняется до тех пор, пока общее количество звезд `totalStars` больше 0.
    -   `starsToPrint = totalStars % divisor`: Вычисляет остаток от деления `totalStars` на `divisor` и сохраняет его в `starsToPrint`. Это количество звезд, которое будет напечатано в текущей строке.
    -   `if starsToPrint == 0:`: Проверяет, равен ли остаток 0. Если да, значит в текущей строке нужно напечатать starsToPrint = divisor.
         -   `starsToPrint = divisor`: Если остаток равен 0, то устанавливает `starsToPrint` равным `divisor` (20).
    -  `print("*" * starsToPrint)`:  Выводит строку, состоящую из `starsToPrint` символов "*", формируя строку со звездами.
    -   `totalStars -= starsToPrint`: Уменьшает общее количество звезд `totalStars` на количество звезд, напечатанных в текущей строке (`starsToPrint`).
"""
```