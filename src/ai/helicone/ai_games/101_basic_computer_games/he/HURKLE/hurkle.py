# HURKLE:
=================
קושי: 5
-----------------
<p>משחק "HURKLE" הוא משחק ניחושים שבו השחקן מנסה למצוא את מיקומו של "HURKLE" (במקור, שמו של רובוט).</p>
<p>ה-HURKLE ממוקם במיקום אקראי על לוח של 10 על 10, והשחקן מנסה לנחש את הקואורדינטות שלו (X,Y). לאחר כל ניחוש, השחקן מקבל רמז המציין את המרחק של הניחוש מהמיקום האמיתי של ה-HURKLE, אך לא בכיוון מסוים.</p>
<p>המטרה היא למצוא את ה-HURKLE במספר הניחושים המינימלי.</p>
-----------------
חוקי המשחק:
1. ה-HURKLE ממוקם באופן אקראי על לוח בגודל 10 על 10.
2. השחקן מזין זוג קואורדינטות (X, Y) בין 1 ל-10.
3. לאחר כל ניחוש, המשחק מציג את המרחק בין הניחוש למיקום של ה-HURKLE.
4. המשחק ממשיך עד שהשחקן מנחש נכון את הקואורדינטות של ה-HURKLE.
5. מספר הניחושים נספר.
-----------------
אלגוריתם:
1. הגדר את מספר הניסיונות ל-0.
2. צור קואורדינטות אקראיות (HURKLE_X, HURKLE_Y) בין 1 ל-10 עבור מיקום ה-HURKLE.
3. התחל לולאה "כל עוד ה-HURKLE לא נמצא":
    3.1 הגדל את מספר הניסיונות ב-1.
    3.2 בקש מהשחקן להזין קואורדינטות (X, Y).
    3.3 חשב את המרחק בין הניחוש למיקום ה-HURKLE באמצעות נוסחת מרחק בין שתי נקודות.
    3.4 אם המרחק הוא 0, סימן שהשחקן ניחש נכון, עבור לשלב 4.
    3.5 הצג לשחקן את המרחק.
4. הצג הודעת ניצחון עם מספר הניסיונות.
5. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    numberOfGuesses = 0<br>
    hurkleX = random(1, 10)<br>
    hurkleY = random(1, 10)
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: כל עוד לא נוחש"}
    LoopStart -- כן --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputCoordinates["קלט קואורדינטות מהמשתמש: <code><b>userX, userY</b></code>"]
    InputCoordinates --> CalculateDistance["חישוב מרחק: <code><b>distance = sqrt((userX - hurkleX)^2 + (userY - hurkleY)^2)</b></code>"]
    CalculateDistance --> CheckDistance{"בדיקה: <code><b>distance == 0?</b></code>"}
    CheckDistance -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES!</b>"]
    OutputWin --> End["סוף"]
    CheckDistance -- לא --> OutputDistance["הצגת מרחק: <b>Distance is {distance}</b>"]
    OutputDistance --> LoopStart
    LoopStart -- לא --> End
```
Legenda:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: numberOfGuesses (מספר הניסיונות) מאותחל ל-0, ו-hurkleX ו-hurkleY (קואורדינטות ה-HURKLE) נוצרים באקראי בין 1 ל-10.
    LoopStart - תחילת הלולאה, הממשיכה כל עוד ה-HURKLE לא נוחש.
    IncreaseGuesses - הגדלת מונה הניסיונות ב-1.
    InputCoordinates - קלט קואורדינטות מהמשתמש ושמירתן במשתנים userX ו-userY.
    CalculateDistance - חישוב המרחק בין הניחוש למיקום ה-HURKLE.
    CheckDistance - בדיקה האם המרחק שווה ל-0 (האם ה-HURKLE נוחש).
    OutputWin - הצגת הודעת ניצחון, אם ה-HURKLE נוחש, עם מספר הניסיונות.
    End - סוף התוכנית.
    OutputDistance - הצגת המרחק מהניחוש למיקום ה-HURKLE.

```python
import random
import math

# אתחול מונה הניסיונות
numberOfGuesses = 0
# יצירת קואורדינטות אקראיות בין 1 ל-10 עבור מיקום ה-HURKLE
hurkleX = random.randint(1, 10)
hurkleY = random.randint(1, 10)


