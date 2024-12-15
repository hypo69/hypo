"""
GUNNER:
=================
Сложность: 5
-----------------
Игра "Артиллерист" - это игра, в которой игрок пытается сбить цель, выпуская снаряды под определенным углом и с определенной скоростью. Цель расположена на фиксированном расстоянии.
Игрок должен подобрать оптимальные значения для угла и скорости, чтобы попасть в цель. Игра заканчивается, когда цель поражена.

Правила игры:
1. Компьютер устанавливает фиксированное расстояние до цели.
2. Игрок вводит угол и скорость выстрела.
3. Программа вычисляет расстояние, на которое упадет снаряд.
4. Если расстояние до цели равно расстоянию падения снаряда, цель поражена, игра заканчивается.
5. Если расстояние до цели не равно расстоянию падения снаряда, игрок вводит новые параметры выстрела.
-----------------
Алгоритм:
1. Установить расстояние до цели (TARGET) равным 1000.
2. Начать цикл "пока цель не поражена":
    2.1 Запросить у игрока ввод угла (ANGLE) в градусах.
    2.2 Запросить у игрока ввод скорости (VELOCITY).
    2.3 Перевести угол из градусов в радианы (RADIAN = ANGLE * 0.01745).
    2.4 Вычислить расстояние полета снаряда (DISTANCE = (VELOCITY * VELOCITY) / 32 * SIN(2 * RADIAN)).
    2.5 Если расстояние полета снаряда (DISTANCE) равно расстоянию до цели (TARGET), вывести сообщение "YOU GOT HIM !!!" и закончить игру.
    2.6 Иначе, если расстояние полета снаряда больше расстояния до цели, вывести сообщение "YOU OVER SHOT HIM".
    2.7 Иначе вывести сообщение "YOU UNDER SHOT HIM".
3. Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeTarget["<p align='left'>Инициализация переменной:
    <code><b>
    targetDistance = 1000
    </b></code></p>"]
    InitializeTarget --> LoopStart{"Начало цикла: пока цель не поражена"}
    LoopStart -- Да --> InputAngle["Ввод угла пользователем: <code><b>userAngle</b></code>"]
    InputAngle --> InputVelocity["Ввод скорости пользователем: <code><b>userVelocity</b></code>"]
    InputVelocity --> CalculateRadian["<code><b>radian = userAngle * 0.01745</b></code>"]
    CalculateRadian --> CalculateDistance["<code><b>distance = (userVelocity * userVelocity) / 32 * sin(2 * radian)</b></code>"]
    CalculateDistance --> CheckHit{"Проверка: <code><b>distance == targetDistance?</b></code>"}
    CheckHit -- Да --> OutputHit["Вывод сообщения: <b>YOU GOT HIM !!!</b>"]
    OutputHit --> End["Конец"]
    CheckHit -- Нет --> CheckOverShot{"Проверка: <code><b>distance > targetDistance</b></code>?"}
    CheckOverShot -- Да --> OutputOverShot["Вывод сообщения: <b>YOU OVER SHOT HIM</b>"]
    OutputOverShot --> LoopStart
    CheckOverShot -- Нет --> OutputUnderShot["Вывод сообщения: <b>YOU UNDER SHOT HIM</b>"]
    OutputUnderShot --> LoopStart
    LoopStart -- Нет --> End
```
    
Legenda:
    Start - Начало программы.
    InitializeTarget - Инициализация переменной targetDistance (расстояние до цели) устанавливается в 1000.
    LoopStart - Начало цикла, который продолжается, пока цель не поражена.
    InputAngle - Запрос у пользователя ввода угла и сохранение его в переменной userAngle.
    InputVelocity - Запрос у пользователя ввода скорости и сохранение его в переменной userVelocity.
    CalculateRadian - Вычисление угла в радианах radian = userAngle * 0.01745.
    CalculateDistance - Вычисление расстояния полета снаряда distance = (userVelocity * userVelocity) / 32 * sin(2 * radian).
    CheckHit - Проверка, равно ли расстояние полета снаряда distance расстоянию до цели targetDistance.
    OutputHit - Вывод сообщения о победе "YOU GOT HIM !!!", если цель поражена.
    End - Конец программы.
    CheckOverShot - Проверка, больше ли расстояние полета снаряда distance расстояния до цели targetDistance.
    OutputOverShot - Вывод сообщения "YOU OVER SHOT HIM", если перелет.
    OutputUnderShot - Вывод сообщения "YOU UNDER SHOT HIM", если недолет.
"""
import math

