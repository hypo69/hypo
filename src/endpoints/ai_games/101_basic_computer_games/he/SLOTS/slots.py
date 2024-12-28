"""
SLOTS:
=================
קושי: 6
-----------------
המשחק "מכונות מזל" מדמה מכונת מזל פשוטה, שבה השחקן מהמר על מספר מסוים של מטבעות, ובתמורה המכונה מסובבת שלושה גלגלים עם סמלים שונים.
אם הסמלים על הגלגלים זהים, השחקן זוכה בכמות מטבעות בהתאם למספר המטבעות שהמר, אחרת השחקן מפסיד את ההימור.

חוקי המשחק:
1. השחקן מתחיל עם 100 מטבעות.
2. בכל סיבוב, השחקן בוחר כמה מטבעות להמר (בין 1 לכל המטבעות שיש לו).
3. המכונה מסובבת שלושה גלגלים, שכל אחד מהם מציג סמל אקראי מתוך רשימה של סמלים אפשריים.
4. אם כל שלושת הסמלים זהים, השחקן זוכה במכפלה של ההימור שלו פי 10.
5. אם הסמלים לא זהים, השחקן מאבד את ההימור.
6. המשחק נמשך עד שהשחקן נגמרים המטבעות או שהוא בוחר להפסיק.
-----------------
אלגוריתם:
1. אתחל את כמות המטבעות של השחקן ל-100.
2. הגדר רשימה של סמלים אפשריים (לדוגמה: "CHERRY", "BAR", "7", "SPACE").
3. התחל לולאה ראשית:
    3.1 הצג לשחקן את מספר המטבעות שיש לו.
    3.2 שאל את השחקן כמה מטבעות הוא רוצה להמר.
        3.2.1 אם השחקן מהמר על מספר לא חוקי (פחות מ-1 או יותר ממה שיש לו), חזור לשלב 3.2.
        3.2.2 אם השחקן מהמר על 0, צא מהלולאה הראשית (סיום המשחק).
    3.3 סובב את גלגלי המכונה: בחר סמל אקראי לכל אחד משלושת הגלגלים.
    3.4 הצג את הסמלים שהתקבלו.
    3.5 אם כל שלושת הסמלים זהים:
        3.5.1 חשב את הזכייה (ההימור כפול 10).
        3.5.2 הוסף את הזכייה לכמות המטבעות של השחקן.
        3.5.3 הצג הודעת זכייה ואת כמות המטבעות הנוכחית של השחקן.
    3.6 אחרת (אם הסמלים לא זהים):
         3.6.1 הפחת את ההימור מכמות המטבעות של השחקן.
         3.6.2 הצג הודעת הפסד ואת כמות המטבעות הנוכחית של השחקן.
    3.7 אם לשחקן אין יותר מטבעות, צא מהלולאה הראשית (סיום המשחק).
4. אם יצאת מהלולאה הראשית בגלל שאין יותר מטבעות: הצג הודעה "נגמרו לך המטבעות".
5. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeCoins["<p align='left'>אתחול משתנים:
    <code><b>
    playerCoins = 100<br>
    symbols = ['CHERRY', 'BAR', '7', 'SPACE']
    </b></code></p>"]
    InitializeCoins --> MainLoopStart{"תחילת לולאה ראשית: כל עוד יש מטבעות והשחקן לא הפסיק"}
    MainLoopStart -- כן --> DisplayCoins["הצגת כמות המטבעות לשחקן: <code><b>playerCoins</b></code>"]
    DisplayCoins --> InputBet["קלט הימור מהשחקן: <code><b>bet</b></code>"]
    InputBet --> ValidateBet{"בדיקה: <code><b>bet > 0 AND bet <= playerCoins</b></code>?"}
    ValidateBet -- לא --> InputBet
    ValidateBet -- כן --> CheckBetZero{"בדיקה: <code><b>bet == 0</b></code>?"}
    CheckBetZero -- כן --> End["סוף"]
    CheckBetZero -- לא --> SpinWheels["<p align='left'>סיבוב גלגלים:
    <code><b>
    wheel1 = random(symbols)<br>
    wheel2 = random(symbols)<br>
    wheel3 = random(symbols)
    </b></code></p>"]
    SpinWheels --> DisplayWheels["הצגת הסמלים: <code><b>wheel1, wheel2, wheel3</b></code>"]
    DisplayWheels --> CheckWin{"בדיקה: <code><b>wheel1 == wheel2 AND wheel2 == wheel3</b></code>?"}
    CheckWin -- כן --> CalculateWin["<code><b>winAmount = bet * 10</b></code>"]
    CalculateWin --> UpdateCoinsWin["<code><b>playerCoins = playerCoins + winAmount</b></code>"]
    UpdateCoinsWin --> OutputWin["הצגת הודעת זכייה: <b>YOU WIN, coins = <code>{playerCoins}</code></b>"]
    OutputWin --> CheckCoinsRemaining{"בדיקה: <code><b>playerCoins > 0</b></code>?"}
    CheckWin -- לא --> UpdateCoinsLose["<code><b>playerCoins = playerCoins - bet</b></code>"]
    UpdateCoinsLose --> OutputLose["הצגת הודעת הפסד: <b>YOU LOSE, coins = <code>{playerCoins}</code></b>"]
    OutputLose --> CheckCoinsRemaining
    CheckCoinsRemaining -- כן --> MainLoopStart
    CheckCoinsRemaining -- לא --> OutputOutOfCoins["הצגת הודעה: <b>OUT OF COINS</b>"]
    OutputOutOfCoins --> End
    MainLoopStart -- לא --> End
```
Legenda:
    Start - התחלת התוכנית.
    InitializeCoins - אתחול משתנים: playerCoins (כמות המטבעות של השחקן) מאותחל ל-100, ו-symbols (רשימת הסמלים האפשריים) מאותחלת.
    MainLoopStart - תחילת הלולאה הראשית, הממשיכה כל עוד יש לשחקן מטבעות והוא לא הפסיק את המשחק.
    DisplayCoins - הצגת כמות המטבעות הנוכחית של השחקן.
    InputBet - קבלת הימור מהשחקן ושמירתו במשתנה bet.
    ValidateBet - בדיקה האם ההימור שהוזן הוא חוקי (גדול מ-0 וקטן או שווה לכמות המטבעות שיש לשחקן).
    CheckBetZero - בדיקה האם ההימור שהוזן הוא 0, אם כן, סיום המשחק.
    SpinWheels - סיבוב שלושת גלגלי המכונה (בחירת סמל אקראי לכל גלגל).
    DisplayWheels - הצגת הסמלים שנבחרו על הגלגלים.
    CheckWin - בדיקה האם כל שלושת הסמלים זהים, שמירת התוצאה.
    CalculateWin - חישוב סכום הזכייה (הימור כפול 10).
    UpdateCoinsWin - עדכון כמות המטבעות של השחקן על ידי הוספת הזכייה.
    OutputWin - הצגת הודעת זכייה וכמות המטבעות הנוכחית של השחקן.
    UpdateCoinsLose - עדכון כמות המטבעות של השחקן על ידי הפחתת ההימור.
    OutputLose - הצגת הודעת הפסד וכמות המטבעות הנוכחית של השחקן.
    CheckCoinsRemaining - בדיקה האם יש לשחקן מטבעות נוספים.
    OutputOutOfCoins - הצגת הודעה שהשחקן נגמרו לו המטבעות.
    End - סוף התוכנית.
"""
import random

