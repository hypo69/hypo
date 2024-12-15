"""
LIFE 2:
=================
קושי: 5
-----------------
המשחק "LIFE 2" מדמה סימולציה של אוטומט תאי פשוט, המכונה "משחק החיים" של ג'ון קונוויי. המשחק מתרחש על גבי לוח דו-ממדי, כאשר כל תא יכול להיות "חי" או "מת". בכל צעד, מצב התאים משתנה בהתאם למספר השכנים החיים שלהם. זהו משחק ללא שחקן אמיתי, וההתפתחות של התאים מוצגת כסדרה של דורות.

חוקי המשחק:
1. הלוח מיוצג על ידי מטריצה דו-ממדית.
2. כל תא יכול להיות במצב "חי" (1) או "מת" (0).
3. בתחילת המשחק, הלוח מאותחל באופן אקראי או מוגדר מראש.
4. בכל דור, כל תא מעודכן על פי הכללים הבאים:
    - תא חי עם פחות משני שכנים חיים מת (תת-אוכלוסיה).
    - תא חי עם שניים או שלושה שכנים חיים נשאר בחיים.
    - תא חי עם יותר משלושה שכנים חיים מת (צפיפות יתר).
    - תא מת עם בדיוק שלושה שכנים חיים הופך לחי (רבייה).
5. המשחק ממשיך להתפתח עד שהמשתמש עוצר אותו.

-----------------
אלגוריתם:
1. אתחל את גודל הלוח (שורות ועמודות).
2. צור לוח אקראי או מוגדר מראש של תאים, כאשר כל תא יכול להיות חי (1) או מת (0).
3. הצג את הלוח הנוכחי.
4. התחל לולאה אינסופית:
    4.1. צור לוח חדש (דור חדש).
    4.2. עבור על כל תא בלוח הנוכחי:
        4.2.1. ספור את מספר השכנים החיים לתא הנוכחי.
        4.2.2. עדכן את מצב התא בלוח החדש לפי חוקי המשחק (תת-אוכלוסיה, הישרדות, צפיפות יתר, רבייה).
    4.3. החלף את הלוח הנוכחי בלוח החדש.
    4.4. הצג את הלוח החדש.
    4.5. המתן זמן קצר.
5. המשחק ממשיך להתפתח עד שהמשתמש עוצר אותו ידנית.

-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeGrid["<p align='left'>אתחול הלוח:
    <code><b>
    rows = 20
    cols = 60
    grid = random(rows, cols)
    </b></code></p>"]
    InitializeGrid --> DisplayGrid["הצגת הלוח הנוכחי"]
    DisplayGrid --> LoopStart{"תחילת לולאה אינסופית: לולאת דורות"}
    LoopStart --> CreateNewGrid["<p align='left'>יצירת לוח חדש (דור הבא):
    <code><b>newGrid = empty(rows, cols)</b></code></p>"]
    CreateNewGrid --> LoopRows{"לולאה על שורות: לכל שורה"}
    LoopRows --> LoopCols{"לולאה על עמודות: לכל עמודה"}
    LoopCols --> CountNeighbors["<p align='left'>ספירת שכנים חיים לתא הנוכחי:
    <code><b>
    neighbors = count_live_neighbors(grid, row, col)
    </b></code></p>"]
    CountNeighbors --> UpdateCell{"<p align='left'>עדכון מצב התא בלוח החדש:
    <code><b>
    newGrid[row][col] = update_cell_state(grid[row][col], neighbors)
    </b></code></p>"}
    UpdateCell --> LoopColsEnd{"סוף לולאה על עמודות"}
    LoopColsEnd -- לא --> LoopCols
    LoopColsEnd -- כן --> LoopRowsEnd{"סוף לולאה על שורות"}
    LoopRowsEnd -- לא --> LoopRows
    LoopRowsEnd -- כן --> UpdateCurrentGrid["<code><b>grid = newGrid</b></code>"]
    UpdateCurrentGrid --> DisplayGridNew["הצגת הלוח החדש"]
    DisplayGridNew --> Wait["המתנה קצרה"]
    Wait --> LoopStart
    LoopStart -- עצור --> End["סוף"]

```
Legenda:
    Start - התחלת התוכנית.
    InitializeGrid - אתחול הלוח: הגדרת גודל הלוח (שורות ועמודות) ויצירת לוח אקראי התחלתי.
    DisplayGrid - הצגת הלוח הנוכחי.
    LoopStart - תחילת הלולאה האינסופית של דורות.
    CreateNewGrid - יצירת לוח חדש (דור הבא) ריק.
    LoopRows - תחילת לולאה על שורות הלוח.
    LoopCols - תחילת לולאה על עמודות הלוח.
    CountNeighbors - ספירת מספר השכנים החיים לתא הנוכחי.
    UpdateCell - עדכון מצב התא בלוח החדש בהתאם לחוקי המשחק.
    LoopColsEnd - סוף הלולאה על העמודות.
    LoopRowsEnd - סוף הלולאה על השורות.
    UpdateCurrentGrid - עדכון הלוח הנוכחי לדור החדש.
    DisplayGridNew - הצגת הלוח החדש (הדור הבא).
    Wait - המתנה קצרה לפני תחילת הדור הבא.
    End - סוף התוכנית (המשחק מסתיים כאשר המשתמש עוצר אותו ידנית).
"""
```python
import random
import time
import os

# הגדרת גודל הלוח
ROWS = 20
COLS = 60

# פונקציה ליצירת לוח התחלתי אקראי
def create_grid():
    """
    יוצרת לוח אקראי של תאים חיים ומתים.

    Returns:
        list: לוח דו-ממדי של תאים (0 או 1).
    """
    return [[random.randint(0, 1) for _ in range(COLS)] for _ in range(ROWS)]

# פונקציה להצגת הלוח
def display_grid(grid):
    """
    מדפיסה את הלוח למסך, כאשר תא חי מסומן ב-*, ותא מת מסומן ברווח.

    Args:
        grid (list): הלוח להצגה.
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # ניקוי מסך
    for row in grid:
        print(''.join('*' if cell == 1 else ' ' for cell in row))

# פונקציה לספירת שכנים חיים
def count_live_neighbors(grid, row, col):
    """
    סופרת את מספר השכנים החיים של תא נתון.
    Args:
        grid (list): הלוח.
        row (int): שורת התא.
        col (int): עמודת התא.
    Returns:
        int: מספר השכנים החיים.
    """
    count = 0
    for i in range(max(0, row - 1), min(ROWS, row + 2)):
        for j in range(max(0, col - 1), min(COLS, col + 2)):
            if (i, j) != (row, col):
                count += grid[i][j]
    return count

# פונקציה לעדכון מצב התא
def update_cell_state(cell, neighbors):
    """
    מעדכנת את מצב התא בהתאם לחוקי המשחק.

    Args:
        cell (int): מצב התא הנוכחי (0 או 1).
        neighbors (int): מספר השכנים החיים.

    Returns:
        int: מצב התא החדש (0 או 1).
    """
    if cell == 1:  # תא חי
        if neighbors < 2 or neighbors > 3:
            return 0  # מת כתוצאה מתת-אוכלוסיה או צפיפות יתר
        else:
            return 1  # נשאר חי
    else:  # תא מת
        if neighbors == 3:
            return 1  # הופך לחי כתוצאה מרבייה
        else:
            return 0  # נשאר מת

# פונקציה ליצירת דור חדש
def create_new_generation(grid):
    """
    יוצרת דור חדש של הלוח לפי חוקי המשחק.
    Args:
        grid (list): הלוח הנוכחי.
    Returns:
        list: לוח חדש (הדור הבא).
    """
    new_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    for row in range(ROWS):
        for col in range(COLS):
            neighbors = count_live_neighbors(grid, row, col)
            new_grid[row][col] = update_cell_state(grid[row][col], neighbors)
    return new_grid

# פונקציית משחק ראשית
def play_life():
    """
    מפעילה את משחק החיים.
    """
    grid = create_grid()  # יצירת לוח התחלתי
    while True:  # לולאה אינסופית
        display_grid(grid)  # הצגת הלוח
        grid = create_new_generation(grid)  # יצירת דור חדש
        time.sleep(0.1)  # המתנה קצרה בין דורות

# הפעלת המשחק
if __name__ == "__main__":
    play_life()
```
"""
הסבר הקוד:
1.  **ייבוא מודולים**:
    - `import random`: ייבוא המודול `random` ליצירת ערכים אקראיים ללוח ההתחלתי.
    - `import time`: ייבוא המודול `time` לשליטה בקצב עדכון הלוח.
    - `import os`: ייבוא מודול `os` לניקוי המסך.
2.  **קבועים**:
    - `ROWS = 20`: מספר השורות בלוח.
    - `COLS = 60`: מספר העמודות בלוח.
3.  **פונקציה `create_grid()`**:
    - יוצרת לוח התחלתי אקראי.
    - מחזירה לוח דו-ממדי, כאשר כל תא מקבל ערך אקראי 0 או 1 (תא מת או חי).
4.  **פונקציה `display_grid(grid)`**:
    - מקבלת את הלוח כקלט ומדפיסה אותו לקונסולה.
    - מנקה את המסך לפני ההדפסה.
    - תאים חיים מוצגים כ-`*`, ותאים מתים כרווחים.
5.  **פונקציה `count_live_neighbors(grid, row, col)`**:
    - מקבלת את הלוח, את שורת התא ואת עמודת התא.
    - סופרת את מספר השכנים החיים של התא הנתון.
    - מחזירה את מספר השכנים החיים.
6.  **פונקציה `update_cell_state(cell, neighbors)`**:
    - מקבלת את מצב התא הנוכחי (חי או מת) ואת מספר השכנים החיים.
    - מעדכנת את מצב התא בהתאם לחוקי המשחק:
        - תא חי עם פחות משני שכנים חיים מת.
        - תא חי עם שניים או שלושה שכנים חיים נשאר בחיים.
        - תא חי עם יותר משלושה שכנים חיים מת.
        - תא מת עם שלושה שכנים חיים הופך לחי.
    - מחזירה את המצב החדש של התא.
7.  **פונקציה `create_new_generation(grid)`**:
    - מקבלת את הלוח הנוכחי ויוצרת את הדור הבא.
    - יוצרת לוח חדש, ובאמצעות לולאה, עבור כל תא בלוח הנוכחי, מעדכנת את מצב התא החדש לפי חוקי המשחק, ומוסיפה אותו ללוח החדש.
    - מחזירה את הלוח החדש (הדור הבא).
8.  **פונקציה `play_life()`**:
    - יוצרת את הלוח הראשוני באמצעות קריאה לפונקציה `create_grid()`.
    - מתחילה לולאה אינסופית.
    - בכל איטרציה של הלולאה, היא:
        - מדפיסה את הלוח באמצעות `display_grid()`.
        - יוצרת את הדור הבא באמצעות `create_new_generation()`.
        - מחכה זמן קצר באמצעות `time.sleep(0.1)` כדי להאט את קצב המשחק.
9.  **הפעלה ראשית של הקוד**:
    - הקוד `if __name__ == "__main__":` מבטיח שפונקציית `play_life()` תופעל רק כאשר הקובץ מופעל ישירות.
"""
