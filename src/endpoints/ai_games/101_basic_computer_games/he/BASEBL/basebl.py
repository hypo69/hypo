<BASEBL>:
=================
קושי: 5
-----------------
משחק הבייסבול הוא משחק ניחושים בו המחשב בוחר רצף של ארבע ספרות ייחודיות, והשחקן מנסה לנחש אותן. לאחר כל ניחוש, המחשב מגיב בכמה "בייס" (ספרה נכונה במיקום נכון) וכמה "בול" (ספרה נכונה במיקום שגוי). השחקן מנצח כאשר הוא מנחש את הרצף הנכון.
חוקי המשחק:
1. המחשב בוחר מספר בן 4 ספרות ייחודיות.
2. השחקן מנסה לנחש את המספר.
3. המחשב מגיב בכמה ספרות נכונות במיקום הנכון (בייס) ובכמה ספרות נכונות במיקום שגוי (בול).
4. המשחק נמשך עד שהשחקן מנחש נכון את המספר.
-----------------
אלגוריתם:
1. הגדר משתנים:
     - `numberOfGuesses` - מספר הניסיונות, אתחול ל-0.
     - `targetNumber` - רשימה של 4 ספרות אקראיות ושונות.
2. הדפס הודעת פתיחה.
3. לולאה ראשית:
    3.1. הגדל את מספר הניסיונות ב-1.
    3.2. קלוט ניחוש מהשחקן (מחרוזת של 4 ספרות).
    3.3. אתחל משתנים לספירת בייס ובול לאפס.
    3.4. לולאה על הספרות:
      - אם הספרה מהניחוש תואמת לספרה במספר המטרה באותו מיקום, הגדל את ספירת הבייס.
      - אחרת, אם הספרה מהניחוש נמצאת במספר המטרה (במיקום אחר), הגדל את ספירת הבול.
    3.5. הצג את מספר הבייס והבול לשחקן.
    3.6. אם ספירת הבייס שווה ל-4, השחקן ניצח, הדפס הודעת ניצחון וצא מהלולאה.
4. סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    numberOfGuesses = 0<br>
    targetNumber =  רשימה של 4 ספרות אקראיות ושונות
    </b></code></p>"]
    InitializeVariables --> OutputStartMessage["הצגת הודעת פתיחה"]
    OutputStartMessage --> LoopStart{"תחילת לולאה"}
    LoopStart --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputGuess["קלט ניחוש מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> InitializeCounts["<p align='left'>אתחול מוני בייס ובול:
    <code><b>
    basesCount = 0<br>
    ballsCount = 0
    </b></code></p>"]
    InitializeCounts --> LoopDigitsStart{"תחילת לולאה על הספרות"}
    LoopDigitsStart --> CheckBase{"בדיקה: <code><b>userGuess[i] == targetNumber[i]</b></code>"}
    CheckBase -- כן --> IncreaseBaseCount["<code><b>basesCount = basesCount + 1</b></code>"]
    IncreaseBaseCount --> LoopDigitsNext{"מעבר לספרה הבאה"}
    CheckBase -- לא --> CheckBall{"בדיקה: האם <code><b>userGuess[i]</b></code> קיימת ב-<code><b>targetNumber</b></code>?"}
    CheckBall -- כן --> IncreaseBallCount["<code><b>ballsCount = ballsCount + 1</b></code>"]
    IncreaseBallCount --> LoopDigitsNext
    CheckBall -- לא --> LoopDigitsNext
    LoopDigitsNext --> LoopDigitsEnd{"סוף לולאה על הספרות?"}
    LoopDigitsEnd -- לא --> LoopDigitsStart
    LoopDigitsEnd -- כן --> OutputFeedback["הצגת פידבק: <code><b>{basesCount} בייס, {ballsCount} בול</b></code>"]
    OutputFeedback --> CheckWin{"בדיקה: <code><b>basesCount == 4</b></code>?"}
    CheckWin -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES!</b>"]
    OutputWin --> End["סוף"]
    CheckWin -- לא --> LoopStart
    LoopStart -- לא --> End
```
Legenda:
  Start - התחלת התוכנית.
  InitializeVariables - אתחול משתנים: `numberOfGuesses` (מספר הניסיונות) מאותחל ל-0, ו-`targetNumber` (רשימת הספרות המוגלות) נוצרת באקראי.
  OutputStartMessage - הצגת הודעת פתיחה למשחק.
  LoopStart - תחילת הלולאה הראשית, הממשיכה עד שהמספר נוחש.
  IncreaseGuesses - הגדלת מונה הניסיונות ב-1.
  InputGuess - קלט ניחוש מהמשתמש ושמירתו במשתנה `userGuess`.
  InitializeCounts - אתחול מוני הבייס (`basesCount`) והבול (`ballsCount`) ל-0.
  LoopDigitsStart - תחילת לולאה על ספרות הניחוש והמספר המוגלה.
  CheckBase - בדיקה האם הספרה במיקום הנוכחי בתוך הניחוש זהה לספרה באותו מיקום במספר המוגלה.
  IncreaseBaseCount - הגדלת מונה הבייס ב-1.
  CheckBall - בדיקה האם הספרה במיקום הנוכחי בתוך הניחוש קיימת במספר המוגלה אך לא באותו מיקום.
  IncreaseBallCount - הגדלת מונה הבול ב-1.
  LoopDigitsNext - מעבר לספרה הבאה.
  LoopDigitsEnd - בדיקה האם סיימנו לעבור על כל הספרות.
  OutputFeedback - הצגת פידבק למשתמש: כמה בייס וכמה בול הוא קיבל בניחוש הנוכחי.
  CheckWin - בדיקה האם מספר הבייס שווה ל-4, מה שמסמן ניצחון.
  OutputWin - הצגת הודעת ניצחון, כולל מספר הניסיונות.
  End - סוף התוכנית.
"""
```python
import random

def generate_target_number():
    """יוצר מספר בן 4 ספרות שונות באופן אקראי."""
    digits = list(range(10))  # רשימה של הספרות 0 עד 9
    random.shuffle(digits)  # ערבוב הספרות
    return digits[:4]  # החזרת 4 הספרות הראשונות

def get_user_guess():
    """קולט ניחוש מהמשתמש ומבטיח שהוא תקין (4 ספרות)."""
    while True:
        guess = input("נסה לנחש מספר בן 4 ספרות שונות: ")
        if len(guess) == 4 and guess.isdigit(): #בדיקה שאורך הקלט 4 והוא מכיל ספרות בלבד
           return guess
        else:
           print("קלט לא חוקי, הזן מספר עם 4 ספרות.")

def calculate_feedback(target, guess):
    """מחזיר את מספר הבייס והבול בהשוואה בין הניחוש למספר המטרה."""
    bases = 0  # מספר הספרות הנכונות במיקום הנכון
    balls = 0  # מספר הספרות הנכונות במיקום שגוי
    for i in range(4):
        if guess[i] == str(target[i]):
           bases +=1
        elif int(guess[i]) in target:
           balls += 1
    return bases, balls

def play_baseball():
    """פונקציית המשחק הראשית."""
    numberOfGuesses = 0 # אתחול מספר הניסיונות
    targetNumber = generate_target_number() # קבלת מספר רנדומלי
    print("בוא נשחק בייסבול!")
    while True:
        numberOfGuesses += 1  # הגדלת מונה הניסיונות
        userGuess = get_user_guess() # קבלת קלט מהמשתמש
        bases, balls = calculate_feedback(targetNumber, userGuess) # חישוב בייס ובול
        print(f"{bases} בייס, {balls} בול")
        if bases == 4:
            print(f"מזל טוב! ניצחת ב-{numberOfGuesses} ניסיונות") # ניצחון
            break

if __name__ == "__main__":
    play_baseball()
```
<הערות סיום>
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    -   `import random`: ייבוא המודול `random`, המשמש ליצירת רשימה אקראית של מספרים.
2.  **הגדרת הפונקציות**:
    -   `generate_target_number()`: פונקציה היוצרת מספר בן 4 ספרות ייחודיות באופן אקראי.
        -   הפונקציה מתחילה ביצירת רשימה של הספרות 0 עד 9.
        -   לאחר מכן, היא מערבבת את הספרות בצורה אקראית ומחזירה את 4 הספרות הראשונות כרשימה.
    -   `get_user_guess()`: פונקציה הקולטת את הניחוש מהמשתמש ומבטיחה שהוא תקין.
        -   הפונקציה משתמשת בלולאה אינסופית כדי לבקש מהמשתמש קלט עד שהוא מזין מחרוזת של 4 ספרות.
        -   הפונקציה בודקת שאורך הקלט הוא 4 והוא מכיל ספרות בלבד.
        -   אם הקלט תקין, הפונקציה מחזירה אותו.
    -   `calculate_feedback(target, guess)`: פונקציה המחשבת את כמות הבייס והבול בהשוואה בין ניחוש המשתמש למספר המטרה.
        -   הפונקציה מקבלת את רשימת הספרות של המספר המטרה ואת ניחוש המשתמש.
        -   הפונקציה סורקת את הספרות ומשווה בין המיקומים. אם יש התאמה בין ספרה ומיקום, הבייס גדל, אם יש התאמה רק בספרה הבול גדל.
        -   הפונקציה מחזירה את מספר הבייס והבול.
    -   `play_baseball()`: פונקציה המכילה את הלוגיקה של המשחק בייסבול.
        -   אתחול משתנים: מספר ניסיונות (`numberOfGuesses`) מאותחל ל-0, ומספר המטרה (`targetNumber`) נוצר באמצעות הפונקציה `generate_target_number()`.
        -   לולאת המשחק הראשית `while True`:
            -   בכל סיבוב, מספר הניסיונות גדל ב-1.
            -   הפונקציה `get_user_guess()` קוראת לקבל את הניחוש מהמשתמש.
            -   הפונקציה `calculate_feedback()` מחשבת את כמות הבייס והבול ומחזירה אותם.
            -   הפונקציה מדפיסה את הפידבק למשתמש.
            -   בדיקה האם מספר הבייס הוא 4, כלומר השחקן ניצח.
            -   במידה והשחקן ניצח, הפונקציה מדפיסה הודעת ניצחון, ויוצאת מהלולאה.
3.  **הפעלת המשחק**:
    -   `if __name__ == "__main__":`: בלוק זה מבטיח שהפונקציה `play_baseball()` תופעל רק אם הקובץ מופעל ישירות, ולא אם הוא מיובא כמודול.
    -   `play_baseball()`: קריאה לפונקציה להפעלת המשחק.
</הערות סיום>
