# ניתוח קוד: משחק ארטילריה

## 1. <algorithm>

**תיאור אלגוריתם:**

1. **אתחול:**
   - הגדרת מספר מקסימלי של ניסיונות (`maxAttempts = 10`).
   - הגדרת כוח הכבידה (`gravity = 32.2`).
   - יצירת מרחק מטרה אקראי בין 100 ל-1000 (`targetDistance`).
   - אתחול מונה ניסיונות (`attempt = 0`).
   - קביעת טווח דיוק של 10% (`accuracy = 0.1`).
   - הדפסת מרחק המטרה.
   דוגמה:
   ```
   maxAttempts = 10
   gravity = 32.2
   targetDistance = 450
   attempt = 0
   accuracy = 0.1
   print(f"מרחק מטרה: {targetDistance}") # מרחק מטרה: 450
   ```

2. **לולאה ראשית (כל עוד מספר הניסיונות לא מוצה):**
   - הגדלת מונה הניסיונות ב-1.
   - הדפסת מספר הניסיון הנוכחי.
   דוגמה:
   ```
    while attempt < maxAttempts:
        attempt += 1
        print(f"ניסיון {attempt} מתוך {maxAttempts}") # ניסיון 1 מתוך 10
   ```

3. **קליטת קלט משתמש:**
   - בקשת זווית ירי (במעלות) ומהירות התחלתית מהמשתמש.
   - בדיקת קלט תקין (מספרים).
   דוגמה:
   ```
        angle = float(input("הכנס זווית ירי (במעלות): ")) # קלט: 45
        initialSpeed = float(input("הכנס מהירות התחלתית: ")) # קלט: 100
   ```

4. **המרת זווית לרדיאנים:**
   - המרת זווית הירי ממעלות לרדיאנים לצורך חישובים טריגונומטריים.
   דוגמה:
   ```
        angle = math.radians(angle) # angle = 0.78539
   ```

5. **חישוב מרחק:**
   - חישוב מרחק הפגז לפי הנוסחה: `distance = (initialSpeed^2 * sin(2 * angle)) / gravity`.
   דוגמה:
   ```
        distance = (initialSpeed ** 2 * math.sin(2 * angle)) / gravity # distance = 310.6
   ```

6. **בדיקת פגיעה:**
   - בדיקה האם מרחק הפגז נמצא בטווח הדיוק (10%) של מרחק המטרה.
   - אם פגע, הודעה למשתמש על ניצחון וסיום המשחק.
   - אם לא, בדיקה האם הפגז קצר או ארוך.
   - הודעה למשתמש אם קצר מידי או ארוך מידי.
   דוגמה:
   ```
     if targetDistance * (1 - accuracy) <= distance <= targetDistance * (1 + accuracy):
        print("פגעת!")
        break
     elif distance < targetDistance:
        print("קצר מדי!")
     else:
        print("ארוך מדי!")
   ```

7. **הפסד:**
   - אם כל הניסיונות נוצלו ולא הייתה פגיעה, הודעה למשתמש על הפסד.
    דוגמה:
   ```
        if attempt == maxAttempts:
            print("הפסדת!")
   ```

**זרימת נתונים:**

- משתמש מזין זווית ומהירות.
- המרת הזווית לרדיאנים.
- חישוב מרחק הפגז.
- השוואת מרחק הפגז עם מרחק המטרה.
- הדפסת הודעות משוב למשתמש.

## 2. <mermaid>

```mermaid
flowchart TD
    Start[התחלה] --> InitializeVariables[<p align='left'>אתחול משתנים:<br><code>maxAttempts = 10<br>gravity = 32.2<br>targetDistance = random(100, 1000)<br>attempt = 0<br>accuracy = 0.1</code></p>]
    InitializeVariables --> LoopStart{התחלת לולאה: <br><code>attempt < maxAttempts</code>?}
    LoopStart -- כן --> IncreaseAttempts[<code>attempt = attempt + 1</code>]
    IncreaseAttempts --> PrintAttempt[הדפס: <br><code>ניסיון {attempt} מתוך {maxAttempts}</code>]
    PrintAttempt --> InputAngleSpeed[<p align='left'>קלט זווית ירי<br> <code>angle</code>(מעלות)<br> ומהירות התחלתית<br> <code>initialSpeed</code></p>]
    InputAngleSpeed --> ConvertAngle[<code>angle = radians(angle)</code>]
    ConvertAngle --> CalculateDistance[<p align='left'>חישוב מרחק:<br><code>distance = (initialSpeed^2 * sin(2 * angle)) / gravity</code></p>]
    CalculateDistance --> CheckHit{<p align='left'>בדיקת פגיעה:<br><code>targetDistance * (1 - accuracy) <= distance <= targetDistance * (1 + accuracy)</code>?</p>}
    CheckHit -- כן --> OutputWin[הדפס: <br><code>"פגעת!"</code>]
    OutputWin --> End[סוף]
    CheckHit -- לא --> CheckShort{<code>distance < targetDistance</code>?}
    CheckShort -- כן --> OutputShort[הדפס: <br><code>"קצר מדי!"</code>]
    OutputShort --> LoopStart
    CheckShort -- לא --> OutputLong[הדפס: <br><code>"ארוך מדי!"</code>]
    OutputLong --> LoopStart
    LoopStart -- לא --> OutputLose[הדפס: <br><code>"הפסדת!"</code>]
    OutputLose --> End
```
**ניתוח תלויות:**
- `random`: משמש לייצור מספר אקראי עבור מרחק המטרה.
- `math`: מספק פונקציות מתמטיות כמו `radians` ו-`sin`.

