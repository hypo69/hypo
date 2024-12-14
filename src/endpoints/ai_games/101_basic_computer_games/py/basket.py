"""
<BASKET>:
=================
Сложность: 3
-----------------
Игра "Корзина" представляет собой простую текстовую игру, в которой игрок пытается поймать мячи, падающие с неба, с помощью корзины. Игрок перемещает корзину влево и вправо, вводя соответствующие команды. Игра ведется до тех пор, пока игрок не пропустит три мяча.
Правила игры:
1. Игровое поле представлено 10 позициями, пронумерованными от 1 до 10.
2. Корзина первоначально находится в позиции 5.
3. Мячи падают в случайных позициях от 1 до 10.
4. Игрок вводит 'L' для перемещения корзины влево, 'R' для перемещения вправо и 'N' для попытки поймать мяч, если корзина находится в той же позиции, что и падающий мяч.
5. Если мяч пойман, то количество пойманных мячей увеличивается, если нет то количество пропущенных мячей увеличивается.
6. Игра заканчивается, когда игрок пропустит 3 мяча.
-----------------
Алгоритм:
1. Инициализация:
   - Установить количество пропущенных мячей (missed_balls) в 0.
   - Установить позицию корзины (basket_position) в 5.
   - Установить количество пойманных мячей (caught_balls) в 0.
2. Начало игрового цикла:
   - Сгенерировать случайную позицию падающего мяча (ball_position) от 1 до 10.
   - Вывести сообщение о позиции падающего мяча.
   - Ввести команду игрока.
3. Обработка команды игрока:
   - Если команда 'L':
     - Переместить корзину влево (уменьшить basket_position на 1, если basket_position > 1).
   - Если команда 'R':
     - Переместить корзину вправо (увеличить basket_position на 1, если basket_position < 10).
   - Если команда 'N':
     - Если позиция мяча совпадает с позицией корзины:
       - Увеличить количество пойманных мячей на 1.
       - Вывести сообщение о том, что мяч пойман.
     - Иначе:
       - Увеличить количество пропущенных мячей на 1.
       - Вывести сообщение о том, что мяч пропущен.
   - Если введена неправильная команда - вывести предупреждение.
4. Проверка окончания игры:
   - Если количество пропущенных мячей равно 3, завершить игру.
5. Повторить шаги 2-4 до окончания игры.
6. Вывести результаты игры.
-----------------
Блок-схема: 
```mermaid
graph TD
    Start[Start] --> Initialize
    Initialize[Initialize: missed_balls=0, basket_position=5, caught_balls=0] --> GameLoop
    GameLoop[Game Loop: missed_balls < 3] --> GenerateBallPosition
    GenerateBallPosition[Generate Ball Position: ball_position = random(1 to 10)] --> OutputBallPosition
    OutputBallPosition[Output: Сообщение о позиции мяча] --> InputCommand
    InputCommand[Input: Команда игрока] --> ProcessCommand
    ProcessCommand{Process Command}
    ProcessCommand -- 'L' --> MoveBasketLeft
    ProcessCommand -- 'R' --> MoveBasketRight
     ProcessCommand -- 'N' --> CheckCatch
     ProcessCommand -- Other --> InvalidCommand
    InvalidCommand[Output: Неверная команда] --> GameLoop

    MoveBasketLeft{Move Basket Left}
     MoveBasketLeft --> CheckBasketLeftBoundary
    CheckBasketLeftBoundary{basket_position > 1?}
    CheckBasketLeftBoundary -- Yes --> DecreaseBasketLeft
     CheckBasketLeftBoundary -- No --> GameLoop
    DecreaseBasketLeft[basket_position = basket_position - 1] --> GameLoop

    MoveBasketRight{Move Basket Right}
     MoveBasketRight --> CheckBasketRightBoundary
     CheckBasketRightBoundary{basket_position < 10?}
    CheckBasketRightBoundary -- Yes --> IncreaseBasketRight
    CheckBasketRightBoundary -- No --> GameLoop
    IncreaseBasketRight[basket_position = basket_position + 1] --> GameLoop


    CheckCatch{Check Catch}
    CheckCatch --> ComparePositions
    ComparePositions{ball_position == basket_position?}
     ComparePositions -- Yes --> BallCaught
     ComparePositions -- No --> BallMissed
    BallCaught[Output: Мяч пойман, caught_balls++] --> GameLoop
    BallMissed[Output: Мяч пропущен, missed_balls++] --> GameLoop
    GameLoop -- missed_balls >=3 --> EndGame
    EndGame[Output: Результаты игры] --> End
    End[End]
```
"""
import random

# Инициализация переменных
missed_balls = 0  # Количество пропущенных мячей
basket_position = 5  # Начальная позиция корзины
caught_balls = 0 # Количество пойманных мячей


# Основной игровой цикл
while missed_balls < 3:
    # Генерируем случайную позицию падающего мяча
    ball_position = random.randint(1, 10)
    print(f"Мяч падает на позицию {ball_position}")
    
    # Получаем команду от игрока
    command = input("Введите команду (L - влево, R - вправо, N - поймать): ").upper()

    # Обрабатываем команду
    if command == 'L':
        # Перемещаем корзину влево, если это возможно
        if basket_position > 1:
            basket_position -= 1
    elif command == 'R':
        # Перемещаем корзину вправо, если это возможно
        if basket_position < 10:
            basket_position += 1
    elif command == 'N':
        # Проверяем, поймал ли игрок мяч
        if ball_position == basket_position:
            print("Поймал!")
            caught_balls += 1
        else:
            print("Пропустил!")
            missed_balls += 1
    else:
        print("Неверная команда. Пожалуйста, введите 'L', 'R' или 'N'.")

# Выводим результаты игры
print("Игра окончена!")
print(f"Поймано мячей: {caught_balls}")
print(f"Пропущено мячей: {missed_balls}")
"""
Пояснения:
1. `missed_balls`: Целочисленная переменная, которая хранит количество пропущенных мячей. Изначально равна 0.
2. `basket_position`: Целочисленная переменная, представляющая позицию корзины на игровом поле. Начальное значение равно 5.
3. `caught_balls`: Целочисленная переменная, которая хранит количество пойманных мячей. Изначально равна 0.
4. `random.randint(1, 10)`: Функция из модуля `random`, которая возвращает случайное целое число от 1 до 10 включительно. Используется для определения позиции падающего мяча.
5. `input(...)`: Функция для получения ввода от пользователя. Она выводит сообщение, переданное в качестве аргумента, и возвращает введенную пользователем строку.
6. `command.upper()`: Метод строки, который преобразует все символы строки в верхний регистр. Используется для того, чтобы не учитывать регистр при вводе команды.
7. `if command == 'L': ... elif command == 'R': ... elif command == 'N': ... else: ...`: Условная конструкция, которая обрабатывает команду, введенную пользователем.
8. `if basket_position > 1:` и `if basket_position < 10:`: Условия, которые проверяют, не выходит ли корзина за границы игрового поля.
9. `print(...)`: Функция для вывода текста на экран.
10. `print(f"...")`: Форматированная строковая литерала (f-строка), которая позволяет включать значения переменных в строку.
11. `missed_balls += 1` и `caught_balls += 1`:  Операторы инкремента, которые увеличивают значения переменных на 1.
12. `while missed_balls < 3:`: Цикл while, который выполняется до тех пор, пока количество пропущенных мячей не станет равным 3.
licence:MIT(../licence)
"""
__author__ = 'hypo69 (hypo69@davidka.net)'
```