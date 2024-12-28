<AMAZIN>:
=================
קושי: 5
-----------------
המשחק "AMAZIN" הוא משחק בו המשתמש מתחיל במבוך בגודל 20x20, המורכב מתאים הממוקמים בקואורדינטות (X,Y). המטרה היא להגיע לקצה המבוך (Y=20).
המשתמש מתקדם צעד אחד בכל פעם בכיוון שהמשתמש בוחר (צפון, דרום, מזרח, מערב) באמצעות הזנת קוד כיוון (1=צפון, 2=מזרח, 3=דרום, 4=מערב). בכל צעד המשתמש מקבל את הקואורדינטות הנוכחיות שלו.
במבוך קיימים "קירות" אקראיים המונעים מהשחקן להתקדם. המשתמש צריך לנווט במבוך ולהגיע לקו הסיום Y=20.

חוקי המשחק:
1. המשתמש מתחיל בנקודה (10,1) במבוך בגודל 20x20.
2. המשתמש יכול לבחור לנוע צעד אחד בכל פעם באחד מארבעת הכיוונים: צפון (1), מזרח (2), דרום (3), מערב (4).
3. אם המשתמש מנסה לצאת מגבולות המבוך, לא יתבצע שינוי במיקום השחקן ויוצג רמז "לא חוקי".
4. חלק מהצעדים חסומים על ידי "קירות" אקראיים. אם השחקן פוגע בקיר, לא יתבצע שינוי במיקום השחקן ויוצג רמז "פגעת בקיר".
5. המטרה היא להגיע לקו הסיום Y=20.
6. המשחק מסתיים כאשר המשתמש מגיע לקו הסיום Y=20, אז תוצג הודעת ניצחון.
-----------------
אלגוריתם:
1. אתחל את מיקום השחקן ל-X=10 ו-Y=1.
2. הגדר את גודל המבוך ל-20x20 (לא מיושם ב-BASIC).
3. צור מבוך עם "קירות" אקראיים (לא מיושם באופן מלא ב-BASIC).
4. התחל לולאה ראשית:
   4.1. הצג את מיקום השחקן הנוכחי (X,Y).
   4.2. קבל מהמשתמש קלט עבור כיוון התנועה (1=צפון, 2=מזרח, 3=דרום, 4=מערב).
   4.3. בצע בדיקה האם הכיוון שהוזן חוקי (בין 1 ל-4).
       4.3.1. אם הכיוון לא חוקי הצג הודעה "לא חוקי" וחזור ל-4.1.
   4.4. חשב את המיקום הבא של השחקן בהתאם לכיוון.
   4.5. בצע בדיקה האם המיקום הבא חוקי (בתוך גבולות המבוך).
       4.5.1 אם המיקום החדש לא חוקי (יצא מגבולות המבוך), אל תשנה את מיקום השחקן, הצג הודעה "לא חוקי" וחזור ל-4.1.
   4.6. בצע בדיקה האם יש "קיר" במיקום הבא (לא מיושם באופן מלא ב-BASIC).
       4.6.1 אם יש קיר, אל תשנה את מיקום השחקן, הצג הודעה "פגעת בקיר" וחזור ל-4.1.
   4.7. עדכן את מיקום השחקן למיקום החדש.
   4.8. בדוק אם השחקן הגיע לקו הסיום (Y=20).
       4.8.1 אם השחקן הגיע לקו הסיום, הצג הודעת ניצחון וסיים את המשחק.
   4.9 המשך את הלולאה וחזור ל 4.1.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:<br><code><b>playerPositionX = 10</b></code><br><code><b>playerPositionY = 1</b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: כל עוד לא הגענו לקו הסיום"}
    LoopStart --> DisplayPosition["הצג מיקום נוכחי:<br><code><b>(playerPositionX, playerPositionY)</b></code>"]
    DisplayPosition --> InputDirection["קבל קלט כיוון מהמשתמש:<br><code><b>direction</b></code> (1-4)"]
    InputDirection --> ValidateDirection{"בדיקה: האם <code><b>direction</b></code> בין 1 ל-4?"}
    ValidateDirection -- לא --> OutputInvalidDirection["הצג הודעה: <b>לא חוקי</b>"]
    OutputInvalidDirection --> LoopStart
    ValidateDirection -- כן --> CalculateNextPosition["חשב מיקום הבא:<br>בהתאם <code><b>direction</b></code>"]
    CalculateNextPosition --> ValidateNextPosition{"בדיקה: האם המיקום הבא בתוך גבולות המבוך?"}
    ValidateNextPosition -- לא --> OutputInvalidMove["הצג הודעה: <b>לא חוקי</b>"]
    OutputInvalidMove --> LoopStart
    ValidateNextPosition -- כן --> CheckWall{"בדיקה: האם יש קיר במיקום הבא?"}
    CheckWall -- כן --> OutputWallCollision["הצג הודעה: <b>פגעת בקיר</b>"]
    OutputWallCollision --> LoopStart
    CheckWall -- לא --> UpdatePosition["עדכן מיקום השחקן"]
    UpdatePosition --> CheckGoal{"בדיקה: האם <code><b>playerPositionY == 20</b></code>?"}
    CheckGoal -- לא --> LoopStart
    CheckGoal -- כן --> OutputWin["הצג הודעה: <b>ניצחת!</b>"]
    OutputWin --> End["סוף"]
