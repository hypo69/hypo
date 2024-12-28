"""
SALVO:
=================
קושי: 4
-----------------
"סלבו" הוא משחק לוח אסטרטגי לשני שחקנים, בו כל שחקן מנסה להטביע את ספינות היריב. המשחק מתרחש על לוח ריבועי, כאשר כל שחקן ממקם את הספינות שלו במיקומים נסתרים. השחקנים מתחלפים בניסיונות לפגוע בספינות היריב על ידי הזנת קואורדינטות. המטרה היא להטביע את כל הספינות של היריב ראשון. גרסה זו היא מופשטת של המשחק.
חוקי המשחק:
1. הלוח הוא בגודל 10x10, אך הוא מיוצג באמצעות משתנים בודדים.
2. המחשב בוחר באופן אקראי 5 מיקומים בספינה (מספרים בין 1 ל-100)
3. השחקן מנסה לפגוע בספינות על ידי הזנת קואורדינטות, שהן בעצם מספרים מ-1 עד 100.
4. המחשב מודיע האם הניסיון פגע בספינה או לא.
5. המשחק נמשך עד שכל הספינות של המחשב הוטבעו.
-----------------
אלגוריתם:
1. אתחל את מספר הספינות (ships) ל-5.
2. אתחל מערך (array) ריק בשם "ships_positions".
3. בצע לולאה 5 פעמים:
  3.1. צור מיקום ספינה אקראי בין 1 ל-100.
  3.2. אם המיקום כבר קיים במערך "ships_positions", חזור לשלב 3.1.
  3.3. הוסף את המיקום החדש למערך "ships_positions".
4. התחל לולאה "כל עוד מספר הספינות גדול מ-0":
  4.1. בקש מהמשתמש להזין מיקום ניסיון.
  4.2. אם המיקום קיים במערך "ships_positions":
    4.2.1. הסר את המיקום מהמערך.
    4.2.2. הורד את מספר הספינות ב-1.
    4.2.3. הצג הודעה "HIT!".
  4.3 אחרת:
    4.3.1. הצג הודעה "MISS".
5. הצג הודעה "YOU SUNK ALL MY SHIPS!".
6. סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    numberOfShips = 5
    shipsPositions = []
    </b></code></p>"]
    InitializeVariables --> GenerateShipsLoopStart{"לולאה: <code><b>5 פעמים</b></code>"}
    GenerateShipsLoopStart --> GenerateRandomPosition["יצירת מיקום אקראי: <code><b>randomPosition = random(1, 100)</b></code>"]
    GenerateRandomPosition --> CheckPosition{"בדיקה: <code><b>randomPosition in shipsPositions?</b></code>"}
    CheckPosition -- כן --> GenerateRandomPosition
    CheckPosition -- לא --> AddPosition["הוספת מיקום למערך: <code><b>shipsPositions.append(randomPosition)</b></code>"]
    AddPosition --> GenerateShipsLoopEnd{"סוף לולאה"}
    GenerateShipsLoopEnd -- פחות מ-5 --> GenerateShipsLoopStart
    GenerateShipsLoopEnd -- שווה ל-5 --> GameLoopStart{"תחילת לולאה: <code><b>numberOfShips > 0</b></code>"}
    GameLoopStart -- כן --> InputGuess["קלט מיקום מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> CheckHit{"בדיקה: <code><b>userGuess in shipsPositions?</b></code>"}
    CheckHit -- כן --> RemoveShip["<p align='left'>הורדת ספינה: 
    <code><b>shipsPositions.remove(userGuess)
    numberOfShips = numberOfShips - 1</b></code></p>"]
    RemoveShip --> OutputHit["הצגת הודעה: <b>HIT!</b>"]
    OutputHit --> GameLoopStart
    CheckHit -- לא --> OutputMiss["הצגת הודעה: <b>MISS</b>"]
    OutputMiss --> GameLoopStart
    GameLoopStart -- לא --> OutputWin["הצגת הודעה: <b>YOU SUNK ALL MY SHIPS!</b>"]
    OutputWin --> End["סוף"]
```
Legenda:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: numberOfShips (מספר הספינות) מאותחל ל-5, ו-shipsPositions (מערך מיקומי הספינות) מאותחל כרשימה ריקה.
    GenerateShipsLoopStart - תחילת לולאה ליצירת מיקומי הספינות (5 פעמים).
    GenerateRandomPosition - יצירת מיקום אקראי של ספינה בין 1 ל-100.
    CheckPosition - בדיקה האם המיקום האקראי כבר קיים במערך.
    AddPosition - הוספת מיקום הספינה למערך אם הוא לא קיים.
    GenerateShipsLoopEnd - סוף לולאת יצירת מיקומי הספינות.
    GameLoopStart - תחילת לולאה של המשחק, כל עוד יש ספינות שלא הוטבעו.
    InputGuess - קליטת מיקום ניסיון מהמשתמש.
    CheckHit - בדיקה האם הניסיון פגע בספינה (האם המיקום נמצא במערך מיקומי הספינות).
    RemoveShip - הורדת הספינה: הסרת המיקום הפגוע מהמערך, והורדת מונה הספינות ב-1.
    OutputHit - הצגת הודעה "HIT!".
    OutputMiss - הצגת הודעה "MISS".
    OutputWin - הצגת הודעת ניצחון "YOU SUNK ALL MY SHIPS!".
    End - סוף התוכנית.
"""
import random

