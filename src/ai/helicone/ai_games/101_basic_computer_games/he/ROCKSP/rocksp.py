"""
ROCKSP:
=================
קושי: 2
-----------------
משחק "אבן, נייר ומספריים" הוא משחק יד קלאסי לשני שחקנים.
במשחק הזה, השחקן משחק נגד המחשב, כל אחד בוחר בו זמנית אחד משלושת האפשרויות: אבן, נייר או מספריים.
המשחק מוגדר על ידי חוקים ברורים, שקובעים איזה מהאפשרויות מנצחת את האחרת,
אבן מנצחת מספריים, מספריים מנצחות נייר ונייר מנצח אבן. אם שני השחקנים בוחרים את אותו הדבר, זה נחשב לתיקו.

חוקי המשחק:
1. השחקן בוחר אופציה בין אבן, נייר ומספריים.
2. המחשב בוחר אופציה באקראי בין אבן, נייר ומספריים.
3. המשחק קובע מנצח לפי החוקים הבאים:
    - אבן מנצחת מספריים.
    - מספריים מנצחות נייר.
    - נייר מנצח אבן.
4. אם השחקן והמחשב בוחרים באותה האופציה, המשחק הוא תיקו.
5. תוצאת המשחק מוצגת לשחקן.
6. השחקן יכול לשחק שוב.
-----------------
אלגוריתם:
1. הדפס את האפשרויות לבחירה (אבן, נייר, מספריים).
2. קבל קלט מהמשתמש עבור בחירתו (אבן, נייר או מספריים).
3. בחר באקראי בחירה עבור המחשב (אבן, נייר או מספריים).
4. השווה את בחירת המשתמש לבחירת המחשב:
    4.1 אם הבחירות שוות - הדפס "תיקו".
    4.2 אחרת:
        4.2.1 אם המשתמש בחר אבן והמחשב בחר מספריים או אם המשתמש בחר מספריים והמחשב בחר נייר או אם המשתמש בחר נייר והמחשב בחר אבן - הדפס "ניצחת".
        4.2.2 אחרת - הדפס "הפסדת".
5. שאל את המשתמש אם הוא רוצה לשחק שוב.
6. חזור לשלב 1 אם המשתמש רוצה לשחק שוב, אחרת - סיים.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> DisplayOptions["הצג אפשרויות: <code><b>אבן, נייר, מספריים</b></code>"]
    DisplayOptions --> GetUserChoice["קבל קלט מהמשתמש: <code><b>userChoice</b></code>"]
    GetUserChoice --> GenerateComputerChoice["יצירת בחירת מחשב אקראית: <code><b>computerChoice</b></code>"]
    GenerateComputerChoice --> CompareChoices{"השוואת בחירות: <code><b>userChoice == computerChoice?</b></code>"}
    CompareChoices -- כן --> OutputTie["הצג: <b>תיקו</b>"]
    OutputTie --> PlayAgainPrompt["שאל: <b>לשחק שוב?</b>"]
    CompareChoices -- לא --> CheckWinCondition["בדיקה: האם המשתמש ניצח?"]
    CheckWinCondition -- כן --> OutputWin["הצג: <b>ניצחת</b>"]
    OutputWin --> PlayAgainPrompt
    CheckWinCondition -- לא --> OutputLose["הצג: <b>הפסדת</b>"]
    OutputLose --> PlayAgainPrompt
    PlayAgainPrompt --> CheckPlayAgain{"בדיקה: <code><b>playAgain?</b></code>"}
    CheckPlayAgain -- כן --> DisplayOptions
    CheckPlayAgain -- לא --> End["סוף"]
```

Legenda:
    Start - תחילת המשחק.
    DisplayOptions - הצגת האפשרויות לבחירה: "אבן, נייר, מספריים".
    GetUserChoice - קבלת בחירת השחקן.
    GenerateComputerChoice - יצירת בחירה אקראית עבור המחשב.
    CompareChoices - השוואה בין בחירת השחקן לבחירת המחשב.
    OutputTie - הצגת הודעת תיקו.
    CheckWinCondition - בדיקה האם השחקן ניצח.
    OutputWin - הצגת הודעת ניצחון.
    OutputLose - הצגת הודעת הפסד.
    PlayAgainPrompt - שאלה לשחקן אם הוא רוצה לשחק שוב.
    CheckPlayAgain - בדיקה אם השחקן רוצה לשחק שוב.
    End - סיום המשחק.
"""
import random

