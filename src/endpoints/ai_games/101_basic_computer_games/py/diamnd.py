"""
DIAMND:
=================
Сложность: 5
-----------------
Игра "Бриллиант" - это игра, в которой игрок управляет движением точки по экрану, оставляя за собой след. Цель игры — нарисовать бриллиант. Игрок может изменять направление движения точки, вводя команды (1-влево, 2-вниз, 3-вправо, 4-вверх). Игра заканчивается, когда бриллиант сформирован (то есть 4 стороны бриллианта нарисованы).

Правила игры:
1. Игрок начинает с позиции в центре экрана.
2. Игрок вводит число от 1 до 4, определяющее направление движения:
    - 1: Влево
    - 2: Вниз
    - 3: Вправо
    - 4: Вверх
3. Точка движется в выбранном направлении, оставляя след.
4. Игра продолжается до тех пор, пока игрок не нарисует все 4 стороны бриллианта. (Количество ходов не ограничено.)
5. В конце игры выводится сообщение о завершении рисования бриллианта.
-----------------
Алгоритм:
1.  Инициализировать позицию точки в центре экрана и счетчик сторон бриллианта (diamondSides) в 0.
2.  Начать цикл "пока diamondSides < 4":
    2.1 Вывести текущее состояние экрана (позицию точки).
    2.2 Запросить у игрока ввод направления движения (1-4).
    2.3 В зависимости от введенного направления, обновить позицию точки.
    2.4 Проверить, образует ли след точки сторону бриллианта.
      2.4.1 Если след образует сторону бриллианта, увеличить счетчик diamondSides.
    2.5 Если diamondSides равен 4, то перейти к шагу 3.
3.  Вывести сообщение о завершении рисования бриллианта.
4.  Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация переменных:
    <code><b>
    xPosition = 20
    yPosition = 20
    diamondSides = 0
    </b></code></p>"]
    InitializeVariables --> LoopStart{"Начало цикла: пока <code><b>diamondSides < 4</b></code>"}
    LoopStart -- Да --> DisplayScreen["Отображение экрана: <code><b>точка в {xPosition}, {yPosition}</b></code>"]
    DisplayScreen --> InputDirection["Ввод направления движения (1-4): <code><b>direction</b></code>"]
    InputDirection --> UpdatePosition{"Обновление позиции: <code><b>xPosition, yPosition</b></code> в зависимости от <code><b>direction</b></code>"}
    UpdatePosition --> CheckDiamondSide{"Проверка: след точки образует сторону бриллианта?"}
    CheckDiamondSide -- Да --> IncreaseSides["<code><b>diamondSides = diamondSides + 1</b></code>"]
    IncreaseSides --> CheckSides{"Проверка: <code><b>diamondSides == 4</b></code>?"}
    CheckDiamondSide -- Нет --> CheckSides
    CheckSides -- Да --> OutputWin["Вывод сообщения: <b>DIAMOND COMPLETE!</b>"]
    OutputWin --> End["Конец"]
    CheckSides -- Нет --> LoopStart
    LoopStart -- Нет --> End

```
Legenda:
    Start - Начало программы.
    InitializeVariables - Инициализация переменных: xPosition и yPosition (позиция точки) устанавливаются в 20, а diamondSides (количество нарисованных сторон) устанавливается в 0.
    LoopStart - Начало цикла, который продолжается, пока не будет нарисовано 4 стороны бриллианта (diamondSides < 4).
    DisplayScreen - Отображение текущей позиции точки на экране.
    InputDirection - Запрос у пользователя ввода направления движения (1-4).
    UpdatePosition - Обновление позиции точки в зависимости от введенного направления.
    CheckDiamondSide - Проверка, образует ли след точки сторону бриллианта.
    IncreaseSides - Увеличение счетчика количества нарисованных сторон бриллианта на 1.
    CheckSides - Проверка, равно ли количество нарисованных сторон 4.
    OutputWin - Вывод сообщения о завершении рисования бриллианта.
    End - Конец программы.
"""
import os

