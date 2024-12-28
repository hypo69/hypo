
<HORSES>:
=================
קושי: 4
-----------------
המשחק "סוסים" מדמה מרוץ סוסים בין מספר סוסים. השחקן בוחר סוס, וצופה במרוץ. הסוסים מתקדמים באקראי עד שאחד מהם חוצה את קו הסיום, והשחקן זוכה אם בחר בסוס המנצח.

חוקי המשחק:
1. המשחק מדמה מרוץ בין מספר סוסים.
2. השחקן בוחר את מספר הסוס שלו, מתוך רשימת סוסים.
3. הסוסים מתקדמים באופן אקראי, כאשר בכל תור מתקדם כל סוס בצעד אחד או לא מתקדם כלל.
4. המרוץ מסתיים כאשר אחד הסוסים הגיע לקו הסיום.
5. השחקן זוכה אם הסוס שבחר הוא הסוס המנצח.
-----------------
אלגוריתם:
1. הצג רשימה של מספרי סוסים לבחירה.
2. קבל קלט מהשחקן, את מספר הסוס שהוא בוחר.
3. אתחל את מיקום כל הסוסים ל-0.
4. כל עוד אין מנצח:
  4.1. עבור על כל סוס:
    4.1.1. צור מספר אקראי (0 או 1).
    4.1.2. אם המספר האקראי הוא 1, קדם את הסוס בצעד אחד.
  4.2. הצג את מיקום כל הסוסים.
  4.3. בדוק האם יש סוס שהגיע לקו הסיום (מיקום 20).
  4.4. אם יש מנצח, צא מהלולאה.
5. הצג את הסוס המנצח.
6. אם הסוס המנצח הוא הסוס שבחר השחקן, הצג הודעת ניצחון, אחרת, הצג הודעת הפסד.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> DisplayHorses["הצגת רשימת סוסים"]
    DisplayHorses --> InputUserChoice["קלט: בחירת מספר סוס מהמשתמש"]
    InputUserChoice --> InitializePositions["אתחול: מיקום כל הסוסים ל-0"]
    InitializePositions --> LoopStart{"תחילת לולאה: כל עוד אין מנצח"}
    LoopStart -- כן --> ForEachHorse["לכל סוס"]
    ForEachHorse --> GenerateRandomStep["צור מספר אקראי (0 או 1)"]
    GenerateRandomStep --> UpdatePosition{"אם המספר האקראי הוא 1: קדם את מיקום הסוס ב-1"}
    UpdatePosition --> NextHorse["מעבר לסוס הבא"]
    NextHorse -- כל הסוסים עברו --> DisplayPositions["הצג את מיקום הסוסים"]
    DisplayPositions --> CheckWinner{"בדיקה: האם סוס הגיע לקו הסיום (20)"}
     CheckWinner -- כן --> OutputWinner["הצג מנצח"]
    OutputWinner --> CheckUserWin{"בדיקה: האם המנצח הוא הסוס שהמשתמש בחר"}
    CheckUserWin -- כן --> OutputWinMessage["הצג: 'ניצחת!'"]
    CheckUserWin -- לא --> OutputLoseMessage["הצג: 'הפסדת!'"]
    OutputLoseMessage --> End["סוף"]
     OutputWinMessage --> End
     CheckWinner -- לא --> LoopStart
      LoopStart -- לא --> End
