"""
<BATTLE>:
=================
קושי: 5
-----------------
משחק קרב יריות פשוט בין שני שחקנים (אחד מהם הוא המחשב). כל שחקן מתחיל עם מספר נתון של חיילים, ובכל תור, כל שחקן בוחר כמה חיילים לתקוף. המנצח הוא זה שמחסל את כל חיילי היריב.
חוקי המשחק:
1. שני שחקנים משחקים אחד נגד השני. אחד השחקנים הוא המחשב.
2. כל שחקן מתחיל עם מספר קבוע של חיילים (בסיסי 100).
3. בכל תור, כל שחקן בוחר כמה חיילים לתקוף את היריב.
4. הפגיעה מושפעת ממספר אקראי (הטלת קובייה).
5.  המשחק נגמר כאשר אחד מהשחקנים איבד את כל חייליו.
6. השחקן שנותר עם חיילים מנצח.
-----------------
אלגוריתם:
1. אתחול מספר החיילים של השחקן ל-100.
2. אתחול מספר החיילים של המחשב ל-100.
3. לולאה ראשית שרצה כל עוד לשני השחקנים יש חיילים:
   3.1. תור השחקן:
        - בקש מהשחקן להכניס את מספר החיילים שהוא שולח להתקפה.
        - בדוק שהמספר שהוזן חוקי (לא שלילי ולא גדול ממספר החיילים של השחקן).
        - צור מספר אקראי בין 1 ל-6 (דמוי הטלת קובייה) וחשב את הנזק שנגרם למחשב. הנזק שווה למספר החיילים שתקפו כפול המספר האקראי חלקי 6.
        - עדכן את מספר החיילים של המחשב.
        - הדפס את מספר החיילים הנוכחיים של המחשב.
        - בדוק אם המחשב הפסיד (מספר החיילים שלו קטן או שווה ל-0). אם כן, המשחק נגמר, השחקן ניצח.
   3.2. תור המחשב:
         - המחשב בוחר באופן אקראי מספר חיילים לתקוף (לא יותר ממספר החיילים שלו).
         - צור מספר אקראי בין 1 ל-6 וחשב את הנזק שנגרם לשחקן.
         - עדכן את מספר החיילים של השחקן.
         - הדפס את מספר החיילים הנוכחיים של השחקן.
         - בדוק אם השחקן הפסיד (מספר החיילים שלו קטן או שווה ל-0). אם כן, המשחק נגמר, המחשב ניצח.
4. הצג הודעת ניצחון בהתאם למנצח.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["אתחול משתנים:<br>playerSoldiers = 100<br>computerSoldiers = 100"]
    InitializeVariables --> MainLoopStart{"תחילת לולאה:<br>כל עוד playerSoldiers > 0 וגם computerSoldiers > 0"}
    MainLoopStart -- כן --> PlayerTurnStart["תור השחקן"]
    PlayerTurnStart --> PlayerInputSoldiers["קלט: מספר חיילים לתקוף"]
    PlayerInputSoldiers --> ValidatePlayerInput{"בדיקה: קלט חוקי?"}
    ValidatePlayerInput -- לא --> PlayerInputSoldiers
    ValidatePlayerInput -- כן --> CalculatePlayerDamage["חישוב נזק:<br>damage = (attackers * random(1,6)) / 6"]
    CalculatePlayerDamage --> UpdateComputerSoldiers["עדכון חיילי מחשב:<br>computerSoldiers -= damage"]
    UpdateComputerSoldiers --> OutputComputerSoldiers["פלט: חיילי מחשב"]
    OutputComputerSoldiers --> CheckComputerLoss{"בדיקה: computerSoldiers <= 0"}
    CheckComputerLoss -- כן --> OutputPlayerWin["פלט: שחקן ניצח"]
    OutputPlayerWin --> End["סוף"]
    CheckComputerLoss -- לא --> ComputerTurnStart["תור המחשב"]
    ComputerTurnStart --> ComputerChooseSoldiers["מחשב בוחר מספר חיילים"]
    ComputerChooseSoldiers --> CalculateComputerDamage["חישוב נזק:<br>damage = (attackers * random(1,6)) / 6"]
    CalculateComputerDamage --> UpdatePlayerSoldiers["עדכון חיילי שחקן:<br>playerSoldiers -= damage"]
    UpdatePlayerSoldiers --> OutputPlayerSoldiers["פלט: חיילי שחקן"]
    OutputPlayerSoldiers --> CheckPlayerLoss{"בדיקה: playerSoldiers <= 0"}
    CheckPlayerLoss -- כן --> OutputComputerWin["פלט: מחשב ניצח"]
    OutputComputerWin --> End
    CheckPlayerLoss -- לא --> MainLoopStart
    MainLoopStart -- לא --> End

```
Legenda:
   Start - התחלת התוכנית.
   InitializeVariables - אתחול משתני המשחק: `playerSoldiers` ו- `computerSoldiers` ל-100.
   MainLoopStart - התחלת הלולאה הראשית: המשחק ממשיך כל עוד לשחקן ולמחשב יש חיילים.
   PlayerTurnStart - תחילת תור השחקן.
   PlayerInputSoldiers - קלט מהשחקן, מספר החיילים שהוא שולח להתקפה.
   ValidatePlayerInput - בדיקה שהקלט מהשחקן חוקי.
   CalculatePlayerDamage - חישוב הנזק שגורם השחקן למחשב, בהתבסס על מספר החיילים ומספר אקראי (קובייה).
   UpdateComputerSoldiers - עדכון מספר החיילים של המחשב לאחר הנזק מהשחקן.
   OutputComputerSoldiers - פלט: הצגת מספר החיילים של המחשב.
   CheckComputerLoss - בדיקה האם המחשב הפסיד (אין לו חיילים).
   OutputPlayerWin - פלט: השחקן ניצח.
   ComputerTurnStart - תחילת תור המחשב.
   ComputerChooseSoldiers - המחשב בוחר באופן אקראי מספר חיילים לתקוף.
   CalculateComputerDamage - חישוב הנזק שגורם המחשב לשחקן, בהתבסס על מספר החיילים ומספר אקראי (קובייה).
   UpdatePlayerSoldiers - עדכון מספר החיילים של השחקן לאחר הנזק מהמחשב.
   OutputPlayerSoldiers - פלט: הצגת מספר החיילים של השחקן.
   CheckPlayerLoss - בדיקה האם השחקן הפסיד (אין לו חיילים).
   OutputComputerWin - פלט: המחשב ניצח.
   End - סיום המשחק.
"""

