## <algorithm>
הקוד מדמה משחק קוביה תלת מימדית. להלן תיאור מפורט של התהליך:

1. **אתחול הקוביה**:
   - הקוד מתחיל ביצירת קוביה תלת ממדית בגודל 3x3x3 באמצעות `numpy`.
   - הקוביה מאותחלת עם ערכים מ-1 עד 27.
   ```python
    cube = np.arange(1, 28).reshape(3, 3, 3)
    # cube  יכיל מערך תלת מימדי של 3x3x3 עם הערכים מ1 עד 27. לדוגמא:
    #  [[[ 1  2  3]
    #    [ 4  5  6]
    #    [ 7  8  9]]

    #   [[10 11 12]
    #    [13 14 15]
    #    [16 17 18]]

    #   [[19 20 21]
    #    [22 23 24]
    #    [25 26 27]]]
    ```

2. **לולאה ראשית**:
   - המשחק רץ בלולאה אינסופית עד שהמשתמש מזין את הפקודה "END" או "0".
    ```python
    while True:
       # לולאה ממשיכה עד שהמשתמש מזין "END"
    ```

3. **קבלת קלט**:
   - הקוד מבקש מהמשתמש להזין קואורדינטות (X Y Z), פקודת סיבוב ('X', 'Y', 'Z') או "END" לסיום.
    ```python
        command = input("Введите координаты (X Y Z) или команду (\'X\', \'Y\', \'Z\') или \'END\' для выхода: ").upper()
        # command יכול להכיל מחרוזת כמו "1 2 3" או "X" או "END"
    ```

4. **בדיקת פקודת סיום**:
   - אם הקלט הוא "END" או "0", המשחק מסתיים.
    ```python
        if command == "END" or command == "0":
            print("Игра завершена.")
            break
        # אם command הוא "END" או "0", הלולאה הראשית מסתיימת.
    ```

5. **פיצול הקלט**:
   - הקלט מפולג לחלקים לפי רווחים.
    ```python
        parts = command.split()
        # אם command הוא "1 2 3", parts יהיה ["1", "2", "3"]
        # אם command הוא "X", parts יהיה ["X"]
    ```

6. **טיפול בקואורדינטות**:
    - אם הקלט כולל שלושה חלקים, הקוד מנסה לפרש אותם כקואורדינטות.
        ```python
        if len(parts) == 3:
           try:
              x, y, z = map(int, parts)
              # אם parts הוא ["1", "2", "3"] אז x=1, y=2, z=3
               if 1 <= x <= 3 and 1 <= y <= 3 and 1 <= z <= 3:
                   # בדיקה שהקואורדינטות בטווח
                    pos = get_cube_position(cube, x, y, z)
                    print(f"Положение кубика ({x}, {y}, {z}): {pos}")
                   # פלט מיקום הקוביה
               else:
                   # טיפול בקואורדינטות לא בטווח
           except ValueError:
                # טיפול בהמרת מספר שגויה
        ```

7. **טיפול בפקודות סיבוב**:
    - אם הקלט כולל חלק אחד, הקוד בודק אם זו פקודת סיבוב.
    ```python
        elif len(parts) == 1:
            if command == "X":
                cube = rotate_x(cube)
                print("Куб повернут вокруг оси X.")
            elif command == "Y":
                cube = rotate_y(cube)
                print("Куб повернут вокруг оси Y.")
            elif command == "Z":
                cube = rotate_z(cube)
                print("Куб повернут вокруг оси Z.")
            else:
                print("Неизвестная команда.")
    ```
    - הקוד מבצע סיבוב בהתאם:
      - `rotate_x`: מסובבת את הקוביה סביב ציר X.
      - `rotate_y`: מסובבת את הקוביה סביב ציר Y.
      - `rotate_z`: מסובבת את הקוביה סביב ציר Z.
    - הפונקציות משתמשות ב `np.rot90()` לצורך סיבוב הקוביה.

8. **טיפול בקלט שגוי**:
  - אם הקלט לא תואם לאף אחד מהמקרים הקודמים, מודפסת הודעת שגיאה.
    ```python
    else:
      print("Неверный формат ввода.")
    ```

9. **סיום המשחק**:
  - כאשר הלולאה הראשית מסתיימת, המשחק מסתיים.

