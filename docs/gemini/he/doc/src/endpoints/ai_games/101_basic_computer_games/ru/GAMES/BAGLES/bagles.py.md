# BAGLES

## סקירה כללית

המשחק "בייגלס" הוא משחק היגיון וחידה בו השחקן מנסה לנחש מספר תלת-ספרתי המורכב מספרות ייחודיות. לאחר כל ניסיון, השחקן מקבל רמזים: "PICO" אומר שאחת הספרות נכונה ובמיקום הנכון, "FERMI" אומר שאחת הספרות נכונה אך לא במיקום הנכון, "BAGELS" אומר שאף אחת מהספרות לא נכונה.

## תוכן עניינים

1. [פונקציות](#functions)
    - [`generate_secret_number`](#generate_secret_number)
    - [`get_clues`](#get_clues)
    - [`play_bagels`](#play_bagels)

## פונקציות

### `generate_secret_number`

**Description**:
הפונקציה מייצרת מספר תלת-ספרתי רנדומלי עם ספרות ייחודיות.

**Parameters**:
אין פרמטרים.

**Returns**:
- `str`: מחזירה מחרוזת המייצגת את המספר התלת-ספרתי.

### `get_clues`

**Description**:
הפונקציה יוצרת רמזים PICO, FERMI ו-BAGELS על סמך השוואה בין המספר הסודי לניחוש המשתמש.

**Parameters**:
- `secret_number` (str): המספר הסודי.
- `user_guess` (str): ניחוש המשתמש.

**Returns**:
- `list`: מחזירה רשימה של רמזים ("PICO", "FERMI", "BAGELS").

### `play_bagels`

**Description**:
מכילה את ההיגיון המרכזי של משחק הבייגלס.

**Parameters**:
אין פרמטרים.

**Returns**:
אין ערך מוחזר.

**Raises**:
אין חריגות שזורקות במפורש.

```