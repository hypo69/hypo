"""
HOCKEY:
=================
קושי: 4
-----------------
משחק הוקי פשוט לשני שחקנים. כל שחקן שולט בקבוצה ויורה לשער של השני.
השחקנים מתחלפים בתורות. כל שחקן מנסה לזרוק דיסקית הוקי (כדור) לשער של השני על ידי בחירת זווית וכוח. המטרה היא להבקיע יותר שערים מהיריב.
חוקי המשחק:
1. שני שחקנים משחקים בתורות.
2. כל שחקן מזין זווית וכוח זריקה.
3. התוצאה של הזריקה מחושבת באופן אקראי, בהתאם לזווית ולכוח.
4. שער מושג אם הזריקה "מוצלחת" (בהתאם לחישוב האקראי).
5. המשחק נמשך 10 תורות.
6. המנצח הוא השחקן עם הכי הרבה שערים בסוף המשחק.
-----------------
אלגוריתם:
1. אתחל את ניקוד השחקן הראשון (P1) ואת ניקוד השחקן השני (P2) ל-0.
2. התחל לולאה שתרוץ 10 פעמים (מספר התורות).
3. עבור כל תור:
   3.1. הדפס את התור הנוכחי.
   3.2. בקש מהשחקן הראשון (P1) להזין זווית זריקה (A1) וחוזק זריקה (S1).
   3.3. חשב את תוצאת הזריקה של P1 באמצעות פונקציה אקראית (האם הזריקה מוצלחת). אם מוצלחת, הגדל את ניקוד P1 ב-1.
   3.4. בקש מהשחקן השני (P2) להזין זווית זריקה (A2) וחוזק זריקה (S2).
   3.5. חשב את תוצאת הזריקה של P2 באמצעות פונקציה אקראית. אם מוצלחת, הגדל את ניקוד P2 ב-1.
   3.6. הדפס את הניקוד הנוכחי של שני השחקנים.
4. לאחר 10 תורות, השווה את הניקוד של שני השחקנים.
5. הדפס את תוצאת המשחק:
   5.1 אם ניקוד P1 גדול מניקוד P2, הכרז על שחקן P1 כמנצח.
   5.2 אם ניקוד P2 גדול מניקוד P1, הכרז על שחקן P2 כמנצח.
   5.3 אם ניקוד P1 שווה לניקוד P2, הכרז על תיקו.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeScores["<p align='left'>אתחול ניקוד:
    <code><b>
    player1Score = 0
    player2Score = 0
    turnNumber = 1
    </b></code></p>"]
    InitializeScores --> LoopStart{"תחילת לולאה: עבור 10 תורות"}
    LoopStart -- turnNumber <= 10 --> DisplayTurn["הצגת תור: <code><b>turnNumber</b></code>"]
    DisplayTurn --> Player1Input["קלט משחקן 1: <code><b>angle1, strength1</b></code>"]
    Player1Input --> CalculatePlayer1Shot["חישוב זריקה לשחקן 1: <code><b> isShotSuccessful(angle1, strength1) </b></code>"]
     CalculatePlayer1Shot -- מוצלח --> UpdatePlayer1Score["<code><b>player1Score = player1Score + 1</b></code>"]
    CalculatePlayer1Shot -- לא מוצלח --> Player2Input
     UpdatePlayer1Score --> Player2Input["קלט משחקן 2: <code><b>angle2, strength2</b></code>"]
    Player2Input --> CalculatePlayer2Shot["חישוב זריקה לשחקן 2: <code><b>isShotSuccessful(angle2, strength2)</b></code>"]
    CalculatePlayer2Shot -- מוצלח --> UpdatePlayer2Score["<code><b>player2Score = player2Score + 1</b></code>"]
    CalculatePlayer2Shot -- לא מוצלח --> DisplayScores
     UpdatePlayer2Score --> DisplayScores["הצגת ניקוד: <code><b>player1Score, player2Score</b></code>"]
    DisplayScores --> IncrementTurn["<code><b>turnNumber = turnNumber + 1</b></code>"]
     IncrementTurn --> LoopStart
    LoopStart -- turnNumber > 10 --> CompareScores["השוואת ניקוד: <code><b>player1Score, player2Score</b></code>"]
    CompareScores -- player1 > player2 --> Player1Wins["הצגת הודעה: <b>Player 1 Wins</b>"]
     CompareScores -- player2 > player1 --> Player2Wins["הצגת הודעה: <b>Player 2 Wins</b>"]
     CompareScores -- player1 == player2 --> Draw["הצגת הודעה: <b>Draw</b>"]
    Player1Wins --> End["סוף"]
    Player2Wins --> End
    Draw --> End
```
Legenda:
    Start - תחילת התוכנית.
    InitializeScores - אתחול הניקוד של שני השחקנים ל-0 ומונה התורות ל-1.
    LoopStart - תחילת לולאה שרצה 10 פעמים (10 תורות).
    DisplayTurn - הדפסת מספר התור הנוכחי.
    Player1Input - קבלת קלט של זווית וחוזק זריקה משחקן 1.
    CalculatePlayer1Shot - חישוב האם הזריקה של שחקן 1 מוצלחת.
    UpdatePlayer1Score - אם הזריקה של שחקן 1 מוצלחת, העלאת הניקוד שלו ב-1.
     Player2Input - קבלת קלט של זווית וחוזק זריקה משחקן 2.
     CalculatePlayer2Shot - חישוב האם הזריקה של שחקן 2 מוצלחת.
     UpdatePlayer2Score - אם הזריקה של שחקן 2 מוצלחת, העלאת הניקוד שלו ב-1.
    DisplayScores - הצגת הניקוד של שני השחקנים.
    IncrementTurn - העלאת מונה התורות ב-1.
    CompareScores - השוואת הניקוד בין שני השחקנים לאחר 10 תורות.
    Player1Wins - הדפסת הודעה ששחקן 1 ניצח.
    Player2Wins - הדפסת הודעה ששחקן 2 ניצח.
    Draw - הדפסת הודעה על תיקו.
     End - סיום התוכנית.
"""
import random

