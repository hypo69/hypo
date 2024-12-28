# <23 MTH>
=================
קושי: 2
-----------------
המשחק "חשבון פשוט" הוא משחק בו המחשב מציג לשחקן תרגיל חיבור, חיסור או כפל, על השחקן להזין את התוצאה הנכונה.
המשחק נמשך עד שהשחקן מזין תשובה שגויה.

חוקי המשחק:
1. המחשב בוחר באופן אקראי פעולה חשבונית: חיבור, חיסור או כפל.
2. המחשב בוחר שני מספרים אקראיים מ-1 עד 10.
3. המחשב מציג לשחקן את התרגיל, על השחקן להזין את התשובה.
4. אם התשובה נכונה - ממשיכים לשאלה הבאה, אחרת - המשחק מסתיים.
-----------------
אלגוריתם:
1. אתחל את מונה התשובות הנכונות ל-0.
2. התחל לולאה "כל עוד התשובות נכונות":
    2.1 בחר מספר אופרנד 1 אקראי בין 1 ל-10.
    2.2 בחר מספר אופרנד 2 אקראי בין 1 ל-10.
    2.3 בחר פעולה אקראית (חיבור, חיסור או כפל).
    2.4 הצג את התרגיל (אופרנד 1, הפעולה, אופרנד 2).
    2.5 קלוט את התשובה מהשחקן.
    2.6 אם התשובה נכונה:
         2.6.1 הגדל את מונה התשובות הנכונות ב-1.
    2.7 אם התשובה שגויה:
        2.7.1 צא מהלולאה.
