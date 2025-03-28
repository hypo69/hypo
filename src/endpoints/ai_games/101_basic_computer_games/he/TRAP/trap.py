<TRAP>:
=================
קושי: 5
-----------------
המשחק "מלכודת" הוא משחק טקסט פשוט בו השחקן צריך לגלות את מיקומה של מלכודת על ידי הזנת קואורדינטות (x,y). המשחק מתחיל במפה ריבועית 5x5 והשחקן מקבל רמזים אם הוא מתקרב למלכודת, או שהוא רחוק ממנה, או שהוא בדיוק במקום. המטרה היא לגלות את המלכודת בפחות מ-15 ניסיונות.

חוקי המשחק:
1. המפה מוגדרת כריבוע 5x5 עם קואורדינטות בין 1 ל-5.
2. המחשב בוחר מיקום אקראי למלכודת (x,y) בתוך המפה.
3. השחקן מזין קואורדינטות (x,y) כניחוש למקום המלכודת.
4. המחשב נותן רמז: "COOL" (רחוק), "WARM" (קרוב), "HOT" (בדיוק במקום).
5. השחקן מוגבל ל-15 ניחושים בלבד.
6. המשחק מסתיים בניצחון אם המלכודת נמצאה, או בהפסד אם הניסיונות נגמרו.
-----------------
אלגוריתם:
1. אתחל את מונה הניחושים ל-0.
2. בחר קואורדינטות אקראיות (x, y) בטווח 1-5 למיקום המלכודת.
3. התחל לולאה (עד 15 ניחושים):
   3.1. הגדל את מונה הניחושים ב-1.
   3.2. בקש מהשחקן להזין קואורדינטות x ו-y.
   3.3. אם הקואורדינטות שהוזנו שוות לקואורדינטות המלכודת, הודע על ניצחון וצא מהלולאה.
   3.4. אחרת, חשב את המרחק בין הניחוש למלכודת:
        - אם המרחק גדול מ-2, הצג "COOL"
        - אם המרחק קטן או שווה ל-2, הצג "WARM"
4. אם הלולאה הסתיימה מבלי שהמלכודת נמצאה, הודע על הפסד.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    numberOfGuesses = 0<br>
    trapX = random(1, 5)<br>
    trapY = random(1, 5)
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: numberOfGuesses < 15"}
    LoopStart -- כן --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputCoordinates["קלט קואורדינטות מהמשתמש: <code><b>userX, userY</b></code>"]
    InputCoordinates --> CheckTrap{"בדיקה: <code><b>userX == trapX AND userY == trapY</b></code>"}
    CheckTrap -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT!</b>"]
    OutputWin --> End["סוף"]
    CheckTrap -- לא --> CalculateDistance["חישוב מרחק: <code><b>distance = sqrt((userX - trapX)^2 + (userY - trapY)^2)</b></code>"]
    CalculateDistance --> CheckDistance{"בדיקה: <code><b>distance > 2?</b></code>"}
    CheckDistance -- כן --> OutputCool["הצגת הודעה: <b>COOL</b>"]
    OutputCool --> LoopStart
    CheckDistance -- לא --> OutputWarm["הצגת הודעה: <b>WARM</b>"]
    OutputWarm --> LoopStart
    LoopStart -- לא --> OutputLose["הצגת הודעה: <b>YOU LOSE!</b>"]
    OutputLose --> End