# הגדרת פונקציה לביצוע המשחק SLOTS
def play_slots_game():
    # 1. אתחול כמות המטבעות של השחקן
    playerCoins = 100
    # 2. רשימת הסמלים האפשריים
    symbols = ["CHERRY", "BAR", "7", "SPACE"]

    # 3. לולאה ראשית של המשחק
    while True:
        # 3.1 הצגת כמות המטבעות לשחקן
        print(f"יש לך {playerCoins} מטבעות.")

        # 3.2 קבלת הימור מהשחקן
        while True:
            try:
                bet = int(input("כמה מטבעות תרצה להמר? (0 כדי לסיים) "))
                if bet < 0:
                  print("ההימור צריך להיות חיובי")
                  continue
                elif bet > playerCoins:
                    print("אין לך מספיק מטבעות בשביל הימור זה.")
                    continue
                else:
                  break
            except ValueError:
                print("אנא הזן מספר שלם.")

        # 3.2.2 סיום המשחק אם השחקן מהמר על 0
        if bet == 0:
            break

        # 3.3 סיבוב גלגלי המכונה
        wheel1 = random.choice(symbols)
        wheel2 = random.choice(symbols)
        wheel3 = random.choice(symbols)

        # 3.4 הצגת הסמלים
        print(f"תוצאה: {wheel1} {wheel2} {wheel3}")

        # 3.5 בדיקה האם כל הסמלים זהים
        if wheel1 == wheel2 == wheel3:
            winAmount = bet * 10 # 3.5.1 חישוב סכום הזכייה
            playerCoins += winAmount # 3.5.2 הוספת הזכייה לכמות המטבעות של השחקן
            # 3.5.3 הצגת הודעת זכייה
            print(f"זכית! קיבלת {winAmount} מטבעות! כעת יש לך {playerCoins} מטבעות.")
        else:
            playerCoins -= bet # 3.6.1 הפחתת ההימור מכמות המטבעות של השחקן
            # 3.6.2 הצגת הודעת הפסד
            print(f"הפסדת! כעת יש לך {playerCoins} מטבעות.")

        # 3.7 בדיקה האם נגמרו המטבעות
        if playerCoins <= 0:
             break

    # 4. סיום המשחק אם אין יותר מטבעות
    if playerCoins <=0:
        print("נגמרו לך המטבעות!")
    print("תודה ששיחקת!")