# 1. אתחול מספר הספינות
numberOfShips = 5
# 2. אתחול רשימה ריקה למיקומי הספינות
shipsPositions = []

# 3. לולאה ליצירת 5 מיקומי ספינות אקראיים
for _ in range(5):
    while True:
        # 3.1 יצירת מיקום אקראי בין 1 ל-100
        randomPosition = random.randint(1, 100)
        # 3.2 בדיקה אם המיקום כבר קיים
        if randomPosition not in shipsPositions:
            # 3.3 הוספת המיקום לרשימה
            shipsPositions.append(randomPosition)
            break # יציאה מהלולאה הפנימית כאשר נמצא מיקום חדש
            
# 4. לולאת המשחק
while numberOfShips > 0:
    try:
        # 4.1 קבלת מיקום ניסיון מהמשתמש
        userGuess = int(input("נסה לפגוע בספינה (1-100): "))
    except ValueError:
        print("אנא הזן מספר שלם בין 1 ל-100.")
        continue # חזרה לתחילת הלולאה אם הקלט אינו חוקי

    # 4.2 בדיקה אם הניסיון פגע בספינה
    if userGuess in shipsPositions:
        # 4.2.1 הסרת המיקום מהרשימה
        shipsPositions.remove(userGuess)
        # 4.2.2 הפחתת מספר הספינות
        numberOfShips -= 1
        # 4.2.3 הודעה על פגיעה
        print("פגיעה!")
    else:
        # 4.3.1 הודעה על החטאה
        print("החטאה.")

# 5. סיום המשחק - כל הספינות הוטבעו
print("הטבעת את כל הספינות שלי!")
"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    - `import random`: ייבוא המודול `random`, המשמש ליצירת מספרים אקראיים.
2.  **אתחול משתנים**:
    - `numberOfShips = 5`: אתחול מספר הספינות ל-5. זהו מספר הספינות שהשחקן צריך להטביע כדי לנצח.
    - `shipsPositions = []`: אתחול רשימה ריקה בשם `shipsPositions`. רשימה זו תשמש לאחסון מיקומי הספינות של המחשב.
3.  **לולאה ליצירת מיקומי ספינות אקראיים**:
    - `for _ in range(5):`: לולאה שרצה 5 פעמים, כל פעם עבור ספינה אחת.
    - `while True:`: לולאה אינסופית, שתרוץ עד שנמצא מיקום ספינה ייחודי.
        - `randomPosition = random.randint(1, 100)`: יצירת מיקום ספינה אקראי בין 1 ל-100.
        - `if randomPosition not in shipsPositions:`: בדיקה האם המיקום האקראי כבר קיים ברשימה.
            - `shipsPositions.append(randomPosition)`: הוספת המיקום לרשימה, אם הוא לא קיים.
            - `break`: יציאה מהלולאה הפנימית לאחר הוספת מיקום ספינה ייחודי.
4.  **לולאת המשחק הראשית**:
    - `while numberOfShips > 0:`: לולאה שתמשיך לרוץ כל עוד יש ספינות שלא הוטבעו.
    - `try...except ValueError`: בלוק לטיפול בשגיאות קלט מהמשתמש.
        - `userGuess = int(input("נסה לפגוע בספינה (1-100): "))`: קבלת קלט מהמשתמש (ניחוש מיקום הספינה), והמרה למספר שלם.
        - `continue`: אם הקלט אינו מספר שלם, חוזר לתחילת הלולאה.
    - `if userGuess in shipsPositions:`: בדיקה האם הניחוש של המשתמש תואם למיקום של אחת הספינות.
        - `shipsPositions.remove(userGuess)`: הסרת המיקום הפגוע מהרשימה.
        - `numberOfShips -= 1`: הפחתת מספר הספינות ב-1, מאחר שאחת הוטבעה.
        - `print("פגיעה!")`: הודעה על פגיעה.
    - `else:`: אם הניחוש לא תואם לאף מיקום ספינה.
        - `print("החטאה.")`: הודעה על החטאה.
5.  **סיום המשחק**:
    - `print("הטבעת את כל הספינות שלי!")`: הצגת הודעה שהמשתמש ניצח.
"""
