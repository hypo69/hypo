# bingo.py

## סקירה כללית

מודול זה מיישם משחק בינגו פשוט. המשחק יוצר כרטיס בינגו 5x5 עם מספרים אקראיים מ-1 עד 75 (לא כולל כפולות של 10), ומציג את המספרים האקראיים עד שכל המספרים בכרטיס סומנו.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [פונקציות](#פונקציות)
    - [`create_bingo_card`](#create_bingo_card)
    - [`print_bingo_card`](#print_bingo_card)
    - [`mark_number`](#mark_number)
    - [`is_bingo`](#is_bingo)
    - [`play_bingo`](#play_bingo)

## פונקציות

### `create_bingo_card`

**תיאור**: יוצר ומחזיר כרטיס בינגו 5x5.

הכרטיס מכיל מספרים אקראיים וייחודיים בין 1 ל-75, לא כולל מספרים שהם כפולות של 10.

**Returns**:
- `list of lists`: כרטיס בינגו.

```python
def create_bingo_card() -> list[list[int]]:
    """
    Args:
        None

    Returns:
        list of lists: כרטיס בינגו.
    """
```

### `print_bingo_card`

**תיאור**: מדפיס את כרטיס הבינגו לקונסולה.

**Parameters**:
- `card` (list of lists): כרטיס הבינגו להדפסה.

```python
def print_bingo_card(card: list[list[int]]) -> None:
    """
    Args:
        card (list of lists): כרטיס הבינגו להדפסה.

    Returns:
        None
    """
```

### `mark_number`

**תיאור**: מסמן מספר בכרטיס הבינגו על ידי החלפתו ב-0.

**Parameters**:
- `card` (list of lists): כרטיס הבינגו.
- `number` (int): המספר לסימון.

```python
def mark_number(card: list[list[int]], number: int) -> None:
    """
    Args:
        card (list of lists): כרטיס הבינגו.
        number (int): המספר לסימון.

    Returns:
        None
    """
```

### `is_bingo`

**תיאור**: בודק האם כל המספרים בכרטיס הבינגו סומנו (הוחלפו ב-0).

**Parameters**:
- `card` (list of lists): כרטיס הבינגו לבדיקה.

**Returns**:
- `bool`: True אם כל המספרים סומנו, אחרת False.

```python
def is_bingo(card: list[list[int]]) -> bool:
    """
    Args:
        card (list of lists): כרטיס הבינגו לבדיקה.

    Returns:
        bool: True אם כל המספרים סומנו, אחרת False.
    """
```

### `play_bingo`

**תיאור**: מריץ את משחק הבינגו.

יוצר כרטיס בינגו, מדפיס אותו, ומבקש מהמשתמש להזין מספרים. המשחק מסתיים כאשר כל המספרים בכרטיס סומנו.

```python
def play_bingo() -> None:
    """
    Args:
        None

    Returns:
        None
    """