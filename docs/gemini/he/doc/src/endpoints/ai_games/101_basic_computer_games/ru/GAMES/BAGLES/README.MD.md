# BAGLES

## סקירה כללית

המשחק "בייגלס" הוא משחק היגיון וחידות בו השחקן מנסה לנחש מספר בעל שלוש ספרות המורכב מספרות שונות. לאחר כל ניסיון, השחקן מקבל רמזים: "PICO" מציין שאחת מהספרות נוחשה ונמצאת במיקום הנכון, "FERMI" מציין שאחת מהספרות נוחשה אך לא במיקום הנכון, ו-"BAGELS" מציין שאף אחת מהספרות לא נוחשה.

## תוכן עניינים

1. [סקירה כללית](#סקירה-כללית)
2. [חוקי המשחק](#חוקי-המשחק)
3. [אלגוריתם](#אלגוריתם)
4. [תרשים זרימה](#תרשים-זרימה)
5. [מקרא](#מקרא)

## חוקי המשחק

1. המחשב מייצר מספר אקראי בעל שלוש ספרות שונות.
2. השחקן מזין ניחוש בדמות מספר בעל שלוש ספרות.
3. המחשב מספק רמזים:
   - "PICO" - ספרה אחת נוחשה ונמצאת במיקום הנכון.
   - "FERMI" - ספרה אחת נוחשה אך לא במיקום הנכון.
   - "BAGELS" - אף אחת מהספרות לא נוחשה.
4. הרמזים ניתנים לפי סדר הספרות במספר הנכון. לדוגמה, אם המספר הוא `123` והשחקן הזין `142`, הרמזים יהיו `PICO FERMI`.
5. המשחק נמשך עד שהשחקן מנחש את המספר.
6. אם השחקן לא מצליח לנחש את המספר לאחר 10 ניסיונות, המשחק מסתיים והמספר הנכון מוצג.

## אלגוריתם

1. יצירת מספר אקראי בעל שלוש ספרות שונות (לדוגמה, 123).
2. הגדרת מספר הניסיונות ל-0.
3. לולאה "כל עוד המספר לא נוחש או מספר הניסיונות קטן מ-10":
    3.1. הגדלת מספר הניסיונות ב-1.
    3.2. בקשת קלט מהשחקן בדמות מספר בעל שלוש ספרות.
    3.3. השוואת הקלט עם המספר הנכון ויצירת רמזים "PICO", "FERMI", ו-"BAGELS".
    3.4. אם המספר נוחש, הצגת הודעת ניצחון ומספר הניסיונות.
    3.5. אם המספר לא נוחש, הצגת הרמזים.
4. אם לאחר 10 ניסיונות המספר לא נוחש, הצגת המספר הנכון והודעה על הפסד.
5. סיום המשחק.

## תרשים זרימה

```mermaid
flowchart TD
    Start["התחלה"] --> GenerateSecretNumber["<p align='left'>יצירת מספר סודי <code><b>secretNumber</b></code> (3 ספרות שונות)\n    <code><b>numberOfGuesses = 0</b></code>\n    </p>"]
    GenerateSecretNumber --> LoopStart{"תחילת לולאה: כל עוד לא נוחש ומספר הניסיונות < 10"}
    LoopStart -- כן --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputGuess["קלט מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> GenerateClues["<p align='left'>יצירת רמזים (<code><b>clues</b></code>):\n    <ul>\n    <li><code><b>PICO</b></code>- ספרה נוחשה ובמקום הנכון</li>\n    <li><code><b>FERMI</b></code> - ספרה נוחשה אבל לא במקום הנכון</li>\n    <li><code><b>BAGELS</b></code> - אף ספרה לא נוחשה</li>\n    </ul></p>"]
    GenerateClues --> CheckWin{"בדיקה: <code><b>userGuess == secretNumber?</b></code>"}
    CheckWin -- כן --> OutputWin["הצגת הודעת ניצחון ומספר הניסיונות"]
    OutputWin --> End["סיום"]
    CheckWin -- לא --> OutputClues["הצגת רמזים <code><b>clues</b></code>"]
    OutputClues --> LoopStart
    LoopStart -- לא --> CheckLose{"בדיקה: <code><b>numberOfGuesses == 10?</b></code>"}
    CheckLose -- כן --> OutputLose["הצגת הודעת הפסד ו-<code><b>secretNumber</b></code>"]
    OutputLose --> End
    CheckLose -- לא --> LoopStart

```

## מקרא

   - Start - תחילת המשחק.
   - GenerateSecretNumber - יצירת מספר סודי `secretNumber` עם 3 ספרות שונות ואתחול מספר הניסיונות ל-`numberOfGuesses = 0`.
   - LoopStart - תחילת לולאה שנמשכת כל עוד המספר לא נוחש ומספר הניסיונות קטן מ-10.
   - IncreaseGuesses - הגדלת מונה הניסיונות ב-1.
   - InputGuess - קבלת קלט מהמשתמש ושמירתו ב-`userGuess`.
   - GenerateClues - יצירת רמזים בהתאם להשוואה בין `userGuess` ל-`secretNumber`.
   - CheckWin - בדיקה האם `userGuess` שווה ל-`secretNumber`.
   - OutputWin - הצגת הודעת ניצחון ומספר הניסיונות.
   - End - סוף המשחק.
   - OutputClues - הצגת הרמזים שנוצרו.
   - CheckLose - בדיקה האם מספר הניסיונות הגיע ל-10.
   - OutputLose - הצגת הודעת הפסד והמספר הסודי `secretNumber`.