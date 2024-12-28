"""
<RUSROU>:
=================
קושי: 3
-----------------
המשחק "רולטה רוסית" הוא משחק מזל בו השחקן בוחר מספר מ-1 עד 6, ומספר אקראי נבחר על ידי המחשב באותו טווח. אם שני המספרים זהים, השחקן "מת". המשחק מציג מספר ניסיונות, ומסתיים כאשר השחקן "מת".

חוקי המשחק:
1. השחקן בוחר מספר מ-1 עד 6.
2. המחשב בוחר מספר אקראי מ-1 עד 6.
3. אם המספרים זהים, השחקן "מת".
4. המשחק נמשך עד שהשחקן "מת", תוך כדי הצגת מספר הניסיונות.
-----------------
אלגוריתם:
1. אתחל את מספר הניסיונות ל-0.
2. התחל לולאה "כל עוד השחקן לא מת":
    2.1. הגדל את מספר הניסיונות ב-1.
    2.2. בקש מהשחקן להזין מספר בין 1 ל-6.
    2.3. צור מספר אקראי בין 1 ל-6.
    2.4. אם המספר שהוזן שווה למספר האקראי, הצג הודעה "אתה מת!" והצג את מספר הניסיונות, צא מהלולאה.
3. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:<br><code><b>numberOfTries = 0</b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: כל עוד השחקן לא 'מת'"}
    LoopStart -- כן --> IncreaseTries["<code><b>numberOfTries = numberOfTries + 1</b></code>"]
    IncreaseTries --> InputNumber["קלט מספר מהמשתמש:<br><code><b>userNumber</b></code>"]
    InputNumber --> GenerateRandomNumber["יצירת מספר אקראי:<br><code><b>randomNumber = random(1, 6)</b></code>"]
    GenerateRandomNumber --> CheckNumbers{"בדיקה: <code><b>userNumber == randomNumber?</b></code>"}
    CheckNumbers -- כן --> OutputGameOver["הצגת הודעה: <b>אתה מת! ב{numberOfTries} נסיונות</b>"]
    OutputGameOver --> End["סוף"]
    CheckNumbers -- לא --> LoopStart
    LoopStart -- לא --> End

```
Legenda:
    Start - תחילת התוכנית.
    InitializeVariables - אתחול משתנה `numberOfTries` (מספר הניסיונות) ל-0.
    LoopStart - תחילת הלולאה, הממשיכה כל עוד השחקן לא "מת".
    IncreaseTries - הגדלת מונה הניסיונות ב-1.
    InputNumber - קבלת מספר מהמשתמש ושמירתו במשתנה `userNumber`.
    GenerateRandomNumber - יצירת מספר אקראי בין 1 ל-6 ושמירתו במשתנה `randomNumber`.
    CheckNumbers - בדיקה האם המספר שהוזן שווה למספר האקראי.
    OutputGameOver - הצגת הודעת סיום ("אתה מת!") עם מספר הניסיונות.
    End - סוף התוכנית.
"""
```python
import random

# אתחול מספר הניסיונות
numberOfTries = 0

# לולאת המשחק
while True:
    # הגדלת מונה הניסיונות
    numberOfTries += 1
    
    # קלט מהמשתמש
    try:
        userNumber = int(input("בחר מספר בין 1 ל-6: "))
        # בדיקה שהקלט תקין
        if userNumber < 1 or userNumber > 6:
             print("מספר לא תקין. אנא בחר מספר בין 1 ל-6.")
             continue
    except ValueError:
        print("קלט לא תקין. אנא הזן מספר שלם.")
        continue


    # יצירת מספר אקראי
    randomNumber = random.randint(1, 6)

    # בדיקה אם המספרים זהים
    if userNumber == randomNumber:
        print(f"אתה מת! ב-{numberOfTries} נסיונות.")
        break  # יציאה מהלולאה
```
"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    - `import random`: ייבוא המודול `random` לצורך יצירת מספר אקראי.
2.  **אתחול מספר הניסיונות**:
    - `numberOfTries = 0`: אתחול משתנה `numberOfTries`, המייצג את מספר הניסיונות, ל-0.
3.  **לולאת המשחק `while True`**:
    - לולאה אינסופית שרצה עד שהשחקן "מת".
    - `numberOfTries += 1`: הגדלת מונה הניסיונות בכל סיבוב של הלולאה.
    - **קבלת קלט מהמשתמש**:
        - `try...except ValueError`: טיפול בשגיאות קלט אפשריות.
        - `userNumber = int(input("בחר מספר בין 1 ל-6: "))`: בקשת קלט מהמשתמש (מספר בין 1 ל-6).
    - **בדיקת קלט תקין**:
        - `if userNumber < 1 or userNumber > 6`: בדיקה שהקלט מהמשתמש תקין (בין 1 ל-6). אם הקלט לא תקין, מוצגת הודעה והלולאה ממשיכה לסיבוב הבא.
    - **יצירת מספר אקראי**:
        - `randomNumber = random.randint(1, 6)`: יצירת מספר אקראי בין 1 ל-6 ושמירתו במשתנה `randomNumber`.
    - **בדיקה האם המספרים זהים**:
        - `if userNumber == randomNumber`: בדיקה האם המספר שהזין המשתמש שווה למספר האקראי.
        - `print(f"אתה מת! ב-{numberOfTries} נסיונות.")`: אם המספרים זהים, מוצגת הודעה שהמשתמש "מת" ומספר הניסיונות.
        - `break`: יציאה מהלולאה.
"""
