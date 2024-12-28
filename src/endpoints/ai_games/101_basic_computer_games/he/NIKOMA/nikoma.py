"""
BAGELS:
=================
קושי: 5
-----------------
המשחק "בייגלס" הוא משחק לוגי בו השחקן מנסה לנחש מספר בן שלוש ספרות, כאשר כל ספרה היא שונה (ללא כפילויות). 
לאחר כל ניחוש, המחשב מספק רמזים: "Pico" אם ספרה אחת נכונה אבל לא במיקום הנכון, "Fermi" אם ספרה אחת נכונה ובמיקום הנכון, ו-"Bagels" אם אף ספרה לא נכונה. השחקן מנצח כאשר הוא מנחש נכון את כל שלוש הספרות במיקום הנכון.

חוקי המשחק:
1. המחשב בוחר מספר אקראי בן שלוש ספרות, כאשר כל הספרות שונות.
2. השחקן מזין ניחוש של מספר בן שלוש ספרות, עם ספרות שונות.
3. המחשב מספק רמזים בהתאם לניחוש:
    - "Fermi": ספרה אחת נכונה ובמיקום הנכון.
    - "Pico": ספרה אחת נכונה אבל לא במיקום הנכון.
    - "Bagels": אף ספרה לא נכונה.
4. השחקן ממשיך לנחש עד שהוא מנחש נכונה את המספר או עד שהוא מבצע מספר מוגבל של ניחושים.
-----------------
אלגוריתם:
1. צור מספר אקראי בן שלוש ספרות, כאשר כל ספרה שונה (ספרת מאות שונה מ-0).
2. הגדר את מספר הניסיונות המרבי.
3. התחל לולאה "כל עוד מספר הניסיונות לא עבר את המקסימום":
   3.1 בקש מהשחקן להזין ניחוש.
   3.2 אם הניחוש שווה למספר המוגרל, הצג הודעת ניצחון וסיים את המשחק.
   3.3 עבור כל ספרה בניחוש:
        3.3.1 אם הספרה נמצאת במספר המוגרל ובמיקום הנכון, הוסף "Fermi" לרמזים.
        3.3.2 אם הספרה נמצאת במספר המוגרל אך לא במיקום הנכון, הוסף "Pico" לרמזים.
   3.4 אם אין רמזים, הצג "Bagels".
   3.5 הצג את הרמזים.
4. אם מספר הניסיונות עבר את המקסימום, הצג הודעת הפסד וסיים את המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים: <br><code><b>targetNumber = random_3_digit_unique()<br>maxGuesses = 10<br>currentGuess = 0</b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: <code><b>currentGuess < maxGuesses</b></code>"}
    LoopStart -- כן --> InputGuess["קלט ניחוש מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> CheckGuess{"בדיקה: <code><b>userGuess == targetNumber</b></code>?"}
    CheckGuess -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT!</b>"]
    OutputWin --> End["סוף"]
    CheckGuess -- לא --> InitializeHints["<code><b>hints = ""</b></code>"]
    InitializeHints --> LoopDigits{"לולאה: עבור כל ספרה ב<code><b>userGuess</b></code>"}
    LoopDigits --> CheckFermi{"בדיקה: ספרה במיקום הנכון? "}
    CheckFermi -- כן --> AddFermi["<code><b>hints += 'Fermi'</b></code>"]
    AddFermi --> LoopDigitsNext
    CheckFermi -- לא --> CheckPico{"בדיקה: ספרה קיימת אבל לא במיקום הנכון? "}
    CheckPico -- כן --> AddPico["<code><b>hints += 'Pico'</b></code>"]
    AddPico --> LoopDigitsNext
    CheckPico -- לא --> LoopDigitsNext
    LoopDigitsNext --> LoopDigitsEnd{"סוף לולאה: עבור כל ספרה ב<code><b>userGuess</b></code>"}
    LoopDigitsEnd --> CheckHints{"בדיקה: <code><b>hints == ""</b></code>?"}
    CheckHints -- כן --> OutputBagels["הצגת הודעה: <b>Bagels</b>"]
    OutputBagels --> OutputHints
    CheckHints -- לא --> OutputHints["הצגת רמזים: <code><b>hints</b></code>"]
    OutputHints --> IncreaseGuesses["<code><b>currentGuess += 1</b></code>"]
    IncreaseGuesses --> LoopStart
    LoopStart -- לא --> OutputLose["הצגת הודעה: <b>YOU LOSE, number was {targetNumber}</b>"]
    OutputLose --> End
```
Legenda:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: targetNumber (המספר המוגלה) נוצר באקראי, maxGuesses (מספר הניסיונות המרבי) מוגדר ל-10, ו-currentGuess (מספר הניסיונות הנוכחי) מאותחל ל-0.
    LoopStart - תחילת הלולאה, הממשיכה כל עוד מספר הניסיונות הנוכחי קטן ממספר הניסיונות המרבי.
    InputGuess - קלט ניחוש מהמשתמש ושמירתו במשתנה userGuess.
    CheckGuess - בדיקה האם הניחוש שווה למספר המוגלה.
    OutputWin - הצגת הודעת ניצחון אם הניחוש נכון.
    End - סוף התוכנית.
    InitializeHints - אתחול משתנה hints (רמזים) למחרוזת ריקה.
    LoopDigits - תחילת לולאה עבור כל ספרה בניחוש.
    CheckFermi - בדיקה אם הספרה נמצאת במספר המוגלה ובמיקום הנכון.
    AddFermi - הוספת הרמז "Fermi" למשתנה hints.
    CheckPico - בדיקה אם הספרה נמצאת במספר המוגלה אך לא במיקום הנכון.
    AddPico - הוספת הרמז "Pico" למשתנה hints.
    LoopDigitsNext - מעבר לספרה הבאה.
    LoopDigitsEnd - סוף הלולאה עבור כל ספרה בניחוש.
    CheckHints - בדיקה אם אין רמזים.
    OutputBagels - הצגת ההודעה "Bagels" אם אין רמזים.
    OutputHints - הצגת הרמזים.
    IncreaseGuesses - הגדלת מונה הניסיונות הנוכחי ב-1.
    OutputLose - הצגת הודעת הפסד וגילוי המספר המוגלה אם מספר הניסיונות המרבי הגיע.
"""
import random

