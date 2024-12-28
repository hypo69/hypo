"""
<BULL>:
=================
קושי: 4
-----------------
במשחק "BULL" המחשב בוחר מספר בן ארבע ספרות כאשר כל ספרה שונה, והשחקן מנסה לנחש את המספר. לאחר כל ניחוש, המחשב מגיב בכמות ה-"BULLS" וה-"COWS". "BULL" מציין ספרה נכונה במקום נכון, ו-"COW" מציין ספרה נכונה במקום לא נכון.
המטרה היא לנחש את המספר עם כמה שפחות ניסיונות.

חוקי המשחק:
1. המחשב בוחר מספר בן 4 ספרות כאשר כל ספרה שונה (למשל 1234).
2. השחקן מנסה לנחש את המספר.
3. המחשב מגיב עם:
   - מספר ה-"BULLS" - מספר הספרות שניחשו נכון ובמיקום נכון.
   - מספר ה-"COWS" - מספר הספרות שניחשו נכון אך במיקום שגוי.
4. המשחק מסתיים כאשר השחקן מנחש את המספר.

-----------------
אלגוריתם:
1. הגדר פונקציה ליצירת מספר אקראי בן 4 ספרות שונות.
2. צור מספר אקראי בן 4 ספרות שונות (מספר המטרה).
3. אתחל את מספר הניסיונות ל-0.
4. התחל לולאה "כל עוד המספר לא נוחש":
  4.1 הגדל את מספר הניסיונות ב-1.
  4.2 קבל קלט מהמשתמש - מספר בן 4 ספרות.
  4.3 אם הקלט תקין:
    4.3.1  אפס את מונה ה-"BULLS" וה-"COWS".
    4.3.2  עבור על כל ספרה במספר המטרה ובמספר שהוזן.
    4.3.3  אם הספרות תואמות ובאותו מיקום, הגדל את מונה ה-"BULLS".
    4.3.4  אם הספרה שהוזנה נמצאת במספר המטרה אך לא באותו מיקום, הגדל את מונה ה-"COWS".
    4.3.5 אם מספר ה-"BULLS" הוא 4, עבור לשלב 5 (ניצחון).
    4.3.6 הצג את מספר ה-"BULLS" וה-"COWS" למשתמש.
  4.4 אם הקלט לא תקין, הצג הודעת שגיאה.
5. הצג הודעה "מזל טוב! ניצחת ב-X ניסיונות!"
6. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> GenerateTargetNumber["יצירת מספר מטרה אקראי עם 4 ספרות שונות"]
    GenerateTargetNumber --> InitializeGuesses["<code><b>numberOfGuesses = 0</b></code>"]
    InitializeGuesses --> LoopStart{"תחילת לולאה: כל עוד המספר לא נוחש"}
    LoopStart -- כן --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputGuess["קלט מספר מהמשתמש (4 ספרות)"]
    InputGuess --> ValidateInput{"בדיקה: קלט תקין (4 ספרות שונות)?"}
    ValidateInput -- כן --> InitializeCounters["<code><b>numberOfBulls = 0, numberOfCows = 0</b></code>"]
    InitializeCounters --> CheckDigits["לולאה: בדיקת ספרות"]
    CheckDigits --> CheckBulls{"בדיקה: ספרה נכונה ובמיקום נכון?"}
    CheckBulls -- כן --> IncreaseBulls["<code><b>numberOfBulls = numberOfBulls + 1</b></code>"]
    IncreaseBulls --> CheckCows{"בדיקה: ספרה נכונה אך לא במיקום?"}
    CheckCows -- כן --> IncreaseCows["<code><b>numberOfCows = numberOfCows + 1</b></code>"]
    IncreaseCows --> CheckDigitsLoop{"סוף לולאת ספרות"}
    CheckBulls -- לא --> CheckCows
    CheckCows -- לא --> CheckDigitsLoop
    CheckDigitsLoop --> CheckWin{"בדיקה: <code><b>numberOfBulls == 4?</b></code>"}
    CheckWin -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES!</b>"]
    OutputWin --> End["סוף"]
    CheckWin -- לא --> OutputResult["הצגת: <br><b>Bulls: <code>{numberOfBulls}</code>, Cows: <code>{numberOfCows}</code></b>"]
    OutputResult --> LoopStart
    ValidateInput -- לא --> OutputError["הצגת הודעת שגיאה: <br><b>קלט לא תקין!</b>"]
    OutputError --> LoopStart
    LoopStart -- לא --> End
```
Legenda:
    Start - התחלת המשחק.
    GenerateTargetNumber - יצירת מספר מטרה אקראי בן 4 ספרות שונות.
    InitializeGuesses - אתחול מונה הניסיונות לאפס.
    LoopStart - תחילת לולאה הממשיכה עד שהשחקן מנצח.
    IncreaseGuesses - הגדלת מספר הניסיונות ב-1.
    InputGuess - קבלת קלט מהמשתמש (מספר בן 4 ספרות).
    ValidateInput - בדיקה האם הקלט תקין (4 ספרות שונות).
    InitializeCounters - אתחול מונים של Bulls ו-Cows לאפס.
    CheckDigits - תחילת לולאה לבדיקת כל ספרה במספר.
    CheckBulls - בדיקה האם ספרה נכונה ובמיקום נכון.
    IncreaseBulls - הגדלת מונה ה-Bulls אם התנאי מתקיים.
    CheckCows - בדיקה האם ספרה נכונה אך לא במיקום נכון.
    IncreaseCows - הגדלת מונה ה-Cows אם התנאי מתקיים.
    CheckDigitsLoop - סוף הלולאה של בדיקת ספרות.
    CheckWin - בדיקה האם השחקן ניחש את כל הספרות (4 Bulls).
    OutputWin - הצגת הודעת ניצחון ומספר הניסיונות.
    End - סיום המשחק.
    OutputResult - הצגת כמות ה-Bulls וה-Cows.
    OutputError - הצגת הודעת שגיאה אם הקלט לא תקין.

"""
import random

