"""
KING:
=================
קושי: 5
-----------------
המשחק "KING" הוא משחק אסטרטגיה פשוט לשני שחקנים, בו כל שחקן מנסה ליצור רצף של שלושה סימנים זהים (X או O) בשורה, בעמודה או באלכסון, על לוח משחק בגודל 3x3. המשחק דומה ל"איקס עיגול", אך עם חוקים מעט שונים.

חוקי המשחק:
1. לוח המשחק הוא מטריצה 3x3.
2. שני שחקנים מתחרים זה בזה, אחד משחק עם 'X' והשני עם 'O'.
3. כל שחקן בתורו בוחר משבצת פנויה על הלוח ומסמן אותה בסימן שלו.
4. המטרה היא ליצור רצף של שלושה סימנים זהים (X או O) בשורה, בעמודה או באלכסון.
5. השחקן הראשון שמצליח ליצור רצף כזה מנצח.
6. אם כל המשבצות על הלוח מלאות ולא נוצר רצף מנצח, המשחק מסתיים בתיקו.
-----------------
אלגוריתם:
1. אתחל לוח משחק 3x3 ריק, שמיוצג על ידי מערך דו-ממדי.
2. הגדר את השחקן הנוכחי לשחקן 'X'.
3. התחל לולאה ראשית:
   3.1. הצג את לוח המשחק הנוכחי.
   3.2. בקש מהשחקן הנוכחי לבחור משבצת.
   3.3. אם המשבצת תפוסה, בקש שוב בחירה עד שתיבחר משבצת פנויה.
   3.4. סמן את המשבצת בסימן של השחקן הנוכחי ('X' או 'O').
   3.5. בדוק אם השחקן הנוכחי ניצח על ידי בדיקה של כל השורות, העמודות והאלכסונים.
   3.6. אם השחקן ניצח, הצג הודעה מתאימה וסיים את המשחק.
   3.7. אם אין מנצח, בדוק אם כל המשבצות מלאות (תיקו).
   3.8. אם הלוח מלא, הצג הודעה מתאימה וסיים את המשחק.
   3.9. אם אין ניצחון ואין תיקו, החלף את השחקן הנוכחי והמשך את הלולאה.
4. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeBoard["אתחול: 
    <code><b>
    board = [[]] # 3x3 ריק
    currentPlayer = 'X'
    </b></code>"]
    InitializeBoard --> GameLoopStart{"תחילת לולאה ראשית: כל עוד אין מנצח או תיקו"}
    GameLoopStart --> DisplayBoard["הצג את הלוח"]
    DisplayBoard --> GetMove["קבל קלט מהמשתמש (שורה ועמודה)"]
    GetMove --> ValidateMove{"בדיקה: האם המשבצת פנויה?"}
    ValidateMove -- לא --> GetMove
    ValidateMove -- כן --> UpdateBoard["עדכן את הלוח:
    <code><b>board[row][col] = currentPlayer</b></code>"]
    UpdateBoard --> CheckWin["בדיקה: האם יש מנצח?"]
    CheckWin -- כן --> DisplayWin["הצג הודעה: <code><b>{currentPlayer}</b></code> ניצח!"]
    DisplayWin --> End["סוף"]
    CheckWin -- לא --> CheckDraw{"בדיקה: האם יש תיקו (הלוח מלא)?"}
    CheckDraw -- כן --> DisplayDraw["הצג הודעה: המשחק נגמר בתיקו!"]
    DisplayDraw --> End
    CheckDraw -- לא --> SwitchPlayer["החלף שחקן: 
    <code><b>currentPlayer = 'O' if currentPlayer == 'X' else 'X'</b></code>"]
    SwitchPlayer --> GameLoopStart
    GameLoopStart -- לא --> End
```

Legenda:
    Start - התחלת התוכנית.
    InitializeBoard - אתחול לוח המשחק (מערך דו מימדי 3x3 ריק), והגדרת השחקן הנוכחי ל'X'.
    GameLoopStart - תחילת הלולאה הראשית של המשחק. הלולאה ממשיכה כל עוד אין מנצח או תיקו.
    DisplayBoard - הצגת לוח המשחק הנוכחי למשתמש.
    GetMove - קבלת קלט מהמשתמש (בחירת שורה ועמודה)
    ValidateMove - בדיקה האם המשבצת שנבחרה פנויה. אם לא, חוזרים לבקש קלט שוב.
    UpdateBoard - עדכון לוח המשחק על ידי סימון המשבצת שנבחרה בסימן של השחקן הנוכחי.
    CheckWin - בדיקה האם יש מנצח (רצף של שלושה סימנים זהים בשורה, עמודה או אלכסון).
    DisplayWin - הצגת הודעה על ניצחון של השחקן הנוכחי.
    End - סוף המשחק.
    CheckDraw - בדיקה האם המשחק הסתיים בתיקו (כל המשבצות מלאות ולא הושג ניצחון).
    DisplayDraw - הצגת הודעה שהמשחק הסתיים בתיקו.
    SwitchPlayer - החלפת השחקן הנוכחי (מ-'X' ל-'O' או מ-'O' ל-'X').
"""
import sys

