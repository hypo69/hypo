## <algorithm>

1.  **אתחול משתנים**:
    *   מחשב מייצר באופן רנדומלי שלושה מספרים שלמים `targetA`, `targetB`, ו-`targetC` בין 1 ל-10.
    *   דוגמא: `targetA = 3`, `targetB = 7`, `targetC = 1`.

2.  **לולאה ראשית**:
    *   הלולאה ממשיכה עד שהמשתמש מנחש נכון את כל שלושת המספרים.
    *   **דוגמא**: אם `userA = 2`, `userB = 7`, ו-`userC = 1` אז הלולאה תמשיך.

3.  **קליטת קלט משתמש**:
    *   המערכת מבקשת מהמשתמש להזין שלושה מספרים שלמים `userA`, `userB`, ו-`userC`.
    *   **דוגמא**: המשתמש מזין `userA = 3`, `userB = 8`, `userC = 2`.

4.  **אתחול הודעה**:
    *   מאתחלים משתנה מחרוזת `message` להיות ריק.
    *   **דוגמא**: `message = ""`.

5.  **בדיקה של `userA`**:
    *   בודקים אם `userA` שונה מ-`targetA`.
    *   אם כן, מוסיפים "A" למשתנה `message`.
    *   **דוגמא**: אם `userA = 3` ו-`targetA = 3` אז המשתנה `message` לא ישתנה, אחרת אם `userA = 2` אז `message = "A"`.

6.  **בדיקה של `userB`**:
    *   בודקים אם `userB` שונה מ-`targetB`.
    *   אם כן, מוסיפים "B" למשתנה `message`.
    *    **דוגמא**: אם `userB = 8` ו-`targetB = 7` אז `message = "AB"` (אם `message` כבר הכיל A), אחרת אם `userB = 7` אז לא משנים את `message`.

7.  **בדיקה של `userC`**:
    *   בודקים אם `userC` שונה מ-`targetC`.
    *   אם כן, מוסיפים "C" למשתנה `message`.
    *   **דוגמא**: אם `userC = 2` ו-`targetC = 1` אז `message = "ABC"` (אם `message` כבר הכיל AB), אחרת אם `userC = 1` אז לא משנים את `message`.

8.  **בדיקת הודעה**:
    *   בודקים אם המשתנה `message` ריק.
    *   אם לא, מוצגת הודעת שגיאה עם הערכים הלא נכונים.
        *   **דוגמא**: אם `message = "ABC"` אז תודפס הודעה "WRONG ON ABC".
    *   אם כן, מוצגת הודעת ניצחון.
        *   **דוגמא**: אם `message = ""` אז תודפס הודעה "YOU GOT IT!".

9.  **סיום**:
    *   אם המשתמש ניחש נכון את כל המספרים, הלולאה מסתיימת, והמשחק נגמר.
    *   אחרת, חוזרים לשלב 3, ומקבלים קלט משתמש נוסף.

## <mermaid>

```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:<br><code><b>targetA = random(1, 10)</b></code><br><code><b>targetB = random(1, 10)</b></code><br><code><b>targetC = random(1, 10)</b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: עד שכל המספרים נוחשו נכון"}
    LoopStart --> InputValues["<p align='left'>קלט משתמש:<br><code><b>userA</b></code><br><code><b>userB</b></code><br><code><b>userC</b></code></p>"]
    InputValues --> InitializeMessage["<code><b>message = ""</b></code>"]
    InitializeMessage --> CheckA{"בדיקה: <code><b>userA == targetA ?</b></code>"}
    CheckA -- לא --> AppendA["<code><b>message = message + 'A'</b></code>"]
    AppendA --> CheckB{"בדיקה: <code><b>userB == targetB ?</b></code>"}
    CheckA -- כן --> CheckB
    CheckB -- לא --> AppendB["<code><b>message = message + 'B'</b></code>"]
    AppendB --> CheckC{"בדיקה: <code><b>userC == targetC ?</b></code>"}
    CheckB -- כן --> CheckC
    CheckC -- לא --> AppendC["<code><b>message = message + 'C'</b></code>"]
    AppendC --> CheckMessage{"בדיקה: <code><b>message != "" ?</b></code>"}
    CheckC -- כן --> CheckMessage
    CheckMessage -- כן --> OutputWrong["הדפסה: <b>WRONG ON {message}</b>"]
    OutputWrong --> LoopStart
    CheckMessage -- לא --> OutputWin["הדפסה: <b>YOU GOT IT!</b>"]
    OutputWin --> End["סיום"]
    LoopStart -- לא --> End
```

