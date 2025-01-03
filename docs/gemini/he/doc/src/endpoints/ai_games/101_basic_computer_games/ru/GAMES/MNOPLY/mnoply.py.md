# MNOPLY

## סקירה כללית

משחק "מונופול" הוא גרסה פשוטה של משחק לוח, בו שני שחקנים מתחלפים בהטלת קובייה ומתקדמים על לוח משחק בן 24 משבצות. כל משבצת מתאימה לערך מסוים, אותו השחקן משלם או מקבל. מטרת המשחק היא להישאר עם הסכום הגדול ביותר של כסף לאחר מספר סיבובים מוגדר.

## תוכן עניינים

1. [סקירה כללית](#סקירה-כללית)
2. [קבועים](#קבועים)
3. [לולאות](#לולאות)
4. [קוד](#קוד)
    - [משתנים](#משתנים)
    - [לולאה ראשית](#לולאה-ראשית)
    - [קביעת מנצח](#קביעת-מנצח)
5. [הסבר קוד](#הסבר-קוד)

## קבועים

- `player1Money`: הסכום ההתחלתי של השחקן הראשון.
- `player2Money`: הסכום ההתחלתי של השחקן השני.
- `boardValues`: רשימה המכילה את הערכים של כל משבצת על הלוח.
- `numberOfRounds`: מספר הסיבובים במשחק.
- `player1Position`: מיקום השחקן הראשון.
- `player2Position`: מיקום השחקן השני.

## לולאות

- הלולאה החיצונית רצה על מספר הסיבובים שנקבע.
- הלולאה הפנימית רצה על כל שחקן בכל סיבוב.

## קוד

### משתנים

- `player1Money` (int): ההון ההתחלתי של השחקן הראשון.
- `player2Money` (int): ההון ההתחלתי של השחקן השני.
- `boardValues` (list): רשימה של ערכים המייצגים את עלות כל משבצת בלוח.
- `numberOfRounds` (int): מספר הסיבובים במשחק.
- `player1Position` (int): מיקום התחלתי של השחקן הראשון.
- `player2Position` (int): מיקום התחלתי של השחקן השני.

### לולאה ראשית

- לולאה שעוברת על מספר הסיבובים שהוגדרו מראש.
- עבור כל שחקן, מדמה הטלת קובייה (מספר אקראי בין 1 ל-6).
- מעדכנת את מיקום השחקן בהתאם לתוצאה של הקובייה.
- מעדכנת את הסכום של השחקן בהתאם לערך המשבצת.
- מדפיסה את המיקום הנוכחי של השחקן והסכום שלו.

### קביעת מנצח

- לאחר כל הסיבובים, המערכת קובעת את המנצח על סמך כמות הכסף שנותרה לכל שחקן.
- מודפסת הודעה עם שם המנצח או הודעה על תיקו.

## הסבר קוד

1.  **הגדרת משתנים**:
    -   `player1Money = 1500`: קובע את הסכום ההתחלתי של השחקן הראשון.
    -   `player2Money = 1500`: קובע את הסכום ההתחלתי של השחקן השני.
    -   `boardValues`: רשימה המכילה את הערכים של כל משבצת במשחק (ערכים חיוביים או שליליים).
    -   `numberOfRounds = 10`: מספר הסיבובים במשחק.
    -   `player1Position = 0`: מיקום התחלתי של השחקן הראשון.
    -   `player2Position = 0`: מיקום התחלתי של השחקן השני.

2.  **לולאת המשחק הראשית**:
    -   `for roundNumber in range(1, numberOfRounds + 1):`: לולאה שחוזרת על כל סיבוב במשחק.
        -   הדפסת מספר הסיבוב הנוכחי.
    -   `for player in range(1, 3):`: לולאה שחוזרת על כל שחקן בכל סיבוב.
        -   הדפסת מידע על השחקן הנוכחי.
        -   `diceRoll = random.randint(1, 6)`: הגרלת מספר אקראי (תוצאת הקובייה).
        -   הדפסת תוצאת הקובייה.
        -   **עדכון מיקום השחקן**:
            -   `if player == 1:`: בדיקה איזה שחקן משחק כרגע.
            -   `player1Position = (player1Position + diceRoll) % 24`: עדכון מיקום השחקן הראשון על הלוח המעגלי.
            -   `currentPosition = player1Position`: עדכון המיקום הנוכחי של השחקן הראשון.
            -   `player1Money += boardValues[currentPosition]`: עדכון הסכום של השחקן הראשון בהתאם למשבצת.
            -   `currentMoney = player1Money`: הסכום הנוכחי של השחקן הראשון.
            -   `else:`: פעולות דומות עבור השחקן השני עם המשתנים שלו.
        -   `print(f"   מיקום: {currentPosition + 1}, כסף: {currentMoney}")`: הדפסת מיקום השחקן הנוכחי והסכום שלו.

3.  **קביעת המנצח**:
    -   `print("\\nהמשחק הסתיים!")`: הדפסת הודעה שהמשחק הסתיים.
    -   `if player1Money > player2Money:`: השוואה בין הסכומים של השחקנים כדי לקבוע מנצח.
        -   הדפסת מידע על המנצח או על תיקו.