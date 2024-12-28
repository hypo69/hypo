# LIT QZ:
=================
קושי: 2
-----------------
המשחק "חידון אותיות" הוא משחק פשוט בו המחשב בוחר אות אקראית מהאלף-בית, והשחקן צריך לנחש את האות הזו. המשחק נמשך עד שהשחקן מנחש את האות הנכונה.

חוקי המשחק:
1. המחשב בוחר אות אקראית מהאלף-בית (A-Z).
2. השחקן מזין את הניחוש שלו, שהינו אות.
3. המשחק ממשיך עד שהשחקן מנחש את האות הנכונה.
4. לאחר שהשחקן ניחש נכון, המשחק מסתיים.
-----------------
אלגוריתם:
1. בחר אות אקראית מ-A עד Z.
2. התחל לולאה "כל עוד לא נוחשה האות":
    2.1 בקש מהמשתמש להזין אות.
    2.2 אם האות שהוזנה שווה לאות שנבחרה, המשחק הסתיים.
3. הצג הודעה "YOU GOT IT!"
4. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    targetLetter = random letter (A-Z)
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: כל עוד לא נוחשה האות"}
    LoopStart -- כן --> InputLetter["קלט אות מהמשתמש: <code><b>userLetter</b></code>"]
    InputLetter --> CheckLetter{"בדיקה: <code><b>userLetter == targetLetter?</b></code>"}
    CheckLetter -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT!</b>"]
    OutputWin --> End["סוף"]
    CheckLetter -- לא --> LoopStart
    LoopStart -- לא --> End
```

Legenda:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנה: targetLetter (האות המוגלה) נוצר באקראי מתוך האותיות A-Z.
    LoopStart - תחילת הלולאה, הממשיכה כל עוד האות לא נוחשה.
    InputLetter - קלט אות מהמשתמש ושמירתו במשתנה userLetter.
    CheckLetter - בדיקה האם האות שהוזנה שווה לאות המוגלה.
    OutputWin - הצגת הודעת ניצחון, אם האות נוחשה.
    End - סוף התוכנית.
"""
import random
import string

# בוחר אות אקראית מ-A עד Z
targetLetter = random.choice(string.ascii_uppercase)

# לולאה שרצה עד שהמשתמש מנחש את האות
while True:
    # בקשת קלט מהמשתמש
    userLetter = input("נחש אות מ-A עד Z: ").upper()

    # בדיקה אם האות שהוזנה שווה לאות שנבחרה
    if userLetter == targetLetter:
        print("YOU GOT IT!")
        break # סיום הלולאה אם האות נוחשה
    else:
        print("נסה שוב.") # בקשה לניסיון נוסף

"""
הסבר הקוד:
1.  **ייבוא מודולים**:
    - `import random`: ייבוא המודול random, המשמש ליצירת בחירה אקראית.
    - `import string`: ייבוא המודול string, המספק אוסף של קבועי מחרוזות, ביניהם אותיות האלף-בית באנגלית.
2.  **בחירת אות אקראית**:
    -  `targetLetter = random.choice(string.ascii_uppercase)`: בוחר אות אקראית מתוך האותיות הגדולות באנגלית (A-Z) ושומר אותה במשתנה `targetLetter`.
3.  **לולאת המשחק**:
    -  `while True:`: לולאה אינסופית שרצה עד שהמשתמש מנחש את האות הנכונה.
    -  `userLetter = input("נחש אות מ-A עד Z: ").upper()`: קולט מהמשתמש אות, וממיר אותה לאות גדולה באמצעות upper().
4.  **בדיקת ניחוש**:
    -  `if userLetter == targetLetter:`: בודק אם האות שהוזנה על ידי המשתמש שווה לאות שנבחרה.
    -   `print("YOU GOT IT!")`: אם הניחוש נכון, מדפיס הודעה.
    -   `break`: מפסיק את הלולאה (ומסיים את המשחק) כאשר האות נוחשה נכון.
    -   `else:`: אם הניחוש שגוי.
        - `print("נסה שוב.")`: מדפיס הודעה למשתמש לנסות שוב.
"""
