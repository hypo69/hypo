# משחק סוסים

## Обзор

קובץ זה מיישם משחק מרוץ סוסים פשוט, בו השחקן בוחר סוס וצופה במרוץ בין מספר סוסים. המשחק מסתיים כאשר אחד הסוסים מגיע לקו הסיום, והשחקן זוכה אם בחר בסוס המנצח.

## Содержание

- [פונקציות](#פונקציות)
    - [`play_horses_game`](#play_horses_game)
    - [`print_track`](#print_track)
    - [`check_winner`](#check_winner)
- [משתנים גלובליים](#משתנים-גלובליים)

## פונקציות

### `play_horses_game`

**תיאור**: מפעיל את משחק מרוץ הסוסים, כולל קבלת קלט מהמשתמש, אתחול המשחק, וביצוע המרוץ עד לקביעת מנצח.

**פרמטרים**: אין

**ערך מוחזר**: אין

**מעלה שגיאות**: אין

### `print_track`

**תיאור**: מדפיס את מצב המסלול, כאשר כל סוס מיוצג על ידי מספרו.

**פרמטרים**:
- `horse_positions` (list): רשימה של מיקום כל סוס.

**ערך מוחזר**: אין

**מעלה שגיאות**: אין

### `check_winner`

**תיאור**: בודק האם יש מנצח ומחזיר את מספר הסוס המנצח, אם קיים.

**פרמטרים**:
- `horse_positions` (list): רשימה של מיקום כל סוס.

**ערך מוחזר**:
- `int | None`: מספר הסוס המנצח, אם קיים, אחרת None.

**מעלה שגיאות**: אין

## משתנים גלובליים

-   `NUM_HORSES`: מספר הסוסים המשתתפים במרוץ (קבוע: 4).
-   `TRACK_LENGTH`: אורך המסלול של המרוץ (קבוע: 20).