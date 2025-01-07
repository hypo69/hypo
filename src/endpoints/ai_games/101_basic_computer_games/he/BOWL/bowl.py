<BOWL>:
=================
קושי: 2
-----------------
המשחק "באולינג" מדמה משחק באולינג פשוט, בו השחקן מנסה להפיל את כל 10 הפינים. המשחק מורכב מ-10 סיבובים, ובכל סיבוב השחקן מקבל עד שני ניסיונות להפיל את הפינים. מספר הפינים שהופלו בכל ניסיון מוזן, וסך הכל הפינים שהופלו עבור כל סיבוב מחושב. בסוף המשחק מוצג מספר הפינים שהופלו בכל הסיבובים ובסה"כ.

חוקי המשחק:
1. המשחק כולל 10 סיבובים.
2. בכל סיבוב, השחקן יכול לנסות עד 2 פעמים להפיל את הפינים.
3. בכל ניסיון, השחקן מזין כמה פינים הפיל.
4. סך הפינים שהופלו בכל סיבוב מחושב ומצטבר לציון הכללי.
5. בסוף המשחק, מוצג ציון הפינים בכל סיבוב ובסה"כ.
-----------------
אלגוריתם:
1. אתחל משתנה `totalScore` ל-0.
2. התחל לולאה עבור 10 סיבובים:
   2.1 אתחל משתנה `roundScore` ל-0.
   2.2 התחל לולאה עבור 2 ניסיונות:
        2.2.1 בקש מהשחקן להזין את מספר הפינים שהופלו בניסיון הנוכחי.
        2.2.2 הוסף את מספר הפינים שהופלו ל-`roundScore`.
   2.3 הדפס את הניקוד לסיבוב הנוכחי.
   2.4 הוסף את `roundScore` ל-`totalScore`.
