# Анализ кода игры "Жизнь"

## <алгоритм>

### 1. Ввод параметров симуляции
   - Пользователю предлагается ввести размеры игрового поля (количество строк и столбцов).
     -  **Пример**: `rows = 10`, `cols = 20`
   - Пользователь вводит количество поколений для симуляции.
     - **Пример**: `generations = 50`
   - Пользователь выбирает случайную или ручную конфигурацию клеток.
     - **Пример**: выбор случайной конфигурации `use_random = 'y'`
   - Если выбрана ручная конфигурация, то пользователь вводит начальное состояние клеток построчно.
     - **Пример**:
        ```
        initial_config = ["*   *     ",
                         "  **   **",
                         " *    *  ",
                          "       * ",
                        ]
        ```
     
### 2. Создание начальной сетки
   - На основе введенных размеров и начальной конфигурации создаётся двумерный список (сетка), представляющий игровое поле.
     -  **Пример**: `grid = [[' ', '*', ' ', ' ', ' ', ' ', ' '], ['*', '*', ' ', ' ', ' ', '*', ' '], [' ', ' ', '*', ' ', ' ', ' ', ' '],  [' ', ' ', ' ', '*', ' ', ' ', ' ']]`

### 3. Цикл симуляции поколений
   - Цикл повторяется `generations` раз.
     - **Пример**: `for generation in range(generations):`
   - В начале каждого цикла:
     - Текущая сетка выводится на экран.
       - **Пример**: 
         ```
         * *
         **
          *  
         ```
     - Создается новое поколение сетки `next_grid`.

### 4. Создание нового поколения
   - Цикл по каждой клетке текущей сетки: `for row in range(rows): for col in range(cols):`
     - Подсчитывается количество живых соседей для текущей клетки с помощью функции `count_live_neighbours`.
       -  **Пример**: для клетки в позиции (1, 1) возвращается количество живых соседей `live_neighbours = 3`
     - Состояние клетки в следующем поколении определяется правилами игры, вызывается функция `apply_rules`.
       - **Пример**: если клетка жива и имеет 3 живых соседа, в `next_grid` клетка остается живой
     - Обновление состояния клетки в `next_grid`.
       -  **Пример**: `next_grid[row][col] = '*' ` или `next_grid[row][col] = ' '`

### 5. Обновление сетки и задержка
   - Текущая сетка `grid` обновляется новым поколением `next_grid`.
      - **Пример**:  `grid = next_grid`
   - Добавляется небольшая задержка перед выводом следующего поколения.
     - **Пример**: `time.sleep(0.5)`
   - Повторить шаг 3.

### 6. Вывод конечного состояния
   - После завершения всех поколений выводится итоговое состояние сетки.

## <mermaid>

```mermaid
flowchart TD
    Start[Начало] --> GetGridSize[<code>get_grid_size()</code><br>Ввод размеров сетки]
    GetGridSize --> GetGenerations[<code>get_generations()</code><br>Ввод количества поколений]
    GetGenerations --> GetInitialConfig[<code>get_initial_config()</code><br>Ввод начальной конфигурации]
    GetInitialConfig --> CreateGrid[<code>create_grid()</code><br>Создание сетки]
    CreateGrid --> GameLoopStart[Начало цикла поколений]
    GameLoopStart -- Итерация есть --> PrintCurrentGrid[<code>print_grid()</code><br>Вывод текущей сетки]
    PrintCurrentGrid --> NextGenGrid[<code>next_generation()</code><br>Создание следующей сетки]
    NextGenGrid --> UpdateGrid[Обновление текущей сетки]
    UpdateGrid --> Delay[Задержка]
    Delay --> GameLoopEnd[Конец цикла поколений]
    GameLoopEnd -- Да --> GameLoopStart
    GameLoopEnd -- Нет --> PrintFinalGrid[<code>print_grid()</code><br>Вывод финальной сетки]
    PrintFinalGrid --> End[Конец]

    subgraph "Функция next_generation()"
    NextGenGrid --> LoopCellsStart[Начало цикла по клеткам]
    LoopCellsStart --> CountNeighbours[<code>count_live_neighbours()</code><br>Подсчет живых соседей]
    CountNeighbours --> ApplyRulesFunc[<code>apply_rules()</code><br>Применение правил]
    ApplyRulesFunc --> UpdateNextGrid[Обновление next_grid]
    UpdateNextGrid --> LoopCellsEnd[Конец цикла по клеткам]
    LoopCellsEnd --> ReturnNextGrid[Возврат next_grid]
    end
    
    style Start fill:#f9f,stroke:#333,stroke-width:2px
    style End fill:#ccf,stroke:#333,stroke-width:2px
```

### Зависимости в диаграмме `mermaid`

В данной диаграмме представлены основные функции и потоки управления в программе "Жизнь". Вот объяснение зависимостей, которые присутствуют в диаграмме:

