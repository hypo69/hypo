# Анализ кода модуля splat.py

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и логически понятен.
    - Используются функции для разделения задач (например, `calculate_distance`).
    - Присутствуют проверки на ввод данных пользователем.
    - Есть документация к модулю и функциям на иврите.
    - Логика игры соответствует описанию в начале файла.
- Минусы
    - Отсутствует логирование ошибок, что затрудняет отладку.
    - Документация на иврите не соответствует стандарту reStructuredText (RST).
    - Присутствуют блоки try-except, которые можно оптимизировать, используя логирование.
    - Комментарии в коде не соответствуют стандарту reStructuredText.
    - Нет импорта модуля `src.logger.logger`.

**Рекомендации по улучшению**
1. **Документация**: Переписать всю документацию в формате reStructuredText (RST), включая docstring функций и комментарии.
2. **Логирование**:  Использовать `from src.logger.logger import logger` для логирования ошибок, заменив `print` для ошибок ввода.
3. **Обработка ошибок**:  Избегать избыточного использования `try-except`, применяя `logger.error` для отслеживания исключений.
4. **Комментарии**: Переписать все комментарии после `#` в соответствии с инструкцией, объясняя, что делает каждая строка кода.
5. **Импорты**: Добавить недостающие импорты, если они есть.
6. **Улучшение читаемости**: Привести код в соответствие с pep8.
7. **Избегать магических чисел**: Заменить магические числа (например, 10, 100, 9.81) константами с описанием.

**Оптимизированный код**
```python
"""
SPLAT:
=================
קושי: 4
-----------------
Игра "SPLAT" - это игра на удачу, в которой пользователь пытается сбить самолет из пушки.
Пользователь вводит угол и скорость выстрела, а игра имитирует траекторию снаряда.
Если снаряд попадает в самолет, пользователь выигрывает. В противном случае самолет улетает.

Правила игры:
1. Пользователь вводит угол и скорость выстрела.
2. Игра рассчитывает траекторию снаряда и имитирует попадание в самолет.
3. Если снаряд попадает в самолет, игра заканчивается победой.
4. Если снаряд не попадает, самолет перемещается вправо.
5. Игра продолжается до тех пор, пока пользователь не попадет в самолет или пока самолет не достигнет края экрана.
-----------------
Алгоритм:
1. Инициализирует позицию самолета в 20.
2. Устанавливает статус игры в "играем".
3. Начинает цикл "пока играем":
    3.1 Запрашивает у пользователя угол (между 0 и 90 градусами) и начальную скорость (между 0 и 90).
    3.2 Вычисляет расстояние, которое пролетел снаряд.
    3.3 Если расстояние близко к позиции самолета, показывает сообщение о победе и заканчивает игру.
    3.4 В противном случае, если самолет не достиг края экрана, перемещает самолет на 10 вправо.
    3.5 Если самолет достиг края экрана, показывает сообщение о проигрыше и заканчивает игру.
4. Конец игры.
-----------------
Диаграмма потока:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация переменных:\n    <code><b>\n    planePosition = 20\n    gameStatus = 'playing'\n    </b></code></p>"]
    InitializeVariables --> LoopStart{"Начало цикла: <code><b>gameStatus == 'playing'</b></code>"}\n
    LoopStart -- Да --> InputAngleVelocity["<p align='left'>Ввод угла и скорости:\n    <code><b>\n    angle\n    velocity\n    </b></code></p>"]\n
    InputAngleVelocity --> CalculateDistance["Расчет расстояния снаряда: <code><b>distance</b></code>"]
    CalculateDistance --> CheckHit{"Проверка: <code><b>distance</b></code> близко к <code><b>planePosition</b></code>?"}
    CheckHit -- Да --> OutputWin["Вывод сообщения: <b>SPLAT!!! YOU GOT IT!</b>"]
    OutputWin --> GameEnd["Конец: <code><b>gameStatus = 'end'</b></code>"]
    CheckHit -- Нет --> CheckPlanePosition{"Проверка: <code><b>planePosition</b></code> < 100?"}
    CheckPlanePosition -- Да --> MovePlane["Перемещение самолета: <code><b>planePosition = planePosition + 10</b></code>"]
    MovePlane --> LoopStart
    CheckPlanePosition -- Нет --> OutputLose["Вывод сообщения: <b>YOU MISSED, PLANE FLEW AWAY</b>"]
    OutputLose --> GameEnd
    LoopStart -- Нет --> End["Конец"]
    GameEnd --> End
```
Легенда:
    Start - Начало программы.
    InitializeVariables - Инициализация переменных: planePosition (позиция самолета) устанавливается в 20, а gameStatus (статус игры) устанавливается в "playing".
    LoopStart - Начало цикла, который продолжается, пока gameStatus равен "playing".
    InputAngleVelocity - Получение от пользователя ввода угла и скорости выстрела.
    CalculateDistance - Вычисление расстояния, которое пролетел снаряд, на основе угла и скорости.
    CheckHit - Проверка, попал ли снаряд в самолет (расстояние, которое пролетел снаряд, близко к позиции самолета).
    OutputWin - Вывод сообщения о победе, если снаряд попал в самолет.
    GameEnd - Окончание игры и изменение gameStatus на "end".
    CheckPlanePosition - Проверка, находится ли самолет еще на экране (его позиция меньше 100).
    MovePlane - Перемещение самолета вправо на 10 единиц, если он еще на экране.
    OutputLose - Вывод сообщения о проигрыше, если самолет достиг края экрана.
    End - Конец программы.