def generate_target_number():
    """
    יוצר מספר אקראי בן 4 ספרות שונות.

    Returns:
        str: מספר אקראי בן 4 ספרות שונות כמחרוזת.
    """
    digits = list(range(10))  # רשימת ספרות מ-0 עד 9
    random.shuffle(digits)    # ערבוב רשימת הספרות
    # בחירת 4 הספרות הראשונות (למניעת מספר שמתחיל באפס)
    target_number = "".join(map(str, digits[1:4]))
    return str(digits[0]) + target_number  # המרת הספרות למחרוזת


def check_guess(target, guess):
    """
    בודק את הניחוש של המשתמש מול המספר המטרה ומחזיר את מספר ה-BULLS וה-COWS.

    Args:
        target (str): מספר המטרה.
        guess (str): הניחוש של המשתמש.

    Returns:
         tuple: (מספר ה-BULLS, מספר ה-COWS)
    """
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == target[i]:
            bulls += 1  # ספרה במקום הנכון
        elif guess[i] in target:
            cows += 1   # ספרה נכונה אבל לא במקום הנכון
    return bulls, cows


def is_valid_guess(guess):
    """
      בודק אם הקלט מהמשתמש תקין (4 ספרות שונות).
    
    Args:
        guess (str): הקלט מהמשתמש.
    
    Returns:
        bool: האם הקלט תקין
    """
    return len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4



# יצירת מספר המטרה
target_number = generate_target_number()
# אתחול מספר הניסיונות
number_of_guesses = 0

# לולאת משחק ראשית
while True:
    # הגדלת מספר הניסיונות
    number_of_guesses += 1
    # קבלת קלט מהמשתמש
    user_guess = input("נסה לנחש מספר בן 4 ספרות שונות: ")

    # בדיקת תקינות הקלט
    if not is_valid_guess(user_guess):
        print("קלט לא תקין! אנא הזן מספר בן 4 ספרות שונות.")
        continue

    # בדיקת הניחוש והצגת תוצאות
    bulls, cows = check_guess(target_number, user_guess)
    print(f"Bulls: {bulls}, Cows: {cows}")

    # בדיקה האם השחקן ניצח
    if bulls == 4:
        print(f"מזל טוב! ניצחת ב-{number_of_guesses} ניסיונות!")
        break # סיום המשחק אם הניחוש נכון

"""
הסבר הקוד:
1.  **ייבוא מודול `random`**:
    - `import random`: ייבוא המודול `random` ליצירת מספרים אקראיים.
2.  **פונקציה `generate_target_number()`**:
    - יוצרת מספר אקראי בן 4 ספרות שונות.
    - `digits = list(range(10))`: יוצרת רשימה של ספרות מ-0 עד 9.
    - `random.shuffle(digits)`: מערבבת את רשימת הספרות.
    - `target_number = "".join(map(str, digits[1:4]))`: יוצרת מחרוזת של 3 ספרות ראשונות מהרשימה המעורבבת, למניעת מצב שבו הספרה הראשונה היא 0.
    - `return str(digits[0]) + target_number`: מחזירה מחרוזת המורכבת מהספרה הראשונה ומ-3 הספרות הבאות.
3.  **פונקציה `check_guess(target, guess)`**:
    - בודקת את הניחוש של המשתמש מול המספר המטרה.
    - `bulls = 0`, `cows = 0`: אתחול מונה ה-BULLS וה-COWS.
    - לולאה על פני כל ספרה בניחוש ובמספר המטרה:
        - אם הספרות זהות ובאותו מיקום, מעדכנים את `bulls`.
        - אם הספרה מופיעה במספר המטרה, מעדכנים את `cows`.
    - `return bulls, cows`: מחזירה את מספר ה-BULLS וה-COWS.
4. **פונקציה `is_valid_guess(guess)`**:
    - מקבלת מחרוזת קלט מהמשתמש.
    - בודקת אם המחרוזת באורך 4.
    - בודקת אם כל התווים הם ספרות.
    - בודקת אם אין ספרות חוזרות.
    - מחזירה True אם כל התנאים מתקיימים, אחרת False.
5.  **משתנים ראשיים**:
    - `target_number = generate_target_number()`: קריאה לפונקציה ליצירת מספר המטרה.
    - `number_of_guesses = 0`: אתחול מונה הניסיונות.
6.  **לולאת המשחק `while True:`**:
    - לולאה אינסופית שמתמשכת עד שהמשתמש מנצח.
    - `number_of_guesses += 1`: הגדלת מונה הניסיונות בכל ניסיון.
    - `user_guess = input("נסה לנחש מספר בן 4 ספרות שונות: ")`: קבלת ניחוש מהמשתמש.
    - `if not is_valid_guess(user_guess):`: בדיקה אם הקלט תקין.
    - `bulls, cows = check_guess(target_number, user_guess)`: קריאה לפונקציה לבדיקת הניחוש.
    - הדפסת תוצאות ה-BULLS וה-COWS.
    - `if bulls == 4:`: בדיקה האם המשתמש ניצח.
    - הדפסת הודעת ניצחון ומספר הניסיונות, ויציאה מהלולאה.
"""
