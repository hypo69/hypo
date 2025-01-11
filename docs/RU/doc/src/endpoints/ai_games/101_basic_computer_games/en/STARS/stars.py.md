# STARS

## Обзор

Игра "Звезды" - это простая текстовая игра, в которой игрок управляет положением звезды на экране, вводя команды для ее перемещения. Цель игры - переместить звезду в правый нижний угол экрана.

## Оглавление

1. [Обзор](#обзор)
2. [Функции](#функции)
    - [`printBoard`](#printboard)
    - [`updatePosition`](#updateposition)

## Функции

### `printBoard`

**Описание**: Выводит на экран игровое поле с текущей позицией звезды.

**Параметры**:
- `starRow` (int): Строка, в которой находится звезда.
- `starCol` (int): Столбец, в котором находится звезда.

**Возвращает**:
- `None`: Функция ничего не возвращает.

```python
def printBoard(starRow, starCol):
  """
  Выводит на экран игровое поле с текущей позицией звезды.
  Аргументы:
    starRow (int): строка, в которой находится звезда.
    starCol (int): столбец, в котором находится звезда.
  """
  for row in range(1, boardSize + 1):
    line = ""
    for col in range(1, boardSize + 1):
      if row == starRow and col == starCol:
        line += "*"  # Отображаем звезду
      else:
        line += "."  # Отображаем пустую клетку
    print(line)
```

### `updatePosition`

**Описание**: Обновляет позицию звезды на основе введенной команды.

**Параметры**:
- `command` (str): Команда перемещения ('R', 'L', 'U', 'D').
- `starRow` (int): Текущая строка звезды.
- `starCol` (int): Текущий столбец звезды.

**Возвращает**:
- `tuple(int, int)`: Новая строка и столбец звезды.

```python
def updatePosition(command, starRow, starCol):
    """
    Обновляет позицию звезды на основе введенной команды.
    Аргументы:
        command (str): команда перемещения ('R', 'L', 'U', 'D').
        starRow (int): текущая строка звезды.
        starCol (int): текущий столбец звезды.
    Возвращает:
        tuple (int, int): новая строка и столбец звезды.
    """
    if command == 'R':  # Двигаемся вправо
        if starCol < boardSize:
           starCol += 1
    elif command == 'L':  # Двигаемся влево
        if starCol > 1:
            starCol -= 1
    elif command == 'U':  # Двигаемся вверх
        if starRow > 1:
            starRow -= 1
    elif command == 'D':  # Двигаемся вниз
        if starRow < boardSize:
            starRow += 1
    return starRow, starCol
```