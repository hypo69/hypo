<HANG>:
=================
קושי: 4
-----------------
משחק ה"תלייה" הוא משחק מילים קלאסי בו שחקן אחד חושב על מילה, והשחקן השני צריך לנחש אותה על ידי ניחוש אותיות. עבור כל ניחוש שגוי, מצויר חלק מאיור התלייה. המטרה היא לנחש את המילה לפני שהאיור מושלם.
חוקי המשחק:
1. המחשב בוחר מילה אקראית מרשימת מילים.
2. השחקן מנסה לנחש את המילה על ידי ניחוש אות אחת בכל פעם.
3. אם האות שנבחרה נמצאת במילה, כל המופעים שלה נחשפים.
4. אם האות שנבחרה אינה במילה, נרשמת טעות.
5. המשחק נמשך עד שהמילה נוחשה או שהשחקן ביצע מספר מסוים של טעויות.
-----------------
אלגוריתם:
1.  הגדר רשימת מילים לבחירה אקראית.
2.  בחר מילה אקראית מהרשימה.
3.  אתחל משתנה לספירת טעויות (מאתחל ל-0)
4.  צור משתנה המייצג את המילה המנוחשת, כאשר כל האותיות מוחלפות בתו '_'.
5.  התחל לולאה "כל עוד המשחק לא הסתיים":
    5.1  הצג את המילה המנוחשת (עם '_' עבור אותיות לא מנוחשות).
    5.2 בקש מהמשתמש להזין אות.
    5.3 אם האות שהוזנה נמצאת במילה הנבחרת, חשוף את כל המופעים שלה במילה המנוחשת.
    5.4 אחרת, הגדל את מספר הטעויות ב-1.
    5.5 אם מספר הטעויות שווה או גדול מ-6, הפסק את המשחק והצג הודעת הפסד.
    5.6 אם המילה המנוחשת זהה למילה הנבחרת, הפסק את המשחק והצג הודעת ניצחון.
6. הצג הודעת סיום (ניצחון או הפסד).
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    words = [...]<br>
    secretWord = randomWord(words)<br>
    incorrectGuesses = 0<br>
    guessedWord = '_____'
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: כל עוד המשחק לא הסתיים"}
    LoopStart -- כן --> ShowGuessedWord["הצג את המילה המנוחשת: <code><b>guessedWord</b></code>"]
    ShowGuessedWord --> InputLetter["קלט אות מהמשתמש: <code><b>userLetter</b></code>"]
    InputLetter --> CheckLetter{"בדיקה: <code><b>userLetter in secretWord?</b></code>"}
    CheckLetter -- כן --> UpdateGuessedWord["עדכן את המילה המנוחשת: <code><b>guessedWord</b></code>"]
    UpdateGuessedWord --> CheckWin{"בדיקה: <code><b>guessedWord == secretWord?</b></code>"}
    CheckWin -- כן --> OutputWin["הצג הודעת ניצחון: <b>YOU GOT IT</b>"]
    OutputWin --> End["סוף"]
    CheckWin -- לא --> LoopStart
    CheckLetter -- לא --> IncreaseIncorrectGuesses["<code><b>incorrectGuesses = incorrectGuesses + 1</b></code>"]
     IncreaseIncorrectGuesses --> CheckLoss{"בדיקה: <code><b>incorrectGuesses >= 6?</b></code>"}
    CheckLoss -- כן --> OutputLoss["הצג הודעת הפסד: <b>YOU LOSE</b>"]
    OutputLoss --> End
    CheckLoss -- לא --> LoopStart
    LoopStart -- לא --> End