# פונקציה להצגת לוח המשחק
def display_board(board):
    print("   0 1 2")
    for i, row in enumerate(board):
        print(f"{i}  {'|'.join(row)}")

# פונקציה לבדיקת ניצחון
def check_win(board, player):
    # בדיקה שורות
    for row in board:
        if all(cell == player for cell in row):
            return True
    # בדיקה עמודות
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # בדיקה אלכסונים
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# פונקציה לבדיקת תיקו
def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# פונקציית משחק
def play_king():
    # אתחול לוח משחק ריק
    board = [[' ' for _ in range(3)] for _ in range(3)]
    # אתחול שחקן נוכחי
    current_player = 'X'
    
    # לולאה ראשית של המשחק
    while True:
        display_board(board)
        
        while True:
            try:
                # קבלת קלט מהמשתמש
                row = int(input(f"שחקן {current_player}, הזן שורה (0-2): "))
                col = int(input(f"שחקן {current_player}, הזן עמודה (0-2): "))
                # בדיקה שהקלט תקין
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if board[row][col] == ' ':
                        break
                    else:
                        print("המשבצת תפוסה. נסה שוב.")
                else:
                    print("קלט לא תקין. הזן מספרים בין 0 ל-2.")
            except ValueError:
                print("קלט לא תקין. הזן מספרים שלמים.")
        
        # עדכון לוח המשחק
        board[row][col] = current_player
        
        # בדיקה אם יש מנצח
        if check_win(board, current_player):
            display_board(board)
            print(f"השחקן {current_player} ניצח!")
            break
        # בדיקה אם יש תיקו
        if check_draw(board):
            display_board(board)
            print("המשחק נגמר בתיקו!")
            break
            
        # החלפת שחקן
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    play_king()


"""
הסבר הקוד:
1.  **ייבוא `sys`**:
    - `import sys`: ייבוא מודול `sys`, שמשמש ליציאה מהתוכנית (לא בשימוש בקוד הנוכחי, אבל נשמר לצורך תאימות).
2.  **פונקציה `display_board(board)`**:
    -   מציגה את לוח המשחק הנוכחי בצורה נוחה למשתמש.
    -   `print("   0 1 2")`: הדפסת מספרי עמודות.
    -   לולאה חיצונית `for i, row in enumerate(board)`: עוברת על כל שורה בלוח.
        -   לולאה פנימית `print(f"{i}  {'|'.join(row)}")`: מדפיסה את השורה עם מספרי השורות ובסימני | בין המשבצות.
3. **פונקציה `check_win(board, player)`**:
    -  מקבלת את הלוח ואת השחקן הנוכחי.
    -  בודקת האם השחקן ניצח על ידי יצירת רצף של שלושה סימנים זהים בשורות, עמודות ואלכסונים.
        -   `for row in board`: בדיקה שורות.
        -   `for col in range(3)`: בדיקה עמודות.
        -   בדיקה אלכסונים.
    - מחזירה `True` אם יש ניצחון ו`False` אחרת.
4. **פונקציה `check_draw(board)`**:
    -   בודקת האם המשחק הסתיים בתיקו על ידי בדיקה האם כל המשבצות מלאות.
    -   אם יש משבצת ריקה ( ' '), הפונקציה מחזירה `False`.
    -   אם כל המשבצות מלאות, הפונקציה מחזירה `True`.
5. **פונקציה `play_king()`**:
    -  מכילה את הלוגיקה של המשחק.
    -  `board = [[' ' for _ in range(3)] for _ in range(3)]`: אתחול לוח משחק ריק 3x3.
    -  `current_player = 'X'`: הגדרת השחקן הראשון להיות X.
    -  `while True:`: לולאה ראשית שמתרחשת כל עוד אין מנצח או תיקו.
        -   `display_board(board)`: הצגת הלוח למשתמש.
        -   `while True:`: לולאת קלט שמתרחשת עד שהמשתמש מכניס קלט תקין.
            -   קלט: קבלת קלט מהמשתמש עבור שורה ועמודה.
            -   בדיקת תקינות: בדיקה שהקלט תקין (בין 0 ל-2) והמשבצת פנויה.
        -   `board[row][col] = current_player`: עדכון הלוח עם הבחירה של השחקן.
        -   `if check_win(board, current_player)`: בדיקה אם השחקן הנוכחי ניצח.
             -  הצגת הודעת ניצחון ויציאה מהלולאה הראשית באמצעות `break`.
        -   `if check_draw(board)`: בדיקה אם המשחק הסתיים בתיקו.
             - הצגת הודעה על תיקו ויציאה מהלולאה הראשית באמצעות `break`.
        -   `current_player = 'O' if current_player == 'X' else 'X'`: החלפת שחקן.
6. **הפעלת המשחק**:
    -   `if __name__ == "__main__":`: הקוד הבא ירוץ רק אם הקובץ רץ כסקריפט ולא כמודול.
    -   `play_king()`: קריאה לפונקציה להפעלת המשחק.
"""
