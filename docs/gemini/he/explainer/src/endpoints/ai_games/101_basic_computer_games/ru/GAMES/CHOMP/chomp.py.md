## <algorithm>

1. **התחלת המשחק:**
   - המשחק מתחיל בקריאה לפונקציה `play_chomp()`.
   - לדוגמה, בהתחלה אין לוח משחק.

2. **קבלת מידות הלוח מהמשתמש:**
   - המשחק מבקש מהמשתמש להזין את מספר השורות והעמודות של לוח המשחק.
   - דוגמה: המשתמש מזין 4 שורות ו-5 עמודות.
   - אם הקלט אינו חוקי (למשל, לא מספר או מספר לא חיובי), מוצגת הודעת שגיאה והמשתמש מתבקש להזין שוב.

3. **יצירת לוח המשחק:**
   - הפונקציה `initialize_board(rows, cols)` יוצרת לוח משחק חדש, כאשר כל התאים מלאים ב-'X', שמייצג שוקולד.
   - דוגמה: עבור 4 שורות ו-5 עמודות, הלוח יהיה:
     ```
     [['X', 'X', 'X', 'X', 'X'],
      ['X', 'X', 'X', 'X', 'X'],
      ['X', 'X', 'X', 'X', 'X'],
      ['X', 'X', 'X', 'X', 'X']]
     ```

4. **לולאת משחק:**
   - המשחק מתחיל לולאה שרצה כל עוד המשחק לא נגמר.
   - בכל סיבוב:
     - מוצג לוח המשחק הנוכחי באמצעות הפונקציה `display_board(board)`.
     - דוגמה: אם לוח המשחק הוא כמו בדוגמה למעלה, כל השורות יודפסו עם X.
     - המשחק מבקש מהשחקן הנוכחי להזין את השורה והעמודה של החתיכה שהוא רוצה "לנגוס".
     - דוגמה: שחקן 1 מזין שורה 2 ועמודה 3.
     - אם הקלט אינו חוקי (למשל, לא מספר, מחוץ לטווח הלוח או תא ריק), מוצגת הודעת שגיאה והמשתמש מתבקש להזין שוב.

5. **עדכון לוח המשחק:**
   - הפונקציה `make_move(board, row_move, col_move)` מעדכנת את לוח המשחק על ידי החלפת כל התאים מימין ולמטה מהתא הנבחר ב-' ', שמייצג תא ריק.
     - דוגמה: אם שחקן 1 בחר שורה 2, עמודה 3, הלוח ישתנה ל:
       ```
       [['X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', ' ', ' '],
        ['X', 'X', 'X', ' ', ' ']]
       ```

6. **בדיקת סיום המשחק:**
   - הפונקציה `is_game_over(board)` בודקת אם המשחק הסתיים על ידי בדיקה האם התא בפינה השמאלית העליונה (0,0) ריק (' ').
   - דוגמה: אם הלוח הוא כפי שמוצג מעל, התא (0,0) הוא עדיין 'X' לכן המשחק לא נגמר.

7. **הכרזת מנצח:**
   - אם המשחק הסתיים, מוכרז השחקן השני כמנצח.
   - לדוגמה: "שחקן 2 ניצח!".

8. **החלפת שחקנים:**
   - השחקן הנוכחי מוחלף לשחקן השני.

9. **סיום המשחק:**
   - הלולאה נגמרת כאשר המשחק מסתיים.

## <mermaid>

```mermaid
flowchart TD
    A[Start Game: play_chomp()] --> B{Get board size from user};
    B --> C{Validate input};
    C -- Invalid input --> B;
    C -- Valid input --> D[initialize_board(rows, cols)];
    D --> E[current_player = 1];
    E --> F{Game loop: while not game_over};
    F --> G[display_board(board)];
    G --> H{Get player move: row_move, col_move};
    H --> I{Validate player move};
    I -- Invalid input --> H;
    I -- Valid input --> J[make_move(board, row_move, col_move)];
    J --> K[is_game_over(board)];
    K -- True --> L{Declare winner: current_player};
    L --> M[Display final board];
    M --> N[End Game];
    K -- False --> O[Switch player];
    O --> F;
   
   
    subgraph initialize_board
    IA[Start] --> IB[Create empty board with 'X'];
    IB --> IC[Return board];
     end
     
    subgraph make_move
    MA[Start] --> MB[Iterate from row_move to end];
    MB --> MC[Iterate from col_move to end];
    MC --> MD[Set board[row][col] to ' '];
     MD --> ME[End iteration];
    ME --> MF[Return modified board];
    end
    
    subgraph is_game_over
      GOA[Start] --> GOB{Check if board[0][0] is ' '};
      GOB -- True --> GOC[Return True];
     GOB -- False --> GOD[Return False]
    end
```

## <explanation>

### ייבואים (Imports)
אין ייבוא מיוחד בקוד זה. זהו סקריפט עצמאי שאינו תלוי בחבילות חיצוניות מלבד פונקציות Python מובנות.

### מחלקות (Classes)
אין מחלקות בקוד הזה. הקוד מורכב מפונקציות בלבד.

