# aceyducey.py

## סקירה כללית

קובץ זה מיישם את המשחק Acey Ducey, משחק קלפים פשוט בו שחקנים מהמרים האם קלף שלישי יהיה בין שני קלפים שהונחו.

## תוכן עניינים

- [פונקציות](#פונקציות)
  - [`create_deck`](#create_deck)
  - [`card_name`](#card_name)
  - [`play_acey_ducey`](#play_acey_ducey)

## פונקציות

### `create_deck`

**Description**: יוצר חפיסת קלפים חדשה.

**Parameters**:
- אין פרמטרים.

**Returns**:
- `list`: רשימה המייצגת את חפיסת הקלפים.

### `card_name`

**Description**: ממיר ערך קלף למחרוזת קריאה.

**Parameters**:
- `value` (int): ערך הקלף (2 עד 14).

**Returns**:
- `str`: מחרוזת המייצגת את שם הקלף (למשל, "2", "ואלט", "דאמה", "מלך", "טוס").

### `play_acey_ducey`

**Description**: מנהל את מחזור המשחק הראשי של Acey Ducey.

**Parameters**:
- אין פרמטרים.

**Returns**:
- אין ערך החזרה.

```markdown
# aceyducey.py

## סקירה כללית

קובץ זה מיישם את המשחק Acey Ducey, משחק קלפים פשוט בו שחקנים מהמרים האם קלף שלישי יהיה בין שני קלפים שהונחו.

## תוכן עניינים

- [פונקציות](#פונקציות)
  - [`create_deck`](#create_deck)
  - [`card_name`](#card_name)
  - [`play_acey_ducey`](#play_acey_ducey)

## פונקציות

### `create_deck`

**Description**: יוצר חפיסת קלפים חדשה.

**Parameters**:
- אין פרמטרים.

**Returns**:
- `list`: רשימה המייצגת את חפיסת הקלפים.

### `card_name`

**Description**: ממיר ערך קלף למחרוזת קריאה.

**Parameters**:
- `value` (int): ערך הקלף (2 עד 14).

**Returns**:
- `str`: מחרוזת המייצגת את שם הקלף (למשל, "2", "ואלט", "דאמה", "מלך", "טוס").

### `play_acey_ducey`

**Description**: מנהל את מחזור המשחק הראשי של Acey Ducey.

**Parameters**:
- אין פרמטרים.

**Returns**:
- אין ערך החזרה.

**Raises**:
- `ValueError`: אם הקלט של המשתמש אינו מספר שלם.