```
Legenda:
   Start - התחלת התוכנית.
   InitializeVariables - אתחול משתנים: numberOfGuesses (מספר הניסיונות) מאותחל ל-0, ו-trapX ו-trapY (קואורדינטות המלכודת) נוצרים באקראי בין 1 ל-5.
   LoopStart - תחילת הלולאה, הממשיכה כל עוד מספר הניסיונות קטן מ-15.
   IncreaseGuesses - הגדלת מונה הניסיונות ב-1.
   InputCoordinates - קלט קואורדינטות X ו-Y מהמשתמש ושמירתן במשתנים userX ו-userY.
   CheckTrap - בדיקה האם הקואורדינטות שהוזנו שוות לקואורדינטות המלכודת.
   OutputWin - הצגת הודעת ניצחון, אם המלכודת נמצאה.
   End - סוף התוכנית.
   CalculateDistance - חישוב המרחק בין הקואורדינטות שהוזנו לקואורדינטות המלכודת.
   CheckDistance - בדיקה האם המרחק בין הניחוש למלכודת גדול מ-2.
   OutputCool - הצגת הודעה "COOL", אם המרחק גדול מ-2.
   OutputWarm - הצגת הודעה "WARM", אם המרחק קטן או שווה ל-2.
   OutputLose - הצגת הודעת הפסד, אם הלולאה הסתיימה מבלי שהמלכודת נמצאה.
"""
import random
import math

# אתחול מונה הניחושים
numberOfGuesses = 0
# יצירת קואורדינטות אקראיות למלכודת בין 1 ל-5
trapX = random.randint(1, 5)
trapY = random.randint(1, 5)


# לולאת המשחק הראשית - עד 15 ניסיונות
while numberOfGuesses < 15:
    numberOfGuesses += 1
    
    # קבלת קואורדינטות מהמשתמש
    try:
      userX = int(input("הכנס קואורדינטת X (1-5): "))
      userY = int(input("הכנס קואורדינטת Y (1-5): "))
    except ValueError:
      print("אנא הזן מספרים שלמים בלבד.")
      continue
    
    # בדיקה אם הקואורדינטות בטווח המותר
    if not (1 <= userX <= 5 and 1 <= userY <= 5):
      print("קואורדינטות לא חוקיות, חייבות להיות בין 1 ל-5.")
      continue
    
    # בדיקה האם המלכודת נמצאה
    if userX == trapX and userY == trapY:
        print("מזל טוב! מצאת את המלכודת!")
        break  # סיום המשחק אם המלכודת נמצאה

    # חישוב מרחק בין הקואורדינטות שנוחשו למלכודת
    distance = math.sqrt((userX - trapX)**2 + (userY - trapY)**2)

    # מתן רמזים בהתאם למרחק
    if distance > 2:
        print("COOL")
    else:
        print("WARM")

# אם הלולאה הסתיימה מבלי שהמלכודת נמצאה, השחקן מפסיד
if numberOfGuesses == 15:
    print("הפסדת! לא מצאת את המלכודת בזמן.")

"""
הסבר הקוד:
1.  **ייבוא מודולים**:
    - `import random`: ייבוא מודול `random` ליצירת מספרים אקראיים.
    - `import math`: ייבוא מודול `math` לחישוב מרחקים (שורש ריבועי).
2.  **אתחול משתנים**:
    - `numberOfGuesses = 0`:  אתחול מונה הניסיונות ל-0.
    - `trapX = random.randint(1, 5)`: יצירת קואורדינטת X אקראית בין 1 ל-5.
    - `trapY = random.randint(1, 5)`: יצירת קואורדינטת Y אקראית בין 1 ל-5.
3.  **לולאת המשחק `while numberOfGuesses < 15:`**:
    - לולאה שרצה כל עוד מספר הניסיונות קטן מ-15.
    - `numberOfGuesses += 1`: הגדלת מונה הניסיונות בכל סיבוב.
4.  **קלט קואורדינטות**:
    - `try...except ValueError`: טיפול בשגיאת קלט - אם המשתמש לא הכניס מספר שלם, תודפס הודעת שגיאה.
    - `userX = int(input("הכנס קואורדינטת X (1-5): "))`: בקשת קלט קואורדינטת X מהמשתמש.
    - `userY = int(input("הכנס קואורדינטת Y (1-5): "))`: בקשת קלט קואורדינטת Y מהמשתמש.
5.  **בדיקת קלט חוקי**:
    -  `if not (1 <= userX <= 5 and 1 <= userY <= 5):`: בדיקה האם הקלט שהמשתמש הכניס נמצא בטווח 1-5. אם לא, מודפסת הודעה והלולאה ממשיכה.
6.  **בדיקה אם המלכודת נמצאה**:
    - `if userX == trapX and userY == trapY:`: בדיקה האם הקואורדינטות שהמשתמש הזין שוות לקואורדינטות המלכודת.
    - `print("מזל טוב! מצאת את המלכודת!")`: הדפסת הודעת ניצחון אם המלכודת נמצאה.
    - `break`: יציאה מהלולאה אם המלכודת נמצאה.
7.  **חישוב מרחק ורמזים**:
    - `distance = math.sqrt((userX - trapX)**2 + (userY - trapY)**2)`: חישוב המרחק בין הקואורדינטות שהוזנו למלכודת.
    - `if distance > 2:`: בדיקה אם המרחק גדול מ-2.
    - `print("COOL")`: הדפסת "COOL" אם המרחק גדול מ-2.
    - `else:`: אם המרחק קטן או שווה ל-2.
    - `print("WARM")`: הדפסת "WARM" אם המרחק קטן או שווה ל-2.
8.  **הפסד במשחק**:
    -  `if numberOfGuesses == 15:`: בדיקה האם הלולאה הסתיימה לאחר 15 ניסיונות.
    -  `print("הפסדת! לא מצאת את המלכודת בזמן.")`: הדפסת הודעת הפסד אם לא נמצאה המלכודת ב-15 ניסיונות.
"""
