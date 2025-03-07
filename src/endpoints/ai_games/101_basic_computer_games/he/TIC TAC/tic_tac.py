"""
<TIC TAC>:
=================
קושי: 4
-----------------
משחק איקס עיגול הוא משחק לשני שחקנים שבו הם מסמנים לסירוגין ריבועים ברשת 3x3. השחקן שמצליח ליצור שורה של שלושה סימנים זהים (אופקית, אנכית או אלכסונית) מנצח.
במשחק זה, השחקן האחד משחק נגד המחשב.

חוקי המשחק:
1. המשחק משוחק על לוח 3x3.
2. השחקן משחק בתור 'X' והמחשב בתור 'O'.
3. השחקנים מסמנים משבצת פנויה בתורם.
4. השחקן הראשון שיוצר שורה של שלושה סימנים זהים (אופקית, אנכית או אלכסונית) מנצח.
5. אם כל המשבצות מלאות ואין מנצח, המשחק מסתיים בתיקו.
-----------------
אלגוריתם:
1. אתחל את לוח המשחק כמערך דו-ממדי בגודל 3x3, כאשר כל התאים ריקים (מיוצגים על ידי רווחים).
2. הגדר את השחקן כ-'X' ואת המחשב כ-'O'.
3. התחל לולאה ראשית:
   3.1 הצג את לוח המשחק הנוכחי.
   3.2 בקש מהשחקן לבחור משבצת פנויה (על ידי הזנת מספר מ-1 עד 9).
   3.3 אם המשבצת שנבחרה כבר תפוסה, בקש מהשחקן לבחור משבצת אחרת.
   3.4 עדכן את לוח המשחק עם הבחירה של השחקן.
   3.5 בדוק אם השחקן ניצח (יש שורה של שלושה איקסים). אם כן, הצג הודעת ניצחון וסיים את המשחק.
   3.6 אם הלוח מלא, הצג הודעת תיקו וסיים את המשחק.
   3.7 המחשב בוחר משבצת פנויה אקראית.
   3.8 עדכן את לוח המשחק עם הבחירה של המחשב.
   3.9 בדוק אם המחשב ניצח (יש שורה של שלושה עיגולים). אם כן, הצג הודעת הפסד וסיים את המשחק.
   3.10 אם הלוח מלא, הצג הודעת תיקו וסיים את המשחק.
4. חזור ללולאה הראשית עד שיש מנצח או תיקו.
5. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeBoard["<p align='left'>אתחול לוח המשחק:
    <code><b>
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    player = 'X'
    computer = 'O'
    </b></code></p>"]
    InitializeBoard --> MainLoopStart{"תחילת לולאה: כל עוד אין מנצח או תיקו"}
    MainLoopStart --> DisplayBoard["הצגת לוח המשחק"]
    DisplayBoard --> PlayerInput["קלט מהשחקן: בחירת משבצת (1-9)"]
    PlayerInput --> ValidateInput{"בדיקה: האם המשבצת פנויה?"}
    ValidateInput -- לא --> PlayerInput
    ValidateInput -- כן --> UpdateBoardPlayer["עדכון לוח המשחק עם בחירת השחקן"]
    UpdateBoardPlayer --> CheckWinPlayer{"בדיקה: האם השחקן ניצח?"}
    CheckWinPlayer -- כן --> OutputWin["הצגת הודעה: <b>YOU WIN!</b>"]
    OutputWin --> End["סוף"]
     CheckWinPlayer -- לא --> CheckBoardFullPlayer{"בדיקה: האם הלוח מלא?"}
    CheckBoardFullPlayer -- כן --> OutputTie["הצגת הודעה: <b>TIE!</b>"]
    OutputTie --> End
    CheckBoardFullPlayer -- לא --> ComputerMove["בחירת משבצת פנויה אקראית על ידי המחשב"]
    ComputerMove --> UpdateBoardComputer["עדכון לוח המשחק עם בחירת המחשב"]
    UpdateBoardComputer --> CheckWinComputer{"בדיקה: האם המחשב ניצח?"}
    CheckWinComputer -- כן --> OutputLose["הצגת הודעה: <b>YOU LOSE!</b>"]
    OutputLose --> End
    CheckWinComputer -- לא --> CheckBoardFullComputer{"בדיקה: האם הלוח מלא?"}
    CheckBoardFullComputer -- כן --> OutputTie2["הצגת הודעה: <b>TIE!</b>"]
    OutputTie2 --> End
    CheckBoardFullComputer -- לא --> MainLoopStart
    MainLoopStart -- לא --> End
```
Legenda:
    Start - התחלת המשחק.
    InitializeBoard - אתחול לוח המשחק כמערך דו-ממדי, הגדרת השחקן כ-'X' והמחשב כ-'O'.
    MainLoopStart - תחילת הלולאה הראשית, הממשיכה עד שיש מנצח או תיקו.
    DisplayBoard - הצגת לוח המשחק הנוכחי למשתמש.
    PlayerInput - קבלת קלט מהמשתמש: בחירת משבצת פנויה בלוח.
    ValidateInput - בדיקה האם המשבצת שבחר המשתמש פנויה. אם לא, חוזרים לבקשת קלט מהמשתמש.
    UpdateBoardPlayer - עדכון לוח המשחק עם בחירת השחקן.
    CheckWinPlayer - בדיקה האם השחקן ניצח.
    OutputWin - הצגת הודעת ניצחון אם השחקן ניצח.
    End - סיום המשחק.
    CheckBoardFullPlayer - בדיקה האם לוח המשחק מלא לאחר תור השחקן.
    OutputTie - הצגת הודעה על תיקו אם הלוח מלא.
    ComputerMove - המחשב בוחר משבצת פנויה באופן אקראי.
    UpdateBoardComputer - עדכון לוח המשחק עם בחירת המחשב.
    CheckWinComputer - בדיקה האם המחשב ניצח.
    OutputLose - הצגת הודעה על הפסד אם המחשב ניצח.
    CheckBoardFullComputer - בדיקה האם לוח המשחק מלא לאחר תור המחשב.
     OutputTie2 - הצגת הודעה על תיקו אם הלוח מלא.

"""
import random