# פונקציה המגדירה את לוגיקת המשחק
def play_rock_paper_scissors():
    # לולאה אינסופית המאפשרת לשחק שוב
    while True:
        # הצגת האפשרויות לשחקן
        print("בחר: (1) אבן, (2) נייר, (3) מספריים")

        # קבלת בחירת המשתמש
        try:
            user_choice = int(input("הכנס את בחירתך (1-3): "))
            # בדיקה האם הקלט תקין
            if user_choice < 1 or user_choice > 3:
                print("בחירה לא חוקית, אנא בחר בין 1 ל 3")
                continue
        except ValueError:
             print("קלט לא חוקי, אנא הזן מספר שלם בין 1 ל 3")
             continue
        
        # יצירת בחירה אקראית למחשב
        computer_choice = random.randint(1, 3)
        
        # המרת בחירות השחקן והמחשב לטקסט
        choices = {1: "אבן", 2: "נייר", 3: "מספריים"}
        user_choice_name = choices[user_choice]
        computer_choice_name = choices[computer_choice]

        # הדפסת הבחירות של השחקן והמחשב
        print(f"אתה בחרת: {user_choice_name}")
        print(f"המחשב בחר: {computer_choice_name}")

        # השוואת הבחירות וקביעת המנצח
        if user_choice == computer_choice:
            print("תיקו!")
        elif (user_choice == 1 and computer_choice == 3) or \
             (user_choice == 2 and computer_choice == 1) or \
             (user_choice == 3 and computer_choice == 2):
            print("ניצחת!")
        else:
            print("הפסדת!")

        # שאלה אם השחקן רוצה לשחק שוב
        play_again = input("רוצה לשחק שוב? (כן/לא): ").lower()
        if play_again != "כן":
            break # סיום המשחק אם השחקן לא מעוניין לשחק שוב

# הפעלת המשחק
if __name__ == "__main__":
    play_rock_paper_scissors()

"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    - `import random`: ייבוא המודול `random` המשמש ליצירת בחירה אקראית של המחשב.
2.  **הגדרת הפונקציה `play_rock_paper_scissors()`**:
    - פונקציה זו מכילה את כל הלוגיקה של המשחק אבן נייר ומספריים.
3.  **לולאת המשחק הראשית `while True:`**:
    - לולאה אינסופית המאפשרת לשחק כמה פעמים שרוצים עד שהמשתמש בוחר שלא לשחק שוב.
4.  **הצגת האפשרויות לשחקן**:
    -  `print("בחר: (1) אבן, (2) נייר, (3) מספריים")`: מציגה למשתמש את אפשרויות הבחירה.
5.  **קבלת קלט מהמשתמש**:
    - `try...except ValueError`: טיפול בשגיאות קלט אפשריות. אם המשתמש יזין משהו שאינו מספר שלם, תודפס הודעת שגיאה.
    - `user_choice = int(input("הכנס את בחירתך (1-3): "))`: קבלת קלט מהמשתמש והמרתו למספר שלם.
     - `if user_choice < 1 or user_choice > 3:` : בדיקה שהקלט שהתקבל מהמשתמש הוא בטווח הנכון.
6.  **יצירת בחירה אקראית למחשב**:
    - `computer_choice = random.randint(1, 3)`: המחשב בוחר באופן אקראי מספר שלם בין 1 ל-3.
7.  **המרה לטקסט**:
     -  `choices = {1: "אבן", 2: "נייר", 3: "מספריים"}`: יצירת מילון למיפוי מספרים למילים.
     -  `user_choice_name = choices[user_choice]`: המרת הבחירה של המשתמש לשם.
     -   `computer_choice_name = choices[computer_choice]`: המרת הבחירה של המחשב לשם.
8.  **הדפסת הבחירות**:
     -  `print(f"אתה בחרת: {user_choice_name}")` : הדפסת הבחירה של המשתמש.
     -  `print(f"המחשב בחר: {computer_choice_name}")` : הדפסת הבחירה של המחשב.
9.  **השוואת הבחירות וקביעת המנצח**:
    - `if user_choice == computer_choice:`: בדיקה אם הבחירות זהות - במקרה כזה המשחק מסתיים בתיקו.
    - `elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):`: בדיקה של כל אחד מתנאי הניצחון עבור המשתמש.
    - `else: print("הפסדת!")`: אם המשתמש לא ניצח, אז הוא הפסיד.
10. **שאלה האם לשחק שוב**:
    - `play_again = input("רוצה לשחק שוב? (כן/לא): ").lower()`: בקשת קלט מהמשתמש, האם הוא רוצה לשחק שוב והמרת הקלט לאותיות קטנות.
    - `if play_again != "כן": break`: אם המשתמש לא מעוניין לשחק שוב, הלולאה הראשית תופסק.
11. **הפעלת המשחק**:
    -  `if __name__ == "__main__":`: בלוק זה מבטיח שהפונקציה `play_rock_paper_scissors()` תופעל רק אם הקובץ מופעל ישירות, ולא אם הוא מיובא כמודול.
    - `play_rock_paper_scissors()`: קריאה לפונקציה להפעלת המשחק.
"""
