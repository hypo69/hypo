"""
DOGS:
=================
קושי: 4
-----------------
במשחק "DOGS" המחשב בוחר 3 מספרים אקראיים בין 1 ל-100, והשחקן מנסה לנחש אותם. לאחר כל ניסיון, המחשב מציג כמה מהמספרים שהשחקן ניחש נמצאים במקומות הנכונים (כלומר "כלבים") וכמה מהמספרים קיימים, אך לא במקום הנכון (כלומר "חתולים"). המשחק נמשך עד שהשחקן מצליח לנחש את כל 3 המספרים.

חוקי המשחק:
1. המחשב בוחר 3 מספרים אקראיים שונים בין 1 ל-100.
2. השחקן מזין 3 מספרים בתור ניחוש.
3. לאחר כל ניחוש, המחשב מציג:
   - מספר "הכלבים" - המספרים שהוזנו במקומות הנכונים.
   - מספר "החתולים" - המספרים שהוזנו קיימים, אך לא במקומות הנכונים.
4. המשחק נמשך עד שהשחקן מנחש את כל 3 המספרים במקומות הנכונים.
-----------------
אלגוריתם:
1. בחר 3 מספרים אקראיים שונים בטווח 1-100. שמור את המספרים ב-`targetNumbers`.
2. אתחל את `numberOfGuesses` ל-0.
3. התחל לולאה:
    3.1. הגדל את `numberOfGuesses` ב-1.
    3.2. קבל מהמשתמש 3 מספרים כניחוש. שמור אותם ב-`userGuess`.
    3.3. אתחל את מספר הכלבים (`dogs`) ל-0 ואת מספר החתולים (`cats`) ל-0.
    3.4. עבור על כל מספר ב-`userGuess` ועל האינדקס שלו:
        3.4.1. אם המספר שווה למספר ב-`targetNumbers` באותו אינדקס, הגדל את `dogs` ב-1.
        3.4.2. אם המספר קיים ב-`targetNumbers`, הגדל את `cats` ב-1.
    3.5. אם `dogs` שווה ל-3, הצג הודעת ניצחון והצג את מספר הניסיונות וסיים את הלולאה.
    3.6. אחרת, הצג את מספר הכלבים והחתולים ואת מספר הניסיונות.
4. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    targetNumbers = [random(1,100), random(1,100), random(1,100)]<br>
    numberOfGuesses = 0
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה"}
    LoopStart --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputGuess["קלט 3 מספרים מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> InitializeCounters["<p align='left'>אתחול מוני כלבים וחתולים:
    <code><b>dogs = 0, cats = 0</b></code></p>"]
    InitializeCounters --> CheckNumbersLoopStart{"תחילת לולאה: עבור כל מספר ב-<code>userGuess</code>"}
    CheckNumbersLoopStart --> CheckDog{"בדיקה: <code><b>userGuess[i] == targetNumbers[i]?</b></code>"}
    CheckDog -- כן --> IncreaseDogs["<code><b>dogs = dogs + 1</b></code>"]
    IncreaseDogs --> CheckCat{"בדיקה: <code><b>userGuess[i] in targetNumbers?</b></code>"}
    CheckDog -- לא -->  CheckCat
    CheckCat -- כן --> IncreaseCats["<code><b>cats = cats + 1</b></code>"]
    CheckCat -- לא --> CheckNumbersLoopEnd{"סוף לולאה"}
    IncreaseCats --> CheckNumbersLoopEnd
    CheckNumbersLoopEnd --> CheckWin{"בדיקה: <code><b>dogs == 3?</b></code>"}
    CheckWin -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES!</b>"]
    OutputWin --> End["סוף"]
    CheckWin -- לא --> OutputHints["הצגת הודעה: <b><code>{dogs}</code> DOGS, <code>{cats - dogs}</code> CATS</b>"]
    OutputHints --> LoopStart
```
Legenda:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: `targetNumbers` (רשימת 3 מספרים אקראיים בין 1 ל-100), `numberOfGuesses` (מספר ניסיונות) מאותחל ל-0.
    LoopStart - תחילת הלולאה הראשית, המשך עד שהשחקן מנחש את כל המספרים.
    IncreaseGuesses - הגדלת מונה הניסיונות ב-1.
    InputGuess - קלט 3 מספרים מהמשתמש ושמירתם במשתנה `userGuess`.
    InitializeCounters - אתחול משתני העזר: `dogs` (מספר הכלבים) ו-`cats` (מספר החתולים) ל-0.
    CheckNumbersLoopStart - תחילת לולאה שרצה על המספרים שהשחקן הכניס.
    CheckDog - בדיקה האם המספר שהוזן נמצא במקום הנכון.
    IncreaseDogs - הגדלת מונה הכלבים ב-1.
    CheckCat - בדיקה האם המספר שהוזן קיים בתוך רשימת המספרים המוגלים, גם אם לא במיקום הנכון.
    IncreaseCats - הגדלת מונה החתולים ב-1.
    CheckNumbersLoopEnd - סיום לולאת בדיקת המספרים.
    CheckWin - בדיקה האם השחקן ניחש את כל המספרים (האם מספר הכלבים שווה ל-3)
    OutputWin - הצגת הודעת ניצחון, אם השחקן ניחש, עם מספר הניסיונות.
    End - סוף התוכנית.
    OutputHints - הצגת רמזים לשחקן: מספר הכלבים והחתולים.
"""
import random

