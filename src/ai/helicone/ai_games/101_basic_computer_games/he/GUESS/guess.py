<GUESS>:
=================
קושי: 2
-----------------
המשחק "נחש את המספר" הוא משחק פשוט שבו המחשב בוחר מספר אקראי בטווח מסוים, והשחקן מנסה לנחש אותו. המשחק נותן רמזים אם הניחוש גבוה או נמוך מדי.

חוקי המשחק:
1. המחשב בוחר מספר אקראי בין 1 ל-100.
2. השחקן מזין ניחוש.
3. המחשב מגיב ב-"TOO LOW" אם הניחוש נמוך מדי, או "TOO HIGH" אם הניחוש גבוה מדי.
4. המשחק ממשיך עד שהשחקן מנחש את המספר הנכון.
-----------------
אלגוריתם:
1. אתחל משתנה לספירת הניסיונות (לדוגמה: `attempts`) ל-0.
2. בחר מספר אקראי בין 1 ל-100 ושמור אותו במשתנה (לדוגמה: `secretNumber`).
3. התחל לולאה:
   - הגדל את מספר הניסיונות ב-1.
   - בקש מהשחקן לנחש מספר.
   - אם הניחוש שווה למספר הסודי, סיים את המשחק עם הודעת ניצחון והצג את מספר הניסיונות.
   - אם הניחוש קטן מהמספר הסודי, הצג הודעה "TOO LOW".
   - אחרת (אם הניחוש גדול מהמספר הסודי), הצג הודעה "TOO HIGH".
4. חזור ללולאה עד שהניחוש נכון.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    attempts = 0
    secretNumber = random(1, 100)
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: כל עוד לא נוחש"}
    LoopStart -- כן --> IncreaseAttempts["<code><b>attempts = attempts + 1</b></code>"]
    IncreaseAttempts --> InputGuess["קלט מספר מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> CheckGuess{"בדיקה: <code><b>userGuess == secretNumber?</b></code>"}
    CheckGuess -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT IN <code>{attempts}</code> GUESSES!</b>"]
    OutputWin --> End["סוף"]
    CheckGuess -- לא --> CheckLow{"בדיקה: <code><b>userGuess < secretNumber</b></code>?"}
    CheckLow -- כן --> OutputLow["הצגת הודעה: <b>TOO LOW</b>"]
    OutputLow --> LoopStart
    CheckLow -- לא --> OutputHigh["הצגת הודעה: <b>TOO HIGH</b>"]
    OutputHigh --> LoopStart
    LoopStart -- לא --> End
```
Legenda:
   Start - התחלת המשחק.
   InitializeVariables - אתחול המשתנים: `attempts` (מספר הניסיונות) מתחיל מ-0 ו-`secretNumber` (המספר הסודי) מקבל מספר אקראי בין 1 ל-100.
    LoopStart - תחילת הלולאה, הממשיכה כל עוד השחקן לא ניחש את המספר.
    IncreaseAttempts - הגדלת מספר הניסיונות ב-1.
    InputGuess - קבלת ניחוש מהשחקן ושמירתו במשתנה `userGuess`.
    CheckGuess - בדיקה האם הניחוש של השחקן שווה ל-`secretNumber`.
    OutputWin - אם הניחוש נכון, מוצגת הודעת ניצחון עם מספר הניסיונות, והמשחק מסתיים.
    End - סיום המשחק.
    CheckLow - בדיקה האם הניחוש נמוך מהמספר הסודי.
    OutputLow - אם הניחוש נמוך מדי, מוצגת ההודעה "TOO LOW".
    OutputHigh - אם הניחוש גבוה מדי, מוצגת ההודעה "TOO HIGH".
"""
import random

# אתחול מספר הניסיונות
attempts = 0
# בחירת מספר אקראי בין 1 ל-100
secretNumber = random.randint(1, 100)

# לולאת המשחק
while True:
    # הגדלת מספר הניסיונות
    attempts += 1
    # קבלת ניחוש מהמשתמש
    try:
      userGuess = int(input("נחש מספר בין 1 ל-100: "))
    except ValueError:
      print("אנא הזן מספר שלם.")
      continue
    # בדיקה אם הניחוש נכון
    if userGuess == secretNumber:
        print(f"מזל טוב! ניחשת את המספר ב-{attempts} ניסיונות!")
        break  # סיום הלולאה אם המספר נוחש
    # בדיקה אם הניחוש נמוך מדי
    elif userGuess < secretNumber:
        print("TOO LOW")
    # אם הניחוש גבוה מדי
    else:
        print("TOO HIGH")

"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    - `import random`: מייבא את המודול `random` שמאפשר ליצור מספרים אקראיים.
2.  **אתחול משתנים**:
    - `attempts = 0`: מאתחל את המשתנה `attempts` לספירת מספר הניסיונות, מתחיל מ-0.
    - `secretNumber = random.randint(1, 100)`: בוחר מספר שלם אקראי בין 1 ל-100 ושומר אותו במשתנה `secretNumber`. זהו המספר שהמשתמש צריך לנחש.
3.  **לולאת המשחק `while True`**:
    - לולאה אינסופית שרצה עד שהמשתמש מנחש את המספר הנכון.
    - `attempts += 1`: מגדיל את מספר הניסיונות ב-1 בכל סיבוב של הלולאה.
    - **קבלת קלט מהמשתמש**:
        - `try...except ValueError`: בלוק try-except שנועד לטפל במקרה שבו המשתמש מזין קלט לא תקין (שאינו מספר).
        - `userGuess = int(input("נחש מספר בין 1 ל-100: "))`: מבקש מהמשתמש להזין ניחוש וממיר אותו למספר שלם.
        - `continue` - אם הקלט לא תקין הלולאה מתחילה מההתחלה.
    - **בדיקת הניחוש**:
        - `if userGuess == secretNumber`: אם הניחוש שווה למספר הסודי:
            - `print(f"מזל טוב! ניחשת את המספר ב-{attempts} ניסיונות!")`: מוצגת הודעה שהמשתמש ניצח, כולל מספר הניסיונות.
            - `break`: יוצאים מהלולאה והמשחק מסתיים.
        - `elif userGuess < secretNumber`: אם הניחוש קטן מהמספר הסודי:
            - `print("TOO LOW")`: מוצגת ההודעה "TOO LOW".
        - `else`: אחרת (אם הניחוש גדול מהמספר הסודי):
            - `print("TOO HIGH")`: מוצגת ההודעה "TOO HIGH".
"""
