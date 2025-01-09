# `bingo.py`

## סקירה כללית

קובץ זה מיישם משחק בינגו בסיסי. המשחק יוצר לוח בינגו אקראי 5x5 עם מספרים מ-1 עד 75 (לא כולל כפולות של 10). המשחק ממשיך עד שכל המספרים בלוח מסומנים, ומכריז על ניצחון.

## תוכן עניינים

1. [פונקציות](#פונקציות)
    - [`create_bingo_card`](#create_bingo_card)
    - [`print_bingo_card`](#print_bingo_card)
    - [`mark_number`](#mark_number)
    - [`is_bingo`](#is_bingo)
    - [`play_bingo`](#play_bingo)

## פונקציות

### `create_bingo_card`

**Description**: יוצר ומחזיר כרטיס בינגו 5x5. הכרטיס מכיל מספרים אקראיים ייחודיים מ-1 עד 75, לא כולל מספרים שהם כפולות של 10.

**Parameters**:
- אין

**Returns**:
- `list of lists`: כרטיס בינגו.

### `print_bingo_card`

**Description**: מדפיס את כרטיס הבינגו לקונסולה.

**Parameters**:
- `card` (list of lists): כרטיס הבינגו להדפסה.

**Returns**:
- אין

### `mark_number`

**Description**: מסמן מספר בכרטיס בינגו, מחליף אותו ב-0.

**Parameters**:
- `card` (list of lists): כרטיס הבינגו.
- `number` (int): המספר לסימון.

**Returns**:
- אין

### `is_bingo`

**Description**: בודק האם כל המספרים בכרטיס הבינגו סומנו (הוחלפו ב-0).

**Parameters**:
- `card` (list of lists): כרטיס הבינגו לבדיקה.

**Returns**:
- `bool`: `True` אם כל המספרים סומנו, אחרת `False`.

### `play_bingo`

**Description**: מפעיל את משחק הבינגו. יוצר כרטיס בינגו, מדפיס אותו למסך, ומבקש מהמשתמש להזין מספרים. המשחק נגמר כאשר כל המספרים בכרטיס מסומנים.

**Parameters**:
- אין

**Returns**:
- אין