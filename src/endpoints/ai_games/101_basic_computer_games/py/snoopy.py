"""
SNOOPY:
=================
Сложность: 3
-----------------
Игра SNOOPY - это игра-симулятор, в которой игрок управляет Снупи, который пытается сбить красные точки, стреляя вверх, 
и избегает сбивания черных точек. Цель игры - сбить как можно больше красных точек, избегая черных.
Игра продолжается, пока Снупи не сбит.
-----------------
Правила игры:
1.  Снупи (символ "^") располагается в нижней части экрана.
2.  Красные точки (символ "*") появляются в верхней части экрана и движутся вниз.
3.  Черные точки (символ "+") также появляются и движутся вниз.
4.  Игрок может перемещать Снупи влево (клавиша "A") и вправо (клавиша "D").
5.  При столкновении Снупи с красной точкой, она исчезает, и игрок получает 1 очко.
6.  При столкновении Снупи с черной точкой, игра заканчивается.
7. Цель игры: получить максимальное количество очков до того, как Снупи будет сбит.
-----------------
Алгоритм:
1.  Установить начальное положение Снупи в середине экрана.
2.  Установить начальный счет в 0.
3.  Начать игровой цикл:
    3.1 Обновить положение Снупи, если была нажата клавиша (влево/вправо).
    3.2  Сгенерировать случайное появление красных и черных точек.
    3.3  Отобразить Снупи, красные точки и черные точки на экране.
    3.4  Проверить столкновения:
        3.4.1 Если Снупи сталкивается с красной точкой, увеличить счет на 1 и удалить точку.
        3.4.2 Если Снупи сталкивается с черной точкой, закончить игру.
    3.5  Передвинуть все точки вниз.
    3.6  Удалить точки, вышедшие за нижний край экрана.
4.  Вывести сообщение "YOU GOT {счет} POINTS".
5. Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация переменных:
    <code><b>
    snoopyPosition =  screen_width / 2
    score = 0
    redPoints = []
    blackPoints = []
    </b></code></p>"]
    InitializeVariables --> LoopStart{"Начало игрового цикла"}
    LoopStart --> InputMovement["Ввод действия игрока (A/D)"]
    InputMovement --> UpdateSnoopyPosition["Обновить позицию Снупи"]
    UpdateSnoopyPosition --> GeneratePoints["Сгенерировать красные и черные точки"]
    GeneratePoints --> DisplayScreen["Отобразить Снупи, точки и счет"]
    DisplayScreen --> CheckCollisions{"Проверка столкновений"}
    CheckCollisions -- Столкновение с красной точкой --> IncreaseScore["<code><b>score = score + 1</b></code>"]
    IncreaseScore --> RemoveRedPoint["Удалить красную точку"]
     RemoveRedPoint --> MovePoints["Сдвинуть точки вниз"]
    CheckCollisions -- Столкновение с черной точкой --> GameOver["Конец игры"]
        GameOver --> OutputScore["Вывести счет игрока"]
         OutputScore --> End["Конец"]
    CheckCollisions -- Нет столкновений --> MovePoints
    MovePoints --> RemoveOffScreenPoints["Удалить точки, вышедшие за экран"]
    RemoveOffScreenPoints --> LoopStart
    LoopStart -- Конец игры --> End
```

Legenda:
    Start - Начало программы.
    InitializeVariables - Инициализация начальных переменных: snoopyPosition (начальная позиция Снупи), score (счет игрока), redPoints (список красных точек), blackPoints (список черных точек).
    LoopStart - Начало игрового цикла.
    InputMovement - Ожидание ввода от пользователя (A или D) для перемещения Снупи.
    UpdateSnoopyPosition - Обновление позиции Снупи в зависимости от ввода пользователя.
    GeneratePoints - Генерация новых красных и черных точек на экране.
    DisplayScreen - Вывод на экран текущего состояния игры (Снупи, точки, счет).
    CheckCollisions - Проверка столкновений Снупи с красными и черными точками.
    IncreaseScore - Увеличение счета игрока при столкновении с красной точкой.
    RemoveRedPoint - Удаление красной точки, с которой столкнулся Снупи.
    MovePoints - Смещение всех точек вниз по экрану.
    GameOver - Завершение игры при столкновении с черной точкой.
    OutputScore - Вывод на экран итогового счета игрока.
    End - Конец программы.
    RemoveOffScreenPoints - Удаление точек, которые вышли за пределы экрана.
"""
import random
import os
import time