## 3. <explanation>

**ייבוא מודולים:**

-   `import random`: משמש ליצירת מספר אקראי של מרחק המטרה. המודול מספק פונקציות ליצירת מספרים פסאודו-אקראיים.
-   `import math`: משמש לביצוע פעולות מתמטיות, כמו המרת זווית ממעלות לרדיאנים (`math.radians()`) וחישוב סינוס (`math.sin()`).

**משתנים:**

-   `maxAttempts` (int): מספר מקסימלי של ניסיונות, שווה ל-10.
-   `gravity` (float): ערך הכבידה, שווה ל-32.2.
-   `targetDistance` (int): מרחק המטרה האקראי שנוצר בין 100 ל-1000.
-   `attempt` (int): מונה הניסיונות, מתחיל מ-0 ועולה בכל ניסיון.
-   `accuracy` (float): טווח הדיוק של הפגיעה במטרה, 10% (0.1).
-   `angle` (float): זווית הירי שנקלטת מהמשתמש (במעלות ואז מומרת לרדיאנים).
-   `initialSpeed` (float): מהירות הירי שנקלטת מהמשתמש.
-   `distance` (float): מרחק הפגז המחושב לפי הנוסחה הפיזיקלית.

**פונקציות:**

- אין פונקציות שנוצרו על ידי המשתמש בקוד זה, נעשה שימוש בפונקציות המובנות בתוך המודולים שייובאו.
- `random.randint(a, b)`: מייצר מספר שלם אקראי בין a ל-b (כולל).
- `math.radians(degrees)`: ממיר זווית ממעלות לרדיאנים.
- `math.sin(x)`: מחשב את הסינוס של x (ברדיאנים).
- `input(prompt)`: מקבל קלט מהמשתמש.
- `float(x)`: ממיר את הקלט למספר עשרוני.
- `print(message)`: מדפיס הודעה לקונסול.

**לולאות:**

-   `while attempt < maxAttempts:`: הלולאה הראשית שממשיכה כל עוד מספר הניסיונות קטן ממספר הניסיונות המקסימלי.
-   `while True:`: לולאה אינסופית שמאפשרת קליטת נתונים מהמשתמש ומוודאת קלט תקין.

**בעיות אפשריות ושיפורים:**

-   **טיפול בקלט:** הקוד מטפל בשגיאות `ValueError` בעת קליטת קלט מהמשתמש, אבל לא מטפל בשגיאות נוספות (כמו קלט שלילי). אפשר לשפר את הקוד כדי לבדוק ולוודא שהערכים שהמשתמש מכניס הינם חיוביים.
-   **משוב למשתמש:**  ניתן להוסיף משוב נוסף למשתמש (למשל, כמה רחוק הפגז מהמטרה).
-   **יכולת בחירת רמת קושי:** אפשר לאפשר למשתמש לבחור רמת קושי שמשפיעה על טווח מרחק המטרה או על מספר הניסיונות.
-   **שימוש בפונקציות:** אפשר לפצל את הקוד לפונקציות קטנות וברורות יותר (למשל, פונקציה לקלט משתמש, פונקציה לחישוב המרחק וכו').
-   **ניקוד:** ניתן להוסיף ניקוד למשתמש בהתאם למספר הניסיונות שנדרשו לפגיעה.

**שרשרת קשרים עם חלקים אחרים בפרויקט:**

- הקוד עומד בפני עצמו ואין לו תלות בקודים נוספים בפרויקט.