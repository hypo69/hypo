# yahtze.py

## סקירה כללית

קובץ זה מיישם משחק Yahtzee בסיסי באמצעות Python. המשחק כולל מספר סבבים, כאשר בכל סבב השחקן מטיל חמישה קוביות ויכול לבחור אילו קוביות לשמור ואילו להטיל מחדש עד שלוש פעמים. לאחר מכן, השחקן בוחר קטגוריה עבור סבב זה ומקבל ניקוד בהתאם לתוצאות הטלת הקוביות.

## תוכן עניינים

- [פונקציות](#פונקציות)
    - [`roll_dice`](#roll_dice)
    - [`calculate_score`](#calculate_score)
    - [`play_yahtzee`](#play_yahtzee)

## פונקציות

### `roll_dice`

**תיאור**:
הפונקציה מדמה הטלת 5 קוביות ומחזירה רשימה של התוצאות.

**פרמטרים**:
אין

**החזרות**:
- `list[int]`: רשימה של 5 מספרים שלמים, כל אחד בין 1 ל-6, המייצגים את תוצאות הטלת הקוביות.

**הערות**:
הפונקציה משתמשת ב-`random.randint` כדי ליצור מספרים אקראיים עבור כל קובייה.

### `calculate_score`

**תיאור**:
הפונקציה מחשבת את הניקוד עבור קטגוריה נתונה בהתבסס על תוצאות הטלת הקוביות.

**פרמטרים**:
- `dice` (list[int]): רשימה של 5 מספרים שלמים, כל אחד בין 1 ל-6, המייצגים את תוצאות הטלת הקוביות.
- `category` (str): מחרוזת המייצגת את הקטגוריה שנבחרה (לדוגמה, "1", "full house", "yahtzee").

**החזרות**:
- `int`: הניקוד המתאים עבור הקטגוריה שנבחרה או 0 אם אין ניקוד.

**הערות**:
הפונקציה מטפלת בכל הקטגוריות האפשריות במשחק, כולל קטגוריות בודדות (1-6), 3 מסוג, 4 מסוג, פול האוס, סטרייט קטן, סטרייט גדול, יהטזה וצ'אנס.

### `play_yahtzee`

**תיאור**:
הפונקציה הראשית שמפעילה את המשחק Yahtzee. היא מנהלת את סבבי המשחק, הקלט מהמשתמש, חישוב הניקוד והצגת התוצאות.

**פרמטרים**:
אין

**החזרות**:
אין

**הערות**:
הפונקציה מחזיקה רשימה של כל הקטגוריות האפשריות, את הניקוד לכל קטגוריה, ואת הקטגוריות שכבר השתמשו בהן. היא עוברת על 13 סבבי המשחק, ובכל סבב היא מאפשרת לשחקן להטיל את הקוביות עד 3 פעמים, לשמור את הקוביות הרצויות ולבחור קטגוריה. בסוף המשחק, הפונקציה מציגה את טבלת הניקוד ואת סך הניקוד.