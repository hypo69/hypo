<GOLF>:
=================
קושי: 4
-----------------
המשחק GOLF הוא משחק מחשב פשוט המדמה משחק גולף. השחקן מזין מרחק וחובט, והמטרה היא להגיע לחור במינימום חבטות. המשחק מציג מרחק לחור, ומשתמש במספרים אקראיים כדי לדמות את הטעויות האפשריות בכל חבטה.

חוקי המשחק:
1. המטרה היא להכניס את הכדור לחור.
2. המרחק לחור מוצג בתחילת המשחק.
3. השחקן מזין את המרחק שהוא רוצה לחבוט.
4. המחשב מחשב את המרחק האמיתי שהכדור עבר (ישנה סטייה אקראית).
5. המשחק ממשיך עד שהשחקן מגיע לחור.
6. מספר החבטות מחושב ומוצג בסוף המשחק.
-----------------
אלגוריתם:
1. הגדר את המרחק לחור (במקרה זה 400 יחידות).
2. אתחל את מספר החבטות ל-0.
3. התחל לולאה שרצה כל עוד המרחק לחור גדול מ-0:
    3.1. הצג לשחקן את המרחק לחור.
    3.2. קבל מהשחקן קלט של מרחק החבטה הרצוי.
    3.3. הגדל את מספר החבטות ב-1.
    3.4. חשב את המרחק האמיתי שהכדור עבר - ערך החבטה עם סטייה אקראית בין -20 ל-20.
    3.5. הפחת את המרחק שעבר הכדור מהמרחק לחור.
    3.6. אם המרחק לחור קטן או שווה ל-0, צא מהלולאה.
4. הצג לשחקן הודעה שהוא הגיע לחור, ובכמה חבטות.
5. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    distanceToHole = 400
    numberOfHits = 0
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: כל עוד המרחק לחור > 0"}
    LoopStart -- כן --> DisplayDistance["הצג מרחק לחור: <code><b>distanceToHole</b></code>"]
    DisplayDistance --> InputHitDistance["קלט מרחק חבטה מהמשתמש: <code><b>hitDistance</b></code>"]
    InputHitDistance --> IncreaseHits["<code><b>numberOfHits = numberOfHits + 1</b></code>"]
    IncreaseHits --> CalculateRealDistance["חישוב מרחק אמיתי: <code><b>realDistance = hitDistance + random(-20, 20)</b></code>"]
    CalculateRealDistance --> UpdateDistanceToHole["<code><b>distanceToHole = distanceToHole - realDistance</b></code>"]
    UpdateDistanceToHole --> CheckHole{"בדיקה: <code><b>distanceToHole <= 0?</b></code>"}
    CheckHole -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT IN <code>{numberOfHits}</code> HITS!</b>"]
    OutputWin --> End["סוף"]
    CheckHole -- לא --> LoopStart
    LoopStart -- לא --> End
```

Legenda:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: distanceToHole (מרחק לחור) מאותחל ל-400, ו-numberOfHits (מספר החבטות) מאותחל ל-0.
    LoopStart - תחילת הלולאה, הממשיכה כל עוד המרחק לחור גדול מ-0.
    DisplayDistance - הצגת המרחק הנוכחי לחור.
    InputHitDistance - קלט מרחק חבטה רצוי מהמשתמש ושמירתו במשתנה hitDistance.
    IncreaseHits - הגדלת מונה החבטות ב-1.
    CalculateRealDistance - חישוב המרחק האמיתי שהכדור עבר, תוך הוספת סטייה אקראית (בין -20 ל-20) למרחק המבוקש.
    UpdateDistanceToHole - עדכון המרחק לחור על ידי הפחתת המרחק האמיתי מהמרחק הקיים.
    CheckHole - בדיקה האם הכדור הגיע לחור (המרחק לחור קטן או שווה ל-0).
    OutputWin - הצגת הודעת ניצחון, אם הכדור הגיע לחור, עם מספר החבטות.
    End - סוף התוכנית.
"""
```python
import random

# מרחק לחור
distanceToHole = 400
# מונה חבטות
numberOfHits = 0

# לולאה ראשית של המשחק
while distanceToHole > 0:
    # הצגת המרחק לחור לשחקן
    print("מרחק לחור:", distanceToHole)

    # קבלת קלט מהמשתמש - מרחק החבטה
    try:
        hitDistance = int(input("מרחק החבטה הרצוי: "))
    except ValueError:
        print("אנא הזן מספר שלם.")
        continue

    # הגדלת מספר החבטות
    numberOfHits += 1

    # חישוב המרחק האמיתי עם סטיה אקראית
    realDistance = hitDistance + random.randint(-20, 20)

    # עדכון המרחק לחור
    distanceToHole -= realDistance
    
    # אם המרחק קטן או שווה ל-0, הגענו לחור.
    if distanceToHole <= 0:
       print(f"הגעת לחור ב-{numberOfHits} חבטות!")

```
<הסברים>
הסבר הקוד:

1.  **ייבוא המודול `random`**:
    -   `import random`: ייבוא המודול random, המשמש ליצירת מספרים אקראיים.
2.  **אתחול משתנים**:
    -   `distanceToHole = 400`: אתחול המרחק לחור ל-400 יחידות.
    -   `numberOfHits = 0`: אתחול מונה החבטות ל-0.
3.  **לולאת המשחק `while distanceToHole > 0:`**:
    -   לולאה שמתקיימת כל עוד המרחק לחור גדול מאפס.
    -   `print("מרחק לחור:", distanceToHole)`: הצגת המרחק הנוכחי לחור לשחקן.
    -   **קלט נתונים**:
        -  `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין משהו שאינו מספר שלם, יוצג הודעת שגיאה.
        -   `hitDistance = int(input("מרחק החבטה הרצוי: "))`: קבלת קלט מהמשתמש - מרחק החבטה הרצוי, והמרתו למספר שלם.
    -   `numberOfHits += 1`: הגדלת מונה החבטות באחד.
    -   `realDistance = hitDistance + random.randint(-20, 20)`: חישוב המרחק האמיתי שהכדור עבר. המרחק האמיתי הוא המרחק שהמשתמש הזין בתוספת מספר אקראי בין -20 ל-20, שמדמה סטיה.
    -   `distanceToHole -= realDistance`: עדכון המרחק לחור על ידי הפחתת המרחק האמיתי ממנו.
    -   **תנאי סיום**:
        -   `if distanceToHole <= 0:`: בדיקה האם הכדור הגיע לחור (המרחק קטן או שווה לאפס).
        -   `print(f"הגעת לחור ב-{numberOfHits} חבטות!")`: הצגת הודעה שהמשחק הסתיים, עם מספר החבטות.
</הסברים>
