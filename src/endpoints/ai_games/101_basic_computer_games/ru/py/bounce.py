"""
BOUNCE:
=================
Сложность: 4
-----------------
Игра "BOUNCE" - это простая графическая игра, в которой шарик отскакивает от стенок. Игрок управляет полоской внизу экрана, отбивая шарик, чтобы он не упал вниз. Игрок получает одно очко за каждый отскок шарика от полоски.

Правила игры:
1. Шарик постоянно движется по экрану, отскакивая от стенок.
2. Полоска внизу экрана управляется игроком, перемещаясь влево или вправо.
3. Игрок должен отбивать шарик полоской, не давая ему упасть за нижний край экрана.
4. За каждый отскок шарика от полоски игрок получает одно очко.
5. Игра заканчивается, если шарик упадёт вниз.
-----------------
Алгоритм:
1.  Инициализация:
    1.1 Установить координаты шарика `X`, `Y` и начальные направления движения `DX`, `DY`.
    1.2 Установить координаты полоски `P`.
    1.3 Установить начальное значение очков `S` в 0.
2.  Основной цикл игры (пока игра не закончится):
    2.1 Отрисовать экран:
        2.1.1 Очистить экран.
        2.1.2 Отрисовать шарик в позиции `(X, Y)`.
        2.1.3 Отрисовать полоску в позиции `P`.
    2.2 Проверить ввод пользователя:
        2.2.1 Если нажата клавиша влево, уменьшить `P`.
        2.2.2 Если нажата клавиша вправо, увеличить `P`.
    2.3 Изменить позицию шарика:
        2.3.1  `X = X + DX`.
        2.3.2  `Y = Y + DY`.
    2.4 Проверить отскок от стенок:
        2.4.1  Если `X` достиг левой или правой границы экрана, изменить направление `DX = -DX`.
        2.4.2  Если `Y` достиг верхней границы экрана, изменить направление `DY = -DY`.
    2.5 Проверить отскок от полоски:
        2.5.1 Если `Y` достиг уровня полоски и `X` находится в пределах полоски, изменить направление `DY = -DY` и увеличить очки `S` на 1.
    2.6 Проверить падение шарика:
        2.6.1 Если `Y` достиг нижней границы экрана, игра заканчивается.
3.  Конец игры:
    3.1 Вывести сообщение о конце игры и количество набранных очков.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация переменных:<br>
    <code>ballX = 10, ballY = 5, ballDirectionX = 1, ballDirectionY = 1, paddlePosition = 20, score = 0</code></p>"]
    InitializeVariables --> GameLoopStart{"Начало игрового цикла"}
    GameLoopStart --> DrawScreen["Отрисовка экрана: очистка, отрисовка шарика и полоски"]
    DrawScreen --> InputCheck["Проверка ввода пользователя"]
    InputCheck --> MovePaddle{"Перемещение полоски влево/вправо по вводу пользователя"}
    MovePaddle --> MoveBall["Перемещение шарика:<br><code>ballX = ballX + ballDirectionX<br>ballY = ballY + ballDirectionY</code>"]
    MoveBall --> CheckWallBounce{"Проверка отскока от стен"}
    CheckWallBounce -- Да --> ReverseBallXDirection["Инвертировать направление шарика по оси X:<br><code>ballDirectionX = -ballDirectionX</code>"]
    ReverseBallXDirection --> CheckCeilingBounce["Проверка отскока от верхней границы"]
    CheckWallBounce -- Нет --> CheckCeilingBounce
    CheckCeilingBounce -- Да --> ReverseBallYDirection["Инвертировать направление шарика по оси Y:<br><code>ballDirectionY = -ballDirectionY</code>"]
    ReverseBallYDirection --> CheckPaddleBounce["Проверка отскока от полоски"]
    CheckCeilingBounce -- Нет --> CheckPaddleBounce
    CheckPaddleBounce -- Да --> IncreaseScore["Увеличить счет на 1:<br><code>score = score + 1</code>"]
    IncreaseScore --> ReverseBallYDirection2["Инвертировать направление шарика по оси Y:<br><code>ballDirectionY = -ballDirectionY</code>"]
    ReverseBallYDirection2 --> CheckBallFell["Проверка падения шарика"]
    CheckPaddleBounce -- Нет --> CheckBallFell
    CheckBallFell -- Нет --> GameLoopStart
    CheckBallFell -- Да --> OutputEndGame["Вывод сообщения о конце игры и набранных очках"]
    OutputEndGame --> End["Конец"]
```
Legenda:
    Start - Начало программы.
    InitializeVariables - Инициализация начальных значений переменных, таких как положение шарика, направление движения, положение полоски и счет.
    GameLoopStart - Начало цикла игры, который продолжается, пока игра не закончится.
    DrawScreen - Отрисовка экрана, включающая очистку экрана и отрисовку шарика и полоски.
    InputCheck - Проверка ввода пользователя для перемещения полоски.
    MovePaddle - Перемещение полоски влево или вправо в зависимости от ввода пользователя.
    MoveBall - Обновление координат шарика на основе его направления движения.
    CheckWallBounce - Проверка столкновения шарика с левой или правой стеной.
    ReverseBallXDirection - Изменение направления шарика по горизонтали на противоположное.
    CheckCeilingBounce - Проверка столкновения шарика с верхней границей экрана.
    ReverseBallYDirection - Изменение направления шарика по вертикали на противоположное.
    CheckPaddleBounce - Проверка отскока шарика от полоски.
    IncreaseScore - Увеличение счета на 1 за отскок от полоски.
    ReverseBallYDirection2 - Инвертирование направления шарика после отскока от полоски.
    CheckBallFell - Проверка, не упал ли шарик за нижнюю границу экрана.
    OutputEndGame - Вывод сообщения о конце игры и набранных очках.
    End - Конец программы.
"""
import time
import os

