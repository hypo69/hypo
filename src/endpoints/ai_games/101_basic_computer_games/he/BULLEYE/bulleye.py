<BULLEYE>:
=================
קושי: 2
-----------------
המשחק "בול פגיעה" הוא משחק ניחושים פשוט בו המחשב בוחר מספר אקראי מ-1 עד 10, והשחקן צריך לנחש את המספר הזה. לאחר כל ניסיון ניחוש, המחשב מציין האם השחקן צדק או טעה, ומספר הניסיונות של השחקן גדל. המשחק נגמר לאחר ניחוש מוצלח.

חוקי המשחק:
1. המחשב בוחר מספר שלם אקראי מ-1 עד 10.
2. השחקן מזין את הניחוש שלו לגבי המספר שנבחר.
3. לאחר כל ניסיון, המחשב מודיע האם הניחוש היה נכון או לא.
4. המשחק נמשך עד שהשחקן מנחש את המספר שנבחר.
-----------------
אלגוריתם:
1. אתחל את מספר הניסיונות ל-0.
2. צור מספר אקראי בין 1 ל-10.
3. התחל לולאה "כל עוד המספר לא נוחש":
    3.1 הגדל את מספר הניסיונות ב-1.
    3.2 בקש מהשחקן להזין מספר.
    3.3 אם המספר שהוזן שווה למספר שנבחר, עבור לשלב 4.
    3.4 אם המספר שהוזן שונה מהמספר שנבחר, הצג הודעה "WRONG NUMBER".
4. הצג הודעה "YOU GOT IT IN {מספר ניסיונות} GUESSES!".
5. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:<br><code><b>numberOfGuesses = 0<br>targetNumber = random(1, 10)</b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: כל עוד לא נוחש"}
    LoopStart -- כן --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputGuess["קלט מספר מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> CheckGuess{"בדיקה: <code><b>userGuess == targetNumber?</b></code>"}
    CheckGuess -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES!</b>"]
    OutputWin --> End["סוף"]
    CheckGuess -- לא --> OutputWrong["הצגת הודעה: <b>WRONG NUMBER</b>"]
    OutputWrong --> LoopStart
	LoopStart -- לא --> End
```
Legenda:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: numberOfGuesses (מספר הניסיונות) מאותחל ל-0, ו-targetNumber (המספר המוגלה) נוצר באקראי בין 1 ל-10.
    LoopStart - תחילת הלולאה, הממשיכה כל עוד המספר לא נוחש.
    IncreaseGuesses - הגדלת מונה הניסיונות ב-1.
    InputGuess - קלט מספר מהמשתמש ושמירתו במשתנה userGuess.
    CheckGuess - בדיקה האם המספר שהוזן שווה למספר המוגלה.
    OutputWin - הצגת הודעת ניצחון, אם המספר נוחש, עם מספר הניסיונות.
    End - סוף התוכנית.
    OutputWrong - הצגת הודעה "WRONG NUMBER", אם המספר שהוזן לא שווה למספר המוגלה.

```python
import random

# אתחול מונה הניסיונות
numberOfGuesses = 0
# יצירת מספר אקראי בין 1 ל-10
targetNumber = random.randint(1, 10)

# לולאת המשחק הראשית
while True:
    # הגדלת מונה הניסיונות
    numberOfGuesses += 1
    # בקשת קלט מספר מהמשתמש
    try:
        userGuess = int(input("נחש מספר בין 1 ל-10: "))
    except ValueError:
        print("אנא הזן מספר שלם.")
        continue

    # בדיקה האם המספר נוחש
    if userGuess == targetNumber:
        print(f"מזל טוב! ניחשת את המספר ב-{numberOfGuesses} ניסיונות!")
        break  # סיום הלולאה אם המספר נוחש
    else:
        print("WRONG NUMBER")  # הודעה שהמספר לא נכון

"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    -  `import random`: ייבוא המודול `random`, המשמש ליצירת מספר אקראי.
2.  **אתחול משתנים**:
    - `numberOfGuesses = 0`: אתחול המשתנה `numberOfGuesses` לספירת מספר הניסיונות.
    - `targetNumber = random.randint(1, 10)`: יצירת מספר שלם אקראי בין 1 ל-10 ושמירתו במשתנה `targetNumber`.
3.  **לולאת המשחק `while True:`**:
    -  לולאה אינסופית, הממשיכה עד שהמשתמש נוחש את המספר (הפקודה `break` תסיים את הלולאה).
    - `numberOfGuesses += 1`: הגדלת מונה הניסיונות ב-1 בכל סיבוב של הלולאה.
    -  **קלט נתונים**:
        - `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין משהו שאינו מספר שלם, יוצג הודעת שגיאה.
        - `userGuess = int(input("הזן את הניחוש: "))`: בקשת מספר מהמשתמש והמרתו למספר שלם, ושמירתו במשתנה `userGuess`.
    -  **תנאי ניצחון**:
        - `if userGuess == targetNumber:`: בדיקה האם המספר שהוזן שווה למספר המוגלה.
        - `print(f"מזל טוב! ניחשת את המספר ב-{numberOfGuesses} ניסיונות!")`: הצגת הודעת ניצחון עם מספר הניסיונות.
        - `break`: סיום הלולאה (והמשחק) אם המספר נוחש.
    - **רמז**:
        - `else:`: אם המספר לא נוחש
        - `print("WRONG NUMBER")`: הצגת רמז שהמספר לא נכון.
"""
```
