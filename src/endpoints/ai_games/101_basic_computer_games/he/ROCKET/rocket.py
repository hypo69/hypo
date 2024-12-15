<ROCKET>:
=================
קושי: 4
-----------------
המשחק "רוקט" מדמה שיגור רקטה לחלל. השחקן מזין ערך של דחף בתחילת השיגור, ולאחר מכן המשחק מדמה את מעוף הרקטה עד לפגיעה בקרקע. המשחק מציג גרף פשוט של גובה הרקטה כפונקציה של זמן, וכן את זמן הפגיעה בקרקע.
חוקי המשחק:
1. השחקן מזין דחף התחלתי.
2. המשחק מדמה את מעוף הרקטה על ידי חישוב גובה הרקטה בכל נקודת זמן.
3. המשחק מציג גרף פשוט של גובה הרקטה כפונקציה של זמן, וכן את זמן הפגיעה בקרקע.
4. המשחק נמשך עד שהרקטה פוגעת בקרקע.
-----------------
אלגוריתם:
1. בקש מהמשתמש להזין דחף התחלתי ושמור ב-`initialThrust`.
2. אתחל את הגובה (`rocketHeight`) ל-0.
3. אתחל את הזמן (`time`) ל-0.
4. הגדר את קפיצת הזמן (`timeStep`) ל-0.1.
5. התחל לולאה כל עוד גובה הרקטה גדול או שווה ל-0:
  5.1 הדפס גרף פשוט של גובה הרקטה בנקודת הזמן הנוכחית.
  5.2 עדכן את הגובה הרקטה:
     `rocketHeight = rocketHeight + initialThrust - 0.5 * 10 * time * time `
  5.3  הגדל את הזמן `time = time + timeStep`.
6. הצג את זמן הפגיעה בקרקע.
7. סיים.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InputThrust["קלט דחף התחלתי: <code><b>initialThrust</b></code>"]
    InputThrust --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    rocketHeight = 0
    time = 0
    timeStep = 0.1
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: כל עוד <code><b>rocketHeight >= 0</b></code>"}
    LoopStart -- כן --> DisplayHeight["הצג גרף גובה הרקטה: <code><b>rocketHeight</b></code>"]
    DisplayHeight --> CalculateNewHeight["חישוב גובה חדש: <code><b>rocketHeight = rocketHeight + initialThrust - 0.5 * 10 * time * time</b></code>"]
    CalculateNewHeight --> IncrementTime["הגדלת זמן: <code><b>time = time + timeStep</b></code>"]
    IncrementTime --> LoopStart
    LoopStart -- לא --> OutputImpactTime["הצג זמן פגיעה: <code><b>time</b></code>"]
    OutputImpactTime --> End["סוף"]
```
Legenda:
    Start - התחלת התוכנית.
    InputThrust - קבלת קלט מהמשתמש עבור הדחף ההתחלתי של הרקטה.
    InitializeVariables - אתחול משתנים: גובה הרקטה, זמן וקפיצת זמן.
    LoopStart - תחילת לולאת החישוב, הממשיכה כל עוד גובה הרקטה חיובי.
    DisplayHeight - הצגת גובה הרקטה בגרף פשוט.
    CalculateNewHeight - חישוב גובה הרקטה בנקודת הזמן הבאה.
    IncrementTime - הגדלת הזמן בקפיצה קבועה.
    OutputImpactTime - הצגת זמן הפגיעה בקרקע.
    End - סוף התוכנית.
"""
```python
import time
def play_rocket_game():
    """
    מדמה שיגור רקטה לחלל ומציג את הגובה כפונקציה של זמן.
    """
    try:
        # בקשת דחף התחלתי מהמשתמש
        initialThrust = float(input("הזן את הדחף ההתחלתי: "))
    except ValueError:
        print("קלט לא תקין, אנא הזן מספר.")
        return

    rocketHeight = 0  # גובה הרקטה
    time = 0  # זמן
    timeStep = 0.1  # קפיצת זמן

    print("\nשיגור הרקטה...")
    time.sleep(1)  # השהייה קלה לסימולציה
    # לולאה ראשית שרצה כל עוד הרקטה באוויר (גובה חיובי)
    while rocketHeight >= 0:
        # הדפסת גרף פשוט המייצג את גובה הרקטה בנקודת זמן נתונה
        print("*" * int(rocketHeight / 10 if rocketHeight > 0 else 0) + f" {time:.1f}")

        # חישוב גובה חדש של הרקטה
        # הנוסחה מדמה השפעת דחף וגרביטציה על הגובה
        rocketHeight = rocketHeight + initialThrust - 0.5 * 10 * time * time

        # הגדלת הזמן
        time += timeStep
        # השהייה קצרה בין שלבי הסימולציה
        time.sleep(0.05)

    # הדפסת זמן הפגיעה בקרקע
    print(f"\nהרקטה פגעה בקרקע בזמן {time:.1f} שניות.")

if __name__ == "__main__":
    play_rocket_game()
```
<הערות סיום>
הסבר הקוד:
1.  **פונקציה `play_rocket_game()`**:
    - הפונקציה מכילה את הלוגיקה של המשחק.
    - `initialThrust`: משתנה השומר את הדחף ההתחלתי שהמשתמש מזין.
    - `rocketHeight`: משתנה המייצג את גובה הרקטה, מתחיל ב-0.
    - `time`: משתנה המייצג את הזמן, מתחיל ב-0.
    - `timeStep`: משתנה המייצג את קפיצת הזמן, בשימוש לסימולציה.
2.  **קלט נתונים**:
    - `try...except ValueError`: בלוק try-except לטיפול בשגיאות קלט. אם המשתמש יזין משהו שאינו מספר, תוצג הודעת שגיאה, והפונקציה תסתיים.
    - `initialThrust = float(input("הזן את הדחף ההתחלתי: "))`: בקשה מהמשתמש להזין את הדחף ההתחלתי, והמרה של הקלט למספר עשרוני.
3.  **לולאת המשחק `while rocketHeight >= 0:`**:
   - לולאה שרצה כל עוד הרקטה באוויר, כלומר הגובה שלה גדול או שווה ל-0.
  - `print("*" * int(rocketHeight / 10 if rocketHeight > 0 else 0) + f" {time:.1f}")`: הדפסת גרף פשוט המייצג את גובה הרקטה בנקודת זמן נתונה. מספר הכוכביות מתאים לערך גובה הרקטה מחולק ב-10. אם הגובה שלילי, לא יודפסו כוכביות.
    - `rocketHeight = rocketHeight + initialThrust - 0.5 * 10 * time * time`: חישוב גובה הרקטה בנקודת הזמן הבאה, תוך שימוש בנוסחה המדמה את השפעת הדחף והגרביטציה.
    - `time += timeStep`: הגדלת הזמן בקפיצה קבועה.
    - `time.sleep(0.05)`: השהייה קצרה כדי להאט את הסימולציה.
4.  **פלט זמן פגיעה**:
    - `print(f"\nהרקטה פגעה בקרקע בזמן {time:.1f} שניות.")`: הדפסת הזמן בו הרקטה פגעה בקרקע.
5.  **הפעלת המשחק**:
    - `if __name__ == "__main__":`: בלוק זה מבטיח שהפונקציה `play_rocket_game()` תופעל רק אם הקובץ מופעל ישירות, ולא אם הוא מיובא כמודול.
    - `play_rocket_game()`: קריאה לפונקציה להפעלת המשחק.
</הערות סיום>
