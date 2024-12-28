# ANIMAL:
=================
קושי: 4
-----------------
משחק ANIMAL הוא משחק מילים פשוט בו המחשב בוחר באופן אקראי חיה מרשימה קבועה. השחקן מנסה לנחש את החיה על ידי הזנת אות אחת בכל פעם. המחשב שומר את האותיות שנוחשו נכון ומציג את המילה עם אותיות גלויות ואותיות מוסתרות. השחקן ממשיך לנחש עד שהוא מנחש את המילה במלואה.
חוקי המשחק:
1. המחשב בוחר באופן אקראי חיה מרשימה של 5 אותיות מרשימה קבועה.
2. השחקן מזין אות אחת בכל פעם.
3. אם האות שהוזנה נמצאת במילה, היא תוצג במקום הנכון. אם לא, לא יקרה כלום.
4. המשחק מסתיים כאשר השחקן מנחש את כל האותיות במילה.
-----------------
אלגוריתם:
1. הגדר רשימה של מילים אפשריות.
2. בחר באקראי מילה מתוך הרשימה.
3. אתחל משתנה לייצוג המילה המנוחשת, כאשר כל האותיות מוסתרות.
4. התחל לולאה "כל עוד המילה לא נוחשה במלואה":
    4.1. הצג את המילה המנוחשת עם האותיות הגלויות והמוסתרות.
    4.2. בקש מהשחקן להזין אות.
    4.3. אם האות שהוזנה נמצאת במילה שנבחרה:
        4.3.1. עדכן את המילה המנוחשת על ידי גילוי האותיות במקומות הנכונים.
5. אם המילה המנוחשת זהה למילה שנבחרה:
    5.1. הצג הודעת ניצחון והמילה המקורית.
6. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    animalList = ['LION', 'TIGER', 'HORSE', 'COW', 'GOAT']
    chosenWord = random(animalList)
    guessedWord = ['_'] * len(chosenWord)
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: כל עוד המילה לא נוחשה"}
    LoopStart -- כן --> DisplayGuessedWord["הצג את המילה המנוחשת: <code><b>guessedWord</b></code>"]
    DisplayGuessedWord --> InputLetter["קלט אות מהמשתמש: <code><b>userLetter</b></code>"]
    InputLetter --> CheckLetter{"בדיקה: <code><b>userLetter in chosenWord</b></code>?"}
    CheckLetter -- כן --> UpdateGuessedWord["עדכן את המילה המנוחשת: <code><b>guessedWord</b></code>"]
    UpdateGuessedWord --> CheckWin{"בדיקה: <code><b>guessedWord == chosenWord</b></code>?"}
    CheckWin -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT, THE WORD IS: <code>{chosenWord}</code></b>"]
    OutputWin --> End["סוף"]
    CheckWin -- לא --> LoopStart
    CheckLetter -- לא --> LoopStart
    LoopStart -- לא --> End

```
Legenda:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: animalList (רשימת החיות), chosenWord (המילה שנבחרה באקראי), ו-guessedWord (ייצוג מוסתר של המילה).
    LoopStart - תחילת הלולאה, הממשיכה כל עוד המילה לא נוחשה במלואה.
    DisplayGuessedWord - הצגת המילה המנוחשת עם אותיות גלויות ואותיות מוסתרות.
    InputLetter - קלט אות מהמשתמש.
    CheckLetter - בדיקה האם האות שהוזנה נמצאת במילה שנבחרה.
    UpdateGuessedWord - עדכון המילה המנוחשת על ידי גילוי האותיות הנכונות.
    CheckWin - בדיקה האם המילה המנוחשת זהה למילה שנבחרה.
    OutputWin - הצגת הודעת ניצחון והמילה המקורית.
    End - סוף התוכנית.
"""
import random

# רשימת החיות האפשריות
animalList = ['LION', 'TIGER', 'HORSE', 'COW', 'GOAT']

# בחירת חיה באופן אקראי מהרשימה
chosenWord = random.choice(animalList)

# יצירת רשימה של קווים תחתונים כמספר האותיות במילה, לייצוג המילה המנוחשת
guessedWord = ['_'] * len(chosenWord)

# לולאת המשחק הראשית
while True:
    # הדפסת המילה המנוחשת (עם האותיות הגלויות והמוסתרות)
    print(" ".join(guessedWord))

    # קבלת קלט מהמשתמש - אות אחת
    userLetter = input("נחש אות: ").upper()

    # בדיקה האם האות שהוזנה נמצאת במילה הנבחרת
    if userLetter in chosenWord:
        # מעבר על כל אות במילה הנבחרת
        for index, letter in enumerate(chosenWord):
             # אם האות הנוכחית במילה הנבחרת זהה לאות שהזין המשתמש
            if letter == userLetter:
                # עדכן את האות במילה המנוחשת
                guessedWord[index] = userLetter

    # בדיקה האם המילה נוחשה במלואה
    if guessedWord == list(chosenWord):
        print(f"מזל טוב! ניחשת את המילה, המילה היא: {''.join(chosenWord)}")
        break  # סיום הלולאה והמשחק אם המילה נוחשה

"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    - `import random`: ייבוא המודול `random`, המשמש לבחירת מילה אקראית.
2.  **הגדרת רשימת המילים**:
    - `animalList = ['LION', 'TIGER', 'HORSE', 'COW', 'GOAT']`: יצירת רשימה של מילים אפשריות.
3.  **בחירת מילה אקראית**:
    - `chosenWord = random.choice(animalList)`: בחירת מילה אקראית מהרשימה ושמירתה במשתנה `chosenWord`.
4.  **אתחול מילה מנוחשת**:
    - `guessedWord = ['_'] * len(chosenWord)`: יצירת רשימה המייצגת את המילה המנוחשת. בתחילה, כל האותיות מוחלפות בקו תחתון.
5.  **לולאת המשחק `while True:`**:
    - לולאה אינסופית, הממשיכה עד שהמשתמש מנחש את המילה (הפקודה `break` תסיים את הלולאה).
    - **הצגת המילה המנוחשת**:
      - `print(" ".join(guessedWord))`: הדפסת המילה המנוחשת עם רווחים בין האותיות.
    - **קבלת קלט מהמשתמש**:
      - `userLetter = input("נחש אות: ").upper()`: בקשת אות מהמשתמש, המרתה לאות גדולה ושמירתה במשתנה `userLetter`.
    - **בדיקת האות**:
      - `if userLetter in chosenWord:`: בדיקה האם האות שהזין המשתמש נמצאת במילה הנבחרת.
      - **עדכון המילה המנוחשת**:
        - `for index, letter in enumerate(chosenWord):`: מעבר על כל האותיות במילה הנבחרת, תוך קבלת האינדקס והאות.
        - `if letter == userLetter:`: בדיקה האם האות הנוכחית שווה לאות שהזין המשתמש.
        - `guessedWord[index] = userLetter`: עדכון המילה המנוחשת, גילוי האות במקום הנכון.
    - **בדיקת ניצחון**:
      - `if guessedWord == list(chosenWord):`: בדיקה האם המילה המנוחשת זהה למילה הנבחרת.
      - `print(f"מזל טוב! ניחשת את המילה, המילה היא: {''.join(chosenWord)}")`: הצגת הודעת ניצחון והמילה הנבחרת.
      - `break`: סיום הלולאה (והמשחק) אם המילה נוחשה.
"""
