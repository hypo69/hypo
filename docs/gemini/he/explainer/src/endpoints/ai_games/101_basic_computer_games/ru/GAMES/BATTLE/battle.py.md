## ניתוח קוד: משחק "קרב ימי"

### 1. <algorithm>

**תיאור אלגוריתם של משחק "קרב ימי":**

1. **אתחול:**
   - הגדרת גודל לוח המשחק (10x10).
   - יצירת שני לוחות משחק (מטריצות) דו-ממדיות, אחד לשחקן ואחד למחשב, המאוכלסים באפסים (תאים ריקים).
   - הצבת 5 ספינות באופן אקראי על לוח המחשב. גודל הספינות הוא תא אחד בלבד.
   - אתחול מונה הסיבובים לאפס.
   - הצגת לוח השחקן הריק למשתמש.

2. **לולאה ראשית (במשך 30 סיבובים):**
   - הגדלת מונה הסיבובים ב-1.
   - **תור השחקן:**
     - קליטת קואורדינטות הירי מהשחקן (שורה ועמודה).
     - בדיקה האם הירי פגע בספינה של המחשב.
     - אם פגע:
       - סימון הפגיעה על לוח המחשב ב-2.
       - הצגת הודעה "HIT!".
     - אם לא פגע:
       - סימון החמצה על לוח המחשב ב-3.
       - הצגת הודעה "MISS!".
     - הצגת לוח השחקן המעודכן עם תוצאות הירי.
   - **תור המחשב:**
     - בחירת קואורדינטות ירי אקראיות.
     - בדיקה האם הירי פגע בספינה של השחקן.
     - אם פגע:
       - סימון הפגיעה על לוח השחקן ב-2.
       - הצגת הודעה "COMPUTER HITS!".
     - אם לא פגע:
       - סימון החמצה על לוח השחקן ב-3.
       - הצגת הודעה "COMPUTER MISSES!".
     - הצגת לוח השחקן המעודכן עם תוצאות הירי של המחשב.

3. **סיום משחק:**
   - הצגת הודעה "END OF GAME".

**זרימת נתונים:**

-   `create_board(size)`: מקבלת גודל, מחזירה מטריצה מאופסת.
-   `place_computer_ships(board)`: מקבלת לוח משחק, משנה אותו על ידי הוספת ספינות באופן אקראי.
-   `display_board(board, is_computer=False)`: מקבלת לוח משחק ודגל is_computer, מדפיסה לוח משחק בפורמט מוגדר.
-   `play_battle()`: משתמשת בפונקציות הנ"ל, מנהלת את המשחק, מקבלת קלט מהמשתמש ומדפיסה פלט לקונסולה.

### 2. <mermaid>

