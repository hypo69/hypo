# GUESS

## סקירה כללית

משחק "נחש את המספר" הוא משחק קלאסי בו המחשב בוחר מספר אקראי בטווח שבין 1 ל-100, והשחקן צריך לנחש את המספר הזה, תוך קבלת רמזים "נמוך מדי" או "גבוה מדי" לאחר כל ניסיון. המשחק נמשך עד שהשחקן מנחש את המספר.

## תוכן עניינים

1. [סקירה כללית](#סקירה-כללית)
2. [חוקי המשחק](#חוקי-המשחק)
3. [אלגוריתם](#אלגוריתם)
4. [תרשים זרימה](#תרשים-זרימה)
5. [מקרא](#מקרא)

## חוקי המשחק

1. המחשב בוחר מספר שלם אקראי מ-1 עד 100.
2. השחקן מזין את ההשערות שלו לגבי המספר הנבחר.
3. לאחר כל ניסיון, המחשב מודיע האם המספר שהוזן היה נמוך מדי, גבוה מדי או שנוחש.
4. המשחק נמשך עד שהשחקן מנחש את המספר הנבחר.

## אלגוריתם

1. הגדר את מספר הניסיונות ל-0.
2. צור מספר אקראי בטווח שבין 1 ל-100.
3. התחל לולאה "כל עוד המספר לא נוחש":
    3.1 הגדל את מספר הניסיונות ב-1.
    3.2 בקש מהשחקן להזין מספר.
    3.3 אם המספר שהוזן שווה למספר הנבחר, עבור לשלב 4.
    3.4 אם המספר שהוזן קטן מהמספר הנבחר, פלט את ההודעה "נמוך מדי".
    3.5 אם המספר שהוזן גדול מהמספר הנבחר, פלט את ההודעה "גבוה מדי".
4. פלט את ההודעה "ניחשת אותו בתוך {מספר ניסיונות} ניסיונות!"
5. סוף המשחק.

## תרשים זרימה

```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:\n    <code><b>\n    numberOfGuesses = 0\n    targetNumber = random(1, 100)\n    </b></code></p>"]
    InitializeVariables --> LoopStart{"התחלת לולאה: כל עוד לא נוחש"}\
    LoopStart -- כן --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputGuess["קלט מספר מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> CheckGuess{"בדיקה: <code><b>userGuess == targetNumber?</b></code>"}\
    CheckGuess -- כן --> OutputWin["פלט הודעה: <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES!</b>"]
    OutputWin --> End["סוף"]
    CheckGuess -- לא --> CheckLow{"בדיקה: <code><b>userGuess &lt; targetNumber</b></code>?"}
    CheckLow -- כן --> OutputLow["פלט הודעה: <b>TOO LOW</b>"]
    OutputLow --> LoopStart
    CheckLow -- לא --> OutputHigh["פלט הודעה: <b>TOO HIGH</b>"]
    OutputHigh --> LoopStart
    LoopStart -- לא --> End

```

## מקרא

    Start - תחילת התוכנית.
    InitializeVariables - אתחול משתנים: numberOfGuesses (מספר ניסיונות) מוגדר ל-0, ו-targetNumber (המספר הנבחר) נוצר באופן אקראי בין 1 ל-100.
    LoopStart - תחילת הלולאה שנמשכת כל עוד המספר לא נוחש.
    IncreaseGuesses - הגדלת מונה מספר הניסיונות ב-1.
    InputGuess - בקשה מהמשתמש להזין מספר ושמירתו במשתנה userGuess.
    CheckGuess - בדיקה האם המספר שהוזן userGuess שווה למספר הנבחר targetNumber.
    OutputWin - פלט הודעת ניצחון, אם המספרים שווים, עם ציון מספר הניסיונות.
    End - סוף התוכנית.
    CheckLow - בדיקה האם המספר שהוזן userGuess קטן מהמספר הנבחר targetNumber.
    OutputLow - פלט הודעה "TOO LOW", אם המספר שהוזן קטן מהנבחר.
    OutputHigh - פלט הודעה "TOO HIGH", אם המספר שהוזן גדול מהנבחר.