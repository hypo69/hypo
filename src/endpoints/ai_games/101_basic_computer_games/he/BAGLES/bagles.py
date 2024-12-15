<BAGLES>:
=================
קושי: 4
-----------------
המשחק "בייגלס" הוא משחק ניחושים בו המחשב בוחר מספר סודי בעל 3 ספרות, כאשר כל ספרה שונה, והשחקן מנסה לנחש את המספר הזה על ידי מתן ניחושים. המחשב מספק רמזים לאחר כל ניחוש: "PICO" אם ספרה קיימת במספר הסודי אך לא במקום הנכון, "FERMI" אם ספרה קיימת במספר הסודי ובמקום הנכון, ו-"BAGELS" אם אף ספרה לא קיימת במספר הסודי. המטרה היא לנחש את המספר הסודי תוך מספר מינימלי של ניסיונות.

חוקי המשחק:
1. המחשב בוחר מספר סודי בן 3 ספרות שונות.
2. השחקן מנסה לנחש את המספר.
3. לאחר כל ניחוש, המחשב מספק רמזים:
   - "FERMI" עבור כל ספרה שנמצאת במספר הסודי ובמקום הנכון.
   - "PICO" עבור כל ספרה שנמצאת במספר הסודי אך לא במקום הנכון.
   - "BAGELS" אם אף ספרה לא נמצאת במספר הסודי.
4. המשחק נמשך עד שהשחקן מנחש נכון את המספר הסודי.
-----------------
אלגוריתם:
1. הגדר את מספר הספרות במספר הסודי ל-3.
2. צור מספר סודי בן 3 ספרות שונות באופן אקראי.
3. אתחל את מספר הניחושים ל-0.
4. התחל לולאה "כל עוד המספר לא נוחש":
   4.1 הגדל את מספר הניחושים ב-1.
   4.2 בקש מהשחקן להזין ניחוש בן 3 ספרות.
   4.3 אם הניחוש תואם למספר הסודי, עבור לשלב 5.
   4.4 אתחל מחרוזת רמזים ריקה.
   4.5 עבור על כל ספרה בניחוש:
        4.5.1 אם הספרה קיימת במספר הסודי ובמקום הנכון, הוסף "FERMI" למחרוזת הרמזים.
        4.5.2 אם הספרה קיימת במספר הסודי אך לא במקום הנכון, הוסף "PICO" למחרוזת הרמזים.
   4.6 אם מחרוזת הרמזים ריקה, הוסף "BAGELS".
   4.7 הצג את מחרוזת הרמזים.