```
Legenda:
  Start - התחלת התוכנית.
  DisplayHorses - הצגת רשימת סוסים למשתמש.
  InputUserChoice - קבלת מספר הסוס שהמשתמש בחר.
  InitializePositions - אתחול מיקום כל הסוסים ל-0.
  LoopStart - תחילת לולאת המשחק, כל עוד אין מנצח.
  ForEachHorse - מעבר על כל הסוסים.
  GenerateRandomStep - יצירת מספר אקראי (0 או 1) לכל סוס.
  UpdatePosition - עדכון מיקום הסוס אם המספר האקראי הוא 1.
  NextHorse - מעבר לסוס הבא.
  DisplayPositions - הצגת מיקום כל הסוסים במסלול.
  CheckWinner - בדיקה האם אחד הסוסים הגיע לסוף המסלול.
  OutputWinner - הצגת הסוס המנצח.
  CheckUserWin - בדיקה האם הסוס המנצח הוא הסוס שהמשתמש בחר.
  OutputWinMessage - הצגת הודעת ניצחון למשתמש.
  OutputLoseMessage - הצגת הודעת הפסד למשתמש.
  End - סיום המשחק.
"""
import random

# הגדרת מספר הסוסים
NUM_HORSES = 4
# הגדרת אורך המסלול
TRACK_LENGTH = 20

def play_horses_game():
    """
    מפעיל את משחק מרוץ הסוסים.
    """
    print("ברוכים הבאים למרוץ הסוסים!")
    print("בחר את הסוס שלך (1-4):")
    # הצגת מספרי הסוסים
    for i in range(NUM_HORSES):
        print(f"{i+1}. סוס {i+1}")
    # קלט בחירת המשתמש
    while True:
        try:
            user_horse = int(input("בחר את מספר הסוס שלך: "))
            if 1 <= user_horse <= NUM_HORSES:
                break
            else:
                print("בחירה לא חוקית, אנא בחר מספר סוס בין 1 ל-4.")
        except ValueError:
            print("בחירה לא חוקית, אנא הזן מספר.")

    # אתחול מיקום הסוסים
    horse_positions = [0] * NUM_HORSES
    
    # לולאת המשחק
    while True:
        # הדפסת מצב המסלול
        print_track(horse_positions)
        
        # בדיקה האם יש מנצח
        winner_horse = check_winner(horse_positions)
        if winner_horse:
            print(f"\nסוס {winner_horse+1} ניצח!")
            if winner_horse + 1 == user_horse:
                print("ניצחת!")
            else:
                print("הפסדת!")
            break
        
        # קידום הסוסים
        for i in range(NUM_HORSES):
            step = random.randint(0, 1)
            horse_positions[i] += step

def print_track(horse_positions):
  """
  מדפיס את מצב המסלול, כאשר כל סוס מיוצג על ידי מספרו.
  
  Args:
    horse_positions (list): רשימה של מיקום כל סוס.
  """
  track = ""
  for i in range(TRACK_LENGTH + 1):
      horse_on_pos = False
      for horse_index, pos in enumerate(horse_positions):
          if pos == i:
            track += str(horse_index + 1) # מדפיס את מספר הסוס
            horse_on_pos = True
            break
      if not horse_on_pos:
         track += "_"
  print(track)

def check_winner(horse_positions):
  """
  בודק האם יש מנצח ומחזיר את מספר הסוס המנצח, אם קיים.

  Args:
    horse_positions (list): רשימה של מיקום כל סוס.

  Returns:
    int: מספר הסוס המנצח, אם קיים, אחרת None.
  """
  for i, pos in enumerate(horse_positions):
        if pos >= TRACK_LENGTH:
            return i
  return None

# הפעלת המשחק רק אם הקובץ מורץ ישירות
if __name__ == "__main__":
    play_horses_game()
```
<הסברים:>
הסבר מפורט לקוד:

1.  **ייבוא מודול `random`:**
    - `import random`: ייבוא מודול `random` לשימוש בפונקציות ליצירת מספרים אקראיים.
2.  **הגדרת קבועים:**
    - `NUM_HORSES = 4`: קבוע המגדיר את מספר הסוסים המשתתפים במרוץ.
    - `TRACK_LENGTH = 20`: קבוע המגדיר את אורך המסלול של המרוץ.
