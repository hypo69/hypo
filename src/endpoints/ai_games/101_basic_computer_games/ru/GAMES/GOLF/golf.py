"""
GOLF:
=================
Сложность: 3
-----------------
Игра "Гольф" - это текстовая игра, в которой игрок пытается достичь лунки за наименьшее количество ударов. Игрок вводит расстояние до лунки, и программа вычисляет результат удара на основе расстояния и случайного фактора. Цель игры - пройти лунку, нанося удары с различными дистанциями, и завершить игру с минимальным количеством ударов.

Правила игры:
1. Игрок начинает игру с нулевым количеством ударов.
2. Игрок вводит расстояние, на которое он хочет ударить мяч.
3. Программа генерирует случайное отклонение от заданного расстояния, симулируя неточность удара.
4. Программа сообщает игроку фактическое расстояние, на которое был нанесен удар.
5. Программа рассчитывает расстояние до лунки.
6. Игра продолжается до тех пор, пока расстояние до лунки не станет равно нулю.
7. После достижения лунки игра заканчивается, и программа сообщает количество ударов, которое понадобилось для достижения цели.
-----------------
Алгоритм:
1. Установить количество ударов в 0.
2. Установить расстояние до лунки в 250 ярдов.
3. Начать цикл, пока расстояние до лунки не равно 0:
    3.1 Запросить у игрока ввод дистанции удара.
    3.2 Сгенерировать случайное число в диапазоне от -10 до 10 (погрешность удара).
    3.3 Увеличить количество ударов на 1.
    3.4 Вычислить фактическое расстояние удара, добавив погрешность к введенной дистанции.
    3.5 Обновить расстояние до лунки, вычитая фактическое расстояние удара.
    3.6 Вывести сообщение с указанием фактического расстояния удара и оставшегося расстояния до лунки.
4. Вывести сообщение "УРА! Вы добрались до лунки за {количество ударов} ударов."
5. Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация переменных:
    <code><b>
    numberOfHits = 0
    distanceToHole = 250
    </b></code></p>"]
    InitializeVariables --> LoopStart{"Начало цикла: пока <code><b>distanceToHole > 0</b></code>"}
    LoopStart -- Да --> InputDistance["Ввод дистанции удара: <code><b>userDistance</b></code>"]
    InputDistance --> GenerateError["Генерация случайной ошибки: <code><b>error = random(-10, 10)</b></code>"]
    GenerateError --> IncreaseHits["<code><b>numberOfHits = numberOfHits + 1</b></code>"]
    IncreaseHits --> CalculateActualDistance["Вычисление фактической дистанции: <code><b>actualDistance = userDistance + error</b></code>"]
    CalculateActualDistance --> UpdateDistanceToHole["Обновление дистанции до лунки: <code><b>distanceToHole = distanceToHole - actualDistance</b></code>"]
    UpdateDistanceToHole --> OutputDistance["Вывод сообщения: <code><b>actualDistance, distanceToHole</b></code>"]
    OutputDistance --> CheckHole{"Проверка: <code><b>distanceToHole <= 0?</b></code>"}
     CheckHole -- Да --> OutputWin["Вывод сообщения: <b>УРА! Вы добрались до лунки за <code>{numberOfHits}</code> ударов.</b>"]
    OutputWin --> End["Конец"]
    CheckHole -- Нет --> LoopStart
    LoopStart -- Нет --> End
```

Legenda:
    Start - Начало программы.
    InitializeVariables - Инициализация переменных: numberOfHits (количество ударов) устанавливается в 0, а distanceToHole (расстояние до лунки) устанавливается в 250.
    LoopStart - Начало цикла, который продолжается, пока distanceToHole больше 0.
    InputDistance - Запрос у пользователя ввода дистанции удара и сохранение его в переменной userDistance.
    GenerateError - Генерация случайного числа в диапазоне от -10 до 10 (ошибка удара) и сохранение его в переменной error.
    IncreaseHits - Увеличение счетчика количества ударов на 1.
    CalculateActualDistance - Вычисление фактической дистанции удара путем сложения введенной дистанции и ошибки и сохранение в переменной actualDistance.
    UpdateDistanceToHole - Обновление расстояния до лунки путем вычитания фактической дистанции удара и сохранение результата в distanceToHole.
    OutputDistance - Вывод сообщения с указанием фактической дистанции удара и оставшегося расстояния до лунки.
     CheckHole - Проверка, достигли ли мы лунки (distanceToHole <= 0).
     OutputWin - Вывод сообщения о победе с количеством ударов.
    End - Конец программы.
"""
import random

