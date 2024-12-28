"""
ORBIT:
=================
קושי: 6
-----------------
המשחק "אורביט" הוא סימולציה של מערכת שמש פשוטה, שבה השחקן שולט בטיל ומנסה להתחמק מהשמש ולהגיע למסלול יציב. השחקן צריך לכוון את הטיל על ידי קביעת זווית השיגור והמהירות הראשונית. המטרה היא להשיג מסלול סביב השמש מבלי להתרסק לתוכה או לברוח מהמערכת. המשחק מסתיים בהודעת ניצחון או הפסד, בהתאם למסלול הטיסה.

חוקי המשחק:
1. המשחק מתחיל עם טיל שנמצא במרחק התחלתי מהשמש.
2. השחקן מזין זווית שיגור (במעלות) ומהירות התחלתית לטיל.
3. הטיל ינוע בהשפעת כוח הכבידה של השמש.
4. המשחק בודק האם הטיל:
   - פגע בשמש - אם כן, השחקן מפסיד.
   - התייצב במסלול - אם כן, השחקן מנצח.
   - ברח מהמערכת - אם כן, השחקן מפסיד.
5. המשחק מסתיים בהודעה בהתאם לתוצאה.
-----------------
אלגוריתם:
1.  הגדר קבועים:
    - מרחק התחלתי של הטיל מהשמש (R).
    - קבוע כוח הכבידה (G).
    - מהירות רדיאלית ראשונית (VR) - מוגדרת כ-0.
    - מהירות טנגנציאלית ראשונית (VT).
    - זווית השיגור (A).
    - פרמטר לבדיקה אם המסלול יציב (K).
    - מרחק מינימלי מהשמש להתרסקות (RMIN).
    - מרחק מקסימלי מהשמש לבריחה (RMAX).
2.  בקש מהמשתמש להזין זווית שיגור (A) ומהירות התחלתית (VT).
3.  המר את זווית השיגור מרדיאנים למעלות.
4.  חשב את הרכיבים הקרטזיים של המיקום ההתחלתי של הטיל (X, Y).
5.  חשב את הרכיבים הקרטזיים של מהירות ההתחלתית של הטיל (VX, VY).
6.  התחל לולאה (שבמקור היתה לולאת FOR עם 1000 איטרציות) שתבצע סימולציה של מסלול הטיסה.
    - חשב את המרחק הנוכחי בין הטיל לשמש (R).
    - אם הטיל קרוב מדי לשמש, הצג הודעת "CRASH" וצא מהמשחק.
    - אם הטיל רחוק מדי מהשמש, הצג הודעת "OUT OF RANGE" וצא מהמשחק.
    - חשב את תאוצת הטיל עקב כוח הכבידה (AG).
    - עדכן את הרכיבים הרדיאליים והטנגנציאליים של המהירות (VR, VT).
    - עדכן את הרכיבים הקרטזיים של המהירות (VX, VY).
    - עדכן את הרכיבים הקרטזיים של המיקום (X, Y).
    - חשב את הערך המוחלט של המהירות (V).
    - חשב את הערך של פרמטר K (שמשמש לבדיקת מסלול יציב).
    - אם הערך של K בין 0.99 ל- 1.01, הצג הודעת "ORBIT ESTABLISHED" וצא מהמשחק.
7.  אם הלולאה הסתיימה מבלי שהתקיימו תנאי הניצחון או ההפסד, סיים את המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeConstants["<p align='left'>אתחול קבועים:
    <code><b>
    initialDistance = 200
    gravitationalConstant = 10000
    initialRadialVelocity = 0
    minCrashDistance = 50
    maxEscapeDistance = 400
    </b></code></p>"]
    InitializeConstants --> InputValues["קלט מהירות התחלתית וזווית שיגור"]
    InputValues --> CalculateInitialPosition["<p align='left'>חישוב מיקום התחלתי:
    <code><b>
    x = initialDistance
    y = 0
    </b></code></p>"]
    CalculateInitialPosition --> CalculateInitialVelocity["<p align='left'>חישוב מהירות התחלתית:
    <code><b>
    vx = velocity * cos(angle)
    vy = velocity * sin(angle)
    </b></code></p>"]
    CalculateInitialVelocity --> SimulationLoopStart{"תחילת לולאת סימולציה (1000 איטרציות)"}
    SimulationLoopStart --"כן"--> CalculateDistance["חישוב מרחק הטיל מהשמש (r)"]
    CalculateDistance --> CheckCrash{"בדיקה: <code><b>r < minCrashDistance</b></code>?"}
    CheckCrash --"כן"--> OutputCrash["הצגת הודעה: <b>CRASH</b>"]
    OutputCrash --> End["סוף"]
    CheckCrash --"לא"--> CheckEscape{"בדיקה: <code><b>r > maxEscapeDistance</b></code>?"}
    CheckEscape --"כן"--> OutputEscape["הצגת הודעה: <b>OUT OF RANGE</b>"]
    OutputEscape --> End
    CheckEscape --"לא"--> CalculateGravity["חישוב תאוצת הכבידה (ag)"]
    CalculateGravity --> UpdateVelocities["<p align='left'>עדכון מהירויות:
    <code><b>
    vr = vr + ag * (x/r)
    vt = vt + ag * (y/r)
    </b></code></p>"]
    UpdateVelocities --> UpdateCartesianVelocity["<p align='left'>עדכון מהירות קרטזית:
    <code><b>
    vx = vt * (y/r)
    vy = vt * (x/r)
    </b></code></p>"]
    UpdateCartesianVelocity --> UpdatePosition["<p align='left'>עדכון מיקום:
    <code><b>
     x = x + vx
    y = y + vy
    </b></code></p>"]
    UpdatePosition --> CalculateTotalVelocity["חישוב מהירות כוללת (v)"]
    CalculateTotalVelocity --> CalculateK["חישוב פרמטר מסלול יציב (k)"]
    CalculateK --> CheckOrbit{"בדיקה: <code><b>0.99 < k < 1.01</b></code>?"}
    CheckOrbit --"כן"--> OutputOrbit["הצגת הודעה: <b>ORBIT ESTABLISHED</b>"]
    OutputOrbit --> End
    CheckOrbit --"לא"--> SimulationLoopStart
    SimulationLoopStart --"לא"--> End
```
Legenda:
    Start - התחלת התוכנית.
    InitializeConstants - אתחול קבועים כגון מרחק התחלתי, קבוע הכבידה, מרחק התרסקות מינימלי ומרחק בריחה מקסימלי.
    InputValues - קבלת קלט מהמשתמש: מהירות התחלתית וזווית שיגור.
    CalculateInitialPosition - חישוב המיקום ההתחלתי של הטיל בקואורדינטות קרטזיות.
    CalculateInitialVelocity - חישוב המהירות ההתחלתית של הטיל בקואורדינטות קרטזיות.
    SimulationLoopStart - תחילת לולאת הסימולציה שרצה 1000 פעמים, מדמה את מסלול הטיל.
    CalculateDistance - חישוב המרחק בין הטיל לשמש.
    CheckCrash - בדיקה האם הטיל קרוב מידי לשמש.
    OutputCrash - הצגת הודעת "CRASH" וסיום המשחק.
    CheckEscape - בדיקה האם הטיל רחוק מידי מהשמש.
    OutputEscape - הצגת הודעת "OUT OF RANGE" וסיום המשחק.
    CalculateGravity - חישוב תאוצת הכבידה הפועלת על הטיל.
    UpdateVelocities - עדכון המהירויות הרדיאלית והטנגנציאלית של הטיל.
    UpdateCartesianVelocity - עדכון רכיבי המהירות הקרטזיים של הטיל.
    UpdatePosition - עדכון רכיבי המיקום הקרטזיים של הטיל.
    CalculateTotalVelocity - חישוב המהירות הכוללת של הטיל.
    CalculateK - חישוב פרמטר מסלול יציב (k).
    CheckOrbit - בדיקה האם הטיל הגיע למסלול יציב.
    OutputOrbit - הצגת הודעת "ORBIT ESTABLISHED" וסיום המשחק.
    End - סיום התוכנית.
"""
import math

