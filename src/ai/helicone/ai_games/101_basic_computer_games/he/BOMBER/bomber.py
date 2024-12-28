<BOMBER>:
=================
קושי: 5
-----------------
במשחק "מפציץ" השחקן צריך להפציץ מטרה נייחת על ידי הזנת זווית ומהירות התחלתית לפגז. המטרה ממוקמת במרחק קבוע. לאחר כל ניסיון, המשחק מחשב את מסלול הפגז ומציג את המרחק בו הפגז פגע ואת המרחק עד למטרה. השחקן צריך לכוון את הזווית והמהירות שלו כדי לפגוע במטרה במרחק מסוים.

חוקי המשחק:
1. המטרה ממוקמת במרחק של 1000 יחידות מהתותח.
2. השחקן מזין זווית ומהירות התחלתית לפגז.
3. המשחק מחשב את המרחק אליו הפגז יגיע על ידי חישוב מסלול בליסטי פשוט (התנגדות אוויר אינה נלקחת בחשבון).
4. המשחק מציג את מרחק הפגיעה של הפגז ואת המרחק בין הפגיעה למטרה.
5. המשחק נמשך עד שהשחקן פוגע במטרה או עד שמספר הניסיונות מגיע ל-10.
6. הפגיעה מוגדרת כהפרש בין מיקום הפגז למיקום המטרה קטן מ-1.

-----------------
אלגוריתם:
1. אתחל את המשתנה `targetDistance` (מרחק המטרה) ל-1000.
2. אתחל את המשתנה `numberOfAttempts` (מספר הניסיונות) ל-0.
3. התחל לולאה "כל עוד מספר הניסיונות קטן מ-10":
    3.1. הגדל את מספר הניסיונות ב-1.
    3.2. בקש מהמשתמש להזין זווית התחלתית (במעלות) ומהירות התחלתית לפגז.
    3.3. המר את הזווית לרדיאנים.
    3.4. חשב את מרחק הפגיעה של הפגז באמצעות הנוסחה:
       `distance = (2 * velocity**2 * sin(angle) * cos(angle)) / gravity`
       כאשר:
          - `velocity` היא המהירות התחלתית של הפגז.
          - `angle` היא הזווית ההתחלתית ברדיאנים.
          - `gravity` היא קבוע הכבידה, מוגדר כ-32.2.
    3.5. חשב את ההפרש בין מרחק הפגיעה למרחק המטרה:
        `distanceToTarget = abs(distance - targetDistance)`
    3.6. הצג את מרחק הפגיעה של הפגז, ואת המרחק בין הפגיעה למטרה.
    3.7. אם המרחק בין הפגיעה למטרה קטן מ-1, הודע "HIT" וצא מהלולאה.
