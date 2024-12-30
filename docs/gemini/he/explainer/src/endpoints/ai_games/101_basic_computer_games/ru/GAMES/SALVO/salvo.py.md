# ניתוח קוד המשחק "SALVO"

## <algorithm>

הקוד מיישם משחק "סלבו" (גרסה של "צוללות") בסיסי, בו השחקן מנסה להטביע את ספינות המחשב על ידי ניחוש קואורדינטות ברשת.

1. **אתחול לוח המשחק**:
   - יוצר לוח משחק ריק בגודל 10x10, כאשר כל תא מאותחל ל-0.
   - לדוגמה: `board = [[0, 0, 0, ...], [0, 0, 0, ...], ...]`.
   - יוצר רשימה של אורכי ספינות (לדוגמה: `ships_lengths = [2, 3, 4, 5]`).
   - מגריל מיקום אקראי לכל ספינה, כאשר כל חלק של הספינה מסומן כ-1 בלוח.

2. **אתחול משתנים**:
   - מגדיר מונה יריות (`numberOfShots`) ומאפס אותו ל-0.
   - מגדיר מונה ספינות שהוטבעו (sunk_ships_count) ומאפס אותו ל-0.
   - מדפיס את לוח המשחק הראשוני למסך, תוך הסתרת מיקומי הספינות (`~` מסמן תא ריק).

3. **לולאת המשחק**:
   - הלולאה רצה עד שכל הספינות הוטבעו (`sunk_ships_count < len(ships)`).
     - מבקש מהשחקן להזין קואורדינטות x ו-y.
       - דוגמה: `x = 3, y = 5`.
     - בודק אם הקואורדינטות תקינות (בין 0 ל-9). אם לא, מבקש להזין מחדש.
     - מגדיל את מונה היריות ב-1.
     - בודק האם הירי פגע בספינה (הערך בתא הלוח הוא 1):
       - אם כן:
         - משנה את ערך התא ל-'hit'.
         - עובר על רשימת הספינות ובודק אם אחת מהן הוטבעה בעזרת פונקציה `is_sunk` .
         - אם הספינה הוטבעה:
           - מדפיס "SINK".
           - מגדיל את מונה הספינות שהוטבעו ב-1.
           - מסיר את הספינה מרשימת הספינות.
         - אחרת, אם הספינה לא הוטבעה:
           - מדפיס "HIT".
       - אם לא פגע בספינה (הערך בתא הלוח הוא 0):
         - משנה את הערך בתא ל-'miss'.
         - מדפיס "MISS".
       - אם כבר ירו לתא הזה:
        - מדפיס "You have already shot at this coordinates".
     - מדפיס את לוח המשחק המעודכן.

4. **סיום המשחק**:
   - כאשר כל הספינות הוטבעו, הלולאה מסתיימת.
   - מדפיס הודעת ניצחון הכוללת את מספר היריות הכולל.

## <mermaid>