# Инициализация начальных параметров
ballX = 10  # Начальная X-координата шарика
ballY = 5   # Начальная Y-координата шарика
ballDirectionX = 1  # Направление движения шарика по оси X (1 - вправо, -1 - влево)
ballDirectionY = 1  # Направление движения шарика по оси Y (1 - вниз, -1 - вверх)
paddlePosition = 20 # Начальная позиция полоски
score = 0 # Инициализация счета

# Размеры игрового поля
WIDTH = 40
HEIGHT = 20
PADDLE_LENGTH = 6  # Длина полоски


def clear_screen():
    """Очистка экрана."""
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_screen():
    """Отрисовка игрового экрана."""
    clear_screen()
    # Создаем пустой экран
    screen = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

    # Отрисовка шарика
    screen[ballY][ballX] = 'O'

    # Отрисовка полоски
    for i in range(paddlePosition, paddlePosition + PADDLE_LENGTH):
        if 0 <= i < WIDTH:
            screen[HEIGHT - 1][i] = '='
    
    # Вывод счета
    print(f"Score: {score}")
    
    # Вывод экрана
    for row in screen:
        print(''.join(row))

def check_input():
    """Проверка ввода пользователя и перемещение полоски."""
    import sys, select
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        key = sys.stdin.read(1)
        global paddlePosition
        if key == 'a' and paddlePosition > 0:
            paddlePosition -= 1
        elif key == 'd' and paddlePosition + PADDLE_LENGTH < WIDTH:
            paddlePosition += 1

def move_ball():
    """Перемещение шарика."""
    global ballX, ballY
    ballX += ballDirectionX
    ballY += ballDirectionY

def check_wall_bounce():
    """Проверка отскока от стенок."""
    global ballDirectionX, ballDirectionY
    if ballX <= 0 or ballX >= WIDTH - 1:
        ballDirectionX *= -1
    if ballY <= 0:
        ballDirectionY *= -1

def check_paddle_bounce():
    """Проверка отскока от полоски."""
    global ballDirectionY, score
    if ballY == HEIGHT - 1 and paddlePosition <= ballX < paddlePosition + PADDLE_LENGTH:
            ballDirectionY *= -1
            score += 1