import random

# אתחול מספר החיילים של השחקן והמחשב
playerSoldiers = 100
computerSoldiers = 100

# לולאת משחק ראשית, ממשיכה כל עוד לשני הצדדים יש חיילים
while playerSoldiers > 0 and computerSoldiers > 0:
    # תור השחקן
    print("\n----- תורך -----")
    while True:  # לולאה לוודא קלט תקין
        try:
            # בקשה מהשחקן להזין את מספר החיילים לתקוף
            attackers = int(input("כמה חיילים לשלוח להתקפה? "))
            if attackers <= 0 or attackers > playerSoldiers:
                # בדיקה שהמספר שהוזן חוקי
                print("מספר לא חוקי. אנא נסה שוב.")
            else:
                break # יציאה מהלולאה לאחר קלט תקין
        except ValueError:
             # טיפול במקרה שהקלט אינו מספר
            print("קלט לא חוקי. אנא הכנס מספר.")

    # חישוב הנזק שגורם השחקן
    damage = (attackers * random.randint(1, 6)) / 6
    computerSoldiers -= int(damage) # עידכון חיילי המחשב
    print(f"הנזק שגרמת למחשב: {int(damage)}. למחשב נותרו {computerSoldiers} חיילים.")


    # בדיקה אם המחשב הפסיד
    if computerSoldiers <= 0:
        print("ניצחת! כל הכבוד!")
        break  # סיום המשחק, שחקן ניצח

    # תור המחשב
    print("\n----- תור המחשב -----")
    # המחשב בוחר מספר חיילים באופן אקראי
    computerAttackers = random.randint(1, computerSoldiers)
    # חישוב הנזק שגורם המחשב
    damage = (computerAttackers * random.randint(1, 6)) / 6
    playerSoldiers -= int(damage) # עידכון חיילי השחקן
    print(f"המחשב תקף אותך עם {computerAttackers} חיילים וגרם לך {int(damage)} נזק. נותרו לך {playerSoldiers} חיילים.")

    # בדיקה אם השחקן הפסיד
    if playerSoldiers <= 0:
        print("הפסדת! המחשב ניצח.")
        break # סיום המשחק, המחשב ניצח
