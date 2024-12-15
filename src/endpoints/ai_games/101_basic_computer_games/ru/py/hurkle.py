"""
HURKLE:
=================
Сложность: 5
-----------------
Игра "HURKLE" - это игра, в которой игрок должен угадать местоположение "хуркла" на карте, состоящей из десяти "городов", расположенных в линейном порядке. 
Игрок начинает с заданным количеством попыток и делает ходы, перемещаясь по городам и угадывая местоположение хуркла. 
После каждого хода игрок получает подсказку о том, находится ли хуркл ближе или дальше от его текущей позиции. 
Игра заканчивается, когда хуркл угадан или у игрока заканчиваются попытки.

Правила игры:
1. Компьютер случайным образом выбирает город от 1 до 10, где будет находиться хуркл.
2. Игрок начинает игру с 5 попытками.
3. Игрок вводит номер города от 1 до 10, где, по его мнению, находится хуркл.
4. После каждого хода компьютер сообщает, стал ли хуркл ближе или дальше от текущей позиции игрока, относительно предыдущего хода.
5. Если игрок угадывает местоположение хуркла, игра заканчивается с сообщением о победе.
6. Если количество попыток игрока заканчивается, игра заканчивается с сообщением о поражении.
-----------------
Алгоритм:
1.  Задать количество попыток (число ходов) равным 5.
2.  Сгенерировать случайное число от 1 до 10 (местоположение хуркла).
3.  Начать цикл "пока количество ходов больше 0":
    3.1 Запросить ввод номера города у игрока.
    3.2 Если введенный номер города совпадает с местоположением хуркла, вывести сообщение о победе и завершить игру.
    3.3 Если номер города не совпадает с местоположением хуркла, уменьшить количество ходов на 1.
    3.4 Вывести подсказку:
        - Если первая попытка, то сообщить, ближе или дальше хуркл, относительно начальной позиции.
        - Если не первая попытка, то сравнить расстояние до хуркла на текущем и предыдущем ходу и сообщить, стал ли хуркл ближе или дальше.
4.  Если цикл завершился, а местоположение хуркла не угадано, вывести сообщение о поражении.
5.  Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация переменных:
    <code><b>
    numberOfGuesses = 5
    hurkleLocation = random(1, 10)
    previousGuess = None
    </b></code></p>"]
    InitializeVariables --> LoopStart{"Начало цикла: пока количество попыток > 0"}
    LoopStart -- Да --> DecreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses - 1</b></code>"]
    DecreaseGuesses --> InputGuess["Ввод номера города пользователем: <code><b>currentGuess</b></code>"]
     InputGuess --> CheckWin{"Проверка: <code><b>currentGuess == hurkleLocation?</b></code>"}
     CheckWin -- Да --> OutputWin["Вывод сообщения: <b>YOU GOT THE HURKLE IN {numberOfGuesses} GUESSES!</b>"]
     OutputWin --> End["Конец"]
    CheckWin -- Нет --> CheckFirstGuess{"<code><b>previousGuess is None?</b></code>"}
    CheckFirstGuess -- Да --> CalculateDistanceFirst["<p align='left'>Вычисление расстояния до хуркла:
    <code><b>
    currentDistance = abs(currentGuess - hurkleLocation)
    </b></code></p>"]
    CalculateDistanceFirst --> SaveCurrentGuess["<code><b>previousGuess = currentGuess</b></code>"]
     SaveCurrentGuess --> OutputHintFirst["<p align='left'>Вывод подсказки:
    <code><b>
        if currentGuess &gt; hurkleLocation:
           print('FURTHER')
        else:
           print('CLOSER')
    </b></code></p>"]
    OutputHintFirst --> LoopStart
     CheckFirstGuess -- Нет --> CalculateDistance["<p align='left'>Вычисление расстояния до хуркла:
    <code><b>
    previousDistance = abs(previousGuess - hurkleLocation)
    currentDistance = abs(currentGuess - hurkleLocation)
    </b></code></p>"]
    CalculateDistance --> CompareDistance{"Проверка: <code><b>currentDistance &lt; previousDistance?</b></code>"}
    CompareDistance -- Да --> OutputHintCloser["Вывод сообщения: <b>CLOSER</b>"]
    OutputHintCloser --> SaveCurrentGuess
    CompareDistance -- Нет --> OutputHintFurther["Вывод сообщения: <b>FURTHER</b>"]
    OutputHintFurther --> SaveCurrentGuess
    SaveCurrentGuess --> LoopStart
    LoopStart -- Нет --> OutputLose["Вывод сообщения: <b>YOU LOSE. THE HURKLE WAS IN {hurkleLocation}</b>"]
    OutputLose --> End
```

Legenda:
    Start - Начало программы.
    InitializeVariables - Инициализация переменных: numberOfGuesses (количество попыток) устанавливается в 5, hurkleLocation (местоположение хуркла) генерируется случайным образом от 1 до 10, previousGuess устанавливается в None.
    LoopStart - Начало цикла, который продолжается, пока количество попыток больше 0.
    DecreaseGuesses - Уменьшение счетчика количества попыток на 1.
    InputGuess - Запрос у пользователя ввода номера города и сохранение его в переменной currentGuess.
    CheckWin - Проверка, равно ли введенное число currentGuess местоположению хуркла hurkleLocation.
    OutputWin - Вывод сообщения о победе, если числа равны, с указанием количества попыток.
    End - Конец программы.
    CheckFirstGuess - Проверка, является ли это первой попыткой (previousGuess равно None).
    CalculateDistanceFirst - Вычисление расстояния от первой попытки до хуркла.
    SaveCurrentGuess - Сохранение текущего предположения в previousGuess.
    OutputHintFirst - Вывод подсказки "CLOSER" или "FURTHER" для первой попытки.
     CalculateDistance - Вычисление расстояния от текущей и предыдущей попытки до хуркла.
    CompareDistance - Проверка, стало ли текущее расстояние до хуркла меньше предыдущего.
    OutputHintCloser - Вывод подсказки "CLOSER", если хуркл стал ближе.
    OutputHintFurther - Вывод подсказки "FURTHER", если хуркл стал дальше.
    OutputLose - Вывод сообщения о поражении и местоположении хуркла, если попытки закончились.
"""
import random

