# ace.py

## סקירה כללית

קובץ זה מיישם את המשחק "ACE", משחק קלפים בו שני שחקנים מחליפים קלפים מתוך חפיסה, ומנסים לצבור את הניקוד הגבוה ביותר. 

## תוכן עניינים

- [פונקציות](#פונקציות)
  - [`calculate_card_value`](#calculate_card_value)
  - [`draw_card`](#draw_card)
  - [`play_ace_game`](#play_ace_game)

## פונקציות

### `calculate_card_value`

**Description**: מחשבת את ערך הקלף. אס שווה 1, נסיך, מלכה ומלך שווים 10, וכל השאר לפי הערך הנקוב.

**Parameters**:
- `card` (str): הקלף שערכו יחושב.

**Returns**:
- `int`: הערך המספרי של הקלף.

**Raises**:
- `ValueError`: אם הקלף לא מזוהה כערך מספרי.

```python
def calculate_card_value(card):
    """
    Args:
        card (str): הקלף שערכו יחושב.
    Returns:
        int: הערך המספרי של הקלף.
    Raises:
        ValueError: אם הקלף לא מזוהה כערך מספרי.
    """
```

### `draw_card`

**Description**: מוציאה קלף אקראי מחפיסת קלפים.

**Parameters**:
- `deck` (list): חפיסת הקלפים ממנה יש להוציא קלף.

**Returns**:
- `tuple[str, int]`: הקלף שהוצא וערכו.

```python
def draw_card(deck):
    """
    Args:
        deck (list): חפיסת הקלפים ממנה יש להוציא קלף.
    Returns:
        tuple[str, int]: הקלף שהוצא וערכו.
    """
```

### `play_ace_game`

**Description**: הפונקציה הראשית שמפעילה את משחק ה ACE.

**Parameters**:
- אין פרמטרים.

**Returns**:
- `None`: הפונקציה לא מחזירה דבר, אלא מדפיסה את תוצאות המשחק.

**Raises**:
- `ValueError`: אם המשתמש לא מכניס מספר שלם תקין עבור כמות הסיבובים.

```python
def play_ace_game():
    """
    Args:
        
    Returns:
        None: הפונקציה לא מחזירה דבר, אלא מדפיסה את תוצאות המשחק.
    Raises:
        ValueError: אם המשתמש לא מכניס מספר שלם תקין עבור כמות הסיבובים.
    """