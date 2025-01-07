# ניתוח קוד מודול gomoko

**איכות הקוד**
8
-   **יתרונות**
    *   הקוד קריא ומובן, עם שמות משתנים ופונקציות ברורים.
    *   הקוד מחולק לפונקציות קטנות וברורות, מה שמקל על תחזוקה ושימוש חוזר.
    *   הקוד מטפל בתקינות הקלט מהמשתמש.
    *   הקוד כולל בדיקה לניצחון ולתיקו, ומסתיים בהתאם.
    *   הקוד מתועד היטב בפורמט reStructuredText (RST).
-   **חסרונות**
    *   אין טיפול בשגיאות ברמה הלוגית (למשל, שגיאות פנימיות במהלך הבדיקה).
    *   הלוגיקה של בדיקת הניצחון יכולה להיות מורכבת יותר ויש מקום לייעל אותה.
    *   חסר שימוש ב-logger לתיעוד שגיאות או מידע בזמן ריצה.
    *   קלט המשתמש יכול להיות משופר עם בדיקות נוספות (למשל, קלט לא מספרי).

**המלצות לשיפור**

1.  **הוספת לוגיקה**: הוסף logger לרישום שגיאות ומידע. השתמש ב `from src.logger.logger import logger`.
2.  **ייעול בדיקת הניצחון**: ניתן לייעל את בדיקת הניצחון על ידי איחוד הלולאות לבדיקת קווים אופקיים, אנכיים ואלכסוניים לפונקציה אחת.
3.  **שיפור הקלט**: אפשר לשפר את קלט המשתמש על ידי הוספת בדיקות נוספות לוודא שהקלט תקין (לדוגמה, אם הוא לא מספר).
4.  **שימוש ב try-except**: יש להימנע משימוש מוגזם בבלוקים try-except, יש להשתמש ב-logger.error לטיפול בשגיאות.
5.  **הפרדת לוגיקה**: כדאי להפריד את הלוגיקה של המשחק מהפלט, מה שיאפשר גמישות רבה יותר בעיצוב המשחק.
6.  **תיעוד**: יש להקפיד על תיעוד מלא בפורמט RST לכל הפונקציות והמשתנים.

**קוד משופר**

```python
# -*- coding: utf-8 -*-
"""
מודול המממש את משחק גומוקו (Gomoku).
==================================================

המשחק מתנהל בין שני שחקנים, כאשר כל שחקן מנסה ליצור רצף של 5 אבנים בצבע שלו (X או O) על לוח בגודל 19x19.
המשחק ממשיך עד שאחד השחקנים מנצח או שהלוח מתמלא ללא מנצח (תיקו).
"""
import logging
from src.logger.logger import logger



# גודל לוח המשחק
BOARD_SIZE = 19

def create_board():
    """
    יוצר לוח משחק ריק בגודל BOARD_SIZE x BOARD_SIZE.

    :return: רשימה דו-ממדית המייצגת את לוח המשחק.
    :rtype: list
    """
    return [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def print_board(board):
    """
    מדפיסה את לוח המשחק למסך.

    :param board: לוח המשחק להדפסה.
    :type board: list
    """
    print("   " + " ".join(str(i % 10) for i in range(BOARD_SIZE))) # הדפסת מספרי עמודות
    for i, row in enumerate(board):
        print(f"{i % 10:2d} " + " ".join(row)) # הדפסת מספרי שורות ותוכן כל שורה


def place_stone(board, row, col, player):
    """
    מניחה אבן של השחקן (player) במקום שצוין בלוח (row, col).

    :param board: לוח המשחק.
    :type board: list
    :param row: שורת המיקום של האבן.
    :type row: int
    :param col: עמודת המיקום של האבן.
    :type col: int
    :param player: השחקן הנוכחי ('X' או 'O').
    :type player: str
    """
    board[row][col] = player

def _check_line(board, row, col, player, dr, dc):
    """
    בודקת האם יש רצף של 5 אבנים בכיוון מסוים.

    :param board: לוח המשחק.
    :type board: list
    :param row: שורת המיקום של האבן האחרונה שהונחה.
    :type row: int
    :param col: עמודת המיקום של האבן האחרונה שהונחה.
    :type col: int
    :param player: השחקן הנוכחי ('X' או 'O').
    :type player: str
    :param dr: שינוי בשורה (1, 0, -1).
    :type dr: int
    :param dc: שינוי בעמודה (1, 0, -1).
    :type dc: int
    :return: True אם נמצא רצף של 5 אבנים, False אחרת.
    :rtype: bool
    """
    count = 0
    for i in range(-4, 5):
        r, c = row + i * dr, col + i * dc
        if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == player:
            count += 1
            if count == 5:
                return True
        else:
            count = 0
    return False

def check_win(board, row, col, player):
    """
    בודקת אם השחקן הנוכחי ניצח על ידי יצירת רצף של 5 אבנים.

    :param board: לוח המשחק.
    :type board: list
    :param row: שורת המיקום של האבן האחרונה שהונחה.
    :type row: int
    :param col: עמודת המיקום של האבן האחרונה שהונחה.
    :type col: int
    :param player: השחקן הנוכחי ('X' או 'O').
    :type player: str
    :return: True אם השחקן ניצח, False אחרת.
    :rtype: bool
    """
    # בדיקה בכיוון האופקי
    if _check_line(board, row, col, player, 0, 1):
        return True
    # בדיקה בכיוון האנכי
    if _check_line(board, row, col, player, 1, 0):
        return True
    # בדיקה באלכסון הראשי
    if _check_line(board, row, col, player, 1, 1):
        return True
    # בדיקה באלכסון המשני
    if _check_line(board, row, col, player, 1, -1):
      return True
    return False

def is_board_full(board):
    """
    בודקת אם לוח המשחק מלא (אין יותר מקומות פנויים).

    :param board: לוח המשחק.
    :type board: list
    :return: True אם הלוח מלא, False אחרת.
    :rtype: bool
    """
    for row in board:
        if ' ' in row:
            return False
    return True

def get_user_input(player):
    """
    מקבלת קלט מהמשתמש עבור קואורדינטות של המהלך.

    :param player: השחקן הנוכחי ('X' או 'O').
    :type player: str
    :return: טופלה שמכילה את השורה והעמודה שהוזנו על ידי המשתמש, או None אם הקלט לא תקין.
    :rtype: tuple or None
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
        except ValueError as e:
            logger.error(f"Invalid input. Please enter numbers for row and col. Error: {e}")
            print("Invalid input. Please enter numbers for row and col.")
        except Exception as e:
            logger.error(f"An unexpected error occurred during input: {e}", exc_info=True)
            print("An unexpected error occurred. Please try again.")

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
      if row is None or col is None:
          continue

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

if __name__ == "__main__":
    play_gomoku()
```