
BAGELS:
=================
קושי: 5
-----------------
המשחק "בייגלס" הוא משחק ניחוש מספרים בו השחקן מנסה לנחש מספר בן 3 ספרות ייחודיות (ללא ספרות חוזרות).
המחשב נותן רמזים: "Pico" אם ספרה קיימת במספר המטרה אך לא במיקום הנכון, "Fermi" אם ספרה קיימת במספר המטרה ובמיקום הנכון,
ו"Bagels" אם אין ספרות מתאימות.

חוקי המשחק:
1. המחשב בוחר מספר בן 3 ספרות שונות (ללא חזרות) באופן אקראי.
2. השחקן מזין מספר בעל 3 ספרות שונות.
3. המחשב נותן רמזים:
    - "Fermi" עבור כל ספרה שנמצאת במקום הנכון.
    - "Pico" עבור כל ספרה שנמצאת במספר, אך לא במיקום הנכון.
    - "Bagels" אם אין ספרות מתאימות.
4. המשחק נמשך עד שהשחקן מנחש את המספר הנכון.
-----------------
אלגוריתם:
1. יצירת מספר סודי בן 3 ספרות שונות.
2. אתחול מספר הניחושים ל-0.
3. לולאה: כל עוד לא נוחש המספר:
   3.1. הגדל את מספר הניחושים ב-1.
   3.2. קלוט את הניחוש של השחקן.
   3.3. אם הניחוש שווה למספר הסודי: הדפס הודעת ניצחון וצא מהלולאה.
   3.4. אם הניחוש אינו נכון:
       3.4.1. אתחל מחרוזת רמז ריקה.
       3.4.2. עבור על כל ספרה במיקום i בניחוש ובמספר הסודי.
          - אם הספרה במיקום i בניחוש שווה לספרה במיקום i במספר הסודי:
             הוסף "Fermi" למחרוזת הרמז.
          - אחרת, אם הספרה במיקום i בניחוש נמצאת במספר הסודי, הוסף "Pico" למחרוזת הרמז.
       3.4.3 אם מחרוזת הרמז ריקה, הוסף "Bagels".
       3.4.4 הדפס את מחרוזת הרמז.
4. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> GenerateSecretNumber["<p align='left'>יצירת מספר סודי:
    <code><b>
    secretNumber = generateRandomUniqueNumber(3)
    </b></code></p>"]
    GenerateSecretNumber --> InitializeGuesses["אתחול ניחושים: <code><b>numberOfGuesses = 0</b></code>"]
    InitializeGuesses --> LoopStart{"תחילת לולאה: כל עוד לא נוחש"}
    LoopStart -- כן --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputGuess["קלט ניחוש מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> CheckGuess{"בדיקה: <code><b>userGuess == secretNumber?</b></code>"}
    CheckGuess -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES!</b>"]
    OutputWin --> End["סוף"]
    CheckGuess -- לא --> InitializeClue["אתחול רמז: <code><b>clue = ''</b></code>"]
    InitializeClue --> LoopDigits{"לולאה על ספרות הניחוש"}
    LoopDigits --> CheckFermi{"בדיקה: <code><b>userGuess[i] == secretNumber[i]?</b></code>"}
    CheckFermi -- כן --> AddFermi["<code><b>clue = clue + 'Fermi '</b></code>"]
    AddFermi --> NextDigit["מעבר לספרה הבאה"]
    CheckFermi -- לא --> CheckPico{"בדיקה: <code><b>userGuess[i] in secretNumber?</b></code>"}
    CheckPico -- כן --> AddPico["<code><b>clue = clue + 'Pico '</b></code>"]
    AddPico --> NextDigit
     CheckPico -- לא --> NextDigit
    NextDigit --> LoopDigitsEnd{"סוף לולאה על ספרות הניחוש"}
    LoopDigitsEnd -- לא --> LoopDigits
    LoopDigitsEnd -- כן --> CheckClueEmpty{"בדיקה: <code><b>clue == ''?</b></code>"}
    CheckClueEmpty -- כן --> AddBagels["<code><b>clue = 'Bagels'</b></code>"]
    AddBagels --> OutputClue["הצגת רמז: <code><b>clue</b></code>"]
    CheckClueEmpty -- לא --> OutputClue
    OutputClue --> LoopStart
    LoopStart -- לא --> End
```
Legenda:
    Start - התחלת המשחק.
    GenerateSecretNumber - יצירת מספר סודי בן 3 ספרות שונות.
    InitializeGuesses - אתחול מספר הניחושים ל-0.
    LoopStart - תחילת לולאת המשחק, שמתרחשת כל עוד השחקן לא ניחש את המספר.
    IncreaseGuesses - הגדלת מספר הניחושים ב-1.
    InputGuess - קליטת הניחוש של השחקן.
    CheckGuess - בדיקה האם הניחוש שווה למספר הסודי.
    OutputWin - הצגת הודעה שהשחקן ניצח, כולל מספר הניחושים.
    End - סיום המשחק.
    InitializeClue - אתחול מחרוזת הרמז לריקה.
    LoopDigits - לולאה העוברת על כל ספרה במספר הניחוש.
    CheckFermi - בדיקה האם הספרה במיקום הנוכחי בניחוש שווה לספרה במיקום הנוכחי במספר הסודי.
    AddFermi - הוספת "Fermi " לרמז.
     NextDigit - מעבר לספרה הבאה
    CheckPico - בדיקה האם הספרה הנוכחית בניחוש נמצאת במספר הסודי, אך לא במיקום הנכון.
    AddPico - הוספת "Pico " לרמז.
    LoopDigitsEnd - סיום לולאת המעבר על הספרות.
    CheckClueEmpty - בדיקה האם מחרוזת הרמז ריקה.
    AddBagels - הוספת "Bagels" לרמז, אם מחרוזת הרמז ריקה.
    OutputClue - הצגת הרמז לשחקן.
```
```python
import random

def generate_secret_number():
    """
    יצירת מספר סודי בן 3 ספרות שונות (ללא חזרות).
    """
    digits = list(range(10))  # רשימה של ספרות 0 עד 9
    random.shuffle(digits)  # ערבוב רשימת הספרות באופן אקראי
    secret_number = digits[:3]  # בחירת 3 ספרות ראשונות מהרשימה המעורבבת
    # המרת הספרות לרשימה של מחרוזות
    return "".join(map(str, secret_number))

def get_clues(user_guess, secret_number):
    """
    הפקת רמזים על פי הניחוש של המשתמש והמספר הסודי.
    """
    clue = ""  # אתחול מחרוזת הרמז הריקה
    for i in range(len(user_guess)):
        if user_guess[i] == secret_number[i]:  # ספרה במקום הנכון
            clue += "Fermi "
        elif user_guess[i] in secret_number:  # ספרה קיימת אך לא במקום הנכון
            clue += "Pico "
    if clue == "":  # אם אין התאמה, נותנים "Bagels"
        clue = "Bagels"
    return clue.strip()  # החזרת הרמז, ללא רווחים מיותרים בקצה

def play_bagels():
    """
    המשחק "בייגלס" - המשתמש מנסה לנחש מספר בן 3 ספרות שונות.
    """
    secret_number = generate_secret_number()  # יצירת מספר סודי
    number_of_guesses = 0  # אתחול מספר הניסיונות

    print("בייגלס: נסה לנחש מספר בן 3 ספרות שונות.")

    while True: # לולאה אינסופית - עד שהשחקן מנצח
        number_of_guesses += 1 # הגדלת מונה הניסיונות
        user_guess = input("הזן ניחוש: ")  # קלט מהמשתמש

        if not user_guess.isdigit() or len(user_guess) != 3:
            print("ניחוש לא תקין. יש להזין מספר בן 3 ספרות")
            continue # חוזרים לתחילת הלולאה

        if user_guess == secret_number: # בדיקה האם הניחוש נכון
            print(f"ניצחת! ניחשת את המספר {secret_number} ב-{number_of_guesses} ניסיונות.")
            break # יציאה מהלולאה
        else:
            clue = get_clues(user_guess, secret_number) # קבלת רמז
            print(clue)

if __name__ == "__main__":
    play_bagels() # הפעלת המשחק
```
הסברים:
1.  **ייבוא המודול `random`**:
    - `import random`: ייבוא המודול `random`, המשמש ליצירת מספר אקראי.
2.  **פונקציה `generate_secret_number()`**:
    - הפונקציה יוצרת מספר סודי אקראי בן 3 ספרות שונות (ללא חזרות).
    - `digits = list(range(10))`: יוצרת רשימה של הספרות 0 עד 9.
    - `random.shuffle(digits)`: מערבבת את רשימת הספרות באופן אקראי.
    - `secret_number = digits[:3]`: לוקחת את 3 הספרות הראשונות מהרשימה המעורבבת.
    - `return "".join(map(str, secret_number))`: ממירה את רשימת הספרות למחרוזת ומחזירה אותה.
3.  **פונקציה `get_clues(user_guess, secret_number)`**:
    - פונקציה המקבלת את הניחוש של השחקן ואת המספר הסודי ומחזירה רמזים.
    - `clue = ""`: מאתחלת מחרוזת ריקה שתכיל את הרמז.
    - לולאה העוברת על כל ספרה בניחוש:
        - `if user_guess[i] == secret_number[i]`: בודקת אם הספרה במיקום i שווה לספרה באותו מיקום במספר הסודי. אם כן, מוסיפה "Fermi " למחרוזת הרמז.
        - `elif user_guess[i] in secret_number`: בודקת אם הספרה קיימת במספר הסודי, אך לא במיקום הנכון. אם כן, מוסיפה "Pico " למחרוזת הרמז.
    - `if clue == ""`: אם אין התאמה, הרמז הוא "Bagels".
    - `return clue.strip()`: מחזירה את הרמז, ללא רווחים מיותרים.
4.  **פונקציה `play_bagels()`**:
    - פונקציה המנהלת את משחק ה"בייגלס".
    - `secret_number = generate_secret_number()`: יוצרת מספר סודי באופן אקראי.
    - `number_of_guesses = 0`: מאתחלת את מספר הניחושים ל-0.
    - `while True:`: לולאה אינסופית, שתמשיך עד שהשחקן ינחש את המספר.
    - `number_of_guesses += 1`: הגדלת מספר הניחושים.
    - `user_guess = input("הזן ניחוש: ")`: מבקשת מהשחקן להזין ניחוש.
    - בדיקת תקינות קלט:
        - `if not user_guess.isdigit() or len(user_guess) != 3:` בודקת האם הקלט מכיל רק ספרות והוא באורך 3.
        - אם הקלט לא תקין, מוצגת הודעת שגיאה והלולאה ממשיכה לקלט הבא.
    - `if user_guess == secret_number`: בודקת אם הניחוש נכון.
        - אם הניחוש נכון, מוצגת הודעה שהשחקן ניצח ומספר הניחושים והלולאה מסתיימת.
    - אחרת:
        - `clue = get_clues(user_guess, secret_number)`: מקבלת את הרמז.
        - הרמז מוצג לשחקן.
5.  `if __name__ == "__main__":`: בלוק זה מוודא שהקוד יופעל רק כאשר הקובץ מורץ ישירות, ולא כאשר הוא מיובא כמודול.
6. `play_bagels()`: הפעלת המשחק.
```