1. **`Start` (Начало)**: Начальная точка программы.
2. **`get_grid_size()`**: Функция, запрашивающая у пользователя размеры сетки (количество строк и столбцов).
3. **`get_generations()`**: Функция, запрашивающая у пользователя количество поколений для симуляции.
4. **`get_initial_config()`**: Функция, запрашивающая у пользователя начальную конфигурацию сетки (случайная или ручная).
5. **`create_grid()`**: Функция, создающая начальную сетку на основе размеров и начальной конфигурации.
6. **`GameLoopStart` (Начало цикла поколений)**: Начало основного цикла симуляции, который повторяется заданное количество раз (поколений).
7. **`print_grid()`**: Функция, выводящая текущее состояние сетки на экран.
8. **`next_generation()`**: Функция, создающая следующее поколение сетки на основе текущего.
    - Внутри функции `next_generation()` есть подграф:
      -   **`LoopCellsStart` (Начало цикла по клеткам)**: Начало цикла для каждой клетки в сетке.
      -   **`count_live_neighbours()`**: Функция, подсчитывающая количество живых соседей у текущей клетки.
      -   **`apply_rules()`**: Функция, применяющая правила игры "Жизнь" для определения состояния клетки в следующем поколении.
      -   **`UpdateNextGrid`**: Обновление состояния клетки в `next_grid`
      -   **`LoopCellsEnd` (Конец цикла по клеткам)**: Конец цикла для каждой клетки в сетке.
      -   **`ReturnNextGrid`**: Возврат `next_grid`.
9.  **`UpdateGrid`**: Обновление текущей сетки (grid) новой сеткой (next_grid).
10. **`Delay`**: Задержка перед выводом следующего поколения.
11. **`GameLoopEnd` (Конец цикла поколений)**: Конец основного цикла симуляции. Если есть еще поколения, цикл повторяется.
12. **`print_grid()`**: Функция, выводящая финальное состояние сетки на экран.
13. **`End` (Конец)**: Конечная точка программы.

Все эти функции работают в последовательности, передавая данные от одной к другой и создавая необходимую структуру симуляции игры "Жизнь". Функция `next_generation()` содержит в себе подграф, что наглядно показывает её более сложную структуру.

## <объяснение>

### Импорты
- `import random`: Используется для генерации случайных чисел при создании начальной конфигурации сетки, если пользователь выбирает случайное заполнение.
- `import time`: Используется для добавления задержки между поколениями, чтобы симуляция была более наглядной.

### Функции

1.  **`get_grid_size()`**:
    -   **Назначение**: Запрашивает у пользователя размеры сетки (количество строк и столбцов), обрабатывает неверный ввод, и возвращает валидные значения.
    -   **Аргументы**: Нет.
    -   **Возвращаемое значение**: `rows` (int), `cols` (int) - размеры сетки.
    -   **Пример**:
        ```python
        rows, cols = get_grid_size()  # Ввод: 10, 20
        print(rows, cols) # Вывод: 10, 20
        ```
2.  **`get_generations()`**:
    -   **Назначение**: Запрашивает у пользователя количество поколений, обрабатывает неверный ввод, и возвращает валидное значение.
    -   **Аргументы**: Нет.
    -   **Возвращаемое значение**: `generations` (int) - количество поколений.
    -   **Пример**:
        ```python
        generations = get_generations()  # Ввод: 50
        print(generations) # Вывод: 50
        ```
3. **`get_initial_config(rows, cols)`**:
   - **Назначение**: Запрашивает у пользователя выбор случайной конфигурации или ввода своей, проверяет корректность ввода и возвращает начальную конфигурацию.
   - **Аргументы**:
     - `rows` (int): количество строк в сетке.
     - `cols` (int): количество столбцов в сетке.
   - **Возвращаемое значение**: `initial_config` (list of strings) - начальная конфигурация сетки.
   - **Примеры**:
     ```python
     # Случайная конфигурация
     initial_config = get_initial_config(5, 5)
     print(initial_config) # Вывод: [[' ', '*', ' ', '*', ' '], [' ', '*', '*', ' ', ' '], ... ]

     # Ручная конфигурация
     initial_config = get_initial_config(2, 3)  # Ввод: n, "*  ", " * "
     print(initial_config) # Вывод: ["*  ", " * "]
     ```
4.  **`create_grid(rows, cols, initial_config=None)`**:
    -   **Назначение**: Создает сетку (список списков) на основе заданных размеров и начальной конфигурации.
    -   **Аргументы**:
        -   `rows` (int): Количество строк в сетке.
        -   `cols` (int): Количество столбцов в сетке.
        -   `initial_config` (list of strings, optional): Начальная конфигурация сетки. По умолчанию `None`.
    -   **Возвращаемое значение**: `grid` (list of lists of strings) - сетка.
    -   **Пример**:
        ```python
        grid = create_grid(3, 3) # Случайная сетка
        print(grid) # Вывод: [[' ', '*', ' '], ['*', ' ', '*'], ['*', '*', ' ']]

        initial_config = ["***", "*  ", " **"]
        grid = create_grid(3, 3, initial_config) # Создание сетки на основе введенных данных
        print(grid) # Вывод: [['*', '*', '*'], ['*', ' ', ' '], ['*', ' ', '*']]
        ```
