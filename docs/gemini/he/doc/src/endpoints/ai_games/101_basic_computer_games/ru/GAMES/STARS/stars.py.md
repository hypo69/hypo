# STARS

## סקירה כללית

משחק הטקסט "כוכבים" בו השחקן שולט על מיקום "כוכב" על המסך על ידי הזנת פקודות להזזתו. מטרת המשחק היא להזיז את הכוכב לפינה הימנית התחתונה של המסך.

## תוכן עניינים

1. [סקירה כללית](#סקירה-כללית)
2. [פונקציות](#פונקציות)
    - [`printBoard`](#printboard)
    - [`updatePosition`](#updateposition)

## פונקציות

### `printBoard`

**Description**:
מדפיס את לוח המשחק עם מיקום הכוכב הנוכחי.

**Parameters**:
- `starRow` (int): השורה שבה הכוכב נמצא.
- `starCol` (int): העמודה שבה הכוכב נמצא.

**Returns**:
- None

**Raises**:
- None

```python
def printBoard(starRow, starCol):
    """
    Args:
        starRow (int): שורה בה נמצא הכוכב.
        starCol (int): עמודה בה נמצא הכוכב.

    Returns:
        None: פונקציה זו לא מחזירה דבר.

    Raises:
        None: לא נזרקות חריגות.
    """
    for row in range(1, boardSize + 1):
        line = ""
        for col in range(1, boardSize + 1):
            if row == starRow and col == starCol:
                line += "*"  # הצגת כוכב
            else:
                line += "."  # הצגת משבצת ריקה
        print(line)
```

### `updatePosition`

**Description**:
מעדכן את מיקום הכוכב על סמך הפקודה שהוזנה.

**Parameters**:
- `command` (str): פקודת התנועה ('R', 'L', 'U', 'D').
- `starRow` (int): השורה הנוכחית של הכוכב.
- `starCol` (int): העמודה הנוכחית של הכוכב.

**Returns**:
- `tuple (int, int)`: שורה ועמודה חדשות של הכוכב.

**Raises**:
- None

```python
def updatePosition(command, starRow, starCol):
    """
    Args:
        command (str): פקודת התנועה ('R', 'L', 'U', 'D').
        starRow (int): שורה נוכחית של הכוכב.
        starCol (int): עמודה נוכחית של הכוכב.

    Returns:
        tuple (int, int): שורה ועמודה חדשות של הכוכב.

    Raises:
        None: לא נזרקות חריגות.
    """
    if command == 'R':  # תנועה ימינה
        if starCol < boardSize:
           starCol += 1
    elif command == 'L':  # תנועה שמאלה
        if starCol > 1:
            starCol -= 1
    elif command == 'U':  # תנועה למעלה
        if starRow > 1:
            starRow -= 1
    elif command == 'D':  # תנועה למטה
        if starRow < boardSize:
            starRow += 1
    return starRow, starCol