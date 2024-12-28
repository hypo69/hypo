# <SPACWRD>
=================
קושי: 5
-----------------
"SPACWRD" הוא משחק מילים בו השחקן מנסה לנחש מילה בת 5 אותיות שהמחשב בחר. לאחר כל ניסיון ניחוש, המחשב מספק רמזים: כוכבית (*) מציינת אות נכונה במיקום הנכון, נקודה (.) מציינת אות נכונה במיקום שגוי, ורווח מציין שהאות אינה במילה. המטרה היא לנחש את המילה בכמה שפחות ניסיונות.

חוקי המשחק:
1. המחשב בוחר מילה אקראית בת 5 אותיות מתוך רשימת מילים מוגדרת מראש.
2. השחקן מנסה לנחש את המילה.
3. לאחר כל ניסיון, המחשב נותן רמז:
    - * : אות נכונה במיקום הנכון.
    - . : אות נכונה במיקום שגוי.
    -   (רווח): אות שאינה במילה.
4. המשחק נמשך עד שהשחקן מנחש נכון את המילה או עד שמספר הניסיונות המקסימלי מגיע.
5. בסוף המשחק מוצגת המילה שנבחרה ומספר הניסיונות.
-----------------
אלגוריתם:
1. הגדר רשימת מילים בת 5 אותיות.
2. בחר מילה אקראית מהרשימה.
3. הגדר את מספר הניסיונות ל-0 ואת מספר הניסיונות המקסימלי (למשל 10).
4. התחל לולאה "כל עוד מספר הניסיונות קטן מהמספר המקסימלי":
  4.1. הגדל את מספר הניסיונות ב-1.
  4.2. קבל קלט מהשחקן - ניחוש של מילה בת 5 אותיות.
  4.3. אם הניחוש זהה למילה הנבחרת, עבור לשלב 6.
  4.4. צור רמז עבור הניחוש:
      - עבור כל אות בניחוש:
        - אם האות במקום הנכון במילה הנבחרת, הוסף * לרמז.
        - אם האות קיימת במילה הנבחרת במקום אחר, הוסף . לרמז.
        - אחרת, הוסף רווח לרמז.
  4.5 הצג את הרמז לשחקן.