# Инициализация позиции точки и счетчика сторон бриллианта
xPosition = 20
yPosition = 20
diamondSides = 0
previousPositions = []

# Функция для очистки экрана (кроссплатформенная)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Функция для отображения экрана
def display_screen(x, y, positions):
    clear_screen()
    # Создаем "экран" - список строк
    screen = [[' ' for _ in range(40)] for _ in range(40)]
    for pos_x, pos_y in positions:
        screen[pos_y][pos_x] = '#'
    # Устанавливаем текущую позицию точки
    screen[y][x] = '*'

    for row in screen:
        print(''.join(row))
    print(f"Текущая позиция: x={x}, y={y}, стороны: {diamondSides}")

# Основной игровой цикл
while diamondSides < 4:
    # Выводим экран
    display_screen(xPosition, yPosition, previousPositions)

    # Запрашиваем ввод направления движения
    try:
        direction = int(input("Введите направление (1-влево, 2-вниз, 3-вправо, 4-вверх): "))
    except ValueError:
        print("Пожалуйста, введите число от 1 до 4")
        continue

    # Обновляем позицию точки
    previousPositions.append((xPosition, yPosition))
    if direction == 1:  # Влево
        xPosition -= 1
    elif direction == 2:  # Вниз
        yPosition += 1
    elif direction == 3:  # Вправо
        xPosition += 1
    elif direction == 4:  # Вверх
        yPosition -= 1
    else:
        print("Неверное направление. Введите число от 1 до 4.")
        continue


    # Проверка условий для завершения стороны бриллианта
    # Здесь можно добавить более сложную логику
    # В данном примере простое условие: если точка вернулась в начальную точку по одной из сторон, считаем ее завершенной
    sideComplete = False
    if len(previousPositions) > 1:
        first_x, first_y = previousPositions[0]
        if (xPosition == first_x and yPosition == first_y):
              sideComplete=True

    if sideComplete :
        diamondSides += 1
        previousPositions = [] # начинаем отслеживать следующую сторону
# Выводим сообщение о завершении рисования бриллианта
display_screen(xPosition, yPosition, previousPositions)
print("DIAMOND COMPLETE!")
"""
Пояснения:
1. **Импорт модуля `os`**:
   - `import os`: Импортирует модуль `os`, который используется для очистки экрана.

2. **Инициализация переменных**:
   - `xPosition = 20`: Начальная координата x точки на экране.
   - `yPosition = 20`: Начальная координата y точки на экране.
   - `diamondSides = 0`: Счетчик нарисованных сторон бриллианта.
   - `previousPositions = []`: Список для хранения предыдущих позиций точки.

3. **Функция `clear_screen()`**:
   -  `os.system('cls' if os.name == 'nt' else 'clear')`: Очищает экран терминала. Используется `cls` для Windows и `clear` для других ОС.

4. **Функция `display_screen(x, y, positions)`**:
   -  Очищает экран, создает псевдографический "экран" (список списков).
   -  Отображает пройденный путь ('#') и текущую позицию точки ('*').

5. **Основной цикл `while diamondSides < 4:`**:
   -  Выводит текущее состояние экрана.
   -  Запрашивает ввод направления (1-4) у пользователя.
   -  Обрабатывает ввод:
     -  Обновляет координаты `xPosition`, `yPosition` в зависимости от выбранного направления.
     -  Добавляет текущую позицию в список `previousPositions`.
   -  Проверка, завершена ли сторона бриллианта.
     -  Условие: если точка вернулась в начальную точку по одной из сторон
   -  Если сторона завершена - увеличиваем счетчик `diamondSides` и обнуляем список `previousPositions`

6. **Вывод сообщения о завершении игры**:
    - После выхода из цикла, выводится сообщение "DIAMOND COMPLETE!", и экран в последний раз отображается.

"""