3.  **פונקציה `play_horses_game()`:**
    -   מגדירה את הלוגיקה הראשית של המשחק.
    -  `print("ברוכים הבאים למרוץ הסוסים!")`: הצגת הודעת פתיחה למשחק.
    -  `print("בחר את הסוס שלך (1-4):")`: הנחיית השחקן לבחור סוס.
    -  **לולאת קלט בחירת השחקן:**
        -  `while True:`: לולאה אינסופית עד שהשחקן יזין קלט חוקי.
        -  `try...except ValueError`: טיפול בשגיאות במקרה שהשחקן מזין קלט שאינו מספר.
        -  `user_horse = int(input("בחר את מספר הסוס שלך: "))`: קבלת קלט מהשחקן (מספר הסוס) והמרתו למספר שלם.
        -  `if 1 <= user_horse <= NUM_HORSES:`: בדיקה שהקלט חוקי (בין 1 למספר הסוסים).
        -   `break`: יציאה מהלולאה אם הקלט חוקי.
        -   `else:`: הצגת הודעת שגיאה אם הקלט לא חוקי.
    - `horse_positions = [0] * NUM_HORSES`: יצירת רשימה המכילה את מיקומי הסוסים. כל הסוסים מתחילים במיקום 0.
    -   **לולאת המשחק:**
        -   `while True:`: לולאה אינסופית עד שמוכרע מנצח.
        -   `print_track(horse_positions)`: קריאה לפונקציה המציגה את מצב המסלול.
        -   `winner_horse = check_winner(horse_positions)`: קריאה לפונקציה שבודקת אם יש מנצח ומחזירה את מספר הסוס המנצח או None.
        -   `if winner_horse:`: בדיקה האם יש מנצח.
             - `print(f"\nסוס {winner_horse+1} ניצח!")`: הודעה על הסוס המנצח.
             - `if winner_horse + 1 == user_horse:`: בדיקה האם הסוס המנצח הוא הסוס שהמשתמש בחר.
                 - הצגת הודעת ניצחון או הפסד.
             -  `break`: יציאה מלולאת המשחק לאחר שהוכרע מנצח.
         -   **קידום הסוסים:**
             - `for i in range(NUM_HORSES)`: מעבר על כל הסוסים.
             -  `step = random.randint(0, 1)`: יצירת מספר אקראי (0 או 1) עבור כל סוס, לצורך קידומו.
             -   `horse_positions[i] += step`: עדכון מיקום הסוס, או שלא מקדם אם יצא 0.
4.  **פונקציה `print_track(horse_positions)`:**
    -   מדפיסה את מסלול המרוץ כאשר כל סוס מיוצג על ידי מספרו.
    - `track = ""`: מחרוזת ריקה לאתחול המסלול.
    - `for i in range(TRACK_LENGTH + 1):`: לולאה שעוברת על כל מיקום במסלול.
    -   `horse_on_pos = False`: משתנה בוליאני המשמש לסימון אם יש סוס במיקום הנוכחי.
    -   `for horse_index, pos in enumerate(horse_positions):`: לולאה שעוברת על כל הסוסים ומיקומם.
    -   `if pos == i:`: אם מיקום הסוס הנוכחי שווה למיקום הנוכחי במסלול:
        -   `track += str(horse_index + 1)`: הוספת מספר הסוס למחרוזת המסלול.
        -   `horse_on_pos = True`: סימון שיש סוס במיקום הנוכחי.
        -   `break`: יציאה מהלולאה הפנימית.
    -    `if not horse_on_pos:`: אם אין סוס במיקום הנוכחי:
        -   `track += "_" `: הוספת סימן '_' למחרוזת המסלול.
    -   `print(track)`: הדפסת המסלול.
5.  **פונקציה `check_winner(horse_positions)`:**
    -  מקבלת רשימת מיקומי הסוסים ובודקת אם יש מנצח.
    -  `for i, pos in enumerate(horse_positions):`: מעבר על כל הסוסים ומיקומם.
    -  `if pos >= TRACK_LENGTH:`: בדיקה אם סוס הגיע לסוף המסלול.
    -  `return i`: החזרת מספר הסוס המנצח (אינדקס ברשימה).
    - `return None`: החזרת `None` אם אין מנצח עדיין.
6. **הפעלת המשחק:**
   - `if __name__ == "__main__":`: בדיקה אם הקובץ מורץ ישירות (לא מיובא כמודול).
   - `play_horses_game()`: הפעלת המשחק.
</הסברים:>