__author__ = 'hypo69 (hypo69@davidka.net)'

# Устанавливаем расстояние до цели
targetDistance = 1000

# Основной игровой цикл
while True:
    # Запрашиваем у игрока угол выстрела в градусах
    try:
        userAngle = float(input("Введите угол выстрела в градусах: "))
    except ValueError:
        print("Пожалуйста, введите число.")
        continue

    # Запрашиваем у игрока скорость выстрела
    try:
        userVelocity = float(input("Введите скорость выстрела: "))
    except ValueError:
        print("Пожалуйста, введите число.")
        continue

    # Преобразуем угол из градусов в радианы
    radian = userAngle * 0.01745

    # Вычисляем дальность полета снаряда
    distance = (userVelocity * userVelocity) / 32 * math.sin(2 * radian)

    # Проверяем, попал ли снаряд в цель
    if abs(distance - targetDistance) < 0.001: # Используем маленькую погрешность для сравнения float
        print("YOU GOT HIM !!!")
        break  # Завершаем цикл, если цель поражена
    elif distance > targetDistance:
        print("YOU OVER SHOT HIM")  # Сообщаем, что перелет
    else:
        print("YOU UNDER SHOT HIM")  # Сообщаем, что недолет
"""
Пояснения:
1.  **Импорт модуля `math`**:
    -   `import math`: Импортирует модуль `math`, который предоставляет математические функции, такие как `sin` и `pi`.
2.  **Инициализация `targetDistance`**:
    -   `targetDistance = 1000`: Устанавливает расстояние до цели в 1000 единиц.
3.  **Основной цикл `while True:`**:
    -   Бесконечный цикл, который продолжается до тех пор, пока игрок не поразит цель.
    -   **Ввод данных**:
        -   `try...except ValueError`: Блок try-except обрабатывает возможные ошибки ввода. Если пользователь введет не число, то будет выведено сообщение об ошибке.
        -   `userAngle = float(input("Введите угол выстрела в градусах: "))`: Запрашивает у пользователя угол выстрела и преобразует его в число с плавающей точкой.
        -   `userVelocity = float(input("Введите скорость выстрела: "))`: Запрашивает у пользователя скорость выстрела и преобразует ее в число с плавающей точкой.
    -   **Преобразование угла в радианы**:
        -   `radian = userAngle * 0.01745`: Преобразует угол из градусов в радианы, так как тригонометрические функции в Python работают с радианами.
    -   **Вычисление дальности полета**:
        -   `distance = (userVelocity * userVelocity) / 32 * math.sin(2 * radian)`: Вычисляет дальность полета снаряда по формуле.
    -   **Проверка попадания**:
        -   `if abs(distance - targetDistance) < 0.001:`: Проверяет, попал ли снаряд в цель. Используется `abs()` для сравнения с погрешностью, так как вычисления с плавающей точкой могут быть неточными.
        -   `print("YOU GOT HIM !!!")`: Выводит сообщение о победе, если цель поражена.
        -   `break`: Завершает цикл (игру), если цель поражена.
    -   **Подсказки**:
        -   `elif distance > targetDistance:`: Проверяет, перелетел ли снаряд.
        -   `print("YOU OVER SHOT HIM")`: Выводит подсказку о перелете.
        -   `else:`: Если снаряд не перелетел и не попал, значит, он не долетел.
        -   `print("YOU UNDER SHOT HIM")`: Выводит подсказку о недолете.
"""
```