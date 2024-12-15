<UGLY>:
=================
קושי: 2
-----------------
המשחק "UGLY" הוא משחק ניחושים פשוט שבו המחשב בוחר מספר אקראי בטווח מ-1 עד 10, והשחקן מנסה לנחש את המספר הזה. המשחק נמשך עד שהשחקן מצליח לנחש את המספר הנכון. אין רמזים ניתנים לשחקן, המשחק מסתיים בניחוש נכון בלבד.
חוקי המשחק:
1. המחשב בוחר מספר אקראי בין 1 ל-10.
2. השחקן מזין ניחוש אחד בלבד.
3. אם הניחוש נכון, המשחק מסתיים והודעת ניצחון מוצגת.
4. אם הניחוש לא נכון, המשחק מסתיים בהודעת הפסד.
-----------------
אלגוריתם:
1. בחר מספר אקראי בין 1 ל-10.
2. בקש מהמשתמש להזין ניחוש.
3. אם הניחוש שווה למספר האקראי, הצג הודעת ניצחון וסיים.
4. אחרת, הצג הודעת הפסד וסיים.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    targetNumber = random(1, 10)
    </b></code></p>"]
    InitializeVariables --> InputGuess["קלט מספר מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> CheckGuess{"בדיקה: <code><b>userGuess == targetNumber?</b></code>"}
    CheckGuess -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT!</b>"]
    OutputWin --> End["סוף"]
    CheckGuess -- לא --> OutputLose["הצגת הודעה: <b>YOU UGLY LOSER!</b>"]
    OutputLose --> End
```
Legenda:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנה: targetNumber (המספר המוגלה) נוצר באקראי בין 1 ל-10.
    InputGuess - קלט מספר מהמשתמש ושמירתו במשתנה userGuess.
    CheckGuess - בדיקה האם המספר שהוזן שווה למספר המוגלה.
    OutputWin - הצגת הודעת ניצחון, אם המספר נוחש.
    OutputLose - הצגת הודעת הפסד, אם המספר לא נוחש.
    End - סוף התוכנית.
"""
```python
import random

# אתחול המספר המוגרל באופן אקראי בין 1 ל-10
targetNumber = random.randint(1, 10)

# קבלת ניחוש מהמשתמש
try:
    userGuess = int(input("נחש מספר בין 1 ל-10: "))
except ValueError:
    print("אנא הזן מספר שלם.")
    exit() # סיום התוכנית במקרה של קלט שגוי.

# בדיקה האם הניחוש נכון
if userGuess == targetNumber:
    print("YOU GOT IT!") # הודעה על ניצחון
else:
    print("YOU UGLY LOSER!") # הודעה על הפסד
    
"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    - `import random`: ייבוא המודול `random`, המשמש ליצירת מספר אקראי.
2.  **אתחול המשתנה `targetNumber`**:
    - `targetNumber = random.randint(1, 10)`: יצירת מספר שלם אקראי בין 1 ל-10 ושמירתו במשתנה `targetNumber`.
3. **קבלת קלט מהמשתמש**:
    -  `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין משהו שאינו מספר שלם, תוצג הודעת שגיאה והתוכנית תסתיים.
    - `userGuess = int(input("נחש מספר בין 1 ל-10: "))`: בקשת מספר מהמשתמש והמרתו למספר שלם, ושמירתו במשתנה `userGuess`.
4. **בדיקה והודעה**:
    - `if userGuess == targetNumber:`: בדיקה האם המספר שהוזן שווה למספר המוגלה.
    - `print("YOU GOT IT!")`: אם המספר נוחש, מוצגת הודעת ניצחון.
    - `else:`: אם המספר לא נוחש, הקוד עובר לחלק ה-else.
    - `print("YOU UGLY LOSER!")`: הצגת הודעת הפסד אם הניחוש שגוי.
"""
```
