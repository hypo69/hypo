"""
QUBIK:
=================
קושי: 5
-----------------
המשחק "קוביק" הוא משחק לוח פשוט בו המשתמש צריך להזין 9 מספרים בטווח 1-9 לתוך ריבוע 3x3. לאחר מכן, המשחק בודק האם כל השורות, העמודות והאלכסונים בריבוע מסתכמים לאותו סכום. אם כן, המשתמש ניצח.

חוקי המשחק:
1. על השחקן להזין 9 מספרים שלמים, כל אחד בטווח מ-1 עד 9.
2. המספרים מוצבים בריבוע 3x3.
3. המשחק בודק האם סכום כל שורה, עמודה ואלכסון זהה.
4. אם הסכומים זהים, השחקן ניצח, אחרת המשחק מסתיים בהודעת הפסד.
-----------------
אלגוריתם:
1. הגדר ריבוע 3x3 ריק (רשימה דו-ממדית).
2. עבור על כל תא בריבוע (לולאה מקוננת):
    2.1 בקש מהמשתמש להזין מספר בין 1 ל-9.
    2.2 מקם את המספר שהוזן בתא המתאים בריבוע.
3. חשב את סכום השורה הראשונה בריבוע.
4. עבור על כל השורות, העמודות והאלכסונים:
    4.1 אם סכום השורה/העמודה/האלכסון לא שווה לסכום השורה הראשונה, עבור לשלב 5.
5. אם כל הסכומים זהים, הצג הודעה "מזל טוב! ניצחת!".
6. אחרת, הצג הודעה "הפסדת!".
7. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeBoard["<p align='left'>אתחול לוח ריק:
    <code><b>board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]</b></code></p>"]
    InitializeBoard --> InputNumbersLoopStart{"לולאה: עבור כל תא בלוח"}
    InputNumbersLoopStart --> InputNumber["קלט מספר בין 1 ל-9: <code><b>number</b></code>"]
    InputNumber --> PlaceNumber["הצבת מספר בלוח: <code><b>board[row][col] = number</b></code>"]
    PlaceNumber --> CheckLoopEnd{"בדיקה: האם כל התאים מלאים?"}
    CheckLoopEnd -- לא --> InputNumbersLoopStart
    CheckLoopEnd -- כן --> CalculateFirstRowSum["חישוב סכום השורה הראשונה: <code><b>firstRowSum</b></code>"]
    CalculateFirstRowSum --> CheckSumsLoopStart{"לולאה: עבור כל השורות, העמודות והאלכסונים"}
    CheckSumsLoopStart --> CalculateSum["חישוב סכום הנוכחי: <code><b>currentSum</b></code>"]
    CalculateSum --> CompareSums{"בדיקה: <code><b>currentSum == firstRowSum?</b></code>"}
    CompareSums -- לא --> OutputLose["הצגת הודעה: <b>הפסדת!</b>"]
    OutputLose --> End["סוף"]
    CompareSums -- כן --> CheckSumsLoopEnd{"בדיקה: האם כל הסכומים נבדקו?"}
    CheckSumsLoopEnd -- לא --> CheckSumsLoopStart
    CheckSumsLoopEnd -- כן --> OutputWin["הצגת הודעה: <b>מזל טוב! ניצחת!</b>"]
    OutputWin --> End
```

Legenda:
    Start - התחלת המשחק.
    InitializeBoard - אתחול לוח ריק, רשימה דו ממדית בגודל 3x3 עם ערכים מאופסים.
    InputNumbersLoopStart - תחילת לולאה מקוננת המאפשרת מעבר על כל התאים בלוח.
    InputNumber - קלט מספר מהמשתמש, כאשר כל מספר בין 1 ל-9.
    PlaceNumber - הצבת המספר שהתקבל מהמשתמש בתוך הלוח במיקום הנוכחי.
    CheckLoopEnd - בדיקה האם כל התאים בלוח מלאים.
    CalculateFirstRowSum - חישוב סכום השורה הראשונה בלוח.
    CheckSumsLoopStart - תחילת לולאה המאפשרת מעבר על כל השורות, העמודות והאלכסונים.
    CalculateSum - חישוב הסכום של השורה/העמודה/האלכסון הנוכחי.
    CompareSums - השוואה בין הסכום הנוכחי לסכום השורה הראשונה.
    OutputLose - הצגת הודעה שהמשתמש הפסיד.
    CheckSumsLoopEnd - בדיקה האם כל השורות, העמודות והאלכסונים נבדקו.
    OutputWin - הצגת הודעה שהמשתמש ניצח.
    End - סיום המשחק.
"""
import sys

