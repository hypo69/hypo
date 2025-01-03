# Анализ кода модуля ROCKET

**Качество кода**
9
-  Плюсы
    -   Документ хорошо структурирован и понятен.
    -   Подробно описаны правила игры, шаги реализации, примеры работы и возможные ограничения.
    -   Предложены идеи для улучшения игры.
-  Минусы
    -   Отсутствует код реализации игры.
    -   Не все разделы имеют одинаковую глубину проработки (например, "Реализация" и "Рекомендуемые улучшения" довольно краткие).

**Рекомендации по улучшению**
1.  **Добавить реализацию игры**:
    -   На основе предоставленной пошаговой инструкции и требований нужно добавить код на Python.
    -   Разделить код на функции для лучшей организации.
2.  **Дополнить разделы "Реализация" и "Рекомендуемые улучшения"**:
    -   В разделе "Реализация" можно привести примеры кода для работы с сеткой, проверки ввода и т.д.
    -   В разделе "Рекомендуемые улучшения" можно более детально описать предложенные улучшения и добавить новые (например, сохранение истории ходов).
3. **Форматирование кода:**
    -   Добавить подсветку синтаксиса для кода в примерах (например, использовать ```python```).
4. **Добавить обработку ошибок**:
   - Добавить обработку ошибок ввода пользователя, чтобы игра не завершалась аварийно.

**Оптимизированный код**
```markdown
### Название игры: **ROCKET** (Ракета)

---

#### Описание
**ROCKET** — это стратегическая игра, в которой игроки управляют космическими кораблями (ракетами), стремясь первыми достичь цели — орбиты планеты. Игроки по очереди перемещают свои ракеты по сетке, избегая препятствий и пытаясь опередить соперника. Игра заканчивается, когда один из игроков достигает орбиты планеты.

---

### Пошаговая инструкция для реализации

#### 1. **Инициализация игры**
   - Программа выводит приветственное сообщение и объясняет правила:
     ```
     Добро пожаловать в ROCKET!
     Ваша задача — первым достичь орбиты планеты, перемещая свою ракету по сетке.
     Игра продолжается до тех пор, пока один из игроков не достигнет орбиты или пока не будет достигнуто максимальное количество ходов.
     Удачи!
     ```

   - Программа создаёт игровую сетку размером 10x10.
   - Ракеты двух игроков размещаются на противоположных концах сетки (например, ракета Игрока 1 на клетке A1, а ракета Игрока 2 на клетке J10).
   - На сетке случайным образом размещаются препятствия (например, астероиды), которые нельзя пересекать.
   - Игроки поочерёдно делают ходы, перемещая свои ракеты.

---

#### 2. **Основной процесс игры**

##### **2.1. Ход игрока:**
   - Игрок выбирает направление и количество клеток, на которое хочет переместить свою ракету (например, вверх на 2 клетки).
   - Программа проверяет, является ли ход допустимым:
     - Ракета не может перемещаться за пределы сетки.
     - Ракета не может перемещаться на клетку с препятствием.
     - Ракета не может перемещаться на клетку, занятую ракетой соперника.

   - Если ход допустим, программа перемещает ракету и отображает текущее состояние сетки:
     ```
     Текущее состояние сетки:
     A B C D E F G H I J
     1 [R][ ][ ][ ][ ][ ][ ][ ][ ][ ]
     2 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
     3 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
     4 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
     5 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
     6 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
     7 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
     8 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
     9 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
    10 [ ][ ][ ][ ][ ][ ][ ][ ][ ][R]
     ```

   - Если ход недопустим, программа сообщает об ошибке и предлагает игроку повторить ход:
     ```
     Недопустимый ход. Попробуйте снова.
     ```

##### **2.2. Проверка условий победы:**
   - После каждого хода программа проверяет, достигла ли ракета игрока орбиты планеты.
   - Если ракета достигла орбиты, программа объявляет победителя:
     ```
     Игра окончена! Победил Игрок 1.
     ```

##### **2.3. Проверка условий завершения игры:**
   - Игра заканчивается, если достигнуто максимальное количество ходов (например, 20 ходов).
   - Программа объявляет ничью:
     ```
     Игра окончена! Ничья.
     ```

---

#### 3. **Завершение игры**
   - После завершения игры программа предлагает сыграть снова:
     ```
     Хотите сыграть снова? (да/нет)
     ```

   - Если игрок выбирает "да", игра начинается заново с новой расстановкой ракет и препятствий.

---

### Пример работы программы

1. **Начало игры:**
   ```
   Добро пожаловать в ROCKET!
   Игрок 1, ваш ход.
   Введите направление и количество клеток для перемещения ракеты (например, вверх 2):
   > вверх 2
   Ракета Игрока 1 перемещена на клетку A3.
   ```

2. **Игровой процесс:**
   ```
   Игрок 2, ваш ход.
   Введите направление и количество клеток для перемещения ракеты:
   > вниз 1
   Ракета Игрока 2 перемещена на клетку J9.

   Игрок 1, ваш ход.
   Введите направление и количество клеток для перемещения ракеты:
   > вправо 3
   Ракета Игрока 1 перемещена на клетку D3.
   ```

3. **Завершение игры:**
   ```
   Игра окончена! Победил Игрок 1.
   Хотите сыграть снова? (да/нет):
   > нет
   Спасибо за игру!
   ```

---

### Возможные ограничения
- Игрок должен вводить направление и количество клеток в правильном формате.
- Программа должна обрабатывать неверный ввод и предлагать повторить попытку.
- Ракеты не могут перемещаться за пределы сетки или на клетки с препятствиями.

---

### Реализация
Игра может быть реализована на Python с использованием следующих возможностей:
- **Массивы или списки** для представления сетки и положения ракет.
- **Циклы и условия** для проверки ввода игрока и обработки его ходов.
- **Функции** для проверки условий победы и завершения игры.

Пример реализации:
```python
import random