3. הדפס את הניקוד הכולל.
4. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeTotalScore["<p align='left'>אתחול משתנה:
    <code><b>
    totalScore = 0
    </b></code></p>"]
    InitializeTotalScore --> RoundLoopStart{"תחילת לולאה עבור 10 סיבובים"}
    RoundLoopStart -- עבור כל סיבוב --> InitializeRoundScore["<p align='left'>אתחול משתנה:
    <code><b>
    roundScore = 0
    </b></code></p>"]
    InitializeRoundScore --> TryLoopStart{"תחילת לולאה עבור 2 ניסיונות"}
    TryLoopStart -- עבור כל ניסיון --> InputPins["קלט מספר פינים שהופלו: <code><b>pins</b></code>"]
    InputPins --> AddPinsToRoundScore["<code><b>roundScore = roundScore + pins</b></code>"]
    AddPinsToRoundScore --> TryLoopEnd{"סוף לולאת ניסיונות?"}
    TryLoopEnd -- לא --> TryLoopStart
    TryLoopEnd -- כן --> OutputRoundScore["הצגת ניקוד לסיבוב: <code><b>roundScore</b></code>"]
    OutputRoundScore --> AddRoundScoreToTotal["<code><b>totalScore = totalScore + roundScore</b></code>"]
    AddRoundScoreToTotal --> RoundLoopEnd{"סוף לולאת הסיבובים?"}
     RoundLoopEnd -- לא --> RoundLoopStart
    RoundLoopEnd -- כן --> OutputTotalScore["הצגת ניקוד כולל: <code><b>totalScore</b></code>"]
    OutputTotalScore --> End["סוף"]
```

Legenda:
    Start - התחלת התוכנית.
    InitializeTotalScore - אתחול משתנה totalScore ל-0. משמש לספירת הניקוד הכולל במשחק.
    RoundLoopStart - תחילת לולאה, הפועלת עבור כל 10 הסיבובים במשחק.
    InitializeRoundScore - אתחול משתנה roundScore ל-0. משמש לספירת הניקוד בסיבוב הנוכחי.
    TryLoopStart - תחילת לולאה, הפועלת עבור 2 הניסיונות בכל סיבוב.
    InputPins - קליטת מספר הפינים שהופלו על ידי המשתמש בכל ניסיון.
    AddPinsToRoundScore - הוספת מספר הפינים שהופלו לניקוד של הסיבוב הנוכחי roundScore.
    TryLoopEnd - בדיקה האם סיימנו את הלולאה של 2 הניסיונות בסיבוב הנוכחי.
    OutputRoundScore - הצגת הניקוד של הסיבוב הנוכחי roundScore.
    AddRoundScoreToTotal - הוספת הניקוד של הסיבוב הנוכחי לניקוד הכולל totalScore.
    RoundLoopEnd - בדיקה האם סיימנו את הלולאה של 10 הסיבובים.
    OutputTotalScore - הצגת הניקוד הכולל totalScore.
    End - סוף התוכנית.
"""



"""
הסברים:
הקוד מדמה משחק באולינג פשוט. הוא כולל לולאה ראשית עבור 10 סיבובים. בכל סיבוב יש 2 ניסיונות להפיל פינים.
התוכנית קולטת את מספר הפינים שהופלו בכל ניסיון, מחשבת את הניקוד לסיבוב ואת הניקוד הכולל, ובסוף מציגה את התוצאות.
"""
# אתחול הניקוד הכולל של המשחק
totalScore = 0

# לולאה ראשית - עבור 10 סיבובים
for round in range(1, 11):
    # אתחול ניקוד הסיבוב הנוכחי
    roundScore = 0
    print(f"סיבוב {round}:")

    # לולאה עבור 2 ניסיונות בכל סיבוב
    for attempt in range(1, 3):
        # קבלת קלט מהמשתמש - כמה פינים הופלו בניסיון הנוכחי
        try:
            pins = int(input(f"  ניסיון {attempt}: כמה פינים הפלת? "))
            # הוספת הניקוד מהניסיון הנוכחי לניקוד הסיבוב
            roundScore += pins
        except ValueError:
            print("אנא הזן מספר שלם.")
            # חזרה לתחילת הלולאה הנוכחית
            continue
    # הדפסת ניקוד הסיבוב הנוכחי
    print(f"  ניקוד הסיבוב: {roundScore}")
    # הוספת ניקוד הסיבוב הנוכחי לניקוד הכולל
    totalScore += roundScore

# הדפסת הניקוד הכולל של המשחק
print(f"הניקוד הכולל שלך: {totalScore}")

"""
הסבר מפורט:
1. `totalScore = 0`: אתחול משתנה לספירת הניקוד הכולל של המשחק.
2. `for round in range(1, 11):`: לולאה שרצה 10 פעמים (לכל אחד מ-10 הסיבובים במשחק).
3.  `roundScore = 0`: אתחול משתנה לספירת הניקוד בסיבוב הנוכחי.
4.  `print(f"סיבוב {round}:")`: הדפסת מספר הסיבוב הנוכחי למשתמש.
5. `for attempt in range(1, 3):`: לולאה שרצה 2 פעמים, לכל אחד משני הניסיונות בכל סיבוב.
6.  `try...except ValueError`: קליטת קלט מהמשתמש עם טיפול בשגיאות קלט (כאשר המשתמש מזין משהו שאינו מספר שלם).
7.  `pins = int(input(f" ניסיון {attempt}: כמה פינים הפלת? "))`: בקשת קלט מהמשתמש לגבי מספר הפינים שהופלו בניסיון הנוכחי.
8.   `roundScore += pins`: הוספת מספר הפינים מהניסיון הנוכחי לניקוד הסיבוב הנוכחי.
9.  `print(f" ניקוד הסיבוב: {roundScore}")`: הדפסת הניקוד שהושג בסיבוב הנוכחי.
10. `totalScore += roundScore`: הוספת הניקוד של הסיבוב הנוכחי לניקוד הכולל של המשחק.
11. `print(f"הניקוד הכולל שלך: {totalScore}")`: הדפסת הניקוד הכולל של המשחק לאחר סיום כל הסיבובים.
"""
