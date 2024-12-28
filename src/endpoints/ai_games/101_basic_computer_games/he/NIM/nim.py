<NIM>:
=================
קושי: 4
-----------------
משחק NIM הוא משחק מתמטי בין שני שחקנים, שבו השחקנים לסירוגין מסירים חפצים מערימות שונות. המטרה היא להיות השחקן האחרון שמסיר חפצים. המשחק הזה מממש את הגרסה הפשוטה של NIM עם שלוש שורות/ערימות של חפצים. המחשב והשחקן מתחרים לסירוגין להסיר מספר חפצים משורה אחת בכל תור. השחקן שמסיר את החפץ האחרון מפסיד.
חוקי המשחק:
1. המשחק מתחיל עם 3 שורות של חפצים (אחת עם 3 חפצים, אחת עם 5, ואחת עם 7).
2. השחקנים (המחשב והאדם) מסירים חפצים בתורות מכל שורה.
3. בכל תור, השחקן בוחר שורה ומספר חפצים להסיר.
4. מספר החפצים שניתן להסיר בתור חייב להיות לפחות 1 ולא יותר ממספר החפצים שנותרו בשורה.
5. השחקן שמסיר את החפץ האחרון מפסיד.
-----------------
אלגוריתם:
1. אתחל את מספר החפצים בכל שורה (שורה 1: 3 חפצים, שורה 2: 5 חפצים, שורה 3: 7 חפצים).
2. הצג את מצב החפצים בשורות.
3. כל עוד נשארו חפצים:
   3.1. תור השחקן:
        3.1.1. בקש מהשחקן לבחור שורה ומספר חפצים להסיר.
        3.1.2. בדוק שהבחירה חוקית. אם לא, חזור על הבקשה.
        3.1.3. עדכן את מספר החפצים בשורה שנבחרה.
   3.2. אם נשארו חפצים, תור המחשב:
        3.2.1. המחשב בוחר שורה ומספר חפצים להסיר (באופן אקראי ובחוקיות).
        3.2.2. עדכן את מספר החפצים בשורה שנבחרה.
4. אם השחקן הוריד את החפץ האחרון, המחשב ניצח.
5. אם המחשב הוריד את החפץ האחרון, השחקן ניצח.
6. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> Initialize["אתחול שורות: <code><b>rows = [3, 5, 7]</b></code>"]
    Initialize --> DisplayRows["הצגת מצב השורות"]
    DisplayRows --> LoopStart{"תחילת לולאה: כל עוד נשארו חפצים"}
    LoopStart -- כן --> PlayerTurnStart["תור השחקן"]
    PlayerTurnStart --> PlayerInputRow["קלט: <code><b>row, amount</b></code>"]
    PlayerInputRow --> ValidatePlayerInput{"בדיקת קלט: חוקי?"}
    ValidatePlayerInput -- לא --> PlayerInputRow
    ValidatePlayerInput -- כן --> UpdateRowsPlayer["עדכון שורה: <code><b>rows[row] -= amount</b></code>"]
    UpdateRowsPlayer --> CheckRowsEmpty{"בדיקה: שורות ריקות?"}
    CheckRowsEmpty -- כן --> OutputPlayerLose["הודעה: הפסדת!"]
    CheckRowsEmpty -- לא --> ComputerTurnStart{"תור המחשב"}
    ComputerTurnStart --> ComputerChooseMove["בחירת שורה וכמות"]
    ComputerChooseMove --> UpdateRowsComputer["עדכון שורה: <code><b>rows[computerRow] -= computerAmount</b></code>"]
    UpdateRowsComputer --> CheckRowsEmptyComputer{"בדיקה: שורות ריקות?"}
    CheckRowsEmptyComputer -- כן --> OutputComputerLose["הודעה: ניצחת!"]
    CheckRowsEmptyComputer -- לא --> DisplayRows
    LoopStart -- לא --> End["סוף"]
    OutputPlayerLose --> End
    OutputComputerLose --> End