5. הצג הודעה "YOU GOT IT IN {מספר ניסיונות} GUESSES!"
6. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:<br><code><b>
    numberOfDigits = 3<br>
    secretNumber = generateSecretNumber(numberOfDigits)<br>
    numberOfGuesses = 0<br>
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: כל עוד לא נוחש"}
    LoopStart -- כן --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputGuess["קלט ניחוש מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> CheckGuess{"בדיקה: <code><b>userGuess == secretNumber?</b></code>"}
    CheckGuess -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES!</b>"]
    OutputWin --> End["סוף"]
    CheckGuess -- לא --> InitializeClues["<code><b>clues = \"\"</b></code>"]
    InitializeClues --> LoopDigitsStart{"תחילת לולאת ספרות"}
    LoopDigitsStart --> CheckDigitFermi{"בדיקה: <code><b>userGuess[i] == secretNumber[i]?</b></code>"}
    CheckDigitFermi -- כן --> AddFermi["<code><b>clues = clues + \"FERMI\"</b></code>"]
    AddFermi --> LoopDigitsEnd["סוף לולאת ספרות"]
    CheckDigitFermi -- לא --> CheckDigitPico{"בדיקה: <code><b>userGuess[i] in secretNumber?</b></code>"}
    CheckDigitPico -- כן --> AddPico["<code><b>clues = clues + \"PICO\"</b></code>"]
    AddPico --> LoopDigitsEnd
    CheckDigitPico -- לא --> LoopDigitsEnd
    LoopDigitsEnd --> LoopDigitsNext{"ספרה הבאה?"}
    LoopDigitsNext -- כן --> LoopDigitsStart
    LoopDigitsNext -- לא --> CheckCluesEmpty{"בדיקה: <code><b>clues == \"\"?</b></code>"}
    CheckCluesEmpty -- כן --> AddBagels["<code><b>clues = \"BAGELS\"</b></code>"]
    AddBagels --> OutputClues["הצגת רמזים: <code><b>clues</b></code>"]
    CheckCluesEmpty -- לא --> OutputClues
     OutputClues --> LoopStart
    LoopStart -- לא --> End
```
Legenda:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: numberOfDigits (מספר הספרות) מאותחל ל-3, secretNumber (המספר הסודי) נוצר אקראית עם ספרות שונות, numberOfGuesses (מספר הניסיונות) מאותחל ל-0.
    LoopStart - תחילת הלולאה, הממשיכה כל עוד המספר לא נוחש.
    IncreaseGuesses - הגדלת מונה הניסיונות ב-1.
    InputGuess - קלט ניחוש מהמשתמש ושמירתו במשתנה userGuess.
    CheckGuess - בדיקה האם הניחוש שווה למספר הסודי.
    OutputWin - הצגת הודעת ניצחון, אם המספר נוחש, עם מספר הניסיונות.
    End - סוף התוכנית.
    InitializeClues - אתחול מחרוזת הרמזים למחרוזת ריקה.
    LoopDigitsStart - תחילת לולאת הספרות, בדיקת כל ספרה בניחוש.
    CheckDigitFermi - בדיקה האם הספרה נמצאת במקום הנכון.
    AddFermi - הוספת "FERMI" למחרוזת הרמזים.
    CheckDigitPico - בדיקה האם הספרה נמצאת במספר הסודי אך לא במקום הנכון.
    AddPico - הוספת "PICO" למחרוזת הרמזים.
    LoopDigitsEnd - סוף לולאת הספרות.
    LoopDigitsNext - בדיקה האם יש ספרות נוספות ללולאה.
    CheckCluesEmpty - בדיקה האם מחרוזת הרמזים ריקה.
    AddBagels - הוספת "BAGELS" למחרוזת הרמזים.
    OutputClues - הצגת הרמזים.
    
"""
import random

def generate_secret_number(num_digits):
    """
    פונקציה ליצירת מספר סודי אקראי עם ספרות שונות.
    Args:
        num_digits: מספר הספרות במספר הסודי.
    Returns:
        מחרוזת המכילה את המספר הסודי.
    """
    digits = list(range(10)) # יצירת רשימה של ספרות מ-0 עד 9
    random.shuffle(digits) # ערבוב הספרות
    secret_number = "".join(map(str, digits[:num_digits])) # בחירת num_digits ספרות ראשונות והמרתן למחרוזת
    return secret_number # החזרת המספר הסודי כמחרוזת


def get_clues(user_guess, secret_number):
    """
    פונקציה ליצירת רמזים עבור הניחוש של המשתמש.
    Args:
        user_guess: הניחוש של המשתמש.
        secret_number: המספר הסודי.
    Returns:
        מחרוזת המכילה את הרמזים.
    """
    clues = "" # אתחול מחרוזת הרמזים
    for i, digit in enumerate(user_guess): # מעבר על כל ספרה בניחוש של המשתמש
        if digit == secret_number[i]: # בדיקה האם הספרה קיימת ובמקום הנכון
            clues += "FERMI " # הוספת רמז "FERMI"
        elif digit in secret_number: # בדיקה האם הספרה קיימת במספר הסודי, אך לא במקום הנכון
            clues += "PICO " # הוספת רמז "PICO"
    if not clues: # אם מחרוזת הרמזים ריקה, כלומר לא נמצאו התאמות
        clues = "BAGELS"  # הוספת רמז "BAGELS"
    return clues # החזרת מחרוזת הרמזים

def play_bagels_game():
    """
    פונקציה המנהלת את משחק ה"בייגלס".
    """
    numberOfDigits = 3 # מספר הספרות במספר הסודי
    secretNumber = generate_secret_number(numberOfDigits) # יצירת מספר סודי אקראי עם ספרות שונות
    numberOfGuesses = 0 # אתחול מונה הניסיונות
    print("אני חושב על מספר בן 3 ספרות שונות. נסה לנחש אותו.")
    while True: # לולאת משחק ראשית, ממשיכה עד שהמשתמש מנחש נכון
        numberOfGuesses += 1 # הגדלת מונה הניסיונות
        userGuess = input(f"ניסיון {numberOfGuesses}: הזן ניחוש בן {numberOfDigits} ספרות: ")
         # קלט ניחוש מהמשתמש
        if not userGuess.isdigit() or len(userGuess) != numberOfDigits:
            print(f"אנא הזן מספר בן {numberOfDigits} ספרות.")
            continue

        if userGuess == secretNumber: # בדיקה האם הניחוש נכון
            print(f"מזל טוב! ניחשת את המספר ב-{numberOfGuesses} ניסיונות!") # הודעה על ניצחון
            break # סיום הלולאה והמשחק
        else: # אם הניחוש לא נכון
            clues = get_clues(userGuess, secretNumber) # קבלת רמזים
            print("רמזים: ", clues) # הצגת הרמזים למשתמש

if __name__ == "__main__":
    play_bagels_game() # הפעלת המשחק רק כאשר הקובץ מופעל ישירות

"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    - `import random`: ייבוא מודול `random`, המשמש ליצירת מספרים אקראיים.
2. **הגדרת הפונקציה `generate_secret_number(num_digits)`**:
    - `def generate_secret_number(num_digits):`: פונקציה זו מקבלת את מספר הספרות הרצוי למספר הסודי.
    - `digits = list(range(10))`: יצירת רשימה של ספרות מ-0 עד 9.
    - `random.shuffle(digits)`: ערבוב רשימת הספרות באופן אקראי.
    - `secret_number = "".join(map(str, digits[:num_digits]))`: בחירת מספר הספרות הרצוי מהרשימה המעורבבת והמרתן למחרוזת.
    - `return secret_number`: החזרת המספר הסודי כמחרוזת.
3.  **הגדרת הפונקציה `get_clues(user_guess, secret_number)`**:
    - `def get_clues(user_guess, secret_number):`: פונקציה זו מקבלת את הניחוש של המשתמש ואת המספר הסודי.
    - `clues = ""`: אתחול מחרוזת ריקה שתכיל את הרמזים.
    - לולאת `for` עם `enumerate`: מעבר על כל ספרה בניחוש של המשתמש תוך שמירת האינדקס של הספרה.
        - `if digit == secret_number[i]:`: בדיקה האם הספרה נמצאת במקום הנכון במספר הסודי.
            - `clues += "FERMI "`: הוספת רמז "FERMI" למחרוזת הרמזים אם התנאי מתקיים.
        - `elif digit in secret_number`: בדיקה האם הספרה קיימת במספר הסודי אך לא במקום הנכון.
            - `clues += "PICO "`: הוספת רמז "PICO" למחרוזת הרמזים אם התנאי מתקיים.
    - `if not clues:`: בדיקה האם מחרוזת הרמזים ריקה, אם כן זה אומר שאין התאמות.
        - `clues = "BAGELS"`: הוספת רמז "BAGELS" למחרוזת הרמזים אם אין התאמות.
    - `return clues`: החזרת מחרוזת הרמזים.
4. **הגדרת הפונקציה `play_bagels_game()`**:
    - `def play_bagels_game():`: פונקציה זו מנהלת את כל מהלך המשחק.
    - `numberOfDigits = 3`: הגדרת מספר הספרות במספר הסודי.
    - `secretNumber = generate_secret_number(numberOfDigits)`: קריאה לפונקציה ליצירת מספר סודי.
    - `numberOfGuesses = 0`: אתחול מונה הניסיונות.
    - `print("I am thinking of a number that has {} unique digits. Try to guess it.".format(numberOfDigits))`: הודעה למשתמש על תחילת המשחק.
    - לולאת `while True`: לולאה אינסופית עד שהמשתמש מנחש את המספר נכון.
        - `numberOfGuesses += 1`: הגדלת מונה הניסיונות.
        - `userGuess = input(f"Guess {numberOfGuesses}: Enter a {numberOfDigits}-digit guess: ")`: בקשת קלט מהמשתמש.
        - `if not userGuess.isdigit() or len(userGuess) != numberOfDigits:` בדיקה אם הקלט תקין.
            - `print(f"Please enter a {numberOfDigits}-digit number.")`: הודעה למשתמש על קלט לא תקין
            - `continue`: המשך הלולאה לניחוש נוסף.
        - `if userGuess == secretNumber`: בדיקה האם הניחוש נכון.
            - `print(f"You got it in {numberOfGuesses} guesses!")`: הודעה על ניצחון.
            - `break`: יציאה מהלולאה.
        - `else`: אם הניחוש לא נכון.
            - `clues = get_clues(userGuess, secretNumber)`: קריאה לפונקציה לקבלת רמזים.
            - `print("Clues: ", clues)`: הצגת רמזים למשתמש.
5. **הפעלת המשחק**:
    - `if __name__ == "__main__":`: בלוק זה מוודא שהפונקציה `play_bagels_game()` תופעל רק כאשר הסקריפט רץ ישירות, ולא כאשר הוא מיובא כמודול.
    - `play_bagels_game()`: קריאה לפונקציה להפעלת המשחק.
"""
