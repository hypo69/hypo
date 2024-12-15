<BULLCOW>:
=================
קושי: 5
-----------------
המשחק "שור-פרה" הוא משחק ניחושים בו המחשב בוחר מספר בעל 4 ספרות שונות, והשחקן מנסה לנחש אותו. לאחר כל ניחוש, המחשב מספק רמזים: "שור" עבור כל ספרה במקום הנכון, ו"פרה" עבור כל ספרה נכונה במקום הלא נכון. המטרה היא לנחש את המספר בכמה שפחות ניסיונות.

חוקי המשחק:
1. המחשב בוחר מספר בן 4 ספרות שונות באופן אקראי.
2. השחקן מזין ניחוש של מספר בעל 4 ספרות שונות.
3. המחשב מגיב על ידי ציון מספר ה"שור" (ספרות נכונות במקום הנכון) ומספר ה"פרות" (ספרות נכונות במקום הלא נכון).
4. המשחק נמשך עד שהשחקן מנחש את המספר המדויק.
5. ניחוש לא תקין נפסל והשחקן מתבקש להזין מספר תקין.
-----------------
אלגוריתם:
1.  צור מספר אקראי בן 4 ספרות שונות.
2.  התחל לולאה:
    2.1. קלוט מהמשתמש ניחוש בן 4 ספרות.
    2.2. אם הקלט אינו 4 ספרות שונות, בקש קלט חוזר.
    2.3. אם הניחוש נכון, הצג הודעת ניצחון וצא מהלולאה.
    2.4. אם הניחוש אינו נכון, חשב את מספר השוורים והפרות.
    2.5. הצג למשתמש את מספר השוורים והפרות.
    2.6. המשך בלולאה.
3. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> GenerateTargetNumber["<p align='left'>יצירת מספר מטרה אקראי: 
    <code><b>targetNumber = generate_random_4_digit_number()</b></code></p>"]
    GenerateTargetNumber --> LoopStart{"תחילת לולאה: כל עוד לא נוחש"}
    LoopStart -- כן --> InputGuess["קלט ניחוש מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> ValidateGuess["בדיקה: האם הניחוש תקין (4 ספרות שונות)?"]
    ValidateGuess -- לא --> InputError["הצגת הודעה: <b>קלט לא תקין. אנא הזן 4 ספרות שונות.</b>"]
    InputError --> LoopStart
    ValidateGuess -- כן --> CheckWin{"בדיקה: <code><b>userGuess == targetNumber?</b></code>"}
    CheckWin -- כן --> OutputWin["הצגת הודעה: <b>מזל טוב! ניחשת את המספר.</b>"]
    OutputWin --> End["סוף"]
    CheckWin -- לא --> CalculateBullsCows["חישוב שוורים ופרות: 
    <code><b>bulls, cows = calculate_bulls_cows(userGuess, targetNumber)</b></code>"]
    CalculateBullsCows --> OutputBullsCows["הצגת הודעה: <b>{bulls} שוורים, {cows} פרות.</b>"]
    OutputBullsCows --> LoopStart
    LoopStart -- לא --> End

```

Legenda:
    Start - התחלת התוכנית.
    GenerateTargetNumber - יצירת מספר מטרה (בן 4 ספרות שונות) באופן אקראי.
    LoopStart - תחילת הלולאה, הממשיכה כל עוד המספר לא נוחש.
    InputGuess - קלט מספר (ניחוש) מהמשתמש.
    ValidateGuess - בדיקה האם הקלט תקין (4 ספרות שונות).
    InputError - הצגת הודעת שגיאה במקרה של קלט לא תקין, וחזרה ללולאה.
    CheckWin - בדיקה האם הניחוש נכון.
    OutputWin - הצגת הודעת ניצחון וסיום המשחק.
    CalculateBullsCows - חישוב מספר השוורים והפרות.
    OutputBullsCows - הצגת מספר השוורים והפרות למשתמש.
    End - סיום התוכנית.
"""
```python
import random

def generate_random_4_digit_number():
    """
    פונקציה ליצירת מספר אקראי בן 4 ספרות שונות.

    Returns:
        str: מספר בן 4 ספרות שונות.
    """
    digits = list(range(10)) # רשימה של כל הספרות 0-9
    random.shuffle(digits)   # ערבוב הספרות
    while digits[0] == 0:     # מוודאים שהספרה הראשונה אינה 0
        random.shuffle(digits)
    return "".join(map(str, digits[:4])) # המרת 4 הספרות הראשונות למחרוזת

def is_valid_guess(guess):
    """
    פונקציה לבדיקה האם הניחוש תקין (4 ספרות שונות).

    Args:
        guess (str): הניחוש מהמשתמש.

    Returns:
        bool: האם הניחוש תקין.
    """
    if not guess.isdigit() or len(guess) != 4: # בדיקה האם הקלט הוא 4 ספרות
         return False
    return len(set(guess)) == 4 # בדיקה האם כל הספרות שונות

def calculate_bulls_cows(guess, target):
    """
    פונקציה לחישוב מספר השוורים והפרות.
    
    Args:
        guess (str): ניחוש המשתמש.
        target (str): מספר המטרה.
    Returns:
        tuple: מספר השוורים והפרות.
    """
    bulls = 0 # מספר השוורים
    cows = 0  # מספר הפרות
    for i, digit in enumerate(guess): # בדיקת כל ספרה בניחוש
        if digit == target[i]:
            bulls += 1  # ספרה נכונה במקום הנכון - שור
        elif digit in target:
            cows += 1   # ספרה נכונה במקום לא נכון - פרה
    return bulls, cows

def play_bullcow_game():
    """
    פונקציה המגדירה את המשחק שור-פרה.
    """
    target_number = generate_random_4_digit_number() # יצירת מספר המטרה
    print("אני חושב על מספר בן 4 ספרות שונות. נסה לנחש אותו!")

    while True:
        user_guess = input("הזן ניחוש (4 ספרות שונות): ") # קבלת ניחוש מהמשתמש

        if not is_valid_guess(user_guess): # בדיקת תקינות הניחוש
            print("קלט לא תקין. אנא הזן 4 ספרות שונות.")
            continue

        if user_guess == target_number: # בדיקה האם הניחוש נכון
            print("מזל טוב! ניחשת את המספר!")
            break

        bulls, cows = calculate_bulls_cows(user_guess, target_number) # חישוב שוורים ופרות
        print(f"{bulls} שוורים, {cows} פרות.") # הצגת רמזים למשתמש

if __name__ == "__main__":
    play_bullcow_game() # הפעלת המשחק
```
<הערות סיום>
הסברים:

1.  **ייבוא מודול `random`**:
    - `import random`: ייבוא המודול random, המשמש ליצירת מספר אקראי.
2.  **פונקציה `generate_random_4_digit_number()`**:
    -   פונקציה זו יוצרת מספר אקראי בן 4 ספרות שונות.
    -   `digits = list(range(10))`: יצירת רשימה של ספרות מ-0 עד 9.
    -   `random.shuffle(digits)`: ערבוב רשימת הספרות באופן אקראי.
    -   `while digits[0] == 0:`: לולאה המבטיחה שהספרה הראשונה לא תהיה 0.
    -   `return "".join(map(str, digits[:4]))`: החזרת 4 הספרות הראשונות כמחרוזת.
3. **פונקציה `is_valid_guess(guess)`**:
    - פונקציה זו בודקת האם הקלט מהמשתמש (ניחוש) תקין.
    - `if not guess.isdigit() or len(guess) != 4:`: בדיקה האם הקלט הוא 4 ספרות בדיוק.
    - `return len(set(guess)) == 4`: בדיקה האם כל הספרות בניחוש שונות אחת מהשניה.
4. **פונקציה `calculate_bulls_cows(guess, target)`**:
    - פונקציה זו מחשבת את מספר ה"שוורים" (ספרות נכונות במקום הנכון) וה"פרות" (ספרות נכונות במקום הלא נכון).
    -   `bulls = 0`, `cows = 0`: אתחול מונים לשוורים ולפרות.
    -   `for i, digit in enumerate(guess):`: מעבר על כל ספרה בניחוש.
    -   `if digit == target[i]:`: בדיקה אם הספרה נמצאת במקום הנכון.
    -   `elif digit in target`: בדיקה אם הספרה נמצאת במספר המטרה אך לא במקום הנכון.
    -   `return bulls, cows`: החזרת מספר השוורים והפרות.
5. **פונקציה `play_bullcow_game()`**:
    - הפונקציה הראשית המגדירה את המשחק שור-פרה.
    - `target_number = generate_random_4_digit_number()`: יצירת מספר המטרה.
    -   `while True`: לולאה ראשית של המשחק, אשר תרוץ עד שהמשתמש ינחש את המספר.
    -   `user_guess = input("הזן ניחוש (4 ספרות שונות): ")`: קבלת ניחוש מהמשתמש.
    -   `if not is_valid_guess(user_guess)`: בדיקה האם הניחוש תקין.
    -   `if user_guess == target_number`: בדיקה האם הניחוש נכון.
    - `bulls, cows = calculate_bulls_cows(user_guess, target_number)`: חישוב שוורים ופרות עבור הניחוש.
    -  `print(f"{bulls} שוורים, {cows} פרות.")`: הצגת מספר השוורים והפרות למשתמש.
6. **`if __name__ == "__main__":`**:
    -   בלוק זה מבטיח שהפונקציה `play_bullcow_game()` תופעל רק אם הקובץ מופעל ישירות, ולא אם הוא מיובא כמודול.
    -  `play_bullcow_game()`: קריאה לפונקציה כדי להפעיל את המשחק.
</הערות סיום>
