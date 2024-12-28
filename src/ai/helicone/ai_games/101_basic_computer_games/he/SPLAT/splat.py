"""
SPLAT:
=================
קושי: 4
-----------------
המשחק "SPLAT" הוא משחק מזל שבו המשתמש מנסה להפיל מטוס באמצעות תותח. המשתמש מזין את הזווית והמהירות של הירי, והמשחק מדמה את מסלול הפגז. אם הפגז פוגע במטוס, המשתמש מנצח. אחרת, המטוס מתרחק.

חוקי המשחק:
1. המשתמש מזין את הזווית והמהירות של הירי.
2. המשחק מחשב את מסלול הפגז ומדמה את הפגיעה במטוס.
3. אם הפגז פוגע במטוס, המשחק מסתיים בניצחון.
4. אם הפגז לא פוגע, המטוס זז ימינה.
5. המשחק נמשך עד שהמשתמש פוגע במטוס או שהמטוס מגיע לקצה המסך.
-----------------
אלגוריתם:
1. אתחל את מיקום המטוס ל-20.
2. אתחל את מצב המשחק ל"במשחק".
3. התחל לולאה "כל עוד המשחק במשחק":
    3.1 בקש מהמשתמש להזין זווית (בין 0 ל-90 מעלות) ומהירות התחלתית (בין 0 ל-90).
    3.2 חשב את המרחק שהפגז עובר.
    3.3 אם המרחק קרוב למיקום המטוס, הצג הודעת ניצחון וסיים את המשחק.
    3.4 אחרת, אם המטוס לא הגיע לקצה המסך, הזז את המטוס ב-10 ימינה.
    3.5 אם המטוס הגיע לקצה המסך, הצג הודעת הפסד וסיים את המשחק.
4. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    planePosition = 20
    gameStatus = 'playing'
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: <code><b>gameStatus == 'playing'</b></code>"}
    LoopStart -- כן --> InputAngleVelocity["<p align='left'>קלט זווית ומהירות:
    <code><b>
    angle
    velocity
    </b></code></p>"]
    InputAngleVelocity --> CalculateDistance["חישוב מרחק הפגז: <code><b>distance</b></code>"]
    CalculateDistance --> CheckHit{"בדיקה: <code><b>distance</b></code> קרוב ל-<code><b>planePosition</b></code>?"}
    CheckHit -- כן --> OutputWin["הצגת הודעה: <b>SPLAT!!! YOU GOT IT!</b>"]
    OutputWin --> GameEnd["סוף: <code><b>gameStatus = 'end'</b></code>"]
    CheckHit -- לא --> CheckPlanePosition{"בדיקה: <code><b>planePosition</b></code> < 100?"}
    CheckPlanePosition -- כן --> MovePlane["הזזת המטוס: <code><b>planePosition = planePosition + 10</b></code>"]
    MovePlane --> LoopStart
    CheckPlanePosition -- לא --> OutputLose["הצגת הודעה: <b>YOU MISSED, PLANE FLEW AWAY</b>"]
    OutputLose --> GameEnd
    LoopStart -- לא --> End["סוף"]
    GameEnd --> End
```
Legenda:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: planePosition (מיקום המטוס) מאותחל ל-20 ו-gameStatus (מצב המשחק) מאותחל ל-"playing".
    LoopStart - תחילת הלולאה, הממשיכה כל עוד gameStatus שווה ל-"playing".
    InputAngleVelocity - קבלת קלט מהמשתמש של זווית ומהירות הירי.
    CalculateDistance - חישוב המרחק שהפגז עובר בהתבסס על הזווית והמהירות.
    CheckHit - בדיקה האם הפגז פגע במטוס (האם המרחק שהפגז עבר קרוב למיקום המטוס).
    OutputWin - הצגת הודעת ניצחון אם הפגז פגע במטוס.
    GameEnd - סיום המשחק ושינוי gameStatus ל-"end".
    CheckPlanePosition - בדיקה האם המטוס עדיין בתוך המסך (האם מיקומו קטן מ-100).
    MovePlane - הזזת המטוס ימינה ב-10 יחידות אם הוא עדיין בתוך המסך.
    OutputLose - הצגת הודעת הפסד אם המטוס הגיע לקצה המסך.
    End - סוף התוכנית.
"""
import math

# פונקציה לחישוב מרחק הפגז
def calculate_distance(angle, velocity):
    """
    פונקציה זו מחשבת את מרחק הפגז בהתבסס על זווית ומהירות ההתחלה.

    Args:
        angle: זווית השיגור במעלות.
        velocity: מהירות השיגור.

    Returns:
        float: מרחק הפגז.
    """
    # המרת הזווית מרדיאנים
    angle_rad = math.radians(angle)
    # חישוב המרחק האופקי של הפגז
    distance = (velocity ** 2 * math.sin(2 * angle_rad)) / 9.81
    return distance

