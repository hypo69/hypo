<ACEDU>:
=================
קושי: 5
-----------------
המשחק ACEDU הוא משחק ניחושים בו השחקן צריך לנחש רצף של 4 ספרות, כאשר כל ספרה היא בין 1 ל-6. המשחק נותן רמזים על מספר הספרות שנמצאות במקום הנכון ("Aced") ועל מספר הספרות שנמצאות ברצף אבל במקום הלא נכון ("Dueces"). המשחק נמשך עד שהשחקן מנחש נכון את הרצף.

חוקי המשחק:
1. המחשב בוחר רצף של 4 ספרות אקראיות, כל ספרה בין 1 ל-6.
2. השחקן מזין רצף של 4 ספרות כניחוש.
3. המשחק מגיב בשני סוגי רמזים:
    * "Aced": מספר הספרות בניחוש שנמצאות במקום הנכון ברצף המקורי.
    * "Dueces": מספר הספרות בניחוש שנמצאות ברצף המקורי אך לא במקום הנכון.
4. המשחק נמשך עד שהשחקן מנחש את הרצף המדויק.
-----------------
אלגוריתם:
1. הגדר את משתנה `continue_game` כ-`True`.
2. צור רצף אקראי של 4 ספרות (בין 1 ל-6), ושמור במשתנה `target_sequence`.
3. התחל לולאה "כל עוד `continue_game` שווה ל-`True`":
   3.1 קבל קלט מהמשתמש, רצף של 4 ספרות.
   3.2 אתחל משתנים `aced` ו-`dueces` ל-0.
   3.3 עבור על כל הספרות ברצף של השחקן:
        3.3.1 אם הספרה במקום ה-i שווה לספרה ברצף המטרה באותו המקום, הגדל את `aced` ב-1.
   3.4 צור עותקים של רצף המטרה ורצף השחקן.
   3.5 עבור על כל הספרות בעותק של רצף השחקן:
       3.5.1 אם הספרה בעותק של רצף השחקן קיימת בעותק של רצף המטרה:
           3.5.1.1 הגדל את `dueces` ב-1.
           3.5.1.2 הסר את הספרה מרצף המטרה כדי שלא תיספר שוב.
   3.6 הדפס את מספר ה-"Aced" ואת מספר ה-"Dueces".
   3.7 אם `aced` שווה ל-4, הדפס הודעת ניצחון, והגדר את `continue_game` ל-`False`.
4. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeGame["<p align='left'>אתחול:
    <code><b>
    continueGame = True
    targetSequence = random([1-6], 4)
    </b></code></p>"]
    InitializeGame --> GameLoopStart{"תחילת לולאה: כל עוד continueGame"}
    GameLoopStart -- כן --> InputGuess["קלט מהמשתמש: userSequence (4 ספרות)"]
    InputGuess --> InitializeCounters["<p align='left'>אתחול מוני רמזים:
    <code><b>
        aced = 0
        dueces = 0
    </b></code></p>"]
    InitializeCounters --> CheckAced["לולאה: בדיקת ספרות במקום הנכון"]
    CheckAced -- עבור כל ספרה --> CheckAcedPos["בדיקה: userSequence[i] == targetSequence[i]?"]
    CheckAcedPos -- כן --> IncreaseAced["<code><b>aced = aced + 1</b></code>"]
    IncreaseAced --> EndAcedLoop["סוף לולאת בדיקת Aced"]
    CheckAcedPos -- לא --> EndAcedLoop
    EndAcedLoop --> CopySequences["<p align='left'>יצירת עותקים של רצפים:
    <code><b>
        tempTarget = copy(targetSequence)
        tempUser = copy(userSequence)
    </b></code></p>"]
    CopySequences --> CheckDueces["לולאה: בדיקת ספרות קיימות"]
    CheckDueces -- עבור כל ספרה --> CheckDuecesPos["בדיקה: tempUser[i] in tempTarget?"]
    CheckDuecesPos -- כן --> IncreaseDueces["<code><b>dueces = dueces + 1</b></code>"]
    IncreaseDueces --> RemoveDigit["הסרת ספרה מ-tempTarget"]
    RemoveDigit --> EndDuecesLoop["סוף לולאת בדיקת Dueces"]
    CheckDuecesPos -- לא --> EndDuecesLoop
    EndDuecesLoop --> OutputHints["הצגת רמזים: 'Aced:' {aced}, 'Dueces:' {dueces}"]
    OutputHints --> CheckWin{"בדיקה: aced == 4?"}
    CheckWin -- כן --> OutputWin["הצגת הודעה: 'You got it!'"]
    OutputWin --> EndGame["<code><b>continueGame = False</b></code>"]
    CheckWin -- לא --> GameLoopStart
    EndGame --> End["סוף"]
    GameLoopStart -- לא --> End
```

Legenda:
    Start - תחילת התוכנית.
    InitializeGame - אתחול משתנים: continueGame=True, ו-targetSequence רצף אקראי של 4 ספרות בין 1 ל-6.
    GameLoopStart - תחילת לולאה, הממשיכה כל עוד continueGame שווה ל-True.
    InputGuess - קבלת קלט מהמשתמש: רצף של 4 ספרות (userSequence).
    InitializeCounters - אתחול משתנים: aced = 0, ו-dueces = 0.
    CheckAced - לולאה שעוברת על כל הספרות, ובודקת את המיקום הנכון שלהן.
    CheckAcedPos - בדיקה: האם הספרה במקום ה-i ב-userSequence שווה לספרה ב-targetSequence באותו המקום?
    IncreaseAced - הגדלת מונה ה-aced ב-1.
    EndAcedLoop - סוף הלולאה לבדיקת aced.
    CopySequences - יצירת עותקים של הרצפים: tempTarget ו-tempUser.
    CheckDueces - לולאה שעוברת על הספרות, ובודקת אם קיימות ספרות נכונות במיקום לא נכון.
    CheckDuecesPos - בדיקה: האם הספרה הנוכחית ב-tempUser קיימת ב-tempTarget?
    IncreaseDueces - הגדלת מונה ה-dueces ב-1.
    RemoveDigit - הסרת הספרה מ-tempTarget.
    EndDuecesLoop - סוף הלולאה לבדיקת dueces.
    OutputHints - הצגת רמזים: "Aced" ו-"Dueces" למסך.
    CheckWin - בדיקה: האם aced שווה ל-4 (ניצחון).
    OutputWin - הצגת הודעה "You got it!".
    EndGame - עדכון continueGame ל-False.
    End - סוף התוכנית.
"""
import random

def play_acedu():
    # אתחול משתנה להמשך משחק
    continue_game = True
    # יצירת רצף מטרה אקראי של 4 ספרות (בין 1 ל-6)
    target_sequence = [random.randint(1, 6) for _ in range(4)]

    # לולאת המשחק הראשית
    while continue_game:
        # קבלת קלט מהמשתמש (ניחוש רצף של 4 ספרות)
        while True:
            try:
                user_input = input("הזן ניחוש של 4 ספרות (1-6): ")
                user_sequence = [int(digit) for digit in user_input]
                if len(user_sequence) == 4 and all(1 <= digit <= 6 for digit in user_sequence):
                    break
                else:
                   print("קלט לא תקין. אנא הזן רצף של 4 ספרות בין 1 ל-6.")
            except ValueError:
                print("קלט לא תקין. אנא הזן רק ספרות.")


        # אתחול מוני "Aced" ו-"Dueces"
        aced = 0
        dueces = 0

        # בדיקת מספר הספרות במקום הנכון ("Aced")
        for i in range(4):
           if user_sequence[i] == target_sequence[i]:
              aced += 1

        # יצירת עותקים של רצף המטרה ורצף השחקן
        temp_target = target_sequence[:]
        temp_user = user_sequence[:]
         
        # בדיקת מספר הספרות הנכונות שאינן במקום הנכון ("Dueces")
        for digit in temp_user:
          if digit in temp_target:
            dueces += 1
            temp_target.remove(digit)

        # הפחתת מספר "Aced" מ-"Dueces" כדי למנוע ספירה כפולה
        dueces -= aced

        # הצגת רמזים למשתמש
        print(f"Aced: {aced}, Dueces: {dueces}")

        # בדיקת ניצחון
        if aced == 4:
            print("You got it!")
            continue_game = False

if __name__ == "__main__":
    play_acedu()

"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    - `import random`: ייבוא המודול `random` המשמש ליצירת מספרים אקראיים.
2.  **פונקציה `play_acedu()`**:
    - פונקציה המכילה את לוגיקת המשחק ACEDU.
    - `continue_game = True`: אתחול משתנה בוליאני לקביעת המשך המשחק.
    - `target_sequence = [random.randint(1, 6) for _ in range(4)]`: יצירת רצף אקראי של 4 ספרות בין 1 ל-6, ושמירתו במשתנה `target_sequence`.
3.  **לולאת המשחק הראשית `while continue_game:`**:
    - לולאה הממשיכה כל עוד המשתנה `continue_game` הוא `True`.
    - **קלט נתונים**:
      - `while True:`: לולאה אינסופית לקבלת קלט תקין מהמשתמש.
      - `try...except ValueError`: טיפול בשגיאות קלט, אם המשתמש מזין משהו שאינו ספרות.
      - `user_input = input("הזן ניחוש של 4 ספרות (1-6): ")`: בקשת קלט מהמשתמש (רצף של 4 ספרות).
      - `user_sequence = [int(digit) for digit in user_input]`: המרת הקלט לרשימה של ספרות שלמות.
      - בדיקת תקינות הקלט: האם הקלט מכיל 4 ספרות בין 1 ל-6.
    - `aced = 0`: אתחול מונה הספרות במקום הנכון.
    - `dueces = 0`: אתחול מונה הספרות הנכונות, שאינן במקום הנכון.
    - **בדיקת "Aced"**:
      - `for i in range(4):`: לולאה על כל הספרות ברצף.
      - `if user_sequence[i] == target_sequence[i]:`: בדיקה אם הספרה במקום ה-i שווה לספרה ברצף המטרה באותו המקום.
      - `aced += 1`: הגדלת מונה ה-"Aced" ב-1.
    - **יצירת עותקים של רצף המטרה ורצף השחקן**:
      - `temp_target = target_sequence[:]`: יוצר עותק של הרצף המטרה.
      - `temp_user = user_sequence[:]`: יוצר עותק של הרצף מהמשתמש.
    - **בדיקת "Dueces"**:
      - `for digit in temp_user:`: לולאה שעוברת על כל הספרות בניחוש השחקן.
      - `if digit in temp_target:`: בדיקה האם הספרה הנוכחית קיימת ברצף המטרה.
        - `dueces += 1`: הגדלת מונה ה-"Dueces" ב-1.
        - `temp_target.remove(digit)`: הסרת הספרה מרשימת המטרה, כדי למנוע ספירה כפולה.
    - `dueces -= aced`: הפחתת מספר "Aced" מ-"Dueces" כדי למנוע ספירה כפולה.
    - `print(f"Aced: {aced}, Dueces: {dueces}")`: הצגת הרמזים למשתמש: מספר ה-"Aced" ומספר ה-"Dueces".
    - **בדיקת ניצחון**:
      - `if aced == 4:`: בדיקה האם כל הספרות נוחשו נכון ובמקום הנכון.
      - `print("You got it!")`: הצגת הודעה שהמשתמש ניצח.
      - `continue_game = False`: הפסקת המשחק.
4. **הפעלת המשחק**:
    - `if __name__ == "__main__":`: בלוק זה מבטיח שהפונקציה `play_acedu()` תופעל רק אם הקובץ מופעל ישירות, ולא אם הוא מיובא כמודול.
    - `play_acedu()`: קריאה לפונקציה להפעלת המשחק.
"""
