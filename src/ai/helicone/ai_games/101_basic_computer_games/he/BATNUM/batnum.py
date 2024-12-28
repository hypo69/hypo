"""
BATNUM: 5
=================
קושי: 4
-----------------
המשחק "בונקר" הוא משחק מילים פשוט בו המחשב בוחר מילה בת 5 אותיות, והשחקן צריך לנחש את המילה הזו. 
לאחר כל ניסיון, המחשב מספק רמזים: "A" עבור אות שהיא במקום הנכון, "B" עבור אות שהיא במילה, אבל לא במקום הנכון, ו-"-" עבור אות שלא נמצאת במילה כלל.

חוקי המשחק:
1. המחשב בוחר מילה אקראית בת 5 אותיות מתוך מאגר מילים.
2. השחקן מזין את ההשערות שלו לגבי המילה שנבחרה.
3. לאחר כל ניסיון, המחשב מספק רמזים: "A" עבור אות שהיא במקום הנכון, "B" עבור אות שהיא במילה, אבל לא במקום הנכון, ו-"-" עבור אות שלא נמצאת במילה כלל.
4. המשחק נמשך עד שהשחקן מנחש את המילה שנבחרה.

-----------------
אלגוריתם:
1. הגדר מילון המכיל מילים באורך 5 אותיות.
2. בחר מילה רנדומלית מהמילון.
3. כל עוד המילה לא נוחשה, בצע:
    3.1. קבל קלט מהשחקן (ניחוש).
    3.2. עבור כל אות במיקום:
        3.2.1. אם האות במקום הנכון, הצג "A".
        3.2.2. אם האות קיימת במילה, אבל לא במקום הנכון, הצג "B".
        3.2.3. אם האות לא קיימת במילה, הצג "-".
    3.3. הצג את הרמזים לשחקן.
    3.4. אם כל הרמזים הם "A", סימן שהמילה נוחשה, צא מהלולאה.
4. הצג הודעת ניצחון.
5. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeDictionary["<p align='left'>אתחול מילון מילים:
    <code><b>
    wordDictionary = ["words"]
    </b></code></p>"]
    InitializeDictionary --> ChooseTargetWord["בחירת מילה אקראית: <code><b>targetWord</b></code>"]
    ChooseTargetWord --> LoopStart{"תחילת לולאה: כל עוד המילה לא נוחשה"}
    LoopStart -- כן --> InputGuess["קבלת קלט מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> InitializeHints["אתחול רמזים: <code><b>hints = ""</b></code>"]
    InitializeHints --> LoopChars{"לולאה על כל אות ב-<code><b>userGuess</b></code>"}
    LoopChars -- כן --> CheckCharPosition["בדיקה: <code><b>userGuess[i] == targetWord[i]?</b></code>"]
    CheckCharPosition -- כן --> AppendHintA["הוספת רמז <b>'A'</b> ל-<code><b>hints</b></code>"]
    AppendHintA --> LoopChars
    CheckCharPosition -- לא --> CheckCharInWord{"בדיקה: האם <code><b>userGuess[i]</b></code> ב-<code><b>targetWord?</b></code>"}
    CheckCharInWord -- כן --> AppendHintB["הוספת רמז <b>'B'</b> ל-<code><b>hints</b></code>"]
    AppendHintB --> LoopChars
    CheckCharInWord -- לא --> AppendHintDash["הוספת רמז <b>'-'</b> ל-<code><b>hints</b></code>"]
    AppendHintDash --> LoopChars
    LoopChars -- לא --> OutputHints["הצגת רמזים: <code><b>hints</b></code>"]
    OutputHints --> CheckWinCondition{"בדיקה: האם <code><b>hints == 'AAAAA'?</b></code>"}
    CheckWinCondition -- כן --> OutputWin["הצגת הודעת ניצחון"]
    OutputWin --> End["סוף"]
    CheckWinCondition -- לא --> LoopStart
    LoopStart -- לא --> End
```
Legenda:
    Start - התחלת התוכנית.
    InitializeDictionary - אתחול מילון המילים.
    ChooseTargetWord - בחירת מילה אקראית מתוך המילון.
    LoopStart - תחילת הלולאה, הנמשכת כל עוד המילה לא נוחשה.
    InputGuess - קבלת קלט מהמשתמש (ניחוש המילה).
    InitializeHints - אתחול מחרוזת הרמזים.
    LoopChars - לולאה העוברת על כל אות במילה שהמשתמש ניחש.
    CheckCharPosition - בדיקה האם האות נמצאת במקום הנכון.
    AppendHintA - הוספת רמז 'A' למחרוזת הרמזים.
    CheckCharInWord - בדיקה האם האות קיימת במילה הנכונה, אך לא במקום הנכון.
    AppendHintB - הוספת רמז 'B' למחרוזת הרמזים.
    AppendHintDash - הוספת רמז '-' למחרוזת הרמזים (האות לא נמצאת במילה).
    OutputHints - הצגת הרמזים למשתמש.
    CheckWinCondition - בדיקה האם המשתמש ניחש את המילה בהצלחה.
    OutputWin - הצגת הודעת ניצחון.
    End - סוף התוכנית.
"""
import random