# Инициализируем количество ударов
numberOfHits = 0
# Устанавливаем начальное расстояние до лунки в 250 ярдов
distanceToHole = 250

# Начинаем основной игровой цикл
while distanceToHole > 0:
    # Запрашиваем у пользователя расстояние удара
    try:
        userDistance = float(input("Введите дистанцию удара: "))
    except ValueError:
        print("Пожалуйста, введите число.")
        continue
    # Генерируем случайную ошибку удара в диапазоне от -10 до 10
    error = random.randint(-10, 10)
    # Увеличиваем количество ударов на 1
    numberOfHits += 1
    # Вычисляем фактическое расстояние удара, учитывая ошибку
    actualDistance = userDistance + error
    # Обновляем расстояние до лунки
    distanceToHole -= actualDistance

    # Выводим информацию о текущем ударе и оставшемся расстоянии
    print(f"Фактическая дистанция удара: {actualDistance:.2f} ярдов")
    print(f"Расстояние до лунки: {distanceToHole:.2f} ярдов")

# После выхода из цикла выводим сообщение о победе
print(f"УРА! Вы добрались до лунки за {numberOfHits} ударов.")

"""
Объяснение кода:
1. **Импорт модуля random**:
   - `import random`: Импортирует модуль `random`, который используется для генерации случайных чисел.
2. **Инициализация переменных**:
   - `numberOfHits = 0`: Инициализирует переменную `numberOfHits` для подсчета количества ударов.
   - `distanceToHole = 250`: Устанавливает начальное расстояние до лунки в 250 ярдов.
3. **Основной игровой цикл `while distanceToHole > 0:`**:
   - Этот цикл продолжается до тех пор, пока расстояние до лунки `distanceToHole` не станет меньше или равно 0.
    -  **Ввод данных**:
        -   `try...except ValueError`: Блок try-except обрабатывает возможные ошибки ввода. Если пользователь введет не число, то будет выведено сообщение об ошибке.
        -   `userDistance = float(input("Введите дистанцию удара: "))`: Запрашивает у пользователя дистанцию удара и преобразует ее в число с плавающей точкой.
    - `error = random.randint(-10, 10)`: Генерирует случайное целое число от -10 до 10, которое представляет собой ошибку в ударе.
    - `numberOfHits += 1`: Увеличивает счетчик количества ударов на 1.
    - `actualDistance = userDistance + error`: Вычисляет фактическую дистанцию удара, добавляя ошибку к введенной пользователем дистанции.
    - `distanceToHole -= actualDistance`: Обновляет расстояние до лунки, вычитая из него фактическую дистанцию удара.
    - `print(f"Фактическая дистанция удара: {actualDistance:.2f} ярдов")`: Выводит фактическую дистанцию удара с точностью до двух знаков после запятой.
    - `print(f"Расстояние до лунки: {distanceToHole:.2f} ярдов")`: Выводит оставшееся расстояние до лунки с точностью до двух знаков после запятой.
4. **Вывод сообщения о победе**:
   - `print(f"УРА! Вы добрались до лунки за {numberOfHits} ударов.")`: Выводит сообщение о победе с указанием количества ударов, потребовавшихся для достижения лунки.
"""