def play_dogs_game():
    # בחירת 3 מספרים אקראיים שונים בין 1 ל-100
    targetNumbers = random.sample(range(1, 101), 3)
    numberOfGuesses = 0  # אתחול מונה הניסיונות

    # לולאת המשחק הראשית
    while True:
        numberOfGuesses += 1  # הגדלת מספר הניסיונות
        
        # קבלת קלט מהמשתמש
        userGuess = []
        while len(userGuess) < 3:
            try:
                num = int(input(f"נחש את המספר ה-{len(userGuess)+1} (1-100): "))
                if 1 <= num <= 100:
                  userGuess.append(num)
                else:
                    print("אנא הזן מספר בין 1 ל-100.")
            except ValueError:
                print("אנא הזן מספר שלם.")

        dogs = 0  # אתחול מונה הכלבים
        cats = 0  # אתחול מונה החתולים

        # בדיקת כל מספר שהשחקן ניחש
        for i in range(3):
            if userGuess[i] == targetNumbers[i]:
                dogs += 1 # הגדלת מספר הכלבים אם המספר במקום הנכון
            if userGuess[i] in targetNumbers:
                 cats += 1 # הגדלת מספר החתולים אם המספר קיים ברשימה

        # בדיקה אם כל המספרים נוחשו
        if dogs == 3:
            print(f"מזל טוב! ניחשת את כל המספרים ב-{numberOfGuesses} ניסיונות!")
            break  # סיום הלולאה אם כל המספרים נוחשו
        else:
            print(f"ניסית {numberOfGuesses}, יש לך {dogs} כלבים, ו- {cats - dogs} חתולים")

if __name__ == "__main__":
    play_dogs_game()
"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    - `import random`: ייבוא המודול `random`, המשמש ליצירת מספרים אקראיים.

2.  **הגדרת הפונקציה `play_dogs_game()`**:
    - פונקציה זו מכילה את כל הלוגיקה של המשחק "DOGS".

3.  **אתחול משתנים**:
    - `targetNumbers = random.sample(range(1, 101), 3)`: יצירת רשימה של 3 מספרים אקראיים שונים בין 1 ל-100.
    - `numberOfGuesses = 0`: אתחול מונה הניסיונות.

4.  **לולאת המשחק הראשית (`while True`)**:
    - לולאה אינסופית, שתמשיך עד שהשחקן ינצח.
    - `numberOfGuesses += 1`: הגדלת מונה הניסיונות בכל סיבוב.
        
5.  **קבלת קלט מהמשתמש**:
    - לולאת `while` שרצה עד שהמשתמש יזין 3 מספרים תקינים (בטווח 1-100).
    - בלוק `try-except` לטיפול בשגיאות קלט.

6.  **אתחול מוני כלבים וחתולים**:
    - `dogs = 0`: אתחול מונה הכלבים ל-0.
    - `cats = 0`: אתחול מונה החתולים ל-0.

7.  **בדיקת המספרים שהשחקן ניחש**:
    - לולאת `for` שרצה על כל אחד מהמספרים שהשחקן ניחש.
    - `if userGuess[i] == targetNumbers[i]`: בדיקה האם המספר במקום הנכון - אם כן, מגדילה את מונה הכלבים (`dogs`).
    - `if userGuess[i] in targetNumbers`: בדיקה האם המספר קיים ברשימת המספרים המוגלים - אם כן, מגדילה את מונה החתולים (`cats`).

8.  **בדיקת ניצחון**:
    - `if dogs == 3`: בדיקה האם השחקן ניחש את כל המספרים במקומות הנכונים.
    - אם כן, מודפסת הודעת ניצחון עם מספר הניסיונות, והלולאה מסתיימת באמצעות `break`.
    - אחרת מודפסת הודעה עם מספר הכלבים והחתולים, וממשיכים לסיבוב נוסף.

9.  **הפעלת המשחק**:
    - `if __name__ == "__main__":`: בדיקה האם הקובץ מופעל ישירות.
    - `play_dogs_game()`: הפעלת המשחק על ידי קריאה לפונקציה.
"""