"""
import math
from src.logger.logger import logger

# Константы
PLANE_START_POSITION = 20
PLANE_MOVE_STEP = 10
PLANE_MAX_POSITION = 100
HIT_THRESHOLD = 10
GRAVITY = 9.81

def calculate_distance(angle: float, velocity: float) -> float:
    """
    Вычисляет расстояние, которое пролетает снаряд, на основе угла и начальной скорости.

    :param angle: Угол выстрела в градусах.
    :param velocity: Начальная скорость снаряда.
    :return: Расстояние, которое пролетел снаряд.
    """
    # Преобразование угла из градусов в радианы.
    angle_rad = math.radians(angle)
    # Вычисление горизонтального расстояния, которое пролетел снаряд.
    distance = (velocity ** 2 * math.sin(2 * angle_rad)) / GRAVITY
    return distance

# Инициализация позиции самолета.
plane_position = PLANE_START_POSITION
# Инициализация статуса игры.
game_status = 'playing'

# Основной игровой цикл.
while game_status == 'playing':
    # Получение ввода от пользователя.
    try:
        angle = float(input("Введите угол (0-90): "))
        velocity = float(input("Введите скорость (0-90): "))
        # Проверка, что угол и скорость находятся в допустимых пределах.
        if not (0 <= angle <= 90) or not (0 <= velocity <= 90):
           print("Угол и скорость должны быть между 0 и 90. Попробуйте еще раз.")
           continue
    except ValueError as e:
        # Логирование ошибки при некорректном вводе.
        logger.error(f"Некорректный ввод данных: {e}")
        print("Некорректный ввод, пожалуйста, введите числа.")
        continue

    # Вычисление расстояния, которое пролетел снаряд.
    distance = calculate_distance(angle, velocity)

    # Проверка, попал ли снаряд в самолет.
    if abs(distance - plane_position) < HIT_THRESHOLD:  # Пороговое значение попадания.
        print("SPLAT!!! ВЫ ПОПАЛИ!")
        game_status = 'end' # Завершение игры.
    else:
        # Проверка, не достиг ли самолет края экрана.
        if plane_position < PLANE_MAX_POSITION:
            plane_position += PLANE_MOVE_STEP # Перемещение самолета вправо.
        else:
             print("ВЫ ПРОМАХНУЛИСЬ, САМОЛЕТ УЛЕТЕЛ")
             game_status = 'end' # Завершение игры.


"""
Объяснение кода:
1. **Импорт модуля `math`**:
    - `import math`: Импортирует модуль `math`, который используется для математических операций, таких как преобразование градусов в радианы.
    - `from src.logger.logger import logger`: Импортирует модуль `logger` для логирования ошибок.

2. **Константы**:
    - `PLANE_START_POSITION = 20`:  Начальная позиция самолета.
    - `PLANE_MOVE_STEP = 10`:  Шаг смещения самолета.
    - `PLANE_MAX_POSITION = 100`:  Максимальная позиция самолета на экране.
    - `HIT_THRESHOLD = 10`:  Порог для определения попадания.
    - `GRAVITY = 9.81`: Ускорение свободного падения.

3. **Функция `calculate_distance(angle, velocity)`**:
    - Функция вычисляет расстояние, пройденное снарядом, на основе угла и начальной скорости.
    - `angle_rad = math.radians(angle)`: Преобразует угол из градусов в радианы.
    - `distance = (velocity ** 2 * math.sin(2 * angle_rad)) / GRAVITY`: Вычисляет расстояние, пройденное снарядом, используя физическую формулу.
    - Функция возвращает вычисленное расстояние.

4. **Инициализация переменных**:
    - `plane_position = PLANE_START_POSITION`: Инициализирует позицию самолета значением `PLANE_START_POSITION`.
    - `game_status = 'playing'`: Инициализирует статус игры значением `playing`, указывающим на то, что игра продолжается.

5. **Основной игровой цикл `while game_status == 'playing':`**:
    - Цикл продолжается, пока переменная `game_status` равна `'playing'`.
    - **Ввод данных**:
        - `try...except ValueError as e:`: Обрабатывает возможные ошибки ввода данных.
        - `angle = float(input("Введите угол (0-90): "))` и `velocity = float(input("Введите скорость (0-90): "))`: Запрашивает у пользователя ввод угла и скорости и преобразует их в числа с плавающей точкой.
        - `if not (0 <= angle <= 90) or not (0 <= velocity <= 90):`: Проверяет, что введенные угол и скорость находятся в допустимом диапазоне.
        - `continue`: Если ввод недействителен, то переходит к началу цикла.
        - `logger.error(f"Некорректный ввод данных: {e}")`: Если ввод недействителен, то ошибка логируется в журнал.

    - **Вычисление расстояния**:
        - `distance = calculate_distance(angle, velocity)`: Вызывает функцию `calculate_distance` для вычисления расстояния, пройденного снарядом.

    - **Проверка попадания**:
        - `if abs(distance - plane_position) < HIT_THRESHOLD:`: Проверяет, находится ли расстояние, пройденное снарядом, в пределах `HIT_THRESHOLD` от позиции самолета.
        - `print("SPLAT!!! ВЫ ПОПАЛИ!")`: Если снаряд попал в самолет, выводится сообщение о победе.
        - `game_status = 'end'`: Устанавливает статус игры на `end`, завершая игровой цикл.

    - **Перемещение самолета**:
        - `else:`: Если снаряд не попал в самолет.
        - `if plane_position < PLANE_MAX_POSITION:`: Проверяет, находится ли самолет еще в пределах экрана.
            - `plane_position += PLANE_MOVE_STEP`: Перемещает самолет вправо на `PLANE_MOVE_STEP`.
        - `else:`: Если самолет достиг края экрана.
            - `print("ВЫ ПРОМАХНУЛИСЬ, САМОЛЕТ УЛЕТЕЛ")`: Выводит сообщение о проигрыше.
            - `game_status = 'end'`: Устанавливает статус игры на `end`, завершая игровой цикл.
"""