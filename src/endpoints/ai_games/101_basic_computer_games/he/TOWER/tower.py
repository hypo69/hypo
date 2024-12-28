<TOWER>:
=================
קושי: 5
-----------------
המשחק "מגדל" הוא משחק טקסטואלי בו השחקן בונה מגדל על ידי הזנת מספרים. כל מספר שיוזן על ידי השחקן יתווסף לגובה המגדל. מטרת המשחק היא לבנות מגדל גבוה ככל האפשר, כאשר המשחק מסתיים לאחר 10 מהלכים או כאשר השחקן מזין מספר שאינו חיובי.
חוקי המשחק:
1. המשחק מתחיל עם גובה מגדל של 0.
2. בכל מהלך, השחקן מזין מספר חיובי.
3. המספר שהוזן מתווסף לגובה המגדל.
4. המשחק מסתיים לאחר 10 מהלכים, או אם הוזן מספר לא חיובי.
5. בסיום המשחק מוצג גובה המגדל הסופי.
-----------------
אלגוריתם:
1. אתחל את גובה המגדל (towerHeight) ל-0.
2. אתחל את מונה המהלכים (moves) ל-0.
3. התחל לולאה שתרוץ עד 10 מהלכים או עד שהשחקן יכניס מספר לא חיובי:
   3.1 הגדל את מונה המהלכים ב-1.
   3.2 בקש מהשחקן להזין מספר (heightToAdd).
   3.3 אם המספר (heightToAdd) הוא שלילי או אפס, צא מהלולאה.
   3.4 הוסף את המספר (heightToAdd) לגובה המגדל (towerHeight).
4. הצג את גובה המגדל הסופי.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    towerHeight = 0
    moves = 0
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: <code><b>moves < 10</b></code>"}
    LoopStart -- כן --> IncreaseMoves["<code><b>moves = moves + 1</b></code>"]
    IncreaseMoves --> InputHeight["קלט מספר מהמשתמש: <code><b>heightToAdd</b></code>"]
    InputHeight --> CheckHeight{"בדיקה: <code><b>heightToAdd <= 0?</b></code>"}
    CheckHeight -- כן --> OutputTowerHeight["הצגת הודעה: <b>TOWER HEIGHT IS <code>{towerHeight}</code></b>"]
    OutputTowerHeight --> End["סוף"]
    CheckHeight -- לא --> AddToTowerHeight["<code><b>towerHeight = towerHeight + heightToAdd</b></code>"]
    AddToTowerHeight --> LoopStart
    LoopStart -- לא --> OutputTowerHeight
    
```
Legenda:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: towerHeight (גובה המגדל) מאותחל ל-0, ו-moves (מונה מהלכים) מאותחל ל-0.
    LoopStart - תחילת הלולאה, הממשיכה כל עוד מספר המהלכים קטן מ-10.
    IncreaseMoves - הגדלת מונה המהלכים ב-1.
    InputHeight - קלט מספר מהמשתמש ושמירתו במשתנה heightToAdd.
    CheckHeight - בדיקה האם המספר שהוזן קטן או שווה ל-0.
    OutputTowerHeight - הצגת הודעת גובה המגדל הסופי.
    End - סוף התוכנית.
    AddToTowerHeight - הוספת המספר שהוזן לגובה המגדל.
"""
```python
# אתחול גובה המגדל
towerHeight = 0
# אתחול מונה המהלכים
moves = 0

# לולאה ראשית של המשחק
while moves < 10:
    # הגדלת מונה המהלכים
    moves += 1
    # קלט מהמשתמש
    try:
        heightToAdd = int(input("הזן מספר חיובי להוספה לגובה המגדל (0 או שלילי לסיום): "))
    except ValueError:
        print("קלט לא תקין, אנא הזן מספר שלם.")
        continue
    # בדיקה אם הקלט שלילי או 0, סיום המשחק אם כן
    if heightToAdd <= 0:
        break
    # הוספת הקלט לגובה המגדל
    towerHeight += heightToAdd

# הצגת גובה המגדל הסופי
print(f"גובה המגדל הסופי הוא: {towerHeight}")

```
<הערות סיום>
הסבר מפורט לקוד:
1. **אתחול משתנים:**
    - `towerHeight = 0`: משתנה המאחסן את גובה המגדל הנוכחי, מתחיל מ-0.
    - `moves = 0`: משתנה המאחסן את מספר המהלכים שבוצעו במשחק, מתחיל מ-0.
2. **לולאת המשחק:**
    - `while moves < 10:`: לולאה שתמשיך עד שבוצעו 10 מהלכים, או עד שהמשתמש יזין מספר לא חיובי.
        - `moves += 1`: בכל איטרציה של הלולאה, מונה המהלכים גדל ב-1.
        - **קבלת קלט מהמשתמש:**
            - `try...except ValueError`: בלוק זה מטפל בשגיאות קלט אפשריות, במקרה שהמשתמש מזין קלט שאינו מספר.
            - `heightToAdd = int(input(...))`: מוצגת בקשה למשתמש להזין מספר שלם חיובי להוספה למגדל. הקלט מומר למספר שלם.
        - **בדיקת סיום:**
            - `if heightToAdd <= 0:`: בדיקה האם המספר שהוזן קטן או שווה ל-0, מה שמסמן סיום המשחק.
                - `break`: יציאה מהלולאה אם התנאי מתקיים.
        - **עדכון גובה המגדל:**
            - `towerHeight += heightToAdd`: הוספת הערך שהוזן על ידי המשתמש לגובה המגדל.
3. **הצגת תוצאה:**
    - `print(f"גובה המגדל הסופי הוא: {towerHeight}")`: הצגת גובה המגדל הסופי לאחר סיום המשחק.
</הערות סיום>