# אתחול לוח ריק בגודל 3x3
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# פונקציה המקבלת קלט מהמשתמש ומוודאת שהוא תקין
def get_valid_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if 1 <= user_input <= 9:
                return user_input
            else:
                print("המספר חייב להיות בין 1 ל-9.")
        except ValueError:
            print("אנא הזן מספר שלם.")


# מילוי הלוח בקלט מהמשתמש
for row in range(3):
    for col in range(3):
        prompt = f"הזן מספר בין 1 ל-9 עבור שורה {row + 1}, עמודה {col + 1}: "
        board[row][col] = get_valid_input(prompt)

# חישוב סכום השורה הראשונה
first_row_sum = sum(board[0])

# בדיקת סכומים של שורות, עמודות ואלכסונים
for i in range(3):
    # בדיקת שורות
    if sum(board[i]) != first_row_sum:
        print("הפסדת!")
        sys.exit()

    # בדיקת עמודות
    column_sum = 0
    for row in range(3):
        column_sum += board[row][i]
    if column_sum != first_row_sum:
        print("הפסדת!")
        sys.exit()

# בדיקת אלכסונים
diagonal1_sum = board[0][0] + board[1][1] + board[2][2]
diagonal2_sum = board[0][2] + board[1][1] + board[2][0]

if diagonal1_sum != first_row_sum or diagonal2_sum != first_row_sum:
    print("הפסדת!")
else:
    print("מזל טוב! ניצחת!")


"""
הסבר הקוד:
1.  **ייבוא המודול `sys`**:
    - `import sys`: ייבוא המודול `sys`, המשמש ליציאה מהתוכנית במקרה של הפסד.

2.  **אתחול לוח ריק**:
    - `board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]`: יצירת רשימה דו-ממדית המייצגת את הלוח 3x3, ומילוי כל התאים באפסים.

3.  **הפונקציה `get_valid_input(prompt)`**:
    - פונקציה שמקבלת מחרוזת prompt כארגומנט.
    -  מבקשת קלט מהמשתמש ומבטיחה שהקלט יהיה מספר שלם בטווח בין 1 ל-9.
    -  אם הקלט אינו תקין, תוצג הודעת שגיאה, ותתבצע בקשה חוזרת לקלט.

4.  **מילוי הלוח**:
    -   לולאה כפולה שעוברת על כל שורה ועמודה בלוח.
    -   עבור כל תא בלוח, הפונקציה `get_valid_input` נקראת על מנת לקבל קלט תקין מהמשתמש, והוא מוצב בלוח.

5.  **חישוב סכום השורה הראשונה**:
    - `first_row_sum = sum(board[0])`:  חישוב סכום השורה הראשונה בלוח ושמירתו במשתנה `first_row_sum`. סכום זה ישמש להשוואה מול שאר הסכומים.

6.  **בדיקת סכומים**:
    -   לולאה שעוברת על כל השורות והעמודות בלוח.
    -   **בדיקת שורות**: סכום כל שורה מחושב ומושווה ל`first_row_sum`. אם הסכום אינו זהה, תוצג הודעה "הפסדת!", והתוכנית תסיים את פעולתה.
    -   **בדיקת עמודות**: סכום כל עמודה מחושב ומושווה ל`first_row_sum`. אם הסכום אינו זהה, תוצג הודעה "הפסדת!", והתוכנית תסיים את פעולתה.

7.  **בדיקת אלכסונים**:
    -   חישוב סכומי שני האלכסונים: `diagonal1_sum` ו-`diagonal2_sum`.
    -   אם אחד מסכומי האלכסונים אינו זהה ל`first_row_sum`, תוצג הודעה "הפסדת!".

8.  **הודעת ניצחון**:
    -  אם כל בדיקות הסכומים עברו בהצלחה, תוצג הודעה "מזל טוב! ניצחת!".
"""