# משתנה המייצג את מיקום המטוס
plane_position = 20
# מצב המשחק
game_status = 'playing'

# לולאת המשחק הראשית
while game_status == 'playing':
    # קבלת קלט מהמשתמש
    try:
        angle = float(input("הזן זווית (0-90): "))
        velocity = float(input("הזן מהירות (0-90): "))
        if not (0 <= angle <= 90) or not (0 <= velocity <= 90):
           print("הזווית והמהירות חייבות להיות בין 0 ל-90. נסה שוב.")
           continue
    except ValueError:
        print("קלט לא תקין, אנא הזן מספרים.")
        continue

    # חישוב מרחק הפגז
    distance = calculate_distance(angle, velocity)

    # בדיקה אם הפגז פגע במטוס
    if abs(distance - plane_position) < 10:  # סף הפגיעה הוא 10 יחידות
        print("SPLAT!!! YOU GOT IT!")
        game_status = 'end' # סיום המשחק
    else:
        # בדיקה אם המטוס הגיע לקצה המסך
        if plane_position < 100:
            plane_position += 10 # הזזת המטוס ימינה
        else:
             print("YOU MISSED, PLANE FLEW AWAY")
             game_status = 'end' # סיום המשחק

"""
הסבר הקוד:
1.  **ייבוא המודול `math`**:
    - `import math`: ייבוא המודול `math`, המשמש לפעולות מתמטיות כמו המרת מעלות לרדיאנים.

2.  **הפונקציה `calculate_distance(angle, velocity)`**:
    - פונקציה זו מחשבת את המרחק שהפגז יעבור בהתבסס על הזווית והמהירות ההתחלתית שלו.
    - `angle_rad = math.radians(angle)`: ממיר את הזווית ממעלות לרדיאנים.
    - `distance = (velocity ** 2 * math.sin(2 * angle_rad)) / 9.81`: מחשב את מרחק הפגז באמצעות הנוסחה הפיזיקלית.
    - הפונקציה מחזירה את המרחק המחושב.

3.  **אתחול משתנים**:
    - `plane_position = 20`: אתחול מיקום המטוס ל-20.
    - `game_status = 'playing'`: אתחול מצב המשחק ל-"playing", מצב זה מאפשר להמשך המשחק.

4.  **לולאת המשחק הראשית `while game_status == 'playing':`**:
    - לולאה זו ממשיכה כל עוד משתנה `game_status` שווה ל-"playing".
    - **קלט נתונים**:
        - `try...except ValueError`: מטפל בשגיאות קלט אפשריות.
        - `angle = float(input("הזן זווית (0-90): "))` ו-`velocity = float(input("הזן מהירות (0-90): "))`: מבקש מהמשתמש להזין זווית ומהירות, וממיר אותם למספרים עשרוניים.
        - `if not (0 <= angle <= 90) or not (0 <= velocity <= 90):`: בודק שהזווית והמהירות נמצאות בטווח המותר.
        - `continue`: אם הקלט לא תקין, חוזרים לתחילת הלולאה ומבקשים קלט חדש.
    - **חישוב מרחק הפגז**:
        - `distance = calculate_distance(angle, velocity)`: קריאה לפונקציה `calculate_distance` לחישוב מרחק הפגז.
    - **בדיקת פגיעה**:
        - `if abs(distance - plane_position) < 10:`: בודק אם מרחק הפגז קרוב למיקום המטוס (בטווח של 10 יחידות).
        - `print("SPLAT!!! YOU GOT IT!")`: אם הפגז פגע, מוצגת הודעת ניצחון.
        - `game_status = 'end'`: משנה את מצב המשחק ל-"end" כדי לסיים את הלולאה.
    - **הזזת המטוס**:
        - `else:`: אם הפגז לא פגע במטוס:
            - `if plane_position < 100:`: בודק אם המטוס עדיין בתוך המסך (מיקום קטן מ-100).
                - `plane_position += 10`: אם המטוס במסך, הוא מוזז ימינה ב-10 יחידות.
            - `else:`: אם המטוס הגיע לקצה המסך:
                - `print("YOU MISSED, PLANE FLEW AWAY")`: מוצגת הודעת הפסד.
                - `game_status = 'end'`: משנה את מצב המשחק ל-"end" כדי לסיים את הלולאה.
"""