```mermaid
flowchart TD
    Start["התחלה"] --> InitializeGame["<p align='left'>אתחול:\n    <code><b>\n    boardSize = 10\n    playerBoard = matrix(boardSize x boardSize, 0)\n    computerBoard = matrix(boardSize x boardSize, 0)\n    placeComputerShips()\n    turnCount = 0\n    </b></code></p>"]
    InitializeGame --> GameLoopStart{"התחלת לולאה: <code><b>turnCount < 30</b></code>"}
    GameLoopStart -- כן --> IncreaseTurnCount["<code><b>turnCount = turnCount + 1</b></code>"]
    IncreaseTurnCount --> PlayerInput["קלט קואורדינטות ירי מהשחקן: <code><b>playerRow, playerCol</b></code>"]
    PlayerInput --> CheckPlayerHit{"בדיקה: <code><b>computerBoard[playerRow][playerCol] == 1</b></code>?"}
    CheckPlayerHit -- כן --> PlayerHit["<code><b>computerBoard[playerRow][playerCol] = 2</b></code><br>פלט: <b>HIT!</b>"]
    PlayerHit --> PrintPlayerBoard["הצגת לוח השחקן"]
     PrintPlayerBoard --> ComputerTurn["תור המחשב: <code><b>computerRow = random(0, boardSize-1); computerCol = random(0, boardSize-1)</b></code>"]
    CheckPlayerHit -- לא --> PlayerMiss["<code><b>computerBoard[playerRow][playerCol] = 3</b></code><br>פלט: <b>MISS</b>"]
     PlayerMiss --> PrintPlayerBoard
    ComputerTurn --> CheckComputerHit{"בדיקה: <code><b>playerBoard[computerRow][computerCol] == 1</b></code>?"}
    CheckComputerHit -- כן --> ComputerHit["<code><b>playerBoard[computerRow][computerCol] = 2</b></code><br>פלט: <b>COMPUTER HITS!</b>"]
    ComputerHit --> PrintPlayerBoard2["הצגת לוח השחקן"]
    CheckComputerHit -- לא --> ComputerMiss["<code><b>playerBoard[computerRow][computerCol] = 3</b></code><br>פלט: <b>COMPUTER MISSES</b>"]
     ComputerMiss --> PrintPlayerBoard2
     PrintPlayerBoard2 --> GameLoopStart
    GameLoopStart -- לא --> End["סיום: <b>END OF GAME</b>"]
```

**הסבר תרשים זרימה:**

-   **Start**: התחלת המשחק.
-   **InitializeGame**: אתחול משתנים ולוחות משחק:
    - הגדרת גודל הלוח (`boardSize` = 10).
    - יצירת לוחות משחק לשחקן ולמחשב (`playerBoard`, `computerBoard`) כמטריצות מאופסות.
    - הצבת ספינות למחשב באופן רנדומלי על ידי הפונקציה `placeComputerShips()`.
    - אתחול מונה הסיבובים (`turnCount` = 0).
-   **GameLoopStart**: תחילת לולאת המשחק, שרצה כל עוד `turnCount` קטן מ-30.
-   **IncreaseTurnCount**: הגדלת מונה הסיבובים ב-1.
-   **PlayerInput**: קבלת קלט קואורדינטות הירי מהשחקן (`playerRow`, `playerCol`).
-   **CheckPlayerHit**: בדיקה האם ירי השחקן פגע בספינת המחשב (הערך במטריצה הוא 1).
-   **PlayerHit**: אם פגע, סימון פגיעה במטריצת המחשב ב-2, הדפסת "HIT!".
-    **PlayerMiss**: אם לא פגע, סימון החמצה במטריצת המחשב ב-3, הדפסת "MISS!".
-   **PrintPlayerBoard**: הצגת מצב לוח השחקן לאחר הירי.
-   **ComputerTurn**: תור המחשב - בחירת קואורדינטות ירי רנדומליות (`computerRow`, `computerCol`).
-   **CheckComputerHit**: בדיקה האם ירי המחשב פגע בספינת השחקן.
-   **ComputerHit**: אם פגע, סימון פגיעה במטריצת השחקן ב-2, הדפסת "COMPUTER HITS!".
-   **ComputerMiss**: אם לא פגע, סימון החמצה במטריצת השחקן ב-3, הדפסת "COMPUTER MISSES".
-   **PrintPlayerBoard2**: הצגת מצב לוח השחקן לאחר ירי המחשב.
-   **End**: סיום המשחק, הדפסת "END OF GAME".

**הסבר התלויות:**
אין תלויות מיובאות מלבד המודול `random` אשר משמש לצורך:
-   יצירת מיקום אקראי לספינות המחשב בפונקציה `place_computer_ships`.
-   יצירת קורדינאטות ירי אקראיות בפונקציה `play_battle` עבור המחשב.

### 3. <explanation>

**הסברים מפורטים:**

-   **ייבוא (Imports):**
    -   `import random`: מודול המשמש ליצירת מספרים אקראיים.
    