```mermaid
flowchart TD
    Start["התחלה"] --> InitializeBoard["<p align='left'>אתחול לוח המשחק:\n    <code><b>board[10][10] = 0</b></code><br><code><b>ships = [x, y]...</b></code></p>"]
    InitializeBoard --> InitializeShots["<code><b>numberOfShots = 0</b></code><br><code><b>sunk_ships_count = 0</b></code>"]
    InitializeShots --> PrintBoard["הדפסת לוח ראשוני"]
    PrintBoard --> GameLoopStart{"תחילת לולאה: כל עוד יש ספינות להטביע"}
    GameLoopStart -- כן --> InputCoordinates["קלט קואורדינטות X,Y: <code><b>userX, userY</b></code>"]
    InputCoordinates --> ValidateCoordinates{"בדיקת תקינות קואורדינטות\n <code><b>0 <= userX < boardSize</b></code>\n <code><b>0 <= userY < boardSize</b></code>"}
    ValidateCoordinates -- לא תקין --> InputCoordinates
    ValidateCoordinates -- תקין --> IncreaseShots["<code><b>numberOfShots = numberOfShots + 1</b></code>"]
    IncreaseShots --> CheckHit{"בדיקה: <code><b>board[userX][userY] == 1?</b></code>"}
    CheckHit -- כן --> MarkHit["סימון פגיעה: <code><b>board[userX][userY] = 'hit'</b></code>"]
    MarkHit --> CheckSink{"בדיקה: <code><b>is_sunk(ship)?</b></code>"}
     CheckSink -- כן --> OutputSink["הדפסה: <b>SINK</b>"]
     OutputSink --> UpdateSunkCount["<code><b>sunk_ships_count += 1</b></code><br>הסר ספינה מרשימה"]
     UpdateSunkCount -->  PrintBoardLoop["הדפסת לוח"]
    CheckSink -- לא --> OutputHit["הדפסה: <b>HIT</b>"]
     OutputHit -->  PrintBoardLoop
    CheckHit -- לא --> CheckMiss{"בדיקה: <code><b>board[userX][userY] == 0?</b></code>"}
    CheckMiss -- כן --> MarkMiss["סימון החטאה: <code><b>board[userX][userY] = 'miss'</b></code>"]
     MarkMiss --> OutputMiss["הדפסה: <b>MISS</b>"]
     OutputMiss -->  PrintBoardLoop
     CheckMiss -- לא --> OutputAlreadyShot["הדפסה: <b>You have already shot at this coordinates</b>"]
      OutputAlreadyShot --> PrintBoardLoop
     PrintBoardLoop --> GameLoopStart
    GameLoopStart -- לא --> OutputWin["הדפסה: <b>YOU SUNK ALL MY SHIPS IN {numberOfShots} SHOTS</b>"]
    OutputWin --> End["סיום"]

    subgraph "הפונקציה `place_ships`"
        direction LR
        startPlaceShips[התחלה]
        startPlaceShips --> loopShips["לכל אורך ספינה"]
        loopShips --> placeShip{האם ספינה הוצבה?}
        placeShip -- לא --> chooseOrientation[בחר אוריינטציה אקראית (אופקי/אנכי)]
        chooseOrientation --> checkPlacement{אפשר להציב ספינה?}
        checkPlacement -- כן --> placeCells[סמן את תאי הספינה בלוח]
         placeCells --> saveShipData[שמור נתוני הספינה]
          saveShipData --> placeShip
         checkPlacement -- לא --> chooseOrientation
         placeShip -- כן --> loopShips
        loopShips --> endPlaceShips[סיום]
    end
     subgraph "הפונקציה `is_sunk`"
        direction LR
        startIsSunk[התחלה]
        startIsSunk --> checkAllHits{"בדיקה: כל תאי הספינה == 'hit' ?"}
        checkAllHits -- כן --> endIsSunkTrue[החזר True]
        checkAllHits -- לא --> endIsSunkFalse[החזר False]

    end

```

**הסבר התלויות:**

*   הקוד משתמש במודול `random` לצורך:
    *   בחירת כיוון אקראי של הספינות (אופקי או אנכי).
    *   בחירת קואורדינטות התחלתיות אקראיות עבור כל ספינה.
*   אין תלויות בקבצים אחרים בפרויקט (למשל `import header`).

## <explanation>

1.  **ייבוא (Imports)**:
    *   `import random`: מייבא את המודול `random` שמשמש ליצירת מספרים אקראיים, לדוגמה בבחירת כיוון הספינה ובמיקומה. אין תלות בין המודול לבין תיקיית `src`.