5.  **`print_grid(grid)`**:
    -   **Назначение**: Выводит текущую сетку на экран с разделителем.
    -   **Аргументы**:
        -   `grid` (list of lists of strings): Сетка для вывода.
    -   **Возвращаемое значение**: Нет.
    -   **Пример**:
        ```python
        grid = [['*', ' '], [' ', '*']]
        print_grid(grid)
         # Вывод:
         # *
         #  *
         # --
        ```
6.  **`count_live_neighbours(grid, row, col)`**:
    -   **Назначение**: Подсчитывает количество живых соседей у клетки с координатами `row`, `col`.
    -   **Аргументы**:
        -   `grid` (list of lists of strings): Игровая сетка.
        -   `row` (int): Индекс строки клетки.
        -   `col` (int): Индекс столбца клетки.
    -   **Возвращаемое значение**: `count` (int) - количество живых соседей.
    -   **Пример**:
        ```python
        grid = [['*', '*', ' '], ['*', ' ', '*'], [' ', '*', ' ']]
        live_neighbours = count_live_neighbours(grid, 1, 1) # Для клетки в центре
        print(live_neighbours) # Вывод: 4
        ```
7.  **`apply_rules(grid, row, col)`**:
    -   **Назначение**: Применяет правила игры "Жизнь" для клетки в позиции `row`, `col`.
    -   **Аргументы**:
        -   `grid` (list of lists of strings): Игровая сетка.
        -   `row` (int): Индекс строки клетки.
        -   `col` (int): Индекс столбца клетки.
    -   **Возвращаемое значение**: Состояние клетки в следующем поколении (`*` или ` `).
    -   **Пример**:
        ```python
        grid = [['*', '*', ' '], ['*', ' ', '*'], [' ', '*', ' ']]
        new_state = apply_rules(grid, 1, 1) # Для клетки в центре
        print(new_state) # Вывод: ' ' # Клетка умрет
        ```
8.  **`next_generation(grid)`**:
    -   **Назначение**: Создает новое поколение сетки на основе текущего.
    -   **Аргументы**:
        -   `grid` (list of lists of strings): Текущая игровая сетка.
    -   **Возвращаемое значение**: `new_grid` (list of lists of strings) - следующее поколение сетки.
    -   **Пример**:
        ```python
         grid = [['*', '*', ' '], ['*', ' ', '*'], [' ', '*', ' ']]
         next_grid = next_generation(grid)
         print(next_grid) # Вывод: [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
        ```
9.  **`play_game_of_life()`**:
    -   **Назначение**: Основная функция, управляющая симуляцией игры "Жизнь", выполняет ввод параметров, создает игровую сетку, симулирует поколения и выводит результаты.
    -   **Аргументы**: Нет.
    -   **Возвращаемое значение**: Нет.
    -   **Пример**:
        ```python
        play_game_of_life() #  запустит симуляцию игры
        ```
### Переменные

-   `rows`, `cols`: Целые числа, представляющие размеры сетки.
-   `generations`: Целое число, представляющее количество поколений для симуляции.
-   `grid`: Список списков строк, представляющий текущее состояние игрового поля.
-   `initial_config`: Список строк, представляющий начальную конфигурацию клеток.
-   `new_grid`: Список списков строк, представляющий сетку следующего поколения.
-   `count`: Целое число, представляющее количество живых соседей.
-   `live_neighbours`: Целое число, количество живых соседей для клетки.

### Потенциальные ошибки и области для улучшения
1. **Обработка ввода:**
     - В функциях `get_grid_size()` и `get_generations()` используется простой try-except для обработки ошибок ввода. Можно добавить проверку на максимальные значения, чтобы избежать избыточного потребления ресурсов.
2. **Производительность:** 
     - Для больших игровых полей и большого количества поколений, производительность может быть узким местом. Можно оптимизировать алгоритм подсчета живых соседей, например, кешировать результаты или использовать более эффективные структуры данных.
3. **Настройка:** 
     - Можно добавить возможность настраивать правила игры, цвет клеток, или другие визуальные эффекты.
4. **Начальная конфигурация:**
     -  Можно расширить возможность задавать начальную конфигурацию более гибко (например, загрузка из файла).

### Цепочка взаимосвязей
1. `play_game_of_life()` инициирует игру, вызывая `get_grid_size()` и `get_generations()` для получения параметров игры.
2. Затем `play_game_of_life()` вызывает `create_grid()` для создания начальной игровой сетки.
3. `play_game_of_life()` управляет циклом поколений, вызывая `print_grid()` для вывода текущего состояния и `next_generation()` для вычисления следующего поколения.
4. `next_generation()` в свою очередь использует `apply_rules()` для вычисления состояния каждой клетки, а `apply_rules()` использует `count_live_neighbours()` для подсчета соседей.
5. В конце `play_game_of_life()` снова вызывает `print_grid()` для вывода финального состояния поля.

Таким образом, функции образуют четкую цепочку взаимодействия, где каждая функция выполняет свою роль, обеспечивая работу всей симуляции.