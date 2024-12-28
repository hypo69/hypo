"""
<HMRABI>:
=================
קושי: 5
-----------------
המשחק HMRABI מדמה משחק של ניסיון לנחש מספר שאותו המחשב בחר, בדומה למשחק "נחש את המספר", אבל כאן במקום להשתמש במספרים רגילים, משתמשים בבסיס הקסדצימלי. כלומר, המספר המבוקש יהיה בין 0 ל-FFF (4095 בבסיס עשרוני), והמשתמש צריך להכניס מספרים בבסיס זה עד שהוא מצליח. המשחק מספק רמזים אם הניחוש גבוה או נמוך מדי, אבל בניגוד למשחק הקודם הרמזים האלו ניתנים בבסיס הקסדצימלי.

חוקי המשחק:
1. המחשב בוחר מספר אקראי בין 0 ל-4095 (שזה FFF בבסיס הקסדצימלי).
2. השחקן מזין ניחוש בבסיס הקסדצימלי.
3. המשחק מגיב ב"TOO LOW" אם הניחוש נמוך מהמספר הנבחר, או "TOO HIGH" אם הניחוש גבוה מהמספר הנבחר. התגובות ניתנות בבסיס הקסדצימלי.
4. המשחק ממשיך עד שהשחקן מנחש את המספר הנכון.
-----------------
אלגוריתם:
1. הגרל מספר אקראי בין 0 ל-4095 (בבסיס עשרוני) ושמור אותו במשתנה `targetNumber`.
2. התחל לולאה שרצה כל עוד לא ניחשנו נכון:
    2.1. קלוט ניחוש מהמשתמש בבסיס הקסדצימלי ושמור אותו במשתנה `userGuess`.
    2.2. המר את הניחוש מהבסיס ההקסדצימלי לבסיס העשרוני.
    2.3. אם הניחוש שווה למספר הנבחר, צא מהלולאה.
    2.4. אם הניחוש קטן מהמספר הנבחר, הצג "TOO LOW" בבסיס הקסדצימלי.
    2.5. אם הניחוש גדול מהמספר הנבחר, הצג "TOO HIGH" בבסיס הקסדצימלי.
3. הצג הודעה שהשחקן ניצח עם מספר הניסיונות.
4. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    numberOfGuesses = 0
    targetNumber = random(0, 4095)
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: כל עוד לא נוחש"}
    LoopStart -- כן --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputGuess["קלט מספר הקסדצימלי מהמשתמש: <code><b>userGuessHex</b></code>"]
    InputGuess --> ConvertHexToDec["המרה מבסיס הקסדצימלי לבסיס עשרוני: <code><b>userGuess = int(userGuessHex, 16)</b></code>"]
    ConvertHexToDec --> CheckGuess{"בדיקה: <code><b>userGuess == targetNumber?</b></code>"}
    CheckGuess -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES!</b>"]
    OutputWin --> End["סוף"]
    CheckGuess -- לא --> CheckLow{"בדיקה: <code><b>userGuess < targetNumber</b></code>?"}
    CheckLow -- כן --> OutputLow["הצגת הודעה: <b>TOO LOW</b> (בבסיס הקסדצימלי)"]
    OutputLow --> LoopStart
    CheckLow -- לא --> OutputHigh["הצגת הודעה: <b>TOO HIGH</b> (בבסיס הקסדצימלי)"]
    OutputHigh --> LoopStart
    LoopStart -- לא --> End
```
Legenda:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: numberOfGuesses (מספר הניסיונות) מאותחל ל-0, ו-targetNumber (המספר המוגלה) נוצר באקראי בין 0 ל-4095.
    LoopStart - תחילת הלולאה, הממשיכה כל עוד המספר לא נוחש.
    IncreaseGuesses - הגדלת מונה הניסיונות ב-1.
    InputGuess - קלט מספר הקסדצימלי מהמשתמש ושמירתו במשתנה userGuessHex.
    ConvertHexToDec - המרת המספר מבסיס הקסדצימלי לבסיס עשרוני ושמירתו במשתנה userGuess.
    CheckGuess - בדיקה האם המספר שהוזן (בבסיס עשרוני) שווה למספר המוגלה.
    OutputWin - הצגת הודעת ניצחון, אם המספר נוחש, עם מספר הניסיונות.
    End - סוף התוכנית.
    CheckLow - בדיקה האם המספר שהוזן (בבסיס עשרוני) קטן מהמספר המוגלה.
    OutputLow - הצגת הודעה "TOO LOW" (בבסיס הקסדצימלי), אם המספר שהוזן קטן מהמספר המוגלה.
    OutputHigh - הצגת הודעה "TOO HIGH" (בבסיס הקסדצימלי), אם המספר שהוזן גדול מהמספר המוגלה.
"""
```python
import random

# אתחול מונה הניסיונות
numberOfGuesses = 0
# יצירת מספר אקראי בין 0 ל-4095
targetNumber = random.randint(0, 4095)

# לולאת המשחק הראשית
while True:
    # הגדלת מונה הניסיונות
    numberOfGuesses += 1
    # בקשת קלט מספר הקסדצימלי מהמשתמש
    userGuessHex = input("נחש מספר הקסדצימלי בין 0 ל-FFF: ")
    
    try:
        # המרת הקלט מבסיס הקסדצימלי לעשרוני
        userGuess = int(userGuessHex, 16)
    except ValueError:
        print("אנא הזן מספר הקסדצימלי חוקי.")
        continue

    # בדיקה האם המספר נוחש
    if userGuess == targetNumber:
        print(f"מזל טוב! ניחשת את המספר ב-{numberOfGuesses} ניסיונות!")
        break  # סיום הלולאה אם המספר נוחש
    elif userGuess < targetNumber:
        # המרת התגובה לבסיס הקסדצימלי
        print(f"TOO LOW ({hex(userGuess)[2:].upper()})")  # הודעה שהמספר המוגלה גדול יותר
    else:
        # המרת התגובה לבסיס הקסדצימלי
        print(f"TOO HIGH ({hex(userGuess)[2:].upper()})")  # הודעה שהמספר המוגלה קטן יותר
```
"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    -   `import random`: ייבוא המודול `random`, המשמש ליצירת מספר אקראי.
2.  **אתחול משתנים**:
    -   `numberOfGuesses = 0`: אתחול מונה הניסיונות ל-0.
    -   `targetNumber = random.randint(0, 4095)`: יצירת מספר אקראי בין 0 ל-4095 (שזה FFF בבסיס הקסדצימלי) ושמירתו במשתנה `targetNumber`.