def check_ball_fell():
    """Проверка падения шарика."""
    return ballY >= HEIGHT


# Основной игровой цикл
while True:
    draw_screen()
    check_input()
    move_ball()
    check_wall_bounce()
    check_paddle_bounce()

    if check_ball_fell():
        print("Game Over!")
        print(f"Final Score: {score}")
        break

    time.sleep(0.1) # Задержка для более плавной анимации
"""
Объяснение кода:
1.  **Импорт модулей**:
    -   `import time`: Модуль `time` используется для создания задержки в игровом цикле, чтобы анимация не была слишком быстрой.
    -   `import os`: Модуль `os` используется для очистки экрана в консоли.
2.  **Инициализация начальных параметров**:
    -   `ballX`, `ballY`: Начальные координаты шарика по осям X и Y.
    -   `ballDirectionX`, `ballDirectionY`: Направления движения шарика по осям X и Y (1 - вправо/вниз, -1 - влево/вверх).
    -   `paddlePosition`: Начальная позиция полоски.
    -   `score`: Начальное значение счета.
    -   `WIDTH`, `HEIGHT`: Размеры игрового поля.
    -   `PADDLE_LENGTH`: Длина полоски.
3.  **Функция `clear_screen()`**:
    -   Очищает экран консоли с помощью `os.system('cls' if os.name == 'nt' else 'clear')`.
4.  **Функция `draw_screen()`**:
    -   Очищает экран с помощью `clear_screen()`.
    -   Создаёт двумерный список `screen`, представляющий игровое поле.
    -   Отрисовывает шарик `'O'` на экране в позиции `(ballX, ballY)`.
    -   Отрисовывает полоску `'='` на последней строке экрана в позиции `paddlePosition` до `paddlePosition + PADDLE_LENGTH`.
    -   Выводит текущий счет на экран.
    -   Выводит экран в консоль.
5.  **Функция `check_input()`**:
    -   Проверяет, был ли ввод пользователя, и обрабатывает его.
    -   Если пользователь нажал `a`, полоска сдвигается влево (если это возможно).
    -   Если пользователь нажал `d`, полоска сдвигается вправо (если это возможно).
    -   Использует `sys`, `select` для неблокирующего ввода.
6.  **Функция `move_ball()`**:
    -   Изменяет координаты шарика в зависимости от текущих направлений `ballDirectionX` и `ballDirectionY`.
7.  **Функция `check_wall_bounce()`**:
    -   Проверяет, столкнулся ли шарик с левой или правой стеной (границей экрана) и изменяет направление `ballDirectionX` на противоположное, если это произошло.
    -   Проверяет, столкнулся ли шарик с верхней границей экрана и изменяет направление `ballDirectionY` на противоположное, если это произошло.
8.  **Функция `check_paddle_bounce()`**:
    -   Проверяет, столкнулся ли шарик с полоской.
    -   Если это произошло, изменяет направление шарика `ballDirectionY` на противоположное и увеличивает счет на 1.
9.  **Функция `check_ball_fell()`**:
    -   Проверяет, не упал ли шарик за нижнюю границу экрана (ниже полоски) и возвращает `True`, если это произошло.
10. **Основной игровой цикл `while True`**:
    -   Отрисовывает экран с помощью `draw_screen()`.
    -   Проверяет ввод пользователя с помощью `check_input()`.
    -   Перемещает шарик с помощью `move_ball()`.
    -   Проверяет отскок шарика от стенок и полоски с помощью `check_wall_bounce()` и `check_paddle_bounce()`.
    -   Проверяет, не упал ли шарик за нижнюю границу экрана с помощью `check_ball_fell()`.
    -   Если шарик упал, выводит сообщение "Game Over!" и финальный счет, затем завершает цикл.
    -   Создает задержку 0.1 секунды с помощью `time.sleep(0.1)`, чтобы игра не была слишком быстрой.
"""