```
Legenda:
    Start - התחלת המשחק.
    Initialize - אתחול מספר החפצים בשלוש השורות (3, 5, 7).
    DisplayRows - הצגת מצב החפצים בשורות לשחקן.
    LoopStart - תחילת לולאה, שממשיכה כל עוד יש חפצים בשורות.
    PlayerTurnStart - תחילת תור השחקן.
    PlayerInputRow - קבלת קלט מהמשתמש - מספר שורה ומספר חפצים להסרה.
    ValidatePlayerInput - בדיקה אם הקלט מהשחקן חוקי (בטווח, חפצים קיימים בשורה).
    UpdateRowsPlayer - עדכון מספר החפצים בשורה הנבחרת על ידי השחקן.
    CheckRowsEmpty - בדיקה האם נשארו חפצים בשורות אחרי תור השחקן.
    OutputPlayerLose - הודעה על הפסד השחקן.
    ComputerTurnStart - תחילת תור המחשב.
    ComputerChooseMove - בחירת שורה ומספר חפצים להסרה על ידי המחשב.
    UpdateRowsComputer - עדכון מספר החפצים בשורה הנבחרת על ידי המחשב.
    CheckRowsEmptyComputer - בדיקה האם נשארו חפצים בשורות אחרי תור המחשב.
    OutputComputerLose - הודעה על הפסד המחשב (ניצחון השחקן).
    End - סוף המשחק.
"""
import random

# אתחול מספר החפצים בכל שורה
rows = [3, 5, 7]

# פונקציה להצגת מצב השורות
def display_rows():
    print("מצב השורות:")
    for i, row in enumerate(rows):
        print(f"שורה {i + 1}: {'*' * row} ({row} חפצים)")

# פונקציה לבחירת מהלך מחשב
def computer_move():
    # בחירת שורה אקראית שיש בה חפצים
    available_rows = [i for i, count in enumerate(rows) if count > 0]
    if not available_rows:
        return None, None

    computer_row = random.choice(available_rows)
    # בחירת כמות אקראית של חפצים להסרה, אך לא יותר ממספר החפצים בשורה
    computer_amount = random.randint(1, rows[computer_row])
    return computer_row, computer_amount

# לולאת המשחק הראשית
while True:
    display_rows()  # הצגת מצב השורות בכל תור

    # תור השחקן
    while True:
        try:
            row = int(input("בחר שורה (1, 2 או 3): ")) - 1 # קבלת שורה מהמשתמש והמרתה לאינדקס
            amount = int(input("בחר כמות להסרה: "))  # קבלת כמות מהמשתמש
            if 0 <= row < 3 and 1 <= amount <= rows[row]: #בדיקה אם הבחירה של השחקן חוקית
                rows[row] -= amount   # עדכון מספר החפצים בשורה
                break
            else:
                print("בחירה לא חוקית. נסה שוב.") # הודעה על בחירה לא חוקית
        except (ValueError, IndexError):
            print("קלט לא תקין. הזן מספרים בלבד.") # הודעה על קלט לא תקין
    
    # בדיקה האם השחקן הפסיד
    if all(count == 0 for count in rows):
        print("הפסדת! המחשב ניצח.")
        break

    # תור המחשב
    computer_row, computer_amount = computer_move()
    if computer_row is not None:
        rows[computer_row] -= computer_amount
        print(f"המחשב הסיר {computer_amount} חפצים משורה {computer_row + 1}.")

    # בדיקה האם המחשב הפסיד
    if all(count == 0 for count in rows):
         print("ניצחת! המחשב הפסיד.")
         break
"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    -   `import random`: ייבוא המודול `random` ליצירת מספרים אקראיים.
2.  **אתחול משתנה `rows`**:
    -   `rows = [3, 5, 7]`: רשימה המייצגת את מספר החפצים בכל שורה בהתחלה.
3.  **פונקציה `display_rows()`**:
    -   הדפסת מצב השורות למסך, כולל מספר החפצים בכל שורה.
4.  **פונקציה `computer_move()`**:
    -  בחירת מהלך אקראי עבור המחשב.
    -  `available_rows`: רשימה המכילה את מספרי השורות שאינן ריקות.
    -  בחירת שורה אקראית מתוך השורות הלא ריקות.
    -  בחירת כמות אקראית של חפצים להסרה, מ-1 ועד למספר החפצים בשורה.
    -   החזרת השורה שנבחרה והכמות שנבחרה.
5.  **לולאת המשחק הראשית `while True`**:
    -   לולאה אינסופית הממשיכה עד שאחד מהשחקנים מפסיד.
    -   `display_rows()`: הצגת מצב השורות בתחילת כל תור.
    -  **תור השחקן**:
        -   `while True`: לולאה פנימית שממשיכה עד שהשחקן מבצע מהלך תקין.
        -   `try...except`: בלוק טיפול בשגיאות קלט אפשריות.
        -   `row = int(input(...)) - 1`: קבלת בחירת השורה מהמשתמש, והמרתה לאינדקס (הפחתה ב-1).
        -   `amount = int(input(...))`: קבלת מספר החפצים להסרה מהמשתמש.
        -  בדיקה שהמהלך של השחקן חוקי: מספר השורה בטווח, וכמות החפצים קטנה או שווה למספר החפצים בשורה.
        -  `rows[row] -= amount`: עדכון מספר החפצים בשורה שנבחרה.
        -   `break`: יציאה מהלולאה הפנימית אחרי מהלך תקין.
        -   אם בחירת השחקן לא חוקית, מוצגת הודעה והלולאה ממשיכה.
    -  בדיקה אם כל השורות ריקות: אם כן השחקן הפסיד והמשחק מסתיים.
    -   **תור המחשב**:
        -   `computer_row, computer_amount = computer_move()`: קבלת מהלך המחשב.
        -   `if computer_row is not None`: בדיקה שהמחשב יכול לבחור מהלך.
        -   `rows[computer_row] -= computer_amount`: עדכון מצב החפצים בעקבות מהלך המחשב.
        -   הצגת מהלך המחשב למסך.
   - בדיקה אם כל השורות ריקות: אם כן המחשב הפסיד והמשחק מסתיים.
"""
