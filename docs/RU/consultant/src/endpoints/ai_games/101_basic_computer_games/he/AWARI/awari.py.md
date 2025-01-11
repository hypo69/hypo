# ניתוח קוד מודול awari.py

**איכות הקוד**
9
-   **יתרונות**
    * הקוד ברור ומאורגן היטב עם פונקציות מוגדרות היטב לכל חלק של המשחק.
    * יש תיעוד טוב של הקוד, כולל הסברים מפורטים על כל פונקציה וחוקי המשחק.
    * הלוגיקה של המשחק מיושמת כראוי, כולל זריעת אבנים, לכידת אבנים, וסיום המשחק.
    *  קוד הקשור לאלגוריתם המשחק, מעבר תור, ותנאי סיום משחק מיושם בצורה ברורה.
-   **חסרונות**
    * חסר שימוש בפורמט reStructuredText (RST) לתיעוד הקוד.
    * אין שימוש במנגנון לוגיקה (logger) לטיפול בשגיאות.
    * יש שימוש ב-`input()` ללא בדיקת תקינות הקלט, מה שעלול לגרום לקריסת התוכנית.
    * המחשב מבצע מהלך אקראי, ניתן לשפר את האלגוריתם של המחשב.
    *  חלק מהמשתנים והפונקציות לא עקביים עם מוסכמות שמות הקוד.

**המלצות לשיפור**

