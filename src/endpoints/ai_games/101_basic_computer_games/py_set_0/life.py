"""
<LIFE>:
=================
Сложность: 6
-----------------
Игра LIFE - это имитация клеточного автомата, разработанная Джоном Конвеем. На прямоугольном поле случайным образом размещаются "живые" клетки. В каждом шаге игры клетки либо умирают от одиночества или перенаселения, либо рождаются, если рядом достаточно живых клеток. Игроку предоставляется возможность начальной настройки поля, а затем наблюдать за развитием колонии.
Правила игры: 
-----------------
1. Игровое поле представляет собой матрицу размером 20x20.
2. В начале игры пользователь вводит количество начальных "живых" клеток.
3. Для каждой клетки в каждом шаге игры проверяется количество ее соседей.
4. Если у клетки два или три живых соседа, она выживает в следующем поколении.
5. Если у клетки меньше двух или больше трех живых соседей, она умирает.
6. Если у пустой клетки три живых соседа, в следующем поколении в этом месте рождается клетка.
7. Игра продолжается до тех пор, пока пользователь не решит ее остановить.
-----------------
Алгоритм:
1. Инициализация:
   - Запрашивается количество начальных живых клеток.
   - Игровое поле (матрица 20x20) заполняется нулями (мертвые клетки).
   - Случайным образом выбираются координаты для заданного количества начальных живых клеток.
   - В выбранных координатах клетки становятся "живыми" (записывается 1).
2. Основной цикл:
   - Выводится текущее состояние игрового поля.
   - Создается временная матрица для хранения следующего поколения клеток.
   - Для каждой клетки на игровом поле:
     - Подсчитывается количество живых соседей.
     - Временная матрица обновляется в соответствии с правилами игры (рождение, смерть, выживание).
   - Исходная матрица обновляется из временной матрицы.
   - Запрашивается ввод пользователя для продолжения игры.
   - Если пользователь вводит "N", игра завершается.
   - Если пользователь вводит что-либо другое, цикл повторяется.
-----------------
Блок-схема: 
```mermaid
graph TD
    A[Start] --> B(Initialize Game: Get initial alive cells);
    B --> C{Is initial alive cells > 0?};
    C -- Yes --> D(Generate random coordinates);
    D --> E(Set alive cell in field by coordinates);
    E --> F{Decrement initial alive cells};
    F --> G{Is initial alive cells > 0?};
    G -- Yes --> D
    G -- No --> H(Show Game Field);
    H --> I(Create temporary field);
    I --> J{For each cell in field};
    J --> K(Count alive neighbors);
    K --> L(Apply game rules to update temporary field);
    L --> M{Is current cell the last cell?};
    M -- No --> J
    M -- Yes --> N(Update Game Field from temporary field);
    N --> O(Input User Choice (continue?));
    O --> P{Is user choice == "N"?};
    P -- Yes --> Q(End);
    P -- No --> H
```
"""
import random

def initialize_field(field_size: int) -> list[list[int]]:
    """
    Инициализирует игровое поле заданного размера, заполняя его нулями (мертвыми клетками).

    Args:
        field_size: Размер стороны игрового поля.

    Returns:
        list[list[int]]: Двумерный список, представляющий игровое поле.
    """
    return [[0 for _ in range(field_size)] for _ in range(field_size)]

def generate_random_coordinates(field_size: int) -> tuple[int, int]:
    """
    Генерирует случайные координаты для размещения живой клетки на игровом поле.

    Args:
        field_size: Размер стороны игрового поля.

    Returns:
       tuple[int, int]: Случайные координаты (строка, столбец).
    """
    row = random.randint(0, field_size - 1)
    col = random.randint(0, field_size - 1)
    return row, col

def set_alive_cell(field: list[list[int]], row: int, col: int) -> None:
   """
   Устанавливает клетку в заданных координатах как "живую" (значение 1).

   Args:
       field: Игровое поле (матрица).
       row: Координата строки.
       col: Координата столбца.
   """
   field[row][col] = 1

def show_field(field: list[list[int]]) -> None:
    """
    Выводит текущее состояние игрового поля на экран.

    Args:
        field: Игровое поле (матрица).
    """
    for row in field:
        for cell in row:
            print("*" if cell == 1 else ".", end=" ")
        print()

