"""
QUEEN:
=================
Сложность: 4
-----------------
Игра "Ферзь" - это игра, в которой на шахматной доске 8x8 размещается ферзь, а игрок пытается угадать, сколько ходов он может сделать. 
В начале игры ферзь ставится на случайную позицию, затем игроку предлагается ввести предполагаемое количество ходов, которые может сделать ферзь.
Программа вычисляет фактическое количество возможных ходов ферзя и сравнивает его с предположением игрока.
Игроку сообщается, был ли его ответ правильным или нет.
Правила игры:
-----------------
1. Ферзь размещается на случайно сгенерированной позиции на шахматной доске 8x8.
2. Игроку предлагается ввести количество ходов, которые ферзь может сделать с текущей позиции.
3. Программа вычисляет фактическое количество возможных ходов ферзя.
4. Программа сообщает игроку, было ли его предположение правильным или нет.
-----------------
Алгоритм:
1. Генерируется случайная позиция ферзя на шахматной доске (ряд row и столбец column от 1 до 8).
2. Инициализируется переменная countOfMoves для подсчета возможных ходов ферзя.
3. Для каждого возможного направления (горизонталь, вертикаль и диагонали) выполняется цикл.
4. Внутри каждого направления проверяются клетки, пока не достигнута граница доски или препятствие.
   Если клетка свободна, countOfMoves увеличивается на 1.
5. Игроку предлагается ввести число предполагаемых ходов.
6. Программа сравнивает введенное игроком число ходов с фактическим countOfMoves.
7. Выводится сообщение, угадал ли игрок количество ходов ферзя.
-----------------
Блок-схема: 
```mermaid
graph TD
    Start[Start] --> GenerateRandomPosition
    GenerateRandomPosition[Сгенерировать случайную позицию ферзя (row, column)] --> InitializeCountMoves
    InitializeCountMoves[Инициализировать countOfMoves = 0] --> CheckHorizontal
    CheckHorizontal[Проверка горизонтальных ходов] --> CheckVertical
    CheckVertical[Проверка вертикальных ходов] --> CheckDiagonal1
    CheckDiagonal1[Проверка диагональных ходов (слева-вверх/право-вниз)] --> CheckDiagonal2
    CheckDiagonal2[Проверка диагональных ходов (слева-вниз/право-вверх)] --> InputPlayerGuess
    InputPlayerGuess[Ввод предположения игрока о количестве ходов] --> CompareGuess
    CompareGuess[Сравнение предположения игрока с реальным количеством ходов] --> OutputResult
    OutputResult[Вывод результата] --> End[End]
    
    
    subgraph Horizontal Loop
        CheckHorizontal --> Horizontal_CheckLeft[Проверка клеток слева]
         Horizontal_CheckLeft --> Horizontal_IncrementLeft {Увеличить countOfMoves}
         Horizontal_IncrementLeft --> Horizontal_CheckLeft
        Horizontal_CheckLeft --> CheckHorizontal_Right[Проверка клеток справа]
        CheckHorizontal_Right --> Horizontal_IncrementRight {Увеличить countOfMoves}
        Horizontal_IncrementRight --> CheckHorizontal_Right
        Horizontal_CheckLeft -- "граница/препятствие" --> CheckVertical
        CheckHorizontal_Right -- "граница/препятствие" --> CheckVertical
    end
    
     subgraph Vertical Loop
        CheckVertical --> Vertical_CheckUp[Проверка клеток вверх]
        Vertical_CheckUp --> Vertical_IncrementUp {Увеличить countOfMoves}
        Vertical_IncrementUp --> Vertical_CheckUp
        Vertical_CheckUp --> Vertical_CheckDown[Проверка клеток вниз]
        Vertical_CheckDown --> Vertical_IncrementDown {Увеличить countOfMoves}
        Vertical_IncrementDown --> Vertical_CheckDown
        Vertical_CheckUp -- "граница/препятствие" --> CheckDiagonal1
        Vertical_CheckDown -- "граница/препятствие" --> CheckDiagonal1

    end

     subgraph Diagonal1 Loop
        CheckDiagonal1 --> Diagonal1_CheckUpLeft[Проверка клеток слева-вверх]
        Diagonal1_CheckUpLeft --> Diagonal1_IncrementUpLeft {Увеличить countOfMoves}
        Diagonal1_IncrementUpLeft --> Diagonal1_CheckUpLeft
        Diagonal1_CheckUpLeft --> Diagonal1_CheckDownRight[Проверка клеток справа-вниз]
        Diagonal1_CheckDownRight --> Diagonal1_IncrementDownRight {Увеличить countOfMoves}
        Diagonal1_IncrementDownRight --> Diagonal1_CheckDownRight
       Diagonal1_CheckUpLeft -- "граница/препятствие" --> CheckDiagonal2
        Diagonal1_CheckDownRight -- "граница/препятствие" --> CheckDiagonal2

     end

    subgraph Diagonal2 Loop
        CheckDiagonal2 --> Diagonal2_CheckDownLeft[Проверка клеток слева-вниз]
        Diagonal2_CheckDownLeft --> Diagonal2_IncrementDownLeft {Увеличить countOfMoves}
         Diagonal2_IncrementDownLeft --> Diagonal2_CheckDownLeft
        Diagonal2_CheckDownLeft --> Diagonal2_CheckUpRight[Проверка клеток справа-вверх]
        Diagonal2_CheckUpRight --> Diagonal2_IncrementUpRight {Увеличить countOfMoves}
        Diagonal2_IncrementUpRight --> Diagonal2_CheckUpRight
       Diagonal2_CheckDownLeft -- "граница/препятствие" --> InputPlayerGuess
       Diagonal2_CheckUpRight -- "граница/препятствие" --> InputPlayerGuess
    end
```
"""
import random

