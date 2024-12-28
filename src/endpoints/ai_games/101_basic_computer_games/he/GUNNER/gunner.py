"""
GUNNER:
=================
קושי: 5
-----------------
"GUNNER" הוא משחק יריות פשוט בו השחקן מנסה לפגוע במטרה נעה על ידי הזנת מרחק הפגיעה. המשחק מדמה תותח יורה, המטרה נעה קדימה ואחורה בטווח מוגדר, והשחקן מנסה לפגוע במטרה.
חוקי המשחק:
1. המטרה מתחילה במיקום התחלתי, ומתחילה לנוע קדימה ואחורה.
2. השחקן מזין מרחק פגיעה, שהמשחק מפרש כמרחק שהפגז התותח עבר.
3. אם מרחק הפגיעה שווה למיקום המטרה באותו הרגע, השחקן פוגע במטרה.
4. אם המרחק שונה, השחקן לא פוגע במטרה, והמשחק ממשיך.
5. המשחק מסתיים כאשר השחקן פוגע במטרה.
-----------------
אלגוריתם:
1. אתחול משתנים: מיקום המטרה ההתחלתי (TargetLocation) ל-50, קצב תנועה (Step) ל-5, כיוון תנועה (Direction) ל-1.
2. כל עוד המטרה לא נפגעה:
    2.1 הצג את מיקום המטרה הנוכחי.
    2.2 קלוט מהמשתמש את מרחק הפגיעה (ShootDistance).
    2.3 אם מרחק הפגיעה שווה למיקום המטרה, הצג "HIT" וסיים את המשחק.
    2.4 אחרת, הצג "MISS".
    2.5 עדכן את מיקום המטרה:
        2.5.1 הוסף את קצב התנועה (Step) לכיוון התנועה (Direction) למיקום המטרה (TargetLocation).
    2.6 אם מיקום המטרה הגיע לגבולות הטווח (0 או 100):
        2.6.1 שנה את כיוון התנועה (Direction) למינוס הכיוון הנוכחי.
3. סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
        <code><b>
            targetLocation = 50<br>
            step = 5<br>
            direction = 1
        </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: כל עוד המטרה לא נפגעה"}
    LoopStart -- כן --> OutputTargetLocation["הצג מיקום מטרה: <code><b>{targetLocation}</b></code>"]
    OutputTargetLocation --> InputShootDistance["קלט מרחק פגיעה: <code><b>shootDistance</b></code>"]
    InputShootDistance --> CheckHit{"בדיקה: <code><b>shootDistance == targetLocation?</b></code>"}
    CheckHit -- כן --> OutputHit["הצג: <b>HIT</b>"]
    OutputHit --> End["סוף"]
    CheckHit -- לא --> OutputMiss["הצג: <b>MISS</b>"]
    OutputMiss --> UpdateTargetLocation["עדכן מיקום מטרה: <code><b>targetLocation = targetLocation + step * direction</b></code>"]
    UpdateTargetLocation --> CheckBoundaries{"בדיקה: <code><b>targetLocation <= 0 or targetLocation >= 100?</b></code>"}
    CheckBoundaries -- כן --> ChangeDirection["שנה כיוון: <code><b>direction = -direction</b></code>"]
    ChangeDirection --> LoopStart
     CheckBoundaries -- לא --> LoopStart
    LoopStart -- לא --> End
```
Legenda:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: targetLocation (מיקום המטרה) ל-50, step (קצב התנועה) ל-5, direction (כיוון התנועה) ל-1.
    LoopStart - תחילת הלולאה, הממשיכה כל עוד המטרה לא נפגעה.
    OutputTargetLocation - הצגת מיקום המטרה הנוכחי למשתמש.
    InputShootDistance - קלט מרחק הפגיעה מהמשתמש.
    CheckHit - בדיקה האם מרחק הפגיעה שווה למיקום המטרה.
    OutputHit - הצגת הודעת "HIT", אם הפגיעה מוצלחת.
    End - סוף התוכנית.
    OutputMiss - הצגת הודעת "MISS", אם הפגיעה לא מוצלחת.
    UpdateTargetLocation - עדכון מיקום המטרה על ידי הוספת קצב התנועה כפול כיוון התנועה.
    CheckBoundaries - בדיקה האם מיקום המטרה הגיע לגבולות הטווח (0 או 100).
    ChangeDirection - שינוי כיוון התנועה של המטרה.
"""
import random

# אתחול מיקום המטרה, קצב התנועה וכיוון התנועה
targetLocation = 50  # מיקום המטרה ההתחלתי
step = 5  # קצב התנועה של המטרה
direction = 1  # כיוון התנועה של המטרה (1 - ימינה, -1 - שמאלה)

# לולאה ראשית של המשחק
while True:
    # הצגת מיקום המטרה הנוכחי
    print("מיקום המטרה:", targetLocation)

    # קלט מרחק הפגיעה מהמשתמש
    try:
      shootDistance = int(input("הזן מרחק פגיעה: "))
    except ValueError:
        print("אנא הזן מספר שלם.")
        continue


    # בדיקה האם הפגיעה הצליחה
    if shootDistance == targetLocation:
        print("פגיעה!")
        break  # יציאה מהלולאה אם הפגיעה הצליחה
    else:
        print("החטאה.")

    # עדכון מיקום המטרה
    targetLocation += step * direction

    # בדיקה אם המטרה הגיעה לקצה הטווח
    if targetLocation <= 0 or targetLocation >= 100:
        direction *= -1  # שינוי כיוון התנועה

"""
הסבר הקוד:
1.  **ייבוא מודול `random` (לא בשימוש במשחק הזה):**
  - `import random`: מודול זה יובא לצורך דוגמה של משחק אחר, אך אינו בשימוש כאן.
2.  **אתחול משתנים:**
   - `targetLocation = 50`: הגדרת מיקום המטרה ההתחלתי ל-50 (באמצע הטווח).
   - `step = 5`: הגדרת קצב התנועה של המטרה (בכל צעד היא תזוז ב-5 יחידות).
   - `direction = 1`: הגדרת כיוון התנועה ההתחלתי של המטרה (1 - ימינה, -1 - שמאלה).
3.  **לולאת המשחק `while True:`:**
    - לולאה אינסופית שרצה עד שהמשתמש פוגע במטרה (ואז יוצאים מהלולאה עם `break`).
    - `print("מיקום המטרה:", targetLocation)`: הדפסת המיקום הנוכחי של המטרה למסך.
    - `shootDistance = int(input("הזן מרחק פגיעה: "))`: קבלת קלט מהמשתמש (מרחק הפגיעה) והמרתו למספר שלם.
    - **בדיקת פגיעה:**
        - `if shootDistance == targetLocation:`: בדיקה האם מרחק הפגיעה שווה למיקום המטרה.
        - `print("פגיעה!")`: אם הפגיעה הצליחה, מדפיסים הודעה מתאימה.
        - `break`: יציאה מהלולאה, סיום המשחק.
        -`else:`: אם מרחק הפגיעה אינו תואם למיקום המטרה, מדפיסים "החטאה".
    - **עדכון מיקום המטרה:**
        - `targetLocation += step * direction`: עדכון מיקום המטרה. המיקום החדש הוא המיקום הנוכחי ועוד קצב התנועה (5) כפול כיוון התנועה (1 או -1).
    - **שינוי כיוון המטרה:**
        -`if targetLocation <= 0 or targetLocation >= 100:`: בדיקה האם המטרה הגיעה לגבולות המסך (0 או 100).
        -`direction *= -1`: אם המטרה הגיעה לקצה הטווח, הכיוון משתנה (מ-1 ל--1 או להפך).
"""