def count_alive_neighbors(field: list[list[int]], row: int, col: int, field_size: int) -> int:
    """
    Подсчитывает количество живых соседей у клетки в заданных координатах.

    Args:
        field: Игровое поле (матрица).
        row: Координата строки клетки.
        col: Координата столбца клетки.
        field_size: Размер стороны игрового поля.

    Returns:
        int: Количество живых соседей.
    """
    alive_neighbors = 0
    for i in range(max(0, row - 1), min(field_size, row + 2)):
        for j in range(max(0, col - 1), min(field_size, col + 2)):
            if i == row and j == col: # пропускаем саму клетку
                continue
            alive_neighbors += field[i][j]
    return alive_neighbors

def update_cell_state(field: list[list[int]], temp_field: list[list[int]], row: int, col: int, field_size: int) -> None:
    """
    Обновляет состояние клетки в соответствии с правилами игры LIFE.

    Args:
        field: Игровое поле (матрица).
        temp_field: Временное поле для хранения нового состояния клеток.
        row: Координата строки клетки.
        col: Координата столбца клетки.
        field_size: Размер стороны игрового поля.
    """
    alive_neighbors = count_alive_neighbors(field, row, col, field_size)
    if field[row][col] == 1:  # Клетка жива
        if alive_neighbors < 2 or alive_neighbors > 3:
             temp_field[row][col] = 0  # Умирает от одиночества или перенаселения
        else:
            temp_field[row][col] = 1 # Выживает
    else: # Клетка мертва
        if alive_neighbors == 3:
             temp_field[row][col] = 1 # Рождается новая клетка
        else:
            temp_field[row][col] = 0 # Остается мертвой

def update_field(field: list[list[int]], field_size: int) -> list[list[int]]:
    """
    Создает новое поколение игрового поля на основе правил игры.

    Args:
         field: Игровое поле (матрица).
         field_size: Размер стороны игрового поля.
    Returns:
        list[list[int]]:  Новое игровое поле
    """
    temp_field = initialize_field(field_size)
    for row in range(field_size):
        for col in range(field_size):
             update_cell_state(field,temp_field, row, col, field_size)
    return temp_field
    
def main() -> None:
    """
     Основная функция для запуска игры LIFE
    """
    field_size = 20
    field = initialize_field(field_size)

    initial_alive_cells = int(input("Введите количество начальных живых клеток: "))
    for _ in range(initial_alive_cells):
        row, col = generate_random_coordinates(field_size)
        set_alive_cell(field,row, col)

    while True:
        show_field(field)
        temp_field = update_field(field, field_size)
        field = temp_field
        user_choice = input("Продолжить? (N для выхода): ").strip().upper()
        if user_choice == "N":
            break

if __name__ == "__main__":
    main()
"""
Пояснения:
----------------
1. Инициализация:
   - `initialize_field(field_size)`: Создает игровое поле заданного размера и заполняет его нулями (мертвые клетки).
   - `initial_alive_cells`: Запрашивает у пользователя количество начальных живых клеток.
   -  Цикл `for _ in range(initial_alive_cells)`:
       -  `generate_random_coordinates(field_size)`: Генерирует случайные координаты.
       -  `set_alive_cell(field,row, col)`: Устанавливает клетку в полученных случайных координатах как живую.

2. Основной игровой цикл `while True`:
   - `show_field(field)`: Выводит текущее состояние игрового поля на экран.
   - `temp_field = update_field(field, field_size)`:  Обновляет игровое поле на основе правил игры, создает новое поколение.
   - `field = temp_field`: Обновляет основное игровое поле новым поколением.
   -  `user_choice`: Запрашивает у пользователя ввод для продолжения игры.
   -  Условие `if user_choice == "N"`:
       - Если пользователь вводит 'N', игра завершается.

3. Функции:
   - `initialize_field(field_size)`: создает и возвращает игровое поле (матрица).
   -  `generate_random_coordinates(field_size)`: генерирует случайные координаты для клеток.
   -  `set_alive_cell(field, row, col)`: устанавливает клетку в заданных координатах как "живую".
   -  `show_field(field)`: выводит текущее состояние игрового поля.
   -  `count_alive_neighbors(field, row, col, field_size)`: подсчитывает живых соседей клетки.
   -  `update_cell_state(field, temp_field, row, col, field_size)`: применяет правила игры, чтобы определить состояние клетки в следующем поколении.
   -  `update_field(field, field_size)`: создает новое поколение игрового поля.
   - `main()`:  функция для запуска игры
----------------
licence:MIT(../licence)
"""
__author__ = 'hypo69 (hypo69@davidka.net)'
```