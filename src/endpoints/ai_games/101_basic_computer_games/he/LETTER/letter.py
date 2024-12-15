
BAGELS:
=================
קושי: 5
-----------------
המשחק "בייגלס" הוא משחק לוגי בו המחשב בוחר מספר תלת-ספרתי ייחודי, והשחקן צריך לנחש אותו. לאחר כל ניסיון, המחשב מספק רמזים: "Pico" אם ספרה נכונה מופיעה במיקום שגוי, "Fermi" אם ספרה נכונה מופיעה במיקום הנכון, ו"Bagels" אם אף ספרה אינה נכונה. המטרה היא לנחש את המספר בכמה שפחות ניסיונות.

חוקי המשחק:
1. המחשב בוחר מספר תלת-ספרתי ייחודי (ללא ספרות חוזרות).
2. השחקן מזין ניחוש תלת-ספרתי.
3. לאחר כל ניחוש, המחשב מספק רמזים:
   - "Fermi": אם ספרה נכונה נמצאת במיקום הנכון.
   - "Pico": אם ספרה נכונה נמצאת במיקום שגוי.
   - "Bagels": אם אף ספרה אינה נכונה.
4. הרמזים מוצגים לפי הסדר (קודם "Fermi", לאחר מכן "Pico").
5. המשחק נמשך עד שהשחקן מנחש את המספר הנכון.
-----------------
אלגוריתם:
1. צור מספר תלת-ספרתי אקראי וייחודי (ללא ספרות חוזרות).
2. התחל לולאה "כל עוד המספר לא נוחש":
   2.1. קבל קלט מהמשתמש - ניחוש תלת-ספרתי.
   2.2. אתחל משתנה לרמזים - ריק.
   2.3. עבור על כל ספרה בניחוש:
      2.3.1 אם הספרה נמצאת במיקום הנכון במספר המקורי, הוסף "Fermi" לרמזים.
      2.3.2 אם הספרה נמצאת במספר המקורי אך במיקום שגוי, הוסף "Pico" לרמזים.
   2.4. אם אין רמזים, הצג "Bagels".
   2.5. הצג את הרמזים.
   2.6. אם הניחוש נכון, צא מהלולאה.
