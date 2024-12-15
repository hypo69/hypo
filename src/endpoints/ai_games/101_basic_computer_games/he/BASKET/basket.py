<BASKET>:
=================
קושי: 2
-----------------
המשחק <BASKET> הוא סימולציה פשוטה של משחק כדורסל, בו השחקן מנסה לקלוע לסל תוך התחשבות במרחק הסל. המטרה היא לצבור את מירב הנקודות האפשריות. לאחר כל זריקה, מוצג המרחק לסל, והשחקן מקבל מידע אם הזריקה קלעה לסל או לא, וגם כמה נקודות צבר. המשחק מסתיים לאחר 10 זריקות.

חוקי המשחק:
1. השחקן מבצע 10 זריקות לסל.
2. בכל זריקה, המרחק לסל (מרחק אקראי) מוצג לשחקן.
3. השחקן מנסה לקלוע לסל בהתאם למרחק.
4. קליעה לסל מזכה בנקודות (10 נקודות).
5. בסוף המשחק מוצג סיכום של מספר הזריקות, מספר הקליעות והניקוד הכולל.

-----------------
אלגוריתם:
1. אתחל את משתנה מספר הזריקות (numberOfShots) ל-0.
2. אתחל את משתנה מספר הקליעות (numberOfHits) ל-0.
3. אתחל את משתנה הניקוד (score) ל-0.
4. התחל לולאה שתרוץ 10 פעמים (כל זריקה):
    4.1. הגדל את מספר הזריקות ב-1.
    4.2. צור מרחק אקראי לסל בין 1 ל-100 (basketDistance).
    4.3. הצג למשתמש את המרחק לסל.
    4.4. צור מספר אקראי נוסף בין 1 ל-100 (randomShot).
    4.5. אם המספר האקראי (randomShot) קטן מהמרחק לסל (basketDistance)  ב-30,
            אז קליעה (הוסף 1 למספר הקליעות, והוסף 10 לניקוד), והצג "HIT!".
         אחרת, אם לא קלע, הצג "MISS!".
5. סוף הלולאה.
6. הצג למשתמש סיכום תוצאות המשחק:
   - סך כל הזריקות
   - סך כל הקליעות
   - הניקוד הסופי
7. סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    numberOfShots = 0<br>
    numberOfHits = 0<br>
    score = 0<br>
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: numberOfShots < 10"}
    LoopStart -- כן --> IncreaseShots["<code><b>numberOfShots = numberOfShots + 1</b></code>"]
    IncreaseShots --> GenerateDistance["<code><b>basketDistance = random(1, 100)</b></code>"]
    GenerateDistance --> OutputDistance["הצגת מרחק: <b>basketDistance</b>"]
    OutputDistance --> GenerateRandomShot["<code><b>randomShot = random(1, 100)</b></code>"]
    GenerateRandomShot --> CheckHit{"בדיקה: <code><b>randomShot <= basketDistance - 30</b></code>?"}
    CheckHit -- כן --> IncreaseHits["<code><b>numberOfHits = numberOfHits + 1<br> score = score + 10</b></code>"]
    IncreaseHits --> OutputHit["הצגת הודעה: <b>HIT!</b>"]
    OutputHit --> LoopStart
    CheckHit -- לא --> OutputMiss["הצגת הודעה: <b>MISS!</b>"]
    OutputMiss --> LoopStart
    LoopStart -- לא --> OutputResults["<p align='left'>הצגת תוצאות:<br>
    Total Shots: <b>numberOfShots</b><br>
    Total Hits: <b>numberOfHits</b><br>
    Total Score: <b>score</b></p>"]
    OutputResults --> End["סוף"]
```
Legenda:
  Start - תחילת המשחק.
  InitializeVariables - אתחול משתנים: numberOfShots (מספר הזריקות), numberOfHits (מספר הקליעות), ו-score (הניקוד) ל-0.
  LoopStart - תחילת הלולאה, הממשיכה כל עוד מספר הזריקות קטן מ-10.
  IncreaseShots - הגדלת מונה הזריקות ב-1.
  GenerateDistance - יצירת מרחק אקראי לסל בין 1 ל-100.
  OutputDistance - הצגת המרחק לסל.
  GenerateRandomShot - יצירת מספר אקראי נוסף בין 1 ל-100.
  CheckHit - בדיקה האם המספר האקראי קטן או שווה למרחק פחות 30 (האם הזריקה קלעה).
  IncreaseHits - אם קלעה, הגדלת מונה הקליעות ב-1 והגדלת הניקוד ב-10.
  OutputHit - הצגת הודעה "HIT!" אם הזריקה קלעה.
  OutputMiss - הצגת הודעה "MISS!" אם הזריקה לא קלעה.
  OutputResults - הצגת סיכום תוצאות המשחק (סך הזריקות, סך הקליעות והניקוד הכולל).
  End - סוף המשחק.
"""
import random

# אתחול מספר הזריקות, מספר הקליעות והניקוד
numberOfShots = 0
numberOfHits = 0
score = 0

# לולאה ראשית של המשחק (10 זריקות)
for _ in range(10):
    # הגדלת מונה הזריקות
    numberOfShots += 1

    # יצירת מרחק אקראי לסל בין 1 ל-100
    basketDistance = random.randint(1, 100)
    print(f"מרחק לסל: {basketDistance}")

    # יצירת מספר אקראי נוסף בין 1 ל-100 עבור סימולציית הזריקה
    randomShot = random.randint(1, 100)
    
    # בדיקה האם הזריקה הצליחה (המספר האקראי צריך להיות נמוך מהמרחק פחות 30)
    if randomShot <= basketDistance - 30:
        print("HIT!")
        numberOfHits += 1  # הגדלת מונה הקליעות
        score += 10  # הוספת 10 נקודות לניקוד
    else:
        print("MISS!")
        
# הדפסת סיכום תוצאות המשחק
print("----- סיכום משחק -----")
print(f"מספר זריקות: {numberOfShots}")
print(f"מספר קליעות: {numberOfHits}")
print(f"ניקוד כולל: {score}")

"""
הסבר הקוד:
1. **ייבוא מודול random**:
   - `import random`: ייבוא המודול random לצורך יצירת מספרים אקראיים.

2. **אתחול משתנים**:
   - `numberOfShots = 0`: אתחול משתנה לספירת מספר הזריקות.
   - `numberOfHits = 0`: אתחול משתנה לספירת מספר הקליעות.
   - `score = 0`: אתחול משתנה לספירת הניקוד הכולל.

3. **לולאת המשחק הראשית (for _ in range(10))**:
   - לולאה שרצה 10 פעמים, פעם אחת לכל זריקה.
   - `numberOfShots += 1`: בכל איטרציה, מספר הזריקות גדל ב-1.

4. **יצירת מרחק אקראי**:
   - `basketDistance = random.randint(1, 100)`: יצירת מרחק אקראי בין 1 ל-100, המייצג את המרחק לסל.
   - `print(f"מרחק לסל: {basketDistance}")`: הדפסת המרחק לשחקן.

5. **סימולציה של הזריקה**:
   - `randomShot = random.randint(1, 100)`: יצירת מספר אקראי בין 1 ל-100, המייצג את טיב הזריקה.

6. **בדיקת קליעה**:
   - `if randomShot <= basketDistance - 30:`: בדיקה האם הזריקה הצליחה. הזריקה מצליחה אם המספר האקראי קטן או שווה למרחק פחות 30. ככל שהמספר האקראי יותר קטן, כך הסיכוי לקלוע גדול יותר.
   - אם הזריקה הצליחה:
     - `print("HIT!")`: הדפסה שהזריקה קלעה.
     - `numberOfHits += 1`: הגדלת מונה הקליעות ב-1.
     - `score += 10`: הוספת 10 נקודות לניקוד.
   - אחרת:
     - `print("MISS!")`: הדפסה שהזריקה החטיאה.

7. **הצגת תוצאות**:
   - לאחר שהלולאה מסתיימת, מודפס סיכום של המשחק:
     - `print("----- סיכום משחק -----")`
     - `print(f"מספר זריקות: {numberOfShots}")`
     - `print(f"מספר קליעות: {numberOfHits}")`
     - `print(f"ניקוד כולל: {score}")`
"""
