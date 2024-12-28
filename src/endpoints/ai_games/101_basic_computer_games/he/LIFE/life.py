"""
LIFE:
=================
קושי: 5
-----------------
המשחק "חיים" הוא סימולציה פשוטה של תאים המתקיימים על גבי לוח משחק. כל תא יכול להיות "חי" או "מת". במהלך כל "דור" או איטרציה, התאים משנים את מצבם בהתאם למספר השכנים החיים שלהם. המשחק מדגים דפוסים מורכבים הנוצרים מתוך חוקים פשוטים.

חוקי המשחק:
1. המשחק מתרחש על גבי לוח דו-מימדי של תאים.
2. כל תא יכול להיות במצב "חי" (מסומן כ-1) או "מת" (מסומן כ-0).
3. כל איטרציה או "דור" מחושבת על פי הכללים הבאים:
   - תא חי עם פחות משני שכנים חיים - מת.
   - תא חי עם 2 או 3 שכנים חיים - נשאר חי.
   - תא חי עם יותר מ-3 שכנים חיים - מת.
   - תא מת עם בדיוק 3 שכנים חיים - קם לתחייה.
4. השכנים של תא הם 8 התאים הסובבים אותו (כולל אלכסונים).
5. המשחק ממשיך ומתעדכן באיטרציות עד שמספר הדורות המבוקש מגיע לסופו, או שהמשתמש מחליט לעצור אותו.
-----------------
אלגוריתם:
1. אתחל את הלוח:
  1.1. קבל קלט מהמשתמש עבור גודל הלוח (מספר שורות ועמודות).
  1.2. אתחל את הלוח עם תאים אקראיים חיים או מתים.
2. עבור כל דור עד למספר הדורות שצוין או עד שהמשתמש יבחר לעצור:
    2.1. צור לוח חדש עבור הדור הבא.
    2.2. עבור כל תא בלוח:
        2.2.1. ספור את מספר השכנים החיים של התא.
        2.2.2. החל את כללי המשחק:
            - אם התא חי ויש לו פחות מ-2 שכנים חיים, התא מת בדור הבא.
            - אם התא חי ויש לו 2 או 3 שכנים חיים, התא נשאר חי בדור הבא.
            - אם התא חי ויש לו יותר מ-3 שכנים חיים, התא מת בדור הבא.
            - אם התא מת ויש לו בדיוק 3 שכנים חיים, התא חי בדור הבא.
        2.2.3. עדכן את הלוח החדש במצב התא המחושב.
    2.3. הדפס את הלוח החדש.
    2.4. העבר את הלוח החדש להיות הלוח הנוכחי.
3. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InputBoardSize["<p align='left'>קלט גודל הלוח:
    <code><b>rows, cols</b></code></p>"]
    InputBoardSize --> InitializeBoard["<p align='left'>אתחול הלוח:
    <code><b>board = random(rows, cols)</b></code></p>"]
    InitializeBoard --> InputGenerations["<p align='left'>קלט מספר דורות:
    <code><b>numberOfGenerations</b></code></p>"]
    InputGenerations --> LoopStart{"תחילת לולאה: עבור כל דור"}
    LoopStart -- כן --> CreateNewBoard["יצירת לוח חדש: <code><b>newBoard</b></code>"]
    CreateNewBoard --> LoopCellsStart{"תחילת לולאה: עבור כל תא בלוח"}
    LoopCellsStart -- כן --> CountLiveNeighbors["ספירת שכנים חיים: <code><b>liveNeighbors</b></code>"]
    CountLiveNeighbors --> ApplyRules{"החלת חוקי המשחק"}
    ApplyRules --> UpdateNewBoard["עדכון הלוח החדש: <code><b>newBoard[row][col]</b></code>"]
    UpdateNewBoard --> LoopCellsEnd{"סוף לולאה: עבור כל תא בלוח"}
    LoopCellsEnd -- כן --> LoopCellsStart
    LoopCellsEnd -- לא --> PrintBoard["הדפסת הלוח: <code><b>newBoard</b></code>"]
    PrintBoard --> UpdateBoard["עדכון הלוח: <code><b>board = newBoard</b></code>"]
     UpdateBoard --> LoopEnd{"סוף לולאה: עבור כל דור"}
    LoopEnd -- כן --> LoopStart
    LoopEnd -- לא --> End["סוף"]
```

Legenda:
    Start - התחלת התוכנית.
    InputBoardSize - קבלת גודל הלוח מהמשתמש (מספר שורות ועמודות).
    InitializeBoard - אתחול הלוח עם ערכים אקראיים (חי או מת).
    InputGenerations - קבלת מספר הדורות שיוצגו.
    LoopStart - תחילת לולאה לביצוע מספר הדורות שנקלטו.
    CreateNewBoard - יצירת לוח חדש לדור הבא.
    LoopCellsStart - תחילת לולאה לכל תא בלוח.
    CountLiveNeighbors - ספירת השכנים החיים של תא מסוים.
    ApplyRules - החלת חוקי המשחק של "החיים" על התא, בהתאם למספר שכניו.
    UpdateNewBoard - עדכון מצב התא בלוח החדש.
    LoopCellsEnd - סיום הלולאה עבור כל תא בלוח.
     PrintBoard - הדפסת הלוח החדש למסך.
     UpdateBoard - עדכון הלוח הנוכחי ללוח החדש.
    LoopEnd - סיום הלולאה עבור כל הדורות.
    End - סיום התוכנית.
"""
import random
import time