def play_orbit_game():
    # קבועים
    initial_distance = 200  # מרחק התחלתי מהשמש
    gravitational_constant = 10000 # קבוע כוח הכבידה
    initial_radial_velocity = 0  # מהירות רדיאלית ראשונית
    min_crash_distance = 50  # מרחק מינימלי להתרסקות
    max_escape_distance = 400 # מרחק מקסימלי לבריחה

    # קלט מהמשתמש
    try:
        launch_angle_degrees = float(input("הזן זווית שיגור במעלות (0-90): "))
        initial_velocity = float(input("הזן מהירות התחלתית: "))
    except ValueError:
        print("קלט לא תקין. אנא הזן מספרים.")
        return

    # המרת זווית מרדיאנים למעלות
    launch_angle_radians = math.radians(launch_angle_degrees)

    # מיקום התחלתי
    x = initial_distance
    y = 0

    # מהירות התחלתית
    vx = initial_velocity * math.cos(launch_angle_radians)
    vy = initial_velocity * math.sin(launch_angle_radians)

    # סימולציה
    for _ in range(1000): # במקור, הייתה לולאת FOR עם 1000 איטרציות
        # חישוב מרחק מהשמש
        r = math.sqrt(x**2 + y**2)

        # בדיקה אם הטיל התרסק או ברח
        if r < min_crash_distance:
            print("CRASH")
            return
        if r > max_escape_distance:
            print("OUT OF RANGE")
            return

        # חישוב תאוצת כוח הכבידה
        ag = -gravitational_constant / r**2

        # עדכון מהירויות (רדיאלית וטנגנציאלית)
        vr = initial_radial_velocity + ag * (x / r)
        vt = initial_velocity + ag * (y / r)

        # עדכון מהירויות קרטזיות
        vx = vt * (y / r)
        vy = vt * (x / r)


        # עדכון מיקום
        x = x + vx
        y = y + vy

        # חישוב מהירות כוללת
        v = math.sqrt(vx**2 + vy**2)

        # חישוב פרמטר מסלול יציב
        k = (v**2 * r) / gravitational_constant

        # בדיקה אם המסלול יציב
        if 0.99 < k < 1.01:
             print("ORBIT ESTABLISHED")
             return

    print("לא נוצר מסלול יציב.")

