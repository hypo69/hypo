"""
HILO:
=================
קושי: 4
-----------------
המשחק "גבוה או נמוך" הוא משחק ניחושים בו המחשב בוחר מספר אקראי בין 1 ל-100, והשחקן מנסה לנחש את המספר. לאחר כל ניסיון, המחשב מגיב ב"גבוה מדי" או "נמוך מדי" עד שהשחקן מצליח לנחש את המספר הנכון.

חוקי המשחק:
1. המחשב בוחר מספר אקראי בין 1 ל-100.
2. השחקן מזין את הניחוש שלו.
3. המחשב מגיב עם "גבוה מדי" או "נמוך מדי" בהתאם לניחוש.
4. המשחק ממשיך עד שהשחקן מנחש את המספר הנכון.
-----------------
אלגוריתם:
1. אתחל את מספר הניחושים ל-0.
2. הגרל מספר אקראי בין 1 ל-100.
3. התחל לולאה: כל עוד לא נוחש המספר:
    3.1. הגדל את מספר הניחושים ב-1.
    3.2. קלוט ניחוש מהמשתמש.
    3.3. אם הניחוש שווה למספר המוגרל, עבור לשלב 4.
    3.4. אם הניחוש קטן מהמספר המוגרל, הדפס "TOO LOW".
    3.5. אם הניחוש גדול מהמספר המוגרל, הדפס "TOO HIGH".
4. הדפס "YOU GOT IT IN {מספר הניחושים} GUESSES!".
5. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    numberOfGuesses = 0
    targetNumber = random(1, 100)
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: כל עוד לא נוחש"}
    LoopStart -- כן --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputGuess["קלט מספר מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> CheckGuess{"בדיקה: <code><b>userGuess == targetNumber?</b></code>"}
    CheckGuess -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES!</b>"]
    OutputWin --> End["סוף"]
    CheckGuess -- לא --> CheckLow{"בדיקה: <code><b>userGuess < targetNumber</b></code>?"}
    CheckLow -- כן --> OutputLow["הצגת הודעה: <b>TOO LOW</b>"]
    OutputLow --> LoopStart
    CheckLow -- לא --> OutputHigh["הצגת הודעה: <b>TOO HIGH</b>"]
    OutputHigh --> LoopStart
    LoopStart -- לא --> End

```
Legenda:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: numberOfGuesses (מספר הניסיונות) מאותחל ל-0, ו-targetNumber (המספר המוגלה) נוצר באקראי בין 1 ל-100.
    LoopStart - תחילת הלולאה, הממשיכה כל עוד המספר לא נוחש.
    IncreaseGuesses - הגדלת מונה הניסיונות ב-1.
    InputGuess - קלט מספר מהמשתמש ושמירתו במשתנה userGuess.
    CheckGuess - בדיקה האם המספר שהוזן שווה למספר המוגלה.
    OutputWin - הצגת הודעת ניצחון, אם המספר נוחש, עם מספר הניסיונות.
    End - סוף התוכנית.
    CheckLow - בדיקה האם המספר שהוזן קטן מהמספר המוגלה.
    OutputLow - הצגת הודעה "TOO LOW", אם המספר שהוזן קטן מהמספר המוגלה.
    OutputHigh - הצגת הודעה "TOO HIGH", אם המספר שהוזן גדול מהמספר המוגלה.
"""
```python
import random

# אתחול מונה הניסיונות
numberOfGuesses = 0
# יצירת מספר אקראי בין 1 ל-100
targetNumber = random.randint(1, 100)

# לולאת המשחק הראשית
while True:
    # הגדלת מונה הניסיונות
    numberOfGuesses += 1
    # בקשת קלט מספר מהמשתמש
    try:
        userGuess = int(input("נחש מספר בין 1 ל-100: "))
    except ValueError:
        print("אנא הזן מספר שלם.")
        continue

    # בדיקה האם המספר נוחש
    if userGuess == targetNumber:
        print(f"מזל טוב! ניחשת את המספר ב-{numberOfGuesses} ניסיונות!")
        break  # סיום הלולאה אם המספר נוחש
    elif userGuess < targetNumber:
        print("TOO LOW")  # הודעה שהמספר המוגלה גדול יותר
    else:
        print("TOO HIGH")  # הודעה שהמספר המוגלה קטן יותר
```
"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    -  `import random`: ייבוא המודול `random`, המשמש ליצירת מספר אקראי.
2. **אתחול משתנים**:
    - `numberOfGuesses = 0`: אתחול מונה הניחושים לאפס.
    - `targetNumber = random.randint(1, 100)`: יצירת מספר אקראי שלם בין 1 ל-100 ושמירתו במשתנה `targetNumber`. זהו המספר שהשחקן צריך לנחש.
3.  **לולאת המשחק `while True:`**:
    - לולאה אינסופית, שתרוץ עד שהשחקן ינחש את המספר הנכון.
    - `numberOfGuesses += 1`: בכל סיבוב של הלולאה, מונה הניחושים גדל באחד.
4. **קבלת קלט מהמשתמש**:
   -  `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין משהו שאינו מספר שלם, תוצג הודעת שגיאה.
   -  `userGuess = int(input("נחש מספר בין 1 ל-100: "))`:  הצגת בקשה למשתמש להזין מספר. הקלט מומר למספר שלם ונשמר במשתנה `userGuess`.
5. **בדיקת הניחוש**:
    - `if userGuess == targetNumber:`: בדיקה האם הניחוש שווה למספר המוגרל.
        -  `print(f"מזל טוב! ניחשת את המספר ב-{numberOfGuesses} ניסיונות!")`: אם הניחוש נכון, תוצג הודעת ניצחון עם מספר הניחושים.
        - `break`: סיום הלולאה (והמשחק) אם הניחוש נכון.
   - `elif userGuess < targetNumber:`: בדיקה האם הניחוש קטן מהמספר המוגרל.
      - `print("TOO LOW")`: אם הניחוש קטן, תוצג הודעה "TOO LOW"
   - `else:`: אם הניחוש אינו נכון ואינו נמוך מהמספר המוגרל, הוא חייב להיות גדול ממנו.
     - `print("TOO HIGH")`: אם הניחוש גבוה, תוצג הודעה "TOO HIGH".
"""