4. אם הלולאה הסתיימה (בגלל ש-10 ניסיונות מוצו) והפגיעה לא הושגה, הודע "YOU MISSED!".
5. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    targetDistance = 1000<br>
    numberOfAttempts = 0<br>
    gravity = 32.2
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: numberOfAttempts < 10"}
    LoopStart -- כן --> IncreaseAttempts["<code><b>numberOfAttempts = numberOfAttempts + 1</b></code>"]
    IncreaseAttempts --> InputValues["קלט מהמשתמש:<br><code><b>initialAngle</b></code> (במעלות) <br><code><b>initialVelocity</b></code>"]
    InputValues --> AngleToRadians["<p align='left'> המרת זווית למעלות לרדיאנים:
    <code><b>angleInRadians = initialAngle * PI / 180</b></code></p>"]
    AngleToRadians --> CalculateDistance["<p align='left'>חישוב מרחק הפגיעה:
    <code><b>distance = (2 * initialVelocity**2 * sin(angleInRadians) * cos(angleInRadians)) / gravity</b></code></p>"]
    CalculateDistance --> CalculateDistanceToTarget["<p align='left'>חישוב המרחק מהמטרה:
    <code><b>distanceToTarget = abs(distance - targetDistance)</b></code></p>"]
    CalculateDistanceToTarget --> OutputResults["<p align='left'>פלט: <code><b>distance</b></code>, <code><b>distanceToTarget</b></code></p>"]
    OutputResults --> CheckHit{"בדיקה: <code><b>distanceToTarget < 1</b></code>?"}
    CheckHit -- כן --> OutputHit["הצגת הודעה: <b>HIT</b>"]
    OutputHit --> End["סוף"]
    CheckHit -- לא --> LoopStart
    LoopStart -- לא --> OutputMiss["הצגת הודעה: <b>YOU MISSED!</b>"]
    OutputMiss --> End

```

Legenda:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: targetDistance (מרחק המטרה) מוגדר ל-1000, numberOfAttempts (מספר הניסיונות) מאותחל ל-0, ו-gravity (קבוע הכבידה) מוגדר ל-32.2.
    LoopStart - תחילת הלולאה, הממשיכה כל עוד מספר הניסיונות קטן מ-10.
    IncreaseAttempts - הגדלת מונה הניסיונות ב-1.
    InputValues - קליטת זווית התחלתית (initialAngle) ומהירות התחלתית (initialVelocity) מהמשתמש.
    AngleToRadians - המרת הזווית ממעלות לרדיאנים.
    CalculateDistance - חישוב מרחק הפגיעה של הפגז.
    CalculateDistanceToTarget - חישוב המרחק בין הפגיעה למטרה.
    OutputResults - הצגת מרחק הפגיעה והמרחק למטרה.
    CheckHit - בדיקה האם הפגיעה קרובה מספיק למטרה (פחות מ-1).
    OutputHit - הצגת הודעת "HIT" אם הפגיעה קרובה למטרה.
    End - סוף התוכנית.
    OutputMiss - הצגת הודעה "YOU MISSED!" אם לא פגעו במטרה אחרי 10 ניסיונות.
"""
import math

# הגדרת קבוע הכבידה
GRAVITY = 32.2

# מרחק המטרה
TARGET_DISTANCE = 1000

def play_bomber():
    """פונקציה המכילה את הלוגיקה של המשחק BOMBER."""
    # אתחול מונה הניסיונות
    number_of_attempts = 0

    # לולאת המשחק
    while number_of_attempts < 10:
        number_of_attempts += 1
        print(f"ניסיון {number_of_attempts}:")
    
        # קלט מהמשתמש
        try:
            initial_angle = float(input("הזן זווית התחלתית (במעלות): "))
            initial_velocity = float(input("הזן מהירות התחלתית: "))
        except ValueError:
            print("אנא הזן מספרים חוקיים.")
            continue
        
        # המרת הזווית מרדיאנים למעלות
        angle_in_radians = math.radians(initial_angle)

        # חישוב מרחק הפגיעה
        distance = (2 * initial_velocity**2 * math.sin(angle_in_radians) * math.cos(angle_in_radians)) / GRAVITY

        # חישוב המרחק מהמטרה
        distance_to_target = abs(distance - TARGET_DISTANCE)

        print(f"מרחק פגיעה: {distance:.2f}")
        print(f"מרחק מהמטרה: {distance_to_target:.2f}")

        # בדיקה האם הפגיעה קרובה מספיק למטרה
        if distance_to_target < 1:
            print("פגעת!")
            return  # סיום הפונקציה (יציאה מהמשחק)

    # אם לא פגעו אחרי 10 ניסיונות
    print("לא פגעת!")


if __name__ == "__main__":
    play_bomber()

"""
הסבר הקוד:
1.  **ייבוא המודול `math`**:
   -  `import math`: ייבוא המודול `math`, המשמש לחישובים מתמטיים כמו סינוס וקוסינוס, והמרת מעלות לרדיאנים.
2.  **הגדרת קבוע הכבידה `GRAVITY`**:
   -  `GRAVITY = 32.2`: הגדרת קבוע הכבידה, המשמש לחישוב מסלול הפגז.
3. **הגדרת קבוע `TARGET_DISTANCE`**:
    - `TARGET_DISTANCE = 1000`: הגדרת מרחק המטרה מהתותח.
4.  **פונקציה `play_bomber()`**:
    -  מגדירה פונקציה המכילה את הלוגיקה של המשחק "מפציץ".
    -   `number_of_attempts = 0`: אתחול המשתנה `number_of_attempts` לספירת מספר הניסיונות.
5.  **לולאת המשחק `while number_of_attempts < 10:`**:
    -  לולאה הממשיכה עד שמספר הניסיונות מגיע ל-10.
    -  `number_of_attempts += 1`: הגדלת מונה הניסיונות ב-1 בכל סיבוב של הלולאה.
    -  **קלט נתונים**:
        - `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין משהו שאינו מספר, תוצג הודעת שגיאה.
        -  `initial_angle = float(input("הזן זווית התחלתית (במעלות): "))`: בקשת זווית התחלתית מהמשתמש ושמירתה במשתנה `initial_angle`.
        -  `initial_velocity = float(input("הזן מהירות התחלתית: "))`: בקשת מהירות התחלתית מהמשתמש ושמירתה במשתנה `initial_velocity`.
    -   **המרה למעלות לרדיאנים**:
         - `angle_in_radians = math.radians(initial_angle)`: המרת הזווית ממעלות לרדיאנים.
    -  **חישוב מרחק הפגיעה**:
        -  `distance = (2 * initial_velocity**2 * math.sin(angle_in_radians) * math.cos(angle_in_radians)) / GRAVITY`: חישוב מרחק הפגיעה באמצעות הנוסחה הבליסטית.
    -  **חישוב המרחק מהמטרה**:
        -  `distance_to_target = abs(distance - TARGET_DISTANCE)`: חישוב המרחק בין נקודת הפגיעה למטרה.
    -  **פלט נתונים**:
        -  `print(f"מרחק פגיעה: {distance:.2f}")`: הצגת מרחק הפגיעה.
        -  `print(f"מרחק מהמטרה: {distance_to_target:.2f}")`: הצגת המרחק בין הפגיעה למטרה.
    -  **תנאי ניצחון**:
        - `if distance_to_target < 1:`: בדיקה האם הפגיעה קרובה מספיק למטרה (מרחק קטן מ-1).
        - `print("פגעת!")`: הודעה על פגיעה במטרה.
        - `return`: סיום הפונקציה (יציאה מהמשחק) במקרה של פגיעה.
6.  **סיום המשחק ללא פגיעה**:
    - `print("לא פגעת!")`: הודעה על סיום המשחק אם לא פגעו במטרה אחרי 10 ניסיונות.
7.  **הפעלת המשחק**:
    -  `if __name__ == "__main__":`: בלוק זה מבטיח שהפונקציה `play_bomber()` תופעל רק אם הקובץ מופעל ישירות, ולא אם הוא מיובא כמודול.
    -  `play_bomber()`: קריאה לפונקציה להפעלת המשחק.
"""
