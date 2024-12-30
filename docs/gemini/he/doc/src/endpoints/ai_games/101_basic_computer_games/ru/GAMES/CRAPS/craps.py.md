# craps.py

## סקירה כללית

קובץ זה מיישם את המשחק "קראפס", משחק קוביות בו השחקן מהמר על תוצאות הטלת שתי קוביות. במשחק ישנם חוקים מוגדרים לניצחון או הפסד, ומשתמשים בו בסיבובים שונים, עד שהמשחק מסתיים.

## תוכן עניינים

- [פונקציות](#Functions)
    - [`roll_dice`](#roll_dice)
    - [`calculate_sum`](#calculate_sum)
    - [`play_craps`](#play_craps)

## Functions

### `roll_dice`

**Description**: מטיל שתי קוביות משחק ומחזיר את הערכים שלהן.

**Parameters**:
- None

**Returns**:
- `tuple[int, int]`: טאפל המכיל את הערכים של שתי הקוביות.

### `calculate_sum`

**Description**: מחשב את סכום הערכים של שתי קוביות.

**Parameters**:
- `dice1` (int): הערך של הקובייה הראשונה.
- `dice2` (int): הערך של הקובייה השנייה.

**Returns**:
- `int`: סכום הערכים של שתי הקוביות.

### `play_craps`

**Description**: מפעיל את משחק הקראפס.

**Parameters**:
- None

**Returns**:
- None: הפונקציה מדפיסה תוצאות למסוף ואינה מחזירה ערך.