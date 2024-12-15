"""
<ORBIT>:
=================
Сложность: 5
-----------------
Игра "ORBIT" - это простая игра, в которой игрок управляет ракетой, вращающейся вокруг планеты. Цель игры - маневрировать ракетой, чтобы успешно достичь орбиты.  Игрок вводит угол старта (в градусах) и скорость ракеты. Игра моделирует траекторию ракеты и сообщает, достигла ли ракета орбиты, упала на планету или улетела в космос. 
-----------------
Правила игры:
1.  Игрок вводит начальный угол запуска ракеты (в градусах) и начальную скорость ракеты.
2.  Игра вычисляет траекторию ракеты на основе введенных параметров.
3.  Если ракета достигает определенной высоты над планетой (условно задано), то считается, что ракета вышла на орбиту.
4.  Если ракета не достигает нужной высоты или падает на планету, то это считается провалом.
5.  Игра выводит результат - "Орбита!", "Слишком низко!" или "Слишком высоко!".

-----------------
Алгоритм:
1. Задать константу радиуса планеты `planetRadius` равной 20.
2. Запросить у игрока начальный угол запуска ракеты `launchAngle` в градусах.
3. Запросить у игрока начальную скорость ракеты `launchVelocity`.
4. Перевести угол запуска `launchAngle` в радианы `launchAngleRad`.
5. Рассчитать начальные координаты ракеты `rocketX` и `rocketY`: `rocketX` = 20 * cos(угол в радианах), `rocketY` = 20 * sin(угол в радианах).
6. Задать начальное время `currentTime` = 0.
7. Задать временной шаг `timeStep` = 0.1.
8. В цикле, пока время `currentTime` меньше 10:
    9.  Рассчитать новые координаты ракеты `rocketX` и `rocketY` с учетом времени и скорости: 
        `rocketX` = 20 * cos(угол в радианах) + скорость * время * cos(угол в радианах)
        `rocketY` = 20 * sin(угол в радианах) + скорость * время * sin(угол в радианах)  - 1/2 * (9.8 * время^2)
    10. Рассчитать расстояние ракеты от центра планеты `rocketDistance` = sqrt(x^2 + y^2)
    11. Если `rocketDistance`  больше, чем 25, то вывести "Слишком высоко!" и перейти к шагу 14.
    12. Если `rocketDistance` меньше, чем 19, то вывести "Слишком низко!" и перейти к шагу 14.
    13. Увеличить время `currentTime` на `timeStep`.
14. Вывести "Орбита!" если цикл завершился успешно.
15. Завершить игру.
-----------------
Блок-схема:
```mermaid
graph TD
    Start(Start) --> InputAngle(Input launchAngle in degrees)
    InputAngle --> InputVelocity(Input launchVelocity)
    InputVelocity --> AngleToRad(Convert launchAngle to launchAngleRad)
    AngleToRad --> CalcStartPos(Calculate initial rocketX and rocketY)
    CalcStartPos --> InitTime(Initialize currentTime = 0)
    InitTime --> LoopStart(Loop: currentTime < 10)
    LoopStart -- Yes --> CalcRocketPos(Calculate new rocketX and rocketY)
    CalcRocketPos --> CalcDistance(Calculate rocketDistance)
    CalcDistance --> CheckHigh(Check if rocketDistance > 25)
    CheckHigh -- Yes --> OutputHigh(Output "Too high!")
    OutputHigh --> End(End)
    CheckHigh -- No --> CheckLow(Check if rocketDistance < 19)
    CheckLow -- Yes --> OutputLow(Output "Too low!")
    OutputLow --> End
    CheckLow -- No --> IncrementTime(Increment currentTime by timeStep)
    IncrementTime --> LoopStart
    LoopStart -- No --> OutputOrbit(Output "Orbit!")
    OutputOrbit --> End
```
"""
import math

def orbit_game():
    """
    Моделирует запуск ракеты на орбиту вокруг планеты.
    """
    planetRadius = 20 # Радиус планеты
    gravity = 9.8 # Ускорение свободного падения (для простоты)
    
    # Запрашиваем у игрока начальные параметры запуска ракеты
    launchAngleDegrees = float(input("Введите начальный угол запуска ракеты (в градусах): "))
    launchVelocity = float(input("Введите начальную скорость ракеты: "))

    # Переводим угол запуска из градусов в радианы
    launchAngleRad = math.radians(launchAngleDegrees)

    # Вычисляем начальные координаты ракеты
    rocketX = planetRadius * math.cos(launchAngleRad) # начальная координата X
    rocketY = planetRadius * math.sin(launchAngleRad) # начальная координата Y
    
    currentTime = 0 # начальное время полета
    timeStep = 0.1 # шаг времени (для моделирования движения)
    
    # Цикл моделирования полета ракеты
    while currentTime < 10:
        # Вычисляем новые координаты ракеты с учетом начальной скорости, угла и гравитации
        rocketX = planetRadius * math.cos(launchAngleRad) + launchVelocity * currentTime * math.cos(launchAngleRad)
        rocketY = planetRadius * math.sin(launchAngleRad) + launchVelocity * currentTime * math.sin(launchAngleRad) - 0.5 * gravity * currentTime**2
    
        # Вычисляем расстояние от ракеты до центра планеты
        rocketDistance = math.sqrt(rocketX**2 + rocketY**2)

        # Проверяем условия выхода на орбиту, падения на планету или улета в космос
        if rocketDistance > 25:
           print("Слишком высоко!")
           return #завершаем игру
        if rocketDistance < 19:
           print("Слишком низко!")
           return #завершаем игру

        currentTime += timeStep # увеличиваем время на шаг
    
    print("Орбита!") # если цикл завершен, значит ракета на орбите

# Запускаем игру
if __name__ == "__main__":
    orbit_game()
"""
Пояснения:
1.  `planetRadius`: Радиус планеты (задаем константой, так как в оригинале константа `20`).
2.  `gravity`:  Ускорение свободного падения (задано для упрощенной модели).
3.  `launchAngleDegrees`: Начальный угол запуска ракеты в градусах, вводится пользователем.
4.  `launchVelocity`:  Начальная скорость ракеты, вводится пользователем.
5.  `launchAngleRad`:  Начальный угол запуска ракеты в радианах (получаем путем преобразования `launchAngleDegrees`).
6.  `rocketX` и `rocketY`:  Координаты ракеты на плоскости. Рассчитываются на основе начального угла, скорости, времени и гравитации.
7.  `currentTime`:  Текущее время моделирования. Используется для расчета положения ракеты в каждый момент времени.
8.  `timeStep`:  Шаг времени, на который увеличивается `currentTime` в каждой итерации цикла.
9.  `rocketDistance`: Расстояние ракеты до центра планеты.
10. `math.cos()` и `math.sin()`:  Косинус и синус угла для вычисления координат ракеты.
11. `math.radians()`: Переводит угол из градусов в радианы.
12. `math.sqrt()`: Квадратный корень.
13. `while currentTime < 10:`: Цикл моделирования, который продолжается, пока время не достигнет 10.
14. Комментарии в коде описывают каждый шаг алгоритма и переменные.
15. Функция `orbit_game()` содержит основную логику игры,  запрос параметров, вычисления и вывод результатов.
16. `if __name__ == "__main__":` -  Этот блок кода запускает игру, если файл запущен напрямую.

licence:MIT(../licence)
"""
__author__ = 'hypo69 (hypo69@davidka.net)'
```