__author__ = 'hypo69 (hypo69@davidka.net)'
"""
Пояснения:
1.  Импорт необходимых модулей `random`, `os` и `time`
2.  Объявление констант
    - `SCREEN_WIDTH` - ширина экрана
    - `SCREEN_HEIGHT` - высота экрана
    - `SNOOPY_SYMBOL` - символ Снупи
    - `RED_POINT_SYMBOL` - символ красной точки
    - `BLACK_POINT_SYMBOL` - символ черной точки
    - `SNOOPY_SPEED` - скорость Снупи
    - `POINT_SPEED` - скорость точек
3.  Инициализация переменных
    -  `snoopy_position` - начальная позиция Снупи
    - `score` - счет игрока
    -  `red_points` - список красных точек
    -   `black_points` - список черных точек
4.   Функция `clear_screen()` очищает экран
5.   Функция `display_screen()` отображает текущее состояние игры
6.  Функция `generate_points()` создает новые красные и черные точки в случайных местах в верхней части экрана
7.  Функция `update_snoopy_position()` изменяет положение Снупи в зависимости от ввода пользователя
8.  Функция `move_points()` перемещает точки вниз
9.  Функция `check_collisions()` проверяет столкновения Снупи с точками
10. Функция `remove_off_screen_points()` удаляет точки, вышедшие за границы экрана
11. Основной игровой цикл
    -   выполняется пока игра не окончена
    -   принимает ввод от пользователя (A/D)
    -   генерирует точки
    -   отображает экран
    -   проверяет столкновения
    -   перемещает точки
    -   удаляет вышедшие точки
12. Вывод результата и завершение игры
"""
SCREEN_WIDTH = 40
SCREEN_HEIGHT = 20
SNOOPY_SYMBOL = "^"
RED_POINT_SYMBOL = "*"
BLACK_POINT_SYMBOL = "+"
SNOOPY_SPEED = 2
POINT_SPEED = 1

def clear_screen():
    """Очищает экран."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_screen(snoopy_position, red_points, black_points, score):
    """Отображает текущее состояние игры."""
    clear_screen()
    screen = [[' ' for _ in range(SCREEN_WIDTH)] for _ in range(SCREEN_HEIGHT)]

    # Отображение точек
    for x, y in red_points:
        if 0 <= y < SCREEN_HEIGHT:
            screen[y][x] = RED_POINT_SYMBOL
    for x, y in black_points:
        if 0 <= y < SCREEN_HEIGHT:
            screen[y][x] = BLACK_POINT_SYMBOL

    # Отображение Снупи
    if 0 <= snoopy_position < SCREEN_WIDTH:
      screen[SCREEN_HEIGHT - 1][snoopy_position] = SNOOPY_SYMBOL

    # Вывод экрана
    for row in screen:
        print(''.join(row))
    print(f"Score: {score}")

def generate_points(red_points, black_points):
    """Генерирует новые красные и черные точки."""
    if random.randint(0, 4) == 0:  # Регулирует частоту появления точек
        x = random.randint(0, SCREEN_WIDTH - 1)
        red_points.append([x, 0])
    if random.randint(0, 5) == 0:  # Регулирует частоту появления точек
        x = random.randint(0, SCREEN_WIDTH - 1)
        black_points.append([x, 0])

def update_snoopy_position(snoopy_position, move):
    """Обновляет позицию Снупи."""
    if move == "a" and snoopy_position > 0:
        snoopy_position -= SNOOPY_SPEED
    elif move == "d" and snoopy_position < SCREEN_WIDTH - 1:
        snoopy_position += SNOOPY_SPEED
    return snoopy_position

def move_points(points):
    """Перемещает точки вниз."""
    for point in points:
        point[1] += POINT_SPEED

def check_collisions(snoopy_position, red_points, black_points):
    """Проверяет столкновения Снупи с точками."""
    global score
    snoopy_y = SCREEN_HEIGHT - 1
    
    red_points_to_remove = []
    for i, (x, y) in enumerate(red_points):
        if x == snoopy_position and y == snoopy_y:
            score += 1
            red_points_to_remove.append(i)
    
    # Удаление красных точек после обработки, чтобы не было проблем с итерацией списка
    for i in reversed(red_points_to_remove):
        del red_points[i]

    for x, y in black_points:
        if x == snoopy_position and y == snoopy_y:
            return True  # Столкновение с черной точкой, игра окончена
    return False

def remove_off_screen_points(points):
    """Удаляет точки, вышедшие за пределы экрана."""
    return [point for point in points if point[1] < SCREEN_HEIGHT]

# Инициализация игры
snoopy_position = SCREEN_WIDTH // 2
score = 0
red_points = []
black_points = []
game_over = False

# Основной игровой цикл
while not game_over:
    display_screen(snoopy_position, red_points, black_points, score)
    
    move = input("Enter A to move left, D to move right, or press Enter to do nothing: ").lower()
    
    snoopy_position = update_snoopy_position(snoopy_position, move)

    generate_points(red_points, black_points)
    
    move_points(red_points)
    move_points(black_points)

    game_over = check_collisions(snoopy_position, red_points, black_points)

    red_points = remove_off_screen_points(red_points)
    black_points = remove_off_screen_points(black_points)
    
    time.sleep(0.1)  # Задержка для регулировки скорости игры

# Конец игры
display_screen(snoopy_position, red_points, black_points, score)
print(f"YOU GOT {score} POINTS")

"""
Пояснения:
1.  **Импорт модулей**:
    -   `random`: Используется для генерации случайных чисел, таких как начальные положения точек.
    -   `os`: Используется для очистки экрана (`os.system('cls')` для Windows и `os.system('clear')` для других ОС).
    -   `time`: Используется для задержки (паузы) между кадрами игры.
