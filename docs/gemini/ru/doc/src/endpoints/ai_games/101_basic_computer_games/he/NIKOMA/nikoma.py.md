# משחק בייגלס

## Обзор

קובץ זה מיישם את המשחק "בייגלס", משחק לוגי שבו השחקן מנסה לנחש מספר בן שלוש ספרות שונות. המשחק מספק רמזים לאחר כל ניחוש: "Fermi" אם ספרה אחת נכונה ובמיקום הנכון, "Pico" אם ספרה אחת נכונה אך לא במיקום הנכון, ו-"Bagels" אם אף ספרה לא נכונה.

## תוכן עניינים

- [פונקציות](#פונקציות)
  - [`generate_unique_3_digit_number`](#generate_unique_3_digit_number)
  - [`get_hints`](#get_hints)
  - [`play_bagels`](#play_bagels)

## פונקציות

### `generate_unique_3_digit_number`

**תיאור**:
פונקציה היוצרת מספר אקראי בן 3 ספרות שונות.

**פרמטרים**:
- אין פרמטרים.

**מחזירה**:
- `str`: מחזירה מחרוזת המייצגת מספר בן 3 ספרות שונות.

**הערות**:
- הספרה הראשונה (ספרת המאות) אינה 0.

### `get_hints`

**תיאור**:
פונקציה שמקבלת את המספר הסודי ואת הניחוש ומחזירה רמזים בהתאם.

**פרמטרים**:
- `secret_number` (str): המספר הסודי.
- `guess` (str): ניחוש המשתמש.

**מחזירה**:
- `str`: מחרוזת המכילה רמזים: "Fermi" עבור ספרה נכונה ובמיקום נכון, "Pico" עבור ספרה קיימת אך לא במיקום נכון, ו-"Bagels" אם אף ספרה לא נכונה.

### `play_bagels`

**תיאור**:
פונקציה שמפעילה את משחק "בייגלס".

**פרמטרים**:
- אין פרמטרים.

**מחזירה**:
- `None`: הפונקציה לא מחזירה ערך. היא מדפיסה את תוצאות המשחק לקונסולה.

**הערות**:
- המשחק מאפשר עד 10 ניסיונות.
- הפונקציה מדפיסה הודעת ניצחון או הפסד בהתאם לתוצאת המשחק.