2.  **פונקציות (Functions)**:
    *   `create_board(size)`:
        *   פרמטרים: `size` (גודל הלוח, לדוגמה 10).
        *   ערך מוחזר: לוח משחק דו-ממדי (רשימה של רשימות) בגודל `size`x`size`, מאותחל באפסים.
        *   מטרה: יצירת לוח משחק חדש וריק.
        *   דוגמה לשימוש: `board = create_board(10)`.
    *   `place_ships(board, ships_lengths)`:
        *   פרמטרים:
            *   `board`: לוח המשחק הדו-ממדי.
            *   `ships_lengths`: רשימה של אורכי ספינות (לדוגמה: `[2, 3, 4, 5]`).
        *   ערך מוחזר: רשימה של מיקומי הספינות שמוקמו (קואורדינטות, כיוון ואורך).
        *   מטרה: מיקום אקראי של ספינות על הלוח.
        *   דוגמה לשימוש: `ships = place_ships(board, [2, 3, 4, 5])`.
    * `is_sunk(board, ship)`:
        *   פרמטרים:
            *   `board`: לוח המשחק הדו-ממדי.
            *   `ship`: רשימה של נתוני ספינה (קואורדינטות, כיוון ואורך).
        *   ערך מוחזר: `True` אם הספינה הוטבעה, `False` אחרת.
        *   מטרה: בדיקה האם כל תאי הספינה סומנו כ"פגיעה".
        *   דוגמה לשימוש: `if is_sunk(board, ship): print("SINK")`.
    *   `print_board(board)`:
        *   פרמטרים: `board` (לוח המשחק הדו-ממדי).
        *   ערך מוחזר: None.
        *   מטרה: הדפסת לוח המשחק לקונסולה, כאשר ספינות מוסתרות (מסומנות כ '~' אם ערך התא הוא 0 או 1, אחרת הערך עצמו מודפס).
        *   דוגמה לשימוש: `print_board(board)`.
    *   `play_salvo()`:
        *   פרמטרים: None.
        *   ערך מוחזר: None.
        *   מטרה: הפונקציה הראשית המפעילה את המשחק. היא יוצרת את הלוח, מציבה את הספינות, מנהלת את מהלך המשחק, ובסופו מדפיסה את הודעת הניצחון.
        *   דוגמה לשימוש: `play_salvo()`.

3.  **משתנים (Variables)**:
    *   `board_size`: גודל לוח המשחק (מספר השורות והטורים).
    *   `ships_lengths`: רשימה של אורכי הספינות.
    *   `board`: לוח המשחק הדו-ממדי.
    *   `ships`: רשימה של מיקומי הספינות (אורך, כיוון וקואורדינטות).
    *   `numberOfShots`: מונה מספר היריות.
    *  `sunk_ships_count`: מונה הספינות שהוטבעו.
    *   `x`, `y`: קואורדינטות הירי שהשחקן מזין.

4.  **שרשרת קשרים עם חלקים אחרים בפרויקט**:
    *   אין קשר עם קבצים אחרים בתוך פרויקט `hypotez` (לדוגמה אין שימוש ב `header.py` או מודולים אחרים מהספרייה `src`). הקוד עצמאי ועומד בפני עצמו.

5.  **בעיות אפשריות או תחומים לשיפור**:
    *   האלגוריתם למיקום ספינות הוא פשוט ולא מונע מיקומים חופפים. ניתן לשפר זאת על ידי בדיקה של תאים שכנים לפני הצבת הספינה.
    *   הקוד לא מטפל בתרחישים בהם הספינות ממוקמות בצמוד אחת לשניה.
    *   הממשק משתמש בסיסי (טקסטואלי בלבד), וניתן לשפר אותו על ידי שימוש בספריית גרפיקה.
    *   ניתן להוסיף רמות קושי על ידי שינוי כמות הספינות, אורך הספינות או גודל הלוח.
    *   אין בדיקה אם השחקן הזין קלט לא תקין כמו אותיות או תווים מיוחדים, אפשר להוסיף בדיקה כזאת.
    *  ניתן לשפר את פונקציית `is_sunk` ע"י החזרת `False` ברגע שקיים תא אחד של הספינה שלא סומן כ- `hit`, במקום לבדוק את כל התאים.

בסך הכל הקוד מציג מימוש בסיסי של משחק צוללות, ומספק מסגרת שאפשר להרחיב אותה בעתיד.