## Анализ кода `life_2.py`

### <алгоритм>
1. **Начало**: Программа запускается.
2. **Ввод параметров поля**: Пользователь вводит количество строк `numRows` и столбцов `numCols` игрового поля.
   - _Пример_: `numRows = 5`, `numCols = 5`
3. **Ввод количества живых клеток**: Пользователь вводит количество начальных живых клеток `initialAliveCells`.
   - _Пример_: `initialAliveCells = 5`
4. **Инициализация поля**: Создается игровое поле `grid` размером `numRows` x `numCols`, заполненное мертвыми клетками (' ').
   - _Пример_: `grid = [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]`
5. **Размещение живых клеток**: Случайным образом на поле `grid` размещаются `initialAliveCells` живых клеток ('*').
    - _Пример_: После размещения: `grid = [[' ', '*', ' ', ' ', ' '], [' ', ' ', ' ', '*', ' '], ['*', ' ', ' ', ' ', ' '], [' ', ' ', '*', ' ', ' '], [' ', ' ', ' ', ' ', '*']]`
6. **Вывод начального состояния поля**: Игровое поле `grid` выводится на экран.
7. **Начало игрового цикла**: Запускается бесконечный цикл, который выполняется до тех пор, пока пользователь не введет '0'.
8. **Вычисление следующего поколения**:
    - Создается копия текущего поля `nextGrid` для вычисления следующего поколения.
    - Для каждой клетки в `grid`:
        - Подсчитывается количество живых соседей с помощью `count_alive_neighbors`.
        - Применяются правила игры "Жизнь" для определения состояния клетки в `nextGrid`.
            - Если клетка живая ('*'):
                - Если живых соседей меньше 2 или больше 3, клетка умирает.
            - Если клетка мертвая (' '):
                - Если живых соседей ровно 3, клетка рождается.
9. **Обновление поля**: Текущее поле `grid` заменяется на новое поле `nextGrid`.
10. **Вывод текущего состояния поля**: Игровое поле `grid` выводится на экран.
11. **Запрос на продолжение**: Пользователь вводит '0' для выхода или любое другое значение для продолжения.
    - Если ввод '0':
        - **Конец**: Игра завершается.
    - Если ввод не '0':
        - Переход к шагу 8.

### <mermaid>

```mermaid
flowchart TD
    Start[Начало] --> InputRowsCols[Ввод количества строк: <code>numRows</code>\n и столбцов: <code>numCols</code>];
    InputRowsCols --> InputAliveCells[Ввод количества начальных живых клеток: <code>initialAliveCells</code>];
    InputAliveCells --> InitializeGrid[Инициализация игрового поля: <code>grid</code>\n(заполнено мертвыми клетками ' ')];
    InitializeGrid --> PlaceAliveCells[Размещение начальных живых клеток ('*')\nна игровом поле: <code>grid</code>];
    PlaceAliveCells --> OutputGrid[Вывод начального состояния\nигрового поля: <code>grid</code>];
    OutputGrid --> GameLoopStart{Начало игрового цикла};
    GameLoopStart --> ComputeNextGeneration[Вычисление следующего поколения:\n<code>nextGrid</code> = <code>compute_next_generation(grid)</code>];
     ComputeNextGeneration --> UpdateGrid[Обновление игрового поля:\n<code>grid</code> = <code>nextGrid</code>];
    UpdateGrid --> OutputCurrentGrid[Вывод текущего состояния игрового поля: <code>grid</code>];
    OutputCurrentGrid --> InputUserContinue[Ввод пользователя (0 - выход)];
    InputUserContinue -- "0" --> End[Конец];
    InputUserContinue -- "Другое значение" --> GameLoopStart;
     ComputeNextGeneration -->  CalculateNeighbors[Для каждой клетки подсчет количества живых соседей: <code>alive_neighbors = count_alive_neighbors(grid, row, col)</code>];
    CalculateNeighbors  --> ApplyRules[Применение правил игры «Жизнь»\n для определения состояния клетки\n в новом поколении: <code>nextGrid</code>]
    ApplyRules --> |Далее|  ComputeNextGeneration
    
    
    subgraph calculate_next_generation
     CalculateNeighbors
     ApplyRules
    end

```

