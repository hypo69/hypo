"""
QUEEN:
=================
קושי: 6
-----------------
המשחק "מלכה" הוא משחק לוח בו המחשב מנסה להציב מלכות על לוח שחמט בגודל 8x8, כך שאף מלכה לא מאיימת על מלכה אחרת. המטרה היא לפתור את בעיית שמונה המלכות, כלומר להציב 8 מלכות על הלוח כך שאף אחת מהן לא מאיימת על האחרות.

חוקי המשחק:
1. הלוח הוא בגודל 8x8.
2. מטרת המשחק היא למצוא פתרון לבעיית 8 המלכות, כלומר למקם 8 מלכות על הלוח כך שאף מלכה לא מאיימת על מלכה אחרת (באותה שורה, טור או אלכסון).
3. המשחק מציג את הפתרון הראשון שהוא מוצא, ללא אינטראקציה עם השחקן.
-----------------
אלגוריתם:
1. אתחל לוח בגודל 8x8, שמיוצג על ידי מערך דו-ממדי.
2. אתחל את המשתנה `row` ל-0.
3. אתחל לולאה: כל עוד `row` קטן מ-8, בצע את השלבים הבאים:
   3.1 אתחל את המשתנה `column` ל-0.
   3.2 אתחל לולאה פנימית: כל עוד `column` קטן מ-8, בצע את השלבים הבאים:
        3.2.1 בדוק האם ניתן להציב מלכה בעמדה (row, column), על ידי בדיקה שאין מלכות אחרות מאיימות עליה.
        3.2.2 אם המיקום בטוח, הצב מלכה במיקום זה.
        3.2.3 אם הגענו לשורה האחרונה (row=7) והצלחת להציב 8 מלכות, סיים והצג את הפתרון.
        3.2.4 אם הצבת מלכה, הגדל את `row` ב-1 וצא מהלולאה הפנימית.
        3.2.5 אם לא הצבת מלכה (במיקום הנוכחי), עבור לעמודה הבאה (הגדל את `column` ב-1).
4. אם לא נמצא פתרון, צא מהתוכנית.
5. הצג את הלוח עם הפתרון.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeBoard["אתחול הלוח: <code><b>board = [[0]*8 for _ in range(8)]</b></code>"]
    InitializeBoard --> InitializeRow["אתחול: <code><b>row = 0</b></code>"]
    InitializeRow --> RowLoopStart{"תחילת לולאה חיצונית: <code><b>row < 8</b></code>"}
    RowLoopStart -- כן --> InitializeColumn["אתחול: <code><b>column = 0</b></code>"]
    InitializeColumn --> ColumnLoopStart{"תחילת לולאה פנימית: <code><b>column < 8</b></code>"}
    ColumnLoopStart -- כן --> IsPositionSafe{"בדיקה: <code><b>isPositionSafe(row, column)?</b></code>"}
    IsPositionSafe -- כן --> PlaceQueen["הצבת מלכה: <code><b>board[row][column] = 1</b></code>"]
    PlaceQueen --> CheckLastRow{"בדיקה: <code><b>row == 7 and all queens placed?</b></code>"}
    CheckLastRow -- כן --> OutputSolution["הצגת פתרון: <code><b>print(board)</b></code>"]
    OutputSolution --> End["סוף"]
    CheckLastRow -- לא --> IncreaseRow["<code><b>row = row + 1</b></code>"]
    IncreaseRow --> ColumnLoopEnd["סוף לולאה פנימית"]
    ColumnLoopEnd --> RowLoopStart
    IsPositionSafe -- לא --> IncreaseColumn["<code><b>column = column + 1</b></code>"]
    IncreaseColumn --> ColumnLoopStart
    ColumnLoopStart -- לא --> RowLoopStart
    RowLoopStart -- לא --> NoSolution["הודעה: אין פתרון"]
    NoSolution --> End
```
Legenda:
    Start - תחילת התוכנית.
    InitializeBoard - אתחול לוח המשחק כמערך דו מימדי בגודל 8x8, המייצג לוח שחמט ריק.
    InitializeRow - אתחול משתנה השורה row ל-0.
    RowLoopStart - תחילת לולאה חיצונית, הממשיכה כל עוד row קטן מ-8.
    InitializeColumn - אתחול משתנה העמודה column ל-0.
    ColumnLoopStart - תחילת לולאה פנימית, הממשיכה כל עוד column קטן מ-8.
    IsPositionSafe - בדיקה האם מיקום המלכה (row, column) בטוח, כלומר לא מאוים על ידי מלכה אחרת.
    PlaceQueen - הצבת מלכה במיקום (row, column) בלוח.
    CheckLastRow - בדיקה האם הגענו לשורה האחרונה (row = 7) וכל 8 המלכות הוצבו בהצלחה.
    OutputSolution - הצגת פתרון הלוח.
    End - סוף התוכנית.
    IncreaseRow - הגדלת מונה השורה row ב-1.
    ColumnLoopEnd - סוף לולאה פנימית, שחוזרת ללולאה החיצונית.
    IncreaseColumn - הגדלת מונה העמודה column ב-1.
    NoSolution - הודעה שאין פתרון, אם כל האפשרויות נבדקו ולא נמצא פתרון.
"""
```python
def is_position_safe(board, row, col):
    """
    פונקציה שבודקת אם ניתן להציב מלכה במיקום (row, col) בלוח,
    בלי שהיא תהיה מאויימת ע"י מלכה אחרת.

    Args:
        board: לוח המשחק כמערך דו-ממדי.
        row: מספר השורה.
        col: מספר העמודה.

    Returns:
        True אם המיקום בטוח, False אחרת.
    """
    # בדיקה לאורך השורה הנוכחית
    for i in range(col):
        if board[row][i] == 1:
            return False

    # בדיקה לאורך האלכסון העולה
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # בדיקה לאורך האלכסון היורד
    for i, j in zip(range(row, 8, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_queens():
    """
    פונקציה שמנסה לפתור את בעיית שמונה המלכות, על ידי הצבת מלכות על לוח שחמט
    בצורה כזו שאף מלכה לא תאיים על מלכה אחרת.
    """
    # יצירת לוח שחמט 8x8 ריק
    board = [[0] * 8 for _ in range(8)]
    row = 0

    while row < 8:
        column = 0
        while column < 8:
            if is_position_safe(board, row, column):
                board[row][column] = 1

                if row == 7:
                    print("פתרון:")
                    for row_board in board:
                        print(row_board)
                    return  # נמצא פתרון
                row += 1
                break # מעבר לשורה הבאה
            column += 1
        else:
             # אם לא הצלחנו למצוא מיקום בטוח בשורה הנוכחית,
            # סימן שהגענו למבוי סתום ויש לצאת
            print("לא נמצא פתרון")
            return

    print("לא נמצא פתרון")



if __name__ == "__main__":
    solve_queens()
```
"""
הסבר הקוד:
1. **הפונקציה `is_position_safe(board, row, col)`**:
    - מקבלת את לוח המשחק (`board`), שורה (`row`), ועמודה (`col`) כקלט.
    - בודקת האם ניתן להציב מלכה במיקום (`row`, `col`) מבלי להיות מאוימת על ידי מלכה אחרת.
    - עוברת על השורה הנוכחית, האלכסון העולה והאלכסון היורד, וחוזרת `False` אם נמצאה מלכה מאיימת.
    - אם לא נמצאה מלכה מאיימת, הפונקציה מחזירה `True`.

2. **הפונקציה `solve_queens()`**:
    - אתחול לוח המשחק:
        - `board = [[0] * 8 for _ in range(8)]`: יוצרת לוח משחק 8x8 ריק (מיוצג על ידי רשימה של רשימות).
        - row = 0 - משתנה שמציין את השורה הנוכחית
        - column = 0 - משתנה שמציין את העמודה הנוכחית
    - לולאה חיצונית `while row < 8`:
        -  עוברת על כל שורה ושורה בלוח.
        - לולאה פנימית `while column < 8`:
            -  עוברת על כל עמודה ועמודה בשורה הנוכחית.
            - `if is_position_safe(board, row, column)`: בודקת אם המיקום הנוכחי (`row`, `column`) בטוח להצבת מלכה.
                - אם בטוח, היא מציבה מלכה: `board[row][column] = 1`.
                - בודקת האם הגענו לשורה האחרונה `row == 7`. אם כן, הפונקציה מדפיסה את לוח המשחק עם הפתרון ויוצאת מהפונקציה.
                - אם לא הגענו לשורה האחרונה, מגדילה את `row` ב-1 ועוברת לשורה הבאה.
            - אחרת (לא בטוח), עוברת לעמודה הבאה על ידי הגדלת `column` ב-1.
        - אם לא נמצא מיקום בטוח בשורה הנוכחית:
             -  הפונקציה מדפיסה הודעה "לא נמצא פתרון" ויוצאת מהפונקציה.

3.  **הפעלת המשחק**:
   - `if __name__ == "__main__":`: בלוק זה מבטיח שהקוד יופעל רק כאשר הסקריפט מורץ ישירות ולא כאשר הוא מיובא כמודול.
   -  `solve_queens()`: קריאה לפונקציה שפותרת את בעיית שמונה המלכות.
"""