-   **משתנים (Variables):**
    -   `BOARD_SIZE = 10`: קבוע המגדיר את גודל לוח המשחק.
    -   `player_board`: מטריצה דו-ממדית המייצגת את לוח המשחק של השחקן.
    -   `computer_board`: מטריצה דו-ממדית המייצגת את לוח המשחק של המחשב.
    -   `turn_count`: מונה המייצג את מספר הסיבובים במשחק.
    -   `player_row`, `player_col`: משתנים המכילים את קואורדינטות הירי של השחקן.
    -   `computer_row`, `computer_col`: משתנים המכילים את קואורדינטות הירי של המחשב.

-   **פונקציות (Functions):**
    -   `create_board(size)`:
        -   פרמטרים: `size` (גודל לוח המשחק).
        -   ערך מוחזר: מטריצה דו-ממדית בגודל `size x size`, מלאה באפסים.
        -   מטרה: יצירת לוח משחק חדש ריק.
        -   דוגמה: `create_board(10)` יחזיר לוח 10x10 מלא באפסים.
    -   `place_computer_ships(board)`:
        -   פרמטרים: `board` (לוח המשחק של המחשב).
        -   ערך מוחזר: אין (משנה את הלוח ישירות).
        -   מטרה: הצבת 5 ספינות באופן אקראי על לוח המשחק של המחשב.
        -   דוגמה: `place_computer_ships(computer_board)` תציב 5 ספינות בלוח המחשב.
    -   `display_board(board, is_computer=False)`:
        -   פרמטרים: `board` (לוח המשחק להצגה), `is_computer` (דגל האם להציג ספינות מחשב).
        -   ערך מוחזר: אין (מדפיס לקונסולה).
        -   מטרה: הצגת לוח המשחק בקונסולה, הסתרת ספינות המחשב אם `is_computer` הוא `True`.
        -   דוגמה: `display_board(player_board)` תציג את לוח השחקן.
    -   `play_battle()`:
        -   פרמטרים: אין.
        -   ערך מוחזר: אין (מנהל את המשחק).
        -   מטרה: ניהול משחק הקרב הימי, קבלת קלט מהשחקן, ביצוע מהלכים, והצגת תוצאות.
        -   דוגמה: קריאה לפונקציה `play_battle()` תתחיל את המשחק.

-   **מחלקות (Classes):**
    -   אין מחלקות בקוד זה.

**בעיות אפשריות ושיפורים:**

1.  **מיקום ספינות:**
    -   המיקום הנוכחי של הספינות הוא רנדומלי ללא אפשרות הגדרה של גודל הספינות או כיוונן.
    -   שיפור: להוסיף אפשרות להצבת ספינות בגדלים שונים ובכיוונים שונים (אופקי או אנכי).
2.  **סיום המשחק:**
    -   המשחק מסתיים לאחר 30 סיבובים ולא כאשר כל הספינות הוטבעו.
    -   שיפור: להוסיף בדיקה אם כל הספינות של השחקן או המחשב הוטבעו, ולקבוע מנצח.
3.  **קלט שחקן:**
     -   קלט לא תקין עלול לגרום לשגיאות
     -   שיפור:  להוסיף בדיקות תקינות יותר (למשל, לוודא שהקואורדינטות לא הוזנו בעבר) וטיפול בטעויות קלט.
4.  **ממשק משתמש:**
    -   ממשק המשחק מוגבל לקונסולה.
    -   שיפור: יצירת ממשק משתמש גרפי (GUI) יכול לשפר את חוויית המשתמש.

**קשרים לחלקים אחרים בפרויקט:**
   -   הקוד הזה הוא משחק עצמאי. הוא לא תלוי בחלקים אחרים בפרויקט, מלבד מודול ה-`random`, שהוא חלק מהספרייה הסטנדרטית של פייתון.
   -   המשחק משתמש בקונסולה לצורך קלט/פלט, ולכן הוא יכול להיות חלק ממערכת משחקים מבוססת טקסט.