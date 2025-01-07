<GOMOKO>:
=================
קושי: 7
-----------------
גומוקו הוא משחק לוח אסטרטגי לשני שחקנים, שבו המטרה היא ליצור רצף של חמישה אבנים בצבע שלך בשורה אופקית, אנכית או אלכסונית על גבי לוח המשחק. השחקנים מתחלפים בהנחת אבנים על לוח ריק.
חוקי המשחק:
1. לוח המשחק הוא רשת של 19X19 נקודות.
2. שני שחקנים מתחלפים בתורם, כאשר שחקן אחד משחק עם "X" והשני עם "O".
3. כל שחקן מניח אבן בצבע שלו על נקודה פנויה בלוח המשחק.
4. השחקן הראשון שיוצר רצף של חמישה אבנים בצבע שלו בשורה אופקית, אנכית או אלכסונית, מנצח.
5. אם כל לוח המשחק מתמלא מבלי שאף שחקן יצר רצף של חמישה אבנים, המשחק מסתיים בתיקו.
-----------------
אלגוריתם:
1. אתחל לוח משחק ריק בגודל 19x19 (מיוצג על ידי רשימה דו-ממדית).
2. הגדר את השחקן הנוכחי לשחקן 'X'.
3. התחל לולאה ראשית:
    3.1. הצג את לוח המשחק הנוכחי.
    3.2. בקש מהשחקן הנוכחי להזין את קואורדינטות (שורות ועמודות) למיקום האבן.
    3.3. ודא שהקואורדינטות שהוזנו תקינות ושהמיקום בלוח פנוי. אם לא, בקש קלט מחדש.
    3.4. הנח את האבן של השחקן הנוכחי על הלוח.
    3.5. בדוק אם השחקן הנוכחי ניצח (יצר רצף של 5 אבנים).
    3.6. אם השחקן ניצח, הצג הודעה על ניצחון וסיים את המשחק.
    3.7. אם הלוח מלא, הצג הודעה על תיקו וסיים את המשחק.
    3.8. העבר את התור לשחקן השני (החלף את השחקן הנוכחי ל-'O' אם השחקן הנוכחי היה 'X', ולהיפך).
4. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeBoard["אתחול לוח ריק 19x19"]
    InitializeBoard --> SetCurrentPlayer["הגדר שחקן נוכחי = 'X'"]
    SetCurrentPlayer --> GameLoopStart{"תחילת לולאה ראשית"}
    GameLoopStart --> DisplayBoard["הצגת לוח"]
    DisplayBoard --> InputCoordinates["קלט קואורדינטות מהשחקן הנוכחי"]
    InputCoordinates --> ValidateCoordinates{"בדיקת קואורדינטות תקינות ומיקום פנוי?"}
    ValidateCoordinates -- לא --> InputCoordinates
    ValidateCoordinates -- כן --> PlaceStone["הנחת אבן של השחקן הנוכחי"]
    PlaceStone --> CheckWin["האם השחקן הנוכחי ניצח?"]
    CheckWin -- כן --> OutputWin["הודעת ניצחון"]
    OutputWin --> End["סוף"]
    CheckWin -- לא --> CheckBoardFull["האם הלוח מלא?"]
    CheckBoardFull -- כן --> OutputTie["הודעת תיקו"]
    OutputTie --> End
    CheckBoardFull -- לא --> SwitchPlayer["החלפת שחקן נוכחי"]
    SwitchPlayer --> GameLoopStart
