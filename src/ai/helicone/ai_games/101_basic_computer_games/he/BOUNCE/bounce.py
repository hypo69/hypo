"""
<BOUNCE>:
=================
קושי: 2
-----------------
המשחק "BOUNCE" מדמה כדור קופץ על מסך, נע מצד לצד ומשנה כיוון כשהוא פוגע בקצוות המסך. הוא מציג סימון של הכדור על ידי '*' במסך המורכב מרווחים. מהירות הכדור ניתנת לשינוי באמצעות קלט מהמשתמש. המשחק נמשך עד שהמשתמש בוחר לסיים.
חוקי המשחק:
1. הכדור מתחיל בתנועה אופקית, כאשר הוא מיוצג על ידי התו *.
2. הכדור נע במסך שרוחבו קבוע (40 עמודות) וקופץ מהקצוות.
3. המשתמש יכול לשנות את מהירות הכדור על ידי הזנת ערך חדש בכל שלב של המשחק.
4. אם המשתמש יזין מהירות 0, המשחק יסתיים.
5. המשחק מתבצע בלולאה אינסופית עד שהמשתמש יחליט לסיים.
-----------------
אלגוריתם:
1. הגדר את מיקום הכדור ההתחלתי ל-2.
2. הגדר את כיוון התנועה ההתחלתי ל-1 (ימינה).
3. הגדר את מהירות הכדור ההתחלתית ל-1.
4. התחל לולאה אינסופית:
    4.1. צור מחרוזת של 40 רווחים.
    4.2. החלף את הרווח במיקום הכדור בכוכבית (*).
    4.3. הצג את המחרוזת.
    4.4. בקש מהמשתמש להזין מהירות חדשה (אם יזין 0, צא מהלולאה).
    4.5. שנה את כיוון התנועה אם הכדור פוגע באחד מקצוות המסך.
    4.6. שנה את מיקום הכדור בהתאם לכיוון ולמהירות.
5. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
        <code><b>
        ballPosition = 2<br>
        ballDirection = 1<br>
        ballSpeed = 1<br>
        screenWidth = 40
        </b></code></p>"]
    InitializeVariables --> MainLoopStart{"תחילת לולאה ראשית"}
    MainLoopStart --> CreateScreen["יצירת מחרוזת רווחים بطول 40"]
    CreateScreen --> DrawBall["הצבת כוכבית (*) במיקום הכדור"]
    DrawBall --> DisplayScreen["הצגת המסך"]
    DisplayScreen --> InputSpeed["קלט מהירות חדשה מהמשתמש: <code><b>newSpeed</b></code>"]
    InputSpeed --> CheckExit{"בדיקה: <code><b>newSpeed == 0</b></code>?"}
    CheckExit -- כן --> End["סוף"]
    CheckExit -- לא --> UpdateSpeed["<code><b>ballSpeed = newSpeed</b></code>"]
    UpdateSpeed --> CheckBoundaries{"בדיקה: האם הכדור בקצה המסך?"}
    CheckBoundaries -- כן --> ChangeDirection["<code><b>ballDirection = -ballDirection</b></code>"]
    ChangeDirection --> UpdatePosition["<code><b>ballPosition = ballPosition + ballSpeed * ballDirection</b></code>"]
    UpdatePosition --> MainLoopStart
    CheckBoundaries -- לא --> UpdatePosition
```
Legenda:
    Start - תחילת התוכנית.
    InitializeVariables - אתחול משתנים: ballPosition (מיקום הכדור) ל-2, ballDirection (כיוון הכדור) ל-1, ballSpeed (מהירות הכדור) ל-1, screenWidth (רוחב המסך) ל-40.
    MainLoopStart - תחילת הלולאה הראשית של המשחק.
    CreateScreen - יצירת מחרוזת המכילה 40 רווחים לייצוג המסך.
    DrawBall - הצבת הכוכבית (*) במחרוזת הרווחים במיקום הנוכחי של הכדור.
    DisplayScreen - הצגת המסך המעודכן.
    InputSpeed - קבלת מהירות חדשה מהמשתמש.
    CheckExit - בדיקה האם המהירות החדשה היא 0, אם כן, המשחק מסתיים.
    UpdateSpeed - עדכון מהירות הכדור למהירות החדשה שהוזנה.
    CheckBoundaries - בדיקה האם הכדור הגיע לקצה המסך.
    ChangeDirection - שינוי כיוון התנועה של הכדור.
    UpdatePosition - עדכון מיקום הכדור בהתאם לכיוון ולמהירות.
    End - סוף התוכנית.
"""
import time

