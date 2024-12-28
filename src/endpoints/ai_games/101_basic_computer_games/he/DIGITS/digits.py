"""
DIGITS:
=================
קושי: 2
-----------------
המשחק "דיגיטס" הוא משחק ניחושים בו המחשב בוחר מספר אקראי בין 100 ל-999, והשחקן מנסה לנחש את המספר הזה תוך כדי קבלת רמזים על מיקום הספרות הנכונות.
כל ניחוש מעובד על ידי המחשב, והוא מציין כמה ספרות השחקן ניחש נכונות ובאיזה מיקום.

חוקי המשחק:
1. המחשב בוחר מספר תלת-ספרתי אקראי (בין 100 ל-999).
2. השחקן מנסה לנחש את המספר הזה על ידי הזנת מספר תלת-ספרתי.
3. המחשב מגיב על ידי מתן רמזים: מספר הספרות שהשחקן ניחש נכונות, ובאיזה מיקום הם נמצאות.
4. המשחק נמשך עד שהשחקן מנחש את המספר המוגלה בצורה נכונה.
-----------------
אלגוריתם:
1. צור מספר אקראי תלת-ספרתי (בין 100 ל-999).
2. התחל לולאה:
   2.1. קבל קלט מהמשתמש (מספר תלת-ספרתי).
   2.2. בדוק אם הקלט תואם למספר האקראי. אם כן, הצג הודעת ניצחון וסיים את המשחק.
   2.3. אם הקלט לא תואם, ספר כמה ספרות נכונות יש במקום הנכון וכמה ספרות נכונות יש במקום לא נכון.
   2.4. הצג את הרמז לשחקן.
3. המשך בלולאה עד לניחוש נכון.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> GenerateTargetNumber["יצירת מספר אקראי תלת-ספרתי: <code><b>targetNumber</b></code>"]
    GenerateTargetNumber --> LoopStart{"תחילת לולאה"}
    LoopStart --> InputUserGuess["קבלת קלט מהמשתמש: <code><b>userGuess</b></code>"]
    InputUserGuess --> CheckGuess{"בדיקה: <code><b>userGuess == targetNumber?</b></code>"}
    CheckGuess -- כן --> OutputWin["הצגת הודעת ניצחון"]
    OutputWin --> End["סוף"]
    CheckGuess -- לא --> CountCorrectDigits["ספירת ספרות נכונות במקום נכון וספרות נכונות במקום לא נכון"]
    CountCorrectDigits --> OutputHint["הצגת רמז: מספר ספרות נכונות ובמקום נכון ובמקום לא נכון"]
    OutputHint --> LoopStart
```
Legenda:
    Start - התחלת המשחק.
    GenerateTargetNumber - יצירת מספר אקראי תלת-ספרתי ושמירתו במשתנה `targetNumber`.
    LoopStart - תחילת הלולאה, שתמשיך עד שהשחקן ינחש את המספר הנכון.
    InputUserGuess - קבלת קלט מהמשתמש (ניחוש מספר תלת-ספרתי) ושמירתו במשתנה `userGuess`.
    CheckGuess - בדיקה האם הניחוש שווה למספר המוגלה.
    OutputWin - הצגת הודעת ניצחון, אם הניחוש נכון.
    End - סיום המשחק.
    CountCorrectDigits - ספירת הספרות הנכונות במיקומן הנכון ובמיקום שגוי, ושמירה של המידע הזה.
    OutputHint - הצגת הרמז לשחקן על בסיס ספירת הספרות הנכונות.
"""
import random

# פונקציה ליצירת מספר אקראי תלת ספרתי
def generate_target_number():
    """
    יוצרת מספר אקראי תלת-ספרתי בין 100 ל-999.
    """
    return random.randint(100, 999)


# פונקציה להשוואת ספרות
def compare_digits(target, guess):
    """
    משווה את הספרות במספר המטרה ובניחוש המשתמש, ומחזירה את הרמזים.
    :param target: מספר המטרה (מספר תלת-ספרתי)
    :param guess: ניחוש המשתמש (מספר תלת-ספרתי)
    :return: מחזירה מחרוזת של רמזים.
    """
    target_str = str(target)
    guess_str = str(guess)
    correct_place = 0 # מספר ספרות במקום הנכון
    correct_digit = 0  # מספר ספרות נכונות במקום לא נכון

    # סופר ספרות במקום הנכון
    for i in range(3):
        if target_str[i] == guess_str[i]:
            correct_place += 1

    # סופר ספרות נכונות במקום שגוי
    for i in range(3):
        for j in range(3):
            if i != j and target_str[i] == guess_str[j]:
                correct_digit += 1

    return f"{correct_place} נכונים במקום, {correct_digit} נכונים במקום לא נכון."