```
Legenda:
    Start - התחלת המשחק.
    InitializeVariables - אתחול משתנים: רשימת המילים, בחירת מילה אקראית, אתחול מונה טעויות, ויצירת משתנה המייצג את המילה המנוחשת עם קווים תחתונים.
    LoopStart - תחילת הלולאה הראשית של המשחק, כל עוד המשחק לא הסתיים (לא ניצחון ולא הפסד).
    ShowGuessedWord - הצגת המילה המנוחשת, עם קווים תחתונים במקום אותיות שלא נוחשו.
    InputLetter - קבלת קלט מהמשתמש - אות לניחוש.
    CheckLetter - בדיקה האם האות שהוזנה קיימת במילה הסודית.
    UpdateGuessedWord - עדכון המילה המנוחשת עם האות שנוחשה, אם היא קיימת במילה הסודית.
    CheckWin - בדיקה האם המילה המנוחשת זהה למילה הסודית (ניצחון).
    OutputWin - הצגת הודעת ניצחון.
    End - סיום המשחק.
    IncreaseIncorrectGuesses - הגדלת מונה הטעויות באחד, אם האות לא נמצאת במילה.
    CheckLoss - בדיקה האם מונה הטעויות גדול או שווה ל-6 (הפסד).
    OutputLoss - הצגת הודעת הפסד.
"""
import random

# רשימת מילים למשחק
words = ["python", "hangman", "computer", "programming", "algorithm", "variable"]

# בחירת מילה אקראית מהרשימה
secretWord = random.choice(words)
# אתחול מספר טעויות
incorrectGuesses = 0
# יצירת תבנית המילה המנוחשת (אותיות מוחלפות בקו תחתון)
guessedWord = "_" * len(secretWord)

# לולאת המשחק הראשית
while True:
    # הצגת המילה המנוחשת
    print("מילה: ", guessedWord)
    # קבלת קלט מהמשתמש
    userLetter = input("נחש אות: ").lower()

    # בדיקה האם האות נמצאת במילה
    if userLetter in secretWord:
        # עדכון המילה המנוחשת באותיות שהתגלו
        for i in range(len(secretWord)):
            if secretWord[i] == userLetter:
                guessedWord = guessedWord[:i] + userLetter + guessedWord[i + 1:]
        # בדיקה האם השחקן ניצח
        if guessedWord == secretWord:
             print("מזל טוב! ניצחת!")
             break  # סיום המשחק
    else:
        # הגדלת מספר הטעויות
        incorrectGuesses += 1
        print("טעות! מספר טעויות:", incorrectGuesses)
        # בדיקה האם השחקן הפסיד
        if incorrectGuesses >= 6:
            print("הפסדת! המילה הייתה:", secretWord)
            break  # סיום המשחק
"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    - `import random`: ייבוא מודול random המאפשר לבחור מילה אקראית מהרשימה.
2.  **הגדרת רשימת מילים `words`**:
    - `words = ["python", "hangman", "computer", "programming", "algorithm", "variable"]`: רשימה של מילים אפשריות למשחק התלייה.
3.  **בחירת מילה אקראית `secretWord`**:
    - `secretWord = random.choice(words)`: בחירה אקראית של מילה מרשימת המילים ושמירתה במשתנה secretWord.
4.  **אתחול משתנים**:
    - `incorrectGuesses = 0`: אתחול משתנה לספירת מספר הניחושים השגויים, מתחיל ב-0.
    - `guessedWord = "_" * len(secretWord)`: יצירת מחרוזת שמייצגת את המילה שהמשתמש מנסה לנחש, כל אות מוחלפת בתו "_".
5.  **לולאת המשחק `while True:`**:
    - לולאה אינסופית שרצה עד שהמשחק מסתיים (ניצחון או הפסד).
    - `print("מילה: ", guessedWord)`: הצגת המילה המנוחשת למשתמש, עם קווים תחתונים במקומות בהם עדיין לא נוחשו אותיות.
    - `userLetter = input("נחש אות: ").lower()`: קבלת קלט מהמשתמש (אות לניחוש), המרה לאותיות קטנות כדי למנוע בעיות רישיות.
6.  **בדיקה האם האות קיימת במילה `if userLetter in secretWord:`**:
    - אם האות נמצאת במילה הסודית:
        - מעבר על כל אות במילה הסודית.
        - אם אות מהמילה הסודית שווה לאות שהוזנה, האות נחשפת במחרוזת `guessedWord`.
        - `if guessedWord == secretWord:`: אם המילה המנוחשת זהה למילה הסודית, השחקן ניצח.
        - `print("מזל טוב! ניצחת!")`: הודעת ניצחון.
        - `break`: יציאה מלולאת המשחק.
7.  **אם האות לא קיימת במילה `else:`**:
    - `incorrectGuesses += 1`: הגדלת מספר הטעויות.
    - `print("טעות! מספר טעויות:", incorrectGuesses)`: הצגת הודעה על הטעות ומספר הטעויות הנוכחי.
    - `if incorrectGuesses >= 6:`: בדיקה האם מספר הטעויות הגיע ל-6 או יותר.
        - `print("הפסדת! המילה הייתה:", secretWord)`: הודעה על הפסד והצגת המילה הסודית.
        - `break`: יציאה מלולאת המשחק.
"""