# פונקציה להדפסת לוח המשחק
def print_board(board):
    """
    מדפיסה את לוח המשחק הנוכחי.
    הלוח מוצג עם מספרים 1-9 כדי שהמשתמש יוכל לבחור את המשבצת
    """
    print("   1 | 2 | 3 ")
    print("  ---+---+---")
    print(f" 4 | {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("  ---+---+---")
    print(f" 5 | {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("  ---+---+---")
    print(f" 6 | {board[2][0]} | {board[2][1]} | {board[2][2]} ")
    print("   ---+---+---")
    print("   7 | 8 | 9 ")


# פונקציה לבדיקת ניצחון
def check_win(board, player):
  """
    בודקת אם שחקן מסוים ניצח.
    היא בודקת את כל השורות, העמודות והאלכסונים
    """
  # בדיקת שורות
  for row in board:
    if all(cell == player for cell in row):
      return True
  # בדיקת עמודות
  for col in range(3):
    if all(board[row][col] == player for row in range(3)):
      return True
  # בדיקת אלכסונים
  if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
    return True
  return False

# פונקציה לבדיקה אם הלוח מלא
def is_board_full(board):
    """
    בודקת האם כל המשבצות בלוח מלאות, כלומר אין יותר מקומות פנויים.
    """
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


# פונקציה למהלך המחשב
def computer_move(board):
    """
      המחשב בוחר משבצת פנויה באופן אקראי.
      הוא ממשיך לבחור עד שהוא מוצא משבצת פנויה.
      """
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            return row, col


# פונקציה ראשית של המשחק
def play_tic_tac_toe():
    """
      הפונקציה הראשית של המשחק איקס עיגול.
      מנהלת את כל התהליך של המשחק, משחקן נגד המחשב
    """
    # אתחול לוח המשחק
    board = [[' ' for _ in range(3)] for _ in range(3)] # יוצר לוח 3X3 ריק
    player = 'X'
    computer = 'O'

    # לולאת משחק ראשית
    while True:
        # הדפסת הלוח
        print_board(board)

        # קלט מהשחקן
        while True:
            try:
                choice = int(input("בחר משבצת (1-9): "))
                if 1 <= choice <= 9:
                    row = (choice - 1) // 3
                    col = (choice - 1) % 3
                    if board[row][col] == ' ': # בדיקה שהמשבצת פנויה
                        break # יציאה מהלולאה
                    else:
                        print("משבצת תפוסה, נסה שוב.")
                else:
                    print("בחירה לא חוקית, אנא בחר מספר בין 1 ל-9.")
            except ValueError:
                print("קלט לא תקין, אנא הזן מספר.")


        # עדכון לוח המשחק עם הבחירה של השחקן
        board[row][col] = player

        # בדיקה אם השחקן ניצח
        if check_win(board, player):
            print_board(board)
            print("ניצחת!")
            break # סיום המשחק
        # בדיקה אם הלוח מלא
        if is_board_full(board):
            print_board(board)
            print("תיקו!")
            break # סיום המשחק


        # מהלך המחשב
        print("תור המחשב...")
        row, col = computer_move(board)
        board[row][col] = computer

         # בדיקה אם המחשב ניצח
        if check_win(board, computer):
            print_board(board)
            print("הפסדת!")
            break # סיום המשחק

        # בדיקה אם הלוח מלא
        if is_board_full(board):
            print_board(board)
            print("תיקו!")
            break  # סיום המשחק


# הפעלת המשחק אם הקובץ מורץ
if __name__ == "__main__":
    play_tic_tac_toe()

"""
הסבר מפורט לקוד:
1.  **ייבוא מודול `random`**:
    - `import random`: ייבוא המודול `random` כדי ליצור בחירות אקראיות עבור מהלכי המחשב.
2.  **פונקציה `print_board(board)`**:
    - מדפיסה את לוח המשחק הנוכחי למסוף. היא מציגה את הלוח בצורה גרפית קריאה, עם מספרי משבצות כדי שהמשתמש יוכל לבחור את המשבצת הרצויה.
3.  **פונקציה `check_win(board, player)`**:
    - בודקת האם השחקן שצוין (player) ניצח במשחק.
    - היא בודקת את כל השורות, העמודות והאלכסונים בלוח, ומוודאת האם יש רצף של 3 סימנים זהים (איקס או עיגול)
    - מחזירה `True` אם נמצא ניצחון ו `False` אחרת.
4.  **פונקציה `is_board_full(board)`**:
    - בודקת האם לוח המשחק מלא, כלומר האם אין יותר מקומות פנויים.
    - מחזירה `True` אם הלוח מלא ו `False` אם יש מקומות פנויים.
5.  **פונקציה `computer_move(board)`**:
    - המחשב בוחר משבצת פנויה אקראית.
    - הוא בוחר שורה ועמודה אקראיות, ואם המשבצת פנויה, הוא מחזיר את השורה והעמודה.
    - אם המשבצת תפוסה, הוא ממשיך לבחור משבצת אחרת עד שהוא מוצא אחת פנויה.
6.  **פונקציה `play_tic_tac_toe()`**:
    - זוהי הפונקציה הראשית שמנהלת את מהלך המשחק.
    - היא יוצרת לוח משחק ריק, מגדירה את הסימנים של השחקן והמחשב, ומתחילה לולאה ראשית של המשחק.
    - בתוך הלולאה, הפונקציה מבצעת את הפעולות הבאות:
        - מציגה את לוח המשחק.
        - מבקשת מהשחקן לבחור משבצת.
        - מעדכנת את לוח המשחק עם הבחירה של השחקן.
        - בודקת האם השחקן ניצח.
        - אם השחקן לא ניצח, בודקת האם הלוח מלא.
        - אם הלוח לא מלא, מבצעת את מהלך המחשב.
        - מעדכנת את לוח המשחק עם הבחירה של המחשב.
        - בודקת האם המחשב ניצח.
        - אם המחשב לא ניצח, בודקת האם הלוח מלא.
    - אם המשחק הסתיים בניצחון או בתיקו, יוצאים מהלולאה, ומודפסת הודעה מתאימה.
7.  **הפעלה של הפונקציה הראשית**:
     - `if __name__ == "__main__":`: הבלוק הזה מאפשר הפעלה של המשחק רק אם הסקריפט מורץ ישירות, ולא אם הוא יובא כמודול
     -  `play_tic_tac_toe()`: הפעלת פונקצית המשחק.
"""
