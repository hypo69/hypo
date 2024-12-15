<CAN AM>:
=================
קושי: 4
-----------------
המשחק CAN AM מדמה מירוץ מכוניות על מסלול מוגדר. המשתמש שולט במכונית אחת, ומנסה להגיע לקו הסיום לפני שהמחשב מגיע. המהירות של המכונית שלך מושפעת מהבחירות שלך, וניתן להאיץ או להאט. המחשב נע במהירות קבועה.

חוקי המשחק:
1. המשחק מתחיל בקו ההתחלה, כאשר המכונית של השחקן והמחשב נמצאות באותה עמדה.
2. השחקן מזין קלט כדי לשלוט במהירות המכונית שלו:
   - 0 - האט
   - 1 - שמור על מהירות נוכחית
   - 2 - האץ
3. המחשב נע במהירות קבועה של 2.
4. המירוץ מסתיים כאשר אחת המכוניות עוברת את קו הסיום (מרחק של 500).
5. מוצגת הודעת ניצחון או הפסד, בהתאם למי שהגיע ראשון לקו הסיום.
-----------------
אלגוריתם:
1. אתחל את מיקום המכונית של השחקן (`userDistance`) ל-0.
2. אתחל את מהירות המכונית של השחקן (`userSpeed`) ל-0.
3. אתחל את מיקום המכונית של המחשב (`computerDistance`) ל-0.
4. אתחל את מהירות המכונית של המחשב (`computerSpeed`) ל-2.
5. התחל לולאה "כל עוד אף מכונית לא עברה את קו הסיום (500)":
    5.1. הצג את מיקום המכונית של השחקן והמחשב.
    5.2. בקש מהשחקן לבחור מהירות (0 - האט, 1 - שמור, 2 - האץ).
    5.3. עדכן את מהירות המכונית של השחקן בהתאם לקלט.
    5.4. עדכן את מיקום המכונית של השחקן בהתאם למהירות.
    5.5. עדכן את מיקום המכונית של המחשב בהתאם למהירות (שהיא קבועה).
