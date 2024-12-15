"""
<3D PLOT>:
=================
קושי: 7
-----------------
המשחק "3D PLOT" מדמה גרפיקה תלת-מימדית פשוטה על ידי ציור קווים בין נקודות שמוגדרות על ידי קואורדינטות X, Y ו-Z.
השחקן מגדיר את הנקודות על ידי הזנת קואורדינטות X, Y, ו-Z עבור כל נקודה וחיבורן על ידי קווים.
המשחק מציג את גרף הקווים באמצעות קואורדינטות X ו-Y בלבד על גבי מסך הטקסט.

חוקי המשחק:
1. המשחק מבקש מהמשתמש להזין את מספר הנקודות (עד 10 נקודות).
2. עבור כל נקודה, המשתמש מזין קואורדינטות X, Y ו-Z.
3. המשחק יוצר קווים המחברים בין כל הנקודות הסמוכות (נקודה ראשונה עם שנייה, שנייה עם שלישית וכו').
4. הקווים מצוירים על מסך טקסט המבוסס על קואורדינטות X ו-Y בלבד, כאשר קואורדינטת ה-Z לא משפיעה על המיקום הגרפי, אלא משמשת רק לצורך חישוב הקווים.
5. התצוגה משתמשת בסימנים '*' כדי לצייר את הקווים במסך הטקסט.
6. מסך הטקסט מוגבל לטווח של 0 עד 39 עבור ציר ה-X ו-0 עד 24 עבור ציר ה-Y.
7. הקווים מצוירים באמצעות אלגוריתם DDA (Digital Differential Analyzer) פשוט.
-----------------
אלגוריתם:
1. קבע את גודל מסך הטקסט (רוחב 40, גובה 25) ואתחול מסך ריק באמצעות רשימה של רשימות.
2. בקש מהמשתמש להזין את מספר הנקודות (עד 10).
3. צור רשימות לאחסון קואורדינטות X, Y ו-Z עבור כל נקודה.
4. עבור כל נקודה:
   4.1 בקש מהמשתמש להזין את קואורדינטות X, Y ו-Z.
   4.2 שמור את הקואורדינטות ברשימות המתאימות.
5. עבור כל זוג נקודות סמוכות:
   5.1 חשב את ההפרש בין קואורדינטות X ו-Y של שתי הנקודות.
   5.2 קבע את מספר הצעדים לצורך ציור הקו על ידי לקיחת המקסימום בין ערכי ההפרש.
   5.3 חשב את השינוי בכל צעד עבור X ו-Y.
   5.4 עבור כל צעד בציור הקו:
       5.4.1 חשב את הקואורדינטות הנוכחיות של הנקודה על הקו.
       5.4.2 אם הקואורדינטות נמצאות בתוך מסך הטקסט, צייר את הקו באמצעות הסימן '*'.
6. הדפס את מסך הטקסט.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeScreen["אתחול מסך: 
    <br><code><b>screen = [[' ']*40 for _ in range(25)]</b></code>
    <br><code><b>width = 40, height = 25</b></code>"]
    InitializeScreen --> InputNumPoints["קלט: <code><b>numberOfPoints</b></code>"]
    InputNumPoints --> InitializeCoords["אתחול רשימות קואורדינטות:
    <br><code><b>xCoords = []</b></code>, <code><b>yCoords = []</b></code>, <code><b>zCoords = []</b></code>"]
    InitializeCoords --> LoopInputPointsStart{"לולאה: עבור <code><b>numberOfPoints</b></code> פעמים"}
    LoopInputPointsStart --> InputPointCoords["קלט: <code><b>x, y, z</b></code>"]
    InputPointCoords --> StoreCoords["שמירת קואורדינטות:
     <br><code><b>xCoords.append(x)</b></code>, <code><b>yCoords.append(y)</b></code>, <code><b>zCoords.append(z)</b></code>"]
    StoreCoords --> LoopInputPointsEnd{"סוף לולאה: <code><b>numberOfPoints</b></code> פעמים"}
    LoopInputPointsEnd --> LoopDrawLinesStart{"לולאה: עבור כל זוג נקודות סמוכות"}
    LoopDrawLinesStart --> CalcDelta["חישוב הפרשים: 
    <br><code><b>deltaX = xCoords[i+1] - xCoords[i]</b></code>
    <br><code><b>deltaY = yCoords[i+1] - yCoords[i]</b></code>"]
    CalcDelta --> CalcSteps["חישוב מספר צעדים: 
    <br><code><b>steps = max(abs(deltaX), abs(deltaY))</b></code>"]
    CalcSteps --> CalcIncrement["חישוב שינוי בכל צעד: 
    <br><code><b>xIncrement = deltaX / steps</b></code>
    <br><code><b>yIncrement = deltaY / steps</b></code>"]
    CalcIncrement --> LoopDrawLineStart{"לולאה: עבור כל צעד"}
    LoopDrawLineStart --> CalcCurrentCoords["חישוב קואורדינטות נוכחיות:
    <br><code><b>currentX = xCoords[i] + step * xIncrement</b></code>
    <br><code><b>currentY = yCoords[i] + step * yIncrement</b></code>"]
    CalcCurrentCoords --> CheckBounds{"בדיקה:
    <br><code><b>0 <= currentX < width  ו- 0 <= currentY < height</b></code>"}
    CheckBounds -- כן --> DrawPoint["ציור נקודה: 
     <br><code><b>screen[int(currentY)][int(currentX)] = '*'</b></code>"]
    DrawPoint --> LoopDrawLineEnd{"סוף לולאה: עבור כל צעד"}
    CheckBounds -- לא --> LoopDrawLineEnd
    LoopDrawLineEnd --> LoopDrawLinesEnd{"סוף לולאה: עבור כל זוג נקודות סמוכות"}
    LoopDrawLinesEnd --> PrintScreen["הדפסת המסך"]
    PrintScreen --> End["סוף"]
    LoopDrawLinesStart -- לא -->PrintScreen
```

Legenda:
    Start - התחלת התוכנית.
    InitializeScreen - אתחול מסך טקסט ריק בגודל 40x25.
    InputNumPoints - קבלת מספר הנקודות מהמשתמש.
    InitializeCoords - אתחול רשימות לאחסון קואורדינטות X, Y ו-Z של הנקודות.
    LoopInputPointsStart - תחילת לולאה לקבלת קואורדינטות עבור כל הנקודות.
    InputPointCoords - קבלת קואורדינטות X, Y ו-Z של נקודה מהמשתמש.
    StoreCoords - שמירת הקואורדינטות ברשימות המתאימות.
    LoopInputPointsEnd - סוף הלולאה לקבלת קואורדינטות.
    LoopDrawLinesStart - תחילת לולאה לציור קווים בין הנקודות.
    CalcDelta - חישוב ההפרש בין קואורדינטות X ו-Y של שתי נקודות סמוכות.
    CalcSteps - חישוב מספר הצעדים לציור הקו בין הנקודות.
    CalcIncrement - חישוב השינוי בכל צעד לציר X ו-Y.
    LoopDrawLineStart - תחילת לולאה לציור הקו בין שתי נקודות.
    CalcCurrentCoords - חישוב הקואורדינטות הנוכחיות של הנקודה על הקו.
    CheckBounds - בדיקה האם הקואורדינטות הנוכחיות נמצאות בתוך גבולות מסך הטקסט.
    DrawPoint - ציור הנקודה על מסך הטקסט.
    LoopDrawLineEnd - סוף הלולאה לציור הקו בין שתי נקודות.
    LoopDrawLinesEnd - סוף הלולאה לציור קווים בין כל הנקודות.
    PrintScreen - הדפסת מסך הטקסט.
    End - סיום התוכנית.
"""
```python
# הגדרת גודל מסך הטקסט
WIDTH = 40
HEIGHT = 25

def draw_3d_plot():
    """
    מצייר גרף תלת מימדי פשוט על ידי חיבור נקודות באמצעות קווים
    על מסך טקסט.
    """

    # יצירת מסך טקסט ריק
    screen = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

    # קבלת מספר הנקודות מהמשתמש
    while True:
        try:
            num_points = int(input("הזן את מספר הנקודות (עד 10): "))
            if 1 <= num_points <= 10:
                break
            else:
                print("מספר הנקודות צריך להיות בין 1 ל-10.")
        except ValueError:
            print("אנא הזן מספר שלם.")

    # אתחול רשימות לקואורדינטות X, Y ו-Z
    x_coords = []
    y_coords = []
    z_coords = []

    # קבלת קואורדינטות עבור כל נקודה
    for i in range(num_points):
        while True:
            try:
                x = float(input(f"הזן קואורדינטת X עבור נקודה {i + 1}: "))
                y = float(input(f"הזן קואורדינטת Y עבור נקודה {i + 1}: "))
                z = float(input(f"הזן קואורדינטת Z עבור נקודה {i + 1}: "))
                x_coords.append(x)
                y_coords.append(y)
                z_coords.append(z)
                break
            except ValueError:
                print("אנא הזן מספרים.")


    # ציור קווים בין הנקודות הסמוכות
    for i in range(num_points - 1):
        # חישוב ההפרש בין קואורדינטות ה-X וה-Y של הנקודות
        delta_x = x_coords[i+1] - x_coords[i]
        delta_y = y_coords[i+1] - y_coords[i]

        # קביעת מספר הצעדים לצורך ציור הקו
        steps = max(abs(delta_x), abs(delta_y))

        # חישוב השינוי בכל צעד עבור X ו-Y
        x_increment = delta_x / steps if steps != 0 else 0
        y_increment = delta_y / steps if steps != 0 else 0

        # ציור הקו צעד אחר צעד
        for step in range(int(steps) + 1):
            # חישוב קואורדינטות נוכחיות על הקו
            current_x = x_coords[i] + step * x_increment
            current_y = y_coords[i] + step * y_increment

            # בדיקה האם הנקודה בתוך גבולות המסך
            if 0 <= int(current_x) < WIDTH and 0 <= int(current_y) < HEIGHT:
                # ציור נקודה על המסך
                screen[int(current_y)][int(current_x)] = '*'


    # הדפסת המסך
    for row in screen:
        print("".join(row))

if __name__ == "__main__":
    draw_3d_plot()

```
"""
הסבר הקוד:
1.  **הגדרת גודל מסך הטקסט**:
    - `WIDTH = 40`: מגדיר את רוחב מסך הטקסט ל-40 תווים.
    - `HEIGHT = 25`: מגדיר את גובה מסך הטקסט ל-25 שורות.

2.  **הפונקציה `draw_3d_plot()`**:
    - מכילה את כל הלוגיקה של המשחק.
    - `screen = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]`: יוצרת מסך טקסט דו-ממדי ריק המלא ברווחים.
    - **קלט מספר הנקודות**:
        - לולאה שמבקשת מהמשתמש להזין את מספר הנקודות (בין 1 ל-10), ומטפלת בשגיאות קלט אפשריות.
    - **אתחול רשימות**:
        - `x_coords = []`, `y_coords = []`, `z_coords = []`: רשימות לאחסון קואורדינטות ה-X, Y וה-Z של הנקודות.
    - **קלט קואורדינטות**:
        - לולאה שמבקשת מהמשתמש להזין את קואורדינטות ה-X, Y וה-Z עבור כל נקודה.
    - **ציור קווים**:
        - לולאה שעוברת על כל זוג נקודות סמוכות.
        - `delta_x = x_coords[i+1] - x_coords[i]`, `delta_y = y_coords[i+1] - y_coords[i]`: חישוב ההפרשים בין קואורדינטות ה-X וה-Y של שתי הנקודות.
        - `steps = max(abs(delta_x), abs(delta_y))`: קביעת מספר הצעדים לציור הקו.
        - `x_increment = delta_x / steps`, `y_increment = delta_y / steps`: חישוב השינוי בכל צעד עבור קואורדינטות ה-X וה-Y.
        - לולאה פנימית שעוברת על כל צעד בציור הקו:
            - `current_x = x_coords[i] + step * x_increment`, `current_y = y_coords[i] + step * y_increment`: חישוב הקואורדינטות הנוכחיות של הנקודה על הקו.
            - בדיקה האם הנקודה נמצאת בתוך גבולות מסך הטקסט: `0 <= int(current_x) < WIDTH and 0 <= int(current_y) < HEIGHT`.
            - אם הנקודה בתוך הגבולות, מציירים אותה על המסך: `screen[int(current_y)][int(current_x)] = '*'`.
    - **הדפסת המסך**:
        - לולאה שעוברת על כל שורה במסך ומדפיסה אותה.
3.  **הפעלת המשחק**:
    - `if __name__ == "__main__":`: מבטיח שהפונקציה `draw_3d_plot()` תופעל רק אם הסקריפט מורץ ישירות, ולא אם הוא מיובא כמודול.
    - `draw_3d_plot()`: קריאה לפונקציה להפעלת המשחק.
"""
