"""
<FURS>:
=================
קושי: 4
-----------------
המשחק "FURS" הוא משחק טקסט פשוט בו המחשב בוחר מילה בת ארבע אותיות, והשחקן צריך לנחש אותה. לאחר כל ניסיון, המחשב מודיע לשחקן כמה אותיות הוא ניחש במקום הנכון וכמה אותיות הוא ניחש בכלל.
המשחק נמשך עד שהשחקן מנחש את המילה.

חוקי המשחק:
1. המחשב בוחר מילה בת 4 אותיות.
2. השחקן מזין ניחוש של מילה בת 4 אותיות.
3. לאחר כל ניסיון, המחשב מחזיר שני מספרים:
    - הראשון מייצג את מספר האותיות שהשחקן ניחש במקום הנכון.
    - השני מייצג את מספר האותיות שהשחקן ניחש בכלל, גם אם לא במקום הנכון.
4. המשחק נמשך עד שהשחקן מנחש את המילה.
-----------------
אלגוריתם:
1. בחר מילה אקראית בת 4 אותיות.
2. אתחל את מספר הניסיונות ל-0.
3. התחל לולאה "כל עוד המילה לא נוחשה":
    3.1. הגדל את מספר הניסיונות ב-1.
    3.2. קלוט מהשחקן ניחוש בן 4 אותיות.
    3.3. אם הניחוש שווה למילה שנבחרה, עבור לשלב 4.
    3.4. חשב את מספר האותיות הנכונות במקום הנכון.
    3.5. חשב את מספר האותיות הנכונות בכלל.
    3.6. הצג את מספר האותיות הנכונות במקום הנכון ואת מספר האותיות הנכונות בכלל.
4. הצג הודעת ניצחון עם מספר הניסיונות.
5. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:<br><code><b>targetWord = random word (4 letters)</b></code><br><code><b>numberOfGuesses = 0</b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: כל עוד לא נוחש"}
    LoopStart -- כן --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputGuess["קלט מילה מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> CheckWin{"בדיקה: <code><b>userGuess == targetWord?</b></code>"}
    CheckWin -- כן --> OutputWin["הצגת הודעה: <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES!</b>"]
    OutputWin --> End["סוף"]
    CheckWin -- לא --> CalculateCorrectPlaces["<code><b>correctPlaces = calculateCorrectPlaces(userGuess, targetWord)</b></code>"]
    CalculateCorrectPlaces --> CalculateCorrectLetters["<code><b>correctLetters = calculateCorrectLetters(userGuess, targetWord)</b></code>"]
    CalculateCorrectLetters --> OutputClue["הצגת רמז: <b>correctPlaces</b> correct, <b>correctLetters</b> total"]
    OutputClue --> LoopStart
    LoopStart -- לא --> End
```
Legenda:
    Start - התחלת המשחק.
    InitializeVariables - אתחול משתנים: בחירת מילה אקראית בת 4 אותיות (targetWord) ואתחול מונה הניסיונות (numberOfGuesses) ל-0.
    LoopStart - תחילת לולאה, שממשיכה כל עוד המילה לא נוחשה.
    IncreaseGuesses - הגדלת מונה הניסיונות ב-1.
    InputGuess - קלט מילה בת 4 אותיות מהמשתמש ושמירתה במשתנה userGuess.
    CheckWin - בדיקה האם הניחוש שווה למילה הנבחרה.
    OutputWin - הצגת הודעת ניצחון, אם המילה נוחשה, עם מספר הניסיונות.
    End - סוף המשחק.
    CalculateCorrectPlaces - חישוב מספר האותיות שהשחקן ניחש במקום הנכון.
    CalculateCorrectLetters - חישוב מספר האותיות שהשחקן ניחש בכלל (גם אם לא במקום הנכון).
    OutputClue - הצגת רמז לשחקן: מספר האותיות הנכונות במקום הנכון ומספר האותיות הנכונות בכלל.
"""