def create_board(rows, cols):
    """
    יוצר לוח משחק ריק בגודל שורות X עמודות,
    ומאתחל אותו עם ערכים אקראיים של 0 או 1 (מת או חי).

    Args:
        rows: מספר השורות בלוח.
        cols: מספר העמודות בלוח.

    Returns:
        רשימה דו-ממדית (לוח) המכילה 0 או 1 באופן אקראי.
    """
    board = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]
    return board

def count_live_neighbors(board, row, col):
    """
    סופר את מספר השכנים החיים של תא מסוים בלוח.
    תא נחשב שכן אם הוא סמוך (אופקי, אנכי או אלכסוני).

    Args:
        board: לוח המשחק.
        row: שורת התא.
        col: עמודת התא.

    Returns:
        מספר השכנים החיים של התא.
    """
    rows = len(board)
    cols = len(board[0])
    live_neighbors = 0

    # סריקה של 8 השכנים
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i, j) != (row, col):  # לא לספור את התא עצמו כשכן
                live_neighbors += board[i][j]
    return live_neighbors

def next_generation(board):
    """
    יוצר לוח חדש שמייצג את הדור הבא של המשחק,
    על ידי החלת חוקי המשחק על כל תא.

    Args:
        board: לוח המשחק הנוכחי.

    Returns:
        לוח המשחק המעודכן (הדור הבא).
    """
    rows = len(board)
    cols = len(board[0])
    new_board = [[0 for _ in range(cols)] for _ in range(rows)]

    # מעבר על כל תא בלוח
    for row in range(rows):
        for col in range(cols):
            live_neighbors = count_live_neighbors(board, row, col)
            # החלת חוקי המשחק
            if board[row][col] == 1:  # תא חי
                if live_neighbors < 2 or live_neighbors > 3:
                    new_board[row][col] = 0  # מת
                else:
                    new_board[row][col] = 1  # נשאר חי
            else:  # תא מת
                if live_neighbors == 3:
                    new_board[row][col] = 1  # קם לתחייה

    return new_board

def print_board(board):
    """
     מדפיס את הלוח למסך, כאשר כל תא מודפס כ-0 או 1.

    Args:
         board: הלוח להדפסה.
    """
    for row in board:
        print(' '.join(str(cell) for cell in row))
    print()  # שורה ריקה בין דור לדור

def play_life(rows, cols, generations):
    """
    מפעיל את משחק החיים.

    Args:
        rows: מספר השורות בלוח.
        cols: מספר העמודות בלוח.
         generations: מספר הדורות להרצה.
    """
    board = create_board(rows, cols)
    for generation in range(generations):
        print(f"דור {generation + 1}:")
        print_board(board)
        board = next_generation(board)
        time.sleep(0.5)