## <mermaid>
```mermaid
flowchart TD
    Start[התחלה] --> InitializeCube[אתחול הקוביה<br><code>cube = np.arange(1, 28).reshape(3, 3, 3)</code>]
    InitializeCube --> MainLoop["לולאה ראשית:<br><code>while True</code>"]
    MainLoop --> InputCommand[קבלת קלט מהמשתמש<br><code>command = input(...)</code>]
    InputCommand --> CheckEnd[בדיקה: <code>command == 'END' or command == '0'</code>]
    CheckEnd -- כן --> End[סיום המשחק<br><code>break</code>]
    CheckEnd -- לא --> SplitCommand[פיצול הקלט<br><code>parts = command.split()</code>]
    SplitCommand --> CheckCoordinates[בדיקה: <code>len(parts) == 3</code>]
    CheckCoordinates -- כן --> TryConvertCoordinates[ניסיון המרת קואורדינטות<br><code>x, y, z = map(int, parts)</code>]
     TryConvertCoordinates --> ValidateCoordinates[בדיקת קואורדינטות<br><code>1 <= x <= 3 and 1 <= y <= 3 and 1 <= z <= 3</code>]
    ValidateCoordinates -- כן --> GetCubePosition[קבלת מיקום הקוביה<br><code>pos = get_cube_position(cube, x, y, z)</code>]
    GetCubePosition --> OutputPosition[פלט מיקום הקוביה<br><code>print(f"Положение кубика ({x}, {y}, {z}): {pos}")</code>]
    OutputPosition --> MainLoop
     ValidateCoordinates -- לא --> CoordinatesOutOfRange[פלט הודעת שגיאה על קואורדינטות שגויות]
     CoordinatesOutOfRange --> MainLoop
     TryConvertCoordinates -- שגיאה --> InvalidCoordinates[פלט הודעה על קואורדינטות לא תקינות]
     InvalidCoordinates --> MainLoop
    CheckCoordinates -- לא --> CheckRotationCommand[בדיקה: <code>len(parts) == 1</code>]
   CheckRotationCommand -- כן --> CheckXCommand[בדיקה: <code>command == 'X'</code>]
   CheckXCommand -- כן --> RotateX[סיבוב הקוביה סביב ציר X<br><code>cube = rotate_x(cube)</code>]
    RotateX --> OutputRotateX[פלט הודעה: "הקוביה סובבה סביב ציר X"]
     OutputRotateX --> MainLoop
    CheckXCommand -- לא --> CheckYCommand[בדיקה: <code>command == 'Y'</code>]
    CheckYCommand -- כן --> RotateY[סיבוב הקוביה סביב ציר Y<br><code>cube = rotate_y(cube)</code>]
    RotateY --> OutputRotateY[פלט הודעה: "הקוביה סובבה סביב ציר Y"]
     OutputRotateY --> MainLoop
     CheckYCommand -- לא --> CheckZCommand[בדיקה: <code>command == 'Z'</code>]
    CheckZCommand -- כן --> RotateZ[סיבוב הקוביה סביב ציר Z<br><code>cube = rotate_z(cube)</code>]
    RotateZ --> OutputRotateZ[פלט הודעה: "הקוביה סובבה סביב ציר Z"]
    OutputRotateZ --> MainLoop
    CheckZCommand -- לא --> UnknownCommand[פלט הודעה על פקודה לא מוכרת]
    UnknownCommand --> MainLoop
     CheckRotationCommand -- לא --> InvalidInputFormat[פלט הודעה על פורמט קלט לא תקין]
     InvalidInputFormat --> MainLoop
```
## <explanation>
### ייבוא מודולים
- **`import numpy as np`**:
    - **מטרה**: מודול `numpy` מספק תמיכה במערכים רב-ממדיים ובפונקציות מתמטיות מותאמות לעבודה עם מערכים כאלה.
    - **קשר לחבילות `src`**: אין קשר ישיר לחבילות `src` אחרות, זהו מודול חיצוני.
    - **שימוש**: משמש ליצירת הקוביה התלת ממדית, לביצוע פעולות סיבוב עליה, ולגישה לערכים שבתוכה.
    - **דוגמאות**:
      - `np.arange(1, 28)`: יוצר מערך של מספרים מ-1 עד 27.
      - `np.reshape(3, 3, 3)`: משנה את צורת המערך למערך תלת-ממדי בגודל 3x3x3.
      - `np.rot90(cube, k=-1, axes=(1, 2))`: מסובב את המערך ב-90 מעלות נגד כיוון השעון בצירים נתונים.

### פונקציות