```
Legenda:
* **Start** - התחלת המשחק.
*   **InitializeVariables** - אתחול מיקום השחקן ההתחלתי: playerPositionX = 10 ו- playerPositionY = 1.
*   **LoopStart** - תחילת הלולאה, אשר תמשיך עד שהשחקן יגיע לקו הסיום.
*  **DisplayPosition** - הצגת מיקום השחקן הנוכחי על המסך.
*   **InputDirection** - קבלת קלט כיוון מהמשתמש (1=צפון, 2=מזרח, 3=דרום, 4=מערב).
*   **ValidateDirection** - בדיקה האם הקלט של הכיוון חוקי (בין 1 ל-4).
*   **OutputInvalidDirection** - הצגת הודעה שהכיוון לא חוקי.
*   **CalculateNextPosition** - חישוב המיקום הבא של השחקן בהתאם לכיוון שהוזן.
*   **ValidateNextPosition** - בדיקה האם המיקום הבא הוא בתוך גבולות המבוך.
*  **OutputInvalidMove** - הצגת הודעה שהתנועה לא חוקית, השחקן יצא מגבולות המבוך.
*  **CheckWall** - בדיקה האם יש "קיר" במיקום הבא (לא מיושם באופן מלא).
*  **OutputWallCollision** - הצגת הודעה שהשחקן פגע בקיר.
*   **UpdatePosition** - עדכון מיקום השחקן למיקום החדש.
*   **CheckGoal** - בדיקה האם השחקן הגיע לקו הסיום (Y=20).
*   **OutputWin** - הצגת הודעת ניצחון אם השחקן הגיע לקו הסיום.
*   **End** - סוף המשחק.
"""
import random

def play_amazin_game():
    """
    משחק המבוך "AMAZIN" בו השחקן מנסה להגיע לקו הסיום.
    """

    # 1. אתחול מיקום השחקן
    playerPositionX = 10
    playerPositionY = 1

    # 2. הגדרת גודל המבוך (לא מיושם באופן מלא ב-BASIC)
    mazeSizeX = 20
    mazeSizeY = 20

    # 3. יצירת "קירות" אקראיים (לא מיושם באופן מלא ב-BASIC)
    # במקום קירות, נגדיר סיכוי לפגוש קיר (הקוד המקורי ב-BASIC אינו מיישם קירות)
    wall_probability = 0.2 # 20% סיכוי לפגוש קיר

    # 4. לולאת המשחק הראשית
    while True:
        # 4.1. הצגת מיקום השחקן
        print(f"מיקום נוכחי: (X={playerPositionX}, Y={playerPositionY})")

        # 4.2. קבלת קלט כיוון מהמשתמש
        try:
            direction = int(input("בחר כיוון (1=צפון, 2=מזרח, 3=דרום, 4=מערב): "))
        except ValueError:
            print("קלט לא חוקי. אנא הזן מספר שלם בין 1 ל-4.")
            continue

        # 4.3. בדיקה האם הכיוון חוקי
        if direction < 1 or direction > 4:
            print("לא חוקי. אנא בחר כיוון בין 1 ל-4.")
            continue

        # 4.4. חישוב המיקום הבא
        newPositionX = playerPositionX
        newPositionY = playerPositionY

        if direction == 1:  # צפון
            newPositionY += 1
        elif direction == 2:  # מזרח
            newPositionX += 1
        elif direction == 3:  # דרום
            newPositionY -= 1
        elif direction == 4:  # מערב
            newPositionX -= 1

        # 4.5 בדיקה האם המיקום הבא חוקי (בתוך גבולות המבוך)
        if newPositionX < 1 or newPositionX > mazeSizeX or newPositionY < 1 or newPositionY > mazeSizeY:
           print("לא חוקי. אתה מנסה לצאת מגבולות המבוך")
           continue

        # 4.6. בדיקה האם יש "קיר" במיקום הבא (לא מיושם באופן מלא ב-BASIC)
        if random.random() < wall_probability:
            print("פגעת בקיר!")
            continue

        # 4.7. עדכון מיקום השחקן
        playerPositionX = newPositionX
        playerPositionY = newPositionY

        # 4.8. בדיקה האם הגיע לקו הסיום
        if playerPositionY == mazeSizeY:
            print("ניצחת!")
            break

if __name__ == "__main__":
    play_amazin_game()

"""
הסבר מפורט לקוד:
1.  **ייבוא המודול `random`**:
    - `import random`: מייבא את המודול random, שמשמש ליצירת מספרים אקראיים עבור "קירות" (סימולציה בלבד)
2.  **הגדרת הפונקציה `play_amazin_game()`**:
    -  הפונקציה מכילה את הלוגיקה הראשית של המשחק.
3.  **אתחול משתנים**:
    - `playerPositionX = 10`: מאתחל את מיקום השחקן בציר ה-X ל-10.
    - `playerPositionY = 1`: מאתחל את מיקום השחקן בציר ה-Y ל-1.
    - `mazeSizeX = 20`, `mazeSizeY = 20`: מגדיר את גודל המבוך ל-20x20 (לא מיושם ב-BASIC).
    - `wall_probability = 0.2`: מגדיר את הסיכוי לפגוש "קיר" כ-20%.
4.  **לולאת המשחק הראשית (`while True`):**
    - הלולאה ממשיכה עד שהשחקן מגיע לקו הסיום.
    - `print(f"מיקום נוכחי: (X={playerPositionX}, Y={playerPositionY})")`: מציג את מיקום השחקן הנוכחי.
    - **קבלת קלט כיוון:**
    - `try...except ValueError`: מטפל במקרה שהמשתמש מזין קלט שאינו מספר שלם.
    - `direction = int(input("בחר כיוון (1=צפון, 2=מזרח, 3=דרום, 4=מערב): "))`: מבקש מהמשתמש לבחור כיוון וממיר אותו למספר שלם.
    - `if direction < 1 or direction > 4:`: בדיקה האם הכיוון שהוזן חוקי. אם לא, מוצגת הודעה וממשיכים לסיבוב הבא של הלולאה.
    - **חישוב המיקום הבא:**
    - `newPositionX = playerPositionX`, `newPositionY = playerPositionY`: יוצר עותקים של מיקום השחקן הנוכחי, כדי שאם התנועה לא תהיה חוקית, המיקום לא ישתנה.
    - קובע את המיקום החדש בהתאם לכיוון שהוזן (1=צפון, 2=מזרח, 3=דרום, 4=מערב).
    - **בדיקת מיקום חדש:**
        - `if newPositionX < 1 or newPositionX > mazeSizeX or newPositionY < 1 or newPositionY > mazeSizeY:`: בודק האם השחקן יצא מגבולות המבוך.
        - אם כן, מוצגת הודעה והמשחק חוזר לתחילת הלולאה.
    - **בדיקת פגיעה ב"קיר":**
        - `if random.random() < wall_probability:`: מדמה פגיעה ב"קיר" בהסתברות מסוימת. אם כן, מוצגת הודעה והמשחק חוזר לתחילת הלולאה.
    - **עדכון מיקום השחקן:**
        - `playerPositionX = newPositionX`, `playerPositionY = newPositionY`: מעדכן את מיקום השחקן בהתאם למיקום החדש.
    - **בדיקה האם הגיע לקו הסיום:**
        - `if playerPositionY == mazeSizeY:`: בודק האם השחקן הגיע לקו הסיום (Y=20). אם כן, מוצגת הודעת ניצחון והמשחק מסתיים.
5.  **הפעלת המשחק**:
    - `if __name__ == "__main__":`: בלוק זה מבטיח שהפונקציה `play_amazin_game()` תופעל רק אם הקובץ מופעל ישירות, ולא אם הוא מיובא כמודול.
    - `play_amazin_game()`: קריאה לפונקציה להפעלת המשחק.
"""
