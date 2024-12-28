"""
ICHECK:
=================
קושי: 4
-----------------
המשחק "ICHECK" הוא משחק שבו המחשב בוחר מספר רנדומלי בין 1 ל-9, והשחקן מנסה לנחש אותו. לאחר כל ניסיון, המחשב מציג רמז אם הניחוש גבוה או נמוך מדי, עד שהשחקן מצליח לנחש את המספר הנכון.

חוקי המשחק:
1. המחשב בוחר מספר אקראי בין 1 ל-9.
2. השחקן מנסה לנחש את המספר על ידי הזנת ניחוש.
3. אם הניחוש נכון, המשחק מסתיים.
4. אם הניחוש לא נכון, המחשב מציג הודעה "TOO HIGH" אם הניחוש גבוה מדי, או "TOO LOW" אם הניחוש נמוך מדי.
5. המשחק ממשיך עד שהשחקן מנחש את המספר הנכון.
-----------------
אלגוריתם:
1. בחר מספר רנדומלי בין 1 ל-9.
2. התחל לולאה:
    3. קבל ניחוש מהמשתמש.
    4. אם הניחוש שווה למספר הרנדומלי:
        - הצג הודעה "GOOD" וסיים את הלולאה.
    5. אחרת, אם הניחוש גדול מהמספר הרנדומלי:
        - הצג הודעה "TOO HIGH".
    6. אחרת:
        - הצג הודעה "TOO LOW".
7. סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeTargetNumber["<p align='left'>אתחול משתנה: <br><code><b>targetNumber = random(1, 9)</b></code></p>"]
    InitializeTargetNumber --> LoopStart{"תחילת לולאה: כל עוד לא נוחש"}
    LoopStart --> InputGuess["קלט מספר מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> CheckGuess{"בדיקה: <code><b>userGuess == targetNumber?</b></code>"}
    CheckGuess -- כן --> OutputWin["הצגת הודעה: <b>GOOD</b>"]
    OutputWin --> End["סוף"]
    CheckGuess -- לא --> CheckLow{"בדיקה: <code><b>userGuess < targetNumber?</b></code>"}
    CheckLow -- כן --> OutputLow["הצגת הודעה: <b>TOO LOW</b>"]
    OutputLow --> LoopStart
    CheckLow -- לא --> OutputHigh["הצגת הודעה: <b>TOO HIGH</b>"]
    OutputHigh --> LoopStart
    LoopStart -- לא --> End
```
Legenda:
   Start - התחלת התוכנית.
   InitializeTargetNumber - אתחול משתנה targetNumber (המספר המוגלה) עם מספר אקראי בין 1 ל-9.
   LoopStart - תחילת הלולאה, הממשיכה כל עוד המספר לא נוחש.
   InputGuess - קלט מספר מהמשתמש ושמירתו במשתנה userGuess.
   CheckGuess - בדיקה האם המספר שהוזן שווה למספר המוגלה.
   OutputWin - הצגת הודעת ניצחון "GOOD", אם המספר נוחש.
   End - סוף התוכנית.
   CheckLow - בדיקה האם המספר שהוזן קטן מהמספר המוגלה.
   OutputLow - הצגת הודעה "TOO LOW", אם המספר שהוזן קטן מהמספר המוגלה.
   OutputHigh - הצגת הודעה "TOO HIGH", אם המספר שהוזן גדול מהמספר המוגלה.
"""
```python
import random

# פונקציה שמגדירה את המשחק
def play_icheck_game():
    # יצירת מספר אקראי בין 1 ל-9
    targetNumber = random.randint(1, 9)

    # לולאה ראשית של המשחק
    while True:
        # בקשת ניחוש מהמשתמש
        try:
            userGuess = int(input("נחש מספר בין 1 ל-9: "))
        except ValueError:
            print("אנא הזן מספר שלם.")
            continue

        # בדיקה האם הניחוש נכון
        if userGuess == targetNumber:
            print("GOOD")
            break  # סיום הלולאה והמשחק אם הניחוש נכון
        elif userGuess < targetNumber:
            print("TOO LOW") # רמז שהניחוש נמוך מדי
        else:
            print("TOO HIGH") # רמז שהניחוש גבוה מדי

# הפעלת המשחק רק אם הקובץ רץ ישירות
if __name__ == "__main__":
    play_icheck_game()
```
<הערות סיום>
הסבר מפורט לקוד:

1.  **ייבוא המודול `random`**:
    -   `import random`: מייבא את מודול `random` שימושי ליצירת מספרים אקראיים.
2.  **הגדרת הפונקציה `play_icheck_game()`**:
    -   `def play_icheck_game():`: מגדיר את הפונקציה שתכיל את כל הלוגיקה של המשחק.
3.  **יצירת מספר אקראי**:
    -   `targetNumber = random.randint(1, 9)`: משתמש בפונקציה `randint` ממודול `random` כדי לייצר מספר שלם אקראי בין 1 ל-9 (כולל 1 ו-9) ושומר אותו במשתנה `targetNumber`. זה המספר שהמשתמש צריך לנחש.
4.  **לולאת המשחק `while True:`**:
    -   לולאה אינסופית שתמשיך לרוץ עד שהמשתמש מנחש נכון את המספר.
5.  **קבלת ניחוש מהמשתמש**:
    -   `try...except ValueError`: בלוק לטיפול בשגיאות, כדי לוודא שהמשתמש מזין מספר שלם ולא טקסט או ערך אחר שאינו מספר.
    -   `userGuess = int(input("נחש מספר בין 1 ל-9: "))`: מציג הודעה למשתמש ומקבל את הניחוש שלו.
    -   `int(...)`: ממיר את הקלט של המשתמש למספר שלם.
    -   `continue`: אם המשתמש הכניס ערך שאינו מספר, הלולאה חוזרת להתחלה ומבקשת קלט מחדש.
6.  **בדיקת הניחוש**:
    -   `if userGuess == targetNumber:`: בודק האם הניחוש של המשתמש שווה למספר האקראי שהוגרל.
        -   `print("GOOD")`: אם הניחוש נכון, מדפיס הודעה למשתמש "GOOD".
        -   `break`: יוצא מהלולאה ומשחק מסתיים.
    -   `elif userGuess < targetNumber:`: בודק האם הניחוש נמוך מהמספר האקראי.
        -   `print("TOO LOW")`: אם הניחוש נמוך, מציג למשתמש הודעה "TOO LOW" כדי לתת רמז.
    -   `else:`: אם הניחוש לא נכון ולא נמוך, אז הוא חייב להיות גבוה.
        -   `print("TOO HIGH")`: מציג הודעה למשתמש "TOO HIGH" כרמז.
7.  **הפעלת המשחק**:
    -   `if __name__ == "__main__":`: בלוק זה מבטיח שהפונקציה `play_icheck_game` תפעל רק כאשר הקובץ רץ ישירות, ולא כאשר הוא מיובא כמודול.
    -   `play_icheck_game()`: קורא לפונקציה להפעלת המשחק.
</הערות סיום>