def is_shot_successful(angle, strength):
    """
    פונקציה המחזירה האם הזריקה הצליחה בהתאם לחישוב אקראי.

    :param angle: זווית הזריקה (לא בשימוש ישיר בחישוב).
    :param strength: חוזק הזריקה (לא בשימוש ישיר בחישוב).
    :return: True אם הזריקה הצליחה, False אם לא.
    """
    # סיכוי הצלחה אקראי, לצורך הפשטות
    return random.random() > 0.3

def play_hockey_game():
    """
    פונקציה המנהלת את משחק ההוקי בין שני שחקנים.
    """
    player1Score = 0  # אתחול ניקוד שחקן 1
    player2Score = 0  # אתחול ניקוד שחקן 2

    for turn in range(1, 11):  # לולאה עבור 10 תורות
        print(f"\nתור {turn}:")

        # תור של שחקן 1
        try:
            angle1 = int(input("שחקן 1, הזן זווית זריקה (0-90): "))
            strength1 = int(input("שחקן 1, הזן חוזק זריקה (1-10): "))
        except ValueError:
            print("קלט לא חוקי, אנא הזן מספרים שלמים.")
            continue

        if is_shot_successful(angle1, strength1): # קריאה לפונקציה האקראית
            player1Score += 1
            print("שחקן 1 הבקיע שער!")
        else:
            print("שחקן 1 החמיץ.")
        
        # תור של שחקן 2
        try:
            angle2 = int(input("שחקן 2, הזן זווית זריקה (0-90): "))
            strength2 = int(input("שחקן 2, הזן חוזק זריקה (1-10): "))
        except ValueError:
             print("קלט לא חוקי, אנא הזן מספרים שלמים.")
             continue

        if is_shot_successful(angle2, strength2): # קריאה לפונקציה האקראית
            player2Score += 1
            print("שחקן 2 הבקיע שער!")
        else:
            print("שחקן 2 החמיץ.")
        
        # הצגת הניקוד הנוכחי
        print(f"ניקוד: שחקן 1 = {player1Score}, שחקן 2 = {player2Score}")

    # הכרזת מנצח
    print("\n--- סיכום המשחק ---")
    if player1Score > player2Score:
        print("שחקן 1 ניצח!")
    elif player2Score > player1Score:
        print("שחקן 2 ניצח!")
    else:
        print("תיקו!")

if __name__ == "__main__":
    play_hockey_game()
"""
הסברים:
1.  ייבוא מודול `random`:
   - `import random`: ייבוא המודול `random` ליצירת מספרים אקראיים, לשימוש בחישוב האם הזריקה הצליחה.
2.  פונקציה `is_shot_successful(angle, strength)`:
   -  מקבלת את זווית הזריקה (`angle`) ואת חוזק הזריקה (`strength`) כארגומנטים (לא נעשה בהם שימוש ישיר).
   -  הפונקציה מחזירה `True` אם הזריקה הצליחה (אקראית) ו-`False` אם לא. לצורך הפשטות, ההצלחה נקבעת באופן אקראי באמצעות `random.random() > 0.3`.
3.  פונקציה `play_hockey_game()`:
   - מכילה את הלוגיקה הראשית של המשחק.
   - `player1Score = 0` ו-`player2Score = 0`: מאתחלת את ניקוד שני השחקנים לאפס.
   - לולאה ראשית `for turn in range(1, 11)`: הלולאה רצה 10 פעמים, ומייצגת את 10 התורות של המשחק.
    - הדפסת מספר התור הנוכחי.
  -   בקשה משחקן 1 להזין זווית זריקה וחוזק זריקה.
  -   קריאה לפונקציה `is_shot_successful` לבדיקה אם שחקן 1 הבקיע שער. אם כן, הניקוד שלו גדל.
   -  בקשה משחקן 2 להזין זווית זריקה וחוזק זריקה.
   -   קריאה לפונקציה `is_shot_successful` לבדיקה אם שחקן 2 הבקיע שער. אם כן, הניקוד שלו גדל.
   -  הדפסה של הניקוד המעודכן של שני השחקנים בסוף כל תור.
   -  הדפסה של הכרזת המנצח (או תיקו) בסוף המשחק.
4.  הפעלת המשחק:
   -  `if __name__ == "__main__":`: בלוק זה מבטיח שהפונקציה `play_hockey_game()` תופעל רק אם הקובץ מופעל ישירות ולא אם הוא מיובא כמודול.
   -  `play_hockey_game()`: קריאה לפונקציה שמפעילה את המשחק.
"""