3. הצג הודעה "YOU GOT {מספר התשובות הנכונות} RIGHT".
4. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeCorrectAnswers["<p align='left'>אתחול משתנים:
    <code><b>
    correctAnswers = 0
    </b></code></p>"]
    InitializeCorrectAnswers --> LoopStart{"תחילת לולאה: כל עוד התשובות נכונות"}
    LoopStart -- כן --> GenerateOperandsAndOperator["<p align='left'>יצירת אופרנדים ואופרטור:
    <code><b>
    operand1 = random(1, 10)
    operand2 = random(1, 10)
    operator = random(+, -, *)
    </b></code></p>"]
    GenerateOperandsAndOperator --> DisplayQuestion["הצגת שאלה: <code><b>operand1 operator operand2 = ?</b></code>"]
    DisplayQuestion --> InputAnswer["קלט תשובה מהמשתמש: <code><b>userAnswer</b></code>"]
    InputAnswer --> CheckAnswer{"בדיקה: <code><b>userAnswer == result?</b></code>"}
    CheckAnswer -- כן --> IncreaseCorrectAnswers["<code><b>correctAnswers = correctAnswers + 1</b></code>"]
    IncreaseCorrectAnswers --> LoopStart
    CheckAnswer -- לא --> OutputResult["הצגת הודעה: <b>YOU GOT <code>{correctAnswers}</code> RIGHT</b>"]
    OutputResult --> End["סוף"]
    LoopStart -- לא --> OutputResult
```
Legenda:
    Start - התחלת התוכנית.
    InitializeCorrectAnswers - אתחול משתנה correctAnswers (מספר התשובות הנכונות) ל-0.
    LoopStart - תחילת הלולאה, הממשיכה כל עוד השחקן עונה נכון.
    GenerateOperandsAndOperator - יצירת שני מספרים אקראיים בין 1 ל-10 (operand1, operand2) ובחירת פעולה אקראית (+, -, *) ושמירתם במשתנה operator.
    DisplayQuestion - הצגת התרגיל למשתמש עם הערכים שיצרו בשלב הקודם.
    InputAnswer - קבלת תשובה מהמשתמש ושמירתה במשתנה userAnswer.
    CheckAnswer - בדיקה האם התשובה שהתקבלה מהמשתמש שווה לתוצאה הנכונה.
    IncreaseCorrectAnswers - אם התשובה נכונה, הגדלת המונה של מספר התשובות הנכונות ב-1.
    OutputResult - הצגת הודעה עם מספר התשובות הנכונות שהשחקן צבר.
    End - סוף התוכנית.
"""
import random

# אתחול מונה התשובות הנכונות
correctAnswers = 0

# לולאת המשחק
while True:
    # בחירת שני מספרים אקראיים בין 1 ל-10
    operand1 = random.randint(1, 10)
    operand2 = random.randint(1, 10)

    # בחירת פעולה אקראית
    operations = ['+', '-', '*']
    operator = random.choice(operations)

    # הצגת השאלה למשתמש
    question = f"{operand1} {operator} {operand2} = ?"
    print(question)

    # קבלת תשובה מהמשתמש
    try:
        userAnswer = int(input("הזן את התשובה: "))
    except ValueError:
        print("אנא הזן מספר שלם.")
        break

    # חישוב התשובה הנכונה
    if operator == '+':
        correctAnswer = operand1 + operand2
    elif operator == '-':
        correctAnswer = operand1 - operand2
    else: # operator == '*'
        correctAnswer = operand1 * operand2

    # בדיקה האם התשובה נכונה
    if userAnswer == correctAnswer:
        correctAnswers += 1
    else:
        break # יציאה מהלולאה אם התשובה שגויה

# הצגת מספר התשובות הנכונות שהמשתמש צבר
print(f"YOU GOT {correctAnswers} RIGHT")

"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    - `import random`: ייבוא המודול `random`, המשמש ליצירת ערכים אקראיים (מספרים ופעולות).
2.  **אתחול מונה התשובות הנכונות:**
    - `correctAnswers = 0`: אתחול משתנה לספירת מספר התשובות הנכונות, שמתחיל מ-0.
3. **לולאת המשחק `while True:`**:
    -   לולאה אינסופית, הממשיכה עד שהמשתמש טועה בתשובה (הפקודה `break` תסיים את הלולאה).
    -   **יצירת שאלה אקראית**:
        - `operand1 = random.randint(1, 10)`: יצירת מספר אקראי שלם בין 1 ל-10 ושמירתו במשתנה `operand1`.
        - `operand2 = random.randint(1, 10)`: יצירת מספר אקראי שלם נוסף בין 1 ל-10 ושמירתו במשתנה `operand2`.
        - `operations = ['+', '-', '*']`: יצירת רשימה של פעולות אפשריות.
        - `operator = random.choice(operations)`: בחירת פעולה אקראית מהרשימה ושמירתה במשתנה `operator`.
    -   **הצגת השאלה למשתמש**:
        - `question = f"{operand1} {operator} {operand2} = ?"`: יצירת מחרוזת שאלה המכילה את המספרים והפעולה.
        - `print(question)`: הצגת השאלה למשתמש.
    -   **קבלת תשובה מהמשתמש**:
        - `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין משהו שאינו מספר שלם, יוצג הודעת שגיאה.
        - `userAnswer = int(input("הזן את התשובה: "))`: בקשת מספר מהמשתמש והמרתו למספר שלם, ושמירתו במשתנה `userAnswer`.
    -   **חישוב התשובה הנכונה**:
        - `if operator == '+'`: בדיקה האם הפעולה היא חיבור.
            - `correctAnswer = operand1 + operand2`: חישוב התשובה הנכונה.
        - `elif operator == '-'`: בדיקה האם הפעולה היא חיסור.
            - `correctAnswer = operand1 - operand2`: חישוב התשובה הנכונה.
        - `else:`: אם הפעולה אינה חיבור או חיסור, היא כפל.
            - `correctAnswer = operand1 * operand2`: חישוב התשובה הנכונה.
    -   **בדיקת תשובת המשתמש**:
        - `if userAnswer == correctAnswer:`: בדיקה האם התשובה שהזין המשתמש נכונה.
            - `correctAnswers += 1`: אם התשובה נכונה, הגדלת מונה התשובות הנכונות ב-1.
        - `else:`: אם התשובה אינה נכונה.
            -`break`: סיום הלולאה (והמשחק) אם התשובה שגויה.
4.  **הצגת תוצאה**:
    - `print(f"YOU GOT {correctAnswers} RIGHT")`: הצגת הודעה עם מספר התשובות הנכונות שהמשתמש צבר.
"""