# לולאת המשחק הראשית
while True:
    # הגדלת מונה הניסיונות
    numberOfGuesses += 1
    # בקשת קלט קואורדינטות מהמשתמש
    try:
        userX = int(input("הכנס את קואורדינטת X (בין 1 ל-10): "))
        userY = int(input("הכנס את קואורדינטת Y (בין 1 ל-10): "))
        # בדיקה שהקלט הוא בטווח המותר
        if not (1 <= userX <= 10 and 1 <= userY <= 10):
            print("קואורדינטות צריכות להיות בין 1 ל-10.")
            continue
    except ValueError:
        print("אנא הזן מספרים שלמים.")
        continue
    # חישוב המרחק בין הניחוש למיקום ה-HURKLE
    distance = math.sqrt((userX - hurkleX)**2 + (userY - hurkleY)**2)
    # בדיקה האם ה-HURKLE נוחש
    if distance == 0:
        print(f"מזל טוב! מצאת את ה-HURKLE ב-{numberOfGuesses} ניסיונות!")
        break  # סיום הלולאה אם ה-HURKLE נוחש
    else:
      print(f"המרחק מה-HURKLE הוא: {distance:.2f}")


```
<br>
הסבר הקוד:
1. **ייבוא מודולים**:
   - `import random`: ייבוא המודול `random` לצורך יצירת מספרים אקראיים.
   - `import math`: ייבוא המודול `math` לצורך שימוש בפונקציה `sqrt` לחישוב שורש ריבועי.
2. **אתחול משתנים**:
   - `numberOfGuesses = 0`: אתחול משתנה לספירת מספר הניסיונות, מתחיל מ-0.
   - `hurkleX = random.randint(1, 10)`: יצירת קואורדינטת X אקראית בין 1 ל-10 למיקום ה-HURKLE.
   - `hurkleY = random.randint(1, 10)`: יצירת קואורדינטת Y אקראית בין 1 ל-10 למיקום ה-HURKLE.
3. **לולאת המשחק `while True:`**:
   - לולאה אינסופית, הממשיכה עד שהמשתמש מנחש את מיקום ה-HURKLE.
   - `numberOfGuesses += 1`: הגדלת מונה הניסיונות ב-1 בכל סיבוב של הלולאה.
4. **קבלת קלט מהמשתמש**:
   - `try...except ValueError`: בלוק try-except לטיפול בשגיאות קלט (אם המשתמש מכניס משהו שאינו מספר שלם).
   - `userX = int(input("הכנס את קואורדינטת X (בין 1 ל-10): "))`: בקשת קואורדינטת X מהמשתמש והמרתה למספר שלם.
   - `userY = int(input("הכנס את קואורדינטת Y (בין 1 ל-10): "))`: בקשת קואורדינטת Y מהמשתמש והמרתה למספר שלם.
   -  `if not (1 <= userX <= 10 and 1 <= userY <= 10):`: בדיקה האם הקואורדינטות שהוזנו נמצאות בטווח המותר (1 עד 10), במידה ולא, מוצגת הודעה והלולאה ממשיכה לסיבוב הבא.
5. **חישוב המרחק**:
   - `distance = math.sqrt((userX - hurkleX)**2 + (userY - hurkleY)**2)`: חישוב המרחק בין הניחוש למיקום ה-HURKLE באמצעות נוסחת המרחק בין שתי נקודות.
6. **בדיקת ניצחון**:
   - `if distance == 0:`: בדיקה האם המרחק הוא 0, כלומר שהשחקן ניחש את מיקום ה-HURKLE.
   - `print(f"מזל טוב! מצאת את ה-HURKLE ב-{numberOfGuesses} ניסיונות!")`: הצגת הודעת ניצחון עם מספר הניסיונות.
   - `break`: סיום הלולאה (והמשחק) אם ה-HURKLE נמצא.
7. **הצגת מרחק**:
   - `else:`: אם ה-HURKLE לא נמצא.
   -  `print(f"המרחק מה-HURKLE הוא: {distance:.2f}")`: הצגת המרחק בין הניחוש למיקום ה-HURKLE, מעוגל לשני מקומות עשרוניים.