6. לאחר סיום הלולאה, בדוק מי עבר את קו הסיום ראשון והצג הודעה מתאימה.
7. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    userDistance = 0
    userSpeed = 0
    computerDistance = 0
    computerSpeed = 2
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה:
    <code><b>userDistance < 500 AND computerDistance < 500</b></code>"}
    LoopStart -- כן --> DisplayPositions["הצג מיקום מכונית שחקן ומחשב"]
    DisplayPositions --> InputSpeedChoice["קלט: בחירת מהירות (0, 1, 2)"]
    InputSpeedChoice --> UpdateUserSpeed["<p align='left'>עדכן מהירות שחקן:
    <code><b>
    userSpeed = userSpeed + (speedChoice - 1)
    </b></code></p>"]
    UpdateUserSpeed --> UpdateUserDistance["<code><b>userDistance = userDistance + userSpeed</b></code>"]
    UpdateUserDistance --> UpdateComputerDistance["<code><b>computerDistance = computerDistance + computerSpeed</b></code>"]
    UpdateComputerDistance --> LoopStart
    LoopStart -- לא --> CheckWinner{"בדיקה:
    <code><b>userDistance >= 500?</b></code>"}
    CheckWinner -- כן --> OutputUserWin["הצג הודעה: <b>YOU WIN</b>"]
    OutputUserWin --> End["סוף"]
    CheckWinner -- לא --> OutputComputerWin["הצג הודעה: <b>COMPUTER WIN</b>"]
    OutputComputerWin --> End
```
Legenda:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתני המשחק: מיקום השחקן, מהירות השחקן, מיקום המחשב ומהירות המחשב.
    LoopStart - תחילת לולאת המשחק, כל עוד אף אחד מהשחקנים לא עבר את קו הסיום (500).
    DisplayPositions - הצגת מיקום המכוניות של השחקן והמחשב.
    InputSpeedChoice - קבלת קלט מהמשתמש לבחירת מהירות.
    UpdateUserSpeed - עדכון מהירות המכונית של השחקן בהתאם לבחירת המשתמש.
    UpdateUserDistance - עדכון מיקום המכונית של השחקן בהתאם למהירות הנוכחית.
    UpdateComputerDistance - עדכון מיקום המכונית של המחשב בהתאם למהירות הקבועה שלו.
    CheckWinner - בדיקה האם השחקן עבר את קו הסיום.
    OutputUserWin - הצגת הודעה שהשחקן ניצח.
    OutputComputerWin - הצגת הודעה שהמחשב ניצח.
     End - סוף התוכנית.
"""
import time

# אתחול משתנים
userDistance = 0  # מרחק המכונית של המשתמש
userSpeed = 0    # מהירות המכונית של המשתמש
computerDistance = 0  # מרחק המכונית של המחשב
computerSpeed = 2  # מהירות המכונית של המחשב

# לולאת המשחק הראשית
while userDistance < 500 and computerDistance < 500:
    # הצגת מיקום המכוניות
    print(f"מיקום שלך: {userDistance}, מיקום מחשב: {computerDistance}")

    # קבלת קלט מהמשתמש
    while True:
        try:
            speedChoice = int(input("בחר מהירות (0=האט, 1=שמור, 2=האץ): "))
            if speedChoice in [0, 1, 2]:
                break
            else:
                print("בחירה לא חוקית. אנא בחר 0, 1 או 2.")
        except ValueError:
            print("קלט לא חוקי. אנא הכנס מספר.")

    # עדכון מהירות המכונית של המשתמש
    userSpeed += (speedChoice - 1)
    if userSpeed < 0:  # הגבלת מהירות המשתמש שלא תהיה שלילית
        userSpeed = 0

    # עדכון מיקום המכוניות
    userDistance += userSpeed
    computerDistance += computerSpeed

    time.sleep(0.5)  # השהיה קצרה כדי שיהיה נוח לקרוא את הפלט


# בדיקה מי ניצח
if userDistance >= 500:
    print("ניצחת!")
else:
    print("המחשב ניצח!")
"""
הסבר הקוד:
1.  **ייבוא המודול `time`**:
    - `import time`: ייבוא המודול `time`, המשמש להוספת השהיה קצרה בין עדכוני המסך.
2.  **אתחול משתנים**:
    - `userDistance = 0`: אתחול המרחק של מכונית המשתמש ל-0.
    - `userSpeed = 0`: אתחול המהירות של מכונית המשתמש ל-0.
    - `computerDistance = 0`: אתחול המרחק של מכונית המחשב ל-0.
    - `computerSpeed = 2`: אתחול המהירות של מכונית המחשב ל-2 (קבועה).
3.  **לולאת המשחק `while userDistance < 500 and computerDistance < 500:`**:
    - לולאה זו רצה כל עוד אף מכונית לא עברה את קו הסיום (500).
    - `print(f"מיקום שלך: {userDistance}, מיקום מחשב: {computerDistance}")`: הצגת המיקום הנוכחי של שתי המכוניות.
    - **קבלת קלט מהמשתמש**:
        - `while True:`: לולאה שממשיכה עד שהמשתמש מזין קלט תקין.
        - `try...except ValueError`: טיפול בשגיאות קלט אפשריות.
        - `speedChoice = int(input("בחר מהירות (0=האט, 1=שמור, 2=האץ): "))`: בקשת קלט מהמשתמש לבחירת מהירות (0, 1 או 2).
        - `if speedChoice in [0, 1, 2]:`: בדיקה שהקלט תקין (0, 1 או 2).
        - `break`: יציאה מהלולאה הפנימית אם הקלט תקין.
        - `else`: אם הקלט לא תקין, תודפס הודעה למשתמש.
    - `userSpeed += (speedChoice - 1)`: עדכון מהירות מכונית המשתמש.
    - `if userSpeed < 0:`: הגבלה שהמהירות לא תהיה שלילית.
    - `userDistance += userSpeed`: עדכון מרחק מכונית המשתמש בהתאם למהירות.
    - `computerDistance += computerSpeed`: עדכון מרחק מכונית המחשב.
    - `time.sleep(0.5)`: השהיה קצרה של 0.5 שניות בין עדכוני המסך.
4.  **בדיקת מנצח**:
    - `if userDistance >= 500:`: בדיקה האם מכונית המשתמש עברה את קו הסיום.
    - `print("ניצחת!")`: הדפסת הודעה שהמשתמש ניצח.
    - `else`: אם מכונית המשתמש לא עברה את קו הסיום, אז המחשב ניצח.
    - `print("המחשב ניצח!")`: הדפסת הודעה שהמחשב ניצח.
"""
