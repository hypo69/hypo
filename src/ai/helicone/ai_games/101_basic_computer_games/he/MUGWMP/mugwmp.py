"""
MUGWMP:
=================
קושי: 5
-----------------
המשחק "MUGWMP" הוא משחק ניחושים בו השחקן מנסה לנחש סדרה בת ארבע ספרות, כאשר כל ספרה היא בין 1 ל-6. לאחר כל ניסיון, המחשב מספק רמזים על מספר הספרות הנכונות במקום הנכון (Mugs) ומספר הספרות הנכונות במקום הלא נכון (Wumps).
המשחק נמשך עד שהשחקן מנחש את הסדרה במלואה.

חוקי המשחק:
1. המחשב בוחר סדרה אקראית בת 4 ספרות, כאשר כל ספרה היא בין 1 ל-6.
2. השחקן מזין סדרה בת 4 ספרות כניסיון ניחוש.
3. המחשב מגיב בשני רמזים: "Mugs" - מספר הספרות הנכונות במקום הנכון, ו-"Wumps" - מספר הספרות הנכונות במקום הלא נכון.
4. המשחק נמשך עד שהשחקן מנחש את הסדרה במלואה (4 Mugs).

-----------------
אלגוריתם:
1. צור סדרה אקראית בת 4 ספרות בין 1 ל-6.
2. אתחל את מספר הניסיונות ל-0.
3. התחל לולאה "כל עוד לא נוחשה הסדרה":
   3.1 הגדל את מספר הניסיונות ב-1.
   3.2 קלוט מהמשתמש סדרה בת 4 ספרות.
   3.3 חשב את מספר ה-"Mugs" (ספרות נכונות במיקום נכון).
   3.4 חשב את מספר ה-"Wumps" (ספרות נכונות במיקום לא נכון).
   3.5 הצג את מספר ה-"Mugs" וה-"Wumps".
   3.6 אם יש 4 "Mugs", סיימנו את המשחק.
4. הצג הודעת ניצחון עם מספר הניסיונות.
5. סוף המשחק.

-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeGame["<p align='left'>אתחול:
    <code><b>
    targetSequence = randomSequence(1, 6, 4)<br>
    numberOfGuesses = 0
    </b></code></p>"]
    InitializeGame --> LoopStart{"תחילת לולאה: כל עוד לא נוחש"}
    LoopStart -- כן --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputGuess["קלט מהמשתמש סדרה בת 4 ספרות: <code><b>userSequence</b></code>"]
    InputGuess --> CalculateMugs["חישוב <code><b>mugs</b></code>: מספר הספרות הנכונות במיקום נכון"]
    CalculateMugs --> CalculateWumps["חישוב <code><b>wumps</b></code>: מספר הספרות הנכונות במיקום לא נכון"]
    CalculateWumps --> OutputHints["הצגת רמזים: <b>Mugs: <code>{mugs}</code>, Wumps: <code>{wumps}</code></b>"]
    OutputHints --> CheckWin{"בדיקה: <code><b>mugs == 4?</b></code>"}
    CheckWin -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES!</b>"]
    OutputWin --> End["סוף"]
    CheckWin -- לא --> LoopStart
    LoopStart -- לא --> End
```
Legenda:
    Start - התחלת התוכנית.
    InitializeGame - אתחול משתנים: targetSequence (הסדרה המוגלה) נוצרת באקראי בין 1 ל-6 באורך 4, ו-numberOfGuesses (מספר הניסיונות) מאותחל ל-0.
    LoopStart - תחילת הלולאה, הממשיכה כל עוד הסדרה לא נוחשה.
    IncreaseGuesses - הגדלת מונה הניסיונות ב-1.
    InputGuess - קלט סדרה בת 4 ספרות מהמשתמש ושמירתו במשתנה userSequence.
    CalculateMugs - חישוב מספר הספרות הנכונות במיקום נכון (mugs).
    CalculateWumps - חישוב מספר הספרות הנכונות במיקום לא נכון (wumps).
    OutputHints - הצגת רמזים: מספר ה-mugs וה-wumps.
    CheckWin - בדיקה האם מספר ה-mugs שווה ל-4.
    OutputWin - הצגת הודעת ניצחון, אם הסדרה נוחשה, עם מספר הניסיונות.
    End - סוף התוכנית.
"""
```python
import random

def create_target_sequence():
    """
    יוצר סדרה אקראית בת 4 ספרות, כאשר כל ספרה בין 1 ל-6.
    """
    return [random.randint(1, 6) for _ in range(4)]

def calculate_mugs_wumps(target_sequence, user_sequence):
    """
    מחשב את מספר ה"Mugs" (ספרות נכונות במיקום נכון) וה-"Wumps" (ספרות נכונות במיקום לא נכון).

    Args:
      target_sequence (list): הסדרה המקורית שהמשתמש מנסה לנחש.
      user_sequence (list): הסדרה שהמשתמש הזין כניחוש.

    Returns:
      tuple: מספר ה-mugs ומספר ה-wumps.
    """
    mugs = 0
    wumps = 0
    temp_target = list(target_sequence)
    temp_user = list(user_sequence)

    # חישוב Mugs
    for i in range(4):
        if temp_user[i] == temp_target[i]:
            mugs += 1
            temp_user[i] = None
            temp_target[i] = None

    # חישוב Wumps
    for i in range(4):
        if temp_user[i] is not None:
          for j in range(4):
              if temp_target[j] is not None and temp_user[i] == temp_target[j]:
                  wumps += 1
                  temp_target[j] = None
                  break
    return mugs, wumps

def play_mugwmp():
    """
    מנהל את משחק ה-MUGWMP.
    """
    target_sequence = create_target_sequence() # יצירת הסדרה האקראית שהמשתמש מנסה לנחש
    numberOfGuesses = 0 # אתחול מונה הניסיונות

    while True: # לולאת המשחק
        numberOfGuesses += 1 # הגדלת מונה הניסיונות
        try:
            user_input = input("הזן סדרה בת 4 ספרות (בין 1 ל-6): ") # קבלת קלט מהמשתמש
            user_sequence = [int(digit) for digit in user_input] # המרת הקלט למספרים שלמים

            if len(user_sequence) != 4 or any(digit < 1 or digit > 6 for digit in user_sequence):
                print("אנא הזן סדרה בת 4 ספרות, כאשר כל ספרה היא בין 1 ל-6.")
                continue
        except ValueError:
            print("אנא הזן סדרה של ספרות בלבד.")
            continue

        mugs, wumps = calculate_mugs_wumps(target_sequence, user_sequence) # חישוב הרמזים

        print(f"Mugs: {mugs}, Wumps: {wumps}") # הצגת הרמזים

        if mugs == 4: # בדיקה אם השחקן ניחש נכון
            print(f"מזל טוב! ניחשת את הסדרה ב-{numberOfGuesses} ניסיונות!")
            break # סיום המשחק

if __name__ == "__main__":
    play_mugwmp()
```
"""
הסבר הקוד:

1. **ייבוא מודול `random`**:
   - `import random`: ייבוא מודול `random` ליצירת רצף מספרים אקראיים.

2. **פונקציה `create_target_sequence()`**:
   - יוצרת רצף של 4 מספרים אקראיים בין 1 ל-6.
   - משתמשת ב-`list comprehension` ליצירת הרשימה בקצרה.

3. **פונקציה `calculate_mugs_wumps(target_sequence, user_sequence)`**:
   - מקבלת שני רצפים: את הרצף שהמשתמש מנסה לנחש ואת הניחוש שלו.
   - משתמשת בשני משתנים `mugs` ו-`wumps` לספירת מספר הניחושים הנכונים במקום ובמקום שגוי.
   - מעתיקה את הרצפים למשתנים זמניים כדי לשנות את הערכים שלהם בלי להשפיע על הרצפים המקוריים.
   - עוברת על הרצפים, וכל איבר שזהה ברצף המקורי וברצף שהמשתמש הזין, מעלה את מונה ה-`mugs` ומאפסת את האיבר ברצפים הזמניים.
   - עוברת שוב על הרצפים, וכל איבר ברצף שהמשתמש הזין שקיים ברצף המקורי, מעלה את מונה ה-`wumps` ומאפסת את האיבר ברצף המקורי הזמני.

4. **פונקציה `play_mugwmp()`**:
   - מגדירה את הלוגיקה של המשחק.
   - יוצרת את הסדרה שהמשתמש צריך לנחש באמצעות `create_target_sequence()`.
   - מאתחלת את מונה הניסיונות (`numberOfGuesses`) לאפס.
   - **לולאת משחק `while True:`**:
     - מגדילה את מונה הניסיונות בכל סיבוב.
     - מקבלת קלט מהמשתמש:
       - באמצעות `input()` המשתמש מזין רצף של 4 ספרות.
       - באמצעות `try-except` מטפלים במקרים שבהם הקלט שגוי.
       - אם אורך הרצף אינו 4 או שיש בו מספרים מחוץ לטווח 1-6, מוצגת הודעה והלולאה חוזרת.
     - קוראת ל-`calculate_mugs_wumps()` כדי לקבל את מספר ה-`mugs` וה-`wumps`.
     - מציגה את הרמזים למשתמש.
     - בודקת אם מספר ה-`mugs` שווה ל-4 (המשתמש ניחש נכון):
       - אם כן, מוצגת הודעת ניצחון והמשחק מסתיים באמצעות `break`.

5. **הפעלת המשחק**:
   -  `if __name__ == "__main__":`: בלוק זה מבטיח שהפונקציה `play_mugwmp()` תופעל רק אם הקובץ מופעל ישירות, ולא אם הוא מיובא כמודול.
   -  `play_mugwmp()`: קריאה לפונקציה להפעלת המשחק.
"""