3. הצג הודעת ניצחון.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> GenerateSecretNumber["<p align='left'>יצירת מספר סודי תלת-ספרתי ייחודי:
    <code><b>secretNumber</b></code></p>"]
    GenerateSecretNumber --> LoopStart{"תחילת לולאה: כל עוד לא נוחש"}
    LoopStart -- כן --> InputGuess["קלט ניחוש תלת-ספרתי: <code><b>userGuess</b></code>"]
    InputGuess --> InitializeClues["<p align='left'>אתחול רמזים:
    <code><b>clues = ""</b></code></p>"]
    InitializeClues --> CheckEachDigit{"לולאה: עבור כל ספרה ב <code><b>userGuess</b></code>"}
    CheckEachDigit --> CheckFermi{"בדיקה: ספרה במיקום הנכון ב<code><b>secretNumber</b></code>?"}
    CheckFermi -- כן --> AddFermi["<code><b>clues += 'Fermi '</b></code>"]
    AddFermi --> CheckPico{"בדיקה: ספרה קיימת ב<code><b>secretNumber</b></code> אך במיקום שגוי?"}
    CheckFermi -- לא --> CheckPico
    CheckPico -- כן --> AddPico["<code><b>clues += 'Pico '</b></code>"]
    AddPico --> NextDigit{"ספרה הבאה"}
    CheckPico -- לא --> NextDigit
    NextDigit -- יש עוד ספרות --> CheckEachDigit
    NextDigit -- אין עוד ספרות --> CheckBagels{"בדיקה: <code><b>clues</b></code> ריק?"}
    CheckBagels -- כן --> OutputBagels["הצגת הודעה: <b>Bagels</b>"]
    OutputBagels --> OutputClues
    CheckBagels -- לא --> OutputClues["הצגת רמזים: <code><b>clues</b></code>"]
    OutputClues --> CheckWin{"בדיקה: <code><b>userGuess == secretNumber</b></code>?"}
    CheckWin -- כן --> OutputWin["הצגת הודעה: <b>ניצחת!</b>"]
    OutputWin --> End["סוף"]
    CheckWin -- לא --> LoopStart
     LoopStart -- לא --> End
```

Legenda:
    Start - התחלת התוכנית.
    GenerateSecretNumber - יצירת מספר סודי תלת-ספרתי ייחודי (ללא ספרות חוזרות) ושמירתו במשתנה `secretNumber`.
    LoopStart - תחילת הלולאה, הממשיכה כל עוד המספר הסודי לא נוחש.
    InputGuess - קבלת קלט מהמשתמש - ניחוש תלת-ספרתי ושמירתו במשתנה `userGuess`.
    InitializeClues - אתחול משתנה הרמזים (`clues`) למחרוזת ריקה.
    CheckEachDigit - תחילת לולאה העוברת על כל ספרה בניחוש המשתמש.
    CheckFermi - בדיקה האם הספרה הנוכחית בניחוש נמצאת במיקום הנכון במספר הסודי.
    AddFermi - הוספת "Fermi " למחרוזת הרמזים.
    CheckPico - בדיקה האם הספרה הנוכחית בניחוש קיימת במספר הסודי אך במיקום שגוי.
    AddPico - הוספת "Pico " למחרוזת הרמזים.
    NextDigit - מעבר לספרה הבאה בלולאה או המשך התהליך אם אין יותר ספרות.
    CheckBagels - בדיקה האם מחרוזת הרמזים ריקה (לא נמצאו רמזים).
    OutputBagels - הצגת הודעה "Bagels" אם לא נמצאו רמזים.
    OutputClues - הצגת מחרוזת הרמזים.
    CheckWin - בדיקה האם הניחוש של המשתמש שווה למספר הסודי.
    OutputWin - הצגת הודעת ניצחון אם הניחוש נכון.
    End - סיום התוכנית.
```
```python
import random

def generate_secret_number():
    """
    יוצר מספר סודי תלת-ספרתי ייחודי.

    Returns:
        str: מחרוזת המייצגת את המספר הסודי.
    """
    # יצירת רשימה של ספרות מ-0 עד 9
    digits = list(range(10))
    # בחירת ספרה ראשונה שאינה 0
    first_digit = random.choice(digits[1:])
    digits.remove(first_digit)
    # בחירת שתי ספרות נוספות באופן אקראי
    second_digit = random.choice(digits)
    digits.remove(second_digit)
    third_digit = random.choice(digits)

    # החזרת המספר כמחרוזת
    return str(first_digit) + str(second_digit) + str(third_digit)

def get_clues(secret_number, user_guess):
    """
    מייצר רמזים עבור הניחוש של המשתמש.

    Args:
        secret_number (str): המספר הסודי.
        user_guess (str): הניחוש של המשתמש.

    Returns:
        str: מחרוזת המכילה את הרמזים.
    """
    clues = ""
    # בדיקה עבור כל ספרה בניחוש
    for i in range(3):
        if user_guess[i] == secret_number[i]:
            # אם הספרה נמצאת במיקום הנכון, הוסף "Fermi"
            clues += "Fermi "
        elif user_guess[i] in secret_number:
            # אם הספרה קיימת במספר הסודי אך במיקום שגוי, הוסף "Pico"
            clues += "Pico "

    # אם אין רמזים, החזר "Bagels"
    if not clues:
        return "Bagels"
    return clues

def play_bagels():
    """
     מגדיר את המשחק בייגלס.
    """
    # יצירת מספר סודי
    secret_number = generate_secret_number()
    print("בחרתי מספר תלת-ספרתי. נסה לנחש אותו.")

    # לולאת המשחק
    while True:
        # קלט מהמשתמש
        user_guess = input("הכנס ניחוש: ")
        # בדיקה שהקלט הוא מספר תלת ספרתי
        if not user_guess.isdigit() or len(user_guess) != 3:
          print("הניחוש חייב להיות מספר תלת ספרתי. נסה שוב.")
          continue

        # יצירת רמזים
        clues = get_clues(secret_number, user_guess)
        print(clues)

        # בדיקה אם הניחוש נכון
        if user_guess == secret_number:
            print("ניצחת!")
            break

if __name__ == "__main__":
    play_bagels()
"""
הסבר הקוד:
1.  **ייבוא מודול `random`**:
    -   `import random`: מייבא את המודול `random`, המשמש ליצירת מספרים אקראיים.

2.  **פונקציה `generate_secret_number()`**:
    -   פונקציה זו יוצרת מספר סודי תלת-ספרתי ייחודי, ללא ספרות חוזרות.
    -   `digits = list(range(10))`: יוצרת רשימה של ספרות מ-0 עד 9.
    -   `first_digit = random.choice(digits[1:])`: בוחרת ספרה ראשונה באופן אקראי מתוך הספרות שאינן 0.
    -   `digits.remove(first_digit)`: מסירה את הספרה הראשונה מהרשימה כדי שלא תופיע שוב.
    -   `second_digit = random.choice(digits)`: בוחרת ספרה שנייה באופן אקראי.
    -   `digits.remove(second_digit)`: מסירה את הספרה השנייה מהרשימה.
    -   `third_digit = random.choice(digits)`: בוחרת ספרה שלישית באופן אקראי.
    -   `return str(first_digit) + str(second_digit) + str(third_digit)`: מחזירה את המספר הסודי כמחרוזת.

3.  **פונקציה `get_clues(secret_number, user_guess)`**:
    -   פונקציה זו מקבלת את המספר הסודי ואת הניחוש של המשתמש, ומחזירה רמזים.
    -   `clues = ""`: מאתחלת מחרוזת ריקה לרמזים.
    -   `for i in range(3):`: לולאה העוברת על כל ספרה בניחוש.
        -   `if user_guess[i] == secret_number[i]`: אם הספרה במיקום הנכון, מוסיפה "Fermi " לרמזים.
        -   `elif user_guess[i] in secret_number`: אם הספרה קיימת במספר הסודי אך במיקום אחר, מוסיפה "Pico " לרמזים.
    -   `if not clues:`: אם אין רמזים (המחרוזת ריקה), מחזירה "Bagels".
    -   `return clues`: מחזירה את הרמזים.

4.  **פונקציה `play_bagels()`**:
    -   מגדירה את המשחק בייגלס.
    -   `secret_number = generate_secret_number()`: יוצרת את המספר הסודי באמצעות הפונקציה `generate_secret_number()`.
    -   `print("בחרתי מספר תלת-ספרתי. נסה לנחש אותו.")`: מדפיסה הודעה למשתמש.
    -   `while True:`: לולאה אינסופית, המאפשרת למשתמש לנחש שוב ושוב עד שמנצח.
    -   `user_guess = input("הכנס ניחוש: ")`: מבקשת קלט מהמשתמש.
    -  `if not user_guess.isdigit() or len(user_guess) != 3:`, בודקת שהקלט מהמשתמש הוא מספר תלת ספרתי. אם לא, מבקשת קלט חדש.
    -   `clues = get_clues(secret_number, user_guess)`: מקבלת רמזים מהפונקציה `get_clues()`.
    -   `print(clues)`: מדפיסה את הרמזים.
    -   `if user_guess == secret_number:`: אם הניחוש נכון, מדפיסה הודעת ניצחון ויוצאת מהלולאה.
    -   `break`: יוצאת מהלולאה אם המשתמש ניצח.

5.  `if __name__ == "__main__":`: בלוק זה מבטיח שהפונקציה `play_bagels()` תופעל רק אם הקובץ מופעל ישירות ולא אם הוא מיובא כמודול.
"""
```