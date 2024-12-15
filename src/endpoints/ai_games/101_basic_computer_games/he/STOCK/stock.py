"""
STOCK:
=================
קושי: 5
-----------------
משחק "מניות" הוא סימולציה פשוטה של מסחר במניות. השחקן מתחיל עם סכום כסף מסוים ועליו לקנות ולמכור מניות במחירים משתנים על מנת להרוויח כסף. המשחק נמשך עד שהשחקן מחליט לסיים או כאשר אין לו יותר כסף להשקיע.

חוקי המשחק:
1. השחקן מתחיל עם סכום כסף התחלתי.
2. בכל תור, השחקן יכול לקנות או למכור מניות.
3. מחיר המניות משתנה באקראי בכל תור.
4. השחקן יכול לראות את כמות הכסף שלו, את כמות המניות שברשותו ואת מחיר המניה הנוכחי בכל תור.
5. המשחק מסתיים כאשר השחקן בוחר לסיים או כאשר אין לו מספיק כסף לקנות מניות.
-----------------
אלגוריתם:
1. אתחל את סכום הכסף ההתחלתי של השחקן (1000).
2. אתחל את מספר המניות שברשות השחקן (0).
3. אתחל את מחיר המניה לערך התחלתי (5).
4. הצג לשחקן את מצב ההתחלתי: סכום כסף, מניות ומחיר מניה.
5. התחל לולאה "כל עוד השחקן לא בחר לסיים":
   5.1. שאל את השחקן מה הוא רוצה לעשות (לקנות, למכור, לסיים).
   5.2. אם השחקן בחר לקנות מניות:
      5.2.1. שאל את השחקן כמה מניות הוא רוצה לקנות.
      5.2.2. חשב את סך המחיר של המניות.
      5.2.3. אם לשחקן אין מספיק כסף, הצג הודעה מתאימה וחזור לתחילת הלולאה.
      5.2.4. עדכן את סכום הכסף של השחקן ע"י הפחתת סך המחיר.
      5.2.5. עדכן את כמות המניות של השחקן ע"י הוספת המניות שנקנו.
   5.3. אם השחקן בחר למכור מניות:
      5.3.1. שאל את השחקן כמה מניות הוא רוצה למכור.
      5.3.2. אם לשחקן אין מספיק מניות, הצג הודעה מתאימה וחזור לתחילת הלולאה.
      5.3.3. חשב את הרווח ממכירת המניות.
      5.3.4. עדכן את סכום הכסף של השחקן ע"י הוספת הרווח.
      5.3.5. עדכן את כמות המניות של השחקן ע"י הפחתת המניות שנמכרו.
   5.4. אם השחקן בחר לסיים, צא מהלולאה.
   5.5. עדכן את מחיר המניה בערך אקראי בין 1 ל-10.
   5.6. הצג לשחקן את מצב הנוכחי: סכום כסף, מניות ומחיר מניה.
6. הצג לשחקן הודעת סיום.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    money = 1000<br>
    stocks = 0<br>
    stockPrice = 5
    </b></code></p>"]
    InitializeVariables --> DisplayStatus["הצג מצב התחלתי: 
    <code><b>
    כסף: {money}<br>
    מניות: {stocks}<br>
    מחיר מניה: {stockPrice}
    </b></code>"]
    DisplayStatus --> LoopStart{"תחילת לולאה: כל עוד השחקן לא בחר לסיים"}
    LoopStart -- כן --> InputAction["קלט פעולה: <b>קנה/מכור/סיים</b>"]
    InputAction --> CheckAction{"בדיקה: <code><b>action == 'קנה'?</b></code>"}
    CheckAction -- כן --> InputBuyStocks["קלט כמה מניות לקנות: <code><b>buyStocks</b></code>"]
    InputBuyStocks --> CalculateCost["חשב עלות: <code><b>cost = buyStocks * stockPrice</b></code>"]
    CalculateCost --> CheckEnoughMoney{"בדיקה: <code><b>money >= cost?</b></code>"}
    CheckEnoughMoney -- כן --> UpdateMoneyBuy["<code><b>money = money - cost</b></code>"]
    UpdateMoneyBuy --> UpdateStocksBuy["<code><b>stocks = stocks + buyStocks</b></code>"]
    UpdateStocksBuy --> UpdateStockPrice["<code><b>stockPrice = random(1,10)</b></code>"]
     UpdateStockPrice --> DisplayStatusLoop["הצג מצב נוכחי:
    <code><b>
    כסף: {money}<br>
    מניות: {stocks}<br>
    מחיר מניה: {stockPrice}
    </b></code>"]
     DisplayStatusLoop --> LoopStart
    CheckEnoughMoney -- לא --> OutputNotEnoughMoney["הודעה: <b>אין מספיק כסף</b>"]
    OutputNotEnoughMoney --> LoopStart
    CheckAction -- לא --> CheckSell{"בדיקה: <code><b>action == 'מכור'?</b></code>"}
    CheckSell -- כן --> InputSellStocks["קלט כמה מניות למכור: <code><b>sellStocks</b></code>"]
    InputSellStocks --> CheckEnoughStocks{"בדיקה: <code><b>stocks >= sellStocks?</b></code>"}
    CheckEnoughStocks -- כן --> CalculateProfit["חשב רווח: <code><b>profit = sellStocks * stockPrice</b></code>"]
    CalculateProfit --> UpdateMoneySell["<code><b>money = money + profit</b></code>"]
    UpdateMoneySell --> UpdateStocksSell["<code><b>stocks = stocks - sellStocks</b></code>"]
     UpdateStocksSell --> UpdateStockPrice2["<code><b>stockPrice = random(1,10)</b></code>"]
        UpdateStockPrice2 --> DisplayStatusLoop2["הצג מצב נוכחי:
    <code><b>
    כסף: {money}<br>
    מניות: {stocks}<br>
    מחיר מניה: {stockPrice}
    </b></code>"]
    DisplayStatusLoop2 --> LoopStart
    CheckEnoughStocks -- לא --> OutputNotEnoughStocks["הודעה: <b>אין מספיק מניות</b>"]
    OutputNotEnoughStocks --> LoopStart
     CheckSell -- לא --> CheckExit{"בדיקה: <code><b>action == 'סיים'?</b></code>"}
      CheckExit -- כן --> OutputEndGame["הודעה: <b>המשחק הסתיים</b>"]
     OutputEndGame --> End["סוף"]
     CheckExit -- לא --> OutputInvalidAction["הודעה: <b>פעולה לא חוקית</b>"]
      OutputInvalidAction --> LoopStart
     LoopStart -- לא --> End
```

Legenda:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: money (כסף התחלתי) = 1000, stocks (מניות התחלתיות) = 0, stockPrice (מחיר מניה התחלתי) = 5.
    DisplayStatus - הצגת מצב התחלתי: כסף, מניות ומחיר מניה.
    LoopStart - תחילת הלולאה, הממשיכה כל עוד השחקן לא בחר לסיים.
    InputAction - קלט פעולה מהמשתמש: קנה, מכור או סיים.
    CheckAction - בדיקה האם הפעולה היא 'קנה'.
    InputBuyStocks - קלט כמה מניות השחקן רוצה לקנות.
    CalculateCost - חישוב עלות הקנייה.
    CheckEnoughMoney - בדיקה האם יש מספיק כסף לקנות.
    UpdateMoneyBuy - עדכון כמות הכסף לאחר קנייה.
    UpdateStocksBuy - עדכון כמות המניות לאחר קנייה.
    OutputNotEnoughMoney - הצגת הודעה שאין מספיק כסף.
    CheckSell - בדיקה האם הפעולה היא 'מכור'.
    InputSellStocks - קלט כמה מניות השחקן רוצה למכור.
    CheckEnoughStocks - בדיקה האם יש מספיק מניות למכירה.
    CalculateProfit - חישוב הרווח ממכירת המניות.
    UpdateMoneySell - עדכון כמות הכסף לאחר מכירה.
    UpdateStocksSell - עדכון כמות המניות לאחר מכירה.
    OutputNotEnoughStocks - הצגת הודעה שאין מספיק מניות למכירה.
    CheckExit - בדיקה האם הפעולה היא 'סיים'.
    OutputEndGame - הצגת הודעה שהמשחק הסתיים.
    OutputInvalidAction - הודעה שהפעולה לא חוקית.
    End - סוף התוכנית.
     UpdateStockPrice - עדכון מחיר המניה באקראי.
      DisplayStatusLoop- הצגת מצב נוכחי: כסף, מניות ומחיר מניה.
     UpdateStockPrice2- עדכון מחיר המניה באקראי.
     DisplayStatusLoop2 - הצגת מצב נוכחי: כסף, מניות ומחיר מניה.
"""
import random