def create_grid(size=10):
    """
    Создает игровую сетку заданного размера.

    :param size: Размер сетки (по умолчанию 10).
    :return: Двумерный список, представляющий игровую сетку.
    """
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    return grid

def place_rockets(grid):
    """
    Размещает ракеты игроков на сетке.

    :param grid: Игровая сетка.
    :return: Кортеж с координатами ракет (x1, y1), (x2, y2).
    """
    grid[0][0] = 'R1' # Ракета 1 в верхнем левом углу
    grid[-1][-1] = 'R2' # Ракета 2 в нижнем правом углу
    return (0, 0), (len(grid)-1, len(grid)-1)

def place_obstacles(grid, num_obstacles=10):
   """
   Размещает препятствия (астероиды) на сетке.

   :param grid: Игровая сетка.
   :param num_obstacles: Количество препятствий (по умолчанию 10).
   """
   size = len(grid)
   obstacles_placed = 0
   while obstacles_placed < num_obstacles:
       x, y = random.randint(0, size - 1), random.randint(0, size - 1)
       if grid[x][y] == ' ':
           grid[x][y] = 'X' # X - препятствие (астероид)
           obstacles_placed += 1

def print_grid(grid):
   """
   Выводит текущее состояние сетки в консоль.

   :param grid: Игровая сетка.
   """
   print("  ", end="")
   for i in range(len(grid)):
       print(chr(65 + i), end=" ") # Печать буквенных координат (A, B, C...)
   print()
   for i, row in enumerate(grid):
       print(i + 1, end=" ") # Печать числовых координат (1, 2, 3...)
       for cell in row:
           print(f"[{cell}]", end="")
       print()

def get_move(current_player):
   """
   Запрашивает у игрока направление и количество клеток для перемещения ракеты.

   :param current_player: Номер текущего игрока (1 или 2).
   :return: Строка, содержащая ввод игрока.
   """
   return input(f"Игрок {current_player}, введите направление и количество клеток (например, вверх 2): ")

