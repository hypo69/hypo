<AWARI>:
=================
קושי: 5
-----------------
משחק אווארי הוא משחק לוח אסטרטגי לשני שחקנים, המשוחק על לוח עם שורות של גומות. כל שחקן שולט בשורה אחת של גומות. בתחילת המשחק, כל גומה מכילה מספר מסוים של אבנים. מטרת המשחק היא לאסוף יותר אבנים מהיריב. במהלך התור, שחקן בוחר גומה משלו, ומשתמש באבנים שבה כדי לזרוע אותן אחת אחת בגומות הבאות. אם האבן האחרונה מגיעה לגומה שמכילה אבן נוספת, כל האבנים בגומה זו מועברות לגומה הבאה. השחקן אוסף את האבנים כשהוא מסיים את זריעת האבנים בגומה ריקה.

חוקי המשחק:
1. הלוח מורכב משתי שורות של גומות, כאשר לכל שחקן שורה אחת.
2. כל גומה מכילה מספר מסוים של אבנים בתחילת המשחק.
3. בתורו, שחקן בוחר גומה משלו שאינה ריקה, ומשתמש באבנים שבה לזרוע אותן אחת אחת בגומות הבאות בכיוון השעון.
4. אם האבן האחרונה נוחתת בגומה שהיא לא ריקה, כל האבנים בגומה זו מועברות לזריעה, וזה ממשיך עד שהאבן האחרונה מגיעה לגומה ריקה.
5. כאשר האבן האחרונה מגיעה לגומה ריקה, השחקן אוסף את כל האבנים בגומה המקבילה של היריב.
6. המשחק מסתיים כאשר אחד השחקנים אינו יכול לבצע מהלך (כל הגומות שלו ריקות) או כאשר כל האבנים נאספו.
7. המנצח הוא השחקן עם מספר האבנים הרב ביותר בסוף המשחק.
-----------------
אלגוריתם:
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
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeBoard["אתחול לוח המשחק:
        <p align='left'>
        <code><b>
        board = [[4, 4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4, 4]]
        currentPlayer = 0
        </b></code>
        </p>"]
    InitializeBoard --> GameLoopStart{"תחילת לולאת המשחק: כל עוד המשחק לא הסתיים"}
    GameLoopStart -- כן --> DisplayBoard["הצגת לוח המשחק"]
    DisplayBoard --> GetInput["קלט מהשחקן: בחירת גומה <code><b>selectedPit</b></code>"]
    GetInput --> ValidateInput{"בדיקה: האם הגומה ריקה?"}
    ValidateInput -- כן --> DisplayError["הצגת הודעת שגיאה: הגומה ריקה"]
    DisplayError --> GetInput
    ValidateInput -- לא --> DistributeStones["זריעת אבנים מהגומה הנבחרת"]
    DistributeStones --> CheckLastStone{"בדיקה: האם האבן האחרונה נחתה בגומה לא ריקה?"}
    CheckLastStone -- כן --> DistributeFromLastPit["המשך זריעה מהגומה האחרונה"]
     DistributeFromLastPit --> CheckLastStone
    CheckLastStone -- לא --> CheckEmptyPit{"בדיקה: האם האבן האחרונה נחתה בגומה ריקה של השחקן הנוכחי?"}
    CheckEmptyPit -- כן --> CollectOppositeStones["איסוף אבנים מהגומה המקבילה של היריב"]
    CollectOppositeStones --> UpdateBoard["עדכון לוח המשחק"]
    CheckEmptyPit -- לא --> UpdateBoard
    UpdateBoard --> SwitchPlayer["החלפת תור שחקן <code><b>currentPlayer = 1 - currentPlayer</b></code>"]
    SwitchPlayer --> GameLoopStart
    GameLoopStart -- לא --> CheckGameEnd{"בדיקה: האם המשחק הסתיים?"}
    CheckGameEnd -- כן --> DetermineWinner["קביעת מנצח"]
    DetermineWinner --> OutputWinner["הצגת מנצח"]
    OutputWinner --> End["סוף המשחק"]
```

Legenda:
    Start - התחלת המשחק.
    InitializeBoard - אתחול לוח המשחק: יצירת לוח דו-ממדי המייצג את הגומות, אתחול מספר האבנים בכל גומה, והגדרת השחקן הנוכחי.
    GameLoopStart - תחילת הלולאה הראשית של המשחק, כל עוד המשחק לא הסתיים.
    DisplayBoard - הצגת לוח המשחק למשתמש.
    GetInput - קבלת קלט מהשחקן: בחירת גומה.
    ValidateInput - בדיקה האם הגומה שנבחרה ריקה.
    DisplayError - הצגת הודעה אם הגומה ריקה.
    DistributeStones - זריעת האבנים מהגומה שנבחרה לגומות הבאות.
    CheckLastStone - בדיקה האם האבן האחרונה נחתה בגומה שאינה ריקה.
     DistributeFromLastPit - המשך הזריעה מהגומה האחרונה (אם היא לא ריקה)
    CheckEmptyPit - בדיקה האם האבן האחרונה נחתה בגומה ריקה של השחקן הנוכחי.
    CollectOppositeStones - איסוף האבנים מהגומה המקבילה של היריב, אם התנאי הקודם מתקיים.
    UpdateBoard - עדכון לוח המשחק בהתאם למהלכים.
    SwitchPlayer - החלפת תור השחקן.
    CheckGameEnd - בדיקה האם המשחק הסתיים.
    DetermineWinner - קביעת המנצח על ידי השוואת כמות האבנים.
    OutputWinner - הצגת המנצח.
    End - סיום המשחק.
"""
__author__ = 'hypo69 (hypo69@davidka.net)'
import copy
# הסברים:
# משחק אווארי בסיסי למשתמש יחיד נגד המחשב
# אין ממשק גרפי, המשחק מתבצע באמצעות קלט טקסטואלי
# לוח המשחק מיוצג על ידי רשימה של רשימות - שורה אחת לשחקן ושורה אחת למחשב
# כל גומה מכילה מספר אבנים
# השחקן יכול לבחור גומה משלו בתורו
# האבנים מהגומה שנבחרה נזרעות אחת אחת בגומות הבאות
# אם האבן האחרונה נופלת על גומה ריקה, השחקן לוקח את כל האבנים בגומה המקבילה בצד השני
# המשחק מסתיים כשצד אחד לא יכול לבצע מהלך, או כשכל האבנים נאספו
# הרעיון הוא לשמור על פשטות, כך שיהיה מובן למתחילים
"""
licence:MIT(../licence)
"""
def initialize_board():
    """
    אתחול לוח המשחק
    
    :return: רשימה דו-ממדית המייצגת את לוח המשחק
    """
    # הלוח מיוצג כרשימה של רשימות, כאשר כל רשימה פנימית מייצגת שורה של גומות
    # כל גומה מכילה 4 אבנים בהתחלה
    return [[4, 4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4, 4]]


def display_board(board, player_turn):
    """
     מציג את לוח המשחק למשתמש.
    
    :param board: רשימה דו-ממדית המייצגת את לוח המשחק.
    :param player_turn: אינדקס השחקן שהתור שלו (0 - שחקן, 1 - מחשב).
    """

    print("--------------------")
    if player_turn == 0:
        print("   Your Turn   ")
    else:
         print("   Computer Turn   ")
    print("--------------------")
    print("Computer:", board[1])
    print("   1  2  3  4  5  6  7")
    print("You:     ", board[0])


def get_player_move(board):
    """
    מבקש מהשחקן לבחור גומה.
    
    :param board: רשימה דו-ממדית המייצגת את לוח המשחק.
    :return: אינדקס הגומה שנבחרה על ידי השחקן (0-6).
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


def make_move(board, player, pit):
    """
    מבצע את המהלך על הלוח.
    
    :param board: רשימה דו-ממדית המייצגת את לוח המשחק.
    :param player: אינדקס השחקן הנוכחי (0 - שחקן, 1 - מחשב).
    :param pit: אינדקס הגומה שנבחרה למהלך (0-6).
    :return: הלוח לאחר המהלך.
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

def is_game_over(board):
    """
    בודק אם המשחק הסתיים.
    
    :param board: רשימה דו-ממדית המייצגת את לוח המשחק.
    :return: True אם המשחק הסתיים, False אחרת.
    """
    return all(stones == 0 for stones in board[0]) or all(stones == 0 for stones in board[1])


def calculate_winner(board):
    """
    מחשב ומחזיר את המנצח, אם יש.
    :param board: לוח המשחק הנוכחי
    :return: מנצח המשחק (0 - שחקן, 1 - מחשב), -1 - תיקו.
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

def computer_move(board):
    """
    המחשב בוחר מהלך בצורה אקראית.
    
    :param board: רשימה דו-ממדית המייצגת את לוח המשחק.
    :return: אינדקס הגומה שנבחרה על ידי המחשב (0-6).
    """
    available_pits = [i for i, stones in enumerate(board[1]) if stones > 0]
    import random
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
2. **פונקציות**:
   -  `initialize_board()`: מאתחלת את לוח המשחק כרשימה דו ממדית, כאשר כל גומה מכילה 4 אבנים.
    -  `display_board(board, player_turn)`: מציגה את לוח המשחק הנוכחי למשתמש, כולל תורו של השחקן.
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