```
Legenda:
    Start - התחלת התוכנית.
    InitializeBoard - אתחול לוח המשחק כרשת ריקה בגודל 19x19.
    SetCurrentPlayer - הגדרת השחקן הנוכחי להתחיל כשחקן 'X'.
    GameLoopStart - תחילת הלולאה הראשית של המשחק.
    DisplayBoard - הצגת לוח המשחק הנוכחי למשתמש.
    InputCoordinates - קבלת קלט של קואורדינטות (שורות ועמודות) מהשחקן הנוכחי.
    ValidateCoordinates - בדיקה שהקואורדינטות שהוזנו תקינות ושהמיקום בלוח פנוי.
    PlaceStone - הנחת אבן של השחקן הנוכחי במיקום שצוין בלוח.
    CheckWin - בדיקה האם השחקן הנוכחי יצר רצף של 5 אבנים (ניצח).
    OutputWin - הצגת הודעת ניצחון וסיום המשחק.
    CheckBoardFull - בדיקה האם לוח המשחק מלא.
    OutputTie - הצגת הודעה על תיקו וסיום המשחק.
    SwitchPlayer - העברת התור לשחקן השני.
    End - סוף התוכנית.
"""
```python
# -*- coding: utf-8 -*-
"""
 GOMOKO:
 =================
 קושי: 7
 -----------------
 גומוקו הוא משחק לוח אסטרטגי לשני שחקנים, שבו המטרה היא ליצור רצף של חמישה אבנים בצבע שלך בשורה אופקית, אנכית או אלכסונית על גבי לוח המשחק. השחקנים מתחלפים בהנחת אבנים על לוח ריק.
 חוקי המשחק:
 1. לוח המשחק הוא רשת של 19X19 נקודות.
 2. שני שחקנים מתחלפים בתורם, כאשר שחקן אחד משחק עם "X" והשני עם "O".
 3. כל שחקן מניח אבן בצבע שלו על נקודה פנויה בלוח המשחק.
 4. השחקן הראשון שיוצר רצף של חמישה אבנים בצבע שלו בשורה אופקית, אנכית או אלכסונית, מנצח.
 5. אם כל לוח המשחק מתמלא מבלי שאף שחקן יצר רצף של חמישה אבנים, המשחק מסתיים בתיקו.
 -----------------
 אלגוריתם:
 1. אתחל לוח משחק ריק בגודל 19x19 (מיוצג על ידי רשימה דו-ממדית).
 2. הגדר את השחקן הנוכחי לשחקן 'X'.
 3. התחל לולאה ראשית:
     3.1. הצג את לוח המשחק הנוכחי.
     3.2. בקש מהשחקן הנוכחי להזין את קואורדינטות (שורות ועמודות) למיקום האבן.
     3.3. ודא שהקואורדינטות שהוזנו תקינות ושהמיקום בלוח פנוי. אם לא, בקש קלט מחדש.
     3.4. הנח את האבן של השחקן הנוכחי על הלוח.
     3.5. בדוק אם השחקן הנוכחי ניצח (יצר רצף של 5 אבנים).
     3.6. אם השחקן ניצח, הצג הודעה על ניצחון וסיים את המשחק.
     3.7. אם הלוח מלא, הצג הודעה על תיקו וסיים את המשחק.
     3.8. העבר את התור לשחקן השני (החלף את השחקן הנוכחי ל-'O' אם השחקן הנוכחי היה 'X', ולהיפך).
 4. סוף המשחק.
 -----------------
 תרשים זרימה:
 ```mermaid
 flowchart TD
     Start["התחלה"] --> InitializeBoard["אתחול לוח ריק 19x19"]
     InitializeBoard --> SetCurrentPlayer["הגדר שחקן נוכחי = 'X'"]
     SetCurrentPlayer --> GameLoopStart{"תחילת לולאה ראשית"}
     GameLoopStart --> DisplayBoard["הצגת לוח"]
     DisplayBoard --> InputCoordinates["קלט קואורדינטות מהשחקן הנוכחי"]
     InputCoordinates --> ValidateCoordinates{"בדיקת קואורדינטות תקינות ומיקום פנוי?"}
     ValidateCoordinates -- לא --> InputCoordinates
     ValidateCoordinates -- כן --> PlaceStone["הנחת אבן של השחקן הנוכחי"]
     PlaceStone --> CheckWin["האם השחקן הנוכחי ניצח?"]
     CheckWin -- כן --> OutputWin["הודעת ניצחון"]
     OutputWin --> End["סוף"]
     CheckWin -- לא --> CheckBoardFull["האם הלוח מלא?"]
     CheckBoardFull -- כן --> OutputTie["הודעת תיקו"]
     OutputTie --> End
     CheckBoardFull -- לא --> SwitchPlayer["החלפת שחקן נוכחי"]
     SwitchPlayer --> GameLoopStart
 ```
 Legenda:
     Start - התחלת התוכנית.
     InitializeBoard - אתחול לוח המשחק כרשת ריקה בגודל 19x19.
     SetCurrentPlayer - הגדרת השחקן הנוכחי להתחיל כשחקן 'X'.
     GameLoopStart - תחילת הלולאה הראשית של המשחק.
     DisplayBoard - הצגת לוח המשחק הנוכחי למשתמש.
     InputCoordinates - קבלת קלט של קואורדינטות (שורות ועמודות) מהשחקן הנוכחי.
     ValidateCoordinates - בדיקה שהקואורדינטות שהוזנו תקינות ושהמיקום בלוח פנוי.
     PlaceStone - הנחת אבן של השחקן הנוכחי במיקום שצוין בלוח.
     CheckWin - בדיקה האם השחקן הנוכחי יצר רצף של 5 אבנים (ניצח).
     OutputWin - הצגת הודעת ניצחון וסיום המשחק.
     CheckBoardFull - בדיקה האם לוח המשחק מלא.
     OutputTie - הצגת הודעה על תיקו וסיום המשחק.
     SwitchPlayer - העברת התור לשחקן השני.
     End - סוף התוכנית.
 """

