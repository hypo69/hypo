# ניתוח קוד: משחק "REVRSE"

## <algorithm>

1. **אתחול משתנים:**
   - `numberOfGuesses` = 0 (מונה מספר הניסיונות).
   - `targetSequence` = רצף אקראי של 4 מספרים בין 1 ל-6 (לדוגמה, `[3, 1, 6, 2]`).

2. **לולאה:** כל עוד `numberOfGuesses` < 10 (מגבלה של 10 ניסיונות):
   - הגדלת `numberOfGuesses` ב-1.
     - דוגמה: אם `numberOfGuesses` היה 0, עכשיו הוא יהיה 1.
   - קבלת קלט מהמשתמש (רצף של 4 מספרים).
     - דוגמה: משתמש מזין `1 2 3 4`.
   - השוואת רצף המשתמש עם `targetSequence` וחישוב:
     - `directHits`: מספר הספרות הנכונות במיקומן הנכון.
       - דוגמה: אם `targetSequence` היה `[3, 1, 6, 2]` ו-`userSequence` היה `[3, 5, 6, 4]`, אז `directHits` יהיה 2 (3 ו-6).
     - `indirectHits`: מספר הספרות הנכונות שאינן במיקומן הנכון.
       - דוגמה: אם `targetSequence` היה `[3, 1, 6, 2]` ו-`userSequence` היה `[1, 3, 4, 6]`, אז `indirectHits` יהיה 3 (1, 3 ו-6).
   - הצגת תוצאות השוואה (`directHits`, `indirectHits`).
   - אם `directHits` == 4:
     - הצגת הודעת ניצחון וסיום המשחק.

3. **סיום המשחק:** אם הלולאה מסתיימת (אחרי 10 ניסיונות):
   - הצגת הודעת הפסד.
   - הצגת הרצף הנכון (`targetSequence`).

**זרימת הנתונים:**

-   `generate_target_sequence`: מייצר רצף אקראי ומוחזר לתוך `targetSequence` בפונקציה `play_reverse_game`.
-   `play_reverse_game`: מקבלת קלט מהמשתמש, מעבירה את `targetSequence` ואת הקלט לפונקציה `compare_sequences`, ומקבלת את `directHits` ו-`indirectHits`.
-   `compare_sequences`: מקבלת את `targetSequence` ורצף המשתמש, ומחזירה את `directHits` ו-`indirectHits` לפונקציה `play_reverse_game`.

## <mermaid>

```mermaid
flowchart TD
    Start[התחלה] --> InitializeVariables[אתחול משתנים:<br><code>numberOfGuesses = 0</code><br><code>targetSequence = generate_target_sequence()</code>]
    InitializeVariables --> LoopStart{<code>numberOfGuesses < 10?</code>}
    LoopStart -- כן --> IncreaseGuesses[<code>numberOfGuesses += 1</code>]
    IncreaseGuesses --> GetUserInput[קבל קלט מהמשתמש:<br><code>userSequence</code>]
     GetUserInput --> ValidateInput{קלט תקין?<br><code>len(userSequence) == 4 & 1 <= x <= 6</code>}
    ValidateInput -- כן --> CompareSequences[השוואת רצפים:<br><code>directHits, indirectHits = compare_sequences(targetSequence, userSequence)</code>]
    ValidateInput -- לא --> GetUserInput
    CompareSequences --> DisplayResults[הצגת תוצאות:<br><code>directHits, indirectHits</code>]
    DisplayResults --> CheckWin{<code>directHits == 4?</code>}
    CheckWin -- כן --> WinMessage[הודעת ניצחון]
    WinMessage --> End[סיום]
    CheckWin -- לא --> LoopStart
    LoopStart -- לא --> LoseMessage[הודעת הפסד]
    LoseMessage --> ShowTarget[הצגת רצף נכון:<br><code>targetSequence</code>]
    ShowTarget --> End
```

**ניתוח תלויות:**

הקוד משתמש במודול `random` מתוך ספריית הפייתון הסטנדרטית לצורך יצירת רצפים אקראיים. אין תלויות מיוחדות בחבילות `src.`.

## <explanation>

### ייבוא (Imports)

-   `import random`: מודול `random` משמש ליצירת רצפים של מספרים אקראיים. נעשה בו שימוש בפונקציה `generate_target_sequence` על מנת ליצור את רצף המטרה שהמשתמש צריך לנחש. המודול הוא חלק מספרית הסטנדרט של פייתון ואינו תלוי בחבילות אחרות בפרוייקט.