# משחק הדיגיטס
def play_digits():
    """
    מנהל את משחק הדיגיטס.
    """
    target_number = generate_target_number()  # יוצר מספר מטרה אקראי
    print("אני חושב על מספר תלת-ספרתי. נסה לנחש אותו!")

    while True:
        try:
            user_guess = int(input("הזן ניחוש (מספר תלת-ספרתי): "))
        except ValueError:
            print("אנא הזן מספר תלת-ספרתי תקין.")
            continue

        if not 100 <= user_guess <= 999:
            print("אנא הזן מספר תלת-ספרתי תקין.")
            continue

        if user_guess == target_number:
            print("מזל טוב! ניחשת את המספר!")
            break
        else:
            hint = compare_digits(target_number, user_guess)
            print(hint)

# הפעלת המשחק
if __name__ == "__main__":
    play_digits()
"""
הסבר הקוד:
1.  **ייבוא מודול `random`**:
    -  `import random`: מייבא את המודול random, המאפשר יצירת מספרים אקראיים.
2.  **פונקציה `generate_target_number()`**:
    -   `def generate_target_number():`: מגדירה פונקציה שיוצרת מספר אקראי תלת ספרתי בין 100 ל-999.
    -  `return random.randint(100, 999)`:  מחזירה מספר שלם אקראי בתחום שצוין.
3.  **פונקציה `compare_digits(target, guess)`**:
    -   `def compare_digits(target, guess):`: מגדירה פונקציה המשווה בין המספר הנכון לבין ניחוש המשתמש.
    -   `target_str = str(target)` ו- `guess_str = str(guess)`: המרת המספרים למחרוזות לצורך גישה נוחה לספרות.
    -  `correct_place = 0` ו- `correct_digit = 0`: אתחול משתנים לספירת הספרות הנכונות במיקום הנכון ובמיקום השגוי.
    -  `for i in range(3):`: לולאה הסורקת את הספרות.
    -   `if target_str[i] == guess_str[i]:`: בדיקה אם הספרה במיקום הנוכחי זהה בשני המספרים.
    -  `correct_place += 1`: אם הספרה במקום הנכון - מוסיפים למונה.
    -   לולאה מקוננת: ספירת ספרות נכונות אך לא במקום הנכון.
    -  `return f"{correct_place} נכונים במקום, {correct_digit} נכונים במקום לא נכון."`: מחזירה את הרמז כטקסט.
4.  **פונקציה `play_digits()`**:
    -   `def play_digits():`: מגדירה את פונקציית המשחק.
    -   `target_number = generate_target_number()`: יצירת מספר אקראי על ידי קריאה לפונקציה המוגדרת.
    -  `print("אני חושב על מספר תלת-ספרתי. נסה לנחש אותו!")`: מדפיס הודעה למשתמש.
    -  `while True:`: לולאה אינסופית המאפשרת למשתמש לנחש עד שהוא מצליח.
    -  `try...except ValueError`: טיפול בשגיאות קלט אפשריות. אם המשתמש יזין משהו שאינו מספר שלם, תוצג הודעת שגיאה.
    -   `user_guess = int(input("הזן ניחוש (מספר תלת-ספרתי): "))`: קבלת ניחוש מהמשתמש והמרתו למספר שלם.
    -   `if not 100 <= user_guess <= 999:`: בדיקה שהקלט הוא מספר תלת-ספרתי חוקי.
    -   `if user_guess == target_number:`: בדיקה האם הניחוש שווה למספר המוגלה.
    -   `print("מזל טוב! ניחשת את המספר!")`: הצגת הודעת ניצחון.
    -   `break`: סיום הלולאה אם הניחוש נכון.
    -   `else:`: אם הניחוש שגוי.
    -   `hint = compare_digits(target_number, user_guess)`: יצירת רמז על ידי קריאה לפונקציה המוגדרת.
    -   `print(hint)`: הצגת הרמז למשתמש.
5. **הפעלת המשחק**:
    - `if __name__ == "__main__":`: בדיקה אם הסקריפט מורץ ישירות.
    -  `play_digits()`: קריאה לפונקציית המשחק להפעלתו.
"""