"""
הסברים:
הקוד מממש את משחק הלוח גומוקו (Gomoku) בסיסי.
המשחק מתנהל בין שני שחקנים, כאשר כל שחקן מנסה ליצור רצף של 5 אבנים בצבע שלו (X או O) על לוח בגודל 19x19.
המשחק ממשיך עד שאחד השחקנים מנצח או שהלוח מתמלא ללא מנצח (תיקו).

הקוד משתמש בפונקציות ומשתנים לצורך ארגון הקוד ולשיפור קריאותו.
הקוד גם כולל בדיקות קלט כדי לוודא שהמשתמש מזין קואורדינטות תקינות.
"""
# גודל לוח המשחק
BOARD_SIZE = 19

# פונקציה לאתחול לוח המשחק
def create_board():
    """
    יוצרת לוח משחק ריק בגודל BOARD_SIZE x BOARD_SIZE.

    Returns:
        list: רשימה דו-ממדית המייצגת את לוח המשחק.
    """
    return [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# פונקציה להדפסת הלוח
def print_board(board):
    """
    מדפיסה את לוח המשחק למסך.
    משתמשת בלולאות כדי לעבור על השורות והעמודות ולהדפיס את התאים.
    Args:
        board (list): לוח המשחק להדפסה.
    """
    print("   " + " ".join(str(i % 10) for i in range(BOARD_SIZE)))  # הדפסת מספרי עמודות
    for i, row in enumerate(board):
        print(f"{i % 10:2d} " + " ".join(row)) # הדפסת מספרי שורות ותוכן כל שורה

# פונקציה להנחת אבן על הלוח
def place_stone(board, row, col, player):
    """
    מניחה אבן של השחקן (player) במקום שצוין בלוח (row, col).

    Args:
        board (list): לוח המשחק.
        row (int): שורת המיקום של האבן.
        col (int): עמודת המיקום של האבן.
        player (str): השחקן הנוכחי ('X' או 'O').

    """
    board[row][col] = player

# פונקציה לבדיקת ניצחון
def check_win(board, row, col, player):
    """
    בודקת אם השחקן הנוכחי ניצח על ידי יצירת רצף של 5 אבנים.

    Args:
        board (list): לוח המשחק.
        row (int): שורת המיקום של האבן האחרונה שהונחה.
        col (int): עמודת המיקום של האבן האחרונה שהונחה.
        player (str): השחקן הנוכחי ('X' או 'O').

    Returns:
        bool: True אם השחקן ניצח, False אחרת.
    """
    # בדיקה בכיוון האופקי
    count = 0
    for c in range(max(0, col - 4), min(BOARD_SIZE, col + 5)):
        if board[row][c] == player:
            count += 1
            if count == 5:
                return True
        else:
            count = 0

    # בדיקה בכיוון האנכי
    count = 0
    for r in range(max(0, row - 4), min(BOARD_SIZE, row + 5)):
        if board[r][col] == player:
            count += 1
            if count == 5:
                return True
        else:
            count = 0

    # בדיקה באלכסון הראשי
    count = 0
    for i in range(-4, 5):
        r, c = row + i, col + i
        if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == player:
            count += 1
            if count == 5:
                return True
        else:
            count = 0

    # בדיקה באלכסון המשני
    count = 0
    for i in range(-4, 5):
      r, c = row + i, col - i
      if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == player:
          count += 1
          if count == 5:
              return True
      else:
          count = 0
    return False

# פונקציה לבדיקה אם הלוח מלא
def is_board_full(board):
    """
    בודקת אם לוח המשחק מלא (אין יותר מקומות פנויים).

    Args:
        board (list): לוח המשחק.

    Returns:
        bool: True אם הלוח מלא, False אחרת.
    """
    for row in board:
        if ' ' in row:
            return False
    return True

# פונקציה לקבלת קלט מהמשתמש
def get_user_input(player):
    """
    מקבלת קלט מהמשתמש עבור קואורדינטות של המהלך.

    Args:
        player (str): השחקן הנוכחי ('X' או 'O').

    Returns:
        tuple: טופלה שמכילה את השורה והעמודה שהוזנו על ידי המשתמש, או None אם הקלט לא תקין.
    """
    while True:
        try:
            move = input(f"Player {player}, enter your move (row, col): ").split(',')
            if len(move) != 2:
                print("Invalid input. Please enter row, col separated by a comma.")
                continue
            row, col = int(move[0].strip()), int(move[1].strip())
            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
              return row, col
            else:
               print("Invalid move. Please enter valid row and col.")
        except ValueError:
            print("Invalid input. Please enter numbers for row and col.")


# פונקציה שמנהלת את המשחק
def play_gomoku():
    """
    מנהלת את מהלך המשחק.
    מאתחלת את הלוח, מנהלת את תורות השחקנים,
    בודקת ניצחון ומציגה הודעות מתאימות בהתאם.
    """
    board = create_board()
    current_player = 'X'
    while True:
      print_board(board)
      row, col = get_user_input(current_player)

      if board[row][col] != ' ':
        print("This position is already occupied, try again")
        continue

      place_stone(board, row, col, current_player)

      if check_win(board, row, col, current_player):
        print_board(board)
        print(f"Player {current_player} wins!")
        break

      if is_board_full(board):
        print_board(board)
        print("It's a tie!")
        break

      current_player = 'O' if current_player == 'X' else 'X'

# הפעלת המשחק
if __name__ == "__main__":
    play_gomoku()
```
<הערות סיום>
הקוד מציג יישום בסיסי של משחק גומוקו.
הוא משתמש בפונקציות ליצירת לוח, להדפסת הלוח, להנחת אבנים, לבדיקת ניצחון ולבדיקה אם הלוח מלא.
משחק גומוקו הוא משחק מעניין ואסטרטגי.
הקוד מספק פלט משחק בסיסי שאפשר להרחיב כדי ליצור ממשק משתמש גרפי או אפשרויות נוספות.
</הערות סיום>