"""
הסבר הקוד:
1. **ייבוא המודול `random`**:
   - `import random`: ייבוא המודול `random`, המשמש ליצירת מספרים אקראיים עבור "קובייה" וקביעת מספר החיילים שהמחשב תוקף.
2. **אתחול משתנים**:
   - `playerSoldiers = 100`: אתחול מספר החיילים של השחקן ל-100.
   - `computerSoldiers = 100`: אתחול מספר החיילים של המחשב ל-100.
3. **לולאת המשחק הראשית (`while playerSoldiers > 0 and computerSoldiers > 0`)**:
   - הלולאה ממשיכה כל עוד לשני השחקנים יש חיילים.
4. **תור השחקן**:
   - הדפסת הודעה "תורך".
   - **לולאה לקלט תקין**:
      -  `while True`: לולאה אינסופית עד שהשחקן מזין קלט תקין.
      -  `try...except ValueError`: טיפול בשגיאות קלט (לדוגמה, אם השחקן מזין טקסט במקום מספר).
      -  `attackers = int(input("כמה חיילים לשלוח להתקפה? "))`: קליטת מספר החיילים מהשחקן והמרתו למספר שלם.
      -  `if attackers <= 0 or attackers > playerSoldiers`: בדיקה שהמספר שהוזן חוקי (לא שלילי ולא גדול ממספר החיילים).
      -  `break`: יציאה מהלולאה לאחר קלט תקין.
   - **חישוב נזק**:
     - `damage = (attackers * random.randint(1, 6)) / 6`: חישוב הנזק שגורם השחקן למחשב, בהתאם למספר החיילים והטלת קובייה (מספר אקראי בין 1 ל-6).
   - `computerSoldiers -= int(damage)`: עידכון מספר חיילי המחשב.
   - הדפסת הודעה על הנזק שנגרם למחשב ומספר החיילים שנותרו לו.
   - **בדיקה אם המחשב הפסיד**:
     - `if computerSoldiers <= 0`: בדיקה האם למחשב נותרו 0 חיילים או פחות.
     - הדפסת הודעה על ניצחון השחקן וסיום המשחק.
     - `break`: סיום הלולאה הראשית (סיום המשחק).
5. **תור המחשב**:
   - הדפסת הודעה "תור המחשב".
   - `computerAttackers = random.randint(1, computerSoldiers)`: המחשב בוחר באופן אקראי מספר חיילים לתקוף.
   - `damage = (computerAttackers * random.randint(1, 6)) / 6`: חישוב הנזק שגורם המחשב לשחקן.
   - `playerSoldiers -= int(damage)`: עידכון מספר חיילי השחקן.
   - הדפסת הודעה על מספר החיילים שהמחשב תקף ועל הנזק שנגרם לשחקן ומספר החיילים שנותרו לו.
   - **בדיקה אם השחקן הפסיד**:
     - `if playerSoldiers <= 0`: בדיקה האם לשחקן נותרו 0 חיילים או פחות.
     - הדפסת הודעה על ניצחון המחשב וסיום המשחק.
     - `break`: סיום הלולאה הראשית (סיום המשחק).
"""
