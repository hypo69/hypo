<BUZZWD>:
=================
קושי: 2
-----------------
משחק "Buzzword" הוא משחק פשוט בו המחשב בוחר באקראי מילה מתוך רשימה קבועה של מילים, ולאחר מכן מציג אותה למשתמש בצורה מוצפנת. המשתמש מנסה לנחש את המילה המקורית, ומקבל משוב האם הניחוש שלו נכון או לא.

חוקי המשחק:
1. המחשב בוחר באופן אקראי מילה מתוך רשימה קבועה.
2. המחשב מערבב את אותיות המילה (אנגרמה).
3. המחשב מציג למשתמש את האנגרמה.
4. המשתמש מנסה לנחש את המילה המקורית.
5. המחשב מודיע למשתמש האם הניחוש שלו נכון או לא.
6. המשחק מסתיים כאשר המשתמש מנחש את המילה נכון.
-----------------
אלגוריתם:
1. הגדר רשימה של מילים (buzzwords).
2. בחר מילה באקראי מהרשימה.
3. ערבב את אותיות המילה שנבחרה.
4. הצג למשתמש את המילה המעורבבת.
5. בקש מהמשתמש לנחש את המילה.
6. אם הניחוש של המשתמש שווה למילה שנבחרה, הודע למשתמש שהוא ניחש נכון וסיים את המשחק.
7. אם לא, חזור לשלב 5.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeWords["<p align='left'>אתחול רשימת מילים:
    <code><b>
    words = ['COMPUTER', 'PROGRAM', 'SYSTEM', 'SOFTWARE', 'ALGORITHM']
    </b></code></p>"]
    InitializeWords --> SelectWord["<p align='left'>בחר מילה באקראי:
    <code><b>
    targetWord = random(words)
    </b></code></p>"]
    SelectWord --> ShuffleWord["<p align='left'>ערבב את אותיות המילה:
    <code><b>
    shuffledWord = shuffle(targetWord)
    </b></code></p>"]
    ShuffleWord --> OutputShuffledWord["הצג מילה מעורבבת: <code><b>shuffledWord</b></code>"]
    OutputShuffledWord --> InputGuess["קלט ניחוש מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> CheckGuess{"בדיקה: <code><b>userGuess == targetWord?</b></code>"}
    CheckGuess -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT!</b>"]
    OutputWin --> End["סוף"]
    CheckGuess -- לא --> InputGuess
```
Legenda:
  Start - התחלת המשחק.
  InitializeWords - אתחול רשימה של מילים אפשריות.
  SelectWord - בחירת מילה אקראית מתוך הרשימה.
  ShuffleWord - ערבוב האותיות של המילה שנבחרה.
  OutputShuffledWord - הצגת המילה המעורבבת למשתמש.
  InputGuess - קבלת ניחוש מהמשתמש.
  CheckGuess - בדיקה האם הניחוש של המשתמש שווה למילה המקורית.
  OutputWin - הצגת הודעת ניצחון וסיום המשחק.
  End - סוף המשחק.
"""
```python
import random

# רשימת מילים למשחק
buzzwords = ["COMPUTER", "PROGRAM", "SYSTEM", "SOFTWARE", "ALGORITHM"]

# בחירת מילה אקראית מהרשימה
target_word = random.choice(buzzwords)

# פונקציה לערבוב אותיות המילה
def shuffle_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

# ערבוב אותיות המילה
shuffled_word = shuffle_word(target_word)

# הצגת המילה המעורבבת למשתמש
print("נחש את המילה:")
print(shuffled_word)

# לולאת המשחק הראשית
while True:
    # קבלת ניחוש מהמשתמש
    user_guess = input("הכנס את הניחוש שלך: ").upper()

    # בדיקה האם הניחוש נכון
    if user_guess == target_word:
        print("כל הכבוד! ניחשת נכון!")
        break  # סיום המשחק אם הניחוש נכון
    else:
        print("ניסיון נוסף...") # בקשה לנסות שוב

"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    - `import random`: ייבוא המודול random, המשמש לבחירה אקראית של מילה ולערבוב האותיות.
2.  **רשימת המילים `buzzwords`**:
    - `buzzwords = ["COMPUTER", "PROGRAM", "SYSTEM", "SOFTWARE", "ALGORITHM"]`: רשימה של מילים שמהן תבחר המילה למשחק.
3.  **בחירת מילה אקראית**:
    - `target_word = random.choice(buzzwords)`: בחירת מילה באופן אקראי מתוך רשימת המילים ושמירתה במשתנה `target_word`.
4.  **פונקציה `shuffle_word(word)`**:
    - פונקציה המקבלת מילה ומחזירה את אותיותיה מעורבבות.
    - `word_list = list(word)`: המרת המילה לרשימה של תווים.
    - `random.shuffle(word_list)`: ערבוב אקראי של התווים ברשימה.
    - `return ''.join(word_list)`: החזרת המילה המעורבבת כמחרוזת.
5.  **ערבוב המילה**:
    - `shuffled_word = shuffle_word(target_word)`: קריאה לפונקציה `shuffle_word` כדי לערבב את אותיות המילה שנבחרה.
6.  **הצגת המילה המעורבבת**:
    - `print("נחש את המילה:")`: הדפסת הודעה למשתמש.
    - `print(shuffled_word)`: הדפסת המילה המעורבבת שהמשתמש צריך לנחש.
7.  **לולאת המשחק `while True`**:
    - לולאה אינסופית, הנמשכת עד שהמשתמש מנחש נכון את המילה.
    - `user_guess = input("הכנס את הניחוש שלך: ").upper()`: קבלת קלט מהמשתמש והמרתו לאותיות רישיות.
    - **בדיקת הניחוש**:
        - `if user_guess == target_word:`: בדיקה האם הניחוש של המשתמש שווה למילה שנבחרה.
        - `print("כל הכבוד! ניחשת נכון!")`: הדפסת הודעת ניצחון אם הניחוש נכון.
        - `break`: סיום הלולאה (והמשחק) אם הניחוש נכון.
    - `else:`: אם הניחוש לא נכון, ההודעה "ניסיון נוסף..." תוצג והלולאה תמשיך.

"""
```