# אתחול סכום הכסף ההתחלתי של השחקן
money = 1000
# אתחול מספר המניות שברשות השחקן
stocks = 0
# אתחול מחיר המניה
stockPrice = 5

# לולאת המשחק הראשית
while True:
    # הדפסת מצב השחקן
    print(f"כסף: {money}, מניות: {stocks}, מחיר מניה: {stockPrice}")

    # קבלת פקודה מהמשתמש
    action = input("מה תרצה לעשות? (קנה/מכור/סיים): ").lower()

    if action == 'קנה':
        # קבלת מספר מניות לקנייה
        try:
            buyStocks = int(input("כמה מניות תרצה לקנות? "))
        except ValueError:
            print("אנא הזן מספר שלם.")
            continue
        # חישוב עלות הקנייה
        cost = buyStocks * stockPrice

        # בדיקה אם יש מספיק כסף
        if money < cost:
            print("אין לך מספיק כסף לקנות את המניות האלה.")
        else:
             # עדכון כסף ומניות
            money -= cost
            stocks += buyStocks

    elif action == 'מכור':
        # קבלת מספר מניות למכירה
         try:
            sellStocks = int(input("כמה מניות תרצה למכור? "))
         except ValueError:
            print("אנא הזן מספר שלם.")
            continue
        # בדיקה אם יש מספיק מניות
        if stocks < sellStocks:
            print("אין לך מספיק מניות למכור.")
        else:
            # חישוב רווח מהמכירה
            profit = sellStocks * stockPrice
            # עדכון כסף ומניות
            money += profit
            stocks -= sellStocks

    elif action == 'סיים':
        # סיום המשחק
        print("תודה ששיחקת!")
        break
    else:
        # פעולה לא חוקית
        print("פעולה לא חוקית. אנא בחר 'קנה', 'מכור' או 'סיים'.")

    # עדכון מחיר המניה באקראי
    stockPrice = random.randint(1, 10)