if __name__ == "__main__":
    play_orbit_game()


"""
הסבר הקוד:
1.  **ייבוא מודול `math`**:
    -   `import math`: ייבוא המודול `math`, המשמש לחישובים מתמטיים, כגון פונקציות טריגונומטריות וחישוב שורש ריבועי.

2.  **הגדרת הפונקציה `play_orbit_game()`**:
    -   הפונקציה מכילה את כל הלוגיקה של המשחק.

3.  **הגדרת קבועים**:
    -   `initial_distance`: מרחק התחלתי של הטיל מהשמש.
    -   `gravitational_constant`: קבוע כוח הכבידה.
    -   `initial_radial_velocity`: מהירות רדיאלית ראשונית של הטיל (אפס בהתחלה).
    -   `min_crash_distance`: מרחק מינימלי מהשמש שמתחתיו הטיל מתרסק.
    -   `max_escape_distance`: מרחק מקסימלי מהשמש שאחריו הטיל בורח מהמערכת.

4.  **קבלת קלט מהמשתמש**:
    -   קבלת זווית שיגור ומהירות התחלתית מהמשתמש.
    -   בלוק `try-except` לטיפול בשגיאות קלט (אם המשתמש מזין משהו שאינו מספר).

5.  **המרה מזווית במעלות לרדיאנים**:
    -   `math.radians()`: ממירה את הזווית מרדיאנים למעלות, כיוון שפונקציות טריגונומטריות בפייתון עובדות עם רדיאנים.

6.  **אתחול מיקום ומהירות**:
    -   `x`, `y`: רכיבי המיקום ההתחלתי של הטיל (הטיל מתחיל בצד ימין של השמש).
    -   `vx`, `vy`: רכיבי המהירות ההתחלתית של הטיל, מחושבים בעזרת פונקציות הטריגונומטריות.

7. **לולאת סימולציה**:
    -   `for _ in range(1000)`: לולאה שרצה 1000 פעמים ומדמה את מסלול התנועה של הטיל.

8. **בדיקת מצבי קצה**:
    -   `if r < min_crash_distance`: בדיקה אם הטיל התרסק בשמש.
    -   `if r > max_escape_distance`: בדיקה אם הטיל ברח מהמערכת.

9. **חישובים פיזיקליים**:
    -   `r`: מרחק הטיל מהשמש.
    -   `ag`: תאוצת הכבידה הפועלת על הטיל.
    -   `vr`, `vt`: עדכון המהירות הרדיאלית והטנגנציאלית.
     -   `vx`, `vy`: עדכון המהירויות הקרטזיות.
    -    `x`, `y`: עדכון המיקום של הטיל.
    -   `v`: המהירות הכוללת של הטיל.
    -   `k`: פרמטר מסלול יציב, שמשמש לבדיקה אם הטיל במסלול יציב.

10. **בדיקת מסלול יציב**:
     -    `if 0.99 < k < 1.01`: בדיקה אם הטיל במסלול יציב.
     - אם התנאי מתקיים, מודפסת הודעה "ORBIT ESTABLISHED" והמשחק מסתיים.

11. **סיום המשחק**:
      -  אם הלולאה מסתיימת מבלי שהתנאי ליצירת מסלול התקיים, תודפס הודעה שלא נוצר מסלול יציב.

12. **הפעלת המשחק**:
     -  `if __name__ == "__main__":`: בלוק זה מבטיח שהמשחק יופעל רק אם הקובץ מופעל ישירות, ולא כאשר מיובא כמודול.
     -   `play_orbit_game()`: קריאה לפונקצית המשחק.
"""
