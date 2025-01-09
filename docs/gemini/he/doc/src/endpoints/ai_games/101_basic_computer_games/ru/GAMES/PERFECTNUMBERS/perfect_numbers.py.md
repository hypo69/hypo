# perfect_numbers.py

## סקירה כללית

המודול הזה מכיל פונקציות לחישוב וזיהוי מספרים מושלמים בטווח נתון. מספר מושלם הוא מספר שלם חיובי ששווה לסכום המחלקים החיוביים שלו, מלבד עצמו.

## תוכן עניינים

- [פונקציות](#פונקציות)
  - [`sum_of_divisors`](#sum_of_divisors)
  - [`is_perfect_number`](#is_perfect_number)
  - [`find_perfect_numbers`](#find_perfect_numbers)

## פונקציות

### `sum_of_divisors`

**Description**: מחשבת את סכום המחלקים הנכונים של המספר `n`.

**Parameters**:
- `n` (int): מספר שלם.

**Returns**:
- `int`: סכום המחלקים הנכונים של המספר `n`.

### `is_perfect_number`

**Description**: בודקת האם מספר `n` הוא מספר מושלם.

**Parameters**:
- `n` (int): מספר שלם.

**Returns**:
- `bool`: `True` אם המספר `n` מושלם, אחרת `False`.

### `find_perfect_numbers`

**Description**: מוצאת את כל המספרים המושלמים בטווח הנתון.

**Parameters**:
- `limit` (int): הגבול העליון של הטווח (כולל).

**Returns**:
- `list[int]`: רשימה של כל המספרים המושלמים בטווח שבין 1 ל-`limit`.