התרשים מתאר את זרימת הפעולות במשחק, החל מאתחול המשתנים ועד לסיום המשחק. כל שלב מיוצג על ידי תיבה, והחיצים מראים את זרימת השליטה בין השלבים.

*   **Start**: מסמן את תחילת המשחק.
*   **InitializeVariables**: מייצר באופן אקראי שלושה משתנים `targetA`, `targetB`, ו-`targetC`.
*   **LoopStart**: תחילת הלולאה שמתבצעת עד שהמשתמש מנחש את כל המספרים.
*   **InputValues**: קבלת קלט מהמשתמש עבור `userA`, `userB`, ו-`userC`.
*   **InitializeMessage**: אתחול מחרוזת ריקה `message`.
*   **CheckA**: בדיקה האם `userA` שווה ל-`targetA`.
*   **AppendA**: אם `userA` לא שווה ל-`targetA`, מוסיפים "A" למשתנה `message`.
*   **CheckB**: בדיקה האם `userB` שווה ל-`targetB`.
*   **AppendB**: אם `userB` לא שווה ל-`targetB`, מוסיפים "B" למשתנה `message`.
*   **CheckC**: בדיקה האם `userC` שווה ל-`targetC`.
*   **AppendC**: אם `userC` לא שווה ל-`targetC`, מוסיפים "C" למשתנה `message`.
*   **CheckMessage**: בדיקה האם המשתנה `message` ריק.
*   **OutputWrong**: הדפסת הודעת שגיאה עם הערכים הלא נכונים אם `message` לא ריק.
*   **OutputWin**: הדפסת הודעת ניצחון אם `message` ריק.
*   **End**: סיום המשחק.

## <explanation>

*   **ייבואים (Imports)**:
    *   אין ייבוא ספציפי בקוד זה.

*   **משתנים (Variables)**:

    *   `targetA`, `targetB`, `targetC` - שלושה משתנים שמייצגים את המספרים שעל השחקן לנחש, מוגרלים באופן אקראי בתחום של 1-10.
    *   `userA`, `userB`, `userC` - שלושה משתנים שמקבלים קלט מהמשתמש ומייצגים את הניחושים שלו.
    *   `message` - מחרוזת המשמשת לאיסוף מידע לגבי המספרים שהמשתמש טעה בהם. אם המשתמש טעה ב-`userA`, אז `A` יתווסף למחרוזת, וכך הלאה.
    *   **הערה**: קוד זה אינו כולל משתנים גלובליים או ייבוא מחבילות אחרות.

*   **פונקציות (Functions)**:
    *   אין פונקציות מוגדרות בקוד הזה. כל ההיגיון ממוקם בתוך הלולאה הראשית.

*   **הסברים נוספים**:
    *   קוד זה מיישם משחק ניחושים פשוט שבו המחשב מגריל שלושה מספרים אקראיים והמשתמש צריך לנחש אותם. המשחק חוזר על עצמו עד שהמשתמש מנחש נכון את כל המספרים.
    *   הקוד פשוט וקל להבנה, אך יכול להכיל שיפורים, כמו:
        *   ניתן להפוך את הקוד לפונקציות נפרדות, לדוגמה פונקציה ליצירת מספרים רנדומליים, פונקציה לבדיקת הקלט, פונקציה לפלט.
        *   אפשרות למספר ניסיונות מוגבל למשתמש, ואז להוסיף תנאי להפסקת המשחק.

*   **שרשרת קשרים**:
    *   קוד זה הוא משחק עצמאי ואין לו תלות ישירה בחלקים אחרים בפרויקט. עם זאת, ניתן להשתמש בו כחלק ממערכת גדולה יותר של משחקים, כאשר כל משחק ממוקם במודול משלו.