if __name__ == "__main__":
    try:
        rows = int(input("הזן את מספר השורות בלוח: "))
        cols = int(input("הזן את מספר העמודות בלוח: "))
        generations = int(input("הזן את מספר הדורות להרצה: "))

        if rows <= 0 or cols <=0 or generations <= 0:
           print("המספר חייב להיות גדול מ-0")
        else:
           play_life(rows, cols, generations)

    except ValueError:
        print("קלט לא תקין. אנא הזן מספרים שלמים.")

"""
הסבר הקוד:
1.  **ייבוא מודולים**:
    -  `import random`: ייבוא המודול `random` לייצור מספרים אקראיים.
    -  `import time`: ייבוא המודול `time` לשליטה על מהירות ההצגה.

2. **פונקציה `create_board(rows, cols)`**:
    - יוצרת לוח דו-מימדי (רשימה של רשימות) בגודל `rows` על `cols`.
    - מאתחלת את הלוח באקראי עם תאים "חיים" (1) או "מתים" (0).
    - משתמשת ב-`random.choice([0, 1])` כדי לבחור באופן אקראי 0 או 1 עבור כל תא.
    - מחזירה את הלוח המאותחל.

3. **פונקציה `count_live_neighbors(board, row, col)`**:
    - מקבלת את הלוח, השורה והעמודה של תא.
    - סופרת את מספר השכנים החיים של התא, על ידי סקירת שמונה השכנים שלו (כולל אלכסונים).
    - בודקת האם השכן הוא בתוך גבולות הלוח ואינו התא עצמו.
    - מחזירה את מספר השכנים החיים.

4. **פונקציה `next_generation(board)`**:
    - יוצרת לוח חדש שמייצג את הדור הבא של המשחק.
    - עוברת על כל תא בלוח הנוכחי.
    - מחשבת את מספר השכנים החיים של התא על ידי קריאה לפונקציה `count_live_neighbors`.
    - מיישמת את חוקי המשחק כדי לקבוע את מצבו של התא בדור הבא.
    - אם התא חי:
        - אם יש לו פחות מ-2 או יותר מ-3 שכנים חיים, הוא מת.
        - אחרת, הוא נשאר חי.
    - אם התא מת:
        - אם יש לו בדיוק 3 שכנים חיים, הוא קם לתחייה.
    - מחזירה את הלוח החדש, שמייצג את הדור הבא.

5. **פונקציה `print_board(board)`**:
   - מקבלת את הלוח ומדפיסה אותו לקונסולה.
   - כל שורה מודפסת בשורה נפרדת, כאשר כל תא מופרד ברווח.
   - מודפסת שורה ריקה בסוף, להפרדה בין דורות.

6. **פונקציה `play_life(rows, cols, generations)`**:
   - מאתחלת את המשחק על ידי יצירת לוח באמצעות הפונקציה `create_board`.
   - עוברת בלולאה על מספר הדורות שצוין.
   - מדפיסה את הלוח הנוכחי באמצעות הפונקציה `print_board`.
   - יוצרת את הדור הבא באמצעות הפונקציה `next_generation`.
   - עוצרת את התוכנית למשך חצי שניה בעזרת הפונקציה `time.sleep(0.5)`
   - חוזרת על הפעולות עבור הדור הבא.

7.  **התחלת התוכנית**:
    - `if __name__ == "__main__":` - מבטיח שהקוד יורץ רק כאשר הקובץ מופעל ישירות ולא כמודול.
    - **קבלת קלט מהמשתמש**:
      - מבקש מהמשתמש להזין את מספר השורות, העמודות ומספר הדורות.
      - המרת הקלט למספר שלם באמצעות `int()`.
      - טיפול בשגיאת `ValueError` - אם הקלט אינו מספר שלם, מודפסת הודעת שגיאה.
      - בדיקה האם הקלט חוקי, כלומר גדול מ-0.
    - **הפעלת המשחק**:
      - אם הקלט תקין, קורא לפונקציה `play_life` להפעלת המשחק.
"""