1.  **`rotate_x(cube)`**:
    -   **פרמטרים**: `cube` - מערך תלת ממדי המייצג את הקוביה.
    -   **ערך מוחזר**: מערך תלת ממדי חדש שהוא תוצאה של סיבוב הקוביה סביב ציר X.
    -   **מטרה**: לסובב את הקוביה 90 מעלות נגד כיוון השעון סביב ציר X.
    -   **דוגמאות**:
        - קריאה לפונקציה: `rotated_cube = rotate_x(cube)`
        - אם `cube` הוא מערך תלת ממדי, `rotated_cube` יהיה אותו מערך לאחר סיבוב.
2.  **`rotate_y(cube)`**:
    -   **פרמטרים**: `cube` - מערך תלת ממדי המייצג את הקוביה.
    -   **ערך מוחזר**: מערך תלת ממדי חדש שהוא תוצאה של סיבוב הקוביה סביב ציר Y.
    -   **מטרה**: לסובב את הקוביה 90 מעלות נגד כיוון השעון סביב ציר Y.
    -   **דוגמאות**:
        - קריאה לפונקציה: `rotated_cube = rotate_y(cube)`
        - אם `cube` הוא מערך תלת ממדי, `rotated_cube` יהיה אותו מערך לאחר סיבוב.
3.  **`rotate_z(cube)`**:
    -   **פרמטרים**: `cube` - מערך תלת ממדי המייצג את הקוביה.
    -   **ערך מוחזר**: מערך תלת ממדי חדש שהוא תוצאה של סיבוב הקוביה סביב ציר Z.
    -   **מטרה**: לסובב את הקוביה 90 מעלות נגד כיוון השעון סביב ציר Z.
    -   **דוגמאות**:
        - קריאה לפונקציה: `rotated_cube = rotate_z(cube)`
        - אם `cube` הוא מערך תלת ממדי, `rotated_cube` יהיה אותו מערך לאחר סיבוב.
4.  **`get_cube_position(cube, x, y, z)`**:
    -   **פרמטרים**:
        -   `cube`: מערך תלת ממדי המייצג את הקוביה.
        -   `x`, `y`, `z`: קואורדינטות של הקוביה הפנימית.
    -   **ערך מוחזר**: הערך של הקוביה הפנימית במיקום (x, y, z).
    -   **מטרה**: להחזיר את ערך הקוביה הפנימית במיקום הנתון.
    -   **דוגמאות**:
        - קריאה לפונקציה: `position = get_cube_position(cube, 2, 1, 3)`
        - אם הקוביה היא מערך, הפונקציה תחזיר את ערך הקוביה במיקום (2, 1, 3) בתוך המערך.

### משתנים
-   **`cube`**:
    -   **סוג**: `numpy.ndarray`.
    -   **שימוש**: מערך תלת ממדי המייצג את הקוביה, הערכים שלו משתנים לאחר פעולות סיבוב.
-   **`command`**:
    -   **סוג**: `str`.
    -   **שימוש**: מחרוזת שמכילה את הקלט מהמשתמש.
-    **`parts`**:
    -   **סוג**: `list` של `str`.
    -   **שימוש**: רשימה של מחרוזות, שמכילה את הקלט מהמשתמש, אחרי פיצול לפי רווחים.
-   **`x`, `y`, `z`**:
    -   **סוג**: `int`.
    -   **שימוש**: קואורדינטות של הקוביה הפנימית שנבחרה ע"י המשתמש.
-   **`pos`**:
   -   **סוג**: `int`
   -   **שימוש**: הערך של הקוביה הפנימית שנבחרה ע"י המשתמש במיקום הנתון.

### בעיות אפשריות ותחומים לשיפור
1.  **קלט לא תקין**: הקוד מטפל במקרים של קלט שגוי, אבל ניתן לשפר את הטיפול בשגיאות, למשל, להדפיס הודעות שגיאה יותר ברורות למשתמש.
2.  **ממשק משתמש**: ממשק המשתמש בסיסי וכולל רק פלט טקסטואלי. ניתן לשפר את ממשק המשתמש על ידי הוספת תצוגה גרפית של הקוביה והסיבובים, דבר שיכול להקל על ההבנה של פעולת המשחק.
3.  **יעילות**: ניתן לשפר את יעילות הקוד אם הוא יכלול שימוש בכמה משתני עזר למטריצת הקוביה, דבר שיכול לייעל את החישובים בפונקציות סיבוב.

### שרשרת קשרים עם חלקים אחרים בפרויקט
- הקוד הנוכחי הוא משחק עצמאי ואינו תלוי בחלקים אחרים בפרויקט. אין לו קשר ישיר עם חבילות `src` אחרות, אבל הוא יכול להשתלב עם ממשק משתמש גרפי או עם מערכת ניהול משחקים אם יפותח בעתיד.