# Тетрис

## Обзор

Этот модуль содержит реализацию классической игры Тетрис с использованием библиотеки PyQt5. Игровое поле, фигуры и логика игры реализованы с использованием классов и методов.

## Содержание

- [Классы](#классы)
  - [Tetris](#tetris)
  - [Board](#board)
  - [Tetrominoe](#tetrominoe)
  - [Shape](#shape)
- [Функции](#функции)

## Классы

### `Tetris`

**Описание**:
Основной класс окна приложения Tetris.

**Methods**:
- [`__init__`](#__init__)
- [`initUI`](#initui)
- [`center`](#center)

#### `__init__`

```python
def __init__(self) -> None:
    """
    Args:
       
    Returns:
        None: 
    """
```

**Описание**:
Инициализация окна Tetris.

#### `initUI`

```python
def initUI(self) -> None:
    """
    Args:
        
    Returns:
        None:
    """
```

**Описание**:
Инициализация пользовательского интерфейса.

#### `center`

```python
def center(self) -> None:
    """
    Args:

    Returns:
        None: 
    """
```

**Описание**:
Центрирует окно на экране.

### `Board`

**Описание**:
Класс, представляющий игровое поле Tetris.

**Methods**:
- [`__init__`](#__init__-1)
- [`initBoard`](#initboard)
- [`shapeAt`](#shapeat)
- [`setShapeAt`](#setshapeat)
- [`squareWidth`](#squarewidth)
- [`squareHeight`](#squareheight)
- [`start`](#start)
- [`pause`](#pause)
- [`paintEvent`](#paintevent)
- [`keyPressEvent`](#keypressEvent)
- [`timerEvent`](#timerEvent)
- [`clearBoard`](#clearboard)
- [`dropDown`](#dropdown)
- [`oneLineDown`](#onelinedown)
- [`pieceDropped`](#piecedropped)
- [`removeFullLines`](#removefulllines)
- [`newPiece`](#newpiece)
- [`tryMove`](#trymove)
- [`drawSquare`](#drawsquare)

#### `__init__`

```python
def __init__(self, parent: QMainWindow) -> None:
    """
    Args:
        parent (QMainWindow): Родительское окно.
    Returns:
        None: 
    """
```

**Описание**:
Инициализация игрового поля.

#### `initBoard`

```python
def initBoard(self) -> None:
    """
    Args:

    Returns:
        None:
    """
```

**Описание**:
Инициализирует доску и игровые переменные.

#### `shapeAt`

```python
def shapeAt(self, x: int, y: int) -> int:
    """
    Args:
        x (int): Координата x.
        y (int): Координата y.

    Returns:
        int: Форма тетрамино в позиции.
    """
```

**Описание**:
Возвращает форму фигуры в заданной позиции.

#### `setShapeAt`

```python
def setShapeAt(self, x: int, y: int, shape: int) -> None:
    """
    Args:
        x (int): Координата x.
        y (int): Координата y.
        shape (int): Форма тетрамино.
    Returns:
        None: 
    """
```

**Описание**:
Устанавливает форму фигуры в заданной позиции.

#### `squareWidth`

```python
def squareWidth(self) -> int:
    """
    Args:
        
    Returns:
        int: Ширина квадрата.
    """
```

**Описание**:
Возвращает ширину одного квадрата.

#### `squareHeight`

```python
def squareHeight(self) -> int:
    """
    Args:
        
    Returns:
        int: Высота квадрата.
    """
```

**Описание**:
Возвращает высоту одного квадрата.

#### `start`

```python
def start(self) -> None:
    """
    Args:
        
    Returns:
        None:
    """
```

**Описание**:
Запускает игру.

#### `pause`

```python
def pause(self) -> None:
    """
    Args:

    Returns:
        None:
    """
```

**Описание**:
Ставит игру на паузу или возобновляет ее.

#### `paintEvent`

```python
def paintEvent(self, event: object) -> None:
    """
    Args:
         event (object): Событие отрисовки.

    Returns:
         None:
    """
```

**Описание**:
Отрисовывает игровое поле и текущую фигуру.

#### `keyPressEvent`

```python
def keyPressEvent(self, event: object) -> None:
    """
    Args:
        event (object): Событие нажатия клавиши.
    
    Returns:
        None:
    """
```

**Описание**:
Обрабатывает нажатия клавиш.

#### `timerEvent`

```python
def timerEvent(self, event: object) -> None:
    """
    Args:
        event (object): Событие таймера.

    Returns:
        None:
    """
```

**Описание**:
Обрабатывает события таймера.

#### `clearBoard`

```python
def clearBoard(self) -> None:
    """
    Args:

    Returns:
        None:
    """
```

**Описание**:
Очищает игровое поле.

#### `dropDown`

```python
def dropDown(self) -> None:
    """
    Args:

    Returns:
        None:
    """
```

**Описание**:
Опускает текущую фигуру до упора.

#### `oneLineDown`

```python
def oneLineDown(self) -> None:
    """
    Args:

    Returns:
        None:
    """
```

**Описание**:
Опускает текущую фигуру на одну линию.

#### `pieceDropped`

```python
def pieceDropped(self) -> None:
    """
    Args:

    Returns:
        None:
    """
```

**Описание**:
Фиксирует упавшую фигуру на поле.

#### `removeFullLines`

```python
def removeFullLines(self) -> None:
    """
    Args:

    Returns:
        None:
    """
```

**Описание**:
Удаляет полные линии и обновляет счетчик очков.

#### `newPiece`

```python
def newPiece(self) -> None:
    """
    Args:

    Returns:
        None:
    """
```

**Описание**:
Генерирует новую фигуру для игры.

#### `tryMove`

```python
def tryMove(self, newPiece: object, newX: int, newY: int) -> bool:
    """
    Args:
        newPiece (object): Новая форма фигуры.
        newX (int): Новая координата X.
        newY (int): Новая координата Y.

    Returns:
        bool: True, если перемещение успешно, иначе False.
    """
```

**Описание**:
Пытается переместить фигуру на новые координаты.

#### `drawSquare`

```python
def drawSquare(self, painter: QPainter, x: int, y: int, shape: int) -> None:
    """
    Args:
        painter (QPainter): Объект QPainter.
        x (int): Координата x.
        y (int): Координата y.
        shape (int): Форма тетрамино.

    Returns:
         None:
    """
```

**Описание**:
Рисует квадрат на игровом поле.

### `Tetrominoe`

**Описание**:
Перечисление всех возможных фигур тетрамино.

### `Shape`

**Описание**:
Класс, представляющий фигуру тетрамино.

**Methods**:
- [`__init__`](#__init__-2)
- [`shape`](#shape-1)
- [`setShape`](#setshape)
- [`setRandomShape`](#setrandomshape)
- [`x`](#x)
- [`y`](#y)
- [`setX`](#setx)
- [`setY`](#sety)
- [`minX`](#minx)
- [`maxX`](#maxx)
- [`minY`](#miny)
- [`maxY`](#maxy)
- [`rotateLeft`](#rotateleft)
- [`rotateRight`](#rotateright)

#### `__init__`

```python
def __init__(self) -> None:
    """
    Args:

    Returns:
        None:
    """
```

**Описание**:
Инициализация фигуры тетрамино.

#### `shape`

```python
def shape(self) -> int:
    """
    Args:
        
    Returns:
        int: Форма фигуры.
    """
```

**Описание**:
Возвращает форму фигуры.

#### `setShape`

```python
def setShape(self, shape: int) -> None:
    """
    Args:
        shape (int): Форма тетрамино.

    Returns:
        None:
    """
```

**Описание**:
Устанавливает форму фигуры.

#### `setRandomShape`

```python
def setRandomShape(self) -> None:
    """
    Args:

    Returns:
        None:
    """
```

**Описание**:
Устанавливает случайную форму фигуры.

#### `x`

```python
def x(self, index: int) -> int:
    """
    Args:
        index (int): Индекс точки фигуры.

    Returns:
        int: Координата x.
    """
```

**Описание**:
Возвращает координату x для заданной точки фигуры.

#### `y`

```python
def y(self, index: int) -> int:
    """
    Args:
        index (int): Индекс точки фигуры.
    
    Returns:
        int: Координата y.
    """
```

**Описание**:
Возвращает координату y для заданной точки фигуры.

#### `setX`

```python
def setX(self, index: int, x: int) -> None:
    """
    Args:
        index (int): Индекс точки фигуры.
        x (int): Новая координата x.
    
    Returns:
        None:
    """
```

**Описание**:
Устанавливает координату x для заданной точки фигуры.

#### `setY`

```python
def setY(self, index: int, y: int) -> None:
    """
    Args:
        index (int): Индекс точки фигуры.
        y (int): Новая координата y.

    Returns:
        None:
    """
```

**Описание**:
Устанавливает координату y для заданной точки фигуры.

#### `minX`

```python
def minX(self) -> int:
    """
    Args:
        
    Returns:
        int: Минимальная координата x.
    """
```

**Описание**:
Возвращает минимальную координату x для фигуры.

#### `maxX`

```python
def maxX(self) -> int:
    """
    Args:
        
    Returns:
        int: Максимальная координата x.
    """
```

**Описание**:
Возвращает максимальную координату x для фигуры.

#### `minY`

```python
def minY(self) -> int:
    """
    Args:
        
    Returns:
        int: Минимальная координата y.
    """
```

**Описание**:
Возвращает минимальную координату y для фигуры.

#### `maxY`

```python
def maxY(self) -> int:
    """
    Args:
        
    Returns:
        int: Максимальная координата y.
    """
```

**Описание**:
Возвращает максимальную координату y для фигуры.

#### `rotateLeft`

```python
def rotateLeft(self) -> object:
    """
    Args:

    Returns:
        object: Новая фигура после поворота.
    """
```

**Описание**:
Поворачивает фигуру на 90 градусов влево.

#### `rotateRight`

```python
def rotateRight(self) -> object:
    """
    Args:
    
    Returns:
        object: Новая фигура после поворота.
    """
```

**Описание**:
Поворачивает фигуру на 90 градусов вправо.

## Функции
Нет функций вне классов в этом модуле.