5. אם הלולאה הסתיימה ומספר הניסיונות הגיע למקסימום, הצג הודעה שהשחקן הפסיד והצג את המילה הנכונה.
6. אם השחקן ניחש נכון, הצג הודעת ניצחון עם מספר הניסיונות.
7. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeGame["<p align='left'>אתחול משתנים:
    <code><b>
    words = ['APPLE', 'GRAPE', ...]
    secretWord = random(words)
    numberOfGuesses = 0
    maxGuesses = 10
    </b></code></p>"]
    InitializeGame --> LoopStart{"תחילת לולאה: <code><b>numberOfGuesses < maxGuesses</b></code>"}
    LoopStart -- כן --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputGuess["קלט מילה מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> CheckWin{"בדיקה: <code><b>userGuess == secretWord?</b></code>"}
    CheckWin -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES!</b>"]
    OutputWin --> End["סוף"]
    CheckWin -- לא --> GenerateHint["<p align='left'>יצירת רמז:
    <code><b>
    hint = ''
    for each letter in userGuess:
        if letter in correct position: hint += '*'
        else if letter in secretWord: hint += '.'
        else: hint += ' '
    </b></code></p>"]
    GenerateHint --> OutputHint["הצגת רמז: <code><b>hint</b></code>"]
    OutputHint --> LoopStart
    LoopStart -- לא --> OutputLose["הצגת הודעה: <b>YOU LOST! The word was <code>{secretWord}</code></b>"]
    OutputLose --> End

```
Legenda:
    Start - התחלת התוכנית.
    InitializeGame - אתחול משתנים: רשימת המילים, בחירת מילה סודית אקראית, אתחול מספר הניסיונות ל-0 ומספר ניסיונות מקסימלי.
    LoopStart - תחילת הלולאה, הממשיכה כל עוד מספר הניסיונות קטן ממספר הניסיונות המקסימלי.
    IncreaseGuesses - הגדלת מונה הניסיונות ב-1.
    InputGuess - קלט מילה מהמשתמש ושמירתו במשתנה userGuess.
    CheckWin - בדיקה האם המילה שהוזנה שווה למילה הסודית.
    OutputWin - הצגת הודעת ניצחון, אם המילה נוחשה, עם מספר הניסיונות.
    End - סוף התוכנית.
    GenerateHint - יצירת רמז עבור ניחוש המשתמש, הכולל כוכביות, נקודות ורווחים בהתאם למיקום האותיות במילה הסודית.
    OutputHint - הצגת הרמז למשתמש.
    OutputLose - הצגת הודעת הפסד והמילה הסודית לאחר שמספר הניסיונות המקסימלי הגיע.
"""
import random

# רשימת מילים באורך 5 אותיות
words = ["APPLE", "GRAPE", "CHAIR", "TABLE", "MOUSE", "PIANO", "FLUTE", "TIGER", "EARTH", "OCEAN"]

# בחירת מילה אקראית מהרשימה
secretWord = random.choice(words)

# הגדרת מספר הניסיונות והמקסימום
numberOfGuesses = 0
maxGuesses = 10

# לולאת המשחק הראשית
while numberOfGuesses < maxGuesses:
    numberOfGuesses += 1
    try:
        userGuess = input("נחש מילה בת 5 אותיות: ").upper() # קלט מהמשתמש והמרה לאותיות גדולות
        if len(userGuess) != 5 or not userGuess.isalpha():
          print("קלט לא תקין. אנא הזן מילה בת 5 אותיות בלבד.")
          continue
    except ValueError:
      print("קלט לא תקין. אנא הזן מילה בת 5 אותיות בלבד.")
      continue
    
    # בדיקה האם הניחוש נכון
    if userGuess == secretWord:
        print(f"מזל טוב! ניחשת את המילה ב-{numberOfGuesses} ניסיונות!")
        break

    # בניית הרמז
    hint = ""
    for i in range(5):
        if userGuess[i] == secretWord[i]:
            hint += "*"  # אות נכונה במקום הנכון
        elif userGuess[i] in secretWord:
            hint += "."  # אות נכונה במקום לא נכון
        else:
            hint += " "  # אות לא קיימת
    print(f"רמז: {hint}")

# אם הגיעו למספר המקסימלי של ניסיונות, המשחק נגמר בהפסד
if numberOfGuesses == maxGuesses:
    print(f"הפסדת! המילה הייתה {secretWord}")

"""
הסבר הקוד:
1. **ייבוא מודול `random`**:
   - `import random`: ייבוא המודול random, המשמש ליצירת בחירת מילה אקראית.

2. **הגדרת רשימת המילים**:
   - `words = ["APPLE", "GRAPE", ... ]`: רשימה של מילים באורך 5 אותיות מהן המחשב יבחר מילה.

3. **בחירת מילה סודית**:
   - `secretWord = random.choice(words)`: בחירת מילה אקראית מהרשימה ושמירתה במשתנה `secretWord`.

4. **אתחול משתנים**:
   - `numberOfGuesses = 0`: מונה ניסיונות מאותחל ל-0.
   - `maxGuesses = 10`: מספר הניסיונות המקסימלי מוגדר ל-10.

5. **לולאת המשחק `while numberOfGuesses < maxGuesses:`**:
   - לולאה הממשיכה כל עוד מספר הניסיונות קטן ממספר הניסיונות המקסימלי.
   - `numberOfGuesses += 1`: הגדלת מונה הניסיונות ב-1 בכל סיבוב.
    - **קלט נתונים**:
        - `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין משהו שאינו מילה, יוצג הודעת שגיאה.
        - `userGuess = input("נחש מילה בת 5 אותיות: ").upper()`: בקשת ניחוש מילה מהמשתמש והמרתו לאותיות גדולות.
        - `if len(userGuess) != 5 or not userGuess.isalpha():`: בדיקה האם הקלט תקין (מילה בת 5 אותיות).
        - `continue`: אם הקלט לא תקין, חוזרים לתחילת הלולאה.

6. **בדיקת ניצחון**:
    - `if userGuess == secretWord:`: בדיקה האם הניחוש זהה למילה הסודית.
    - `print(f"מזל טוב! ניחשת את המילה ב-{numberOfGuesses} ניסיונות!")`: הצגת הודעת ניצחון עם מספר הניסיונות.
    - `break`: יציאה מהלולאה לאחר ניצחון.

7. **יצירת רמז**:
    - `hint = ""`: אתחול מחרוזת ריקה עבור הרמז.
    - לולאה על כל אות בניחוש:
      - `if userGuess[i] == secretWord[i]`: אם האות במקום הנכון - הוספת `*` לרמז.
      - `elif userGuess[i] in secretWord`: אם האות במילה אך לא במקום הנכון - הוספת `.` לרמז.
      - `else`: אם האות לא במילה - הוספת ` ` (רווח) לרמז.
    - `print(f"רמז: {hint}")`: הצגת הרמז למשתמש.

8. **הודעת הפסד**:
    - `if numberOfGuesses == maxGuesses`: בדיקה אם הגענו למספר המקסימלי של ניסיונות.
    - `print(f"הפסדת! המילה הייתה {secretWord}")`: הצגת הודעת הפסד והמילה הסודית.
"""