"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    -  `import random`: ייבוא המודול random, המשמש ליצירת מספר אקראי.
2.  **אתחול משתנים**:
    -  `money = 1000`: אתחול סכום הכסף ההתחלתי של השחקן.
    -  `stocks = 0`: אתחול מספר המניות שברשות השחקן.
    -  `stockPrice = 5`: אתחול מחיר המניה.
3.  **לולאת המשחק `while True`**:
    -   לולאה אינסופית, הממשיכה עד שהמשתמש יבחר לסיים (הפקודה `break` תסיים את הלולאה).
    -  `print(f"כסף: {money}, מניות: {stocks}, מחיר מניה: {stockPrice}")`: הצגת מצב השחקן הנוכחי (כסף, מניות ומחיר מניה).
    -  `action = input("מה תרצה לעשות? (קנה/מכור/סיים): ").lower()`: קבלת פקודה מהמשתמש (קנה, מכור או סיים) והפיכתה לאותיות קטנות.
    -   **פעולת קנייה**:
        -   `if action == 'קנה':`: בדיקה האם המשתמש בחר לקנות.
        -    `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין משהו שאינו מספר שלם, יוצג הודעת שגיאה.
        -   `buyStocks = int(input("כמה מניות תרצה לקנות? "))`: קבלת מספר מניות לקנייה מהמשתמש.
        -   `cost = buyStocks * stockPrice`: חישוב עלות הקנייה.
        -   `if money < cost:`: בדיקה האם יש מספיק כסף לקנייה. אם לא, הודעה מתאימה תוצג והלולאה תמשיך.
        -   `money -= cost`: עדכון סכום הכסף לאחר הקנייה.
        -   `stocks += buyStocks`: עדכון מספר המניות לאחר הקנייה.
    -   **פעולת מכירה**:
        -  `elif action == 'מכור':`: בדיקה האם המשתמש בחר למכור.
        -   `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט אפשריות. אם המשתמש יזין משהו שאינו מספר שלם, יוצג הודעת שגיאה.
        -    `sellStocks = int(input("כמה מניות תרצה למכור? "))`: קבלת מספר מניות למכירה מהמשתמש.
        -   `if stocks < sellStocks:`: בדיקה האם יש מספיק מניות למכירה. אם לא, הודעה מתאימה תוצג והלולאה תמשיך.
        -   `profit = sellStocks * stockPrice`: חישוב הרווח מהמכירה.
        -   `money += profit`: עדכון סכום הכסף לאחר המכירה.
        -   `stocks -= sellStocks`: עדכון מספר המניות לאחר המכירה.
    -   **סיום המשחק**:
        -   `elif action == 'סיים':`: בדיקה האם המשתמש בחר לסיים.
        -   `print("תודה ששיחקת!")`: הודעת סיום.
        -   `break`: סיום הלולאה (והמשחק).
    -   **פעולה לא חוקית**:
        -   `else:`: אם המשתמש לא בחר באחת האפשרויות החוקיות, מוצגת הודעה שהפעולה לא חוקית.
    -   `stockPrice = random.randint(1, 10)`: עדכון מחיר המניה בערך אקראי בין 1 ל-10.
"""
