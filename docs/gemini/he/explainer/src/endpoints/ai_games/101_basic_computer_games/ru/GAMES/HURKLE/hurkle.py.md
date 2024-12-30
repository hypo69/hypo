## ניתוח קוד המשחק "HURKLE"

### 1. <algorithm>

הקוד מיישם משחק ניחושים פשוט בשם "HURKLE", בו השחקן צריך לנחש את מיקומו של "HURKLE" על גבי לוח 10x10. המשחק מספק רמזים כגון כיוון (צפון, דרום, מזרח, מערב, וכו') לאחר כל ניחוש של השחקן עד שהוא מצליח לנחש את המיקום הנכון.

**תרשים זרימה שלבי:**
1. **התחלה:**
   - התחל את המשחק.
   - לדוגמה: המשחק מתחיל לאחר הפעלת הסקריפט.
2.  **אתחול משתנים:**
    -   הגרל מיקום אקראי של `hurkle_x` ו- `hurkle_y` בין 1 ל-10.
        -   דוגמה: `hurkle_x = 3`, `hurkle_y = 7`.
    -   אתחל את `numberOfGuesses` ל-0.
        -   דוגמה: `numberOfGuesses = 0`.
3.  **לולאה ראשית:**
    -   כל עוד HURKLE לא נמצא:
        -   הגדל את מספר הניחושים ב-1.
            -   דוגמה: `numberOfGuesses = 1`.
        -   קבל קלט מהמשתמש עבור קואורדינטות `user_x` ו- `user_y`.
            -   דוגמה: `user_x = 5`, `user_y = 5`.
            - אם הקלט אינו מספר שלם, הצג הודעת שגיאה וקבל קלט מחדש.
        -   בדוק אם `user_x == hurkle_x` וגם `user_y == hurkle_y`:
            -   אם כן:
                -   הצג הודעת ניצחון וציון מספר הניחושים.
                    -   דוגמה: "YOU GOT IT IN 12 GUESSES!"
                -   סיים את המשחק.
            -   אם לא:
                -   חשב את הכיוון מנקודת המשתמש למיקום HURKLE באמצעות הפונקציה `get_direction`.
                   - דוגמה: אם `user_x = 5`, `user_y = 5`, `hurkle_x = 3`, `hurkle_y = 7` הכיוון יוחזר כ"צפון-מערב".
                -   הצג את הכיוון למשתמש.
                    -   דוגמה: "צפון-מערב".
4.  **סיום:**
    - המשחק מסתיים כאשר השחקן מנחש נכונה את מיקום ה-HURKLE.

**זרימת נתונים:**

*   המשתנה `random` משמש לייצור קואורדינטות אקראיות ל-HURKLE.
*   המשתנים `user_x`, `user_y` מאחסנים את הקלט של המשתמש.
*   המשתנים `hurkle_x`, `hurkle_y` מאחסנים את הקואורדינטות של HURKLE.
*   הפונקציה `get_direction` מקבלת כפרמטרים את הקואורדינטות של המשתמש וה-HURKLE ומחזירה את הכיוון.
*   המשתנה `numberOfGuesses` סופר את מספר הניחושים.

### 2. <mermaid>

```mermaid
flowchart TD
    Start[התחלה] --> InitializeVariables[אתחול משתנים:<br><code>hurkle_x = random(1, 10)</code><br><code>hurkle_y = random(1, 10)</code><br><code>numberOfGuesses = 0</code>]
    InitializeVariables --> GameLoopStart{לולאה: <br><code>while True</code>}
    GameLoopStart -- המשך המשחק --> IncreaseGuesses[<code>numberOfGuesses += 1</code>]
    IncreaseGuesses --> GetUserInput[קבל קלט משתמש:<br><code>user_x = input()</code><br><code>user_y = input()</code>]
    GetUserInput --> CheckInputType{בדיקת סוג קלט:<br><code>isinstance(user_x, int)</code> and <code>isinstance(user_y, int)</code>?}
    CheckInputType -- לא מספר שלם --> ShowError[הצג שגיאה]
    ShowError --> GameLoopStart
    CheckInputType -- מספר שלם --> CheckWin{בדיקה: <br><code>user_x == hurkle_x</code> וגם <br><code>user_y == hurkle_y</code>?}
    CheckWin -- נכון --> WinMessage[הודעת ניצחון:<br><code>print("YOU GOT IT IN {numberOfGuesses} GUESSES!")</code>]
    WinMessage --> End[סיום]
    CheckWin -- לא נכון --> CalculateDirection[<code>direction = get_direction(user_x, user_y, hurkle_x, hurkle_y)</code>]
    CalculateDirection --> ShowDirection[הצג כיוון:<br><code>print(direction)</code>]
    ShowDirection --> GameLoopStart
    GameLoopStart -- המשחק נגמר --> End
    
    subgraph get_direction
        GD_Start[התחלה] --> GD_CheckNE{<code>user_x < hurkle_x</code> and <code>user_y < hurkle_y</code>?}
        GD_CheckNE -- כן --> GD_ReturnNE[החזר "צפון-מזרח"]
        GD_CheckNE -- לא --> GD_CheckSE{<code>user_x < hurkle_x</code> and <code>user_y > hurkle_y</code>?}
        GD_CheckSE -- כן --> GD_ReturnSE[החזר "דרום-מזרח"]
        GD_CheckSE -- לא --> GD_CheckNW{<code>user_x > hurkle_x</code> and <code>user_y < hurkle_y</code>?}
        GD_CheckNW -- כן --> GD_ReturnNW[החזר "צפון-מערב"]
        GD_CheckNW -- לא --> GD_CheckSW{<code>user_x > hurkle_x</code> and <code>user_y > hurkle_y</code>?}
         GD_CheckSW -- כן --> GD_ReturnSW[החזר "דרום-מערב"]
         GD_CheckSW -- לא --> GD_CheckEast{<code>user_x < hurkle_x</code>?}
        GD_CheckEast -- כן --> GD_ReturnE[החזר "מזרח"]
        GD_CheckEast -- לא --> GD_CheckWest{<code>user_x > hurkle_x</code>?}
        GD_CheckWest -- כן --> GD_ReturnW[החזר "מערב"]
        GD_CheckWest -- לא --> GD_CheckNorth{<code>user_y < hurkle_y</code>?}
         GD_CheckNorth -- כן --> GD_ReturnN[החזר "צפון"]
         GD_CheckNorth -- לא --> GD_ReturnS[החזר "דרום"]
         GD_ReturnNE --> GD_End[סיום]
         GD_ReturnSE --> GD_End
         GD_ReturnNW --> GD_End
         GD_ReturnSW --> GD_End
         GD_ReturnE --> GD_End
         GD_ReturnW --> GD_End
         GD_ReturnN --> GD_End
         GD_ReturnS --> GD_End
    end
    
    
```

**ניתוח תלויות:**

*   `random`: מודול שמובנה בשפה python, משמש ליצירת קואורדינטות אקראיות למיקום ה-HURKLE.

### 3. <explanation>

**ייבוא (Imports):**
*   `import random`: מייבא את המודול `random`, אשר מספק פונקציות ליצירת מספרים אקראיים. מודול זה משמש לייצור הקואורדינטות של ה-HURKLE באופן אקראי.

**פונקציות (Functions):**
*   `get_direction(user_x, user_y, hurkle_x, hurkle_y)`:
    *   **פרמטרים**:
        *   `user_x` (int): קואורדינטת X של השחקן.
        *   `user_y` (int): קואורדינטת Y של השחקן.
        *   `hurkle_x` (int): קואורדינטת X של ה-HURKLE.
        *   `hurkle_y` (int): קואורדינטת Y של ה-HURKLE.
    *   **ערך מוחזר**: מחזירה מחרוזת המייצגת את הכיוון מהקואורדינטות של השחקן לקואורדינטות של ה-HURKLE (לדוגמה, "צפון-מזרח", "דרום", "מערב" וכו').
    *   **מטרה**: פונקציה זו מחשבת ומחזירה את הכיוון יחסית למיקום המשתמש ולמיקום ה-HURKLE.
    *   **דוגמאות שימוש**:
         *  `get_direction(2, 3, 5, 7)` תחזיר "צפון-מזרח".
         *  `get_direction(6, 6, 1, 1)` תחזיר "דרום-מערב".

**משתנים (Variables):**
*   `hurkle_x` (int): קואורדינטת X של ה-HURKLE (מגורלת באופן אקראי בין 1 ל-10).
*   `hurkle_y` (int): קואורדינטת Y של ה-HURKLE (מגורלת באופן אקראי בין 1 ל-10).
*   `numberOfGuesses` (int): מונה את מספר הניחושים שהשחקן ביצע. מתחיל מ-0 וגדל ב-1 בכל ניחוש.
*   `user_x` (int): קואורדינטת X שהמשתמש מזין.
*   `user_y` (int): קואורדינטת Y שהמשתמש מזין.
*    `direction` (str): כיוון ה-HURKLE יחסית למיקום המשתמש.

**הסבר מפורט:**

1.  **אתחול:** המשחק מתחיל בהגרלת מיקום אקראי ל-HURKLE על ידי שימוש בפונקציה `random.randint(1, 10)` עבור הקואורדינטות `hurkle_x` ו-`hurkle_y`. בנוסף, המשתנה `numberOfGuesses` מאותחל ל-0 כדי לעקוב אחר מספר הניחושים של השחקן.
2.  **לולאת המשחק:**
    *   הלולאה `while True` ממשיכה לפעול עד שהמשתמש מנחש את מיקום ה-HURKLE.
    *   בכל איטרציה, מספר הניחושים גדל ב-1.
    *   המשתמש מתבקש להזין קואורדינטות X ו-Y.
    *   **טיפול בשגיאות**: קוד ה-`try...except` מטפל במקרה שהמשתמש מזין קלט שאינו מספר שלם.
    *   **בדיקת ניצחון:** הקוד בודק אם הקואורדינטות שהזין המשתמש תואמות לקואורדינטות של ה-HURKLE. אם כן, מוצגת הודעת ניצחון עם מספר הניחושים, והמשחק מסתיים.
    *  **חישוב כיוון**: אם המשתמש לא ניחש נכון, הפונקציה `get_direction` מופעלת כדי לקבוע את הכיוון מנקודת המשתמש למיקום ה-HURKLE. הכיוון מודפס למסך והלולאה ממשיכה.

**בעיות אפשריות ושיפורים:**

*   **קלט משתמש**: ניתן להוסיף בדיקות תקינות לקלט המשתמש כדי לוודא שהוא בין 1 ל-10, ולאפשר למשתמש לנסות שוב במקרה של קלט שגוי.
*   **ממשק משתמש**: ניתן לשפר את ממשק המשתמש (למשל, להוסיף הוראות למשחק או גרפיקה בסיסית).
*   **מורכבות**: ניתן לשפר את המשחק על ידי הוספת רמות קושי (לדוגמה, הגדלת גודל הלוח או הוספת מכשולים).

**קשרים עם חלקים אחרים בפרויקט:**

*   הקוד הוא משחק עצמאי ואינו תלוי בחלקים אחרים בפרויקט.