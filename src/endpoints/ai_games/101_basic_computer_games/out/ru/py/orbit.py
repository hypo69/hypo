"""
ORBIT:
=================
Сложность: 6
-----------------
Игра "ORBIT" - это космическая симуляция, где игрок пытается попасть ракетой на орбиту вокруг планеты. Игрок вводит начальную скорость и угол запуска, а программа рассчитывает траекторию. Цель — достичь устойчивой орбиты с минимальным количеством попыток.

Правила игры:
1. Игрок вводит начальную скорость ракеты в диапазоне от 1000 до 11000 футов/сек.
2. Игрок вводит угол запуска ракеты в диапазоне от 10 до 80 градусов.
3. Программа рассчитывает высоту и расстояние ракеты на каждой итерации.
4. Игра заканчивается, если ракета возвращается на Землю (высота становится 0) или достигает стабильной орбиты (высота между 250 и 260 милями).
5. Выводятся результаты: количество попыток, конечная высота и расстояние.
-----------------
Алгоритм:
1. Инициализировать константы: гравитационная постоянная, радиус Земли,  высоту орбиты, и другие параметры.
2. Установить количество попыток в 0.
3. Начать цикл "пока игрок не выйдет или не достигнет орбиты":
  3.1. Увеличить количество попыток на 1.
  3.2. Запросить у игрока ввод начальной скорости в футах/сек (от 1000 до 11000)
  3.3. Запросить у игрока ввод угла запуска в градусах (от 10 до 80)
  3.4. Преобразовать угол запуска в радианы.
  3.5. Инициализировать начальное расстояние и высоту в 0.
  3.6. Инициализировать начальную горизонтальную и вертикальную скорость.
  3.7. Начать цикл симуляции (пока высота > 0 и высота в пределах орбиты).
     3.7.1 Рассчитать гравитацию, которая действует на ракету.
     3.7.2 Обновить вертикальную и горизонтальную скорость ракеты.
     3.7.3 Обновить высоту и расстояние ракеты.
     3.7.4 Вывести текущие высоту и расстояние ракеты.
  3.8. Проверить, достигла ли ракета стабильной орбиты.
  3.9. Вывести результаты (количество попыток, конечную высоту и расстояние).
4. Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeConstants["Инициализация констант: 
    <code><b>
    gravity = 32.2, earthRadius = 20925300, orbitAltitudeMin = 250 * 5280, orbitAltitudeMax = 260 * 5280
    </b></code>"]
    InitializeConstants --> InitializeVariables["Инициализация переменных: <code><b>numberOfAttempts = 0</b></code>"]
    InitializeVariables --> LoopStart{"Начало цикла: пока не вышли или не достигли орбиты"}
    LoopStart -- Да --> IncreaseAttempts["<code><b>numberOfAttempts = numberOfAttempts + 1</b></code>"]
    IncreaseAttempts --> InputVelocity["Ввод начальной скорости: <code><b>initialVelocity</b></code>"]
    InputVelocity --> InputAngle["Ввод угла запуска: <code><b>launchAngle</b></code>"]
    InputAngle --> CalculateInitialVelocity["<p align='left'>Расчет начальных скоростей:
    <code><b>
    initialAngleRadians = launchAngle * PI / 180
    horizontalVelocity = initialVelocity * cos(initialAngleRadians)
    verticalVelocity = initialVelocity * sin(initialAngleRadians)
    </b></code></p>"]
    CalculateInitialVelocity --> InitializeTrajectory["Инициализация траектории: <code><b>distance = 0, altitude = 0</b></code>"]
    InitializeTrajectory --> SimulationLoopStart{"Начало цикла симуляции: пока высота > 0 и не достигнута орбита"}
    SimulationLoopStart -- Да --> CalculateGravity["Расчет гравитации: <code><b>currentGravity = gravity * (earthRadius / (earthRadius + altitude))^2</b></code>"]
    CalculateGravity --> UpdateVelocity["<p align='left'>Обновление скоростей:
    <code><b>
    verticalVelocity = verticalVelocity - currentGravity * 2
    </b></code></p>"]
    UpdateVelocity --> UpdatePosition["<p align='left'>Обновление позиции:
    <code><b>
    distance = distance + horizontalVelocity * 2
    altitude = altitude + verticalVelocity * 2
    </b></code></p>"]
    UpdatePosition --> OutputCurrentStatus["Вывод текущей высоты и расстояния: <code><b>altitude, distance</b></code>"]
    OutputCurrentStatus --> CheckAltitude{"Проверка высоты: <code><b>altitude <= 0</b></code>"}
    CheckAltitude -- Да --> OutputCrashed["Вывод сообщения: <b>Ракета упала</b>"]
    OutputCrashed --> SimulationLoopEnd
    CheckAltitude -- Нет --> CheckOrbit{"Проверка на стабильную орбиту: <code><b>orbitAltitudeMin <= altitude <= orbitAltitudeMax</b></code>"}
     CheckOrbit -- Да --> OutputOrbitReached["Вывод сообщения: <b>Достигнута стабильная орбита</b>"]
    OutputOrbitReached --> SimulationLoopEnd
    CheckOrbit -- Нет --> SimulationLoopStart
    SimulationLoopStart -- Нет --> SimulationLoopEnd
    SimulationLoopEnd --> CheckContinue{"Проверка: <b>Повторить?</b>"}
    CheckContinue -- Да --> LoopStart
    CheckContinue -- Нет --> OutputResults["Вывод результатов: <b>количество попыток, конечная высота и расстояние</b>"]
    OutputResults --> End["Конец"]
    LoopStart -- Нет --> OutputResults
```
Legenda:
    Start - Начало программы.
    InitializeConstants - Инициализация констант: gravity (гравитационная постоянная), earthRadius (радиус Земли), orbitAltitudeMin (минимальная высота орбиты), orbitAltitudeMax (максимальная высота орбиты).
    InitializeVariables - Инициализация переменной numberOfAttempts (количество попыток) в 0.
    LoopStart - Начало цикла, который продолжается, пока игрок не выйдет или не достигнет орбиты.
    IncreaseAttempts - Увеличение счетчика количества попыток на 1.
    InputVelocity - Запрос у пользователя ввода начальной скорости ракеты.
    InputAngle - Запрос у пользователя ввода угла запуска ракеты.
    CalculateInitialVelocity - Вычисление начальных горизонтальной и вертикальной скоростей ракеты.
    InitializeTrajectory - Инициализация начального расстояния и высоты в 0.
    SimulationLoopStart - Начало цикла симуляции, который продолжается, пока высота > 0 и не достигнута орбита.
    CalculateGravity - Расчет текущей гравитации, воздействующей на ракету.
    UpdateVelocity - Обновление вертикальной скорости ракеты с учетом гравитации.
    UpdatePosition - Обновление высоты и расстояния ракеты.
    OutputCurrentStatus - Вывод текущих высоты и расстояния.
    CheckAltitude - Проверка, не упала ли ракета (высота <= 0).
    OutputCrashed - Вывод сообщения о том, что ракета упала.
    CheckOrbit - Проверка, достигла ли ракета стабильной орбиты.
    OutputOrbitReached - Вывод сообщения о том, что ракета достигла стабильной орбиты.
    SimulationLoopEnd - Завершение цикла симуляции.
    CheckContinue - Запрос на повторение игры.
    OutputResults - Вывод конечных результатов: количество попыток, конечная высота и расстояние.
    End - Конец программы.
"""
import math