```python
import random

def choose_random_word():
    """
    בוחר מילה אקראית באורך 4 אותיות מרשימת מילים.
    במקור המשחק משתמש בקלט מראש של מילים, לצורך הפשטה אנו משתמשים ברשימה קשיחה.
    """
    words = ["FURS", "CATS", "DOGS", "LION", "GAME", "CODE", "PLAY", "TEAM", "BALL", "BOOK"] #רשימת מילים
    return random.choice(words)

def calculate_correct_places(guess, target):
    """
    מקבלת את הניחוש ואת המילה המקורית, ומחזירה את מספר האותיות הנכונות במקום הנכון.
    """
    correct = 0
    for i in range(len(guess)):
        if guess[i] == target[i]:
            correct += 1
    return correct

def calculate_correct_letters(guess, target):
    """
    מקבלת את הניחוש ואת המילה המקורית, ומחזירה את מספר האותיות הנכונות בכלל (גם אם לא במקום הנכון).
    """
    correct = 0
    target_letters = list(target) # יוצר רשימה של האותיות במילה המקורית
    for letter in guess:
        if letter in target_letters: #בודק אם האות קיימת במילה המקורית
            correct += 1
            target_letters.remove(letter) #מוציא את האות מהרשימה על מנת לא לספור אותה שוב
    return correct

def play_furs_game():
    """
    מגדיר את לוגיקת המשחק FURS.
    """
    target_word = choose_random_word() #בחירת מילה אקראית
    number_of_guesses = 0 #אתחול מונה הניחושים

    while True: #לולאת משחק ראשית
        number_of_guesses += 1 #הגדלת מונה הניחושים
        user_guess = input("נחש מילה בת 4 אותיות: ").upper() #קבלת קלט מהמשתמש והפיכתו לאותיות גדולות

        if len(user_guess) != 4: #בדיקה אם הקלט הוא באורך 4 אותיות
            print("הניחוש חייב להיות מילה בת 4 אותיות!")
            continue #חזרה לתחילת הלולאה אם הקלט שגוי

        if user_guess == target_word: # בדיקת תנאי ניצחון
            print(f"מזל טוב! ניחשת את המילה ב-{number_of_guesses} ניסיונות!")
            break #סיום המשחק אם הניחוש נכון
        else: #אם הניחוש אינו נכון
            correct_places = calculate_correct_places(user_guess, target_word) #חישוב האותיות במקום
            correct_letters = calculate_correct_letters(user_guess, target_word) #חישוב האותיות הנכונות
            print(f"{correct_places} correct, {correct_letters} total") #הצגת רמז

if __name__ == "__main__":
    play_furs_game()
```
"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    - `import random`: ייבוא מודול זה מאפשר לבחור מילה אקראית מרשימת המילים.
2.  **פונקציה `choose_random_word()`**:
    -   `words = [...]`: רשימה של מילים מהן תבחר המילה האקראית.
    -   `return random.choice(words)`: בחירת מילה אקראית מתוך הרשימה והחזרתה.
3.  **פונקציה `calculate_correct_places(guess, target)`**:
    - מקבלת את הניחוש של השחקן (`guess`) ואת המילה המקורית (`target`).
    -   `correct = 0`: אתחול משתנה לספירת האותיות במקום הנכון.
    - לולאה על כל אות במילה:
        - בודקת אם האות בניחוש נמצאת באותו מיקום כמו האות במילה המקורית. אם כן, מגדילה את המונה `correct`.
    - החזרת מספר האותיות במקום הנכון.
4.  **פונקציה `calculate_correct_letters(guess, target)`**:
    - מקבלת את הניחוש של השחקן (`guess`) ואת המילה המקורית (`target`).
    -   `correct = 0`: אתחול משתנה לספירת האותיות הנכונות (לאו דווקא במקום הנכון).
    - `target_letters = list(target)`: המרת המילה המקורית לרשימה של אותיות, כדי שניתן יהיה להסיר אותיות שנספרו.
    - לולאה על כל אות בניחוש:
        - אם האות קיימת ברשימת האותיות של המילה המקורית:
            - הגדלת המונה `correct`.
            - הסרת האות מרשימת האותיות של המילה המקורית על מנת שלא תיספר שוב.
    - החזרת מספר האותיות הנכונות (גם אם לא במקום הנכון).
5.  **פונקציה `play_furs_game()`**:
    -  `target_word = choose_random_word()`: בחירת מילה אקראית באמצעות הפונקציה `choose_random_word`.
    -   `number_of_guesses = 0`: אתחול מונה מספר הניסיונות.
    -   `while True:`: לולאה אינסופית הממשיכה עד שהשחקן ינחש את המילה.
        - `number_of_guesses += 1`: הגדלת מונה מספר הניסיונות בכל סיבוב.
        -   `user_guess = input(...).upper()`: קבלת קלט מהמשתמש והמרתו לאותיות גדולות.
        -   `if len(user_guess) != 4`: בדיקה אם הניחוש הוא בן 4 אותיות, אם לא מודפסת הודעה והלולאה ממשיכה לניסיון הבא.
        -   `if user_guess == target_word`: בדיקה אם הניחוש שווה למילה המקורית, אם כן:
            -  הדפסת הודעת ניצחון עם מספר הניסיונות.
            -  `break`: יציאה מהלולאה (סיום המשחק).
        - אחרת:
            - `correct_places = calculate_correct_places(...)`: חישוב מספר האותיות הנכונות במקום הנכון באמצעות הפונקציה `calculate_correct_places`.
            - `correct_letters = calculate_correct_letters(...)`: חישוב מספר האותיות הנכונות בכלל באמצעות הפונקציה `calculate_correct_letters`.
            - הדפסת רמז: מספר האותיות הנכונות במקום ומספר האותיות הנכונות בכלל.
6.  **הפעלת המשחק**:
    - `if __name__ == "__main__":`: בלוק זה מוודא שהפונקציה `play_furs_game()` תופעל רק אם הסקריפט מורץ ישירות ולא כאשר הוא מיובא כמודול.
    - `play_furs_game()`: קריאה להפעלת המשחק.
"""