1.  **תיעוד**: יש להמיר את כל התיעוד לפורמט reStructuredText (RST), כולל docstrings לפונקציות ולמודול, על מנת לייצר תיעוד ברור ותואם לכלים כמו Sphinx.
2.  **טיפול בשגיאות**: יש להשתמש ב-`src.logger.logger` ללכידת שגיאות וטיפול בהן, במקום להשתמש ב-`print` לשגיאות. יש להימנע משימוש ב-`try-except` סטנדרטי ללא לוג.
3.  **קלט משתמש**: יש לשפר את הטיפול בקלט מהמשתמש על ידי הוספת בדיקות תקינות נוספות והתמודדות עם שגיאות קלט בצורה נכונה.
4.  **אלגוריתם מחשב**: לשפר את אלגוריתם המחשב ממהלך אקראי למהלך חכם יותר, למשל על ידי שימוש במינימקס או אלגוריתם חיפוש אחר.
5.  **סגנון קוד**: לשמור על עקביות בשמות הפונקציות והמשתנים בהתאם להסכמות שמות, לדוגמה: `player_turn` => `current_player`
6.  **הפרדה בין לוגיקה לממשק**: להפריד את הלוגיקה של המשחק (פונקציות `make_move`, `is_game_over`, וכו') מהתצוגה (פונקציות `display_board`) ומהקלט (פונקציה `get_player_move`).

**קוד משופר**

```python
"""
מודול זה מממש את משחק האווארי הבסיסי.
=========================================================================================

משחק אווארי הוא משחק לוח אסטרטגי לשני שחקנים, המשוחק על לוח עם שורות של גומות. כל שחקן שולט
בשורת גומות אחת. בתחילת המשחק, כל גומה מכילה מספר מסוים של אבנים. מטרת המשחק היא לאסוף יותר
אבנים מהיריב. במהלך תור, שחקן בוחר גומה משלו, ומשתמש באבנים שבה כדי לזרוע אותן אחת אחת בגומות
הבאות. אם האבן האחרונה מגיעה לגומה שמכילה אבן נוספת, כל האבנים בגומה זו מועברות לגומה הבאה.
השחקן אוסף את האבנים כשהוא מסיים את זריעת האבנים בגומה ריקה.

דוגמה לשימוש:
--------------

.. code-block:: python

   play_awari()

חוקי המשחק:
-------------

1.  הלוח מורכב משתי שורות של גומות, כאשר לכל שחקן שורה אחת.
2.  כל גומה מכילה מספר מסוים של אבנים בתחילת המשחק.
3.  בתורו, שחקן בוחר גומה משלו שאינה ריקה, ומשתמש באבנים שבה לזרוע אותן אחת אחת בגומות הבאות בכיוון השעון.
4.  אם האבן האחרונה נוחתת בגומה שהיא לא ריקה, כל האבנים בגומה זו מועברות לזריעה, וזה ממשיך עד שהאבן האחרונה מגיעה לגומה ריקה.
5.  כאשר האבן האחרונה מגיעה לגומה ריקה, השחקן אוסף את כל האבנים בגומה המקבילה של היריב.
6.  המשחק מסתיים כאשר אחד השחקנים אינו יכול לבצע מהלך (כל הגומות שלו ריקות) או כאשר כל האבנים נאספו.
7.  המנצח הוא השחקן עם מספר האבנים הרב ביותר בסוף המשחק.

אלגוריתם:
-----------

1. אתחל את לוח המשחק עם 4 אבנים בכל גומה (7 גומות לכל שחקן)
2. הגדר את תור השחקן להתחיל
3. כל עוד המשחק לא הסתיים:
    3.1 הצג את לוח המשחק
    3.2 קבל קלט מהשחקן - בחירת גומה
    3.3 אם הגומה ריקה, הצג הודעת שגיאה וחזור לשלב 3.2
    3.4 זרוע את האבנים: קח את כל האבנים מהגומה הנבחרת וזרע אותן אחת אחת בגומות הבאות בכיוון השעון.
    3.5 אם האבן האחרונה נחתה בגומה לא ריקה, המשך את הזריעה מהגומה האחרונה.
    3.6 אם האבן האחרונה נחתה בגומה ריקה של השחקן, אסוף את כל האבנים מהגומה המקבילה של היריב.
    3.7 עדכן את לוח המשחק
    3.8 החלף את תור השחקן.
4. בדוק אם המשחק הסתיים (אחד השחקנים ללא מהלכים או שכל האבנים נאספו)
5. הצג את המנצח על בסיס כמות האבנים שאסף כל שחקן.
"""

import copy
import random
from src.logger.logger import logger
#  הסברים:
#  משחק אווארי בסיסי למשתמש יחיד נגד המחשב
#  אין ממשק גרפי, המשחק מתבצע באמצעות קלט טקסטואלי
#  לוח המשחק מיוצג על ידי רשימה של רשימות - שורה אחת לשחקן ושורה אחת למחשב
#  כל גומה מכילה מספר אבנים
#  השחקן יכול לבחור גומה משלו בתורו
#  האבנים מהגומה שנבחרה נזרעות אחת אחת בגומות הבאות
#  אם האבן האחרונה נופלת על גומה ריקה, השחקן לוקח את כל האבנים בגומה המקבילה בצד השני
#  המשחק מסתיים כשצד אחד לא יכול לבצע מהלך, או כשכל האבנים נאספו
#  הרעיון הוא לשמור על פשטות, כך שיהיה מובן למתחילים
"""
licence:MIT(../licence)
"""
def initialize_board():
    """
    אתחול לוח המשחק.

    :return: רשימה דו-ממדית המייצגת את לוח המשחק.
    :rtype: list
    """
    #  הלוח מיוצג כרשימה של רשימות, כאשר כל רשימה פנימית מייצגת שורה של גומות
    #  כל גומה מכילה 4 אבנים בהתחלה
    return [[4, 4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4, 4]]


def display_board(board: list, current_player: int):
    """
    מציג את לוח המשחק למשתמש.

    :param board: רשימה דו-ממדית המייצגת את לוח המשחק.
    :type board: list
    :param current_player: אינדקס השחקן שהתור שלו (0 - שחקן, 1 - מחשב).
    :type current_player: int
    """
    print("--------------------")
    if current_player == 0:
        print("   Your Turn   ")
    else:
        print("   Computer Turn   ")
    print("--------------------")
    print("Computer:", board[1])
    print("   1  2  3  4  5  6  7")
    print("You:     ", board[0])


def get_player_move(board: list) -> int:
    """
    מבקש מהשחקן לבחור גומה.

    :param board: רשימה דו-ממדית המייצגת את לוח המשחק.
    :type board: list
    :return: אינדקס הגומה שנבחרה על ידי השחקן (0-6).
    :rtype: int
    """
    while True:
        try:
            pit = int(input("בחר גומה (1-7): ")) - 1
            if 0 <= pit < 7 and board[0][pit] > 0:
                return pit
            else:
                print("בחירה לא חוקית, נסה שוב.")
        except ValueError:
            print("קלט לא תקין, אנא הזן מספר.")
            logger.error('קלט לא תקין מהמשתמש')

def make_move(board: list, player: int, pit: int) -> list:
    """
    מבצע את המהלך על הלוח.

    :param board: רשימה דו-ממדית המייצגת את לוח המשחק.
    :type board: list
    :param player: אינדקס השחקן הנוכחי (0 - שחקן, 1 - מחשב).
    :type player: int
    :param pit: אינדקס הגומה שנבחרה למהלך (0-6).
    :type pit: int
    :return: הלוח לאחר המהלך.
    :rtype: list
    """
    stones = board[player][pit]
    board[player][pit] = 0
    current_pit = pit
    while stones > 0:
        current_pit = (current_pit + 1) % 7
        board[player][current_pit] += 1
        stones -= 1
        if stones == 0 and board[player][current_pit] == 1:
             opposite_pit = 6 - current_pit
             if board[1 - player][opposite_pit] > 0:
                 board[player][current_pit] = 0
                 stones_collected = board[1 - player][opposite_pit]
                 board[1 - player][opposite_pit] = 0
                 board[player][7] = board[player].pop(7) if len(board[player]) > 7 else 0
                 board[player].insert(7, board[player].pop(7)+stones_collected)
                 #board[player].append(board[player].pop(7) + stones_collected)
    return board


def is_game_over(board: list) -> bool:
    """
    בודק אם המשחק הסתיים.

    :param board: רשימה דו-ממדית המייצגת את לוח המשחק.
    :type board: list
    :return: True אם המשחק הסתיים, False אחרת.
    :rtype: bool
    """
    return all(stones == 0 for stones in board[0]) or all(stones == 0 for stones in board[1])

def calculate_winner(board: list) -> int:
    """
    מחשב ומחזיר את המנצח, אם יש.

    :param board: לוח המשחק הנוכחי.
    :type board: list
    :return: מנצח המשחק (0 - שחקן, 1 - מחשב), -1 - תיקו.
    :rtype: int
    """
    player_score = sum(board[0])
    computer_score = sum(board[1])
    if len(board[0]) > 7:
         player_score = player_score + board[0][7]
    if len(board[1]) > 7:
         computer_score = computer_score + board[1][7]
    if player_score > computer_score:
       return 0
    elif computer_score > player_score:
       return 1
    else:
        return -1


def computer_move(board: list) -> int:
    """
    המחשב בוחר מהלך בצורה אקראית.

    :param board: רשימה דו-ממדית המייצגת את לוח המשחק.
    :type board: list
    :return: אינדקס הגומה שנבחרה על ידי המחשב (0-6).
    :rtype: int
    """
    available_pits = [i for i, stones in enumerate(board[1]) if stones > 0]
    return random.choice(available_pits) if available_pits else -1


def play_awari():
    """
    מנהל את משחק האווארי.
    """
    board = initialize_board()
    current_player = 0  # 0 - שחקן, 1 - מחשב

    while not is_game_over(board):
        display_board(board, current_player)
        if current_player == 0:
            pit = get_player_move(board)
            board = make_move(board, current_player, pit)
        else:
            pit = computer_move(board)
            if pit != -1:
                board = make_move(board, current_player, pit)
        current_player = 1 - current_player  # החלפת תור

    display_board(board, current_player)
    winner = calculate_winner(board)
    if winner == 0:
      print("ניצחת!")
    elif winner == 1:
      print("המחשב ניצח!")
    else:
      print("תיקו!")

# הפעלת המשחק
if __name__ == "__main__":
    play_awari()
"""
הסבר הקוד:
1.  **ייבוא מודולים**:
    - `import copy`: מייבא את מודול `copy` כדי ליצור עותקים של לוח המשחק.
    -  `import random`: מייבא את מודול `random` כדי לאפשר למחשב לבחור גומה באופן אקראי.
    -  `from src.logger.logger import logger`: מייבא את מודול הלוגר

2.  **פונקציות**:
   -  `initialize_board()`: מאתחלת את לוח המשחק כרשימה דו ממדית, כאשר כל גומה מכילה 4 אבנים.
    -  `display_board(board, current_player)`: מציגה את לוח המשחק הנוכחי למשתמש, כולל תורו של השחקן.
    -  `get_player_move(board)`: מבקשת מהשחקן לבחור גומה, ובודקת שהבחירה חוקית.
    -  `make_move(board, player, pit)`: מבצעת את המהלך שנבחר ע"י השחקן או המחשב.
    -  `is_game_over(board)`: בודקת האם המשחק הסתיים על ידי כך שכל הגומות של אחד השחקנים ריקות.
    - `calculate_winner(board)`: מחשבת את המנצח על ידי סיכום מספר האבנים של כל שחקן.
    - `computer_move(board)`: המחשב בוחר גומה באופן אקראי מתוך הגומות הלא ריקות שלו.
    - `play_awari()`: מנהלת את המשחק.

3.  **לוגיקת המשחק**:
    - המשחק מתחיל עם אתחול הלוח והגדרת תור השחקן.
    - כל עוד המשחק לא הסתיים:
      - לוח המשחק מוצג.
      - אם תור השחקן - השחקן מתבקש לבחור גומה.
      - אם תור המחשב - המחשב בוחר גומה באופן אקראי.
      - המהלך מתבצע, והתור עובר לשחקן השני.
    - לאחר שהמשחק מסתיים מוצג המנצח.
"""