3.  **לולאת המשחק `while True:`**:
    -   לולאה אינסופית, הממשיכה עד שהמשתמש מנחש את המספר.
    -   `numberOfGuesses += 1`: הגדלת מונה הניסיונות ב-1 בכל סיבוב.
    -   **קלט נתונים**:
        -   `userGuessHex = input("נחש מספר הקסדצימלי בין 0 ל-FFF: ")`: בקשת מספר הקסדצימלי מהמשתמש ושמירתו במשתנה `userGuessHex`.
        -   `try...except ValueError`: טיפול בשגיאות אפשריות אם המשתמש מזין קלט שאינו חוקי בבסיס הקסדצימלי.
        -   `userGuess = int(userGuessHex, 16)`: המרת הקלט מבסיס הקסדצימלי לבסיס עשרוני.
    -   **בדיקה אם המספר נוחש**:
        -   `if userGuess == targetNumber:`: בדיקה האם המספר שהומר לבסיס עשרוני שווה למספר המוגלה.
        -   `print(f"מזל טוב! ניחשת את המספר ב-{numberOfGuesses} ניסיונות!")`: הצגת הודעת ניצחון עם מספר הניסיונות.
        -   `break`: סיום הלולאה (והמשחק) אם המספר נוחש.
    -   **רמזים**:
        -   `elif userGuess < targetNumber:`: בדיקה האם המספר שהוזן קטן מהמספר המוגלה.
        -   `print(f"TOO LOW ({hex(userGuess)[2:].upper()})")`: הצגת הודעה "TOO LOW" כאשר התגובה מומרת בחזרה לבסיס הקסדצימלי.
        -  `else`: אם המספר לא נוחש ולא קטן ממנו, הוא גדול ממנו.
        -   `print(f"TOO HIGH ({hex(userGuess)[2:].upper()})")`: הצגת הודעה "TOO HIGH" כאשר התגובה מומרת בחזרה לבסיס הקסדצימלי.

הפונקציה `hex()` ממירה מספר עשרוני למחרוזת הקסדצימלית, והסיומת `[2:].upper()` מסירה את הקידומת `0x` והופכת את האותיות לרישיות.
"""
