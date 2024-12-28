<POETRY>:
=================
קושי: 4
-----------------
משחק "שירה" הוא משחק מחשב בו המחשב בוחר מילה אקראית מתוך רשימה מוגדרת מראש, ולאחר מכן השחקן מתבקש להזין מילה נוספת, אשר מתחרזת עם המילה שנבחרה.

חוקי המשחק:
1. המחשב בוחר מילה אקראית מתוך רשימה של מילים.
2. השחקן מתבקש להזין מילה אשר מתחרזת עם המילה שנבחרה.
3. אם המילה שהוזנה מתחרזת עם המילה שנבחרה, המחשב מודיע שהשחקן צדק.
4. אם המילה שהוזנה אינה מתחרזת עם המילה שנבחרה, המחשב מודיע שהשחקן טעה.
5. המשחק מסתיים לאחר שהשחקן ניסה לנחש 5 פעמים.
-----------------
אלגוריתם:
1.  הגדר רשימה של מילים (DATA)
2.  בחר באקראי מילה מתוך הרשימה.
3.  הדפס לשחקן "YOUR WORD IS <המילה שנבחרה>".
4.  התחל לולאה, שתרוץ 5 פעמים:
    4.1. קלוט מילה מהמשתמש.
    4.2. אם המילה שהוזנה מתחרזת עם המילה הנבחרת, הדפס "RIGHT!".
    4.3. אחרת, הדפס "WRONG!".
5.  סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeWords["<p align='left'>אתחול משתנים:<br><code><b>words = [word1, word2, ...]</b></code></p>"]
    InitializeWords --> ChooseRandomWord["<p align='left'>בחירת מילה אקראית:<br><code><b>selectedWord = random(words)</b></code></p>"]
    ChooseRandomWord --> OutputWord["הצגת מילה: <b>YOUR WORD IS {selectedWord}</b>"]
    OutputWord --> LoopStart{"תחילת לולאה: 5 פעמים"}
    LoopStart -- כן --> InputWord["קלט מילה מהמשתמש: <code><b>userWord</b></code>"]
    InputWord --> CheckRhyme{"בדיקה: <code><b>isRhyme(userWord, selectedWord)?</b></code>"}
    CheckRhyme -- כן --> OutputRight["הצגת הודעה: <b>RIGHT!</b>"]
    OutputRight --> LoopEnd
    CheckRhyme -- לא --> OutputWrong["הצגת הודעה: <b>WRONG!</b>"]
    OutputWrong --> LoopEnd
    LoopEnd --> LoopStart
    LoopStart -- לא --> End["סוף"]
```

Legenda:
    Start - התחלת התוכנית.
    InitializeWords - אתחול רשימת המילים.
    ChooseRandomWord - בחירת מילה אקראית מהרשימה.
    OutputWord - הצגת המילה שנבחרה למשתמש.
    LoopStart - תחילת הלולאה שרצה 5 פעמים.
    InputWord - קליטת מילה מהמשתמש.
    CheckRhyme - בדיקה האם המילה שהוזנה מתחרזת עם המילה שנבחרה.
    OutputRight - הצגת הודעה "RIGHT!" אם המילים מתחרזות.
    OutputWrong - הצגת הודעה "WRONG!" אם המילים לא מתחרזות.
    LoopEnd - סיום איטרציה של הלולאה.
    End - סוף התוכנית.
"""
<code>
import random

# רשימת מילים
words = ["cat", "hat", "bat", "rat", "mat", "fat", "sat", "gnat"]

# בחירת מילה אקראית מהרשימה
selected_word = random.choice(words)

# הדפסת המילה הנבחרת למשתמש
print(f"YOUR WORD IS {selected_word}")

# לולאה למשחק (5 ניסיונות)
for _ in range(5):
    # קבלת מילה מהמשתמש
    user_word = input("ENTER A RHYMING WORD: ").lower()

    # בדיקה אם המילה מתחרזת
    if user_word[-2:] == selected_word[-2:]: # בדיקת התחרזות של שתי אותיות אחרונות
        print("RIGHT!") # המילה מתחרזת
    else:
        print("WRONG!") # המילה לא מתחרזת
print("Game Over")
</code>
"""
הסבר הקוד:

1. **ייבוא מודול random**:
    - `import random`: ייבוא המודול random המאפשר בחירת מילה אקראית מהרשימה.

2. **רשימת מילים**:
    - `words = ["cat", "hat", "bat", "rat", "mat", "fat", "sat", "gnat"]`: רשימה של מילים המשמשות במשחק.

3.  **בחירת מילה אקראית**:
    - `selected_word = random.choice(words)`: בחירה אקראית של מילה אחת מתוך רשימת המילים ושמירתה במשתנה `selected_word`.

4. **הדפסת המילה למשתמש**:
    - `print(f"YOUR WORD IS {selected_word}")`: הדפסת הודעה למשתמש עם המילה האקראית שנבחרה.

5.  **לולאת משחק**:
    - `for _ in range(5):`: לולאה שרצה 5 פעמים, כדי לאפשר למשתמש 5 ניסיונות לנחש מילה מתחרזת.
    - `_`: משתנה הלולאה לא בשימוש (הוא משמש כמחזיק מקום), לכן השתמשנו ב-`_`

6.  **קלט מהמשתמש**:
    - `user_word = input("ENTER A RHYMING WORD: ").lower()`: קבלת קלט מהמשתמש (המילה שהמשתמש מזין), והמרת הקלט לאותיות קטנות באמצעות `lower()` כדי לאפשר השוואה לא תלויית רישיות.

7. **בדיקת התחרזות**:
     - `if user_word[-2:] == selected_word[-2:]:`: בדיקה האם שתי האותיות האחרונות של המילה שהמשתמש הזין זהות לשתי האותיות האחרונות של המילה האקראית שנבחרה. אם כן, המילים מתחרזות.
     -`print("RIGHT!")`: אם המילים מתחרזות, יודפס "RIGHT!"
     -`else:`: אם המילים לא מתחרזות
     -`print("WRONG!")`: אם המילים לא מתחרזות, יודפס "WRONG!"

8.  **סוף המשחק**:
    - `print("Game Over")`: הודעה שמסיימת את המשחק לאחר 5 ניסיונות.
"""