# Инициализация переменных
numberOfGuesses = 5  # Количество попыток
hurkleLocation = random.randint(1, 10)  # Случайное местоположение хуркла от 1 до 10
previousGuess = None  # Предыдущее предположение игрока

# Основной игровой цикл
while numberOfGuesses > 0:
    # Уменьшаем количество попыток
    numberOfGuesses -= 1

    # Запрашиваем ввод у пользователя
    try:
        currentGuess = int(input("Введите номер города от 1 до 10: "))
    except ValueError:
        print("Пожалуйста, введите целое число.")
        continue

    # Проверяем, угадал ли игрок
    if currentGuess == hurkleLocation:
        print(f"ПОЗДРАВЛЯЮ! Вы нашли хуркла за {5 - numberOfGuesses} попыток!")
        break # Завершаем игру если угадали
    
    # Вычисляем расстояние до хуркла
    currentDistance = abs(currentGuess - hurkleLocation)

    # Даём подсказку
    if previousGuess is None: # Первая попытка
         if currentGuess > hurkleLocation:
              print("FURTHER")
         else:
              print("CLOSER")
    else: # Не первая попытка
        previousDistance = abs(previousGuess - hurkleLocation) # Считаем прошлое расстояние
        if currentDistance < previousDistance: # Сравниваем расстояние
            print("CLOSER") # Хуркл стал ближе
        else:
            print("FURTHER") # Хуркл стал дальше
    
    previousGuess = currentGuess  # Сохраняем текущее предположение
    
# Если закончились попытки, игра заканчивается
if numberOfGuesses == 0:
    print(f"Вы проиграли. Хуркл был в городе {hurkleLocation}")
"""
Пояснения:
1.  **Импорт модуля `random`**:
    -   `import random`: Импортирует модуль для генерации случайных чисел.
2.  **Инициализация переменных**:
    -   `numberOfGuesses = 5`: Устанавливает начальное количество попыток игрока равным 5.
    -   `hurkleLocation = random.randint(1, 10)`: Генерирует случайное целое число от 1 до 10, представляющее местоположение хуркла.
    -   `previousGuess = None`: Инициализирует переменную для хранения предыдущего предположения игрока значением `None`.
3.  **Основной цикл `while numberOfGuesses > 0:`**:
    -   Цикл продолжается, пока у игрока есть попытки.
    -   `numberOfGuesses -= 1`: Уменьшает количество попыток после каждой итерации.
    -  **Ввод данных**:
        -   `try...except ValueError`: Блок try-except обрабатывает возможные ошибки ввода. Если пользователь введет не целое число, то будет выведено сообщение об ошибке.
        -   `currentGuess = int(input("Введите номер города от 1 до 10: "))`: Запрашивает у пользователя номер города и преобразует ввод в целое число.
    -   **Проверка на выигрыш**:
        -   `if currentGuess == hurkleLocation:`: Проверяет, угадал ли игрок местоположение хуркла.
        -   `print(f"ПОЗДРАВЛЯЮ! Вы нашли хуркла за {5 - numberOfGuesses} попыток!")`: Выводит сообщение о выигрыше.
        -   `break`: Завершает цикл, если хуркл найден.
    -   **Расчет расстояния**:
         -    `currentDistance = abs(currentGuess - hurkleLocation)`: вычисляем расстояние до хуркла от текущей попытки.
    -   **Подсказки**:
        -  `if previousGuess is None:`: Проверка, является ли это первая попытка.
            -  `if currentGuess > hurkleLocation:`: Если первая попытка и город больше хуркла.
                -  `print("FURTHER")`: Выводим подсказку что нужно двигаться в меньшую сторону.
            -  `else:`: Если первая попытка и город меньше хуркла.
                 -  `print("CLOSER")`: Выводим подсказку что нужно двигаться в большую сторону.
         - `else:`: Если это не первая попытка.
            - `previousDistance = abs(previousGuess - hurkleLocation)`: Вычисляем прошлое расстояние от хуркла.
            - `if currentDistance < previousDistance`: Если текущее расстояние меньше предыдущего.
                - `print("CLOSER")`:  Выводим подсказку что хуркл стал ближе.
            - `else`: если текущее расстояние больше предыдущего.
                - `print("FURTHER")`: Выводим подсказку что хуркл стал дальше.
    -   `previousGuess = currentGuess`: Сохраняет текущее предположение игрока для следующей итерации.
4.  **Проигрыш**:
    -   `if numberOfGuesses == 0:`: Проверяет, закончились ли попытки игрока.
    -   `print(f"Вы проиграли. Хуркл был в городе {hurkleLocation}")`: Выводит сообщение о проигрыше и местоположении хуркла.
"""
```