### פונקציות (Functions)

1.  **`initialize_board(rows, cols)`**
    *   **פרמטרים:**
        *   `rows` (int): מספר השורות בלוח המשחק.
        *   `cols` (int): מספר העמודות בלוח המשחק.
    *   **ערך מוחזר:**
        *   `list of lists`: רשימה דו-ממדית המייצגת את לוח המשחק. כל תא מאותחל ב-'X' (שוקולד).
    *   **מטרה:**
        *   יוצרת את לוח המשחק ההתחלתי, בו כל התאים מלאים בשוקולד.
    *   **דוגמה לשימוש:** `board = initialize_board(4, 5)` תיצור לוח משחק עם 4 שורות ו-5 עמודות, שכולו מלא ב-'X'.

2.  **`display_board(board)`**
    *   **פרמטרים:**
        *   `board` (`list of lists`): רשימה דו-ממדית המייצגת את לוח המשחק.
    *   **ערך מוחזר:**
        *   `None`.
    *   **מטרה:**
        *   מדפיסה את לוח המשחק הנוכחי לקונסולה.
        *  כל שורה של הלוח מוצגת בשורה נפרדת כאשר כל תא מופרד ברווח.
    *   **דוגמה לשימוש:** `display_board(board)` תדפיס את לוח המשחק המיוצג על ידי המשתנה `board`.

3.  **`make_move(board, row_move, col_move)`**
    *   **פרמטרים:**
        *   `board` (`list of lists`): רשימה דו-ממדית המייצגת את לוח המשחק.
        *   `row_move` (`int`): השורה בה השחקן בחר לבצע את המהלך.
        *   `col_move` (`int`): העמודה בה השחקן בחר לבצע את המהלך.
    *   **ערך מוחזר:**
        *   `list of lists`: לוח המשחק המעודכן לאחר המהלך.
    *   **מטרה:**
        *   מעדכנת את לוח המשחק על ידי הסרת (החלפה ב-' ') כל השוקולד מימין ולמטה מהמיקום הנבחר.
    *   **דוגמה לשימוש:** `board = make_move(board, 2, 3)` תעדכן את הלוח על ידי הסרת כל השוקולד החל מהשורה 2 והעמודה 3, וכן מימין ולמטה.

4.  **`is_game_over(board)`**
    *   **פרמטרים:**
        *   `board` (`list of lists`): לוח המשחק.
    *   **ערך מוחזר:**
        *   `bool`: `True` אם המשחק נגמר (אם התא בפינה השמאלית העליונה הוא ריק), אחרת `False`.
    *   **מטרה:**
        *   בודקת האם המשחק הסתיים על ידי בדיקה האם ה"רעל" (התא בפינה השמאלית העליונה) נלקח.
    *   **דוגמה לשימוש:** `if is_game_over(board):` תבדוק אם המשחק נגמר.

5.  **`play_chomp()`**
    *   **פרמטרים:**
        *   אין
    *   **ערך מוחזר:**
        *   `None`
    *   **מטרה:**
        *   הפונקציה הראשית שמפעילה את המשחק.
        *   מנהלת את כל מהלך המשחק, כולל קבלת גודל הלוח, הדפסתו, קבלת מהלכים מהמשתמש ובדיקה מתי המשחק נגמר.
        *    הפונקציה מנהלת את תורות השחקנים ומכריזה על המנצח בסיום המשחק.
    *   **דוגמה לשימוש:** `play_chomp()` תתחיל את משחק ה-CHOMP.

### משתנים (Variables)
*   `rows` (int): משמש לאחסון מספר השורות של לוח המשחק.
*   `cols` (int): משמש לאחסון מספר העמודות של לוח המשחק.
*  `board` (list of lists): משמש לאחסון לוח המשחק.
*   `current_player` (int): משמש לאחסון מספר השחקן הנוכחי (1 או 2).
*   `row_move` (int): משמש לאחסון השורה שבחר השחקן.
*   `col_move` (int): משמש לאחסון העמודה שבחר השחקן.

### בעיות אפשריות או תחומים לשיפור
*   **בדיקות קלט:** הקוד כולל בדיקות קלט בסיסיות למידות הלוח ולמהלכי השחקנים, אבל ניתן להוסיף בדיקות נוספות, למשל לוודא ששני השחקנים לא בוחרים את אותו המהלך.
*   **ממשק משתמש:** הממשק משתמש בקונסולה והוא בסיסי. ניתן לשפר אותו על ידי שימוש ב GUI.
*   **ניקוד:** אין אפשרות לנהל ניקוד במשחק.
*   **אינטליגנציה מלאכותית:** המשחק משחק בין שני משתמשים אנושיים. ניתן להוסיף אלגוריתם בינה מלאכותית כדי לאפשר למשתמש לשחק נגד המחשב.

### קשרים עם חלקים אחרים בפרויקט
*   קוד זה הוא משחק עצמאי, ואין לו קשרים ישירים לחלקים אחרים בפרויקט, מלבד להיות חלק מקבצי המשחקים.