### <объяснение>
**Импорты:**
- `import random`: Используется для генерации случайных координат при размещении начальных живых клеток на игровом поле.
- `import copy`: Используется для создания глубокой копии игрового поля. Это необходимо для вычисления следующего поколения, чтобы изменения в новом поле не влияли на текущее поле во время вычислений.

**Функции:**
1.  `initialize_grid(num_rows, num_cols)`:
    - **Назначение**: Создает игровое поле (сетку) размером `num_rows` x `num_cols` и заполняет его мертвыми клетками (пробелами).
    - **Аргументы**:
        - `num_rows` (int): Количество строк в сетке.
        - `num_cols` (int): Количество столбцов в сетке.
    - **Возвращаемое значение**:
        - `grid` (list of lists): Игровое поле, представленное в виде списка списков.
    - **Пример**: `initialize_grid(3, 4)` возвращает `[[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]`.
2.  `place_alive_cells(grid, initial_alive_cells)`:
    - **Назначение**: Размещает заданное количество живых клеток ('*') на игровом поле в случайных местах.
    - **Аргументы**:
        - `grid` (list of lists): Игровое поле.
        - `initial_alive_cells` (int): Количество живых клеток для размещения.
    - **Возвращаемое значение**: None (модифицирует `grid` напрямую).
    - **Пример**: Если `grid` равно `[[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]`, и `initial_alive_cells` равно 2, то после выполнения `place_alive_cells(grid, 2)`, `grid` может стать, например, `[['*', ' ', ' '], [' ', '*', ' '], [' ', ' ', ' ']]`.
3.  `display_grid(grid)`:
    - **Назначение**: Выводит текущее состояние игрового поля на экран.
    - **Аргументы**:
        - `grid` (list of lists): Игровое поле.
    - **Возвращаемое значение**: None (выводит данные на консоль).
4. `count_alive_neighbors(grid, row, col)`:
    - **Назначение**: Подсчитывает количество живых соседей у клетки с индексами `row` и `col`.
    - **Аргументы**:
        - `grid` (list of lists): Игровое поле.
        - `row` (int): Индекс строки клетки.
        - `col` (int): Индекс столбца клетки.
    - **Возвращаемое значение**:
        - `alive_neighbors` (int): Количество живых соседей.
    - **Пример**: Если `grid` равно `[['*', '*', ' '], [' ', '*', ' '], [' ', ' ', '*']]` и `row=1`, `col=1`, то `count_alive_neighbors(grid, 1, 1)` вернет 3.
5. `compute_next_generation(grid)`:
    - **Назначение**: Вычисляет следующее поколение клеток на основе текущего состояния поля и правил игры "Жизнь".
    - **Аргументы**:
        - `grid` (list of lists): Текущее игровое поле.
    - **Возвращаемое значение**:
        - `next_grid` (list of lists): Новое игровое поле, представляющее следующее поколение.
    - **Пример**: Применяет правила игры "Жизнь" к каждой клетке в `grid` для создания `next_grid`.

**Переменные:**
- `num_rows` (int): Количество строк игрового поля, введенное пользователем.
- `num_cols` (int): Количество столбцов игрового поля, введенное пользователем.
- `initial_alive_cells` (int): Количество начальных живых клеток, введенное пользователем.
- `grid` (list of lists): Текущее состояние игрового поля.
- `next_grid` (list of lists): Новое состояние игрового поля после вычисления следующего поколения.
- `alive_neighbors` (int): Количество живых соседей у клетки.
- `user_input` (str): Строка, введенная пользователем для управления игровым циклом.

**Возможные улучшения:**
- Добавить проверки на ввод пользователя (например, на то, что введены целые числа).
- Можно было бы сделать более наглядным вывод игрового поля, например, с рамкой.
- Возможность выбора начального положения клеток (вместо случайного).

**Связь с другими частями проекта:**
Этот код не имеет явных связей с другими частями проекта, поскольку это автономная реализация игры "Жизнь". Однако, его можно было бы интегрировать в более крупную систему, например, через интерфейс или класс, который управлял бы запуском и отображением игры.