def calculate_queen_moves(row, column):
    """
    Вычисляет количество возможных ходов ферзя на шахматной доске.

    Args:
        row (int): Ряд, где находится ферзь (от 1 до 8).
        column (int): Столбец, где находится ферзь (от 1 до 8).

    Returns:
        int: Количество возможных ходов ферзя.
    """
    countOfMoves = 0  # Инициализируем счетчик ходов
    
    # Проверка горизонтальных ходов
    for i in range(column - 2, -1, -1):  # Ход влево
            countOfMoves += 1
    for i in range(column, 8):  # Ход вправо
            countOfMoves += 1


    # Проверка вертикальных ходов
    for i in range(row - 2, -1, -1):  # Ход вверх
            countOfMoves += 1
    for i in range(row, 8): # Ход вниз
            countOfMoves += 1

    # Проверка диагональных ходов (слева-вверх / право-вниз)
    for i in range(1, 8):
        if row - 1 - i >= 0 and column - 1 - i >= 0:
            countOfMoves += 1  # Вверх и влево
        else:
            break
    for i in range(1, 8):
        if row - 1 + i < 8 and column - 1 + i < 8:
             countOfMoves += 1 # Вниз и вправо
        else:
            break

    # Проверка диагональных ходов (слева-вниз / право-вверх)
    for i in range(1, 8):
         if row - 1 + i < 8 and column - 1 - i >= 0:
             countOfMoves += 1 # Вниз и влево
         else:
            break
    for i in range(1, 8):
        if row - 1 - i >= 0 and column - 1 + i < 8:
             countOfMoves += 1 # Вверх и вправо
        else:
            break
        
    return countOfMoves

def main():
    """Основная функция игры "Ферзь"."""
    # 1. Генерируем случайную позицию ферзя на доске
    row = random.randint(1, 8)  # Случайный ряд от 1 до 8
    column = random.randint(1, 8)  # Случайный столбец от 1 до 8
    print(f"Ферзь размещен на позиции: ряд {row}, столбец {column}")

    # 2. Вычисляем количество возможных ходов
    countOfMoves = calculate_queen_moves(row, column)

    # 3. Запрашиваем у пользователя предположение о количестве ходов
    while True:
        try:
            playerGuess = int(input("Сколько ходов, по вашему мнению, может сделать ферзь? "))
            break  # Выходим из цикла, если ввод успешен
        except ValueError:
            print("Пожалуйста, введите целое число.")
    
    # 4. Сравниваем предположение игрока с реальным количеством ходов
    if playerGuess == countOfMoves:
        print("Поздравляю! Вы угадали количество ходов ферзя.")
    else:
        print(f"К сожалению, вы не угадали. Ферзь может сделать {countOfMoves} ходов.")

if __name__ == "__main__":
    main()
"""
Пояснения:
1. `calculate_queen_moves(row, column)`: 
    - Функция принимает row (ряд) и column (столбец) в качестве входных данных.
    - Переменная `countOfMoves` инициализируется нулем, она будет хранить количество возможных ходов ферзя.
    - Циклы используются для проверки горизонтальных, вертикальных и диагональных ходов.
    - Для каждого направления проверяются клетки, пока не достигнута граница доски.
    - Если клетка свободна, `countOfMoves` увеличивается на 1.
    - Функция возвращает общее количество возможных ходов.

2.  `main()`:
    - Генерируется случайная позиция ферзя (`row`, `column`).
    - Функция `calculate_queen_moves()` вызывается для вычисления количества возможных ходов ферзя.
    - Пользователю предлагается ввести свое предположение о количестве ходов.
    - Происходит проверка ввода, с целью удостовериться что было введено целое число.
    - Сравнивается предположение пользователя с реальным количеством ходов.
    - Выводится результат - угадал ли пользователь количество ходов.

3. **Объяснения переменных:**
    - `row` (int): Ряд, где расположен ферзь (от 1 до 8).
    - `column` (int): Столбец, где расположен ферзь (от 1 до 8).
    - `countOfMoves` (int): Общее количество возможных ходов ферзя.
    - `playerGuess` (int): Предположение игрока о количестве ходов.

4. **Дополнительно**
    - Код разбит на функции для лучшей читаемости и повторного использования.
    - Все имена переменных и функций понятны и описывают свою роль.
    - Код комментирован для простоты понимания новичками.
"""
__author__ = 'hypo69 (hypo69@davidka.net)'
```