def generate_unique_3_digit_number():
    """יצירת מספר אקראי בעל 3 ספרות שונות."""
    digits = list(range(10))
    random.shuffle(digits)
    # וודא שספרת המאות אינה 0
    while digits[0] == 0:
      random.shuffle(digits)
    return str(digits[0]) + str(digits[1]) + str(digits[2])

def get_hints(secret_number, guess):
    """הפקת רמזים עבור הניחוש."""
    hints = ""
    for i, digit in enumerate(guess):
        if digit == secret_number[i]:
            hints += "Fermi " # ספרה במקום הנכון
        elif digit in secret_number:
            hints += "Pico " # ספרה קיימת אך לא במיקום הנכון
    if not hints:
        hints = "Bagels" # אף ספרה לא קיימת
    return hints.strip() # הסרת רווחים מיותרים

def play_bagels():
    """משחק בייגלס."""
    target_number = generate_unique_3_digit_number() # יצירת מספר סודי אקראי
    max_guesses = 10
    current_guess = 0

    print("נסה לנחש מספר בן 3 ספרות שונות.")

    while current_guess < max_guesses:
        user_guess = input(f"ניסיון {current_guess + 1}: ")

        if user_guess == target_number:
          print("מזל טוב! ניצחת!")
          return  # סיום המשחק אם המספר נוחש

        hints = get_hints(target_number, user_guess) # קבלת רמזים
        print("רמזים:", hints)

        current_guess += 1 # הגדלת מספר הניסיונות

    print(f"הפסדת! המספר היה: {target_number}")

if __name__ == "__main__":
    play_bagels()

"""
הסבר הקוד:
1. **ייבוא מודול `random`**:
   - `import random`: מייבא את המודול ליצירת מספרים אקראיים.
2. **פונקציה `generate_unique_3_digit_number()`**:
   - יוצרת מספר בן 3 ספרות שונות באקראי.
   -  `digits = list(range(10))`: יוצרת רשימה של הספרות 0 עד 9.
   - `random.shuffle(digits)`: מערבבת את הספרות באקראי.
   - `while digits[0] == 0`: מוודא שהספרה הראשונה (ספרת המאות) אינה 0.
   - `return str(digits[0]) + str(digits[1]) + str(digits[2])`: מחזירה את המספר כמחרוזת.
3. **פונקציה `get_hints(secret_number, guess)`**:
   - מקבלת את המספר הסודי ואת הניחוש ומחזירה רמזים בהתאם.
    - `hints = ""`: אתחול מחרוזת ריקה לרמזים.
    - `for i, digit in enumerate(guess)`: לולאה שעוברת על כל ספרה בניחוש יחד עם האינדקס שלה.
    - `if digit == secret_number[i]`: אם הספרה נמצאת במקום הנכון, מוסיפה "Fermi" לרמזים.
    - `elif digit in secret_number`: אם הספרה קיימת אך לא במקום הנכון, מוסיפה "Pico" לרמזים.
    - `if not hints`: אם אף רמז לא נוצר (כלומר אף ספרה לא נכונה), מגדירה את הרמז ל-"Bagels".
    - `return hints.strip()`: מחזירה את הרמזים לאחר הסרת רווחים מיותרים.
4. **פונקציה `play_bagels()`**:
    - מפעילה את המשחק "בייגלס".
    - `target_number = generate_unique_3_digit_number()`: יצירת המספר הסודי.
    - `max_guesses = 10`: הגדרת מספר הניסיונות המרבי.
    - `current_guess = 0`: אתחול מונה הניסיונות.
    - `print("נסה לנחש מספר בן 3 ספרות שונות.")`: הצגת הודעת פתיחה.
    - `while current_guess < max_guesses`: לולאה שרצה עד שנגמרים הניסיונות או שהמספר נוחש.
    - `user_guess = input(f"ניסיון {current_guess + 1}: ")`: קבלת ניחוש מהמשתמש.
    - `if user_guess == target_number`: אם הניחוש נכון, המשחק מסתיים בניצחון.
    - `hints = get_hints(target_number, user_guess)`: קבלת רמזים לניחוש.
    - `print("רמזים:", hints)`: הצגת הרמזים.
    - `current_guess += 1`: הגדלת מונה הניסיונות.
    - `print(f"הפסדת! המספר היה: {target_number}")`: אם הלולאה הסתיימה בלי ניצחון, מודפסת הודעת הפסד עם המספר הסודי.
5.  **הפעלת המשחק**:
    -  `if __name__ == "__main__":`: בלוק זה מבטיח שהפונקציה `play_bagels()` תופעל רק אם הקובץ מופעל ישירות, ולא אם הוא מיובא כמודול.
    -  `play_bagels()`: קריאה לפונקציה להפעלת המשחק.
"""
