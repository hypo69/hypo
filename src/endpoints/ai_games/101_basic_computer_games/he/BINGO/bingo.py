<BINGO>:
=================
קושי: 5
-----------------
משחק בינגו קלאסי לשחקן יחיד. השחקן מקבל לוח בינגו עם מספרים אקראיים, והמחשב מכריז על מספרים. מטרת השחקן היא לסמן את המספרים בלוח שלו עד שהוא יוצר שורה, עמודה או אלכסון מלאים, ואז הוא מכריז "בינגו" ומנצח. המשחק ממשיך עד שהשחקן מנצח.
חוקי המשחק:
1.  לוח בינגו 5x5 נוצר עם מספרים אקראיים בין 1 ל-75 (ללא חזרות).
2.  המחשב מכריז על מספרים אקראיים בין 1 ל-75.
3.  השחקן מסמן את המספרים בלוח הבינגו שלו אם הם הוכרזו.
4.  השחקן מנצח אם יש לו שורה, עמודה או אלכסון מלאים של מספרים מסומנים.
5.  המשחק ממשיך עד שהשחקן מנצח.
-----------------
אלגוריתם:
1.  אתחל לוח בינגו 5x5 עם מספרים אקראיים מ-1 עד 75, ללא חזרות.
2.  אתחל רשימה של מספרים שנקראו (כאשר היא ריקה).
3.  התחל לולאה "כל עוד אין ניצחון":
    3.1 בחר מספר אקראי בין 1 ל-75 שלא נקרא בעבר.
    3.2 הוסף את המספר לרשימת המספרים שנקראו.
    3.3 הצג את המספר שנקרא לשחקן.
    3.4 בדוק את לוח הבינגו:
        3.4.1 בדוק אם יש שורה מלאה.
        3.4.2 בדוק אם יש עמודה מלאה.
        3.4.3 בדוק אם יש אלכסון מלא.
    3.5 אם נמצא ניצחון:
        3.5.1 הצג הודעת ניצחון.
        3.5.2 צא מהלולאה.
    3.6 המשך הלולאה עד שיוכרז ניצחון.
4. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeBingoBoard["<p align='left'>אתחול לוח בינגו 5x5
    <br><code><b>bingoBoard = create_bingo_board()</b></code></p>"]
    InitializeBingoBoard --> InitializeCalledNumbers["<p align='left'>אתחול רשימת מספרים שנקראו
    <br><code><b>calledNumbers = []</b></code></p>"]
    InitializeCalledNumbers --> GameLoopStart{"תחילת לולאת המשחק: כל עוד אין ניצחון"}
    GameLoopStart -- כן --> GenerateNumber["<p align='left'>בחר מספר אקראי שטרם נקרא
    <br><code><b>randomNumber = get_random_number(calledNumbers)</b></code></p>"]
    GenerateNumber --> AddNumberToCalled["<p align='left'>הוסף מספר לרשימת המספרים שנקראו
    <br><code><b>calledNumbers.append(randomNumber)</b></code></p>"]
    AddNumberToCalled --> DisplayCalledNumber["<p align='left'>הצגת המספר שנקרא
    <br><code><b>print(randomNumber)</b></code></p>"]
    DisplayCalledNumber --> CheckWinCondition["<p align='left'>בדיקת תנאי ניצחון:
    <br><code><b>is_winner(bingoBoard, calledNumbers)</b></code></p>"]
    CheckWinCondition -- כן --> OutputWin["<p align='left'>הצגת הודעת ניצחון
    <br><code><b>print('BINGO!')</b></code></p>"]
    OutputWin --> End["סוף"]
    CheckWinCondition -- לא --> GameLoopStart
    GameLoopStart -- לא --> End
```
Legenda:
    Start - התחלת התוכנית.
    InitializeBingoBoard - יצירת לוח בינגו 5x5 עם מספרים אקראיים בין 1 ל-75 ללא חזרות.
    InitializeCalledNumbers - יצירת רשימה ריקה, calledNumbers, לשמירת המספרים שהוגרלו.
    GameLoopStart - תחילת לולאת המשחק, הפועלת עד שמוכרז ניצחון.
    GenerateNumber - יצירת מספר אקראי בין 1 ל-75 שלא הוגרל קודם.
    AddNumberToCalled - הוספת המספר שהוגרל לרשימת המספרים שהוגרלו.
    DisplayCalledNumber - הצגת המספר שהוגרל לשחקן.
    CheckWinCondition - בדיקה האם התקיימו תנאי הניצחון (שורה/עמודה/אלכסון מלאים).
    OutputWin - הצגת הודעת ניצחון "BINGO!".
    End - סיום המשחק.

"""
import random

def create_bingo_board():
    """
    יוצר לוח בינגו 5x5 עם מספרים אקראיים בין 1 ל-75 ללא חזרות.

    Returns:
        list: לוח הבינגו כרשימה דו-ממדית.
    """
    numbers = random.sample(range(1, 76), 25)
    board = [numbers[i:i+5] for i in range(0, 25, 5)]
    return board

def display_bingo_board(board):
     """
    מציג את לוח הבינגו בצורה ידידותית למשתמש.
    Args:
    board (list): לוח הבינגו כרשימה דו ממדית.
    """
     for row in board:
         print(' '.join(map(lambda x: f"{x:2}", row))) #הדפסת כל שורה עם רווחים בין מספרים
def get_random_number(called_numbers):
    """
    מגריל מספר אקראי בין 1 ל-75 שלא נקרא קודם.
    Args:
        called_numbers (list): רשימת המספרים שכבר נקראו.
    Returns:
        int: מספר אקראי חדש.
    """
    while True:
        number = random.randint(1, 75)
        if number not in called_numbers:
            return number

def mark_number_on_board(board, number, called_numbers):
    """
    מסמן את המספר בלוח הבינגו ע"י החלפתו ב-"X".

    Args:
        board (list): לוח הבינגו.
        number (int): המספר שנקרא.
    """
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == number:
                board[row][col] = 'X' # סימון המספר שנקרא ב-"X"
                return

def check_winner(board, called_numbers):
     """
    בודק אם יש שורות, עמודות או אלכסונים מלאים בלוח הבינגו.

    Args:
        board (list): לוח הבינגו.
        called_numbers (list): רשימת המספרים שנקראו.

    Returns:
        bool: True אם יש ניצחון, False אחרת.
    """
     # בדיקה של שורות
     for row in board:
         if all(cell == 'X' for cell in row):
             return True
     # בדיקה של עמודות
     for col in range(len(board[0])):
        if all(board[row][col] == 'X' for row in range(len(board))):
           return True
     #בדיקת אלכסונים
     if all(board[i][i] == 'X' for i in range(len(board))):
         return True
     if all(board[i][len(board)-1 - i] == 'X' for i in range(len(board))):
         return True

     return False #אם אף תנאי לא התקיים לא נמצא ניצחון

def play_bingo():
    """
    מנהל את משחק הבינגו.
    """
    bingo_board = create_bingo_board() #אתחול הלוח
    called_numbers = [] #אתחול רשימת המספרים שנקראו
    display_bingo_board(bingo_board) #הצגת הלוח למשתמש
    while True:
        number = get_random_number(called_numbers) #הגרלת מספר
        called_numbers.append(number)
        print(f"המספר שנקרא: {number}")
        mark_number_on_board(bingo_board,number, called_numbers)
        display_bingo_board(bingo_board) #הצגת הלוח לאחר סימון המספר
        if check_winner(bingo_board,called_numbers):#בדיקה אם יש ניצחון
            print("BINGO!")
            break


if __name__ == "__main__":
    play_bingo()


"""
הסבר מפורט לקוד:

1.  **ייבוא מודול `random`**:
    - `import random`: ייבוא המודול `random` לצורך יצירת מספרים אקראיים.

2.  **פונקציה `create_bingo_board()`**:
    - יוצרת לוח בינגו 5x5 עם מספרים אקראיים בין 1 ל-75 ללא חזרות.
    - `numbers = random.sample(range(1, 76), 25)`: יוצרת רשימה של 25 מספרים אקראיים ייחודיים בטווח 1-75.
    - `board = [numbers[i:i+5] for i in range(0, 25, 5)]`: יוצרת לוח בינגו 5x5 מרשימת המספרים.
    - מחזירה את לוח הבינגו כרשימה דו-ממדית.

3.  **פונקציה `display_bingo_board(board)`**:
    - מציגה את לוח הבינגו למשתמש.
    - עוברת על שורות הלוח ומדפיסה כל שורה עם רווחים בין המספרים.

4. **פונקציה `get_random_number(called_numbers)`**:
    - מקבלת את רשימת המספרים שכבר נקראו (`called_numbers`).
    - מגרילה מספר אקראי בין 1 ל-75.
    - אם המספר לא נקרא בעבר, הפונקציה תחזיר אותו.
    - אחרת, היא תגריל מספר חדש עד שיימצא מספר שטרם נקרא.

5.  **פונקציה `mark_number_on_board(board, number,called_numbers)`**:
    - מקבלת את לוח הבינגו, את המספר שנקרא ואת רשימת המספרים שנקראו.
    - עוברת על כל תא בלוח, ובמידה והמספר בתא תואם למספר שנקרא, היא מסמנת את התא ב-"X".

6.  **פונקציה `check_winner(board, called_numbers)`**:
    - מקבלת את לוח הבינגו ואת רשימת המספרים שנקראו.
    - בודקת האם יש שורה, עמודה או אלכסון מלאים בלוח הבינגו:
        - בדיקה של שורות: עוברת על כל השורות ובודקת האם כל התאים בשורה הם "X".
        - בדיקה של עמודות: עוברת על כל העמודות ובודקת האם כל התאים בעמודה הם "X".
        - בדיקה של אלכסונים: בודקת האם האלכסונים הראשיים מלאים ב-"X".
        - מחזירה `True` אם נמצא ניצחון, אחרת מחזירה `False`.

7.  **פונקציה `play_bingo()`**:
    - מנהלת את המשחק:
        - יוצרת לוח בינגו חדש על ידי קריאה לפונקציה `create_bingo_board()`.
        - מאתחלת רשימה ריקה `called_numbers` לשמירת מספרי הבינגו שכבר נקראו.
        - מציגה למשתמש את לוח הבינגו ההתחלתי.
        - נכנסת ללולאה אינסופית, המייצגת את מהלך המשחק.
        - בכל סיבוב:
            - מגרילה מספר אקראי ע"י קריאה לפונקציה `get_random_number()`.
            - מוסיפה את המספר לרשימה `called_numbers` ומציגה אותו למשתמש.
            - מסמנת את המספר בלוח הבינגו ע"י קריאה לפונקציה `mark_number_on_board()`.
            - מציגה למשתמש את לוח הבינגו לאחר סימון המספר.
            - בודקת האם יש ניצחון על ידי קריאה לפונקציה `check_winner()`.
            - אם יש ניצחון, מציגה את ההודעה "BINGO!" ויוצאת מהלולאה.

8.  **בלוק `if __name__ == "__main__":`**:
    - מבטיח שהפונקציה `play_bingo()` תופעל רק אם הקובץ מופעל ישירות, ולא אם הוא מיובא כמודול.
"""