# מילון המכיל מילים באורך 5 אותיות
word_dictionary = ["codes", "games", "train", "hello", "world"]


def play_bunker_game():
    """
    משחק בונקר - ניחוש מילה באורך 5 אותיות.
    """
    # בחירת מילה אקראית מהמילון
    target_word = random.choice(word_dictionary)

    # לולאה ראשית של המשחק, ממשיכה עד שהמילה נוחשה
    while True:
        # קלט מהמשתמש: בקשה לנחש מילה
        user_guess = input("נחש מילה בת 5 אותיות: ").lower()

        # בדיקה שאורך המילה שהוזנה הוא 5 אותיות
        if len(user_guess) != 5:
            print("המילה חייבת להכיל 5 אותיות!")
            continue

        # אתחול הרמזים
        hints = ""

        # לולאה העוברת על כל אות במילה שהמשתמש ניחש
        for i in range(5):
            # אם האות במקום הנכון, הוסף 'A' לרמזים
            if user_guess[i] == target_word[i]:
                hints += "A"
            # אם האות קיימת במילה, אבל לא במקום הנכון, הוסף 'B' לרמזים
            elif user_guess[i] in target_word:
                hints += "B"
            # אם האות לא קיימת במילה, הוסף '-' לרמזים
            else:
                hints += "-"

        # הצגת הרמזים למשתמש
        print("רמזים:", hints)

        # אם כל הרמזים הם 'A', סימן שהמילה נוחשה, המשחק הסתיים
        if hints == "AAAAA":
            print("מזל טוב! ניחשת את המילה!")
            break


# הפעלת המשחק
if __name__ == "__main__":
    play_bunker_game()

"""
הסבר הקוד:

1. **ייבוא המודול `random`**:
   - `import random`: ייבוא המודול `random`, המשמש לבחירת מילה אקראית מהמילון.

2. **מילון מילים `word_dictionary`**:
   - `word_dictionary = ["codes", "games", "train", "hello", "world"]`: רשימה של מילים באורך 5 אותיות.

3. **פונקציה `play_bunker_game()`**:
   - מכילה את כל הלוגיקה של משחק "בונקר".
   - `target_word = random.choice(word_dictionary)`: בחירת מילה אקראית מהמילון ושמירתה במשתנה `target_word`.
   - **לולאה ראשית `while True:`**:
     - לולאה אינסופית שתימשך עד שהמשתמש ינחש את המילה.
     - `user_guess = input("נחש מילה בת 5 אותיות: ").lower()`: קבלת קלט מהמשתמש והמרת האותיות לאותיות קטנות.
     - `if len(user_guess) != 5:`: בדיקה שאורך המילה שהמשתמש הזין הוא 5 אותיות, אחרת הודעת שגיאה והמשך הלולאה.
     - `hints = ""`: אתחול משתנה `hints` שהוא מחרוזת ריקה, שתכיל את הרמזים.
     - **לולאה על אותיות המילה `for i in range(5):`**:
       - `if user_guess[i] == target_word[i]:`: בדיקה האם האות במקום הנכון.
         - `hints += "A"`: הוספת רמז 'A' אם האות במקום הנכון.
       - `elif user_guess[i] in target_word:`: בדיקה האם האות קיימת במילה הנכונה, אך לא במקום הנכון.
         - `hints += "B"`: הוספת רמז 'B' אם האות קיימת במילה, אך לא במקום הנכון.
       - `else:`: אם האות לא נמצאת במילה כלל.
         - `hints += "-"`: הוספת רמז '-' אם האות לא קיימת במילה.
     - `print("רמזים:", hints)`: הצגת הרמזים למשתמש.
     - `if hints == "AAAAA":`: בדיקה אם המשתמש ניחש את המילה בהצלחה.
       - `print("מזל טוב! ניחשת את המילה!")`: הצגת הודעת ניצחון.
       - `break`: סיום הלולאה הראשית (והמשחק) אם המילה נוחשה.

4. **הפעלת המשחק**:
   - `if __name__ == "__main__":`: בלוק שמוודא שהפונקציה `play_bunker_game()` תופעל רק כאשר הקובץ מופעל ישירות, ולא כשהוא מיובא כמודול.
   - `play_bunker_game()`: קריאה לפונקציה להפעלת המשחק.
"""
