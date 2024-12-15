<CHECKR>:
=================
קושי: 5
-----------------
המשחק "דמקה" הוא משחק לוח לשני שחקנים, בו מנסים להגיע עם הכלים לצד השני של הלוח, ובכך לנצח. המשחק משוחק על לוח דמקה סטנדרטי של 8x8. השחקנים מתחלפים בתורות, ומזיזים את כלי המשחק שלהם באלכסון, וביכולתם לדלג מעל כלי יריב כדי להוציא אותם מהלוח.

חוקי המשחק:
1. המשחק משוחק על לוח 8x8 כאשר כל שחקן מתחיל עם 12 כלים.
2. כלים זזים באלכסון צעד אחד קדימה (לכיוון הצד השני של הלוח).
3. אם כלי נמצא מעל כלי יריב, והמשבצת הבאה פנויה, השחקן יכול לדלג מעל כלי היריב, להוציא אותו מהלוח.
4. שחקן יכול לבצע מספר קפיצות בתור אחד.
5. אם כלי מגיע לצד השני של הלוח, הוא הופך ל"מלך" ויכול לזוז אחורה וגם קדימה.
6. המטרה היא להוריד את כל כלי היריב או למנוע מהם לזוז.
-----------------
אלגוריתם:
1. אתחול לוח המשחק עם כלים של שני השחקנים (מיוצגים על ידי '1' ו-'2').
2. הצגת הלוח למשתמש.
3. הגדרת השחקן הנוכחי.
4. לולאה ראשית: כל עוד ישנם מהלכים אפשריים עבור שני השחקנים.
   4.1. הצג לשחקן הנוכחי את האפשרויות שלו.
   4.2. קבל קלט מהשחקן: מיקום כלי ומיקום היעד.
   4.3. בצע בדיקה: האם המהלך חוקי?
      4.3.1. האם הכלי שייך לשחקן הנוכחי?
      4.3.2. האם מיקום היעד חוקי (לא מחוץ ללוח, והאם משבצת פנויה או שיש בה כלי של היריב)?
      4.3.3. האם המהלך הוא קפיצה? (אם כן, הסר את הכלי שנדרס)
   4.4. בצע את המהלך בפועל.
   4.5. אם הכלי הגיע לקצה הלוח, קדם אותו למלך.
   4.6. החלף שחקן.
5. הצג הודעת ניצחון לשחקן שהצליח להוריד את כל כלי היריב או מנע ממנו לזוז.

-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeBoard["אתחול לוח המשחק"]
    InitializeBoard --> DisplayBoard["הצגת לוח"]
    DisplayBoard --> SetCurrentPlayer["הגדרת שחקן נוכחי"]
    SetCurrentPlayer --> GameLoop{"לולאת משחק: כל עוד יש מהלכים"}
    GameLoop -- כן --> DisplayOptions["הצגת אפשרויות לשחקן"]
    DisplayOptions --> GetInput["קבלת קלט משחקן"]
    GetInput --> ValidateMove{"בדיקת מהלך"}
    ValidateMove -- מהלך תקין --> ExecuteMove["ביצוע מהלך"]
    ExecuteMove --> CheckPromotion{"בדיקת קידום כלי"}
    CheckPromotion --> PromotePiece["קידום כלי למלך"]
     CheckPromotion --> SwitchPlayer["החלפת שחקן"]
    SwitchPlayer --> DisplayBoard
    PromotePiece --> SwitchPlayer
    ValidateMove -- מהלך לא תקין --> DisplayOptions
    GameLoop -- לא --> DisplayWinner["הצגת מנצח"]
    DisplayWinner --> End["סוף"]
