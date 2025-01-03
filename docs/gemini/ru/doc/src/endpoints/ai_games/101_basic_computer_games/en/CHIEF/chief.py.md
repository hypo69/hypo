# CHIEF

## Обзор

Игра "CHIEF" - это игра, в которой игрок выступает в роли начальника, планирующего производство на фабрике. Игрок устанавливает количество произведенных изделий каждого типа, и компьютер определяет, соответствуют ли эти значения необходимым требованиям. Если нет, игроку сообщается, какие именно значения были неверны. Цель игры - достичь оптимального производства, правильно угадывая количество изделий.

## Оглавление

- [Обзор](#обзор)
- [Функции](#функции)
- [Алгоритм](#алгоритм)
- [Блок-схема](#блок-схема)
- [Объяснение кода](#объяснение-кода)

## Функции

В данном коде не используются отдельные функции, весь код выполняется в глобальной области видимости.

## Алгоритм
1.  Сгенерировать случайные целые числа `targetA`, `targetB` и `targetC` в диапазоне от 1 до 10.
2.  Начать цикл "пока не угаданы все числа":
    2.1 Запросить у игрока ввод трех целых чисел: `userA`, `userB` и `userC`.
    2.2 Инициализировать строку `message` как пустую.
    2.3 Если `userA` не равно `targetA`, добавить "A" к `message`.
    2.4 Если `userB` не равно `targetB`, добавить "B" к `message`.
    2.5 Если `userC` не равно `targetC`, добавить "C" к `message`.
    2.6 Если `message` не пустая, вывести сообщение "WRONG ON " и `message`.
    2.7 Иначе, вывести сообщение "YOU GOT IT!".
3. Конец игры.

## Блок-схема

```mermaid
flowchart TD
    Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация переменных:\n    <code><b>\n    targetA = random(1, 10)\n    targetB = random(1, 10)\n    targetC = random(1, 10)\n    </b></code></p>"]
    InitializeVariables --> LoopStart{"Начало цикла: пока не угадано"}
    LoopStart --> InputValues["<p align='left'>Ввод чисел пользователем:\n    <code><b>\n    userA\n    userB\n    userC\n    </b></code></p>"]
    InputValues --> InitializeMessage["<code><b>message = ""</b></code>"]
    InitializeMessage --> CheckA{"Проверка: <code><b>userA == targetA?</b></code>"}
    CheckA -- Нет --> AppendA["<code><b>message = message + 'A'</b></code>"]
    AppendA --> CheckB{"Проверка: <code><b>userB == targetB?</b></code>"}
    CheckA -- Да --> CheckB
    CheckB -- Нет --> AppendB["<code><b>message = message + 'B'</b></code>"]
    AppendB --> CheckC{"Проверка: <code><b>userC == targetC?</b></code>"}
    CheckB -- Да --> CheckC
    CheckC -- Нет --> AppendC["<code><b>message = message + 'C'</b></code>"]
    AppendC --> CheckMessage{"Проверка: <code><b>message != "" ?</b></code>"}
    CheckC -- Да --> CheckMessage
    CheckMessage -- Да --> OutputWrong["Вывод сообщения: <b>WRONG ON {message}</b>"]
    OutputWrong --> LoopStart
    CheckMessage -- Нет --> OutputWin["Вывод сообщения: <b>YOU GOT IT!</b>"]
    OutputWin --> End["Конец"]
    LoopStart -- Нет --> End
```

## Объяснение кода

1.  **Импорт модуля `random`**:
    -   `import random`: Импортирует модуль `random`, необходимый для генерации случайных чисел.

2.  **Генерация случайных чисел**:
    -   `targetA = random.randint(1, 10)`: Генерирует случайное целое число от 1 до 10 и присваивает его переменной `targetA`.
    -   `targetB = random.randint(1, 10)`: Генерирует случайное целое число от 1 до 10 и присваивает его переменной `targetB`.
    -   `targetC = random.randint(1, 10)`: Генерирует случайное целое число от 1 до 10 и присваивает его переменной `targetC`.
    Эти переменные представляют собой загаданные числа, которые игрок должен угадать.
3.  **Основной игровой цикл**:
    -   `while True:`: Запускает бесконечный цикл, который будет продолжаться до тех пор, пока игрок не угадает все три числа.
    -   **Ввод чисел от пользователя**:
    	-	`try...except ValueError`: Блок `try-except` обрабатывает возможные ошибки ввода. Если пользователь введет не целое число, то будет выведено сообщение об ошибке.
    	-  `userA = int(input("Введите число для A (от 1 до 10): "))`: Запрашивает у пользователя ввод числа для `A`, преобразует его в целое число и сохраняет в переменной `userA`.
    	-  Аналогично, запрашивает ввод чисел для `B` и `C` и сохраняет их в `userB` и `userC` соответственно.
    -   `message = ""`: Инициализирует пустую строку `message`, которая будет использоваться для хранения информации о том, какие числа были введены неправильно.
4.  **Проверка введенных чисел**:
    -  `if userA != targetA:`: Проверяет, не равно ли введенное пользователем число `userA` загаданному числу `targetA`.
    -  `message += "A"`: Если `userA` не равно `targetA`, добавляет символ "A" к строке `message`, указывая, что число `A` было введено неверно.
    - Аналогичные проверки выполняются для чисел `B` и `C`.
5.  **Вывод результатов**:
    -   `if message != "":`: Проверяет, не пуста ли строка `message`.
    -   `print(f"WRONG ON {message}")`: Если строка `message` не пуста, выводит сообщение о том, какие числа были введены неправильно (например, "WRONG ON AB" - это означает, что числа `A` и `B` были введены неверно).
    -   `else:`: Выполняется, если строка `message` пуста (то есть все числа угаданы правильно).
    -   `print("YOU GOT IT!")`: Выводит сообщение о победе.
    -   `break`: Завершает цикл и игру, если все числа угаданы.