def validate_move(grid, rocket_pos, move, other_rocket_pos):
    """
    Проверяет, является ли ход допустимым.

    :param grid: Игровая сетка.
    :param rocket_pos: Текущая позиция ракеты (x, y).
    :param move: Ввод игрока (например, "вверх 2").
    :param other_rocket_pos: Позиция ракеты соперника (x, y).
    :return: Кортеж (True, new_pos) если ход допустим, (False, None) если нет.
    """
    size = len(grid)
    parts = move.lower().split()
    if len(parts) != 2:
      print("Неверный формат ввода. Пример: вверх 2")
      return False, None
    direction, steps = parts
    try:
      steps = int(steps)
    except ValueError:
      print("Неверное количество шагов. Введите целое число.")
      return False, None

    x, y = rocket_pos
    new_x, new_y = x, y

    if direction == 'вверх':
        new_x -= steps
    elif direction == 'вниз':
        new_x += steps
    elif direction == 'влево':
        new_y -= steps
    elif direction == 'вправо':
        new_y += steps
    else:
        print("Неверное направление. Используйте: вверх, вниз, влево, вправо.")
        return False, None

    if not (0 <= new_x < size and 0 <= new_y < size):
        print("Ход выходит за пределы сетки.")
        return False, None
    if grid[new_x][new_y] == 'X':
        print("Ход на препятствие.")
        return False, None
    if (new_x, new_y) == other_rocket_pos:
        print("Ход на клетку, занятую ракетой соперника.")
        return False, None
    return True, (new_x, new_y)

def make_move(grid, rocket_pos, new_pos, player):
  """
  Перемещает ракету на новое место.

  :param grid: Игровая сетка.
  :param rocket_pos: Текущая позиция ракеты (x, y).
  :param new_pos: Новая позиция ракеты (x, y).
  :param player: Номер игрока (1 или 2).
  """
  x, y = rocket_pos
  grid[x][y] = ' '
  new_x, new_y = new_pos
  grid[new_x][new_y] = f'R{player}'

def check_win(grid, rocket_pos, player):
  """
  Проверяет, достиг ли игрок орбиты планеты.

  :param grid: Игровая сетка.
  :param rocket_pos: Текущая позиция ракеты (x, y).
  :param player: Номер игрока (1 или 2).
  :return: True, если игрок победил, False если нет.
  """
  size = len(grid)
  if player == 1:
     return rocket_pos[0] == size - 1
  if player == 2:
     return rocket_pos[0] == 0
  return False

def play_rocket():
    """
    Запускает игру ROCKET.
    """
    print("Добро пожаловать в ROCKET!")
    print("Ваша задача — первым достичь орбиты планеты, перемещая свою ракету по сетке.")
    print("Игра продолжается до тех пор, пока один из игроков не достигнет орбиты или пока не будет достигнуто максимальное количество ходов.")
    print("Удачи!")
    max_moves = 20
    while True:
        grid = create_grid()
        rocket1_pos, rocket2_pos = place_rockets(grid)
        place_obstacles(grid)
        moves_count = 0
        current_player = 1

        while moves_count < max_moves:
            print_grid(grid)
            move = get_move(current_player)
            if current_player == 1:
                is_valid, new_pos = validate_move(grid, rocket1_pos, move, rocket2_pos)
                if is_valid:
                   make_move(grid, rocket1_pos, new_pos, current_player)
                   rocket1_pos = new_pos
                   if check_win(grid, rocket1_pos, current_player):
                      print_grid(grid)
                      print(f"Игра окончена! Победил Игрок {current_player}.")
                      break
                   current_player = 2
                   moves_count += 1
                else:
                   print("Недопустимый ход. Попробуйте снова.")
            elif current_player == 2:
                is_valid, new_pos = validate_move(grid, rocket2_pos, move, rocket1_pos)
                if is_valid:
                  make_move(grid, rocket2_pos, new_pos, current_player)
                  rocket2_pos = new_pos
                  if check_win(grid, rocket2_pos, current_player):
                     print_grid(grid)
                     print(f"Игра окончена! Победил Игрок {current_player}.")
                     break
                  current_player = 1
                  moves_count += 1
                else:
                  print("Недопустимый ход. Попробуйте снова.")
        if moves_count == max_moves:
            print("Игра окончена! Ничья.")
        play_again = input("Хотите сыграть снова? (да/нет): ")
        if play_again.lower() != "да":
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
   play_rocket()

```

---

### Рекомендуемые улучшения
- Добавить возможность игры с компьютером.
- Реализовать графический интерфейс для визуализации сетки и ходов.
- Добавить возможность выбора размера сетки (например, 8x8 или 12x12).
- Добавить сохранение истории ходов.
- Улучшить ввод, например, с помощью отдельных полей ввода для направления и количества клеток.
- Сделать более гибким добавление препятствий.
```