2. **Константы**:
    - `SCREEN_WIDTH = 40`: Ширина игрового экрана в символах.
    - `SCREEN_HEIGHT = 20`: Высота игрового экрана в символах.
    - `SNOOPY_SYMBOL = "^"`: Символ, представляющий Снупи.
    - `RED_POINT_SYMBOL = "*"`: Символ, представляющий красную точку.
    - `BLACK_POINT_SYMBOL = "+"`: Символ, представляющий черную точку.
    - `SNOOPY_SPEED = 2`: Скорость перемещения Снупи за один шаг.
    - `POINT_SPEED = 1`: Скорость перемещения точек за один шаг.
3. **Функции**:
    - `clear_screen()`: Очищает экран консоли.
    - `display_screen(snoopy_position, red_points, black_points, score)`:
        - Создает и отображает текущее состояние игрового экрана, включая Снупи, красные точки, черные точки и счет.
        - Использует список списков `screen` для представления экрана, заполняет его пробелами и потом добавляет символы Снупи и точек.
        - Выводит на экран счет игрока
    - `generate_points(red_points, black_points)`:
        - Генерирует новые красные и черные точки случайным образом в верхней части экрана.
        - Частота появления точек контролируется с помощью `random.randint()`.
    - `update_snoopy_position(snoopy_position, move)`:
        - Обновляет позицию Снупи на основе ввода пользователя (`'a'` для влево, `'d'` для вправо).
        - Снупи не может выходить за границы экрана.
    - `move_points(points)`:
        - Перемещает каждую точку в списке `points` вниз на `POINT_SPEED`.
    - `check_collisions(snoopy_position, red_points, black_points)`:
        - Проверяет столкновения Снупи с красными и черными точками.
        - Если Снупи сталкивается с красной точкой, увеличивает счет и удаляет точку.
        - Если Снупи сталкивается с черной точкой, возвращает `True`, что означает конец игры.
    - `remove_off_screen_points(points)`:
        - Удаляет точки, которые вышли за пределы экрана, возвращая новый список.
4.  **Инициализация игры**:
    - `snoopy_position = SCREEN_WIDTH // 2`: Начальная позиция Снупи в середине экрана.
    - `score = 0`: Начальный счет игрока.
    - `red_points = []`: Список для хранения красных точек.
    - `black_points = []`: Список для хранения черных точек.
    - `game_over = False`: Флаг, указывающий, продолжается ли игра.
5. **Основной игровой цикл `while not game_over:`**:
    -   Цикл продолжается, пока `game_over` не станет `True`.
    -   `display_screen()`: Выводит текущее состояние игры.
    -  Запрашивает ввод у игрока `move = input(...)` и преобразует к нижнему регистру `.lower()`.
    -   `update_snoopy_position()`: Обновляет позицию Снупи в зависимости от ввода.
    -   `generate_points()`: Генерирует новые точки.
    -  `move_points()`: Перемещает точки вниз.
    -   `check_collisions()`: Проверяет столкновения и завершает игру, если происходит столкновение с черной точкой.
    -   `remove_off_screen_points()`: Удаляет точки, вышедшие за пределы экрана.
    -   `time.sleep(0.1)`: Пауза для регулировки скорости игры.
6. **Конец игры**:
    -  `display_screen()`: Выводит финальный экран.
    -   Выводит финальный счет игрока: `print(f"YOU GOT {score} POINTS")`.
"""
```