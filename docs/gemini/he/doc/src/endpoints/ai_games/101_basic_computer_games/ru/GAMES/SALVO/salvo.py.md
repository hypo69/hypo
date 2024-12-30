# SALVO

## סקירה כללית

משחק "SALVO" הוא משחק קרב ימי בו השחקן מנסה להטביע את ספינות היריב הממוקמות על גבי רשת. השחקן מזין קואורדינטות לירות, והמשחק מודיע על פגיעה או החמצה. מטרת המשחק היא להטביע את כל ספינות היריב במספר המינימלי של מהלכים. המשחק מסתיים כאשר כל ספינות היריב טובעו.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [פונקציות](#פונקציות)
    - [create\_board](#create_board)
    - [place\_ships](#place_ships)
    - [is\_sunk](#is_sunk)
    - [print\_board](#print_board)
    - [play\_salvo](#play_salvo)

## פונקציות

### `create_board`

**תיאור**: יוצרת לוח משחק בגודל נתון, מלא באפסים.

**פרמטרים**:
- `size` (int): גודל לוח המשחק.

**החזרות**:
- `list[list[int]]`: לוח המשחק כמטריצה דו-ממדית.

```python
def create_board(size):
    """
    Args:
        size (int): גודל לוח המשחק.

    Returns:
        list[list[int]]: לוח המשחק כמטריצה דו-ממדית.
    """
```

### `place_ships`

**תיאור**: ממקמת באופן אקראי ספינות על לוח המשחק.

**פרמטרים**:
- `board` (list[list[int]]): לוח המשחק.
- `ships_lengths` (list[int]): רשימה של אורכי הספינות.

**החזרות**:
- `list[tuple[int, int, str, int]]`: רשימה של מיקומי הספינות, כולל שורה, עמודה, כיוון ואורך.

```python
def place_ships(board, ships_lengths):
    """
    Args:
        board (list[list[int]]): לוח המשחק.
        ships_lengths (list[int]): רשימה של אורכי הספינות.

    Returns:
        list[tuple[int, int, str, int]]: רשימה של מיקומי הספינות, כולל שורה, עמודה, כיוון ואורך.
    """
```

### `is_sunk`

**תיאור**: בודקת אם ספינה טובעה.

**פרמטרים**:
- `board` (list[list[str]]): לוח המשחק.
- `ship` (tuple[int, int, str, int]): מיקום ופרטי ספינה.

**החזרות**:
- `bool`: `True` אם הספינה טובעה, אחרת `False`.

```python
def is_sunk(board, ship):
    """
    Args:
        board (list[list[str]]): לוח המשחק.
        ship (tuple[int, int, str, int]): מיקום ופרטי ספינה.

    Returns:
        bool: True אם הספינה טובעה, אחרת False.
    """
```

### `print_board`

**תיאור**: מדפיסה את לוח המשחק לקונסולה, מסתירה את מיקומי הספינות.

**פרמטרים**:
- `board` (list[list[str | int]]): לוח המשחק.

**החזרות**:
- `None`: הפונקציה אינה מחזירה ערך.

```python
def print_board(board):
    """
    Args:
        board (list[list[str | int]]): לוח המשחק.

    Returns:
        None: הפונקציה אינה מחזירה ערך.
    """
```

### `play_salvo`

**תיאור**: הפונקציה הראשית של משחק Salvo.

**פרמטרים**:
- `None`: הפונקציה אינה מקבלת פרמטרים.

**החזרות**:
- `None`: הפונקציה אינה מחזירה ערך.

```python
def play_salvo():
    """
    Args:
        None: הפונקציה אינה מקבלת פרמטרים.

    Returns:
        None: הפונקציה אינה מחזירה ערך.
    """