# הפעלת המשחק
if __name__ == "__main__":
    play_slots_game()
"""
הסבר הקוד:
1. **ייבוא מודול `random`**:
   - `import random`: מייבא את המודול random, שישמש ליצירת בחירה אקראית של סמלים בגלגלי המכונה.

2.  **הגדרת הפונקציה `play_slots_game()`**:
    - `def play_slots_game():`: מגדירה פונקציה שמכילה את כל הלוגיקה של המשחק.
    - `playerCoins = 100`: מאתחלת את כמות המטבעות של השחקן ל-100.
    - `symbols = ["CHERRY", "BAR", "7", "SPACE"]`: יוצרת רשימה של סמלים שיופיעו על גלגלי המכונה.

3.  **לולאת משחק ראשית `while True:`**:
    -  לולאה אינסופית שתמשיך עד שהשחקן יסיים את המשחק או יגמרו לו המטבעות.
    - `print(f"יש לך {playerCoins} מטבעות.")`: מציגה לשחקן כמה מטבעות יש לו.

4.  **קבלת הימור מהשחקן**:
    -  `while True:`: לולאה נוספת שתמשיך עד שהקלט מהשחקן יהיה תקין.
    -  `try...except ValueError`: בלוק לטיפול בשגיאות. אם השחקן מכניס קלט שהוא לא מספר, תודפס הודעת שגיאה, והלולאה תמשיך.
    - `bet = int(input("כמה מטבעות תרצה להמר? (0 כדי לסיים) "))`: מבקשת מהשחקן להזין את ההימור שלו וממירה את הקלט למספר שלם.
    - `if bet < 0:`: בדיקה שההימור חיובי, אם לא, חוזרים ללולאת הקלט
    - `elif bet > playerCoins:`: אם השחקן מנסה להמר יותר ממה שיש לו, מודפסת הודעה והלולאה ממשיכה.
    - `else: break`: אם ההימור תקין, יוצאים מהלולאה הפנימית.

5.  **סיום המשחק אם ההימור הוא 0**:
    -  `if bet == 0: break`: אם השחקן הזין 0, המשחק יסתיים (יוצאים מהלולאה הראשית).

6.  **סיבוב גלגלי המכונה**:
    -   `wheel1 = random.choice(symbols)`: בוחרת סמל אקראי מהרשימה ומכניסה למשתנה wheel1.
    -   `wheel2 = random.choice(symbols)`:  בוחרת סמל אקראי מהרשימה ומכניסה למשתנה wheel2.
    -   `wheel3 = random.choice(symbols)`:  בוחרת סמל אקראי מהרשימה ומכניסה למשתנה wheel3.

7.  **הצגת הסמלים**:
    - `print(f"תוצאה: {wheel1} {wheel2} {wheel3}")`: מציגה את הסמלים שנבחרו על הגלגלים.

8.  **בדיקה האם השחקן ניצח**:
    - `if wheel1 == wheel2 == wheel3`: אם שלושת הסמלים זהים, השחקן ניצח.
    - `winAmount = bet * 10`: סכום הזכייה מחושב (ההימור כפול 10).
    - `playerCoins += winAmount`: סכום הזכייה מתווסף למטבעות של השחקן.
    - `print(f"זכית! קיבלת {winAmount} מטבעות! כעת יש לך {playerCoins} מטבעות.")`: מודפסת הודעת זכייה.

9.  **אם השחקן הפסיד**:
    - `else:`: אם שלושת הסמלים לא זהים, השחקן הפסיד.
    - `playerCoins -= bet`: סכום ההימור מופחת ממטבעות השחקן.
    - `print(f"הפסדת! כעת יש לך {playerCoins} מטבעות.")`: מודפסת הודעת הפסד.

10. **בדיקה האם נגמרו המטבעות**:
    - `if playerCoins <= 0:`: אם כמות המטבעות של השחקן הגיעה ל-0 או פחות, יוצאים מהלולאה הראשית.

11. **סיום המשחק**:
    - `if playerCoins <=0:`: אם השחקן הפסיד את כל המטבעות, מודפסת הודעה.
    - `print("תודה ששיחקת!")`: מודפסת הודעת סיום.

12. **הפעלת המשחק**:
    - `if __name__ == "__main__":`: מוודא שהפונקציה תרוץ רק כאשר מריצים את הסקריפט באופן ישיר.
    - `play_slots_game()`: מפעילה את פונקציית המשחק.
"""