### פונקציות (Functions)

1.  **`generate_target_sequence()`**
    -   **פרמטרים:** אין.
    -   **ערך מוחזר:** רשימה של 4 מספרים אקראיים שלמים בין 1 ל-6.
    -   **מטרה:** לייצר רצף אקראי של 4 מספרים שישמש כרצף המטרה במשחק.
    -   **דוגמה:** `generate_target_sequence()` עשויה להחזיר `[2, 5, 1, 4]`.
2.  **`compare_sequences(target, user)`**
    -   **פרמטרים:**
        -   `target`: רשימת מספרים (רצף המטרה).
        -   `user`: רשימת מספרים (רצף המשתמש).
    -   **ערך מוחזר:** טופל (tuple) המכיל שני מספרים: `direct_hits` (מספר הפגיעות הישירות) ו-`indirect_hits` (מספר הפגיעות העקיפות).
    -   **מטרה:** להשוות בין רצף המטרה לרצף המשתמש, ולחשב כמה מספרים מופיעים במיקום הנכון (פגיעה ישירה) וכמה מופיעים אך לא במיקום הנכון (פגיעה עקיפה).
    -   **דוגמה:** אם `target` הוא `[1, 2, 3, 4]` ו-`user` הוא `[1, 4, 2, 5]`, אז הפונקציה תחזיר `(1, 2)` כי יש פגיעה ישירה אחת (1), ושתי פגיעות עקיפות (2 ו-4).
3.  **`play_reverse_game()`**
    -   **פרמטרים:** אין.
    -   **ערך מוחזר:** אין (מחזירה `None` באופן מרומז).
    -   **מטרה:** להפעיל את המשחק, לאפשר למשתמש להזין ניחושים, להשוות אותם לרצף המטרה, ולדווח על התוצאות.
    -   **דוגמה:** הפונקציה מדפיסה הנחיות, מקבלת קלט מהמשתמש ומדפיסה את מספר הפגיעות הישירות והעקיפות, או הודעה שהמשתמש ניצח/הפסיד.

### משתנים (Variables)

-   `numberOfGuesses`: משתנה שלם ששומר את מספר הניסיונות שעשה המשתמש. מאותחל ל-0 וגדל ב-1 בכל ניסיון.
-   `targetSequence`: רשימה של מספרים שלמים, הרצף האקראי שנוצר על ידי הפונקציה `generate_target_sequence`, שאותו המשתמש צריך לנחש.
-   `userSequence`: רשימה של מספרים שלמים, הרצף שהמשתמש מזין.
-    `directHits`: משתנה שלם, שומר את מספר הפגיעות הישירות (מספרים במיקומם הנכון).
-   `indirectHits`: משתנה שלם, שומר את מספר הפגיעות העקיפות (מספרים נכונים שאינם במיקומם הנכון).

### בעיות ושיפורים אפשריים

1.  **קלט לא תקין:** הקוד מטפל במידה מסוימת בקלט שגוי (למשל, אם המשתמש לא מזין מספרים שלמים או לא מזין 4 מספרים), אבל יש מקום לטיפול יותר מפורט וממוקד בבעיות קלט. לדוגמה:
    *   אפשר להשתמש ב-regex כדי לבדוק שהקלט הוא רצף של 4 מספרים בין 1 ל-6, מופרדים ברווחים.
    *   אפשר להציג הודעות שגיאה יותר ברורות למשתמש.
2.  **קריאות הקוד:** אפשר לפצל את פונקציית `play_reverse_game` למספר פונקציות קטנות יותר על מנת לשפר את הקריאות והארגון של הקוד.
3.  **אינטראקציה עם משתמש:** ניתן לשפר את חווית המשתמש על ידי מתן משוב נוסף, כמו להציג היסטוריה של הניחושים הקודמים ומשוב מפורט יותר על כל ניסיון.

**שרשרת קשרים עם חלקים אחרים בפרויקט:**

קוד זה עומד בפני עצמו ואינו תלוי בקבצים אחרים בפרוייקט. עם זאת, במערכת גדולה יותר, קובץ זה יכול להסתמך על חבילות או מודולים אחרים המטפלים באינטראקציה עם המשתמש (GUI, ממשק שורת פקודה), ובמכניקה של משחקים (למשל, ניהול סשנים של משחק, ניקוד, וכו').