```
Legenda:
    Start - התחלת התוכנית.
    InitializeBoard - אתחול לוח המשחק עם מיקום התחלתי של הכלים.
    DisplayBoard - הצגת לוח המשחק למשתמש.
    SetCurrentPlayer - הגדרת השחקן שמתחיל את התור.
    GameLoop - לולאה שרצה כל עוד המשחק לא הסתיים.
    DisplayOptions - הצגת אפשרויות המהלך לשחקן הנוכחי.
    GetInput - קבלת קלט מהמשתמש (בחירת כלי ויעד).
    ValidateMove - בדיקה אם המהלך חוקי לפי חוקי המשחק.
    ExecuteMove - ביצוע המהלך על לוח המשחק.
    CheckPromotion - בדיקה האם כלי הגיע לקצה הלוח וניתן לקדם אותו למלך.
    PromotePiece - קידום כלי למלך אם הגיע לקצה.
    SwitchPlayer - החלפת השחקן הנוכחי.
    DisplayWinner - הצגת הודעה עם שם המנצח.
    End - סוף התוכנית.

"""
import copy


# פונקציה לאתחול לוח המשחק
def initialize_board():
    # יצירת לוח 8x8 ריק
    board = [[' ' for _ in range(8)] for _ in range(8)]

    # הצבת כלים לשחקן 1
    for row in range(0, 3):
        for col in range(8):
            if (row + col) % 2 == 1:
                board[row][col] = '1'

    # הצבת כלים לשחקן 2
    for row in range(5, 8):
        for col in range(8):
            if (row + col) % 2 == 1:
                board[row][col] = '2'

    return board


# פונקציה להצגת הלוח
def display_board(board):
    print("  0 1 2 3 4 5 6 7")
    for i, row in enumerate(board):
        print(i, " ".join(row))


# פונקציה לבדוק מהלכים חוקיים
def validate_move(board, start_row, start_col, end_row, end_col, current_player):
    # בדיקה האם הקואורדינטות חוקיות
    if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
        print("קואורדינטות לא חוקיות.")
        return False

    # בדיקה האם יש כלי של השחקן במיקום ההתחלה
    piece = board[start_row][start_col]
    if piece != str(current_player) and piece != str(current_player).upper():
        print("זה לא הכלי שלך.")
        return False

    # חישוב תזוזה בשורות ועמודות
    row_diff = end_row - start_row
    col_diff = end_col - start_col
    abs_row_diff = abs(row_diff)
    abs_col_diff = abs(col_diff)

    # מהלך רגיל
    if abs_row_diff == 1 and abs_col_diff == 1:
        # בדיקה שהמשבצת ריקה
        if board[end_row][end_col] == ' ':
            if current_player == 1:
                if row_diff > 0:
                    return True
            elif current_player == 2:
                if row_diff < 0:
                    return True
        else:
             print("משבצת היעד אינה ריקה.")
             return False

    # מהלך קפיצה
    elif abs_row_diff == 2 and abs_col_diff == 2:
        # מציאת קואורדינטות הקפיצה
        jumped_row = (start_row + end_row) // 2
        jumped_col = (start_col + end_col) // 2

        # בדיקה שהמשבצת ריקה
        if board[end_row][end_col] != ' ':
             print("משבצת היעד אינה ריקה.")
             return False

        # בדיקה האם יש כלי של שחקן אחר בקפיצה
        jumped_piece = board[jumped_row][jumped_col]
        if jumped_piece == ' ' or jumped_piece == str(current_player) or jumped_piece == str(current_player).upper():
            print("אין כלי לקפוץ מעליו.")
            return False

        return True
    
    print("מהלך לא חוקי")
    return False


# פונקציה לביצוע מהלך
def execute_move(board, start_row, start_col, end_row, end_col, current_player):
    piece = board[start_row][start_col]
    board[start_row][start_col] = ' '
    board[end_row][end_col] = piece

    # אם המהלך הוא קפיצה, הסר את הכלי שנדרס
    row_diff = abs(end_row - start_row)
    col_diff = abs(end_col - start_col)

    if row_diff == 2 and col_diff == 2:
         jumped_row = (start_row + end_row) // 2
         jumped_col = (start_col + end_col) // 2
         board[jumped_row][jumped_col] = ' '


# פונקציה לבדוק אם כלי הגיע לקצה הלוח
def check_promotion(board, end_row, end_col, current_player):
    if current_player == 1 and end_row == 7:
         board[end_row][end_col] = '1'.upper()
         return True
    elif current_player == 2 and end_row == 0:
         board[end_row][end_col] = '2'.upper()
         return True
    return False

# פונקציה לבדיקה אם יש מהלכים אפשריים
def has_valid_moves(board, current_player):
    for row in range(8):
         for col in range(8):
             piece = board[row][col]
             if piece == str(current_player) or piece == str(current_player).upper():
                 # בדיקה מהלכים רגילים
                 for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                      new_row, new_col = row + dr, col + dc
                      if validate_move(board, row, col, new_row, new_col, current_player):
                         return True

                 # בדיקה מהלכי קפיצה
                 for dr, dc in [(-2, -2), (-2, 2), (2, -2), (2, 2)]:
                      new_row, new_col = row + dr, col + dc
                      if validate_move(board, row, col, new_row, new_col, current_player):
                         return True
    return False

# פונקציה לסיים את המשחק
def check_winner(board):
    player1_pieces = 0
    player2_pieces = 0

    for row in board:
        for cell in row:
            if cell == '1' or cell == '1'.upper():
                player1_pieces += 1
            elif cell == '2' or cell == '2'.upper():
                player2_pieces += 1

    if player1_pieces == 0:
        return 2
    elif player2_pieces == 0:
        return 1
    else:
        return 0


# פונקציית המשחק הראשית
def play_checkers():
    board = initialize_board()
    current_player = 1  # שחקן 1 מתחיל
    display_board(board)

    while True:
        if not has_valid_moves(board, current_player):
            other_player = 3 - current_player
            winner = check_winner(board)
            if winner != 0:
                print(f"שחקן {winner} ניצח!")
                break
            else:
                print(f"לשחקן {current_player} אין מהלכים, שחקן {other_player} מנצח!")
                break


        print(f"תור שחקן {current_player}")
        while True:
            try:
                start_row = int(input("בחר שורה של הכלי: "))
                start_col = int(input("בחר עמודה של הכלי: "))
                end_row = int(input("בחר שורה של המיקום יעד: "))
                end_col = int(input("בחר עמודה של מיקום היעד: "))
                if validate_move(board, start_row, start_col, end_row, end_col, current_player):
                  break
            except ValueError:
                print("קלט לא חוקי, אנא הזן מספרים שלמים.")

        execute_move(board, start_row, start_col, end_row, end_col, current_player)
        check_promotion(board, end_row, end_col, current_player)
        display_board(board)

        current_player = 3 - current_player  # החלף שחקן


if __name__ == "__main__":
    play_checkers()
"""
הסבר הקוד:
1.  **ייבוא המודול `copy`**:
    -   `import copy`: ייבוא מודול copy, המשמש ליצירת עותקים עמוקים של אובייקטים.

2.  **פונקציה `initialize_board()`**:
    -   פונקציה היוצרת לוח משחק ריק 8x8, ולאחר מכן מציבה את כלי המשחק ההתחלתיים עבור שני השחקנים.
    -   השחקן הראשון (1) מיוצג ע"י '1' והשחקן השני (2) מיוצג ע"י '2'.

3.  **פונקציה `display_board(board)`**:
    -   מקבלת את לוח המשחק ומדפיסה אותו בצורה קריאה למשתמש עם מספרי שורות ועמודות.

4.  **פונקציה `validate_move(board, start_row, start_col, end_row, end_col, current_player)`**:
    -   פונקציה זו בודקת האם מהלך מסוים הוא חוקי.
    -   מקבלת את לוח המשחק, קואורדינטות ההתחלה והסיום של המהלך, ואת השחקן הנוכחי.
    -   בדיקות חוקיות: קואורדינטות בתוך הלוח, כלי שייך לשחקן הנוכחי, האם המשבצת היעד ריקה, האם המהלך הוא מהלך חוקי או קפיצה מעל כלי.
    -   מחזירה True אם המהלך חוקי, False אחרת.

5.  **פונקציה `execute_move(board, start_row, start_col, end_row, end_col, current_player)`**:
    -   מבצעת את המהלך בפועל על לוח המשחק.
    -   מעדכנת את לוח המשחק לפי המהלך שבוצע (הזזת כלי, והסרת כלי שנדרס בקפיצה).

6.  **פונקציה `check_promotion(board, end_row, end_col, current_player)`**:
     - בודקת האם כלי הגיע לקצה הלוח, ומקדמת אותו למלך.
     - המלכים מסומנים באותיות גדולות ('1' -> 'A', '2' -> 'B')

7. **פונקציה `has_valid_moves(board, current_player)`**:
   - בודקת האם יש לשחקן מהלכים חוקיים בכלל, ומחזירה TRUE אם יש כאלה, ו-FALSE אחרת.

8.  **פונקציה `check_winner(board)`**:
      - בודקת אם המשחק הסתיים על ידי בדיקה האם אחד השחקנים איבד את כל הכלים שלו.
      - אם שחקן 1 ניצח - תחזיר 1, אם שחקן 2 ניצח - תחזיר 2, ואם אף אחד לא ניצח עדיין - תחזיר 0.

9.  **פונקציה `play_checkers()`**:
    -   הפונקציה הראשית של המשחק, המנהלת את זרימת המשחק.
    -   כוללת לולאה ראשית שרצה עד שהמשחק מסתיים (אחד השחקנים ניצח או לא נותרו מהלכים חוקיים לשחקנים).
    -   בכל סיבוב, הפונקציה מקבלת קלט מהשחקן הנוכחי, בודקת את תקינות המהלך, ומבצעת אותו.
    -   לאחר מכן, הפונקציה מעדכנת את מצב הלוח ומציגה אותו למשתמש, ומעבירה את התור לשחקן השני.

10. **חלק הקוד `if __name__ == "__main__":`**:
    - מבטיח שהפונקציה `play_checkers()` תופעל רק כאשר הקובץ מורץ ישירות, ולא כאשר הוא מיובא כמודול.
"""