__author__ = 'hypo69 (hypo69@davidka.net)'


# Константы
GRAVITY = 32.2  # Гравитационная постоянная (футы/сек^2)
EARTH_RADIUS = 20925300  # Радиус Земли в футах
ORBIT_ALTITUDE_MIN = 250 * 5280  # Минимальная высота орбиты в футах
ORBIT_ALTITUDE_MAX = 260 * 5280  # Максимальная высота орбиты в футах
PI = math.pi


def get_user_input(prompt, min_value, max_value):
    """
    Запрашивает у пользователя ввод числа в заданном диапазоне.

    Args:
        prompt (str): Сообщение для пользователя.
        min_value (int): Минимальное допустимое значение.
        max_value (int): Максимальное допустимое значение.

    Returns:
        int: Введенное пользователем число.
    """
    while True:
        try:
            user_input = int(input(prompt))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(
                    f"Пожалуйста, введите число от {min_value} до {max_value}."
                )
        except ValueError:
            print("Ошибка ввода. Введите целое число.")


def calculate_trajectory(initial_velocity, launch_angle):
    """
    Рассчитывает траекторию ракеты.

    Args:
        initial_velocity (int): Начальная скорость ракеты в футах/сек.
        launch_angle (int): Угол запуска ракеты в градусах.

    Returns:
        tuple: Конечные высота и расстояние.
    """
    # Преобразуем угол запуска в радианы
    initial_angle_radians = math.radians(launch_angle)

    # Вычисляем начальные горизонтальную и вертикальную скорости
    horizontal_velocity = initial_velocity * math.cos(initial_angle_radians)
    vertical_velocity = initial_velocity * math.sin(initial_angle_radians)

    # Инициализируем начальное расстояние и высоту
    distance = 0
    altitude = 0

    # Цикл симуляции
    while altitude > 0 and not (
        ORBIT_ALTITUDE_MIN <= altitude <= ORBIT_ALTITUDE_MAX
    ):
        # Вычисляем текущую гравитацию
        current_gravity = GRAVITY * (EARTH_RADIUS / (EARTH_RADIUS + altitude)) ** 2

        # Обновляем вертикальную скорость
        vertical_velocity = vertical_velocity - current_gravity * 2

        # Обновляем горизонтальную и вертикальную позицию
        distance = distance + horizontal_velocity * 2
        altitude = altitude + vertical_velocity * 2

        # Выводим текущее положение
        print(f"Высота: {altitude:.0f} футов, Расстояние: {distance:.0f} футов")
    return altitude, distance