# הגדרת רוחב המסך
screenWidth = 40
# הגדרת מיקום התחלתי של הכדור
ballPosition = 2
# הגדרת כיוון התחלתי של הכדור (1 = ימינה, -1 = שמאלה)
ballDirection = 1
# הגדרת מהירות התחלתית של הכדור
ballSpeed = 1

# לולאת משחק אינסופית
while True:
    # יצירת מחרוזת רווחים לייצוג המסך
    screen = " " * screenWidth
    # החלפת הרווח במיקום הכדור בכוכבית
    screen = screen[:ballPosition] + "*" + screen[ballPosition + 1:]
    # הצגת המסך
    print(screen)
    # בקשת מהירות חדשה מהמשתמש
    try:
        newSpeed = int(input("הזן מהירות חדשה (0 לצאת): "))
    except ValueError:
         print("אנא הזן מספר שלם.")
         continue
    # אם המשתמש הזין 0, סיום המשחק
    if newSpeed == 0:
        break
    # עדכון מהירות הכדור
    ballSpeed = newSpeed

    # בדיקה האם הכדור הגיע לקצה המסך
    if ballPosition <= 0 or ballPosition >= screenWidth - 1:
        # שינוי כיוון התנועה של הכדור
        ballDirection = -ballDirection

    # עדכון מיקום הכדור
    ballPosition += ballSpeed * ballDirection
    # השהיה קצרה בין כל איטרציה
    time.sleep(0.1)

"""
הסבר הקוד:
1.  **ייבוא המודול `time`**:
    - `import time`: ייבוא המודול `time` המשמש להשהיית התוכנית בין כל איטרציה, כדי לשלוט בקצב המשחק.
2.  **הגדרת משתנים**:
    - `screenWidth = 40`: קובע את רוחב המסך ל-40 תווים.
    - `ballPosition = 2`: מגדיר את המיקום ההתחלתי של הכדור על המסך.
    - `ballDirection = 1`: מגדיר את כיוון התנועה ההתחלתי של הכדור (1 לימין, -1 לשמאל).
    - `ballSpeed = 1`: מגדיר את מהירות התנועה ההתחלתית של הכדור.
3.  **לולאת משחק `while True:`**:
    - לולאה אינסופית המאפשרת למשחק להימשך עד שהמשתמש בוחר לסיים.
    - `screen = " " * screenWidth`: יצירת מחרוזת של רווחים, המייצגת את המסך.
    - `screen = screen[:ballPosition] + "*" + screen[ballPosition + 1:]`: החלפת הרווח במקום בו נמצא הכדור בכוכבית, כדי לצייר את הכדור.
    - `print(screen)`: הדפסת המסך עם הכדור במקומו הנוכחי.
    - **קבלת קלט משתמש**:
        - `try...except ValueError`: בלוק לטיפול בשגיאות קלט מהמשתמש, אם המשתמש מזין קלט שאינו מספר שלם.
        - `newSpeed = int(input("הזן מהירות חדשה (0 לצאת): "))`: קבלת מהירות חדשה מהמשתמש.
    - **יציאה מהלולאה**:
        - `if newSpeed == 0:`: בדיקה האם המשתמש הזין 0, אם כן, סיום המשחק.
        - `break`: יציאה מהלולאה, אם המשתמש הזין 0.
    - **עדכון מהירות**:
        - `ballSpeed = newSpeed`: עדכון מהירות הכדור למהירות החדשה שהוזנה על ידי המשתמש.
    - **בדיקת גבולות**:
        - `if ballPosition <= 0 or ballPosition >= screenWidth - 1:`: בדיקה האם הכדור הגיע לקצה המסך.
        - `ballDirection = -ballDirection`: שינוי כיוון הכדור, אם הוא הגיע לקצה המסך.
    - **עדכון מיקום**:
        - `ballPosition += ballSpeed * ballDirection`: עדכון מיקום הכדור בהתאם לכיוון ולמהירות.
    - `time.sleep(0.1)`: השהייה קצרה בין איטרציות, כדי לשלוט בקצב המשחק.
"""