def play_orbit():
    """
    Основная функция игры "ORBIT".
    """
    number_of_attempts = 0

    while True:
        number_of_attempts += 1
        print(f"\nПопытка №{number_of_attempts}")
        # Запрашиваем начальную скорость ракеты
        initial_velocity = get_user_input(
            "Введите начальную скорость ракеты (1000-11000 футов/сек): ",
            1000,
            11000,
        )

        # Запрашиваем угол запуска ракеты
        launch_angle = get_user_input(
            "Введите угол запуска ракеты (10-80 градусов): ", 10, 80
        )

        # Рассчитываем траекторию и получаем конечные высоту и расстояние
        altitude, distance = calculate_trajectory(initial_velocity, launch_angle)

        # Проверяем, достигла ли ракета стабильной орбиты
        if ORBIT_ALTITUDE_MIN <= altitude <= ORBIT_ALTITUDE_MAX:
            print(f"Поздравляю, вы достигли стабильной орбиты!")
        elif altitude <= 0:
            print(f"Ракета упала на Землю.")
        else:
             print(f"Не удалось выйти на орбиту.")

        # Выводим результаты
        print(f"Количество попыток: {number_of_attempts}")
        print(f"Конечная высота: {altitude:.0f} футов")
        print(f"Конечное расстояние: {distance:.0f} футов")

        # Спрашиваем, хочет ли игрок сыграть еще раз
        play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
        if play_again != "да":
            break


if __name__ == "__main__":
    play_orbit()

"""
Пояснения:
1. **Импорт модуля `math`**:
   - `import math`: Импортирует модуль `math`, который используется для математических вычислений, таких как `cos`, `sin` и `radians`.

2. **Константы**:
   - `GRAVITY = 32.2`: Гравитационная постоянная (футы/сек^2).
   - `EARTH_RADIUS = 20925300`: Радиус Земли в футах.
   - `ORBIT_ALTITUDE_MIN = 250 * 5280`: Минимальная высота орбиты в футах.
   - `ORBIT_ALTITUDE_MAX = 260 * 5280`: Максимальная высота орбиты в футах.
   - `PI = math.pi`: Математическая константа Пи.

3. **Функция `get_user_input(prompt, min_value, max_value)`**:
   - Запрашивает у пользователя ввод числа в заданном диапазоне.
   - `prompt`: Сообщение для пользователя.
   - `min_value`: Минимальное допустимое значение.
   - `max_value`: Максимальное допустимое значение.
   - Возвращает введенное пользователем число.
   - Использует цикл `while True` для повторения ввода, пока не будет введено корректное значение.

4. **Функция `calculate_trajectory(initial_velocity, launch_angle)`**:
   - Рассчитывает траекторию ракеты.
   - `initial_velocity`: Начальная скорость ракеты в футах/сек.
   - `launch_angle`: Угол запуска ракеты в градусах.
   - Возвращает конечные высоту и расстояние.
   - Преобразует угол запуска в радианы.
   - Вычисляет начальные горизонтальную и вертикальную скорости.
   - Инициализирует начальное расстояние и высоту.
   - Цикл симуляции, пока ракета не упадет или не достигнет стабильной орбиты.
   - Вычисляет текущую гравитацию.
   - Обновляет вертикальную скорость.
   - Обновляет горизонтальную и вертикальную позицию.
   - Выводит текущее положение.

5. **Функция `play_orbit()`**:
   - Основная функция игры "ORBIT".
   - `number_of_attempts = 0`: Инициализация количества попыток.
   - `while True`: Основной цикл игры.
   - Запрашивает у пользователя начальную скорость и угол запуска.
   - Вызывает функцию `calculate_trajectory` для расчета траектории.
   - Проверяет, достигла ли ракета стабильной орбиты или упала.
   - Выводит результаты.
   - Спрашивает, хочет ли игрок сыграть еще раз.

6. **Запуск игры**:
   - `if __name__ == "__main__":`: Этот блок гарантирует, что функция `play_orbit()` будет запущена, только если файл исполняется напрямую, а не импортируется как модуль.
   - `play_orbit()`: Вызывает функцию для начала игры.
"""
